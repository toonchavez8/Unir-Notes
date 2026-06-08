# Estado del arte: broker hibrido de mensajeria basado en gRPC y Redis

## 1. Introduccion

Las arquitecturas de software actuales se apoyan cada vez mas en sistemas distribuidos, microservicios y comunicacion orientada a eventos. En estos entornos, una aplicacion deja de ser un unico bloque que ejecuta toda la logica de negocio y pasa a estar formada por servicios independientes que deben intercambiar informacion de manera confiable, eficiente y observable. Este cambio aporta escalabilidad y flexibilidad, pero tambien introduce problemas tecnicos relevantes: latencia de red, duplicacion de mensajes, gestion de consumidores, confirmacion de procesamiento, tolerancia a fallos y mantenimiento de contratos entre servicios (Fowler & Lewis, 2014).

En este contexto, los brokers de mensajeria y las plataformas de streaming han adquirido un papel central. Soluciones como Apache Kafka, RabbitMQ, Apache Pulsar, NATS JetStream, Google Cloud Pub/Sub y Redis Streams ofrecen mecanismos para publicar, enrutar, almacenar y consumir mensajes bajo diferentes modelos de entrega (Apache Kafka, s. f.; Apache Pulsar, s. f.; Google Cloud, s. f.; NATS, s. f.-a; RabbitMQ, s. f.-a; Redis, s. f.-a). Sin embargo, cada alternativa responde mejor a un conjunto particular de necesidades. Algunas priorizan durabilidad y procesamiento masivo; otras se orientan a baja latencia, pub/sub, colas o consumo pull. Esta diversidad hace necesario justificar con claridad que tipo de sistema se desea desarrollar y que combinacion tecnologica resulta adecuada para el alcance del TFM.

El desarrollo practico propuesto consiste en el diseno e implementacion de un broker de mensajeria hibrido para sistemas distribuidos, basado en gRPC, Protocol Buffers y Redis Streams. La propuesta busca combinar comunicacion en tiempo real mediante streaming gRPC con un modelo asincrono de almacenamiento temporal y consumo pull apoyado en Redis. Adicionalmente, se contempla una estrategia de idempotencia para reducir reprocesamientos, un SDK para facilitar el uso del broker desde clientes y una arquitectura desacoplada inspirada en los principios de arquitectura hexagonal y arquitectura limpia (Cockburn, 2005; Martin, 2017).

La finalidad del presente estado del arte es analizar el conocimiento actual sobre las tecnologias, patrones y decisiones arquitectonicas relacionadas con este desarrollo. A partir de dicho analisis se justifica la pertinencia del proyecto, sus caracteristicas principales y su aportacion: una propuesta academica y funcional que permite estudiar la integracion de comunicacion sincrona en tiempo real, mensajeria asincrona, consumo controlado, idempotencia y observabilidad en un unico prototipo.

## 2. Descripcion del desarrollo practico

El proyecto propuesto consiste en desarrollar un broker de mensajeria hibrido orientado a sistemas distribuidos. El sistema permitira que servicios productores publiquen mensajes y que servicios consumidores los reciban mediante dos modalidades principales: comunicacion en tiempo real por streaming gRPC y comunicacion asincrona mediante una cola ligera respaldada por Redis Streams.

El broker actuara como intermediario entre productores y consumidores. Para los escenarios de baja latencia, el sistema utilizara gRPC y sus modalidades de streaming, lo que permite mantener conexiones persistentes y enviar multiples mensajes sobre una misma relacion cliente-servidor (gRPC Authors, s. f.). Para los escenarios donde los consumidores no deben procesar los mensajes inmediatamente, se utilizara Redis Streams como almacenamiento temporal, aprovechando operaciones como lectura por grupos de consumidores y confirmacion mediante acknowledge (Redis, s. f.-a; Redis, s. f.-b; Redis, s. f.-c).

