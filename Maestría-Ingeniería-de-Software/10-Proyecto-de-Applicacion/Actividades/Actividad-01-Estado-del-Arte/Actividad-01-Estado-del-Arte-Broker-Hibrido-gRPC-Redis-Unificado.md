# Estado del arte: broker de mensajeria hibrido basado en gRPC y Redis Streams

## 1. Introduccion

Las arquitecturas de software actuales se apoyan de forma creciente en sistemas distribuidos, microservicios y comunicacion orientada a eventos. En este tipo de soluciones, una aplicacion deja de concentrar toda la logica de negocio en un unico bloque y pasa a organizarse como un conjunto de servicios independientes que necesitan intercambiar informacion de manera confiable, eficiente y observable. Este cambio facilita la escalabilidad y la evolucion independiente de los componentes, pero tambien introduce problemas tecnicos relevantes: latencia de red, duplicacion de mensajes, coordinacion de consumidores, confirmacion de procesamiento, tolerancia a fallos y mantenimiento de contratos entre servicios (Akamai, 2024; Fowler & Lewis, 2014; Hohpe & Woolf, 2003).

En este contexto, los brokers de mensajeria y las plataformas de streaming se han convertido en piezas centrales de muchas arquitecturas modernas. Apache Kafka, RabbitMQ, Apache Pulsar, NATS JetStream, Google Cloud Pub/Sub y Redis Streams ofrecen mecanismos para publicar, enrutar, almacenar y consumir mensajes bajo distintos modelos de entrega y operacion (Apache Kafka, s. f.-a; Apache Pulsar, s. f.; Google Cloud, s. f.; NATS, s. f.-a; RabbitMQ, s. f.-a; Redis Inc., s. f.-a). Sin embargo, ninguna alternativa debe evaluarse como solucion universal: Kafka y Pulsar destacan en streaming distribuido y retencion de eventos; RabbitMQ en enrutamiento y colas tradicionales; NATS JetStream en baja latencia y consumidores ligeros; Pub/Sub en operacion gestionada; y Redis Streams en simplicidad operativa para flujos persistentes y grupos de consumidores.

El desarrollo practico propuesto consiste en el diseno e implementacion de un broker de mensajeria hibrido para sistemas distribuidos, basado en gRPC, Protocol Buffers y Redis Streams. La propuesta busca combinar comunicacion en tiempo real mediante streaming gRPC con mensajeria asincrona basada en almacenamiento temporal, consumo pull y confirmacion explicita de procesamiento. Ademas, incorpora control de idempotencia, un SDK cliente, observabilidad basica y una arquitectura desacoplada inspirada en puertos y adaptadores.

La finalidad de este estado del arte es justificar tecnicamente el proyecto, comparar las tecnologias relacionadas y delimitar su aportacion. La propuesta no pretende reemplazar plataformas industriales consolidadas, sino construir un prototipo academico funcional que permita estudiar de forma integrada los compromisos entre baja latencia, desacoplamiento, persistencia temporal, idempotencia, mantenibilidad y observabilidad.

## 2. Descripcion del desarrollo practico

Se propone desarrollar un broker de mensajeria hibrido que permita a servicios distribuidos intercambiar eventos mediante dos modalidades complementarias. La primera modalidad sera sincronica o cercana al tiempo real, apoyada en gRPC y sus capacidades de streaming sobre HTTP/2. La segunda modalidad sera asincrona, basada en Redis Streams como almacenamiento temporal, con recuperacion de mensajes bajo demanda mediante consumo pull.

El broker actuara como intermediario entre productores y consumidores. Los productores publicaran mensajes hacia un canal, tema o flujo logico. Los consumidores podran recibir eventos en tiempo real mediante una conexion gRPC persistente, o bien solicitar mensajes pendientes cuando tengan capacidad de procesamiento. Esta combinacion permite atender escenarios diferentes dentro de una misma propuesta: comunicacion inmediata cuando se requiere baja latencia, y procesamiento desacoplado cuando se necesita tolerar desconexiones, controlar carga o reprocesar mensajes no confirmados.

La seleccion de gRPC se justifica por su soporte nativo para llamadas unarias, streaming de cliente, streaming de servidor y streaming bidireccional (gRPC Authors, s. f.-a). Protocol Buffers aportara contratos formales e independientes del lenguaje, lo que reduce ambiguedades entre el broker, el SDK y los servicios cliente (Protocol Buffers, s. f.). Redis Streams se utilizara como mecanismo de cola ligera porque ofrece un log append-only, consumer groups, lectura mediante `XREADGROUP` y confirmacion mediante `XACK` (Redis Inc., s. f.-a; Redis Inc., s. f.-b; Redis Inc., s. f.-c).