La propuesta no busca reemplazar plataformas industriales como Kafka, RabbitMQ, Pulsar o NATS JetStream. Su objetivo es academico y experimental: demostrar una arquitectura propia que integre distintas necesidades de comunicacion y permita evaluar sus ventajas, limites y compromisos. En ese sentido, el valor del proyecto no se encuentra en competir con brokers maduros, sino en construir un prototipo controlado que facilite el estudio de contratos gRPC, patrones de mensajeria, idempotencia, consumo pull, fan-out, fan-in, observabilidad y separacion arquitectonica.

El desarrollo practico contemplara, como minimo, los siguientes elementos:

- Un contrato de comunicacion que esta definido por Protocol Buffers.
- Un servidor broker implementado en Go para la cuestion de rapidez.
- Servicios gRPC con comunicacion en tiempo real y operaciones de tipo cola.
- Integracion con Redis Streams para la persistencia temporal de mensajes.
- Control basico de idempotencia mediante el uso claves temporales.
- Mecanismo de confirmacion para el  consumo y  acknowledgement.
- SDK como capa cliente para simplificar el uso del broker.
- Observabilidad basica mediante logs, metricas y endpoints de salud.
- Pruebas unitarias, de integracion y pruebas de comportamiento.
- Arquitectura separada por puertos y adaptadores.

## 3. Caracteristicas previstas del sistema

El broker hibrido propuesto incluira las siguientes caracteristicas funcionales y no funcionales:

- Publicacion de mensajes por parte de multiples productores.
- Enrutamiento de mensajes hacia uno o varios consumidores.
- Soporte de patrones fan-out para distribuir un mensaje a varios destinos.
- Soporte parcial de fan-in para reunir respuestas de varios consumidores hacia un origen.
- Comunicacion en tiempo real mediante streaming gRPC.
- Comunicacion asincrona mediante almacenamiento temporal en Redis Streams.
- Consumo pull para que los consumidores soliciten mensajes cuando esten listos.
- Confirmacion de procesamiento mediante ack.
- Control de duplicados mediante idempotency keys con tiempo de vida limitado.
- Contratos formales con Protocol Buffers.
- SDK cliente para reducir complejidad de consumo.
- Separacion de responsabilidades mediante arquitectura hexagonal o limpia.
- Observabilidad basica mediante metricas, logs y health checks.
- Pruebas que validen comportamiento de los casos de uso principales.

Estas caracteristicas delimitan el alcance de la primera version. No se pretende garantizar exactamente-once absoluto, orden global entre todos los flujos ni escalabilidad equivalente a plataformas distribuidas maduras. Esos aspectos se consideran lineas de mejora o criterios de evaluacion futura.

## 4. Estado del arte

### 4.1 Arquitecturas distribuidas, microservicios y comunicacion por eventos

Las arquitecturas de microservicios favorecen la division de un sistema en servicios pequenos, independientes y desplegables por separado. Fowler y Lewis (2014) explican que este estilo promueve autonomia de equipos y servicios, pero tambien exige mecanismos adecuados de comunicacion, versionado y operacion. Cuando cada servicio tiene responsabilidades delimitadas, la comunicacion entre ellos deja de ser un detalle secundario y se convierte en una preocupacion arquitectonica central.

En este escenario, la comunicacion orientada a eventos permite que un servicio emita informacion sobre algo ocurrido sin conocer de forma directa todos los consumidores interesados. Este enfoque contribuye al desacoplamiento y facilita que nuevos consumidores se integren sin modificar el productor. Hohpe y Woolf (2003) sistematizan estos problemas mediante los Enterprise Integration Patterns, donde patrones como Message Broker, Message Router, Publish-Subscribe Channel y Message Channel proporcionan vocabulario tecnico para explicar la integracion entre aplicaciones.

El patron Message Broker resulta especialmente relevante para este TFM, ya que plantea la necesidad de desacoplar el emisor del receptor y mantener control central sobre el flujo de mensajes (Hohpe & Woolf, 2003). Dominus se alinea con esta idea porque actua como componente intermedio que recibe mensajes y los distribuye a consumidores, ya sea en tiempo real o mediante una cola temporal.

No obstante, las arquitecturas distribuidas tambien generan complejidad. La red puede fallar, los mensajes pueden duplicarse, los consumidores pueden desconectarse y el monitoreo se vuelve indispensable. Por ello, una propuesta de broker no debe limitarse a mover bytes entre servicios; debe considerar confirmaciones, idempotencia, observabilidad, contratos y estrategias de prueba.

### 4.2 gRPC y Protocol Buffers como base de comunicacion

gRPC es un framework de comunicacion remota orientado a servicios que utiliza HTTP/2 y Protocol Buffers. La documentacion oficial describe cuatro modalidades principales: llamadas unarias, streaming de cliente, streaming de servidor y streaming bidireccional (gRPC Authors, s. f.). Esta caracteristica lo diferencia de un enfoque REST tradicional, donde el modelo mas comun es una solicitud seguida de una respuesta.

Para este proyecto, gRPC es relevante porque permite representar distintos modos de comunicacion dentro del mismo contrato. La API tipo cola puede usar llamadas unarias, mientras que la comunicacion en tiempo real puede usar streaming. Microsoft (s. f.) senala que gRPC ofrece beneficios frente a APIs HTTP/JSON cuando se requiere eficiencia, contratos estrictos y comunicacion entre servicios. Sin embargo, tambien presenta limitaciones: no es tan directo para consumo desde navegadores como REST, requiere generacion de codigo y puede resultar menos transparente para depuracion manual.

Protocol Buffers complementa a gRPC como mecanismo de definicion y serializacion de datos. La documentacion oficial lo presenta como un mecanismo independiente de lenguaje y plataforma para serializar datos estructurados (Protocol Buffers, s. f.). En este proyecto, su funcion principal es establecer un contrato formal entre broker, SDK y clientes. Esto se asemeja a usar tipos compartidos en frontend y backend, pero aplicado a comunicacion de red.

La alternativa mas simple habria sido usar REST con JSON. Esta opcion facilitaria pruebas manuales y adopcion por parte de desarrolladores web. No obstante, REST no ofrece de manera natural los tres modelos de streaming que se requieren para el objetivo del proyecto. Otra alternativa habria sido WebSockets, utiles para comunicacion en tiempo real, pero menos adecuados como contrato tipado entre servicios backend. Por ello, gRPC y Protobuf son una eleccion coherente para un broker experimental centrado en comunicacion servicio-a-servicio.

### 4.3 Brokers de mensajeria y plataformas existentes

Apache Kafka es una de las plataformas mas representativas para streaming de eventos. Su arquitectura basada en topics, particiones, productores y consumidores permite alto rendimiento y almacenamiento duradero de eventos. La documentacion oficial de Kafka resalta su papel como plataforma distribuida para publicar, almacenar y procesar flujos de registros (Apache Kafka, s. f.). Ademas, Kafka ha desarrollado mecanismos de idempotencia y transacciones para ofrecer garantias de procesamiento mas fuertes en determinados escenarios (Apache Kafka, s. f.).

Kafka es una referencia importante, pero no coincide exactamente con el alcance propuesto. Su fortaleza esta en el procesamiento masivo, retencion de eventos, particionado y ecosistema de integracion. Dominus, en cambio, busca una arquitectura mas ligera y experimental basada en gRPC y Redis. La comparacion permite justificar que el TFM no intenta superar a Kafka, sino estudiar una alternativa controlada con menor complejidad operativa para escenarios concretos.

RabbitMQ representa una aproximacion distinta. Como broker AMQP, destaca por sus exchanges, colas, enrutamiento flexible y confirmaciones. La documentacion de RabbitMQ enfatiza la importancia de acknowledgements y publisher confirms para la seguridad de entrega en sistemas distribuidos (RabbitMQ, s. f.-a; RabbitMQ, s. f.-b). Frente a Dominus, RabbitMQ tiene mayor madurez como broker de cola y routing. Sin embargo, su interfaz principal no es gRPC ni esta orientada a demostrar la integracion de streaming gRPC con una cola Redis.

Apache Pulsar tambien combina pub/sub, topics, subscriptions y acknowledgements. Su documentacion explica que productores publican mensajes en topics y consumidores se suscriben a ellos, confirmando procesamiento mediante acknowledgements (Apache Pulsar, s. f.). Pulsar ofrece capacidades avanzadas como distintos tipos de suscripcion, redelivery y persistencia. No obstante, su arquitectura es mas compleja y se orienta a una plataforma distribuida de produccion.