El alcance de la primera version sera academico y experimental. No se promete reemplazar Kafka, RabbitMQ, Pulsar o NATS JetStream, ni ofrecer exactamente-once extremo a extremo en cualquier condicion distribuida. La aportacion se ubica en el diseno, implementacion y evaluacion de una arquitectura hibrida que combine streaming gRPC, mensajeria asincrona, consumo pull, idempotencia, SDK cliente y separacion arquitectonica.

## 3. Caracteristicas previstas del sistema

El broker propuesto tendra una lista cerrada de capacidades funcionales y no funcionales:

- Publicacion de mensajes desde multiples productores.
- Suscripcion de consumidores a flujos de eventos en tiempo real.
- Comunicacion mediante gRPC con soporte para streaming de servidor y streaming bidireccional.
- Contratos de comunicacion definidos con Protocol Buffers.
- Almacenamiento temporal de mensajes asincronos en Redis Streams.
- Consumo pull para que los consumidores soliciten mensajes cuando esten listos.
- Confirmacion explicita de procesamiento mediante acknowledgement.
- Control de duplicados mediante claves de idempotencia y, cuando aplique, primitivas de idempotencia disponibles en Redis Streams.
- Soporte de patrones fan-out para distribuir un evento a varios consumidores.
- Soporte acotado de fan-in para consolidar respuestas o eventos desde varios productores.
- SDK cliente para simplificar publicacion, consumo, ack e idempotencia.
- Observabilidad basica mediante logs estructurados, metricas, trazas y endpoints de salud.
- Arquitectura desacoplada basada en puertos y adaptadores para facilitar pruebas y reemplazo de infraestructura.
- Entorno reproducible de pruebas e integracion mediante contenedores e infraestructura como codigo.

Estas caracteristicas delimitan el alcance inicial. Aspectos como orden global entre todos los mensajes, tolerancia a fallos multi-region, retencion historica prolongada, particionado distribuido complejo o garantias exactly-once completas quedan fuera de la primera version y se consideran lineas de mejora o criterios de evaluacion futura.

## 4. Estado del arte

### 4.1 Arquitecturas distribuidas y comunicacion orientada a eventos

Las arquitecturas de microservicios favorecen la division de un sistema en servicios pequenos, autonomos y desplegables de forma independiente. Fowler y Lewis (2014) senalan que este estilo mejora la autonomia y la evolutividad, pero desplaza parte de la complejidad hacia la comunicacion, la operacion y la consistencia entre servicios. Cuando un sistema se distribuye, la red deja de ser un detalle tecnico y se convierte en una fuente permanente de latencia, fallos parciales y duplicados.

La arquitectura orientada a eventos responde a esta complejidad mediante la emision y consumo de eventos entre componentes desacoplados. Hohpe y Woolf (2003) sistematizan estos problemas mediante patrones como Message Channel, Message Broker, Publish-Subscribe Channel, Message Router y Competing Consumers. Estos patrones siguen siendo relevantes porque permiten describir de forma precisa como se conectan productores, intermediarios y consumidores sin acoplar directamente sus implementaciones.

La literatura reciente coincide en que la seleccion de un broker no debe reducirse al rendimiento bruto. Dimitrova et al. (2025) explican que los patrones de arquitectura orientada a eventos dependen de factores tecnicos y organizativos, como consistencia, madurez del equipo, complejidad operativa y modelo de entrega requerido. Arafat et al. (2025) tambien advierten que los benchmarks de plataformas de mensajeria pueden variar de forma significativa segun la carga, el tamano de mensajes, el patron de consumo y la configuracion experimental. Por tanto, el proyecto propuesto no parte de la premisa de que existe un broker "mejor" en terminos absolutos, sino de que hay un espacio academico para estudiar una integracion hibrida, controlada y medible.

### 4.2 gRPC y Protocol Buffers como base de comunicacion

gRPC es un framework de comunicacion remota orientado a servicios que utiliza HTTP/2 y Protocol Buffers. Su documentacion oficial describe cuatro modalidades principales: llamadas unarias, streaming de cliente, streaming de servidor y streaming bidireccional (gRPC Authors, s. f.-a). Ademas, sus guias de rendimiento recomiendan reutilizar canales y aprovechar la multiplexacion de HTTP/2 en escenarios de llamadas frecuentes entre servicios (gRPC Authors, s. f.-b). Esta variedad lo diferencia de REST sobre HTTP/JSON, cuyo modelo mas habitual es una solicitud seguida de una respuesta. Para un broker hibrido, gRPC resulta especialmente util porque permite modelar operaciones tipo cola con llamadas unarias y comunicacion en tiempo real con streams persistentes.

Protocol Buffers complementa a gRPC como mecanismo de definicion y serializacion de datos estructurados. En el proyecto, su funcion principal sera establecer contratos formales entre broker, SDK y clientes. Esta decision reduce ambiguedades de integracion, facilita la generacion de clientes y permite evolucionar los mensajes con mayor control que en esquemas informales basados solo en JSON (Protocol Buffers, s. f.).

Los estudios comparativos recientes respaldan el uso de gRPC en comunicacion interna entre microservicios, aunque con matices. Niswar et al. (2024) comparan REST, GraphQL y gRPC en escenarios de microservicios y reportan menores tiempos de respuesta para gRPC bajo varias condiciones de concurrencia, mientras REST muestra ventajas en simplicidad y consumo moderado de recursos. Sousa et al. (2025) tambien concluyen que gRPC se beneficia de Protobuf, HTTP/2 y un modelo no bloqueante, pero senalan que REST puede seguir siendo competitivo en cargas muy altas con mensajes pequenos y sin necesidad de streaming. Liu et al. (2023) analizan tecnologias RPC de alto rendimiento y refuerzan la idea de que la comunicacion entre microservicios requiere mecanismos eficientes y observables.

La conclusion para este proyecto es que gRPC no debe presentarse como sustituto universal de REST o GraphQL. Microsoft (s. f.) tambien plantea esta distincion al comparar gRPC con APIs HTTP: gRPC ofrece ventajas en contratos, rendimiento y streaming, mientras que HTTP/JSON conserva ventajas de compatibilidad y facilidad de uso. Su valor concreto esta en comunicacion servicio-a-servicio, contratos estrictos y streaming nativo. REST puede ser mas conveniente para interfaces publicas, consumo web directo o depuracion manual, y GraphQL puede aportar flexibilidad de consulta en APIs orientadas a cliente. En cambio, el broker propuesto necesita streams persistentes, baja latencia y contratos compartidos; por ello, gRPC es una eleccion coherente para el canal principal.

### 4.3 Brokers de mensajeria y plataformas existentes

Apache Kafka es una de las plataformas mas representativas para streaming de eventos. Su arquitectura basada en topics, particiones, productores y consumidores permite alto rendimiento, retencion de eventos y procesamiento distribuido (Apache Kafka, s. f.-a). Kafka Streams tambien incorpora conceptos avanzados como procesamiento con garantias exactly-once en escenarios especificos (Apache Kafka, s. f.-b). Esta fortaleza, sin embargo, viene acompanada de mayor complejidad operativa, especialmente cuando se requiere administrar clusters, particiones, retencion, replicacion y ecosistema de conectores.

RabbitMQ representa una aproximacion distinta. Como broker AMQP, destaca por exchanges, colas, claves de enrutamiento, acknowledgements y publisher confirms (RabbitMQ, s. f.-a; RabbitMQ, s. f.-b). Su modelo es adecuado para colas de trabajo, enrutamiento flexible y patrones de mensajeria empresarial. Frente al proyecto propuesto, RabbitMQ tiene mayor madurez como broker general, pero no esta centrado en exponer una API gRPC ni en demostrar la integracion experimental entre streaming gRPC y Redis Streams.

Apache Pulsar combina pub/sub, topics, subscriptions, acknowledgements y una arquitectura distribuida separada entre computo y almacenamiento (Apache Pulsar, s. f.). Pulsar ofrece capacidades avanzadas como distintos tipos de suscripcion, redelivery y persistencia. No obstante, su arquitectura tambien resulta mas compleja que la necesaria para un prototipo academico cuyo objetivo es estudiar los compromisos internos de un broker hibrido.