NATS JetStream ofrece otra alternativa relevante, especialmente para baja latencia, streams persistentes y consumidores pull o push. La documentacion de NATS destaca que JetStream incorpora consumidores con seguimiento de entregas y acknowledgements, y que los consumidores pull permiten procesar mensajes bajo demanda (NATS, s. f.-a; NATS, s. f.-b). Esta alternativa se aproxima mucho al concepto de consumo controlado que persigue Dominus. Aun asi, Dominus se diferencia por su intencion academica de implementar el broker con gRPC, Protobuf y Redis en vez de adoptar directamente una plataforma existente.

Google Cloud Pub/Sub es una alternativa gestionada que permite publicar y consumir mensajes mediante suscripciones push o pull (Google Cloud, s. f.). Su ventaja esta en la operacion gestionada y escalable. Su desventaja para este TFM es que oculta buena parte de la implementacion interna, lo que reduce el valor academico si el objetivo es aprender, implementar y evaluar los compromisos de un broker propio.

### 4.4 Redis Streams como base para almacenamiento temporal

Redis es ampliamente conocido como almacenamiento en memoria, pero Redis Streams introduce una estructura orientada a flujos de mensajes. La documentacion oficial indica que Streams soporta distintas estrategias de consumo y comandos como `XREAD`, `XREADGROUP` y `XRANGE` (Redis, s. f.-a). Para Dominus, esta capacidad permite implementar una cola ligera sin introducir una plataforma de mensajeria completa.

Redis Streams permite agregar mensajes con `XADD`, leer desde grupos de consumidores con `XREADGROUP` y confirmar procesamiento con `XACK` (Redis, s. f.-a; Redis, s. f.-b; Redis, s. f.-c). Esto resulta adecuado para una API de tipo productor-consumidor-ack. El productor publica un mensaje, el consumidor lo solicita cuando esta listo y el ack confirma que fue procesado.

La ventaja principal de Redis Streams para este TFM es la simplicidad operativa. Redis es mas facil de levantar localmente que Kafka o Pulsar y permite demostrar conceptos clave como colas, consumer groups y ack. La limitacion es que la durabilidad, escalabilidad y tolerancia a fallos dependen de la configuracion de Redis. Por ello, Redis Streams es adecuado para prototipo y validacion academica, pero no debe presentarse como sustituto universal de plataformas de streaming de produccion.

### 4.5 Modelos push, pull, ack e idempotencia

La mensajeria distribuida no solo depende de mover mensajes, sino de definir como se entregan y como se confirma su procesamiento. En un modelo push, el broker envia mensajes al consumidor. En un modelo pull, el consumidor solicita mensajes cuando tiene capacidad. NATS JetStream documenta ambos enfoques y destaca que los consumidores pull son utiles cuando se busca escalabilidad y control de flujo desde la aplicacion consumidora (NATS, s. f.-b).

Dominus adopta ambos conceptos. La comunicacion en tiempo real se aproxima a un modelo push/streaming porque el broker distribuye payloads hacia suscriptores. La API asincrona se aproxima a un modelo pull porque el consumidor solicita mensajes mediante una llamada especifica. Esta combinacion es coherente con el objetivo hibrido: tiempo real cuando se requiere inmediatez y cola pull cuando se requiere control del consumo.

El acknowledgement es otro concepto central. RabbitMQ y Pulsar coinciden en que los consumidores deben confirmar cuando han procesado mensajes para que el broker pueda considerarlos completados (Apache Pulsar, s. f.; RabbitMQ, s. f.-a). Redis Streams ofrece una operacion equivalente mediante `XACK` (Redis, s. f.-c). En Dominus, este mecanismo se refleja en la operacion `Ack`, que confirma el procesamiento de un mensaje previamente consumido.