NATS JetStream es una alternativa relevante para baja latencia, streams persistentes y consumidores push o pull. Su documentacion destaca que JetStream incorpora consumidores con seguimiento de entregas y acknowledgements, y que los consumidores pull permiten procesar mensajes bajo demanda (NATS, s. f.-a; NATS, s. f.-b). Esta aproximacion se acerca mucho a la idea de consumo controlado que se busca en el proyecto. La diferencia es que el TFM no pretende adoptar NATS directamente, sino implementar una solucion propia para aprender, evaluar y justificar las decisiones arquitectonicas.

Google Cloud Pub/Sub ofrece mensajeria gestionada con suscripciones push y pull (Google Cloud, s. f.). Su ventaja principal es reducir la carga operativa del equipo. Su limitacion para este trabajo es que oculta gran parte de la implementacion interna, lo cual reduce el valor academico si el objetivo es construir y evaluar el broker como desarrollo practico.

Esta revision muestra que la brecha del proyecto no es la inexistencia de brokers. La brecha esta en disenar, implementar y evaluar una integracion acotada que combine gRPC streaming, Protobuf, Redis Streams, consumo pull, idempotencia, SDK y arquitectura hexagonal dentro de un prototipo comprensible y medible.

### 4.4 Redis Streams como almacenamiento temporal y cola ligera

Redis Streams es una estructura de datos orientada a flujos de mensajes. A diferencia de Redis Pub/Sub, donde los mensajes no quedan retenidos para consumidores desconectados, Streams permite mantener un log append-only, leer rangos, trabajar con grupos de consumidores y confirmar mensajes procesados (Redis Inc., s. f.-a). Para el broker propuesto, esta capacidad permite implementar una cola temporal sin introducir una plataforma de streaming completa.

Las operaciones principales son `XADD` para agregar mensajes, `XREADGROUP` para leer desde un grupo de consumidores y `XACK` para confirmar procesamiento (Redis Inc., s. f.-a; Redis Inc., s. f.-b; Redis Inc., s. f.-c). El modelo encaja con una API productor-consumidor-ack: el productor publica, el broker persiste temporalmente, el consumidor solicita mensajes cuando tiene capacidad y el ack confirma que puede retirarse de la lista pendiente.

Redis tambien ha incorporado mecanismos especificos de idempotencia para Streams. La documentacion actual de Redis indica que, desde Redis 8.6, Streams soporta procesamiento idempotente de mensajes para evitar entradas duplicadas cuando un productor reintenta una escritura despues de fallos de red o reinicios (Redis Inc., 2026a; Redis Inc., 2026b). Esta capacidad es relevante, pero no debe confundirse con exactamente-once extremo a extremo: ayuda a reducir duplicados en la produccion del mensaje, mientras que los consumidores tambien deben ser disenados de forma idempotente para evitar efectos secundarios durante reentregas.

La ventaja principal de Redis Streams para este TFM es la simplicidad operativa. Redis es facil de ejecutar localmente, se integra bien con contenedores y permite demostrar conceptos centrales de mensajeria: cola, consumer groups, ack, mensajes pendientes e idempotencia. Su limitacion esta en que la durabilidad, replicacion, tolerancia a fallos y escalabilidad dependen de la configuracion de Redis y no equivalen automaticamente a plataformas especializadas como Kafka o Pulsar. Por ello, Redis Streams es adecuado para un prototipo academico y para escenarios de mensajeria ligera, pero no debe presentarse como reemplazo universal de brokers industriales.

### 4.5 Modelos push, pull, ack e idempotencia

Un broker de mensajeria no solo transporta datos: tambien define como se entregan los mensajes, como se confirma el procesamiento y que ocurre cuando hay errores. En un modelo push, el broker envia mensajes hacia consumidores conectados. En un modelo pull, el consumidor solicita trabajo cuando tiene capacidad. JetStream documenta ambos enfoques y senala que los consumidores pull son utiles cuando la aplicacion necesita controlar el ritmo de procesamiento (NATS, s. f.-b).

El broker propuesto adopta ambos modelos. La comunicacion en tiempo real se aproxima a un modelo push mediante streaming gRPC: los consumidores conectados reciben eventos conforme son publicados. La mensajeria asincrona se aproxima a un modelo pull: los consumidores solicitan mensajes desde Redis Streams cuando estan listos para procesarlos. Esta combinacion permite cubrir dos necesidades complementarias sin forzar una sola semantica para todos los casos de uso.

El acknowledgement es indispensable para evitar que el broker considere completado un mensaje antes de tiempo. RabbitMQ y Pulsar utilizan confirmaciones para marcar mensajes como procesados o para habilitar reentregas (Apache Pulsar, s. f.; RabbitMQ, s. f.-b). Redis Streams ofrece una primitiva equivalente con `XACK` (Redis Inc., s. f.-c). En este proyecto, el ack sera una operacion explicita del consumidor, lo que permite distinguir entre entrega, procesamiento y confirmacion.

La idempotencia aborda el problema de los duplicados. En sistemas distribuidos, un productor puede publicar un mensaje, sufrir un timeout y reintentar sin saber si la operacion anterior se completo. Un consumidor tambien puede fallar despues de ejecutar parte de su logica y antes de confirmar el mensaje. Por ello, el diseno debe asociar claves unicas a operaciones relevantes y registrar temporalmente si ya fueron procesadas. El proyecto contemplara idempotency keys con TTL y, cuando sea posible, las primitivas de Redis Streams disponibles para produccion idempotente (Redis Inc., 2026b). Esta decision reduce el riesgo de reprocesamiento, aunque no elimina la necesidad de consumidores idempotentes ni equivale por si sola a exactly-once distribuido.

### 4.6 Patrones fan-out y fan-in

Fan-out y fan-in son patrones frecuentes en sistemas concurrentes y distribuidos. Fan-out consiste en distribuir un evento o unidad de trabajo hacia multiples destinos. Fan-in consiste en consolidar respuestas, resultados o flujos desde varias fuentes. Estos patrones aparecen en integracion empresarial, procesamiento paralelo y arquitectura orientada a eventos (Hohpe & Woolf, 2003).

En el broker propuesto, fan-out se manifiesta cuando un productor publica un evento que debe llegar a varios consumidores. El broker centraliza la distribucion y evita que el productor tenga que gestionar conexiones individuales con cada receptor. Este patron es util para notificaciones internas, propagacion de eventos de dominio, actualizacion de caches o activacion de procesos secundarios.

Fan-in aparece cuando multiples productores o consumidores generan respuestas que deben consolidarse hacia un origen o flujo comun. Este caso es mas complejo porque implica concurrencia, orden de llegada, cierres de stream, errores parciales y posibles timeouts. Por ello, el soporte de fan-in debe plantearse de forma acotada en la primera version, evitando prometer coordinacion distribuida completa.

La incorporacion de fan-out y fan-in no busca competir con el routing avanzado de RabbitMQ ni con el particionado de Kafka. Su objetivo es demostrar patrones representativos de mensajeria dentro de una arquitectura propia, con reglas de alcance claras y pruebas que validen los casos principales.

### 4.7 Arquitectura hexagonal y arquitectura limpia

La arquitectura hexagonal, tambien conocida como puertos y adaptadores, fue propuesta por Cockburn (2005) para aislar la logica de aplicacion de detalles externos como interfaces, bases de datos o servicios de infraestructura. Cockburn y Garrido de Paz (2024) han reforzado esta vision como un patron orientado a que la aplicacion pueda ser usada, probada y conectada desde distintos adaptadores sin depender de ellos en su nucleo.

La arquitectura limpia de Martin (2017) comparte una preocupacion similar: las dependencias deben apuntar hacia las reglas de negocio y no hacia detalles externos. Graça (2017) explica que los puertos funcionan como entradas y salidas neutrales para la aplicacion, mientras los adaptadores conectan esos puertos con tecnologias concretas. En el caso del broker, esta separacion permite que la logica de publicacion, distribucion, ack e idempotencia no dependa directamente de gRPC, Redis, Prometheus o Docker.

Esta decision arquitectonica se justifica porque el proyecto integra tecnologias heterogeneas. Si la logica principal estuviera mezclada con clientes Redis, handlers gRPC y detalles de observabilidad, las pruebas serian mas fragiles y el reemplazo tecnologico mas costoso. Con puertos y adaptadores, el broker puede probar sus casos de uso con mocks o implementaciones en memoria, y despues conectar adaptadores reales para gRPC, Redis Streams y metricas.

El riesgo es introducir sobreingenieria. La arquitectura debe mantenerse al servicio de la claridad: separar dominio, casos de uso, puertos y adaptadores solo cuando esa separacion facilite pruebas, mantenimiento y evolucion. En un broker hibrido con streaming, cola, idempotencia y observabilidad, la separacion se considera razonable porque el sistema no es un CRUD simple ni una integracion lineal.

### 4.8 Observabilidad, pruebas e infraestructura reproducible