La idempotencia aborda el problema de duplicacion causado por reintentos, fallos de red o incertidumbre sobre el resultado de una operacion. En sistemas distribuidos, un cliente puede enviar un mensaje, sufrir un timeout y reintentar la misma operacion. Sin control de idempotencia, el mensaje podria procesarse dos veces. La solucion consiste en asociar una clave unica a la operacion y recordar temporalmente si ya fue procesada. En Dominus, esta estrategia se implementa mediante claves en Redis con TTL. La decision es adecuada para un prototipo, aunque debe reconocerse que una garantia fuerte requiere operaciones atomicas, por ejemplo una reserva sincronica con `SET NX`.

### 4.6 Patrones fan-out y fan-in

Los patrones fan-out y fan-in son frecuentes en sistemas concurrentes y distribuidos. Fan-out consiste en distribuir una unidad de trabajo o mensaje hacia multiples destinos. Fan-in consiste en reunir respuestas o resultados de varias fuentes. Estos patrones aparecen en soluciones de integracion empresarial, procesamiento paralelo y arquitectura orientada a eventos (Hohpe & Woolf, 2003).

En Dominus, fan-out se manifiesta cuando un productor envia un payload con una lista de suscriptores y el broker lo reenvia a multiples servicios. Este comportamiento permite desacoplar al productor de los consumidores finales. El productor no necesita gestionar por separado cada conexion si el broker centraliza la distribucion.

Fan-in aparece cuando las respuestas de varios suscriptores pueden regresar hacia el origen mediante el broker. Este caso es mas complejo porque implica concurrencia, orden de llegada, cierre de streams y manejo de errores. Go resulta una tecnologia adecuada para este tipo de prototipo porque sus goroutines y channels permiten expresar ejecucion concurrente y comunicacion entre flujos de forma relativamente directa (The Go Authors, s. f.).

No obstante, los patrones fan-out/fan-in tambien introducen riesgos. Si cada mensaje genera goroutines sin limite o si un suscriptor lento bloquea el flujo, pueden aparecer problemas de backpressure, consumo de memoria o fugas de goroutines. Por ello, una implementacion futura deberia evaluar limites de concurrencia, buffers controlados y politicas de reintento.

### 4.7 Arquitectura hexagonal y arquitectura limpia

La arquitectura hexagonal, tambien conocida como puertos y adaptadores, fue propuesta por Cockburn (2005) para aislar la logica de aplicacion de detalles externos como interfaces de usuario, bases de datos o servicios externos. Su idea central consiste en ubicar la aplicacion en el centro y conectar tecnologias externas mediante puertos y adaptadores.

Esta aproximacion es pertinente para Dominus porque el proyecto combina tecnologias heterogeneas: gRPC, Redis, HTTP, Prometheus, OpenTelemetry y Docker. Si la logica del broker dependiera directamente de cada tecnologia, las pruebas y la evolucion del sistema serian mas costosas. Mediante interfaces como puertos de salida, la aplicacion puede expresar que necesita enviar mensajes, guardar mensajes o verificar claves, mientras la infraestructura decide si eso se implementa con Redis, gRPC u otro mecanismo.

La arquitectura limpia de Martin (2017) comparte una preocupacion similar: las dependencias deben apuntar hacia las reglas de negocio y no hacia detalles externos. En un broker hibrido, esta separacion permite probar casos de uso con mocks, reemplazar adaptadores, aislar infraestructura y justificar decisiones de diseno. Sin embargo, tambien introduce complejidad adicional. Fowler (2003) advierte que las arquitecturas empresariales requieren equilibrio entre abstraccion y simplicidad. Para este proyecto, la separacion por capas se justifica porque el sistema no es un CRUD simple; integra comunicacion distribuida, streaming, Redis, idempotencia y observabilidad.

### 4.8 Observabilidad y operacion

Los sistemas distribuidos requieren observabilidad porque los errores no siempre son evidentes en una sola aplicacion. Un mensaje puede quedar pendiente, un consumidor puede desconectarse, un stream puede cerrarse o Redis puede no responder. OpenTelemetry define senales como trazas, metricas y logs para observar la actividad de sistemas distribuidos (OpenTelemetry, 2026). Prometheus, por su parte, recopila y almacena metricas como series temporales, lo que permite monitorear comportamiento y generar alertas (Prometheus, s. f.).