Los sistemas distribuidos requieren observabilidad porque los errores no siempre son visibles desde un unico componente. Un mensaje puede quedar pendiente, un consumidor puede desconectarse, un stream puede cerrarse, Redis puede responder lentamente o un productor puede reintentar operaciones. OpenTelemetry define senales como trazas, metricas y logs para observar sistemas distribuidos (OpenTelemetry, s. f.). Prometheus, por su parte, recopila metricas como series temporales y permite analizar comportamiento operativo (Prometheus, s. f.).

El broker propuesto incorporara logs estructurados, metricas de publicacion y consumo, latencia de operaciones, conteo de errores, mensajes pendientes y endpoints de salud. Estas senales no solo son utiles para operar el sistema, sino tambien para evaluar el TFM: permiten medir latencia, throughput, tasa de reintentos, duplicados evitados y comportamiento bajo consumidores lentos.

Docker facilita empaquetar y ejecutar servicios en contenedores reproducibles (Docker, s. f.). Terraform permite describir infraestructura como codigo y mantener entornos repetibles (HashiCorp, s. f.). Para este proyecto, estas herramientas ayudan a levantar broker, Redis, Prometheus y Grafana de forma controlada. Aunque Docker Compose podria bastar para un entorno local, Terraform aporta formalidad y conecta el desarrollo con practicas de infraestructura como codigo.

## 5. Analisis comparativo

La siguiente tabla sintetiza la posicion de las tecnologias revisadas frente a las dimensiones mas relevantes del proyecto.

| Dimension | gRPC | REST/HTTP | Redis Streams | Kafka/Pulsar | NATS JetStream |
|---|---|---|---|---|---|
| Uso principal | Comunicacion servicio-a-servicio | APIs generales y web | Cola/stream ligero | Streaming distribuido | Mensajeria ligera y streams |
| Contrato | Protobuf tipado | JSON/OpenAPI opcional | Estructura de mensajes | Esquemas opcionales | Mensajes por subjects |
| Streaming nativo | Si | Limitado | Lectura de streams | Si | Si |
| Modelo pull | Por API propia | Por API propia | `XREADGROUP` | Consumidores | Consumidores pull |
| Ack | Por diseno de API | Por diseno de API | `XACK` | Offsets/acks segun plataforma | Ack de consumidores |
| Idempotencia | Debe implementarse | Debe implementarse | Soporte reciente y patrones con claves | Transacciones/idempotencia en escenarios concretos | Requiere diseno de consumidor |
| Complejidad operativa | Media | Baja | Baja-media | Media-alta | Media |
| Papel en el proyecto | Canal principal | Alternativa no principal | Persistencia temporal | Referencia comparativa | Referencia comparativa |

El analisis muestra que las tecnologias existentes resuelven partes del problema, pero con enfoques diferentes. Kafka y Pulsar son fuertes para streaming distribuido y retencion; RabbitMQ para colas y enrutamiento; NATS JetStream para mensajeria ligera con persistencia; Redis Streams para colas simples con consumer groups; y gRPC para comunicacion eficiente y tipada entre servicios. La aportacion del proyecto consiste en integrar un subconjunto de estas capacidades en un prototipo propio, con alcance claro y evaluacion experimental.

## 6. Brecha identificada y aportacion del proyecto

La brecha no consiste en afirmar que no existen brokers de mensajeria. Esa afirmacion seria tecnicamente incorrecta. La brecha se encuentra en la integracion academica y controlada de varios conceptos dentro de una solucion propia: gRPC streaming, contratos Protobuf, Redis Streams, consumo pull, acknowledgement, idempotencia, SDK cliente, observabilidad y arquitectura hexagonal.

Las plataformas existentes pueden resolver muchos casos de produccion con mayor madurez que el prototipo propuesto. Sin embargo, adoptarlas directamente no permitiria estudiar con el mismo nivel de detalle como se construyen internamente las decisiones de entrega, confirmacion, deduplicacion y desacoplamiento. Por ello, el valor del proyecto es formativo y experimental: construir un broker hibrido medible que permita comparar modos de comunicacion, validar patrones y documentar limites.

La aportacion concreta sera una arquitectura funcional que permita:

- Integrar comunicacion en tiempo real y mensajeria asincrona en una misma propuesta.
- Reducir acoplamiento entre productores y consumidores mediante un intermediario tipado.
- Controlar el ritmo de consumo con un modelo pull respaldado por Redis Streams.
- Mitigar duplicados mediante idempotency keys y consumidores idempotentes.
- Evaluar latencia, throughput, errores, mensajes pendientes y comportamiento bajo carga.
- Probar la mantenibilidad de una arquitectura basada en puertos y adaptadores.

## 7. Conclusiones del estado del arte

El estado del arte evidencia que la comunicacion entre servicios es un problema central en arquitecturas distribuidas. Los microservicios y los sistemas orientados a eventos requieren mecanismos para desacoplar productores y consumidores, controlar entregas, confirmar procesamiento, evitar duplicados y observar el comportamiento de la plataforma. Los patrones de integracion empresarial proporcionan el vocabulario conceptual, mientras que las plataformas modernas de mensajeria ofrecen soluciones especializadas segun el tipo de carga, durabilidad y modelo de consumo.

gRPC y Protocol Buffers resultan adecuados para la capa de comunicacion en tiempo real porque permiten contratos formales, serializacion eficiente y streaming nativo. La literatura revisada muestra ventajas de gRPC frente a REST y GraphQL en varios escenarios de microservicios, aunque tambien deja claro que gRPC no es siempre la mejor opcion. Su uso se justifica en este proyecto porque el canal principal es servicio-a-servicio y requiere streaming, no porque REST sea tecnicamente inferior en todos los contextos.

Redis Streams resulta adecuado para la parte asincrona del prototipo porque ofrece consumer groups, lectura pull y acknowledgement con una complejidad operativa moderada. Frente a Kafka, Pulsar o NATS JetStream, Redis no ofrece automaticamente el mismo nivel de plataforma distribuida, pero su simplicidad facilita la implementacion academica y la validacion experimental. La decision es coherente siempre que se reconozcan sus limites de durabilidad, escalabilidad y garantias de entrega.

La idempotencia aparece como una preocupacion critica. En un sistema distribuido, los reintentos pueden generar duplicados y los consumidores pueden fallar antes de confirmar procesamiento. Incluir idempotency keys y disenar consumidores idempotentes permite reducir este riesgo. No obstante, la propuesta debe evitar prometer exactamente-once absoluto: incluso con soporte reciente de Redis Streams para produccion idempotente, la garantia extremo a extremo depende de la logica de negocio, la atomicidad de las operaciones y el manejo de fallos.

La arquitectura hexagonal o de puertos y adaptadores se justifica porque el proyecto integra tecnologias externas diversas: gRPC, Redis, observabilidad e infraestructura reproducible. Separar nucleo, casos de uso y adaptadores facilita pruebas, evolucion y reemplazo tecnologico. Esta separacion debe aplicarse con moderacion, pero en este caso aporta claridad porque el broker combina varios mecanismos de comunicacion y persistencia.

En conclusion, el desarrollo propuesto es pertinente como TFM porque permite estudiar y demostrar la integracion de comunicacion en tiempo real, mensajeria asincrona, consumo pull, idempotencia y observabilidad en un broker hibrido. Su valor no esta en competir con soluciones industriales consolidadas, sino en construir un prototipo defendible, medible y academicamente riguroso que permita comprender los compromisos de diseno presentes en los sistemas distribuidos modernos.

## Referencias

Akamai. (2024). *What is an event-driven microservices architecture?* Recuperado el 8 de junio de 2026, de https://www.akamai.com/blog/edge/what-is-an-event-driven-microservices-architecture

Apache Kafka. (s. f.-a). *Apache Kafka documentation*. Recuperado el 8 de junio de 2026, de https://kafka.apache.org/documentation/

Apache Kafka. (s. f.-b). *Kafka Streams core concepts*. Recuperado el 8 de junio de 2026, de https://kafka.apache.org/documentation/streams/core-concepts

Apache Pulsar. (s. f.). *Messaging concepts*. Recuperado el 8 de junio de 2026, de https://pulsar.apache.org/docs/next/concepts-messaging/

Arafat, J., Tasmin, F., Poudel, S., & Tareq, A. H. (2025). *Next-generation event-driven architectures: Performance, scalability, and intelligent orchestration across messaging frameworks*. arXiv. https://arxiv.org/abs/2510.04404

Cockburn, A. (2005). *Hexagonal architecture*. Recuperado el 8 de junio de 2026, de https://alistair.cockburn.us/hexagonal-architecture/

Cockburn, A., & Garrido de Paz, J. M. (2024). *Hexagonal architecture explained*. Leanpub.