Dominus contempla logs, metricas y endpoints de salud. Esto es importante porque un broker sin observabilidad seria dificil de defender, operar y evaluar. La observabilidad tambien sirve para las pruebas futuras del TFM, ya que permite medir latencia, errores, consumo de recursos y comportamiento bajo carga.

Docker y Terraform complementan la dimension operativa. Docker facilita empaquetar y ejecutar servicios en contenedores reproducibles (Docker, s. f.). Terraform permite describir infraestructura como codigo, incluyendo recursos locales o de nube. En este proyecto, estas herramientas ayudan a levantar el broker, Redis, Prometheus y Grafana de forma repetible. Aunque Docker Compose podria ser una alternativa mas sencilla para un entorno local, Terraform aporta formalidad y permite vincular el desarrollo con practicas de infraestructura como codigo.

## 5. Analisis comparativo y brecha identificada

El analisis del estado del arte muestra que existen soluciones maduras para casi todos los aspectos individuales del problema. Kafka y Pulsar ofrecen plataformas robustas de streaming distribuido; RabbitMQ ofrece un broker AMQP maduro; NATS JetStream combina baja latencia, persistencia y consumidores pull; Redis Streams ofrece una estructura ligera para flujos y grupos de consumidores; Google Cloud Pub/Sub ofrece mensajeria gestionada con push y pull.

La brecha no consiste en que "no exista ningun broker". Esa afirmacion seria incorrecta. La brecha se encuentra en la integracion academica y controlada de varios conceptos dentro de un prototipo propio: gRPC streaming, Protobuf, Redis Streams, consumo pull, idempotencia, SDK, observabilidad y arquitectura hexagonal. Las herramientas existentes pueden resolver el problema en produccion, pero no necesariamente permiten estudiar de forma directa como se construye internamente una solucion hibrida ni que compromisos aparecen al integrarla.

Por ello, el proyecto se justifica como desarrollo practico de TFM. Su aportacion esta en construir y evaluar una arquitectura que combine capacidades sincronas y asincronas, no en declarar superioridad frente a plataformas consolidadas.

## 6. Conclusiones del estado del arte

El estado del arte evidencia que la comunicacion entre servicios es un problema central en arquitecturas distribuidas. Los microservicios y sistemas orientados a eventos requieren mecanismos para desacoplar productores y consumidores, controlar entregas, confirmar procesamiento, evitar duplicados y observar el comportamiento del sistema. Los patrones de integracion empresarial permiten explicar estas necesidades con un vocabulario consolidado, mientras que las plataformas modernas de mensajeria ofrecen distintas respuestas segun el tipo de carga, durabilidad y modelo de consumo requerido.

gRPC y Protocol Buffers resultan adecuados para la parte de comunicacion en tiempo real porque permiten contratos formales y streaming nativo. En comparacion con REST/JSON, gRPC es menos directo para depuracion manual y adopcion web, pero ofrece mejores capacidades para comunicacion servicio-a-servicio con streaming. Por esta razon, su uso esta justificado en un broker que busca manejar flujos persistentes y no solo solicitudes aisladas.

Redis Streams resulta adecuado para la parte asincrona del prototipo porque permite implementar una cola ligera con consumer groups y ack. Frente a Kafka, Pulsar o NATS JetStream, Redis no ofrece por defecto el mismo nivel de plataforma distribuida, pero su simplicidad operativa facilita la implementacion academica y la validacion experimental. La decision es coherente siempre que se reconozcan sus limites de durabilidad y escalabilidad.

La idempotencia aparece como una necesidad critica. En un sistema distribuido, los reintentos pueden provocar duplicados. Incluir idempotency keys en el diseno permite abordar este problema desde el broker, aunque una version productiva deberia reforzar la atomicidad y definir con precision las garantias ofrecidas.

La arquitectura hexagonal o limpia se justifica porque el proyecto integra multiples tecnologias externas. Separar dominio, casos de uso, puertos y adaptadores ayuda a probar, mantener y evolucionar el sistema. Aun asi, se debe evitar sobreingenieria innecesaria; la arquitectura debe estar al servicio de la claridad y no convertirse en complejidad accidental.