Dimitrova, I., et al. (2025). A review of event-driven architecture patterns using message brokers in .NET. *International Journal of Computer*, 14(9), 2519-2543. https://ijcjournal.org/InternationalJournalOfComputer/article/view/2456

Docker. (s. f.). *Docker overview*. Recuperado el 8 de junio de 2026, de https://docs.docker.com/engine/docker-overview/

Fowler, M., & Lewis, J. (2014). *Microservices: A definition of this new architectural term*. Recuperado el 8 de junio de 2026, de https://martinfowler.com/articles/microservices.html

Google Cloud. (s. f.). *What is Pub/Sub?* Recuperado el 8 de junio de 2026, de https://cloud.google.com/pubsub/docs/overview

Graça, H. (2017). *Ports & adapters architecture*. The Software Architecture Chronicles. Recuperado el 8 de junio de 2026, de https://herbertograca.com/2017/09/14/ports-adapters-architecture/

gRPC Authors. (s. f.-a). *Core concepts, architecture and lifecycle*. Recuperado el 8 de junio de 2026, de https://grpc.io/docs/what-is-grpc/core-concepts/

gRPC Authors. (s. f.-b). *Performance best practices*. Recuperado el 8 de junio de 2026, de https://grpc.io/docs/guides/performance/

HashiCorp. (s. f.). *What is Terraform?* Recuperado el 8 de junio de 2026, de https://developer.hashicorp.com/terraform/intro

Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns: Designing, building, and deploying messaging solutions*. Addison-Wesley.

Liu, X., et al. (2023). High performance microservice communication technology based on modified remote procedure call. *Scientific Reports, 13*, 12023. https://doi.org/10.1038/s41598-023-39355-4

Martin, R. C. (2017). *Clean architecture: A craftsman's guide to software structure and design*. Prentice Hall.

Microsoft. (s. f.). *Compare gRPC services with HTTP APIs*. Recuperado el 8 de junio de 2026, de https://learn.microsoft.com/aspnet/core/grpc/comparison

NATS. (s. f.-a). *JetStream*. Recuperado el 8 de junio de 2026, de https://docs.nats.io/nats-concepts/jetstream

NATS. (s. f.-b). *JetStream consumers*. Recuperado el 8 de junio de 2026, de https://docs.nats.io/nats-concepts/jetstream/consumers

Niswar, M., Safruddin, R. A., Bustamin, A., & Aswad, I. (2024). Performance evaluation of microservices communication with REST, GraphQL, and gRPC. *International Journal of Electronics and Telecommunications, 70*(2). https://doi.org/10.24425/ijet.2024.149562

OpenTelemetry. (s. f.). *Signals*. Recuperado el 8 de junio de 2026, de https://opentelemetry.io/docs/concepts/signals/

Prometheus. (s. f.). *Overview*. Recuperado el 8 de junio de 2026, de https://prometheus.io/docs/introduction/overview/

Protocol Buffers. (s. f.). *Protocol Buffers documentation*. Recuperado el 8 de junio de 2026, de https://protobuf.dev/

RabbitMQ. (s. f.-a). *AMQP 0-9-1 model explained*. Recuperado el 8 de junio de 2026, de https://www.rabbitmq.com/tutorials/amqp-concepts

RabbitMQ. (s. f.-b). *Consumer acknowledgements and publisher confirms*. Recuperado el 8 de junio de 2026, de https://www.rabbitmq.com/docs/confirms

Redis Inc. (s. f.-a). *Redis Streams*. Recuperado el 8 de junio de 2026, de https://redis.io/docs/latest/develop/data-types/streams/

Redis Inc. (s. f.-b). *XREADGROUP*. Recuperado el 8 de junio de 2026, de https://redis.io/docs/latest/commands/xreadgroup/

Redis Inc. (s. f.-c). *XACK*. Recuperado el 8 de junio de 2026, de https://redis.io/docs/latest/commands/xack/

Redis Inc. (2026a). *Announcing Redis 8.6: Performance improvements*. Recuperado el 8 de junio de 2026, de https://redis.io/blog/announcing-redis-86-performance-improvements-streams/

Redis Inc. (2026b). *Idempotent message processing in Redis Streams*. Recuperado el 8 de junio de 2026, de https://redis.io/docs/latest/develop/data-types/streams/idempotency/

Sousa, R., et al. (2025). *Impact of protocol selection on performance and scalability in microservices: A comparison of gRPC, REST, and GraphQL*. ResearchGate. https://www.researchgate.net/publication/392507557