En conclusion, el desarrollo practico propuesto es pertinente porque permite estudiar y demostrar la integracion de comunicacion en tiempo real, mensajeria asincrona, consumo pull, idempotencia y observabilidad en un broker hibrido. El proyecto no pretende reemplazar soluciones industriales, sino construir un prototipo funcional, evaluable y academicamente defendible que ayude a comprender los compromisos de diseno presentes en los sistemas distribuidos modernos.

## Referencias

Apache Kafka. (s. f.). *Apache Kafka documentation*. Recuperado el 2 de junio de 2026, de https://kafka.apache.org/documentation/

Apache Kafka. (s. f.). *Kafka design*. Recuperado el 2 de junio de 2026, de https://kafka.apache.org/42/design/design/

Apache Pulsar. (s. f.). *Messaging concepts*. Recuperado el 2 de junio de 2026, de https://pulsar.apache.org/docs/3.0.x/concepts-messaging/

Cockburn, A. (2005). *Hexagonal architecture: The original 2005 article*. Recuperado el 2 de junio de 2026, de https://alistair.cockburn.us/hexagonal-architecture

Docker. (s. f.). *What is Docker?* Recuperado el 2 de junio de 2026, de https://docs.docker.com/engine/docker-overview/

Fowler, M. (2003). *Patterns of enterprise application architecture*. Addison-Wesley.

Fowler, M., & Lewis, J. (2014). *Microservices: A definition of this new architectural term*. Recuperado el 2 de junio de 2026, de https://martinfowler.com/articles/microservices.html

Google Cloud. (s. f.). *What is Pub/Sub?* Recuperado el 2 de junio de 2026, de https://docs.cloud.google.com/pubsub/docs/pubsub_overview

gRPC Authors. (s. f.). *Core concepts, architecture and lifecycle*. Recuperado el 2 de junio de 2026, de https://grpc.io/docs/what-is-grpc/core-concepts/

Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns: Designing, building, and deploying messaging solutions*. Addison-Wesley.

Martin, R. C. (2017). *Clean architecture: A craftsman's guide to software structure and design*. Prentice Hall.

Microsoft. (s. f.). *Compare gRPC services with HTTP APIs*. Recuperado el 2 de junio de 2026, de https://learn.microsoft.com/en-us/aspnet/core/grpc/comparison

NATS. (s. f.-a). *JetStream*. Recuperado el 2 de junio de 2026, de https://docs.nats.io/nats-concepts/jetstream

NATS. (s. f.-b). *JetStream consumers*. Recuperado el 2 de junio de 2026, de https://docs.nats.io/nats-concepts/jetstream/consumers

OpenTelemetry. (2026). *Signals*. Recuperado el 2 de junio de 2026, de https://opentelemetry.io/docs/concepts/signals/

Prometheus. (s. f.). *Overview*. Recuperado el 2 de junio de 2026, de https://prometheus.io/docs/introduction/overview/

Protocol Buffers. (s. f.). *Protocol Buffers documentation*. Recuperado el 2 de junio de 2026, de https://protobuf.dev/

RabbitMQ. (s. f.-a). *Consumer acknowledgements and publisher confirms*. Recuperado el 2 de junio de 2026, de https://www.rabbitmq.com/docs/4.2/confirms

RabbitMQ. (s. f.-b). *Publishers*. Recuperado el 2 de junio de 2026, de https://www.rabbitmq.com/docs/4.2/publishers

Redis. (s. f.-a). *Redis Streams*. Recuperado el 2 de junio de 2026, de https://redis.io/docs/latest/develop/data-types/streams/

Redis. (s. f.-b). *XREADGROUP*. Recuperado el 2 de junio de 2026, de https://redis.io/docs/latest/commands/xreadgroup/

Redis. (s. f.-c). *XACK*. Recuperado el 2 de junio de 2026, de https://redis.io/docs/latest/commands/xack/

The Go Authors. (s. f.). *Documentation*. Recuperado el 2 de junio de 2026, de https://go.dev/doc/

