![TFM_Unir-F1011-Servicio_Mensajeria-Gdocs](Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs.png)

Universidad Internacional de La Rioja

Escuela Superior de Ingeniería y Tecnología

Maestría en Ingeniería de Software y Sistemas Informáticos

Diseño e implementación de Dominus Broker: broker de mensajería en tiempo real basado en gRPC y Redis Streams

|Trabajo fin de estudio presentado por:|Maikel Barrios Insua<br><br>Daniel Campos Castañeda<br><br>Miguel de Jesús Chávez Barragán<br><br>Fernando Enrique García Castellanos<br><br>César Octavio Sánchez Contreras|
|---|---|
|Tipo de trabajo:|Desarrollo Práctico|
|---|---|
|Modalidad:|Por Equipo|
|---|---|
|Director/a:|Rodrigo Montufar Chaveznava|
|---|---|
|Fecha:|Septiembre 2026|
|---|---|

# Resumen (TBD)

**TBD:** En este apartado se introducirá un breve resumen en español del trabajo realizado (extensión entre 150 y 300 palabras). Este resumen debe incluir el objetivo o propósito de la investigación, la metodología, los resultados y las conclusiones.

El resumen debe contener lo que se ha pretendido realizar (objetivo o propósito de la investigación), cómo se ha realizado (método o proceso desarrollado) y para qué se ha realizado (resultados y conclusiones).

En el aula virtual vas a encontrar información y formación sobre competencias transversales que te ayudarán a elaborar mejor tu trabajo final (gestionar la información: diferenciar entre citar, parafrasear y copiar; buscar y seleccionar bibliografía; citar y referenciar correctamente; conocer los principales errores de ortografía, de puntuación y de gramática; redactar textos académicos y usar herramientas ofimáticas).

Importante: la extensión mínima es de sesenta páginas y la máxima de noventa páginas, sin contar portada, resumen, _abstract,_ índices y anexos. Además, es obligatorio redactar un resumen extendido del TFE en formato de artículo en el anexo A de la memoria.

**Palabras clave:** (de tres a cinco palabras clave).

# Abstract (TBD)

**TBD:** En este apartado se introducirá un breve resumen en **inglés** del trabajo realizado (extensión entre 150 y 300 palabras). Este resumen debe incluir el objetivo o propósito de la investigación, la metodología, los resultados y las conclusiones.

**Keywords:** (de tres a cinco palabras clave en inglés).

Índice de contenidos (TBD)

[Resumen (TBD) 2](#_qus4fc5sule0)

[Abstract (TBD) 3](#_qvi6pen53bt6)

[1. Introducción (TBD) 6](#_uofdr4xs4p3s)

[1.1. Justificación 7](#_pxdvdphmxo5d)

[1.2. Planteamiento del problema 9](#_w2mpyj31kadb)

[1.3. Estructura del trabajo 10](#_xrg9kirmh8up)

[2. Contexto y estado del arte 11](#_kf2oshg7smwy)

[2.1. Descripción del desarrollo práctico 11](#_nkuqbplu98pe)

[2.2. Características previstas del sistema 11](#_b1v7js6jjhm5)

[2.3. Estado del arte 12](#_z8hfrzyxyoq2)

[2.4. Conclusiones del estado del arte 20](#_g6a64og0um4r)

[3. Objetivos concretos y metodología de trabajo 21](#_zb4898xn3wct)

[3.1. Objetivo general 21](#_28eismbgo99k)

[3.2. Objetivos específicos 22](#_qm4frhtpyq25)

[3.3. Metodología del trabajo 22](#_g0xfbeb1r0c6)

[4. Desarrollo específico de la contribución (TBD) 49](#_kzlx5viv94f5)

[4.1. Desarrollo práctico 49](#_u8yqgsbxit4g)

[4.2. Pruebas de Herramientas 51](#_s1wzniqhl70a)

[5. Conclusiones y trabajo futuro (TBD) 88](#_3rq10xam3m0c)

[5.1. Conclusiones (TBD) 88](#_trzsmjdqk2z4)

[5.2. Trabajo futuro (TBD) 88](#_7a57waglitqm)

[6. Referencias bibliográficas 89](#_s1wzniqhl70a)

[Anexo A. Artículo 92](#_tm45hjpi7qx1)

[Anexo B. Puesta en marcha 99](#_3ra5dp33ylul)

[Objetivo y alcance 99](#_bn5ekbvm15y2)

[Requisitos previos. 99](#_t2qe8lhvamxn)

[Clonar los repositorios. 100](#_4miss1jsu61)

[Arranque inicial. 101](#_25dp6bcc42pu)

[Preparacion de Redis 102](#_tvj3yp2uumvs)

[Configuración de Dominus Broker 103](#_9ekdblxd4wyl)

[Pruebas Automatizadas Antes Del Arranque 106](#_lvisgi6ichfv)

[Validación Del Monitor HTTP 107](#_vh3adqo6nwyb)

[Despliegue Completo Con Docker 108](#_a6jg2hhdfo94)

[Infraestructura Con Terraform 112](#_zdrujwadsjo4)

[Solución De Problemas 115](#_zfovgrnsiyt1)

[Para parar y limpiar 118](#_zaaojusvh18g)

[Anexo C. Manual básico de usuario 119](#_3ra5dp33ylul)

[Anexo D. Guía básica de mantenimiento 126](#_3ra5dp33ylul)

[Soporte y atención de incidencias 126](#_6rte963n6zpj)

[Componentes sujetos a mantenimiento 127](#_39mqpwc7v865)

[Actualización controlada de software y dependencias 128](#_gyxtr19wirp9)

[Compatibilidad de contratos y configuración 129](#_vcu44dykecoa)

[Validación posterior a cambios de mantenimiento 130](#_vn9cd49s52ck)

[Revisión de logs, métricas y errores recurrentes 131](#_b6e4g3rnlnth)

[Registro, comunicación y trazabilidad de cambios 132](#_ilyqyrw1gce4)

[Checklist notas de ayuda (BORRAR) 133](#_3ra5dp33ylul)

Índice de figuras (TBD)

[Figura 1. 8](#_zbrnzdhej123)

Índice de tablas (TBD)

[Tabla 1. 8](#_cc1ycjl2nzwx)

# 1. Introducción (TBD)

**TBD:** La introducción presenta el trabajo al lector: se debe resumir de forma esquemática pero suficientemente clara lo **esencial** de **cada una** de las **partes** del **trabajo.** La lectura de este primer capítulo ha de dar una idea clara de lo que se pretendía, las conclusiones a las que se ha llegado y del procedimiento seguido.

Como tal, es uno de los capítulos más importantes de la memoria. Las **ideas principales** que transmitir son la identificación del **problema a tratar,** la **justificación** de su importancia, los **objetivos generales** a grandes rasgos y un adelanto de la **contribución** que esperas hacer.

En esta introducción se engloban, también, los siguientes apartados: **justificación,** **planteamiento** del **problema** y **estructura** del **trabajo.**

Ejemplo de nota al pie[[1]](#footnote-0).

## 1.1. Justificación

En este apartado se deberá presentar el **problema** de **estudio** al que se quiere dar solución y justificar su importancia para la comunidad educativa y científica.

La lectura de este apartado debe dar una idea clara de las razones, motivos e intereses que han llevado a la elección de este tema. Recuerda que para poder justificar este trabajo debe haber referencias a la investigación previa sobre el tema objeto de estudio, independientemente de que luego se profundice en otros apartados.

Las siguientes preguntas puedan ayudar a la redacción de este apartado:

- ¿Cuál es el problema que quieres tratar?
- ¿Cuáles crees que son las causas?
- ¿Por qué es relevante el problema?

A continuación, se indica con un ejemplo cómo deben introducirse los títulos y las fuentes en Tablas y Figuras.

**Tabla 1.**

![TFM_Unir-F1011-Servicio_Mensajeria-Gdocs](Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs.jpeg)

Fuente: American Psychological Association, 2020a.

**Figura 1.**

![TFM_Unir-F1011-Servicio_Mensajeria-Gdocs](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%201.jpeg>)

Fuente: American Psychological Association, 2020b.

## 1.2. Planteamiento del problema

Se debe plantear, de forma breve, el **problema/necesidad** detectada de la que se parte para proponer la **propuesta** y la **finalidad** del **TFE.** Los objetivos se van a plantear posteriormente, pero en este apartado debe quedar claro qué te planteas con la intervención.

Es necesario que los temas escogidos tengan una vinculación directa con la ingeniería de software, el desarrollo web y/o la ciberseguridad y, por tanto, el tema trabajado debe estar en consonancia con la titulación.

Las siguientes preguntas puedan ayudar a la redacción de este apartado:

- ¿Cómo se podría solucionar el problema?
- ¿Qué es lo que se propone? Aquí describes tus objetivos en términos generales.

## 1.3. Estructura del trabajo

Aquí describes brevemente lo que vas a contar en cada uno de los capítulos siguientes.

## 

## 

## 

## 

## 

## 

# 2. Contexto y estado del arte

> [!info] Alcance de la revisión editorial
> A partir de este capítulo se normalizan tablas, figuras, notas, citas y referencias con criterio APA 7. En las piezas visuales se separan el número en negrita y el título en cursiva, y se mantiene debajo una nota con la fuente y la función de la evidencia. Los callouts señalan ajustes que conviene acordar entre los autores antes de modificar la redacción colaborativa.

## 2.1. Descripción del desarrollo práctico

Este proyecto consiste en el diseño y la posterior implementación de un Broker de mensajería híbrido orientado principalmente a sistemas distribuidos, basados en arquitecturas destinadas a eventos en tiempo real. Nuestra propuesta permitirá que servicios productores publiquen mensajes y que otros servicios consumidores los reciban mediante dos modalidades principales; la comunicación en tiempo real utilizando el framework gRPC y como segunda modalidad una comunicación asíncrona respaldada por Redis Stream.

Este Broker actuará como un intermediario entre los servicios productores y los servicios consumidores. Los sistemas distribuidos han crecido exponencialmente y a su vez van requiriendo mayor capacidad para manejar grandes cantidades de eventos sin que se vean afectados por la poca rapidez y la baja disponibilidad que han demostrado tener las soluciones de mensajería tradicionales actuales.

El informe presentado por Gartner Peer Community (2023) indica que el 74% de las organizaciones que son encuestadas ya utilizan arquitecturas de microservicios, con un 23% adicional que planean implementarlas próximamente. IMARC Group (2024) recalca que el mercado global de arquitectura de microservicios alcanzó los 4,200 millones de dólares en 2024 y predice que para 2033 esta cifra aumente a 13,100 millones. Gracias a ello se hace cada vez más evidente la necesidad de una infraestructura de mensajería especializada que integre la comunicación síncrona como asíncrona.

> [!warning] Verificar alcance y actualidad de las cifras
> Conviene confirmar la metodología de Gartner Peer Community y la fecha de consulta de IMARC Group. La frase final también requiere cambiar "síncrona" por "en tiempo real" si ese es el contraste técnico que mantiene el resto del trabajo.

## 2.2. Características previstas del sistema

El Broker que se propone integrará las siguientes características funcionales:

- Un contrato de comunicación definido con Protocol Buffers: Facilitando la comunicación entre servicios, y así reduciendo errores de integración.
- Un servidor broker implementado en Go: Aprovechando su capacidad para manejo de múltiples conexiones simultáneas.
- Servicios gRPC para comunicación en tiempo real y operaciones tipo cola: Para la entrega inmediata de mensajería y cola asíncrona para desacoplar los servicios productores y consumidores.
- Integración con Redis Streams para persistencia temporal de mensajes: Utilizándolo como un buffer de alta velocidad.
- Control básico de idempotencia mediante claves temporales: Para prevenir el procesamiento duplicado de los mensajes.
- Mecanismo de confirmación de consumo o acknowledgement: Eliminando un mensaje de la cola cuando el consumidor confirmó haberlo procesado.
- SDK o capa cliente para simplificar el uso del Broker: Para reducir la barrera de integración para los equipos que consuman el Broker.
- Observabilidad básica mediante logs, métricas y endpoints de salud: Facilitando la detección de problemas y monitoreo del rendimiento.
- Pruebas unitarias, de integración y pruebas de comportamiento bajo escenarios representativos.
- Arquitectura desacoplada basada en puertos y adaptadores.

> [!todo] Homogeneizar la lista de características
> Los elementos alternan sustantivos, oraciones y gerundios después de los dos puntos. Para la versión final conviene formularlos con una misma estructura gramatical y escribir de manera uniforme `broker`, `acknowledgement` y `Redis Streams`.

Estas características delimitan el alcance de la primera versión, no se pretende garantizar en absoluto orden global entre los flujos ni escalabilidad equivalente a las plataformas similares existentes, estos aspectos se consideran líneas de mejoras o criterios de evaluación futura.

## 2.3. Estado del arte

### Brokers de mensajería y plataformas existentes

Los Brokers de mensajería forman parte de una arquitectura distribuida moderna, esto es debido a que permiten desacoplar productores y consumidores. Usan métodos de publicación y suscripción, enrutamiento y persistencia de mensajes para garantizar la transferencia de mensajes entre sistemas. Estos sistemas contemplan la tolerancia de fallos, promueven una estabilidad horizontal, el control del flujo y garantías de entrega de mensajes (Newman, 2021).

Seleccionar un broker de mensajería es indispensable para implementar un sistema híbrido que combina colas de trabajo para streaming de eventos o mensajes como la que proponemos. Cada plataforma ofrece ventajas y limitaciones, particularmente en términos de rendimiento, complejidad y modelos de consumo solo para mencionar algunos. Por esa razón realizamos un análisis comparativo de distintas plataformas como brokers que están usadas en la industria para identificar la más adecuada para el desarrollo del broker híbrido.

Existe Apache Kafka que es una de las plataformas más usadas para el streaming de eventos (Apache Kafka, s. f.). Gracias a su arquitectura basada en retención de evento y presentación distribuido. Kafka streams incorpora conceptos de procesamiento con garantías de _Exactly-Once Processing_ (EOS). El objetivo de EOS es asegurar que cada evento sea procesado exactamente una vez. Esto ayuda a reducir la posibilidad de duplicar los resultados (Kleppmann, 2017). Con esa fortaleza viene con mayor complejidad. Especialmente cuando se requiere de administrar clústeres, particiones, retention, replicación y ecosystem de conectores.

Por otro lado tenemos a RabbitMQ que funciona similar a un broker pero de forma distinta. Como es un broker estilo AMQP que es un protocolo de mensajería estandarizada con mecanismos de enrutamiento y confirmación de entrega para desacoplar sistemas (Richards & Ford, 2020). RabbitMQ destaca por intercambio sus colas y las claves de enrutamiento y el publicador lo confirma (RabbitMQ, s. f.). El modelo cómo se trabaja es muy ágil para colas de trabajo tiene un enrutamiento flexible y patrones de mensajería ya validados a nivel producción. Filtro del proyecto que estaremos desarrollando como propuesta RabbitMQ tiene mayor madurez como broker. El centro de conocimiento no está orientado a exponer una api con grpc ni en demostrar la integración entre streaming a través de grpc y red strings no nos permitiría tener esa Unión.

Otra herramienta que existe es Apache pulsar que combina la publicación y suscripción acontecimientos y una arquitectura distribuida entre el almacenamiento y cómputo (Apache Pulsar, s. f.). Pulsar nos ofrece capacidades avanzadas como distintos tipos de suscripción y mayor persistencia. Una limitante de su arquitectura es que resulta ser más compleja de lo que necesitamos para un prototipo que su objetivo es estudiar los comportamientos internos de un broker híbrido.

Una alternativa para bajar la latencia es NATS JetStream por su forma de tener persistencia de streaming de mensajería y la forma de ser comunicadores de pull y push. La documentación afirma que se incorporan consumidores con mayor seguimiento de entregas y acontecimientos y que los consumidores pueden procesar mensajes bajo demanda (NATS, s. f.). El diseño de Nats es algo que lo hace destacar por su simplicidad y el rendimiento que se ofrece, su ecosistema es menor cuando lo comparamos con otras soluciones.

Finalmente, uno de los creadores de GRPC, Google ofrece Google cloud pub/sub su servicio de mensajería con suscripciones de pull y push (Google Cloud, s. f.). La ventaja de esta herramienta es la carga operativa de equipo dado que es una limitación para este trabajo que se oculta gran parte en una solución interna lo cual reduce mayormente el objetivo que es construir y evaluar el broker híbrido. Dado a que los mecanismos internos están abstraídos por el proveedor esta solución limita la posibilidad de experimentar con los componentes internos que limitan o impactan en el funcionamiento del broker de mensajería.

> [!attention] Revisión de redacción necesaria en esta subsección
> Los párrafos sobre Kafka, RabbitMQ, Pulsar, NATS y Google Cloud contienen fragmentos de oración, repeticiones y términos que parecen errores de transcripción, por ejemplo: "retención de evento y presentación distribuido", "Filtro del proyecto", "red strings" y "el centro de conocimiento". Es una corrección sustantiva que debe validarse con el autor responsable para no alterar su intención técnica.

### gRPC y Protocol Buffers como base de comunicación

gRPC es un framework de comunicación remota orientado a servicios. Permite que una aplicación invoque métodos definidos en otro servicio utilizando HTTP/2 como protocolo de transporte y Protocol Buffers como mecanismo de definición y serialización de datos. La documentación oficial de gRPC describe cuatro modalidades principales de comunicación: llamadas unarias, streaming de cliente, streaming de servidor y streaming bidireccional (gRPC Authors, 2026). Esta capacidad lo diferencia de un enfoque REST tradicional, donde el modelo más común consiste en una solicitud seguida de una respuesta.

En el contexto de este proyecto, gRPC resulta relevante porque permite representar distintos modos de comunicación dentro de un mismo contrato. Por ejemplo, las operaciones de la API tipo cola, como producir, consumir o confirmar mensajes, pueden modelarse mediante llamadas unarias. En cambio, la comunicación en tiempo real puede aprovechar los mecanismos de streaming para mantener flujos de mensajes entre el broker y los servicios suscritos. Microsoft (s. f.) señala que gRPC ofrece beneficios frente a las API HTTP/JSON cuando se requiere eficiencia, contratos estrictos y comunicación entre servicios. También presenta limitaciones: no es tan directo para el consumo desde navegadores como REST, requiere generación de código a partir de archivos de contrato y puede ser menos transparente para realizar pruebas manuales o depuración básica.

Protocol Buffers complementa a gRPC al proporcionar un formato formal para definir los mensajes, servicios y tipos de datos que se intercambian entre sistemas. La documentación oficial lo presenta como un mecanismo independiente de lenguaje y plataforma para serializar datos estructurados (Protocol Buffers, s. f.). En este proyecto, su función principal es establecer un contrato compartido entre el broker, el SDK y los clientes externos. Esto permite que todos los componentes conozcan con precisión qué operaciones existen, qué datos deben enviarse y qué respuestas pueden recibirse, reduciendo errores de integración y ambigüedad en la comunicación.

Una alternativa más simple habría sido utilizar REST con JSON. Esta opción facilitaría las pruebas manuales, la integración con navegadores y la adopción por parte de desarrolladores web. Sin embargo, REST no ofrece de manera natural los distintos modelos de streaming que requiere el objetivo del proyecto. Otra alternativa habría sido el uso de WebSockets, adecuados para comunicación en tiempo real, pero menos orientados a contratos estrictos y generación automática de código entre servicios backend. Por ello, gRPC y Protobuf son una elección coherente para un broker experimental centrado en comunicación servicio-a-servicio.

### Patrones fan-out y fan-in

Un patrón frecuente que se usa mucho en sistemas concurrentes y distribuidos es el patrón de fan out y fan in. Este patrón consiste en distribuir un evento o unidad de trabajo hacia múltiples destinos y de múltiples fuentes de orígenes hacia una eje central. Que termina haciendo una arquitectura estilo abanico de como pasan los datos de múltiples Fuentes a una fuente central aparecen integraciones empresariales y en producción procesamiento paralelo y arquitectura arquitecturas específicamente orientada a eventos (Newman, 2021).

En nuestra propuesta del broker el fan out lo usaremos cuando un productor va a publicar un evento y debe llegar a varios consumidores. En este caso nuestro broker centraliza la distribución y evita que el productor tenga que gestionar más conexiones individuales con cada receptor, por esa razón este patrón es útil para las notificaciones de propagación de eventos y actualización de cachés o activación de procesos secundarios.

Una vez que el consumidor genera una respuesta debe considerarse en su flujo de origen o el punto central en este caso ya aplicamos el fan-ín. Esta es la parte más compleja porque implicaría concurrencia el orden de llegada el cierre es de El stream y evitar errores parciales y time out exceptions por la latencia de la señal. Go, el lenguaje de programación, para este tema tiene justamente la solución mediante goRoutines y canales que permiten la ejecución concurrente y la comunicación entre flujos de forma directa ayudando a aliviar errores parciales (The Go Authors, s. f.).

Aun así, los patrones de Fan-in y Fan-out vienen con riesgos que debemos de mantener en la mente. Cada mensaje enviado es generado sin límite o un suscrito lento bloquea el flujo podemos tener temas de backpressure, el consumo de memoria o fuga de goRoutines. Por eso se debe considerar implementar límites de concurrencias y políticas de reintento.

> [!todo] Precisar fan-out y fan-in
> Esta subsección mezcla ambos patrones y contiene varios errores de concordancia. Conviene definir por separado el fan-out (un origen distribuye a varios destinos) y el fan-in (varios flujos convergen), y después indicar cuál de ellos implementa realmente cada operación de Dominus.

### Arquitectura hexagonal y arquitectura limpia

Se propone la implementación de la arquitectura hexagonal que también es conocida como puertos y adaptadores que fue primera vez implementada por Cockburn (2005) con la intención de encapsular las reglas de negocio los detalles externos como interfaces y servicios de infraestructura por separado. Esta visión de patrón permite que una aplicación ubicada en el centro de la arquitectura pueda ser probada y conectada de distintos adaptadores sin depender de uno como núcleo.

Martin (2017) menciona que las dependencias deben de apuntar hacia las reglas de negocio y no depender totalmente de ellas. En un broker híbrido donde la separación permite probar que los puertos funcionan como entradas y salidas de la aplicación mientras que los adaptadores habilita que se conecten a esos puertos con la tecnología que utilicemos. Para el caso del broker esta separación nos permite tener una distribución y publicación que integra la comunicación entre streaming, Redis, y la idempotencia.

> [!todo] Completar la relación entre arquitectura hexagonal y limpia
> El segundo enunciado es una oración incompleta y la explicación atribuye a Martin una formulación ambigua. Se recomienda distinguir la regla de dependencias de la arquitectura limpia de la metáfora de puertos y adaptadores de Cockburn.

### Redis Streams como almacenamiento temporal y cola ligera

Redis es ampliamente conocido como almacenamiento en memoria, pero Redis Streams introduce una estructura orientada a flujos de mensajes. La documentación oficial indica que Streams soporta distintas estrategias de consumo y comandos como XREAD, XREADGROUP y XRANGE (Redis, s. f.-a). Esta capacidad permite implementar una cola ligera sin introducir una plataforma de mensajería más compleja.

Redis Streams permite agregar mensajes con `XADD`, leer desde grupos de consumidores con `XREADGROUP` y confirmar procesamiento con `XACK` (Redis, s. f.-a, s. f.-c, s. f.-d). Esto resulta adecuado para una API de tipo productor-consumidor-ack. El productor publica un mensaje, el consumidor lo solicita cuando está listo y el Ack confirma que fue procesado.

La ventaja principal de Redis Streams para este TFM es la simplicidad operativa. Redis es más fácil de levantar localmente que Kafka o Pulsar y permite demostrar conceptos clave como colas, consumer groups y Ack. La limitante es la durabilidad, escalabilidad y tolerancia a fallos ya que dependen de la configuración de Redis. Por ello, Redis Streams es adecuado para prototipos y validación académica, pero no debe presentarse como sustituto universal de plataformas de streaming de producción.

### Modelos push, pull, Ack e idempotencia

La mensajería distribuida no es solo de mover mensajes, es definir cómo se entregan y como se confirma su procesamiento. En un modelo push, el broker envía mensajes al consumidor. En un modelo pull, el consumidor solicita mensajes cuando tiene capacidad. NATS JetStream documenta ambos enfoques y destaca que los consumidores pull son útiles cuando se busca escalabilidad y control de flujo desde la aplicación que consume (NATS, s. f.).

La comunicación en tiempo real se aproxima a un modelo push/streaming porque el broker distribuye payloads hacia suscriptores. La API asíncrona se aproxima a un modelo pull porque el consumidor solicita mensajes mediante una llamada específica. Esta combinación concuerda con el objetivo híbrido: tiempo real cuando se requiere inmediatez y cola pull cuando se requiere control del consumo.

El ACK o acknowledgement, es el mecanismo mediante el cual un consumidor confirma que ya procesó correctamente un mensaje. Herramientas como RabbitMQ y Apache Pulsar utilizan este proceso para que el broker sepa cuándo un mensaje puede darse por completado (Apache Pulsar, s. f.; RabbitMQ, s. f.). Redis Streams ofrece una operación equivalente mediante XACK (Redis, s. f.-c). Esta función se representa con la operación Ack, que permite confirmar que un mensaje consumido ya fue procesado y no debe volver a tratarse como pendiente.

La idempotencia aborda el problema de duplicidad causado por reintentos, fallos de red o incertidumbre sobre el resultado de una operación (Fielding et al., 2022). En un sistema distribuido, un cliente puede enviar un mensaje, no recibir respuesta por un timeout y volver a enviarlo. Si no existe un control de duplicados, el mismo mensaje podría procesarse más de una vez. Para reducir este riesgo, se puede asociar una clave única a cada operación y registrar temporalmente si dicha clave ya fue utilizada. Esta estrategia se apoya en Redis mediante claves con tiempo de vida limitado, lo que permite detectar varios intentos y evitar procesar varias veces innecesariamente. La decisión es adecuada para un prototipo, aunque debe reconocerse que una garantía fuerte requiere operaciones atómicas, como el uso de SET NX, y una coordinación cuidadosa entre la recepción del mensaje, su almacenamiento y su confirmación.

### Análisis comparativo

La Tabla 1 resume la comparación de las tecnologías analizadas con base en las dimensiones más relevantes para el desarrollo del proyecto.

**Tabla 1**

*Comparación de tecnologías para el broker híbrido* 

|**Dimensión**|**gRPC**|**REST/HTTP**|**Redis Streams**|**Kafka/Pulsar**|**NATS JetStream**|
|---|---|---|---|---|---|
|Uso principal|Comunicación servicio-a-servicio|APIs generales y web|Cola/stream ligero|Streaming distribuido|Mensajería ligera y streams|
|Contrato|Protobuf tipado|JSON/OpenAPI opcional|Estructura de mensajes|Esquemas opcionales|Mensajes por subjects|
|Streaming nativo|Sí|Limitado|Lectura de streams|Sí|Sí|
|Modelo pull|Por API propia|Por API propia|XREADGROUP|Consumidores|Consumidores pull|
|Ack|Por diseño de API|Por diseño de API|XACK|Offsets/acks según plataforma|Ack de consumidores|
|Idempotencia|Debe implementarse|Debe implementarse|Soporte reciente y patrones con claves|Transacciones/idempotencia en escenarios concretos|Requiere diseño de consumidor|
|Complejidad operativa|Media|Baja|Baja-media|Media-alta|Media|
|Papel en el proyecto|Canal principal|Alternativa no principal|Persistencia temporal|Referencia comparativa|Referencia comparativa|

_Nota._ Elaboración propia. La tabla contrasta el uso, el contrato, el modelo de consumo, la confirmación, la idempotencia y la complejidad operativa de las alternativas consideradas.

Con esto se demuestra que las tecnologías existentes resuelven partes del problema pero con enfoques distintos. Kafka y pulsar son fuertes para streaming mientras que RabbitMQ para enrutamiento. NATS jetstream para mensajería ligera, cuando redis streams para colas simples con grupos de consumidor. La aportación vista aquí de estas herramientas consiste en integrar un conjunto de estas aportaciones en un prototipo.

## 2.4. Conclusiones del estado del arte

El análisis realizado hasta el momento nos muestra distintas alternativas para implementar sistemas de mensajería distribuida. A partir de esta revisión, gRPC y Redis Streams se consideraron adecuados para el desarrollo propuesto. Por un lado, gRPC permitirá la entrega inmediata mediante streaming bidireccional (gRPC Authors, 2024b, 2026), mientras que Redis Streams permitirá el consumo asíncrono y la confirmación de mensajes (Redis, s. f.-a, s. f.-c). En conjunto, ambas tecnologías cubren las necesidades principales del prototipo sin incorporar una infraestructura de mayor alcance.

Las soluciones analizadas ofrecen capacidades maduras, pero su complejidad puede superar el alcance de este proyecto. Además, el paralelismo, las particiones y las reentregas limitan las garantías de orden y procesamiento único. La entrega al menos una vez mejora la recuperación, aunque puede generar duplicados (Kleppmann, 2017; Richardson, 2018).

Estas limitaciones justifican las principales decisiones de diseño. El broker adoptará una semántica de entrega al menos una vez y utilizará idempotencia mediante Redis para controlar posibles repeticiones. Además gRPC se empleará para la distribución en tiempo real, mientras que el modelo pull permitirá regular el ritmo de consumo. La solución también utilizará una arquitectura de puertos y adaptadores para separar la lógica principal de la infraestructura y facilitar las pruebas (Cockburn, 2005).

La aportación diferenciadora no consistirá en competir con brokers consolidados. Su valor estará en integrar comunicación en tiempo real, consumo asíncrono e idempotencia dentro de una interfaz homogénea. Además, se plantea desarrollar un SDK para simplificar la integración de productores y consumidores dentro del prototipo.

En conclusión, el proyecto nos permitirá estudiar estas capacidades dentro de una solución propia y acotada. Las pruebas evaluarán la latencia, la capacidad de procesamiento, la recuperación ante fallos y el control de duplicados. Los resultados permitirán determinar en qué escenarios el enfoque resulta viable y cuáles son sus principales limitaciones prácticas.

# 3. Objetivos concretos y metodología de trabajo

Este apartado establece los objetivos que guían el desarrollo del broker de mensajería propuesto y la metodología utilizada para construirlo, validarlo y evaluar sus resultados. Primero se presenta el objetivo general del trabajo; después, los objetivos específicos que concretan el alcance del desarrollo. Finalmente, se describe la metodología aplicada durante las fases de análisis, diseño, implementación, pruebas y evaluación del prototipo.

## 3.1. Objetivo general

Diseñar, implementar y evaluar un prototipo funcional de broker de mensajería en tiempo real, denominado Dominus Broker, basado en gRPC y Redis Streams, que permita integrar comunicación inmediata mediante streaming y comunicación asíncrona tipo cola con confirmación de mensajes e idempotencia, con el fin de analizar su viabilidad técnica, comportamiento y limitaciones en escenarios representativos de sistemas distribuidos.

## 3.2. Objetivos específicos

- Analizar las necesidades y limitaciones de los sistemas de mensajería distribuida en escenarios que requieren comunicación en tiempo real, consumo asíncrono, alta concurrencia y control de duplicados.
- Comparar tecnologías y enfoques de mensajería existentes, como gRPC, Redis Streams, Kafka, Pulsar, RabbitMQ y NATS JetStream, para justificar la selección tecnológica del prototipo.
- Definir los requisitos funcionales y no funcionales del broker, considerando publicación de mensajes, consumo, confirmación, streaming, idempotencia, observabilidad y facilidad de integración mediante un SDK.
- Diseñar una arquitectura modular basada en puertos y adaptadores, separando la lógica principal del broker de los detalles técnicos de infraestructura, transporte gRPC, persistencia temporal y configuración del entorno.
- Implementar el prototipo utilizando Go, Protocol Buffers, gRPC y Redis Streams, integrando los flujos principales de comunicación en tiempo real y mensajería asíncrona tipo cola.
- Validar el comportamiento del broker mediante pruebas unitarias, pruebas de integración, pruebas de usabilidad técnica, análisis de ciberseguridad y pruebas de rendimiento bajo escenarios representativos.
- Evaluar los resultados obtenidos a partir de métricas como latencia, capacidad de procesamiento, confirmación de mensajes, recuperación ante fallos y control de duplicados, identificando las limitaciones prácticas y posibles líneas de mejora.

## 3.3. Metodología del trabajo

> [!warning] Corregir la jerarquía de encabezados
> Las fases 3.3.1 a 3.3.7 están escritas como párrafos, mientras que 3.4, 3.5 y 3.6 usan niveles Markdown que no corresponden a su numeración. En el capítulo 4 aparecen además encabezados de quinto y sexto nivel. Conviene limitar la estructura a tres niveles numerados y regenerar después el índice.

El desarrollo de este trabajo seguirá un enfoque iterativo e incremental, lo que permitirá construir una solución de manera progresiva, incorporando retroalimentación en cada fase y ajustando las decisiones de diseño conforme avance la implementación.

Se escogió este enfoque en lugar de un modelo en cascada, por su adaptabilidad a proyectos donde no todos los requisitos pueden definirse desde el inicio. Además las entregas parciales permitirán detectar inconsistencias entre componentes prontamente y las pruebas podrán integrarse desde las primeras fases, evitando que los errores se descubran únicamente al final.

La metodología se estructurará en seis fases con retroalimentación entre ellas:

3.3.1 Fase 1: Análisis del Problema

En esta fase se identifican las limitaciones de los sistemas de mensajería existentes, en escenarios que requieren comunicación en tiempo real, alta concurrencia y control de duplicados.

3.3.2 Fase 2: Definición de Requisitos

A partir del análisis anterior se definirán los requisitos que deberá cumplir el sistema. Se distinguen dos categorías:

Requisitos funcionales:

- Permitir la publicación de mensajes por parte de múltiples productores.
- Distribuir mensajes hacia uno o múltiples suscriptores en tiempo real mediante BrokerAPI.
- Soporta la publicación, consumo y confirmación de mensajes mediante SqsAPI con modelo pull.
- Controlar duplicados mediante claves de idempotencia con tiempo de vida configurable.
- Gestionar mensajes pendientes no confirmados y permitir su entrega.
- Exponer un SDK que simplifique la integración de clientes productores y consumidores.

Requisitos no funcionales:

- Baja latencia en la entrega de mensajes.
- Capacidad para gestionar múltiples conexiones concurrentes sin degradación del rendimiento.
- Observabilidad mediante logs estructurados, métricas y endpoints de salud.
- Arquitectura desacoplada que facilite las pruebas y la evolución futura del sistema.

3.3.3 Fase 3: Diseño de la Solución

En esta fase se definirá la arquitectura del sistema. La solución adoptará el patrón de puertos y adaptadores, que separará la lógica central del broker de los detalles técnicos de infraestructura.

La arquitectura se organizará en cinco capas: clientes externos o SDK, capa de entrada gRPC, capa de aplicación, capa de dominio y capa de infraestructura. Los dos flujos principales serán la comunicación en tiempo real mediante BrokerAPI y la comunicación asíncrona mediante SqsAPI respaldada por Redis Streams.

3.3.4 Fase 4: Implementación

Se construirá el prototipo funcional del broker utilizando Go como lenguaje de implementación.

La implementación contempla los siguientes componentes:

- Definición del contrato con Protocol Buffers.
- Servidor broker con los servicios BrokerAPI y SqsAPI sobre gRPC.
- Integración con Redis Streams.
- Mecanismo de idempotencia con claves de tiempo de vida configurable en Redis.
- SDK cliente que encapsula la comunicación con el broker.
- Sistema de logs, métricas y endpoints de salud para observabilidad básica.

3.3.5 Fase 5: Experimentación y pruebas

Se diseñarán escenarios de prueba orientados a validar el comportamiento del sistema bajo diferentes condiciones de carga y concurrencia. Los escenarios contemplados incluirán:

- Distribución de mensajes a múltiples suscriptores mediante BrokerAPI.
- Publicación concurrente desde múltiples productores.
- Consumo y confirmación de mensajes con diferentes ritmos de procesamiento.
- Reentrega de mensajes pendientes dentro del grupo de consumidores.

3.3.6 Fase 6: Evaluación de resultados

Los resultados obtenidos se analizarán a partir de métricas clave que permitirán evaluar el comportamiento del sistema:

- Latencia en la entrega de mensajes.
- Capacidad de procesamiento medida en mensajes por segundo bajo carga sostenida.
- Consistencia en la entrega de mensajes ante fallos parciales simulados.
- Efectividad del mecanismo de idempotencia para descartar duplicados.

Los resultados permitirán determinar en qué escenarios el enfoque híbrido del broker resulta adecuado y cuáles son sus principales limitaciones prácticas frente a plataformas de mensajería existentes.

3.3.7 Justificación de la metodología

La elección de un enfoque iterativo e incremental en este proyecto responde a criterios metodológicos y prácticos, fundamentados en la naturaleza del sistema que se propone desarrollar. Sommerville (2016) señala que los enfoques iterativos resultan especialmente adecuados cuando los requisitos del sistema no pueden especificarse completamente desde el inicio. Este es precisamente el caso del broker propuesto, donde decisiones críticas de diseño solo podrán validarse en la práctica conforme avance la implementación.

### 3.4 Arquitectura general

La arquitectura general se plantea como un sistema backend orientado a la comunicación entre servicios distribuidos. Su función principal es actuar como un intermediario entre aplicaciones productoras y consumidoras de mensajes. Para ello, el broker expone una interfaz gRPC que permite dos formas principales de comunicación: una modalidad en tiempo real basada en streaming y una modalidad asíncrona tipo cola respaldada por Redis Streams.

La solución se organiza bajo un enfoque de arquitectura desacoplada, inspirado en el patrón de puertos y adaptadores. Este enfoque permite separar la lógica principal del broker de los detalles técnicos de infraestructura, como el transporte gRPC, el almacenamiento en Redis, los mecanismos de monitoreo y la configuración del entorno. De esta manera, el núcleo de la aplicación puede concentrarse en las reglas de comunicación, distribución y confirmación de mensajes, mientras que los adaptadores se encargan de conectar el sistema con tecnologías externas.

A nivel general, la arquitectura se compone de cinco bloques principales: clientes externos o SDK, capa de entrada gRPC, capa de aplicación, capa de dominio y capa de infraestructura.

Los clientes externos representan las aplicaciones que desean publicar o consumir mensajes mediante Dominus. Estos clientes pueden comunicarse directamente con el broker utilizando los contratos definidos en Protocol Buffers, o bien hacerlo a través de un SDK que simplifique la integración. El SDK cumple la función de ocultar parte de la complejidad técnica de gRPC y facilitar el uso de las operaciones disponibles por parte de otros equipos o sistemas.

La capa de entrada está formada por los servicios gRPC expuestos por el broker. En esta capa se reciben las solicitudes externas y se transforman en llamadas hacia los casos de uso internos. Se contemplan dos servicios principales. El primero es BrokerAPI, orientado a comunicación en tiempo real mediante streaming de cliente, streaming de servidor y streaming bidireccional. El segundo es SqsAPI, orientado a operaciones tipo cola, como producir un mensaje, consumirlo y confirmar su procesamiento mediante ACK.

La capa de aplicación contiene los casos de uso del sistema. Esta capa coordina las operaciones principales del broker sin depender directamente de una tecnología específica. Por ejemplo, en el flujo de comunicación en tiempo real, la capa de aplicación recibe mensajes desde la interfaz gRPC y coordina su distribución hacia los servicios suscritos. En el flujo asíncrono, coordina la publicación de mensajes, el consumo por parte de trabajadores y la confirmación del procesamiento. También interviene en validaciones básicas, control de flujo y manejo de errores de aplicación.

La capa de dominio representa los conceptos centrales del sistema. En esta capa se ubican las entidades y contratos internos que describen los mensajes y las operaciones necesarias para enviarlos, consumirlos o confirmarlos. También se definen interfaces o puertos que permiten que la aplicación se comunique con componentes externos sin depender de implementaciones concretas. Por ejemplo, el sistema puede definir un puerto para almacenamiento de mensajes y otro para comunicación con suscriptores, mientras que las implementaciones concretas se ubican en infraestructura.

La capa de infraestructura contiene los adaptadores técnicos del sistema. En esta capa se implementa la comunicación gRPC de entrada y salida, la conexión con Redis Streams, el control de idempotencia mediante claves temporales, los endpoints de monitoreo, los logs, las métricas y la configuración del entorno. Redis Streams funciona como almacenamiento intermedio para los mensajes de la API asíncrona, mientras que el cliente gRPC de salida permite reenviar mensajes hacia servicios suscriptores en los flujos de tiempo real.

Desde el punto de vista funcional, se manejan dos flujos principales. En el flujo de comunicación en tiempo real, un cliente envía mensajes al broker mediante gRPC. El broker recibe la solicitud, identifica los suscriptores y distribuye el contenido hacia uno o varios servicios destino. Este flujo es adecuado para escenarios donde se requiere inmediatez, como propagación de eventos, notificaciones o comunicación bidireccional entre servicios.

En el flujo asíncrono, un productor envía un mensaje mediante la operación Producer. El broker valida el contenido y lo almacena temporalmente en Redis Streams. Posteriormente, un consumidor solicita mensajes mediante la operación Consumer. Cuando el consumidor termina de procesar el mensaje, confirma su procesamiento mediante la operación Ack. Este mecanismo permite desacoplar productores y consumidores, ya que el productor no necesita esperar a que el consumidor procese el mensaje en el mismo momento.

La arquitectura también incorpora mecanismos transversales de seguridad, observabilidad y operación. En seguridad, se contempla el uso de tokens o claves de acceso para proteger las llamadas al broker, además de la posibilidad de utilizar TLS según la configuración del entorno (gRPC Authors, 2024a). En observabilidad, el sistema incluye logs, métricas y endpoints de salud que permiten conocer el estado del broker y detectar errores durante la ejecución. Estos elementos son importantes porque un sistema de mensajería distribuida no solo debe entregar mensajes, sino también facilitar su monitoreo y diagnóstico.

En conjunto, esta arquitectura permite que el sistema sea un prototipo modular y extensible. La separación entre capas facilita las pruebas, el mantenimiento y la evolución futura del sistema. Además, el uso de gRPC y Protocol Buffers permite mantener contratos formales entre clientes y broker, mientras que Redis Streams proporciona una base ligera para demostrar el comportamiento de una cola asíncrona. La arquitectura no busca competir directamente con plataformas consolidadas como Kafka, Pulsar o RabbitMQ, sino integrar en un prototipo académico los conceptos principales de comunicación en tiempo real, mensajería asíncrona, confirmación de procesamiento, idempotencia y observabilidad.

### 3.5 Capa de persistencia

La capa de persistencia dará soporte al modelo de comunicación asíncrona del broker. Su función será conservar temporalmente los mensajes cuando productores y consumidores trabajan a ritmos diferentes. De esta forma, la publicación no dependerá de que el consumidor se encuentre disponible en ese momento. Para esta responsabilidad se propone utilizar Redis Streams. Esta estructura permite registrar mensajes dentro de un flujo ordenado y recuperarlos mediante grupos de consumidores. También permite mantener un seguimiento de los mensajes entregados que todavía no han sido confirmados (Redis, s. f.-a).

Redis se utilizará como almacenamiento temporal y no como repositorio histórico. Los mensajes permanecerán disponibles durante el periodo definido por la política de retención. Esta delimitación permite mantener el alcance del prototipo y evitar una infraestructura más compleja.

#### 3.5.1 Justificación de la tecnología seleccionada

Redis Streams se considera adecuado para la primera versión del proyecto por su facilidad de despliegue y su modelo de consumo. Permite representar una cola de mensajes sin incorporar una plataforma distribuida de mayor alcance.

La estructura ofrece operaciones para publicar, recuperar y confirmar mensajes. Además, los grupos de consumidores permiten distribuir el trabajo entre diferentes instancias y mantener un estado independiente para cada grupo.

La elección también responde al objetivo académico del proyecto. El uso de Redis permitirá observar directamente el almacenamiento, la lectura, las confirmaciones y los mensajes pendientes. Estos mecanismos suelen quedar abstraídos en plataformas administradas.

No obstante, Redis no se presentará como sustituto de brokers consolidados. Su durabilidad, disponibilidad y escalabilidad van a depender de la configuración aplicada. En este trabajo se utilizará como soporte de persistencia temporal para validar el comportamiento del modelo asíncrono.

#### 3.5.2 Organización de la capa

La capa seguirá los principios de puertos y adaptadores. Los casos de uso no van a depender directamente de los comandos o librerías de Redis. En su lugar, utilizarán interfaces definidas en la capa de aplicación (Cockburn, 2005).

El puerto de persistencia definirá las operaciones necesarias para almacenar, recuperar y confirmar mensajes. El adaptador de Redis implementará estas operaciones y encapsulará los detalles técnicos de conexión, serialización y gestión de errores.

Esta separación permitirá probar los casos de uso mediante implementaciones simuladas. También facilitará sustituir Redis por otro mecanismo de almacenamiento si el proyecto lo requiere posteriormente.

Los principales elementos serán los siguientes:

- Casos de uso de publicación, consumo y confirmación.
- Puerto de persistencia de mensajes.
- Puerto de control de idempotencia.
- Adaptador de Redis Streams.
- Adaptador de claves temporales.
- Cliente de conexión con Redis.
- Configuración del stream y del grupo de consumidores.

#### 3.5.3 Diseño lógico de los datos

La persistencia se dividirá en dos estructuras lógicas. La primera almacenará los mensajes asíncronos mediante Redis Streams. La segunda conservará claves temporales para controlar la idempotencia.

Cada mensaje podrá contener, al menos, los siguientes datos:

- Identificador único del mensaje.
- Contenido o payload.
- Fecha de creación.
- Tipo de evento.
- Identificador de correlación.
- Productor de origen.
- Metadatos adicionales.

El identificador permitirá seguir el mensaje durante su ciclo de vida. La fecha de creación facilitará el registro y la observabilidad. El identificador de correlación permitirá relacionar varios eventos de una misma operación.

La clave del stream y el nombre del grupo de consumidores se definirán mediante configuración. Esto evitará que dichos valores queden incorporados directamente en el código. La Tabla 2 organiza los elementos previstos para la capa de persistencia y la información asociada a cada uno.

**Tabla 2**

*Elementos previstos para la capa de persistencia* 

|**Elemento**|**Uso dentro del broker**|**Datos o parámetros asociados**|
|---|---|---|
|Redis Stream|Mantener temporalmente los mensajes hasta que sean solicitados por un consumidor|Identificador del mensaje, payload, fecha de creación, tipo de evento e identificador de correlación|
|Grupo de consumidores|Organizar el reparto de mensajes y dar seguimiento a las entregas pendientes|Nombre del grupo, consumidor asignado, identificador del mensaje y estado de confirmación|
|Claves de idempotencia|Detectar mensajes repetidos dentro de una ventana de tiempo definida|Clave única de la operación, estado registrado y tiempo de expiración|
|Configuración de Redis|Centralizar los parámetros necesarios para acceder y operar la capa de persistencia|Host, puerto, credenciales, nombre del stream, grupo de consumidores y tiempo de expiración|

_Nota._ Elaboración propia. La tabla describe la función y los datos asociados a Redis Streams, los grupos de consumidores, las claves de idempotencia y la configuración de Redis.

#### 3.5.4 Flujo de publicación

El flujo comenzará cuando un productor envíe un mensaje mediante la interfaz gRPC. El broker validará la estructura recibida y añadirá los metadatos necesarios.

Después, el caso de uso de publicación se enviará el mensaje al puerto de persistencia. El adaptador de Redis utilizará XADD para agregar una nueva entrada al stream.

Redis asignará un identificador a la entrada almacenada. El broker devolverá al productor la respuesta correspondiente cuando la operación haya finalizado.

El flujo de publicación estará compuesto por los siguientes pasos:

1. El productor envía un mensaje al broker.
2. El adaptador gRPC recibe y transforma la solicitud.
3. El caso de uso valida el mensaje.
4. El puerto de persistencia recibe la orden de almacenamiento.
5. El adaptador ejecuta XADD.
6. Redis registra el mensaje dentro del stream.

#### 3.5.5 Flujo de consumo

El consumo seguirá un modelo pull. El consumidor solicitará mensajes cuando disponga de capacidad para procesarlos.

El caso de uso de consumo tendrá que acceder al puerto de persistencia. El adaptador utilizará XREADGROUP para recuperar nuevas entradas asociadas al grupo correspondiente (Redis, s. f.-d).

Cuando Redis entrega un mensaje, lo registra como pendiente dentro del grupo. Este estado indica que el mensaje fue asignado, pero todavía no ha sido confirmado.

El flujo de consumo seguirá estos pasos:

1. El consumidor solicita nuevos mensajes.
2. El broker valida la identidad y el grupo solicitado.
3. El caso de uso consulta el puerto de persistencia.
4. El adaptador ejecuta XREADGROUP.
5. Redis entrega las entradas disponibles.
6. El broker devuelve los mensajes al consumidor.

Este modelo permitirá que cada consumidor controle su propio ritmo. También facilitará distribuir el trabajo entre varios miembros del mismo grupo.

#### 3.5.6 Confirmación y mensajes pendientes

Después de procesar correctamente un mensaje, el consumidor enviará una confirmación al broker. El caso de uso de confirmación solicitará al adaptador que registre el resultado.

El adaptador utilizará XACK para confirmar el mensaje dentro del grupo de consumidores (Redis, s. f.-c). Esta operación retirará la entrega de la lista de mensajes pendientes.

XACK no eliminará la entrada original del stream. La eliminación física dependerá de la política de retención o recorte definida para la estructura.

Si un consumidor falla antes de confirmar, el mensaje continuará como pendiente. Una versión posterior podrá incorporar una política de recuperación y reasignación de estas entradas.

#### 3.5.7 Control de idempotencia

La solución adoptará una semántica de entrega al menos una vez. Por esta razón, un mensaje podría recibirse nuevamente después de ciertos fallos o reintentos.

Para reducir los efectos de estas repeticiones, cada operación incluirá una clave de idempotencia. El broker comprobará dicha clave antes de continuar con el procesamiento.

Las claves se conservarán temporalmente en Redis. Cada registro tendrá un tiempo de vida configurable para evitar un crecimiento indefinido de la memoria.

La comprobación deberá realizarse mediante una escritura condicional y atómica. Si la clave no existe, se registrará y el procesamiento podrá continuar. Si ya existe, el mensaje se tratará como una repetición.

El tiempo de expiración deberá definirse según la ventana de reintentos esperada. Un periodo demasiado corto podría permitir duplicados tardíos. Un periodo demasiado largo aumentaría el consumo de memoria.

Este mecanismo permitirá controlar repeticiones dentro del broker. Sin embargo, no garantizará por sí mismo que una operación externa se ejecute exactamente una vez.

#### 3.5.8 Política de retención

Los mensajes no se conservarán de forma indefinida. La primera versión utilizará una política de recorte basada en el tamaño o la antigüedad del stream.

La política deberá considerar el volumen estimado de mensajes, el tiempo necesario para su procesamiento y la memoria disponible. También deberá evitar que el stream crezca sin control.

El TTL se utilizará principalmente para las claves de idempotencia. En el caso de Redis Streams, la retención se gestionará mediante una política de recorte del flujo.

#### 3.5.9 Limitaciones de la propuesta

La disponibilidad de la capa dependerá de la instancia de Redis. La primera versión no incluirá replicación, Redis Sentinel ni Redis Cluster.

Tampoco se garantizará un orden global entre todos los consumidores. Redis mantendrá el orden de las entradas dentro del stream, pero la ejecución concurrente podrá alterar el orden de finalización.

La persistencia se limitará a los mensajes asíncronos. La comunicación en tiempo real mediante streaming no almacenará automáticamente los mensajes enviados.

Estas limitaciones deberán considerarse durante las pruebas. También permitirán identificar posibles líneas de evolución para versiones posteriores.

#### 3.5.10 Diagrama de la capa de persistencia

La Figura 1 representa la relación entre el broker y la capa de persistencia prevista. Los productores publican los mensajes mediante gRPC. El broker debe validar la solicitud y utilizar el puerto de persistencia para almacenarla en Redis Streams.

Los consumidores solicitan mensajes mediante el modelo pull. Redis mantiene el estado de las entregas dentro del grupo de consumidores. Después del procesamiento, el consumidor envía la confirmación correspondiente.

La figura también diferencia el almacenamiento de mensajes y el registro de claves de idempotencia. De esta manera, ambas responsabilidades permanecen separadas dentro de la capa de infraestructura. La Figura 1 presenta de forma visual los principales componentes y relaciones de la capa de persistencia:

**Figura 1**

*Diagrama de componentes de la capa de persistencia basada en Redis* 

![Diagrama de componentes de la capa de persistencia basada en Redis](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%201.png>)

_Nota._ Elaboración propia mediante Figma. La figura separa los flujos de almacenamiento de mensajes y de control de idempotencia, así como sus puertos y adaptadores.

### 3.6 Diagramas UML

#### Contexto general del sistema

La arquitectura ubica Dominus Broker dentro del ecosistema completo. El broker recibe mensajes desde servicios productores, los distribuye a consumidores o suscriptores y utiliza Redis sería usado como soporte de persistencia temporal. El SDK y el repositorio de contratos Protobuf reducen el acoplamiento entre clientes y servidores. La Figura 2 aporta una vista de contexto que permite identificar las dependencias externas y los canales de comunicación del sistema.

**Figura 2**

*Contexto general de Dominus Broker* 

![Contexto general de Dominus Broker](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%202.png>)

_Nota._ Elaboración propia. La figura sitúa al SDK, al broker, a los contratos Protobuf, a Redis, a Prometheus y a los servicios suscriptores dentro del ecosistema.

Este diagrama muestra una vista de la separación de la arquitectura conceptual en nuestra implementación interna. Se demuestra claramente que los contratos de Protobuf nos va a generar los tipos y servicios , nos va apoyar con la interfaces para el servicio principal que es Dominus Broker. El servicio productor y el servicio consumidor ambos van a utilizar el Dominus SDK mediante una conexión de GRPC. Dominus Broker por sí mismo utilizará redis streams, redis idempotencia Y para las métricas y salud esta estaría utilizando prometheus y monitor http. Por último para asegurarnos de que este sea un servicio de suscriptor en tiempo real estaremos utilizando el streaming propiamente de GRPC.

> [!attention] Corregir el párrafo de interpretación de la Figura 2
> El texto mezcla futuro y presente, contiene errores de concordancia y repite lo que ya muestra el diagrama. Conviene conservar solo las relaciones que no sean evidentes en la figura y normalizar `gRPC`, `Redis Streams`, `Prometheus` y `monitor HTTP`.

#### Secuencia de cola asíncrona con Producer, Consumer y Ack

La Figura 3 representa la cara asíncrona de la solución. El productor guarda un mensaje en Redis Streams. El consumidor lo solicita mediante un modelo pull y confirma el procesamiento con Ack.

**Figura 3**

*Secuencia asíncrona de Producer, Consumer y Ack* 

![Secuencia asíncrona de Producer, Consumer y Ack](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%203.png>)

_Nota._ Elaboración propia. La figura muestra el recorrido del mensaje entre los actores, el SDK, SqsAPI, el caso de uso y Redis Streams hasta su confirmación.

#### Diagrama de clases del dominio y casos de uso

El modelo de clases se centra en las entidades, puertos y servicios de aplicación que aparecen en el broker actual. La entidad Message mantiene el identificador, el payload y la fecha de creación. Los puertos abstraen Redis y las conexiones gRPC de salida. Dado que la información que guarda el mensaje es la puerta de entrada o la parte principal entre la mayoría de los casos de usos y clases que tenemos dentro de El dominio.

##### Broker / gRPC Streaming

La Figura 4 permite relacionar el caso de uso del broker con el puerto de salida gRPC y con la entidad `Message`, lo que complementa la explicación del flujo en tiempo real.

**Figura 4**

*Diagrama de clases del flujo gRPC de Broker* 

![Diagrama de clases del flujo gRPC de Broker](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%204.png>)

_Nota._ Elaboración propia. La figura presenta las operaciones de streaming del caso de uso, la interfaz `BrokerClient`, su adaptador de salida y la entidad `Message`.

Este diagrama representa la comunicación en tiempo real entre servicios. Todos estamos utilizando la clase mensaje para enviar y recibir información el mensaje es el objeto que contiene la información de que se transmite en general va a tener el contenido del mensaje un identificador y la fecha de creación. En otras palabras termina siendo el paquete de datos que viaja entre los servicios.

Luego tenemos la interfaz de broker cliente, esto define cómo debe comunicarse cualquier cliente de al broker. No contiene la implementación solamente establece los métodos que deben de existir Como por ejemplo

- ClientStream()
- ServerStream()
- BidirectionalStream()

En el Broker Use Case está la lógica de negocio relacionada con el broker.

Recibe las solicitudes y decide:

- abrir un stream,
- enviar mensajes,
- recibir respuestas,
- mantener una conexión bidireccional.

##### SQS / Message Management

Este diagrama representa el almacenamiento y procesamiento de los mensajes aquí directamente nos envían los mensajes a la red pero realmente se administran. Proviene la mayoría desde SQSUseCase que vas directamente a MemoryClient CheckerClient Message. La Figura 5 aporta la relación de clases necesaria para distinguir el almacenamiento de mensajes del control de consumidores e idempotencia.

**Figura 5**

*Diagrama de clases de SqsAPI y la gestión de mensajes* 

![Diagrama de clases de SqsAPI y la gestión de mensajes](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%205.png>)

_Nota._ Elaboración propia. La figura vincula `SqsUseCase` con las interfaces de memoria y verificación, sus adaptadores Redis y la entidad `Message`.

El memory client define como interactuar con el almacenamiento de mensajes. Esto va a permitir guardar los mensajes y obtener los mensajes confirmar que fueron procesados mediante ACK trabajar en grupos de mensajes. Hacer una clase realmente no importa si el almacenamiento termina siendo en redis memoria o cualquier otro sistema pero tener este funcionamiento nos ayuda a manejar si tenemos algún cambio.

Luego tenemos revisar el cliente que se utiliza para llevar el control de los consumidores. Se va a hacer mediante qué vayamos a registrar un consumidor o verificar si el consumidor ya existe.Usando los dos métodos que tenemos definidos como Save Consumer y check consumer. ¿Y por qué hacer esto teniendo estos dos métodos? Porque estos van a ayudar a evitar tener duplicados o Y mantener el estado de los consumidores lo más mínimo posible.

Por último tenemos SQS y use case que contiene la luz Física principal relacionada con la cola. El producir mensajes y consumir mensajes mediante ack cuando un mensaje fue procesado Correctamente,terminará haciéndolo el coordinador en todo el proceso.

Este primer diagrama en esta sección realmente responde a la pregunta de cómo viajan los mensajes entre los servicios mientras que nuestro segundo nos ayuda a definir cómo vamos a almacenar recuperar y controlar estos mensajes juntos.

#### Secuencia de fan-out en tiempo real

El siguiente diagrama es un flujo representativo del envío de un mensaje desde el productor hacia Varios suscriptores utilizando el patrón de fan in fan out Específicamente la secuencia de fan out utilizando Grpc Streaming. El broker válida la solicitud vamos a obtener una lista de suscriptores y delegar la distribución del cliente Grpc de salida. La Figura 6 permite seguir la distribución concurrente del mismo payload hacia dos suscriptores.

**Figura 6**

*Secuencia de fan-out en tiempo real mediante gRPC Streaming* 

![Secuencia de fan-out en tiempo real mediante gRPC Streaming](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%206.png>)

_Nota._ Elaboración propia. La figura detalla la validación de suscriptores, la apertura de conexiones y el envío paralelo del payload desde el productor hasta los suscriptores.

El primer paso que tenemos pensado en nuestro proceso de Broker en tiempo real es que el productor envía el primer mensaje al SDK. El productor es quien estaría enviando el payload más aparte estaría enviando quienes son los suscriptores. El SDK luego va a abrir el stream al broker API Mediante GRPC con clientStreaming. Luego el programa recibe el stream y lo pasa a nuestro propio broker de useCase que se encarga de aceptar los mensajes. Después de verificar que los suscriptores realmente existen si alguno No existe puede devolver un error. Una Vez que creamos las conexiones hacia los suscriptores Estas conexiones también van a permanecer abiertas y empieza la parte bonita, que arranca un ciclo El productor. Es ahí entonces donde empezará a enviar un payload de lo que realmente quiere mandar el SDK se lo manda al broker el el broker API entrega el mensaje. Después el propio useCase envía el mensaje envía este payload a todos los suscriptores y una vez que siga pasando concurrentemente aparecería el bloque de parar que significa que las operaciones ya terminaron . En ese momento es cuando se va a estar haciendo el envío Y luego esperar y ver quién lo recibe. Cuando yo no hay mensajes que enviar el mismo productor termina y el CSDK cierra el string El stream manda un mensaje de OK ya terminé.

#### Estados del mensaje asíncrono

Como bien lo mencionamos anteriormente el mensaje termina siendo la fuente o la espalda principal de este proyecto. El mensaje asíncrono cambia de Estado dependiendo desde qué se produce hasta que se confirma Lo siguiente es una vista que permite discutir los errores los reintentos. Y como el mensaje basta cambiar de distintos Estados como pendientes etcétera. La Figura 7 aporta una representación del ciclo de vida que facilita relacionar cada estado con la operación que provoca la transición.

**Figura 7**

*Estados del ciclo de vida del mensaje asíncrono* 

![Estados del ciclo de vida del mensaje asíncrono](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%207.png>)

_Nota._ Elaboración propia. La figura representa las transiciones desde la creación y validación hasta la confirmación, el rechazo o el reintento del mensaje.

Cuando una aplicación genera un mensaje, este ya existe, pero todavía no ha sido revisado ni almacenado. Por ello, inicialmente se le asigna el estado Creado.

Posteriormente, el sistema verifica que el mensaje sea válido. Por ejemplo, revisa que contenga información, que no esté vacío y que tenga el formato esperado. Si todas las validaciones son correctas, el proceso continúa y el mensaje pasa al estado Validado.

Una vez que el sistema guarda el mensaje en Redis Streams mediante el comando XADD, este queda almacenado de forma persistente. Redis Streams funciona como una bandeja de entrada donde los mensajes permanecen almacenados para evitar que se pierdan. A partir de este momento, como el mensaje ya no depende de la memoria de la aplicación, se le asigna el estado Persistido.

En una fase posterior del proyecto, cuando el mensaje ya está listo para que algún consumidor lo procese, pero todavía nadie lo ha tomado, se le asigna el estado Disponible. Es similar a un paquete que ya se encuentra preparado en un almacén, esperando a que un repartidor lo recoja.

Cuando un consumidor utiliza XREADGROUP para leer el mensaje, este queda asignado a un trabajador para su procesamiento. En ese momento, el mensaje cambia al estado Entregado.

Una vez que el trabajador recibe el mensaje y comienza a procesarlo, el sistema aún no puede dar el proceso por concluido. En esta etapa se encuentra Pendiente, ya que está esperando la confirmación de que el procesamiento finalizó correctamente.

Cuando el procesamiento termina de forma exitosa, el trabajador envía la confirmación correspondiente y el sistema ejecuta el comando XACK para eliminar el mensaje de la lista de pendientes. En este punto, el ciclo de vida del mensaje concluye satisfactoriamente y el sistema queda listo para procesar nuevos mensajes.

Sin embargo, surge una pregunta: ¿qué ocurre si se presenta un error? Por ejemplo, si el trabajador se cierra inesperadamente, falla la aplicación, se pierde la conexión de red o el servidor deja de responder. En estos casos, el mensaje no se pierde; simplemente permanece en estado pendiente para ser reclamado y procesado nuevamente mediante un reintento.

Finalmente, existe otro escenario posible. Si durante la etapa de validación el mensaje no cumple con el formato esperado o carece de la información necesaria, nunca será almacenado en Redis Streams. En consecuencia, el proceso finaliza inmediatamente y al mensaje se le asigna el estado Rechazado.

#### Actividad de idempotencia

Por otra parte, lo central de este proyecto es la idempotencia. Gracias A que esto es algo que nos va a reducir el riesgo de procesar dos veces la misma operación. La Figura 8 aporta la secuencia de decisiones que precede a la ejecución del caso de uso y permite ubicar el punto de reserva de la clave en Redis.

**Figura 8**

*Flujo de validación e idempotencia de una llamada gRPC* 

![Flujo de validación e idempotencia de una llamada gRPC](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%208.png>)

_Nota._ Elaboración propia. La figura muestra la autenticación, la validación de la clave, su reserva con `SET NX` y TTL, y las respuestas posibles del caso de uso.

> [!danger] Distinguir el diseño previsto de la implementación evaluada
> Esta figura describe una reserva atómica con `SET NX`, pero el hallazgo BE-03 de la sección 4.2.4 indica que la implementación comprobada separa la consulta y el guardado asíncrono, por lo que acepta duplicados bajo concurrencia. Debe aclararse si la figura representa el diseño objetivo o el código ejecutado.

Este es el flujo completo que sigue una petición gRPC. Antes de ejecutar la lógica del broker, nuestro objetivo es asegurarnos de que la solicitud sea válida y que no vaya a procesarse más de una vez.

El proceso comienza cuando un cliente, por ejemplo una aplicación o un servicio, envía una solicitud a nuestro servidor. En este punto todavía no se ejecuta la lógica de negocio; la solicitud permanece en espera mientras se realizan las validaciones correspondientes.

Lo primero que hace el servidor es verificar que el token de autenticación sea válido, con el fin de comprobar que el cliente está autorizado para utilizar el servicio. Si el token es inválido, la solicitud se rechaza inmediatamente y el proceso termina.

Si el token es válido, el servidor continúa verificando si la solicitud incluye una Idempotency Key.

Una Idempotency Key es un identificador único asociado a una operación. Por ejemplo:

```text
Idempotency-Key: 4f8d9f21-7d43-4d2f
```

Cada operación debe contar con una clave diferente.

¿Para qué sirve esta clave? Su función es evitar que una misma operación sea procesada varias veces. Esto puede ocurrir, por ejemplo, cuando un cliente reenvía una solicitud debido a un problema de red o porque no recibió respuesta del servidor. Gracias a la Idempotency Key, el servidor puede identificar que esa operación ya fue recibida anteriormente y evitar que se ejecute nuevamente.

Si el cliente no envía esta clave, la solicitud es rechazada.

Cuando la clave está presente, el servidor intenta registrarla en Redis utilizando una operación atómica. Redis responde indicando si la clave pudo reservarse o no.

- Si la reserva es exitosa, significa que es la primera vez que se procesa esa operación, por lo que el flujo continúa y se ejecuta la lógica de negocio.
- Si la reserva falla, significa que esa clave ya existe y, por lo tanto, la operación ya fue enviada o incluso se encuentra en proceso. En este caso, el servidor finaliza la petición sin volver a ejecutar la lógica de negocio, evitando así operaciones duplicadas.

Finalmente, una vez que se ejecuta la lógica de negocio, el sistema verifica el resultado de la operación. Si el procesamiento fue exitoso, se devuelve una respuesta de OK al cliente y el flujo concluye correctamente. En caso de que ocurra algún error, la operación podrá reintentarse utilizando la misma Idempotency Key, lo que permitirá al servidor reconocer la solicitud y garantizar que no se procese más de una vez.

# 4. Desarrollo específico de la contribución (TBD)

> [!danger] Contenido de plantilla pendiente de sustituir
> Los párrafos iniciales de 4.1 todavía son instrucciones de la plantilla y no describen la contribución realizada. Antes de entregar el TFM deben reemplazarse por el desarrollo real: requisitos, decisiones de diseño, proceso de implementación, producto obtenido y evaluación.

**TBD:** En este apartado debes desarrollar la **descripción** de tu **contribución.** Esto depende del tipo de trabajo concreto y puedes contar con la ayuda de tu director para estudiar cómo comunicar los detalles de tu contribución. A continuación, te presentamos la estructura habitual para cada uno de los tipos de trabajo, aunque suele ser común desarrollar los apartados en función de las fases o actividades que se hayan establecido en la metodología de trabajo.

## 4.1. Desarrollo práctico

En este tipo de trabajo es importante **justificar** los criterios de diseño empleados para desarrollar el software, seguido de la **descripción detallada** del producto resultante y finalizando con una **evaluación** de la **calidad** y **aplicabilidad** del producto. Esto suele verse reflejado en la siguiente estructura de subapartados.

Identificación de requisitos

En este apartado se debe indicar el trabajo previo realizado para guiar el desarrollo del software. Esto debería incluir la identificación adecuada del problema a tratar, así como del contexto habitual de uso (empresa, institución, etc.). Idealmente, la identificación de requisitos se debería hacer contando con expertos en la materia a tratar. Además, deberás describir en detalle las características del sistema. Como mínimo querrás mencionar:

- Qué tecnologías se utilizaron (incluyendo justificación de por qué se emplearon y descripciones detalladas de las mismas).
- Cómo se organizó el desarrollo.
- Qué personas participaron (con datos demográficos, si procede) o qué técnicas de sistemas se emplearon.
- Cómo transcurrió el desarrollo.
- Qué instrumentos de seguimiento y evaluación se utilizaron durante el proceso de desarrollo.

Descripción del sistema software desarrollado

En el caso de un desarrollo práctico, deberían aportarse detalles del proceso de desarrollo, incluyendo las fases e hitos del proceso. También deben presentarse diagramas explicativos de la arquitectura o funcionamiento, así como capturas de pantalla que permitan al lector entender el funcionamiento del programa.

Evaluación

Este apartado debería cubrir por lo menos una mínima evaluación de la usabilidad de la herramienta, así como de su aplicabilidad para resolver el problema propuesto. Estas evaluaciones suelen realizarse con usuarios expertos.

## 4.2. Pruebas de Herramientas

### 4.2.1 Pruebas Unitarias

Las pruebas unitarias se enfocaron en validar los principales casos de uso del broker antes de ejecutar pruebas de integración o pruebas de rendimiento. En esta parte no se buscó levantar todo el ecosistema completo, sino comprobar que la lógica principal respondiera correctamente y de forma aislada de acuerdo con las herramientas empleadas.

Para evitar mezclar alcances, las pruebas se documentan tomando como referencia la forma en que fueron organizadas dentro del proyecto. En la copia evaluada, los casos unitarios se concentraron en el directorio tests/units, mientras que las pruebas que involucran infraestructura, comunicación real o servicios externos se ubicaron en tests/integration. Esta organización permite diferenciar las pruebas unitarias de las pruebas de integración. Para este apartado se consideran únicamente las pruebas enfocadas en los casos de uso y sus contratos principales, ya que su objetivo es comprobar el comportamiento del código sin depender directamente de Redis, Docker, Grafana o herramientas de carga.

Las pruebas fueron desarrolladas con el framework nativo de Go, mediante el paquete testing. Además, se utilizaron mocks y dobles de prueba para simular dependencias como clientes de memoria, clientes de comunicación y objetos de transferencia de datos. Esto permitió validar la lógica de aplicación sin requerir la ejecución completa de la infraestructura.

La ejecución general de las pruebas se realizó con el siguiente comando:

```text
go test -count=1 -v ./tests/units/...
```

El parámetro -count=1 evitó reutilizar resultados almacenados en caché, obligando a ejecutar nuevamente las pruebas. El parámetro **-v** permitió obtener una salida detallada de los casos y subcasos ejecutados. La salida fue almacenada en el archivo unit-tests.log, el cual permitió confirmar el número de pruebas ejecutadas y su resultado.

A partir de la salida generada, se identificaron **143 pruebas y sub-pruebas unitarias ejecutadas**. Todas finalizaron con estado PASS, por lo que la ejecución general se consideró satisfactoria.

Como evidencia de la ejecución, la Figura 9 muestra la salida obtenida en PowerShell después de ejecutar las pruebas unitarias y contar los casos reportados en el archivo unit-tests.log. De forma complementaria, la Figura 10 muestra el conteo de pruebas con estado PASS y la búsqueda de posibles resultados fallidos dentro del mismo archivo. Ambas capturas vinculan los resultados cuantitativos con la evidencia generada por la ejecución.

**Figura 9**

*Ejecución y conteo de pruebas unitarias* 

![Ejecución y conteo de pruebas unitarias](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%209.png>)

_Nota._ Elaboración propia a partir de la ejecución de pruebas unitarias del proyecto. La captura muestra casos con resultado `PASS` y el conteo de 143 pruebas y subpruebas.

Como evidencia complementaria, la Figura 10 presenta el conteo de resultados aprobados y la comprobación de que no se registraron resultados `FAIL`.

**Figura 10**

*Conteo de pruebas unitarias aprobadas y verificación de fallos* 

![Conteo de pruebas unitarias aprobadas y verificación de fallos](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%2010.png>)

_Nota._ Elaboración propia a partir de la ejecución de pruebas unitarias del proyecto. La captura presenta el conteo de resultados `PASS` y la consulta utilizada para buscar resultados `FAIL`.

Para la medición de cobertura se utilizó el objetivo definido en el archivo de automatización del proyecto:

```text
.\Makefile.ps1 -Target test-cover
```

Este comando genera el archivo coverage.out y permite obtener el porcentaje de cobertura mediante:

```text
go tool cover -func coverage.out
```

De acuerdo con el reporte de cobertura del proyecto, la cobertura global instrumentada fue de **91.8 %** sobre sentencias. Además, los casos de uso principales del broker y los casos asíncronos **Producer**, **Consumer**, **Ack** y **NewSqs** alcanzaron una cobertura del **100 %**.

La Tabla 3 resume los módulos considerados dentro de las pruebas unitarias, el código evaluado y el resultado obtenido en cada caso; así permite relacionar la cobertura reportada con los flujos principales del broker.

**Tabla 3**

*Módulos incluidos en las pruebas unitarias* 

|**Módulo de prueba**|**Código evaluado**|**Objetivo principal**|**Resultado**|
|---|---|---|---|
|producer_test|Caso de uso Producer|Validar la publicación de mensajes, la construcción de la entidad y el rechazo de payload vacío|PASS|
|consumer_test|Caso de uso Consumer|Comprobar la recuperación de mensajes mediante el puerto de memoria y la respuesta esperada al consumidor|PASS|
|ack_test|Caso de uso Ack|Validar la confirmación de mensajes y el rechazo de identificadores con formato inválido|PASS|
|stream_client_test|Caso de uso StreamClientConn|Comprobar el flujo de envío desde el cliente hacia el broker y su posterior distribución|PASS|
|stream_server_test|Caso de uso StreamServerConn|Validar la entrega de mensajes desde el broker hacia el cliente mediante streaming de servidor|PASS|
|stream_bidirectional_test|Caso de uso StreamBiConn|Comprobar el intercambio simultáneo de mensajes entre cliente, broker y suscriptores|PASS|

_Nota._ Elaboración propia a partir de la documentación técnica y los resultados de cobertura del proyecto. La tabla identifica el módulo, el caso de uso, el objetivo validado y el resultado de cada grupo de pruebas.

> [!question] Trazabilidad de la evidencia
> Conviene registrar el commit, la fecha, la versión de Go y el entorno en el que se obtuvieron las 143 pruebas y el 91,8 % de cobertura. Sin esos datos, otra persona no puede reproducir con precisión el resultado.

En el flujo asíncrono se probaron los casos de uso **Producer**, **Consumer** y **Ack**. Estas pruebas revisaron que el productor no estuviera enviando mensajes vacíos, también que el consumidor pudiera recuperar mensajes desde el puerto correspondiente y la confirmación se realice únicamente cuando el identificador del mensaje tenga un formato válido.

En el flujo de comunicación en tiempo real se probaron los casos StreamClientConn, StreamServerConn y StreamBiConn. Estos módulos nos permitieron revisar los tres escenarios principales de streaming: envío desde cliente, envío desde servidor e intercambio bidireccional.

De acuerdo con el reporte de cobertura, los casos de uso del broker StreamClientConn, StreamServerConn, StreamBiConn y NewBroker alcanzaron una cobertura del 100 %. De igual forma, los casos de uso asíncronos **Producer**, **Consumer**, **Ack** y **NewSqs** también alcanzaron una cobertura del 100 %. Estos datos coinciden con el reporte de cobertura, donde se indica que los casos de uso principales del broker y los casos SQS alcanzaron cobertura completa.

La cobertura global instrumentada fue de **91.8 %** sobre sentencias. Este porcentaje considera código de aplicación, dominio e infraestructura dentro del alcance definido para la medición. No se incluyeron en este cálculo los paquetes de arranque, configuración principal, ejecutables ni mocks generados.

Los resultados muestran que los flujos principales del broker fueron validados satisfactoriamente a nivel unitario. En particular, se comprobó que los mensajes pueden publicarse, consumirse y confirmarse desde los casos de uso correspondientes, y que los flujos de streaming responden a los escenarios definidos en nuestro planteamiento inicial.

Con base en los resultados obtenidos, el criterio de aceptación para esta etapa se cumplió: la corrida finalizó sin resultados FAIL, el conteo de pruebas superadas coincidió con el número de pruebas y subpruebas ejecutadas, y los casos de uso principales alcanzaron cobertura completa dentro del reporte generado.

Esto nos permite concluir que la lógica principal del broker fue validada satisfactoriamente a nivel unitario. Sin embargo, el alcance de esta sección se limita a la validación aislada del código. La interacción real entre componentes, el uso de Redis, la ejecución contenerizada y el comportamiento bajo carga se documentan en las secciones posteriores.

### 4.2.2 Pruebas de Integración

Las pruebas de integración validan que los distintos componentes del proyecto funcionan correctamente (capa gRPC de entrada, casos de uso de aplicación y repositorio Redis) cuando se conectan entre ellas. Se implementaron en Go usando paquete de testing estándar, junto las siguientes bibliotecas auxiliares:

- miniredis/v2**:** que simula un servidor de Redis, sin necesidad de infraestructura real.
- google.golang.org/grpc/test/bufconn**:** este crea una conexión gRPC en memoria, evitando abrir sockets de red reales.
- go.uber.org/mock/gomock**:** que genera mocks controlados para las dependencias de Event y clientes gRPC salientes.
- go.opentelemetry.io/contrib/otrlgrpc**:** esta añade trazabilidad a los flujos de streaming bajo prueba.

A continuación se detallan tres pruebas de integración, estas fueron seleccionadas ya que cubren cada patrón soportado por el broker propuesto, las cuales son: escritura de mensajes (Producer), el ciclo completo de mensajería confiable (Consumer + ack) y streaming bidireccional con múltiples suscriptores.

#### Prueba 1: TestProducerFlow (Producer end-to-end via gRPC)

**Componentes integrados:** capa gRPC de entrada (BrokerSqs), caso de uso Producer y repositorio Redis (cmemory sobre miniredis).

**Objetivo de la prueba:** verificar que un mensaje enviado por gRPC atraviesa el caso de uso Producer y queda registrado en Redis Stream, con el identificador y el cuerpo esperado.

**Flujo:** la prueba levanta un servidor gRPC en memoria con el handler BrokerSqs y llama al Producer con un payload de prueba. Seguidamente inspecciona directamente el Redis Stream con miniredis esto para confirmar que ya existe una entrada, que el campo payload puede deserializar.

**Resultado:** PASS. Status 0, 1 entrada en el stream, cuerpo e identificador verificados correctamente.

#### Prueba 2: TestAckFlow (Ack end-to-end via gRPC after Consumer)

**Componentes integrados:** cada gRPC de entrada (BrokerSqs), casos de uso Consumer y Ack y repositorio Redis (cmemory sobre miniredis).

**Objetivo de la prueba:** verificar el ciclo completo de confirmación de un mensaje (producir, consumir y confirmar mediante el Ack), para comprobar que, después del Ack, el mensaje deja de aparecer como pendiente para el grupo de consumidores. Esta es la prueba más completa, ya que integra los tres casos de uso principales del flujo de mensajería estilo SQS.

**Flujo:** Se inserta un mensaje en el stream y se crea el grupo de consumidores; el cliente llama al consumidor (el mensaje queda en estado pendiente para el grupo) y luego llama a Ack con el identificador del mensaje devuelto. Concluyendo, se consulta Redis con XPendingExt para confirmar que el mensaje ya no está en la lista de mensajes pendientes.

**Resultado:** PASS. El identificador del mensaje del Ack coincide con el del consumo, y XPendingExt devuelve una lista vacía para ese identificador después de la confirmación.

#### Prueba 3: TestBidirectionalStreamFlow

**Componentes integrados:** capa gRPC de entrada, caso de uso BidirectionalStream, middleware de autenticación (ApiToken) y cliente gRPC saliente (GrpClient).

**Objetivo de la prueba:** verificar que el broker retransmita mensajes bidireccionales a múltiples suscriptores de forma simultánea, integrando autenticación, compresión gzip, trazabilidad con OpenTelemetry y enrutamiento hacia pares gRPC reales sobre TCP. Este es el escenario más exigente.

**Flujo:** se levantan 2 servidores TCP que actúan como suscriptores en modo eco. El servidor principal, sobre bufconn, se conecta mediante outbound.GrpClient con autenticación, gzip y OpenTelemetry. El cliente envía 2 mensajes y se esperan 4 respuestas , verificando que cada payload aparece exactamente 2 veces.

**Resultado:** PASS. Se escriben 4 respuestas esperadas.

#### Resumen de los resultados

La Tabla 4 resume las tres pruebas de integración detalladas junto con su resultado final y permite comprobar que los patrones asíncrono y bidireccional cuentan con evidencia específica.

**Tabla 4**

*Resultados de las pruebas de integración* 

|**Prueba**|**Función de prueba**|**Componente principal**|**Resultado**|
|---|---|---|---|
|broker_sqs_flow_test|TestProducerFlow|Producer|PASS|
|broker_sqs_flow_test|TestAckFlow|Consumer + Ack|PASS|
|broker_stream_flow_test|TestBidirectionalStreamFlow|Streaming bidireccional|PASS|

_Nota._ Elaboración propia a partir de la documentación técnica y la ejecución de las pruebas de integración. La tabla vincula cada archivo y función de prueba con el componente principal validado y su resultado.

Las tres pruebas de integración pasaron exitosamente, sin fallos ni condiciones de carrera detectadas por el detector de "race" de Go. La Figura 11 aporta la salida de consola del flujo SQS.

**Figura 11**

*Ejecución de pruebas de integración del flujo SQS* 

![Ejecución de pruebas de integración del flujo SQS](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%2011.png>)

_Nota._ Elaboración propia a partir de la ejecución de `go test ./tests/integration/broker_sqs_flow_test -v`. La captura muestra los resultados de `TestAckFlow`, `TestConsumerFlow` y `TestProducerFlow`.

De manera complementaria, la Figura 12 documenta la salida de consola del flujo de streaming gRPC.

**Figura 12**

*Ejecución de pruebas de integración del flujo de streaming gRPC* 

![Ejecución de pruebas de integración del flujo de streaming gRPC](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%2012.png>)

_Nota._ Elaboración propia a partir de la ejecución de `go test ./tests/integration/broker_stream_flow_test -v`. La captura muestra la aprobación de los flujos bidireccional, de cliente y de servidor.

### 4.2.3 Usabilidad del software

La evaluación de usabilidad se realizó considerando la naturaleza técnica de la herramienta. A diferencia de una aplicación orientada a usuarios finales con interfaz gráfica, esta herramienta es un broker de mensajería dirigido principalmente a desarrolladores, integradores y equipos técnicos que necesitan comunicar servicios mediante gRPC, Protocol Buffers y Redis Streams. Por esta razón, la usabilidad no se evaluó en términos visuales, como colores, botones o disposición de pantallas, sino desde la facilidad con la que un usuario técnico puede comprender, configurar, ejecutar y utilizar las operaciones principales del sistema.

#### Metodología utilizada para medir la usabilidad del software

La metodología empleada combinó una evaluación heurística técnica con pruebas basadas en tareas. La evaluación heurística permitió revisar aspectos como claridad de la documentación, consistencia de nombres, facilidad de configuración, disponibilidad de ejemplos, comprensión del flujo principal y apoyo para diagnosticar errores. Por otro lado, las pruebas basadas en tareas permitieron comprobar si un usuario técnico podía realizar actividades representativas del uso real de la herramienta, como preparar el entorno, ejecutar pruebas, identificar los servicios gRPC disponibles, producir mensajes, consumirlos y confirmar su procesamiento mediante ACK.

El perfil de usuario considerado para esta evaluación fue el de un desarrollador con conocimientos básicos de backend, ejecución de proyectos desde terminal y uso de herramientas de desarrollo. No se asumió un dominio avanzado de gRPC, Redis Streams o arquitectura orientada a eventos, ya que parte del objetivo de la prueba fue identificar si la documentación y la organización del proyecto permiten comprender estos elementos durante la puesta en marcha. Este enfoque resulta adecuado porque el software no está diseñado para un usuario administrativo o cliente final, está diseñado para usuarios técnicos que integran servicios distribuidos.

#### Objetivos

Los objetivos principales de la evaluación fueron:

- Comprobar si el proceso de instalación y ejecución del proyecto puede seguirse a partir de la documentación disponible
- Validar si la estructura del repositorio permite ubicar los componentes principales
- Identificar si los contratos definidos mediante Protocol Buffers son comprensibles
- Verificar si el flujo productor-consumidor-ACK puede entenderse y ejecutarse
- Revisar si las pruebas existentes ayudan a comprender el comportamiento esperado del broker
- Analizar si los mensajes de error, logs o salidas de consola permiten diagnosticar problemas durante la ejecución.

#### Evaluación de la usabilidad

Para realizar la evaluación se revisó la estructura general del código y la documentación incluida, se agregó la herramienta a otro sistema para iniciar el proceso de ambientación desde cero. En esta revisión se identificaron los módulos principales del proyecto: el broker, la definición de contratos Protobuf, el SDK y los ejemplos de consumidor. Esta separación facilita comprender que el sistema no corresponde a una aplicación monolítica, sino a una solución distribuida compuesta por varios elementos que colaboran entre sí.

La primera tarea evaluada consistió en preparar el entorno de ejecución. En esta etapa se revisó si la documentación permitía identificar los requisitos necesarios, las dependencias del proyecto y los comandos requeridos para montar el entorno local. El objetivo de esta tarea fue medir la facilidad con la que un usuario técnico puede pasar del repositorio descargado a un entorno listo para ejecutar pruebas. Como resultado, se observó que el proyecto cuenta con documentación y pruebas previamente organizadas, lo cual facilita el arranque. Sin embargo, también se identificó que la curva inicial puede ser alta para usuarios que no estén familiarizados con Go, Redis, gRPC o ejecución de servicios desde terminal.

La segunda tarea consistió en replicar las pruebas proporcionadas en el repositorio. Esta tarea permitió comprobar si las instrucciones disponibles eran suficientes para ejecutar los casos de prueba en este caso ya preparados. El resultado fue positivo, ya que fue posible montar el entorno y replicar las pruebas documentadas. Esto representa un punto favorable de usabilidad técnica, porque las pruebas no solo sirven para validar el funcionamiento del software, sino también como guía práctica para entender los flujos principales del sistema. Al observar las pruebas, el usuario puede identificar qué componentes intervienen y qué comportamiento se espera de cada operación.

La tercera tarea evaluada fue la comprensión del flujo productor-consumidor-ACK. Este flujo es uno de los elementos centrales del proyecto, ya que representa la comunicación asíncrona tipo cola. En este escenario, un productor envía un mensaje al broker, un consumidor lo solicita cuando está listo para procesarlo y posteriormente se confirma el procesamiento mediante una operación de ACK. Desde el punto de vista de usabilidad, este flujo resulta comprensible cuando se observa como una secuencia de tres pasos. No obstante, puede resultar confuso si el usuario no conoce previamente los conceptos de broker, cola o consumidor.

La cuarta tarea consistió en revisar el contrato gRPC definido mediante Protocol Buffers. Esta revisión permitió verificar si el usuario puede identificar las operaciones disponibles y la forma en que se comunican los clientes con el broker. El uso de archivos `.proto` mejora la claridad técnica porque define de forma explícita los servicios, métodos, mensajes de entrada y respuestas esperadas. Esto reduce ambigüedades al momento de integrar otros sistemas. Sin embargo, para usuarios sin experiencia previa en gRPC, la lectura del contrato puede no ser suficiente. Por ello, resulta recomendable acompañar el contrato con ejemplos mínimos de uso y diagramas de flujo.

La quinta tarea se orientó a revisar los mecanismos de diagnóstico disponibles durante la ejecución. En una herramienta backend, la usabilidad depende en gran medida de que el usuario pueda saber si el sistema se ejecutó correctamente, si Redis está disponible, si el broker respondió y si las pruebas fallaron por un error del código o por un problema de configuración. En este sentido, los logs, salidas de consola, endpoints de salud y documentación de pruebas son elementos importantes para reducir el tiempo de diagnóstico.

#### Resultados de la usabilidad del software

Los resultados generales muestran que la herramienta tiene una usabilidad adecuada para un prototipo académico orientado a usuarios técnicos. La organización por módulos, la existencia de documentación y la disponibilidad de pruebas permiten comprender progresivamente el propósito del sistema. Además, la posibilidad de replicar pruebas ya preparadas facilita validar el comportamiento principal del broker sin tener que construir casos desde cero.

Como conclusión de la evaluación, el sistema es usable para desarrolladores con conocimientos técnicos básicos o intermedios, siempre que cuenten con documentación clara y ejemplos reproducibles. Su principal fortaleza es que las pruebas existentes ayudan a comprender el comportamiento esperado del sistema. Su principal limitación es que la ausencia de una interfaz gráfica y el uso de tecnologías como gRPC, Redis Streams y Go elevan la curva de aprendizaje. Por ello, la mejora de la documentación, los ejemplos y las guías de diagnóstico será fundamental para facilitar su adopción por nuevos usuarios técnicos.

> [!warning] Delimitar qué se evaluó como usabilidad
> No se informa el número de participantes, sus perfiles, un instrumento, tiempos de tarea ni una escala de resultados. Si la revisión fue realizada por el propio equipo, conviene denominarla "evaluación heurística técnica" y evitar generalizar que el sistema es usable para otros desarrolladores sin una prueba con usuarios.

### 4.2.4 Análisis de ciberseguridad

Para el análisis de ciberseguridad de dominus broker, lo evaluamos en dos partes. La primera fuera el backend dominus-broker que es responsable de exponer los servicios HTTP y GRPC, validar tokens, gestionar operaciones concurrentes y comunicarse con Redis. La segunda parte fue el cliente dominus-sdk, que cumple el papel de interfaz de consumo de el broker. Como dominus no dispone de una interfaz gráfica, las aplicaciones que usaron el broker sería mediante el SDK, que construye las conexiones,agrega metadatos, serializa las solicitudes y permite invocar todas las operaciones. Por esta razón el análisis de la interfaz se centró en el comportamiento del sdk y no una pantalla web.

Al ser un SDK no hay exploraciones en una red pública, se ejecutó dentro de un entorno local con docker y las pruebas se limitaron al (127.0.0.1). Primero se define el alcance de qué pruebas podríamos realizar dado a estas limitaciones debido a la arquitectura, con propósito de identificar controles efectivos, fallos observados y aspectos que van a requerir otra segunda revisión. En el Broker se revisaron autentificación, concurrencia, destinos, límites de payload, streams, tls y Redis. Por otro lado en el SDK se analizaron la validación de destinos, protección del canal TLS, el envío de credenciales, el manejo de errores, la serialización, y límite de tiempo.

La distinción entre backend y SDK importa porque no se puede delegar toda la seguridad al cliente. El sdk puede rechazar un destino mal formado, pero una solicitud creada por otro cliente podría llamar directamente al broker. Es por este motivo que las validaciones relaciones con Auth, autorización, límites e idempotencia deben experimentar en backend que debería de ser la frontera de confianza del sistema.

Para precisar el concepto de idempotente es necesario contemplar que una operación idempotente produce el mismo efecto sobre un mensaje aunque el cliente repita una y otra vez el envío o recepción de un mensaje, si el mensaje llega con una llave repetida. En este laboratorio la idempotencia se implementa mediante una clave definida y asociada a una solicitud. si la misma clava llega dos veces el broker debería de procesar una solicitud y reconocer las siguientes como duplicadas. Esto protege operaciones de publicación, consumo, o suscripción frente a intentos causados por timeouts y frente a mensajes concurrentes.

#### Preparación del Laboratorio

Para poder realizar el análisis construimos un entorno mediante docker.

```text
docker image ls dominus-broker:security-lab
```

El entorno quedó compuesto por un contenedor de Redis y otro contenedor de dominus-broker-lab con los puertos puertos locales 6379, 8000 y 5000. El servicio informó los siguientes puntos de escucha:

```text
Rest: http://0.0.0.0:8000  
Grpc: 0.0.0.0:5000
```

Las pruebas HTTP se realizaron con curl; las pruebas de reflexión HTTP , con grpcurl; y las pruebas concurrentes del backend y del SDK, con go test. Las salidas se capturaron mediante tee en la carpeta: \security-evidence

La variable DOMINUS_TEST_TOKEN representa una credencial desechable. El valor real no se repite en este documento.

```text
EVIDENCE="$PWD/Referance/security-evidence"  
export DOMINUS_TEST_TOKEN='<token-desechable-del-laboratorio>'  
  
docker image ls dominus-broker:security-lab  
docker ps --filter "name=redis" --filter "name=dominus-broker-lab"  
docker logs --tail=200 dominus-broker-lab 2>&1 \  
| tee "$EVIDENCE/E21-broker-startup.txt"
```

#### Herramientas Utilizadas

Durante la realización de este análisis se usaron varias herramientas que facilitaron la gestión y obtención de la evidencia. La Tabla 5 relaciona cada herramienta con su función en la obtención y comprobación de la evidencia.

**Tabla 5**

*Herramientas utilizadas en el análisis de ciberseguridad* 

|**Herramienta**|**Uso en la actividad**|
|---|---|
|Docker|Aislar el broker y Redis, revisar puertos y conservar un entorno reproducible.|
|curl|Verificar autenticación HTTP, salud y métricas.|
|grpcurl|Consultar reflexión gRPC y comparar solicitudes sin token, con token inválido y con token válido.|
|Go y go test|Ejecutar pruebas de concurrencia, TLS, metadatos, destinos, timeout, serialización y ciclo de vida.|
|go test -race|Buscar carreras de datos en la prueba de idempotencia.|
|Redis CLI|Comprobar ACL, conectividad y expiración de claves.|
|docker stats y docker logs|Observar memoria, continuidad del proceso y errores durante las pruebas.|
|Certificados efímeros de prueba|Validar en el SDK una CA correcta, una CA incorrecta, un nombre incorrecto y la ausencia de CA.|

_Nota._ Elaboración propia a partir de la documentación técnica. La tabla describe el uso de herramientas de contenedores, clientes HTTP y gRPC, pruebas de Go, Redis y certificados efímeros dentro del laboratorio.

El detector de carreras se incluyó porque una operación puede parecer correcta en una prueba secuencial y fallar cuando varias solicitudes compiten por la misma clave. En este caso se utilizó como control complementario: que no aparezca una carrera de memoria no significa que la lógica de negocio sea atómica.

#### Criterio de análisis

El criterio de análisis fue el siguiente: una prueba tiene un resultado esperado, una observación y una interpretación. Cuando la observación coincide con el criterio, se considera que el control funciona para ese escenario. Cuando difiere, se registra un hallazgo. Cuando el escenario no permite decidir si existe una política, se marca como inconcluso y no se presenta como vulnerabilidad confirmada. Se realizaron alrededor de 15 puntos de revisión mediantes pruebas e intentos ataques para lograr el análisis de lo cual se presentan los siguientes cinco como hallazgos**.**

> [!todo] Justificar la selección de hallazgos
> Se mencionan alrededor de quince puntos de revisión, pero solo se presentan cinco. Conviene incorporar la matriz completa en un anexo o explicar los criterios de selección, el resultado de los controles sin hallazgo y el método empleado para asignar severidad.

#### Hallazgos del Backend Dominus-broker

##### BE-01: autenticación gRPC ante token ausente

##### Objetivo

Comprobar que el interceptor de autenticación rechaza una llama cuando falta x-api-key, sin cerrar el servidor. También se compra un token incorrecto, y uno correcto para validar un fallo válido y un fallo causado por la ausencia del encabezado.

La ruta utilizada por grpcurl list es el stream de reflexión /grpc.reflection.v1.ServerReflection/ServerReflectionInfo. El mismo interceptor ApiToken se instala para las llamadas gRPC de streaming en internal/bootstraps/bootstraps.go:99-103. Por eso el defecto no está limitado a una ruta HTTP ni a una función llamada “Broker API”.

##### Riesgo

El código lee la posición cero del arreglo que devuelve metadata.Get sin comprobar su longitud. Cuando la metadata existe pero no contiene el encabezado, Go produce index out of range. El proceso termina y el servicio deja de atender HTTP y gRPC. Este patrón corresponde a una validación incorrecta de índice y puede afectar la disponibilidad (MITRE, 2026a).

##### Preparación

Se comparó que el contendor estaba activo y que /health respondía antes del caso negativo. Como endpoint http también requiere el token, la línea base se tomó con la credencial del contenedor.

```text
curl -i \  
-H "x-api-key: ${DOMINUS_TEST_TOKEN}" \  
http://127.0.0.1:8000/health \  
2>&1 | tee "$EVIDENCE/E22-BE01-health-before.txt"
```

#### **Comando sin token**

```text
grpcurl -plaintext \  
127.0.0.1:5000 list \  
2>&1 | tee "$EVIDENCE/E23-BE01-no-token.txt"
```

#### **Comando con token incorrecto**

```text
grpcurl -plaintext \  
-H 'x-api-key: token-invalido-de-laboratorio' \  
127.0.0.1:5000 list \  
2>&1 | tee "$EVIDENCE/E25-BE01-invalid-token.txt"
```

#### **Comando con token correcto**

```text
grpcurl -plaintext \  
-H "x-api-key: ${DOMINUS_TEST_TOKEN}" \  
127.0.0.1:5000 list \  
2>&1 | tee "$EVIDENCE/E26-BE01-valid-token.txt"
```

#### **Comprobación del proceso**

```text
curl -i http://127.0.0.1:8000/health \  
2>&1 | tee "$EVIDENCE/E24-BE01-health-after-no-token.txt"  
  
docker ps --filter "name=dominus-broker-lab"  
docker logs --tail=200 dominus-broker-lab
```

#### **_Resultado esperado_**

Sin token y con token incorrecto se esperaba Unauthenticated; con el token correcto, el listado de servicios. El proceso debía permanecer activo en los tres casos.

##### Resultado real

El token incorrecto produjo Unauthenticated y el correcto permite enumerar dominus.BrokerAPI y dominus.SqsAPI. En la ejecución sin token, el log del contenedor registró un panic. La comprobación posterior de /health no pudo establecer conexión. Una repetición de la prueba realizada cuando el contenedor ya estaba detenido, registró “connection refused”; por eso el panic se demuestra con el log de arranque y la indisponibilidad se corrobora con el health check.

##### Evidencia

```text
Archivo: E21-broker-startup.txt  
panic: runtime error: index out of range [0] with length 0  
dominus-broker/internal/infrastructure/grpc/middlewares.(*middlewares).ApiToken  
/app/internal/infrastructure/grpc/middlewares/middlewares.go:48  
  
Archivo: E24-BE01-health-after-no-token.txt  
curl: (7) Failed to connect to 127.0.0.1:8000  
  
Archivo: E25-BE01-invalid-token.txt  
code = Unauthenticated desc = failed to match token  
  
Archivo: E26-BE01-valid-token.txt  
dominus.BrokerAPI  
dominus.SqsAPI  
grpc.reflection.v1.ServerReflection
```

##### Recomendación

Dado a que el middleware intenta guardar el resultado del header sin validar o sanitizar lo que recibió en token := md.Get(enum.X_API_KEY)[0]. La sugerencia o recomendación es comprobar len(values) == 0 y devolver codes.Unauthenticated antes de acceder al primer elemento. La corrección debe cubrir tanto el interceptor unary como el de stream, porque ambos llaman a ApiToken.

##### BE-03: idempotencia bajo concurrencia

##### Objetivo

Verificar que veinte solicitudes al mismo tiempo con la misma clave de idempotencia no ejecuten la operación más de una vez. Esta propiedad se usa en las operación unary de dominus.SqsAPI, como /dominus.SqsAPI/Producer, /dominus.SqsAPI/Consumer y /dominus.SqsAPI/Ack, porque IdemPotency forma parte de ChainUnaryInterceptor.

##### Riesgo

Un cliente puede reintentar una operación cuando pierde la respuesta o alcanza un timeout. Si la comprobación y la reserva de la clave ocurren por separado, dos solicitudes pueden atravesar el middleware antes de que redis registre alguna. El efecto puede ser una publicación, consumo o confirmación de mensajería duplicada. El detector -race de go idéntica acceso incompatible a memoria durante la ejecución pero no demuestra que una secuencia distribuida sea atómica (The Go Team, s. f.).

##### Preparación

La prueba de seguridad de redis inicia vacía, creamos una sola clave por ronda, sincronizamos veinte rutinas de go y se repite el experimento veinte veces. Invoca directamente IdemPotency; así aísla la propiedad de idempotencia de la autenticación y del transporte.

#### **Comando ejecutado**

```text
cd Referance/dominus-broker  
CGO_ENABLED=1 go test -race -count=20 ./tests/security \  
2>&1 | tee ../security-evidence/E31-BE03-idempotencia.txt
```

#### **Comprobación del proceso**

La prueba no usa el contenedor del broker. El proceso observado es **go** test, que concluye y devuelve FAIL porque la invariante “exactamente una aceptación” no se cumple. Esto evita interpretar una caída del contenedor.

##### Resultado Esperado

Cada ronda debía registrar una aceptación y diecinueve duplicados. No se esperaba un reporte de carrera de datos.

##### Resultado Real

Todas las rondas aceptaron más de una solicitud. El mínimo observado fue 3 de 20 y el máximo 20 de 20. Las solicitudes rechazadas recibieron Aborted: rate limit reached, un mensaje que tampoco distingue un duplicado de un límite de tasa. No apareció un reporte WARNING: DATA RACE;

##### Evidencia

```text
Archivo: E31-BE03-idempotencia.txt  
round 0: accepted 4 of 20 concurrent requests with one idempotency key; want exactly 1  
round 1: accepted 12 of 20 concurrent requests with one idempotency key; want exactly 1  
round 4: accepted 3 of 20 concurrent requests with one idempotency key; want exactly 1  
round 6: accepted 20 of 20 concurrent requests with one idempotency key; want exactly 1  
rpc error: code = Aborted desc = rate limit reached
```

La ventana de carrera se encuentra en middlewares.**go** primero consulta Redis y después inicia el guardado en otra goroutine.

```text
if ok := m.ch.CheckConsumer(ctx, keys[0]); ok {  
return nil, status.Error(codes.Aborted, enum.RATE_LIMIT_REACHED)  
}  
go func(key string) {  
_ = m.ch.SaveConsumer(ctx, key)  
}(keys[0])
```

SaveConsumer ya usa NX y expiración en redis/cchecker/outbound.**go**, pero el middleware no utiliza el resultado de esa operación para decidir cuál solicitud puede continuar. Redis define NX como una condición que guarda la clave solo si todavía no existe; la respuesta de esa única operación debe ser la decisión de aceptación (Redis, s. f.-b).

##### Recomendación

Eliminar la secuencia CheckConsumer seguida de un guardado asíncrono. SaveConsumer debe ejecutarse de forma síncrona y devolver tres estados distinguibles: clave reservada, clave existente y error de Redis. Solo la solicitud que reserva la clave puede llegar al handler. Para una clave existente se recomienda un código de duplicado documentado, no rate limit reached.

#### Hallazgos del cliente dominus-sdk

##### CL-01: validación del certificado TLS

##### Objetivo

Verificar que dominus-sdk autentica al servidor antes de crear un stream. La prueba cubre la cadena de confianza y el nombre del servidor. También observa cómo la API del SDK comunica un error de configuración.

La llamada es NewBrokerConfig(...).InitAPIClientsTLSFromFile(...), seguida de UseStreamServerConn(). Esta última abre la ruta gRPC /dominus.BrokerAPI/ServerStream mediante broker_client_conn.**go**

##### Preparación

El análisis de esta prueba se realizó con Go 1.26.1 y gRPC 1.79.1. TestTLS levantó un servidor gRPC en 127.0.0.1 con un puerto efímero. Los archivos se guardaron en t.TempDir() y se eliminaron al terminar el test.

**Certificado utilizado**

Se generó un certificado RSA de 2048 bits válido durante una hora y con uso extendido ServerAuth. No se utilizó un certificado de producción ni se copió la clave privada a la evidencia.

#### **CA**

La CA efímera usa el nombre Dominus SDK Test CA. Para el caso válido, firma el certificado del servidor. En el caso negativo se genera una segunda CA independiente; el cliente debe rechazar el certificado porque su firma no pertenece a la raíz configurada.

#### **SAN y serverName**

El certificado contiene el nombre DNS localhost y la dirección IP 127.0.0.1 como valores SAN. El caso válido configura serverName="localhost"; el caso negativo usa wrong.test.

#### **Comando**

```text
cd Referance/dominus-sdk  
go test -v ./dominus/security -run TestTLS \  
2>&1 | tee ../security-evidence/E34-CL01-tls.txt
```

##### Resultado Esperado

La CA válida y el SAN correcto debían permitir la creación del stream. Una CA distinta y un serverName que no aparece en el SAN debían ser rechazados. Una ruta de CA inexistente debía producir un error de inicialización controlado.

##### Resultado Real

La verificación criptográfica funcionó: el caso válido tuvo éxito y los dos casos de confianza incorrecta fueron rechazados. La CA inexistente también impidió la inicialización. Sin embargo, los casos negativos se comunicaron mediante panic. El test aparece como PASS porque captura ese panic y confirma el rechazo esperado; esto no significa que la API de manejo de errores sea adecuada.

##### Evidencia

```text
Archivo: E34-CL01-tls.txt  
case=valid-ca-san result=success panic=false  
case=wrong-ca result=rejected panic=true  
case=wrong-san result=rejected panic=true  
case=missing-ca result=initialization-error panic=true  
--- PASS: TestTLS (0.51s)
```

La verificación se configura en/dominus-sdk/dominus/broker_client_factory.go. El defecto de manejo aparece en las líneas 29-34:

```text
if _, err := os.Stat(caCertPath); err != nil {  
panic(err)  
}  
cred, err := credentials.NewClientTLSFromFile(caCertPath, serverName)  
if err != nil {  
panic(err)  
}
```

##### Recomendación

Conservar la validación de CA y SAN, pero cambiar la firma de inicialización para devolver (Broker, error). Un archivo ausente, una CA inválida o un fallo de conexión no deberían terminar la aplicación consumidora. También conviene eliminar la alternativa plaintext de las rutas destinadas a producción o exigir una opción explícita para habilitarla.

##### CL-03: validación y autorización de destinos

##### Objetivo

Comprobar si el SDK acepta únicamente destinos con el formato host:puerto y si distingue entre una dirección sintácticamente válida y un destino autorizado. Esta validación ocurre durante NewBrokerConfig(...).InitAPIClients(...), antes de invocar una ruta gRPC.

##### Riesgo

El SDK recibe el destino del broker y la lista de suscriptores. Si una aplicación construye esos valores a partir de entrada externa, una validación demasiado amplia puede dirigir conexiones hacia ubicaciones no previstas. OWASP describe la SSRF como el abuso de una aplicación para interactuar con la red en nombre del usuario y recomienda una allowlist cuando los destinos legítimos son conocidos (OWASP Foundation, s. f.). La prueba no explotó una SSRF ni contactó redes externas; confirmó una debilidad de validación que podría participar en ese escenario.

##### Preparación

El test construyó configuraciones con cinco cadenas. No necesitó conectarse a los destinos: la aceptación o el panic ocurre durante la validación de la fábrica.

#### **Comando**

```text
cd Referance/dominus-sdk  
go test -v ./dominus/security -run TestDestinations \  
2>&1 | tee ../security-evidence/E36-CL03-destinations.txt
```

##### Resultado Esperado

127.0.0.1:5000 debía pasar la validación sintáctica. hostname.test:99999 y hostname.test/path debían rechazarse. La autorización debía ser una decisión separada: que una cadena tenga formato correcto no implica que esté permitida.

##### Resultado Real

hostname.test/path fue aceptado, aunque no tiene el formato host:puerto. La prueba también confirmó que el SDK carece de una allowlist independiente. hostname.test:5000 fue rechazado por la expresión actual, un comportamiento más restrictivo que el formato gRPC general y que debería documentarse si es intencional.

##### Evidencia

```text
Archivo: E36-CL03-destinations.txt  
destination=127.0.0.1:5000 accepted=true expected_syntax_accept=true  
destination=hostname.test:5000 accepted=false expected_syntax_accept=false  
destination=hostname.test:99999 accepted=false expected_syntax_accept=false  
destination=hostname.test/path accepted=true expected_syntax_accept=false  
unexpected destination validation result  
authorization=not implemented as a separate allowlist  
--- FAIL: TestDestinations (0.00s)
```

La ruta del defecto es:

```text
NewBrokerConfig  
-> brokerConfig.validate  
-> rules.checkURI  
-> regexp.MatchString
```

##### Recomendación

Sustituir la expresión regular como decisión única. net.SplitHostPort debe separar host y puerto; el puerto debe estar entre 1 y 65535; y deben rechazarse rutas, esquemas y credenciales embebidas. Después de validar la sintaxis, una allowlist debe decidir qué hosts o direcciones están autorizados. El broker debe repetir esta validación antes de iniciar conexiones salientes, porque el SDK no es una frontera de confianza.

##### CL-05: error de serialización descartado

##### Objetivo

Comprobar que el SDK devuelve el error cuando un valor no puede convertirse a JSON y que no envía una solicitud incompleta. La ruta evaluada es /dominus.BrokerAPI/ClientStream, abierta por UseStreamClientConn().

##### Riesgo

json.Marshal puede fallar con valores como funciones o canales. Si el SDK ignora ese error, el consumidor recibe nil y puede creer que la operación fue enviada correctamente. El broker recibe un payload vacío, lo que afecta la integridad del mensaje y dificulta el diagnóstico. MITRE clasifica la omisión del valor de retorno de una operación como CWE-252, _Unchecked Return Value_ (MITRE, 2026b).

##### Preparación

TestSerializationError levantó un servidor gRPC local, obtuvo la función de envío de UseStreamClientConn() y le pasó **func**() {}, un valor que encoding/json no puede serializar.

#### **Comando**

```text
cd Referance/dominus-sdk  
go test -v ./dominus/security -run TestSerializationError \  
2>&1 | tee ../security-evidence/E37-CL05-serialization.txt
```

##### Resultado Esperado

json.Marshal debía fallar, la función de envío debía retornar ese error y el servidor no debía recibir ningún mensaje.

##### Resultado Real

La función devuelve nil, llamó a Send y el servidor recibió un payload con longitud cero. El test se marcó como fallido de forma intencional para que el comportamiento no pase inadvertido en una suite automatizada.

##### Evidencia

```text
Archivo: E37-CL05-serialization.txt  
marshal_error_input=function  
send_error=<nil>  
send_called=true  
payload_length=0  
FAIL: json.Marshal error was swallowed; Send received an empty payload  
--- FAIL: TestSerializationError (0.01s)
```

El detalle aparece dos veces en Referance/dominus-sdk/dominus/broker_client_services.**go**, para client stream y bidirectional stream:

```text
// Línea 25  
payload, _ := json.Marshal(body)  
// Línea 50  
payload, _ := json.Marshal(body)
```

##### Recomendación

Capturar el error y devolverlo antes de llamar a Send:

```text
payload, err := json.Marshal(body)  
if err != nil {  
return fmt.Errorf("serialize broker payload: %w", err)  
}
```

El mismo cambio debe aplicarse a UseStreamClientConn y UseBiStreamConn. El error debe conservar la causa con %w y no debe registrar el contenido completo del payload.

### 4.2.5 Pruebas de rendimiento y carga

Este apartado presenta la evidencia obtenida durante la evaluación de rendimiento del dominus-broker. El propósito de las pruebas fue observar el comportamiento del sistema bajo condiciones de carga sostenida, considerando tanto el procesamiento de comunicaciones bidireccionales mediante gRPC como el flujo de comunicación asíncrona soportado por Redis. Los resultados se analizan a partir de las métricas registradas en Grafana y de las evidencias obtenidas directamente desde la interfaz de Redis.

##### Diseño y configuración de las pruebas

La evaluación se realizó mediante ghz, utilizando configuraciones de carga definidas para los métodos expuestos por el broker. Se establecieron dos escenarios principales. El primero corresponde al método dominus.BrokerAPI.BidirectionalStream, orientado a evaluar el patrón fan-in/fan-out mediante comunicación bidireccional gRPC. Este flujo no emplea Redis, por lo que permite observar de forma directa el comportamiento del procesamiento en tiempo real. El segundo escenario corresponde al método dominus.SqsAPI.Producer, asociado al flujo asíncrono cuya persistencia intermedia se realiza mediante Redis. La Tabla 6 permite comparar los métodos y parámetros aplicados en ambos escenarios.

**Tabla 6**

*Configuración de los escenarios de rendimiento y carga* 

|**Escenario**|**Método**|**Parámetros principales**|
|---|---|---|
|Comunicación bidireccional|dominus.BrokerAPI.BidirectionalStream|RPS: 680; concurrencia de 20 a 1000; duración: 5 min; stream-call-duration: 500 ms; 20 llamadas por stream; intervalo: 100 ms; 2 CPU.|
|Comunicación asíncrona|dominus.SqsAPI.Producer|RPS: 20.000; concurrencia: 1; total: 100; carga escalonada de 20 a 10.000.|

_Nota._ Elaboración propia a partir de la configuración de `ghz`. La tabla distingue el método, la tasa, la concurrencia, la duración y los parámetros principales de cada escenario.

La configuración anterior permitió someter el broker a una carga progresiva y observar su comportamiento a medida que aumentaba el número de operaciones concurrentes. Para el escenario bidireccional se utilizaron tres suscriptores, mientras que el escenario asíncrono se verificó adicionalmente mediante la observación del consumer group de Redis.

##### Rendimiento y capacidad de procesamiento

La métrica denominada “Handled per second sum” registrada en Grafana muestra un incremento del volumen de mensajes procesados desde aproximadamente 200.000 hasta valores cercanos a 260.000 mensajes por segundo durante la ventana observada. Este comportamiento evidencia que el broker fue capaz de sostener un volumen elevado de operaciones mientras la carga aplicada se incrementaba.

A partir de los datos disponibles, el valor observado se sitúa alrededor de 250.000 mensajes por segundo en determinados momentos de la ejecución. No obstante, el artefacto de pruebas no permite establecer con certeza si esta métrica corresponde exclusivamente a uno de los flujos evaluados o si representa una agregación de diferentes fuentes de carga. Por esta razón, el resultado debe interpretarse como capacidad observada del sistema durante la ejecución y no como una tasa aislada atribuible de forma concluyente a un único camino de procesamiento.

##### Comportamiento de la latencia

El análisis de los percentiles de latencia muestra un comportamiento estable durante la ventana observada. El percentil P99 se mantiene alrededor de 10 ms, mientras que P95 y P50 presentan valores inferiores y una variación reducida. Este comportamiento resulta relevante para un sistema de mensajería en tiempo real, debido a que indica que el incremento de carga no produjo una degradación significativa de los tiempos de respuesta en la ejecución analizada.

La observación de un P99 cercano a 10 ms constituye además un margen favorable respecto de un umbral de 20 ms propuesto posteriormente como objetivo operativo. Sin embargo, este valor debe considerarse un resultado experimental de la ejecución documentada y no una garantía de comportamiento bajo cualquier condición de carga, ya que serían necesarias pruebas adicionales con diferentes duraciones, niveles de concurrencia y escenarios de fallo.

##### Utilización de recursos

La utilización de CPU registrada durante la prueba presenta un incremento aproximado desde 1 % hasta 4 %. Estos valores indican que, para la carga observada, el procesamiento no estuvo limitado por la capacidad de cómputo disponible. En consecuencia, el comportamiento observado sugiere la existencia de margen de CPU durante la ejecución evaluada.

En cuanto a memoria, el consumo pasó aproximadamente de 36 % a 42 %. El incremento se correlaciona con el aumento del throughput observado, aunque los datos disponibles no permiten determinar por sí solos si dicho crecimiento corresponde exclusivamente a la acumulación de datos, a estructuras internas del proceso, a la actividad de Redis o a otros factores del entorno. Por ello, la tendencia debe considerarse un indicador a monitorizar en ejecuciones prolongadas. La Tabla 7 sintetiza los cambios observados en CPU, memoria y disponibilidad.

**Tabla 7**

*Utilización de recursos y disponibilidad observada* 

|**Métrica**|**Valor inicial aproximado**|**Valor observado final**|**Interpretación**|
|---|---|---|---|
|CPU|1%|4%|Baja utilización; no se observa saturación de CPU.|
|Memoria|36%|42%|Incremento moderado asociado temporalmente al aumento de carga.|
|Disponibilidad|≈100 %|≈100 %|No se observa degradación relevante en la ventana evaluada.|

_Nota._ Elaboración propia a partir de las métricas registradas en Grafana. La tabla resume los valores iniciales y finales aproximados y ofrece una interpretación limitada a la ventana evaluada.

La Figura 13 aporta una primera ventana del panel de Grafana para observar la evolución del volumen procesado, el uso de recursos, la disponibilidad y los percentiles de latencia.

**Figura 13**

*Métricas de rendimiento durante la prueba de carga, captura 1* 

![Métricas de rendimiento durante la prueba de carga, captura 1](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%2013.png>)

_Nota._ Elaboración propia a partir del panel de Grafana. La captura presenta CPU, mensajes gestionados, memoria, disponibilidad y percentiles durante una ventana de cinco minutos.

La Figura 14 complementa la evidencia anterior con una segunda ventana temporal del mismo panel.

**Figura 14**

*Métricas de rendimiento durante la prueba de carga, captura 2* 

![Métricas de rendimiento durante la prueba de carga, captura 2](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%2014.png>)

_Nota._ Elaboración propia a partir del panel de Grafana. La captura permite comparar la progresión de CPU, memoria y mensajes gestionados con los percentiles y la disponibilidad.

##### Evidencia del procesamiento asíncrono con Redis

La evaluación del flujo asíncrono se complementó con la inspección de Redis. Las capturas muestran un consumer group denominado “consumer-group” compuesto por tres consumidores y un valor Pending igual a cero. Asimismo, se observan entradas identificadas mediante IDs y marcas temporales. Esta evidencia permite verificar que, durante la ventana observada, los mensajes publicados en el stream no permanecieron acumulados como pendientes en el grupo de consumidores.

El valor Pending = 0 constituye una evidencia relevante para el comportamiento del mecanismo asíncrono, puesto que indica ausencia de backlog pendiente en el momento de la captura. Desde la perspectiva de la arquitectura propuesta, este resultado es consistente con un procesamiento asíncrono en el que la memoria intermedia proporcionada por Redis permite desacoplar productores y consumidores sin evidenciar acumulación de mensajes durante el escenario probado.

##### Disponibilidad y estabilidad del sistema

La métrica de disponibilidad se mantiene próxima al 100 % durante la ventana de observación. Este comportamiento, combinado con el throughput elevado y los bajos percentiles de latencia, aporta evidencia de estabilidad operacional en el escenario evaluado. No se observan en los datos proporcionados indicios de degradación significativa asociados al incremento de carga.

Es importante distinguir, no obstante, entre la estabilidad observada y una validación formal de disponibilidad a nivel de producción. El conjunto de pruebas documentado constituye una evaluación experimental y no incluye, en esta evidencia, inyección de fallos, interrupciones de consumidores, pruebas de recuperación o ejecuciones prolongadas suficientes para caracterizar la disponibilidad bajo condiciones adversas.

La Figura 15 aporta una tercera captura del panel para mostrar la continuidad de las métricas en una ventana posterior.

**Figura 15**

*Métricas de rendimiento durante la prueba de carga, captura 3* 

![Métricas de rendimiento durante la prueba de carga, captura 3](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%2015.png>)

_Nota._ Elaboración propia a partir del panel de Grafana. La captura muestra la evolución del throughput, el consumo de recursos, la disponibilidad y los percentiles durante la ejecución.

La Figura 16 continúa la serie y permite observar los valores más altos registrados al final de la ventana documentada.

**Figura 16**

*Métricas de rendimiento durante la prueba de carga, captura 4* 

![Métricas de rendimiento durante la prueba de carga, captura 4](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%2016.png>)

_Nota._ Elaboración propia a partir del panel de Grafana. La captura registra el aumento final de mensajes gestionados y del consumo de CPU y memoria sin una caída visible de disponibilidad.

La Figura 17 complementa las métricas de Grafana con evidencia directa de las entradas almacenadas en Redis Streams.

**Figura 17**

*Entradas de mensajes registradas en Redis Streams* 

![Entradas de mensajes registradas en Redis Streams](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%2017.png>)

_Nota._ Elaboración propia a partir de la interfaz de Redis en Visual Studio Code. La captura muestra tres entradas del stream `consumer` con sus identificadores y payloads.

##### Síntesis de los resultados obtenidos

Los resultados experimentales permiten establecer una primera caracterización cuantitativa del comportamiento del dominus-broker bajo carga. La evidencia disponible muestra un throughput observado en el intervalo aproximado de 200.000 a 260.000 mensajes por segundo, latencias bajas y estables con P99 alrededor de 10 ms, utilización reducida de CPU, incremento moderado del consumo de memoria y disponibilidad cercana al 100 %.

En el componente asíncrono, la evidencia obtenida desde Redis muestra un consumer group con tres consumidores y Pending = 0, lo que indica que no existía acumulación de mensajes pendientes durante las capturas analizadas. Este resultado complementa las métricas de Grafana y permite evaluar no solo la capacidad de procesamiento del broker, sino también el comportamiento de la memoria intermedia utilizada en el flujo asíncrono. La Tabla 8 reúne los indicadores principales y la evidencia de la que se derivan.

**Tabla 8**

*Síntesis de los resultados de rendimiento* 

|**Indicador**|**Resultado observado**|**Evidencia**|
|---|---|---|
|Throughput|≈200.000–260.000 mensajes/s|Grafana: Handled per second sum|
|P99|≈10 ms|Grafana: percentiles|
|P95 / P50|Bajos y estables|Grafana: percentiles|
|CPU|≈1 %–4 %|Grafana|
|Memoria|≈36 %–42 %|Grafana|
|Disponibilidad|≈100 %|Grafana|
|Consumidores Redis|3|Redis UI|
|Pending Redis|0|Redis UI|

_Nota._ Elaboración propia a partir de Grafana y de la interfaz de Redis. La tabla resume throughput, latencia, recursos, disponibilidad y estado del grupo de consumidores durante la prueba.

> [!danger] Verificar la unidad y el origen de la métrica de throughput
> La carga declarada (680 RPS en un escenario y 20.000 RPS en otro) no se conecta de forma inequívoca con los 200.000–260.000 "mensajes/s" informados. Antes de presentar ese valor como throughput, se debe documentar la consulta de Grafana/Prometheus, distinguir contador de tasa y separar las métricas de cada flujo.

##### Criterios de evaluación derivados de la evidencia

A partir de los resultados obtenidos se definieron indicadores de nivel de servicio (SLI) y objetivos de nivel de servicio (SLO) como referencia para futuras evaluaciones. Estos valores no deben interpretarse como requisitos demostrados del sistema, sino como objetivos preliminares derivados de la evidencia experimental. La Tabla 9 organiza dichos objetivos para facilitar su validación en pruebas posteriores.

**Tabla 9**

*Objetivos preliminares de nivel de servicio* 

|**Indicador**|**Objetivo propuesto**|
|---|---|
|Throughput|≥ 200.000 mensajes/s en ventanas de 1 minuto bajo la carga objetivo.|
|Latencia P99|< 20 ms.|
|Latencia P95|< 10 ms.|
|Disponibilidad|99,95 % de operaciones exitosas; alerta por debajo de 99,9 %.|
|Pending en Redis|0 en condiciones normales; tolerancia < 5 mensajes pendientes por consumidor.|
|Procesamiento SQS end-to-end|P99 < 100 ms y P95 < 50 ms, cuando SQS forme parte del flujo|

_Nota._ Elaboración propia. La tabla propone umbrales preliminares de throughput, latencia, disponibilidad y mensajes pendientes; estos valores todavía requieren validación independiente.

La definición de estos objetivos incorpora un margen respecto de los valores observados, con el propósito de evitar que variaciones normales de la ejecución produzcan falsas alertas. Su validación definitiva requiere nuevas ejecuciones con ventanas más extensas, distintos niveles de carga y escenarios de fallo.

##### Limitaciones de la evaluación

Los resultados deben interpretarse considerando las limitaciones de la evidencia disponible. En primer lugar, la métrica de throughput de aproximadamente 200.000–260.000 mensajes por segundo requiere una separación más precisa por flujo para determinar si corresponde al escenario bidireccional, al flujo asíncrono o a una agregación de fuentes. En segundo lugar, las capturas representan ventanas concretas de observación y no permiten por sí solas caracterizar el comportamiento del sistema durante ejecuciones de larga duración.

Adicionalmente, no se documentan en estas pruebas escenarios de recuperación ante fallos, pérdida de consumidores, incremento progresivo del número de consumidores, inyección de errores ni pruebas específicas destinadas a detectar fugas de memoria. Estas actividades constituyen extensiones naturales de la evaluación y permitirían fortalecer la evidencia sobre resiliencia y estabilidad.

##### Conclusión de la prueba

La evaluación realizada proporciona evidencia experimental favorable respecto al comportamiento del dominus-broker bajo carga. El sistema alcanzó tasas de procesamiento elevadas, mantuvo latencias bajas, presentó una utilización reducida de CPU y conservó una disponibilidad próxima al 100 % durante la ventana observada. Paralelamente, el flujo asíncrono mostró un consumer group de tres consumidores sin mensajes pendientes en Redis, lo que evidencia ausencia de backlog en el escenario analizado.

En conjunto, los resultados respaldan la viabilidad técnica de la solución para los patrones de comunicación evaluados. No obstante, la evidencia obtenida debe considerarse como una validación experimental inicial. La consolidación de conclusiones sobre capacidad máxima, comportamiento sostenido y resiliencia requiere ampliar la matriz de pruebas y separar de manera inequívoca las métricas correspondientes a cada flujo de comunicación.

# 5. Conclusiones y trabajo futuro (TBD)

> [!danger] Sección final incompleta
> Las secciones 5.1 y 5.2 todavía contienen únicamente instrucciones de la plantilla. La versión final debe responder de forma explícita a cada objetivo de la sección 3, distinguir resultados demostrados de limitaciones y convertir las mejoras identificadas en líneas concretas de trabajo futuro.

## 5.1. Conclusiones (TBD)

**TBD:** Este último apartado es habitual en todos los tipos de trabajos y presenta el resumen final de tu trabajo y debe servir para informar del alcance y relevancia de tu aportación.

Suele estructurarse empezando con un resumen del problema tratado, de cómo se ha abordado y de por qué la solución sería válida.

Es recomendable que incluya también un resumen de las contribuciones del trabajo, en el que relaciones las contribuciones y los resultados obtenidos con los objetivos que habías planteado para el trabajo, discutiendo hasta qué punto has conseguido resolver los objetivos planteados. Las conclusiones ofrecidas deberán ser consecuencia del trabajo realizado y, por lo tanto, deberán marcar el grado de consecución de los objetivos propuestos (cada objetivo del trabajo se enlazará con una conclusión).

## 5.2. Trabajo futuro (TBD)

Finalmente, se suele dedicar un último apartado a hablar de líneas de trabajo futuro que podrían aportar valor añadido al trabajo realizado. La sección debería señalar las perspectivas de futuro que abre el trabajo desarrollado para el campo de estudio definido. En el fondo, debes justificar de qué modo puede emplearse la aportación que has desarrollado y en qué campos.

# 6. Referencias bibliográficas

> [!info] Criterio APA 7 aplicado
> Las entradas se ordenaron alfabéticamente, se unificaron los autores corporativos, se ajustaron los títulos a estilo oración y se hicieron coincidir años y sufijos con las citas del texto. Markdown no representa de forma fiable el interlineado doble ni la sangría francesa de 1,27 cm; ambos deben aplicarse a toda esta lista en la versión final de Word o Google Docs.

> [!warning] Referencia duplicada consolidada
> Cockburn (2005) aparecía dos veces con datos distintos. Se conservó una sola entrada, la que incluye la fecha completa de publicación, y se eliminaron los sufijos innecesarios de NATS y RabbitMQ porque solo hay una obra de cada autor en la lista.

> [!info] Obras distintas de un mismo autor corporativo
> Redis tiene cuatro páginas diferentes, identificadas como `s. f.-a` a `s. f.-d`; gRPC tiene dos páginas de 2024, identificadas como `2024a` y `2024b`; y MITRE mantiene `2026a` y `2026b`. No son referencias duplicadas. Los sufijos se asignaron de acuerdo con el orden alfabético de los títulos y se normalizaron en las citas.

> [!question] Confirmar la edición consultada de Kleppmann
> La referencia anterior indicaba una segunda edición de 2023, pero esa combinación de año, edición y autor no corresponde a una edición publicada. Se normalizó como la primera edición de Kleppmann (2017), coherente con las citas de autor único. Si el equipo consultó la segunda edición, deberá sustituir esta entrada por Kleppmann y Riccomini (2026) y actualizar todas las citas relacionadas.

Apache Kafka. (s. f.). *Documentation*. https://kafka.apache.org/documentation/

Apache Pulsar. (s. f.). *Messaging*. https://pulsar.apache.org/docs/3.0.x/concepts-messaging/

Cockburn, A. (2005, 4 de septiembre). *Hexagonal architecture*. https://alistair.cockburn.us/hexagonal-architecture

Fielding, R. T., Nottingham, M., & Reschke, J. (2022). *HTTP semantics* (RFC 9110). Internet Engineering Task Force. https://doi.org/10.17487/RFC9110

Gartner Peer Community. (2023). *Microservices architecture: Have engineering organizations found success?* https://www.gartner.com/peer-community/oneminuteinsights/omi-microservices-architecture-have-engineering-organizations-found-success-u6b

Google Cloud. (s. f.). *What is Pub/Sub?* Google Cloud Documentation. https://cloud.google.com/pubsub/docs/overview

gRPC Authors. (2024a, 12 de enero). *Authentication*. https://grpc.io/docs/guides/auth/

gRPC Authors. (2024b, 12 de noviembre). *Introduction to gRPC*. https://grpc.io/docs/what-is-grpc/introduction/

gRPC Authors. (2026, 11 de mayo). *Core concepts, architecture and lifecycle*. https://grpc.io/docs/what-is-grpc/core-concepts/

IMARC Group. (2024). *Microservices architecture market share, size 2025–2033*. https://www.imarcgroup.com/microservices-architecture-market

Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media.

Martin, R. C. (2017). *Clean architecture: A craftsman's guide to software structure and design*. Prentice Hall.

Microsoft. (s. f.). *Overview for gRPC on .NET*. Microsoft Learn. https://learn.microsoft.com/en-us/aspnet/core/grpc/

MITRE. (2026a, 30 de abril). *CWE-129: Improper validation of array index*. Common Weakness Enumeration. https://cwe.mitre.org/data/definitions/129.html

MITRE. (2026b, 30 de abril). *CWE-252: Unchecked return value*. Common Weakness Enumeration. https://cwe.mitre.org/data/definitions/252.html

NATS. (s. f.). *Pull consumers in depth*. NATS Documentation. https://docs.nats.io/learn/jetstream/pull-consumers

Newman, S. (2021). *Building microservices* (2nd ed.). O'Reilly Media.

OWASP Foundation. (s. f.). *Server-side request forgery prevention cheat sheet*. OWASP Cheat Sheet Series. https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html

Protocol Buffers. (s. f.). *Overview*. https://protobuf.dev/overview/

RabbitMQ. (s. f.). *Consumer acknowledgements and publisher confirms*. https://www.rabbitmq.com/docs/4.2/confirms

Redis. (s. f.-a). *Redis Streams*. https://redis.io/docs/latest/develop/data-types/streams/

Redis. (s. f.-b). *SET*. https://redis.io/docs/latest/commands/set/

Redis. (s. f.-c). *XACK*. https://redis.io/docs/latest/commands/xack/

Redis. (s. f.-d). *XREADGROUP*. https://redis.io/docs/latest/commands/xreadgroup/

Richards, M., & Ford, N. (2020). *Fundamentals of software architecture*. O'Reilly Media.

Richardson, C. (2018). *Microservices patterns: With examples in Java*. Manning Publications.

Sommerville, I. (2016). *Software engineering* (10th ed.). Pearson.

The Go Authors. (s. f.). *Documentation*. https://go.dev/doc/

The Go Team. (s. f.). *Data race detector*. The Go Programming Language. https://go.dev/doc/articles/race_detector

# Anexo A. Artículo

> [!question] Confirmar la convención del artículo anexo
> La numeración se mantiene continua con el cuerpo del TFM, como se solicitó. Si este anexo debe conservar el formato de una revista o congreso, quizá exija una numeración interna independiente —por ejemplo, tablas con números romanos— y deberá ajustarse al final.

Broker de mensajería Dominus

Maikel Barrios Insua

Daniel Campos Castañeda

Miguel de Jesús Chávez Barragán

Fernando Enrique García Castellanos

César Octavio Sánchez Contreras

Como elemento de identificación institucional del artículo, la Figura 18 presenta el logotipo de la universidad a la que se adscribe el trabajo.

**Figura 18**

*Logotipo institucional de la Universidad Internacional de La Rioja* 

![Logotipo institucional de la Universidad Internacional de La Rioja](<Attachments/TFM_Unir-F1011-Servicio_Mensajeria-Gdocs%202.jpeg>)

_Nota._ Fuente: Universidad Internacional de La Rioja (UNIR). La figura identifica la afiliación institucional de los autores.

Universidad Internacional de la Rioja, Latinoamérica

24/08/2026

**Resumen**

Este trabajo presenta Dominus, un broker híbrido que combina comunicación en tiempo real mediante gRPC y comunicación asíncrona respaldada por Redis Streams. La metodología siguió un enfoque iterativo e incremental de seis fases, hasta una implementación en Go con arquitectura de puertos y adaptadores, idempotencia y un SDK cliente. El prototipo se validó mediante 143 pruebas unitarias y 3 de integración (PASS, 91,8 % de cobertura), una evaluación de usabilidad y un análisis de ciberseguridad.

**Palabras clave:** arquitectura de puertos, broker de mensajería, gRPC, idempotencia, Redis Streams.

I. Introducción

Los sistemas distribuidos actuales dependen cada vez más de infraestructuras de mensajerías capaces de combinar comunicación en tiempo real con procesamiento asíncrono. Según Gartner Peer Community (2023), el 74% de las organizaciones ya emplea arquitecturas de microservicios con un 23% adicional que planea adoptarlas, mientras que IMARC Group (2024) estima que el mercado de microservicios pasará de 4,200 a 13,100 millones de dólares entre 2024 y 2033.

Este trabajo presenta un broker híbrido que combina una modalidad síncrona en tiempo real mediante gRPC y una modalidad asíncrona de tipo cola respaldada por Redis Streams, integrando en una sola herramienta capacidades que habitualmente se reparten entre distintas plataformas especializadas.

Del análisis de las alternativas existentes se concluyó que las soluciones maduras de mensajería ofrecen garantías útiles, pero con una complejidad que puede superar el alcance de un prototipo académico, y que el paralelismo, las particiones y las reentregas limitan en general las garantías de orden y de procesamiento único: la entrega al menos una vez mejora la recuperación ante fallos, aunque puede generar duplicados. Estas limitaciones justificaron la principal decisión de diseño del proyecto: adoptar una semántica de entrega al menos una vez y resolver el control de duplicados mediante un mecanismo de idempotencia respaldado por Redis, en lugar de intentar garantizar una semántica de entrega exactamente una vez a nivel de infraestructura.

II. Estado del Arte

Los brokers de mensajería forman parte habitual de las arquitecturas distribuidas modernas, ya que permiten desacoplar productores y consumidores mediante mecanismos de publicación y suscripción, enrutamiento y persistencia de mensajes, además de contemplar la tolerancia a fallos y el control de flujo (Newman, 2021). Seleccionar una plataforma adecuada resulta clave para un sistema híbrido como el propuesto, por lo que se realizó un análisis comparativo de las principales soluciones utilizadas en la industria.

Apache Kafka (s. f.) es una de las plataformas más usadas para el streaming de eventos, gracias a una arquitectura basada en la retención de eventos y su presentación distribuida. Kafka Streams incorpora garantías de procesamiento Exactly-Once (EOS), cuyo objetivo es asegurar que cada evento se procese exactamente una vez, reduciendo la posibilidad de resultados duplicados (Kleppmann, 2017). Esta fortaleza viene acompañada de una mayor complejidad, especialmente al administrar clústeres, particiones, políticas de retención y el ecosistema de conectores.

RabbitMQ (s. f.) funciona como un broker de estilo AMQP, un protocolo de mensajería estandarizado con mecanismos de enrutamiento y confirmación de entrega para desacoplar sistemas (Richards & Ford, 2020). Destaca por su modelo de intercambios, colas y claves de enrutamiento confirmadas por el publicador, con un enrutamiento flexible y patrones de mensajería validados a nivel de producción. Sin embargo, su orientación no está pensada para exponer de forma nativa una API basada en gRPC ni para integrar streaming en tiempo real con una cola asíncrona respaldada por Redis, que es precisamente la unión que busca este trabajo.

Apache Pulsar (s. f.) combina publicación y suscripción con una arquitectura distribuida entre el almacenamiento y el cómputo. Ofrece capacidades avanzadas, como distintos tipos de suscripción y mayor persistencia, pero su arquitectura resulta más compleja de lo necesario para un prototipo cuyo objetivo es estudiar los comportamientos internos de un broker híbrido.

NATS JetStream (NATS, s. f.) es una alternativa orientada a reducir la latencia, con persistencia de streaming y comunicación por pull y por push. Incorpora consumidores con mayor seguimiento de entregas, que pueden procesar mensajes bajo demanda. Su diseño destaca por la simplicidad y el rendimiento, aunque su ecosistema es menor si se compara con otras soluciones.

Finalmente, Google Cloud Pub/Sub (Google Cloud, s. f.), desarrollado por uno de los creadores de gRPC, ofrece un servicio de mensajería con suscripciones de pull y push. Su ventaja es la baja carga operativa para el equipo que lo consume, pero esa misma característica constituye una limitación para este trabajo, que busca estudiar y controlar el comportamiento interno de un broker autogestionado.

Junto a las plataformas de mensajería, también se evaluaron los mecanismos de comunicación disponibles para el propio broker. gRPC soporta cuatro modalidades (llamadas unarias, streaming de cliente, streaming de servidor y streaming bidireccional) sobre HTTP/2 (gRPC Authors, 2026), lo que permite representar dentro de un mismo contrato tanto las operaciones tipo cola de SqsAPI mediante llamadas unitarias como los flujos de tiempo real de BrokerAPI mediante streaming. Frente a REST, que facilita las pruebas manuales y la integración con navegadores pero no ofrece de forma nativa los distintos modelos de streaming requeridos, o frente a WebSockets, adecuados para tiempo real pero menos orientados a contratos estrictos y generación automática de código, gRPC junto con Protocol Buffers resultó la combinación más coherente para un broker experimental centrado en comunicación servicio-a-servicio con contratos tipados.

La Tabla 10 resume la comparación entre las tecnologías analizadas con base en las dimensiones más relevantes para el proyecto y permite reconocer el papel asignado a cada una en el prototipo.

**Tabla 10**

*Comparación de tecnologías de mensajería* 

|**_Tecnología_**|**_Streaming nativo_**|**_Papel en el proyecto_**|
|---|---|---|
|_gRPC_|_Sí_|_Canal principal (tiempo real)_|
|_Redis Streams_|_Lectura de streams_|_Persistencia temporal (asíncrono)_|
|_Apache Kafka_|_Sí_|_Referencia comparativa_|
|_RabbitMQ_|_Limitado_|_Referencia comparativa_|
|_Apache Pulsar_|_Sí_|_Referencia comparativa_|
|_NATS JetStream_|_Sí_|_Referencia comparativa_|

_Nota._ Elaboración propia. La tabla compara la disponibilidad de streaming nativo y el papel de cada tecnología dentro del proyecto.

Más allá del papel general de cada tecnología, el análisis comparativo también consideró el tipo de contrato, el mecanismo de confirmación y la complejidad operativa de cada alternativa. gRPC ofrece un contrato tipado mediante Protobuf y un mecanismo de Ack definido por el propio diseño de la API, con una complejidad operativa media; REST/HTTP, aunque ampliamente extendido, ofrece un contrato opcional mediante JSON u OpenAPI y no resuelve de forma nativa la comunicación en tiempo real ni la idempotencia que debe implementarse manualmente en ambos casos. Redis Streams aporta una estructura de mensajes propia con confirmación mediante XACK y soporte reciente de patrones de idempotencia basados en claves, con una complejidad operativa baja-media que resultó determinante para su elección como capa de persistencia temporal del prototipo.

Con esto se demuestra que las tecnologías existentes resuelven partes del problema, pero con enfoques distintos: Kafka y Pulsar son fuertes para streaming, RabbitMQ para enrutamiento, y NATS JetStream para mensajería ligera, mientras que Redis Streams resulta adecuado para colas simples con grupos de consumidores. Del análisis se concluye que gRPC (gRPC Authors, 2026) y Redis Streams (Redis, s. f.-a) cubren las necesidades del prototipo sin requerir una infraestructura de mayor alcance: el primero permite la entrega inmediata mediante streaming bidireccional, y el segundo habilita el consumo asíncrono y la confirmación de mensajes. El valor diferenciador de Dominus no es competir con brokers consolidados, sino integrar tiempo real, consumo asíncrono e idempotencia dentro de una interfaz homogénea.

III. Objetivos y Metodología

El objetivo general es diseñar e implementar un prototipo de broker de mensajería híbrido que integre comunicación en tiempo real mediante gRPC y comunicación asíncrona respaldada por Redis Streams, evaluando su comportamiento funcional, su usabilidad técnica y su nivel de seguridad. De este objetivo general se derivan los siguientes objetivos específicos:

Definir un contrato de comunicación tipado mediante Protocol Buffers que reduzca los errores de integración entre servicios.

Implementar un servidor broker en Go capaz de gestionar múltiples conexiones concurrentes mediante los servicios BrokerAPI y SqsAPI.

Incorporar un mecanismo de idempotencia y confirmación (Ack) que controle el procesamiento duplicado de mensajes.

Proporcionar un SDK cliente que simplifique la integración de productores y consumidores.

Validar el prototipo mediante pruebas unitarias, pruebas de integración, una evaluación de usabilidad técnica y un análisis de ciberseguridad.

El desarrollo de este trabajo siguió un enfoque iterativo e incremental, que permitió construir la solución de manera progresiva, incorporando retroalimentación en cada fase y ajustando las decisiones de diseño conforme avanzaba la implementación. Se prefirió este enfoque frente a un modelo en cascada por su adaptabilidad a un proyecto donde no todos los requisitos podrían definirse desde el inicio, ya que las entregas parciales permiten detectar inconsistencias entre componentes tempranamente.

La metodología se organizó en seis fases con retroalimentación entre ellas. En la primera, análisis del problema, se identificaron las limitaciones de los sistemas de mensajería existentes en escenarios que requieren comunicación en tiempo real, alta concurrencia y control de duplicados. En la segunda, definición de requisitos, se distinguieron los siguientes requisitos:

**Requisitos funcionales:**

- Permitir la publicación de mensajes por parte de múltiples productores.
- Distribuir mensajes hacia uno o múltiples suscriptores en tiempo real mediante BrokerAPI.
- Soportar la publicación, el consumo y la confirmación de mensajes mediante SqsAPI con modelo pull.
- Controlar duplicados mediante claves de idempotencia con tiempo de vida configurable.
- Gestionar mensajes pendientes no confirmados y permitir su reentrega.
- Exponer un SDK que simplifique la integración de clientes productores y consumidores.

**Requisitos no funcionales:**

- Baja latencia en la entrega de mensajes.
- Capacidad para gestionar múltiples conexiones concurrentes sin degradación del rendimiento.
- Observabilidad mediante logs estructurados, métricas y endpoints de salud.
- Arquitectura desacoplada que facilite las pruebas y la evolución futura del sistema.

En la tercera fase, diseño de la solución, se definió una arquitectura basada en el patrón de puertos y adaptadores (Cockburn, 2005), organizada en cinco capas: clientes externos o SDK, entrada gRPC, aplicación, dominio e infraestructura. En la cuarta fase, implementación, se construyó el prototipo en Go, incluyendo el contrato Protobuf, los servicios BrokerAPI y SqsAPI, la integración con Redis Streams, el mecanismo de idempotencia con claves de tiempo de vida configurable, el SDK cliente y un sistema de logs, métricas y endpoints de salud.

En la quinta fase, experimentación y pruebas, se diseñaron escenarios para validar el comportamiento del sistema bajo distintas condiciones de carga y concurrencia, incluyendo la distribución a múltiples suscriptores, la publicación concurrente desde múltiples productores y la reentrega de mensajes pendientes. En la sexta fase, evaluación de resultados, se analizaron métricas de latencia, capacidad de procesamiento, consistencia de entrega ante fallos parciales y efectividad del mecanismo de idempotencia.

Este enfoque resulta adecuado porque, como señala Sommerville (2016), los modelos iterativos son especialmente apropiados cuando los requisitos del sistema no pueden especificarse por completo desde el inicio, que es precisamente el caso de un broker cuyas decisiones críticas de diseño solo pueden validarse en la práctica conforme avanza la implementación.

IV. Contribución

La contribución principal de este trabajo es un broker de mensajería que organiza su arquitectura en cinco bloques; clientes externos o SDK, capa de entrada gRPC, capa de aplicación, capa de dominio y capa de infraestructura, siguiendo un patrón de puertos y adaptadores (Cockburn, 2005) que separa la lógica central del broker de los detalles técnicos de infraestructura, como el transporte gRPC, el almacenamiento en Redis, los mecanismos de monitoreo y la configuración del entorno.

Los clientes externos representan las aplicaciones que desean publicar o consumir mensajes mediante el broker, ya sea comunicándose directamente con lo definido en Protocol Buffers o a través del SDK, que oculta parte de la complejidad técnica de gRPC. La capa de entrada está formada por los servicios gRPC expuestos por el broker: BrokerAPI, orientado a comunicación en tiempo real mediante streaming de cliente, de servidor y bidireccional, y SqsAPI, orientado a operaciones tipo cola. La capa de aplicación coordina los casos de uso del sistema sin depender de una tecnología específica, mientras que la capa de dominio define las entidades, los contratos internos y los puertos que permiten a la aplicación comunicarse con componentes externos sin depender de implementaciones concretas. Finalmente, la capa de infraestructura contiene los adaptadores técnicos: la comunicación gRPC de entrada y salida, la conexión con Redis Streams, el control de idempotencia, los endpoints de monitoreo, los logs, las métricas y la configuración del entorno.

El sistema soporta dos flujos principales. En el flujo de comunicación en tiempo real, un cliente envía mensajes al broker mediante gRPC; el broker identifica los suscriptores y distribuye el contenido de forma inmediata, lo que resulta adecuado para propagación de eventos, notificaciones o comunicación bidireccional entre servicios. En el flujo asíncrono, un productor publica un mensaje mediante la operación Producer, que se almacena temporalmente en Redis Streams; un consumidor solicita mensajes mediante la operación Consumer, y al finalizar su procesamiento confirma mediante la operación Ack, lo que desacopla a productores y consumidores en el tiempo, ya que el productor no necesita esperar a que el consumidor procese el mensaje en el mismo instante.

La distribución en tiempo real se apoya en el patrón fan-out/fan-in: el broker centraliza la distribución de un evento publicado por un productor hacia varios consumidores (fan-out), evitando que el productor gestione conexiones individuales con cada receptor, y posteriormente recoge las respuestas de vuelta hacia el flujo o punto central (fan-in). La implementación se apoya en las goroutines y los canales del lenguaje Go, que permiten la ejecución concurrente y la comunicación entre flujos de forma directa. Este patrón introduce riesgos que deben gestionarse de forma explícita: un suscriptor lento puede bloquear el flujo y generar backpressure, un envío sin límites puede elevar el consumo de memoria, y una gestión inadecuada del cierre de los canales puede provocar fugas de goroutines, por ello se consideraron necesarios límites de concurrencia y políticas de reintento en la capa de infraestructura.

En el flujo asíncrono, el adaptador de persistencia traduce cada operación del caso de uso a un comando nativo de Redis Streams, la publicación ejecuta XADD para registrar la entrada en el stream, el consumo ejecuta XREADGROUP para recuperar nuevas entradas asociadas al grupo de consumidores correspondiente (quedando marcadas como pendientes hasta su confirmación), y el Ack ejecuta XACK para retirar la entrega de la lista de pendientes, sin eliminar la entrada original del stream, cuya eliminación física depende de la política de recorte configurada. El control de idempotencia se apoya en una clave asociada a cada operación, que se conserva temporalmente en Redis con un tiempo de vida configurable: la comprobación se realiza mediante una escritura condicional y atómica, de forma que, si la clave no existe, se registra y el procesamiento continúa, y si ya existe, el mensaje se trata como una repetición. La elección del tiempo de expiración implica una decisión de compromiso, ya que un periodo demasiado corto puede permitir duplicados tardíos y uno demasiado largo incrementa el consumo de memoria.

Entre las características funcionales implementadas destacan:

- Un contrato de comunicación definido con Protocol Buffers, que reduce errores de integración entre servicios.
- Un servidor broker implementado en Go, que aprovecha su capacidad para el manejo de múltiples conexiones simultáneas.
- Un mecanismo de idempotencia basado en claves con tiempo de vida configurable en Redis, orientado a prevenir el procesamiento duplicado de mensajes.
- Un SDK cliente que encapsula la comunicación con el broker y reduce la barrera de integración.
- Mecanismos transversales de observabilidad (logs estructurados, métricas y endpoints de salud) y de seguridad (autenticación mediante token y soporte de TLS).

Estas características delimitan el alcance de la primera versión del prototipo: no se pretende garantizar un orden global entre los flujos ni una escalabilidad equivalente a la de plataformas consolidadas, aspectos que se consideran líneas de mejora futura.

V. Resultados

_Resultados de las pruebas unitarias_

Las pruebas unitarias se enfocaron en validar los principales casos de uso del broker antes de ejecutar las pruebas de integración, sin levantar todo el ecosistema ni depender de Redis, Docker u otras herramientas externas. El proyecto organiza los casos unitarios en el directorio tests/units, separado de tests/integration, donde se ubican las pruebas que sí requieren infraestructura o comunicación real. Fueron desarrolladas con el framework nativo de Go mediante el paquete testing, apoyadas en mocks y dobles de prueba para simular dependencias como clientes de memoria y de comunicación, lo que permitió validar la lógica de aplicación sin ejecutar la infraestructura completa.

Se ejecutaron 143 pruebas y subpruebas, todas con resultado PASS. La cobertura global instrumentada fue del 91,8 % sobre sentencias, y los casos de uso principales del flujo asíncrono (Producer, Consumer, Ack y NewSqs) y del flujo de streaming (StreamClientConn, StreamServerConn, StreamBiConn y NewBroker) alcanzaron una cobertura del 100 %.

La Tabla 11 resume los módulos de prueba considerados, el código evaluado y el resultado obtenido en cada caso; así vincula los flujos principales con la evidencia unitaria.

**Tabla 11**

*Módulos de prueba unitaria* 

|**Módulo**|**Objetivo**|**Resultado**|
|---|---|---|
|producer_test|Publicación y rechazo de payload vacío|PASS|
|consumer_test|Recuperación de mensajes|PASS|
|ack_test|Confirmación y rechazo de ID inválido|PASS|
|stream_client_test|Envío desde cliente|PASS|
|stream_server_test|Entrega desde servidor|PASS|
|stream_bidirectional_test|Intercambio bidireccional|PASS|

_Nota._ Elaboración propia. La tabla presenta el objetivo y el resultado de los seis módulos incluidos en las pruebas unitarias.

_Resultados de las pruebas de integración_

Las pruebas de integración validan que los distintos componentes del sistema funcionan correctamente al conectarse entre sí. Se implementaron en Go con el paquete de pruebas estándar, apoyadas en bibliotecas auxiliares: miniredis/v2 para simular un servidor Redis sin infraestructura real, bufconn de google.golang.org/grpc/test para crear una conexión gRPC en memoria sin abrir sockets reales, gomock para generar dobles controlados de las dependencias salientes, y el contrib de OpenTelemetry para añadir trazabilidad a los flujos de streaming bajo prueba.

Se seleccionaron tres pruebas que cubren los patrones soportados por el broker. TestProducerFlow verificó que un mensaje enviado por gRPC atraviesa el caso de uso Producer y queda registrado en Redis Stream con el identificador y el cuerpo esperado. TestAckFlow validó el ciclo completo de confirmación (producir, consumir y confirmar mediante Ack), comprobando mediante XPendingExt que tras el Ack el mensaje deja de aparecer como pendiente para el grupo de consumidores. TestBidirectionalStreamFlow, el escenario más exigente, comprobó que el broker retransmite mensajes bidireccionales hacia dos suscriptores simultáneos integrando autenticación, compresión gzip y trazabilidad con OpenTelemetry sobre conexiones TCP reales, el cliente envió dos mensajes y se verificaron las cuatro respuestas esperadas (dos suscriptores por dos mensajes), comprobando que cada payload llegó exactamente dos veces. Las tres pruebas obtuvieron resultado PASS, sin condiciones de carrera detectadas por el detector -race de Go (The Go Team, s. f.).

La Tabla 12 resume las pruebas de integración ejecutadas, el archivo de prueba correspondiente y el resultado obtenido en cada caso, lo que permite comparar los flujos SQS y de streaming.

**Tabla 12**

*Pruebas de integración ejecutadas* 

|**Prueba**|**Función de prueba**|**Resultado**|
|---|---|---|
|broker_sqs_flow_test|TestProducerFlow|PASS|
|broker_sqs_flow_test|TestAckFlow|PASS|
|broker_stream_flow_test|TestBidirectionalStreamFlow|PASS|

_Nota._ Elaboración propia. La tabla relaciona cada archivo con la función de prueba ejecutada y su resultado.

**Usabilidad técnica.** A diferencia de una aplicación con interfaz gráfica orientada a usuarios finales, el broker es una herramienta backend dirigida a desarrolladores e integradores, por lo que su usabilidad no se evaluó en términos visuales, sino desde la facilidad con la que un usuario técnico puede comprender, configurar, ejecutar y utilizar sus operaciones principales. La evaluación combinó una revisión de usabilidad con pruebas basadas en cinco tareas representativas:

Preparar el entorno de ejecución: se revisó si la documentación permitía identificar los requisitos, las dependencias y los comandos necesarios para montar el entorno local.

Replicar las pruebas documentadas en el repositorio: fue posible montar el entorno y replicar las pruebas sin dificultad, lo que representa un punto favorable, ya que estas sirven además como guía práctica para entender los flujos principales del sistema.

Comprender el flujo productor-consumidor-Ack: este flujo resulta comprensible cuando se observa como una secuencia de tres pasos, aunque puede resultar confuso para usuarios que no conozcan previamente los conceptos de broker, cola o consumidor.

Revisar el contrato gRPC definido mediante Protocol Buffers: la lectura del contrato Protobuf por sí sola no siempre resulta suficiente sin ejemplos mínimos de uso que orienten al integrador.

Revisar los mecanismos de diagnóstico disponibles durante la ejecución: los logs, las salidas de consola, los endpoints de salud y la documentación de pruebas resultan elementos importantes para reducir el tiempo de diagnóstico ante fallos.

Los resultados generales muestran que la herramienta tiene una usabilidad adecuada para un prototipo académico orientado a usuarios técnicos: la organización por módulos, la documentación y la disponibilidad de pruebas permiten comprender progresivamente el propósito del sistema, y la posibilidad de replicar pruebas ya preparadas facilita validar el comportamiento principal del broker sin tener que construir casos desde cero. La principal barrera identificada es la curva de aprendizaje inicial para usuarios sin experiencia previa en el stack tecnológico empleado.

_Resultados de las pruebas de ciberseguridad_

El análisis se dividió entre el backend (dominus-broker), responsable de exponer los servicios gRPC y HTTP, validar tokens y comunicarse con Redis, y el cliente (dominus-sdk), que construye las conexiones, agrega metadatos y serializa las solicitudes. El laboratorio se ejecutó en un entorno local con Docker, limitado a 127.0.0.1, revisando en el backend la autenticación, la concurrencia, los destinos, los límites de payload y TLS, y en el SDK la validación de destinos, la protección del canal TLS, el manejo de errores y la serialización.

Esta distinción entre backend y SDK resulta relevante porque la seguridad del sistema no puede delegarse por completo al cliente: el SDK puede rechazar un destino mal formado, pero una solicitud construida por otro cliente podría invocar directamente al broker. Por ello, las validaciones de autenticación, autorización, límites de payload e idempotencia deben residir en el backend, que constituye la frontera de confianza real del sistema.

Para este análisis, una operación se consideró idempotente cuando produce el mismo efecto sobre un mensaje aunque el cliente repita su envío o recepción, si dicha repetición llega asociada a la misma clave. La idempotencia se implementa mediante una clave asociada a cada solicitud: si la misma clave llega dos veces, el broker debería procesar la primera y reconocer las siguientes como duplicadas, protegiendo así las operaciones de publicación, consumo y suscripción frente a reintentos causados por timeouts o por solicitudes concurrentes.

El hallazgo BE-01 mostró que el middleware de autenticación gRPC lee la posición cero de los metadatos sin comprobar su longitud; cuando falta el encabezado x-api-key, Go produce un error de índice fuera de rango identificado como CWE-129 (MITRE, 2026a), que detiene el proceso completo, dejando de atender tanto HTTP como gRPC. El registro de arranque confirmó el panic, y una comprobación posterior del endpoint de salud no pudo establecer conexión, corroborando la indisponibilidad.

El hallazgo BE-03 identificó una condición de carrera en el mecanismo de idempotencia, al lanzar veinte solicitudes concurrentes con la misma clave, repetidas en veinte rondas, el número de solicitudes aceptadas osciló entre 3 y 20 de 20, en lugar de exactamente una. La causa es que el middleware primero consulta Redis y después guarda la clave en una gorutina independiente, por lo que varias solicitudes pueden atravesar la verificación antes de que Redis registre la reserva.

En el SDK, CL-01 confirmó que la validación del certificado TLS rechaza correctamente cadenas de confianza inválidas, aunque los casos negativos se comunican mediante panics capturados por la prueba y no mediante errores explícitos. CL-03 mostró que el SDK acepta destinos que no cumplen el formato host:puerto y carece de una lista de destinos autorizados independiente. CL-05 confirmó que un error de serialización JSON no controlado permite el envío de una solicitud con cuerpo vacío sin advertir al consumidor del SDK, debilidad identificada como CWE-252 (MITRE, 2026b).

La Tabla 13 resume los cinco hallazgos, el componente afectado y su severidad, por lo que facilita distinguir los riesgos del backend de las mejoras requeridas en el SDK.

**Tabla 13**

*Resumen de hallazgos del análisis de ciberseguridad* 

|**ID**|**Componente**|**Resultado**|
|---|---|---|
|BE-01|Backend|Vulnerabilidad crítica de disponibilidad|
|BE-03|Backend|Vulnerabilidad de integridad (duplicados)|
|CL-01|SDK|Mejora recomendada (manejo de errores)|
|CL-03|SDK|Mejora recomendada (validación de entrada)|
|CL-05|SDK|Vulnerabilidad de integridad|

_Nota._ Elaboración propia. La tabla sintetiza los hallazgos identificados en el backend y el SDK y la clasificación asignada a cada resultado.

VI. Discusión

Las pruebas unitarias y de integración confirman que la lógica principal del broker (publicación, consumo, confirmación y los tres patrones de streaming) funciona correctamente de forma aislada y en combinación con Redis y la capa gRPC, lo que respalda la arquitectura de puertos y adaptadores adoptada como base para las pruebas y la evolución futura del sistema. La cobertura elevada de los casos de uso principales refuerza la fiabilidad de la lógica de dominio y de aplicación.

Sin embargo, el análisis de ciberseguridad evidencia que la robustez a nivel funcional no se traslada automáticamente a la robustez frente a condiciones adversas o de concurrencia real. El hallazgo BE-01 constituye una vulnerabilidad de disponibilidad crítica, ya que una única solicitud sin token puede derribar el servicio completo, este tipo de defecto no se manifiesta en pruebas unitarias centradas en el camino feliz, lo que subraya la importancia de complementar la validación funcional con pruebas de seguridad dirigidas. De forma similar, el hallazgo BE-03 muestra que la garantía de idempotencia, uno de los objetivos específicos del proyecto, no se cumple bajo concurrencia real, aun cuando el detector de carreras de datos de Go no reporta advertencias, la ausencia de una carrera de memoria no implica la ausencia de una carrera lógica distribuida.

Los hallazgos del SDK (CL-01, CL-03, CL-05) indican que, si bien los mecanismos de seguridad existen, su manejo de errores mediante panics y la ausencia de validaciones más estrictas de destino y de serialización pueden ocultar fallos al consumidor del SDK, lo que resulta relevante para un componente pensado para integrarse en sistemas de terceros. La evaluación de usabilidad y el análisis de ciberseguridad son, en este sentido, complementarios, un sistema puede ser fácil de comprender y usar en condiciones normales y, al mismo tiempo, ser frágil ante entradas adversas o concurrencia real como ocurre con el broker.

En conjunto, estos resultados sitúan a el broker como un prototipo funcional, pero que requeriría un ciclo adicional de correcciones antes de considerarse apto para un entorno de producción, en línea con la literatura que señala que la entrega al menos una vez y el paralelismo introducen riesgos de duplicación y de orden que deben gestionarse explícitamente (Kleppmann, 2017; Richardson, 2018).

**Limitaciones.** El alcance de la propuesta está delimitado por varias decisiones de diseño explícitas. La disponibilidad de la capa de persistencia depende de una única instancia de Redis, ya que la primera versión no incluye replicación, Redis Sentinel ni Redis Cluster. Tampoco se garantiza un orden global entre todos los consumidores: Redis mantiene el orden de las entradas dentro del stream, pero la ejecución concurrente puede alterar el orden de finalización entre distintos consumidores. Además, la persistencia se limita a los mensajes del flujo asíncrono, ya que la comunicación en tiempo real mediante streaming no almacena automáticamente los mensajes enviados. Estas limitaciones, sumadas a los hallazgos del análisis de ciberseguridad, delimitan con precisión los escenarios en los que el broker resulta adecuado en su estado actual y las líneas de evolución necesarias para versiones posteriores.

VII. Conclusiones

Este trabajo ha permitido diseñar, implementar y evaluar Dominus, un broker de mensajería híbrido que combina comunicación en tiempo real mediante gRPC y comunicación asíncrona respaldada por Redis Streams. Los objetivos específicos planteados se cumplieron parcialmente el contrato Protobuf, el servidor en Go, el mecanismo de idempotencia, el SDK cliente y la observabilidad básica se implementaron y fueron validados mediante 143 pruebas unitarias y 3 pruebas de integración, todas con resultado PASS y una cobertura global del 91,8 %; no obstante, el análisis de ciberseguridad reveló que el objetivo de control de idempotencia no se sostiene bajo concurrencia real y que existe al menos una vulnerabilidad de disponibilidad crítica en el backend, además de puntos de mejora en el manejo de errores del SDK.

En términos más generales, este trabajo confirma que integrar comunicación en tiempo real y consumo asíncrono en un mismo broker es técnicamente viable con un esfuerzo de implementación moderado, pero que sostener las garantías de idempotencia y disponibilidad bajo condiciones adversas exige un esfuerzo de validación adicional que va más allá de las pruebas funcionales convencionales.

## Referencias del artículo

> [!warning] Referencias repetidas respecto de la sección 6
> Las 18 entradas de esta subsección también aparecen en la bibliografía general: Apache Kafka, Apache Pulsar, Cockburn, Gartner Peer Community, Google Cloud, gRPC Authors, IMARC Group, Kleppmann, MITRE (dos obras), NATS, Newman, RabbitMQ, Redis, Richards y Ford, Richardson, Sommerville y The Go Team. Se conservan aquí para que el artículo pueda leerse como una pieza autónoma; si la normativa de entrega de UNIR exige una única lista para todo el documento, esta subsección debe eliminarse después de comprobar que el anexo siga vinculado a la bibliografía general.

Apache Kafka. (s. f.). *Documentation*. https://kafka.apache.org/documentation/

Apache Pulsar. (s. f.). *Messaging*. https://pulsar.apache.org/docs/3.0.x/concepts-messaging/

Cockburn, A. (2005, 4 de septiembre). *Hexagonal architecture*. https://alistair.cockburn.us/hexagonal-architecture

Gartner Peer Community. (2023). *Microservices architecture: Have engineering organizations found success?* https://www.gartner.com/peer-community/oneminuteinsights/omi-microservices-architecture-have-engineering-organizations-found-success-u6b

Google Cloud. (s. f.). *What is Pub/Sub?* Google Cloud Documentation. https://cloud.google.com/pubsub/docs/overview

gRPC Authors. (2026, 11 de mayo). *Core concepts, architecture and lifecycle*. https://grpc.io/docs/what-is-grpc/core-concepts/

IMARC Group. (2024). *Microservices architecture market share, size 2025–2033*. https://www.imarcgroup.com/microservices-architecture-market

Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media.

MITRE. (2026a, 30 de abril). *CWE-129: Improper validation of array index*. Common Weakness Enumeration. https://cwe.mitre.org/data/definitions/129.html

MITRE. (2026b, 30 de abril). *CWE-252: Unchecked return value*. Common Weakness Enumeration. https://cwe.mitre.org/data/definitions/252.html

NATS. (s. f.). *Pull consumers in depth*. NATS Documentation. https://docs.nats.io/learn/jetstream/pull-consumers

Newman, S. (2021). *Building microservices* (2nd ed.). O'Reilly Media.

RabbitMQ. (s. f.). *Consumer acknowledgements and publisher confirms*. https://www.rabbitmq.com/docs/4.2/confirms

Redis. (s. f.-a). *Redis Streams*. https://redis.io/docs/latest/develop/data-types/streams/

Richards, M., & Ford, N. (2020). *Fundamentals of software architecture*. O'Reilly Media.

Richardson, C. (2018). *Microservices patterns: With examples in Java*. Manning Publications.

Sommerville, I. (2016). *Software engineering* (10th ed.). Pearson.

The Go Team. (s. f.). *Data race detector*. The Go Programming Language. https://go.dev/doc/articles/race_detector

# Anexo B. Puesta en marcha

> [!attention] Revisión ortotipográfica del anexo B
> Se observan oraciones incompletas, encabezados con punto final y mayúsculas inconsistentes, además de errores como "assosiados", "duirante", "concidad", "commandos", "require" y "commando". Conviene hacer una corrección lingüística conjunta cuando el equipo valide los pasos técnicos definitivos.

## Objetivo y alcance

Este anexo explica cómo poner en marcha Dominus Broker en una infraestructura nueva. El procedimiento está dirigido a desarrolladores y cubre Windows y Linux. Incluye una ejecución local controlada, las comprobaciones funcionales y una ruta de despliegue con Docker y Terraform.

Dominus es un broker híbrido escrito en Go. Expone BrokerAPI para flujos gRPC en tiempo real y SqsAPI para operaciones de tipo cola sobre Redis Streams. El proceso también abre un monitor HTTP con los endpoints /health y /metrics.

La ruta principal de este anexo ejecuta Redis en Docker y el broker desde el código fuente. Esta separación permite detectar con claridad si un fallo pertenece a Redis, a la configuración o al proceso Go. El despliegue completo en contenedores más adelante.

## Requisitos previos.

La Tabla 14 reúne las herramientas necesarias y aporta una referencia rápida de los requisitos y el uso de cada una. Las versiones se deben comprobar en la terminal que se utilizará durante la instalación.

**Tabla 14**

*Herramientas y requisitos para la puesta en marcha* 

|**Herramienta**|**Requisito**|**Uso**|
|---|---|---|
|Git|Cliente con acceso a los repositorios de Dominus|Obtener el código y sus dependencias privadas|
|Go|1.26.1 o una versión compatible con go.mod|Compilar, probar y ejecutar el broker|
|Docker Engine o Docker Desktop|Motor activo y accesible desde la terminal|Ejecutar Redis y, de forma opcional, el broker|
|PowerShell|5.1 o posterior en Windows|Cargar la configuración y usar Makefile.ps1|
|Bash|Disponible en Linux|Cargar la configuración y ejecutar los comandos del sistema|
|curl|Cliente HTTP|Comprobar /health y /metrics|
|grpcurl|Recomendado|Consultar la reflexión gRPC y probar SqsAPI|
|Terraform|Opcional|Crear la pila Docker definida en terraform/|

_Nota._ Elaboración propia. La tabla identifica las herramientas requeridas u opcionales, su requisito de versión o acceso y su función durante la instalación.

Los siguientes comandos confirman que las herramientas principales están disponibles:

```text
git --version  
go version  
docker version  
grpcurl --version  
terraform version
```

grpcurl y Terraform son opcionales para el primer arranque. Sin grpcurl se puede validar gRPC mediante las pruebas de integración.

## Clonar los repositorios.

Los repositorios assosiados con este proyecto.

- dominus-broker, que ejecuta el servicio;
- dominus-proto-definition, que define los contratos gRPC;
- dominus-sdk, que facilita el consumo desde Go;
- consumer-example, que muestra un consumidor y un suscriptor.

En Windows sin Bash se clonan los repositorios con Git desde PowerShell:

```text
Set-Location Dominus-Broker-Repos  
git clone https://github.com/unir-broker-tfm/dominus-broker.git  
git clone https://github.com/unir-broker-tfm/dominus-sdk.git  
git clone https://github.com/unir-broker-tfm/consumer-example.git  
git clone https://github.com/unir-broker-tfm/dominus-proto-definition.git
```

El broker depende de github.com/MBI-88/dominus-proto-definition v1.3.7. Si ese módulo es privado, la cuenta de Git debe tener permiso de lectura.

## Arranque inicial.

Los comandos de esta sección se ejecutan desde Dominus-Broker-Repos/dominus-broker.

Windows:

```text
Set-Location Dominus-Broker-Repos\dominus-broker  
go env GOMOD  
go mod download
```

Linux:

```text
cd Dominus-Broker-Repos/dominus-broker  
go env GOMOD  
go mod download
```

go env GOMOD debe devolver la ruta de dominus-broker/go.mod. Si go mod download informa que no encuentra dominus-proto-definition, se revisan las credenciales del repositorio privado antes de continuar.

## Preparacion de Redis

El broker crea un consumer group duirante el arranque y termina con error si no se puede conectar a redis. Para la configuracion local concida con el proyecto redis se construye con terraform/dev/redis/Dockerfile. Ese archivo utiliza Redis 7.2 y copia redis.conf, donde se define el usuario ACL dominus, la contraseña local de demostración dominus y dos bases lógicas.

Estas credenciales sólo se usan en un entorno local aislado. En una infraestructura compartida se deben cambiar en redis.conf y en el JSON del broker antes de crear las imágenes.

### **Windows**

Desde Dominus-Broker-Repos\dominus-broker:

```text
docker build --tag dominus-redis:7.2 .\terraform\dev\redis  
docker run --detach `  
--name redis `  
--publish 127.0.0.1:6379:6379 `  
dominus-redis:7.2  
docker ps --filter "name=redis"
```

### **Linux**

Desde Dominus-Broker-Repos/dominus-broker:

```text
docker build --tag dominus-redis:7.2 ./terraform/dev/redis  
docker run --detach \  
--name redis \  
--publish 127.0.0.1:6379:6379 \  
dominus-redis:7.2  
docker ps --filter "name=redis"
```

El estado del contenedor debe ser Up. La conexión se comprueba sin publicar una contraseña nueva en el documento:

```text
docker exec redis redis-cli --user dominus --pass dominus PING
```

El resultado esperado es PONG. redis-cli puede mostrar una advertencia porque la contraseña aparece como argumento. Para una operación real se debe usar un mecanismo de secretos o la variable REDISCLI_AUTH durante la sesión.

Si el contenedor ya existe pero está detenido, se recupera con:

```text
docker start redis
```

## Configuración de Dominus Broker

El código actual no selecciona automáticamente env.local.json por medio del indicador -prod. config.NewConfig() lee el JSON completo desde la variable APP_CONFIG y detiene el proceso si la variable está vacía o si faltan los campos obligatorios.

La Tabla 15 resume los bloques de configuración y permite localizar los parámetros que controlan transporte, monitorización, certificados, Redis y logs.

**Tabla 15**

*Bloques de configuración de `APP_CONFIG`* 

|**Bloque**|**Campos principales**|**Función**|
|---|---|---|
|grpc_config|port, api_token|Listener gRPC y secreto compartido|
|rest_config|port, api_token, allow_origins|Monitor HTTP, autenticación y CIDR permitido|
|cert_config|key_file, ssl_ca_cert, ssl_cert|Archivos usados para TLS|
|redis_config|host, puerto, credenciales, DB, stream y grupo|Redis Streams e idempotencia|
|log_config|log_mode, log_url|Salida de eventos del broker|

_Nota._ Elaboración propia a partir de la estructura de configuración del proyecto. La tabla resume los campos principales y la función de cada bloque de `APP_CONFIG`.

Las plantillas llaman log_config al último bloque. En config.Config, sin embargo, ese campo conserva la etiqueta mapstructure:"infra_config". Si log_mode no se aplica aunque el servicio arranque, se debe corregir esa diferencia en el código o utilizar el nombre que espere la versión compilada. El broker no valida este bloque durante el arranque.

Para una ejecución local se parte de env/template.json y se guarda una copia fuera del repositorio. El siguiente contenido es un ejemplo funcional para el Redis creado en la sección anterior:

```text
{  
"grpc_config": {  
"port": 5000,  
"api_token": "cambie-esta-clave-grpc"  
},  
"rest_config": {  
"port": 8000,  
"api_token": "cambie-esta-clave-rest",  
"allow_origins": "0.0.0.0/0"  
},  
"cert_config": {  
"key_file": "./certs/cert.key",  
"ssl_ca_cert": "./certs/ca_cert.pem",  
"ssl_cert": "./certs/cert.pem"  
},  
"redis_config": {  
"port": 6379,  
"memory_db": 0,  
"checker_db": 1,  
"host": "localhost",  
"password": "dominus",  
"tls": false,  
"username": "dominus",  
"idem_potency_ex": 10,  
"stream_id": "consumer",  
"group_id": "consumer-group"  
},  
"log_config": {  
"log_mode": "cmd",  
"log_url": ""  
}  
}
```

0.0.0.0/0 permite cualquier IP en el middleware del monitor. Se mantiene para facilitar la práctica local, pero debe sustituirse por el CIDR de administración en una infraestructura compartida.

### **Carga De la Configuración En Windows**

Desde Dominus-Broker-Repos\dominus-broker:

```text
$configPath = Join-Path $env:TEMP 'dominus.runtime.json'  
Copy-Item -LiteralPath '.\env\template.json' -Destination $configPath -Force  
notepad $configPath
```

Se sustituye el contenido por el JSON anterior y se cambian las dos claves de ejemplo. Después se carga la variable:

```text
$env:APP_CONFIG = Get-Content -Raw -LiteralPath $configPath  
$env:DOMINUS_GRPC_TOKEN = 'cambie-esta-clave-grpc'  
$env:DOMINUS_REST_TOKEN = 'cambie-esta-clave-rest'
```

Los valores de DOMINUS_GRPC_TOKEN y DOMINUS_REST_TOKEN deben coincidir con el JSON, pero no forman parte de la configuración del broker; se usan en los comandos de comprobación.

### **Carga De la Configuración En Linux**

Desde Dominus-Broker-Repos/dominus-broker:

```text
install -m 600 env/template.json /tmp/dominus.runtime.json  
${EDITOR:-vi} /tmp/dominus.runtime.json  
export APP_CONFIG="$(tr -d '\r\n' < /tmp/dominus.runtime.json)"  
export DOMINUS_GRPC_TOKEN='cambie-esta-clave-grpc'  
export DOMINUS_REST_TOKEN='cambie-esta-clave-rest'
```

> [!warning] Comando reconstruido después de la exportación
> La línea de Linux estaba concatenada y era inejecutable. Se separaron el editor y la asignación de `APP_CONFIG`; el equipo debe validarla en Bash antes de publicar el anexo.

Se sustituye el contenido del archivo por el JSON de ejemplo y se utilizan los mismos valores en las variables auxiliares.

## Pruebas Automatizadas Antes Del Arranque

Las pruebas detectan errores de compilación, integración y concurrencia antes de abrir los puertos del servicio. Desde la raíz de dominus-broker se ejecuta:

```text
go test -race -count=1 ./...
```

En Windows también está disponible el wrapper del proyecto:

.\Makefile.ps1 -Target test

-race activa el detector de carreras de Go y -count=1 evita reutilizar resultados almacenados. La ejecución correcta termina con ok en los paquetes de pruebas. Si sólo se desea revisar la parte de streaming:

```text
go test -race -count=1 -v ./tests/integration/broker_stream_flow_test/...
```

Estas pruebas crean peers controlados y ejercitan ClientStream, ServerStream y BidirectionalStream sin exigir servicios suscriptores externos.

El árbol actual separa pruebas en tests/units y tests/integration. Algunas páginas internas todavía muestran tests/cases o nombres antiguos como broker_flow_test; esos ejemplos no se deben usar sin comprobar primero las carpetas disponibles con go list ./tests/….

## Validación Del Monitor HTTP

### **Windows**

```text
$headers = @{ 'x-api-key' = $env:DOMINUS_REST_TOKEN }  
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/health' -Headers $headers
```

### **Linux**

```text
curl --fail --silent --show-error \  
-H "x-api-key: ${DOMINUS_REST_TOKEN}" \  
http://127.0.0.1:8000/health
```

La respuesta esperada es:

Health ok

El endpoint de métricas usa el mismo token.

**Windows:**

```text
Invoke-WebRequest `  
-Uri 'http://127.0.0.1:8000/metrics' `  
-Headers $headers | Select-Object -ExpandProperty Content
```

**Linux:**

```text
curl --fail --silent --show-error \  
-H "x-api-key: ${DOMINUS_REST_TOKEN}" \  
http://127.0.0.1:8000/metrics
```

La salida contiene métricas Prometheus, entre ellas cpu_usage_percentage, memory_usage_percentage y contadores gRPC. Una llamada sin x-api-key o con un valor distinto debe ser rechazada.

## Despliegue Completo Con Docker

Esta ruta ejecuta el broker y Redis en la misma red Docker. El Dockerfile del broker compila para Linux, copia env/ y utilize env/entrypoint.sh para cargar APP_CONFIG desde env.prod.json.

Hay tres condiciones previas:

1. el build necesita acceso de lectura a dominus-proto-definition;
2. el contexto debe container el directorio certs porque el Dockerfile lo copia;
3. la configuración del contenedor debe usar redis como host, no localhost.

Para no hornear secretos en la imagen, se prepara un JSON externo y se monta sobre /app/env/env.prod.json. Debe tener estos cambios respecto al ejemplo local:

```text
{  
"cert_config": {  
"key_file": "/etc/dominus/certs/cert.key",  
"ssl_ca_cert": "/etc/dominus/certs/ca_cert.pem",  
"ssl_cert": "/etc/dominus/certs/cert.pem"  
},  
"redis_config": {  
"host": "redis"  
}  
}
```

El archivo real debe conservar todos los bloques del JSON completo; el fragmento anterior sólo muestra los campos que cambian.

### **Construcción En Windows**

Desde Dominus-Broker-Repos\dominus-broker:

```text
New-Item -ItemType Directory -Force -Path '.\certs' | Out-Null  
$secureToken = Read-Host 'Token de lectura de GitHub' -AsSecureString  
$credential = New-Object System.Net.NetworkCredential('', $secureToken)  
$env:GITHUB_TOKEN = $credential.Password  
docker build `  
--build-arg "GITHUB_TOKEN=$env:GITHUB_TOKEN" `  
--tag dominus-broker:local .  
Remove-Item Env:GITHUB_TOKEN
```

> [!warning] Comando reconstruido después de la exportación
> La asignación del token y `docker build` estaban unidos. Se separaron para recuperar la intención aparente, pero deben comprobarse el nombre exacto del argumento del `Dockerfile` y la sintaxis en PowerShell antes de la entrega.

### **Construcción En Linux**

Desde Dominus-Broker-Repos/dominus-broker:

```text
mkdir -p certs  
read -rsp 'Token de lectura de GitHub: ' GITHUB_TOKEN  
echo  
docker build \  
--build-arg GITHUB_TOKEN="${GITHUB_TOKEN}" \  
--tag dominus-broker:local .  
unset GITHUB_TOKEN
```

El Dockerfile actual recibe el token como build argument. Se debe evitar la salida detallada del build en evidencias académicas. Para un pipeline real conviene sustituir ese mecanismo por un secreto de BuildKit y comprobar que la credencial no quede en capas ni metadatos.

### **Creación De la Red Y Los Contenedores**

Los siguientes commandos son iguales en PowerShell y Bash:

```text
docker network create dominus  
docker build --tag dominus-redis:7.2 ./terraform/dev/redis  
docker run --detach --name redis --network dominus dominus-redis:7.2
```

Si ya se creó el contenedor Redis de la ruta local, se puede detener y retirar antes de iniciar esta variante:

```text
docker stop redis  
docker rm redis
```

En Linux, suponiendo que el JSON completo se guardó en /tmp/dominus.container.json:

chmod 644 /tmp/dominus.container.json

La imagen ejecuta el proceso como appuser, por lo que el archivo montado debe tener permiso de lectura para ese usuario. El modo 644 se limita a esta práctica con credenciales de demostración. En una infraestructura compartida se debe usar una ACL específica, un secreto de Docker o un mecanismo equivalente.

```text
docker run --detach \  
--name dominus-broker \  
--network dominus \  
--publish 5000:5000 \  
--publish 8000:8000 \  
--env MODE=prod \  
--mount type=bind,source=/tmp/dominus.container.json,target=/app/env/env.prod.json,readonly \  
dominus-broker:local
```

En Windows se crea una copia específica para el contenedor. Debe conservar el JSON completo, usar redis como host y utilizar las rutas de certificados bajo /etc/dominus/certs:

```text
$containerConfigPath = Join-Path $env:TEMP 'dominus.container.json'  
Copy-Item -LiteralPath $configPath -Destination $containerConfigPath -Force  
notepad $containerConfigPath
```

Después de guardar esos cambios, se monta la copia en modo de sólo lectura:

```text
docker run --detach `  
--name dominus-broker `  
--network dominus `  
--publish 5000:5000 `  
--publish 8000:8000 `  
--env MODE=prod `  
--mount "type=bind,source=$containerConfigPath,target=/app/env/env.prod.json,readonly" `  
dominus-broker:local
```

El estado y los logs se revisan con:

```text
docker ps --filter "name=dominus-broker"  
docker logs dominus-broker
```

La salida debe indicar MODE=prod, confirmar que encontró el archivo y anunciar los puertos 8000 y 5000. Las comprobaciones HTTP y gRPC se repiten con los tokens del JSON montado.

## Infraestructura Con Terraform

El directorio terraform/ crea una red Docker y módulos para Dominus, Redis, Nginx sidecar, Prometheus y Grafana. Esta ruta es útil para reconstruir el entorno completo, pero require configuración previa.

No hay un archivo .tfvars versionado y las variables raíz no tienen valores predeterminados. Se crea terraform/terraform.tfvars, que ya coincide con el patrón ignorado por Git:

```text
dominus_server_file = ".."  
dominus_server_container_cpu = "2"  
dominus_server_container_memory = 1024  
  
dominus_server_container_ports = [  
{ internal = 5000, external = 5000 },  
{ internal = 8000, external = 8000 }  
]  
  
redis_server_container_ports = [  
{ internal = 6379, external = 6379 }  
]  
  
prometheus_server_container_ports = [  
{ internal = 9090, external = 9090 }  
]  
  
grafana_server_container_ports = [  
{ internal = 3000, external = 3000 }  
]  
  
sidecar_server_container_ports = [  
{ internal = 80, external = 80 }  
]  
  
network_driver = "bridge"  
network_name = "dominus"
```

El token privado se pasa como variable de entorno y no se escribe en terraform.tfvars.

Antes de ejecutar Terraform en Linux, se cambia el proveedor de terraform/terraform.tf porque el archivo versionado apunta al named pipe de Windows:

```text
provider "docker" {  
host = "unix:///var/run/docker.sock"  
}
```

Windows:

```text
$env:TF_VAR_dominus_server_token = '<TOKEN_DE_LECTURA>'  
.\Makefile.ps1 -Target terraform-init  
.\Makefile.ps1 -Target terraform-validate  
.\Makefile.ps1 -Target terraform-plan  
.\Makefile.ps1 -Target terraform-apply  
Remove-Item Env:TF_VAR_dominus_server_token
```

Linux:

```text
export TF_VAR_dominus_server_token='<TOKEN_DE_LECTURA>'  
cd terraform  
terraform init  
terraform validate  
terraform plan  
terraform apply  
unset TF_VAR_dominus_server_token
```

En Windows, terraform/terraform.tf ya apunta a npipe:////.//pipe//docker_engine y no require ese cambio.

La configuración Terraform actual construye el broker con el env.prod.json incluido en la imagen y no monta un archivo externo. Su health check y el sidecar Nginx también contienen un token de ejemplo que debe coincidir con rest_config.api_token; si no coincide, Dominus puede arrancar pero aparecer como unhealthy y Prometheus no podrá leer /metrics.

El health check de Redis ejecuta redis-cli -p 6379 ping sin usuario ni contraseña, mientras que redis.conf exige autenticación. Esa comprobación puede devolver NOAUTH y marcar el contenedor como no saludable aunque Redis esté escuchando. Antes de aplicar Terraform se debe parametrizar el commando para autenticar al usuario ACL sin dejar la contraseña en el repositorio.

Estas condiciones hacen que la ruta Terraform requiera una adaptación previa: montar la configuración y los certificados desde un almacén seguro, parametrizar los tokens, corregir el health check de Redis y retirar la publicación de 6379. Redis sólo necesita set accessible dentro de la red Docker.

Los recursos creados se consultan con:

```text
terraform output  
docker ps
```

En Windows puede usarse ./Makefile.ps1 -Target terraform-output. La eliminación de esta infraestructura se realiza desde el mismo directorio con terraform destroy, después de revisar el plan de destrucción.

## **Solución De Problemas**

La Tabla 16 relaciona los fallos más frecuentes con una causa probable y una acción de comprobación o corrección, lo que facilita el diagnóstico durante la puesta en marcha.

**Tabla 16**

*Diagnóstico de fallos frecuentes* 

|**Síntoma**|**Causa probable**|**Comprobación y corrección**|
|---|---|---|
|APP_CONFIG is empty or not set|La variable no existe en esa terminal|Volver a cargar el JSON y ejecutar el broker en la misma sesión|
|RedisConfig.Host empty o RedisConfig.Port empty|JSON incompleto o clave con nombre incorrecto|Comparar el archivo con config/config.go y mantener redis_config en la raíz|
|Error WRONGPASS o autenticación Redis|Usuario y contraseña no coinciden con redis.conf|Comprobar dominus/dominus en local o actualizar ambos archivos|
|connection refused en 6379|Redis está detenido o el host es incorrecto|Ejecutar docker ps; usar localhost desde el host y redis desde la red Docker|
|failed to match token|Se usó un token incorrecto|Distinguir grpc_config.api_token de rest_config.api_token|
|idempotency not found|Falta idempotency-header|Añadir una clave no vacía a cada llamada unary|
|rate limit reached|La clave de idempotencia ya fue utilizada|Generar una clave nueva o esperar el TTL configurado|
|invalid message id|Ack no recibió el ID exacto de Redis Stream|Copiar messageId de la respuesta de Consumer|
|ResourceExhausted|El mensaje supera el límite gRPC|Reducir el payload o configurar límites coordinados en cliente y servidor|
|Fallo al descargar dominus-proto-definition|Falta acceso al módulo privado|Revisar la autenticación Git sin imprimir el token|
|El build Docker falla al copiar certs|El directorio no está en el contexto|Crear certs/ o proporcionar los certificados antes del build|
|Terraform solicita variables|No existe terraform.tfvars|Crear el archivo local mostrado y pasar el token mediante TF_VAR_…|
|Terraform no conecta con Docker en Linux|El proveedor usa el named pipe de Windows|Cambiar host a unix:///var/run/docker.sock|
|Redis aparece unhealthy con Terraform|El health check ejecuta PING sin autenticación|Añadir usuario y secreto al health check mediante un mecanismo seguro|
|No aparece el modo de log configurado|log_config y la etiqueta mapstructure:"infra_config" no coinciden|Corregir la etiqueta o usar el nombre admitido por la revisión compilada|

_Nota._ Elaboración propia a partir de los comportamientos observados en el proyecto. La tabla reúne síntomas, causas probables y acciones de diagnóstico para la configuración, Redis, autenticación, Docker y Terraform.

## Para parar y limpiar

El broker ejecutado con go run se detiene con Ctrl+C. Después se eliminan las variables de la sesión.

Windows:

```text
Remove-Item Env:APP_CONFIG -ErrorAction SilentlyContinue  
Remove-Item Env:DOMINUS_GRPC_TOKEN -ErrorAction SilentlyContinue  
Remove-Item Env:DOMINUS_REST_TOKEN -ErrorAction SilentlyContinue
```

Linux:

```text
unset APP_CONFIG DOMINUS_GRPC_TOKEN DOMINUS_REST_TOKEN
```

Los contenedores locales se detienen y retiran por nombre:

```text
docker stop dominus-broker redis  
docker rm dominus-broker redis
```

Si sólo se ejecutó Redis, se aplica el commando únicamente a redis. Las imágenes y volúmenes no se eliminan automáticamente porque pueden reutilizarse. Terraform mantiene su propio estado y sus recursos se retiran con terraform destroy desde terraform/.

# Anexo C. Manual básico de usuario

Este apartado resume el uso del SDK de Dominus a partir del proyecto `consumer-example`. El ejemplo está construido en Go y emplea `github.com/MBI-88/dominus-sdk/dominus` para comunicarse con el broker mediante gRPC. Su finalidad es mostrar dos capacidades relacionadas:

- Operaciones de mensajería tipo SQS: producción, consumo y confirmación.
- Exposición de un servicio compatible con el Broker API para trabajar con streams gRPC.

El documento describe el contrato observable en `dominus-sdk v1.3.5` y `dominus-proto-definition v1.3.7`. Las pausas de 15 segundos, la API key incluida en el ejemplo y los mensajes de demostración no deben interpretarse como valores recomendados para producción.

### Objeto y alcance

El alcance se limita al contrato y patrones de uso observables en las versiones indicadas, sin asumir que los valores del ejemplo sean adecuados para producción.

### Requisitos

- Go `1.26.1` o compatible con el módulo del proyecto.
- Acceso al endpoint Dominus, expresado como `host:puerto` o dominio válido.
- API key autorizada por el broker.
- Dependencias declaradas en `go.mod`:
    - `github.com/MBI-88/dominus-sdk v1.3.5`;
    - `github.com/MBI-88/dominus-proto-definition v1.3.7`;
    - `github.com/google/uuid v1.6.0`.

El ejemplo usa `127.0.0.1:5000` como endpoint remoto y recibe por línea de comandos el puerto local donde publica su servidor gRPC.

### Modelo conceptual

El SDK separa configuración, cliente y operación. La Tabla 17 aporta una vista compacta de los componentes, sus responsabilidades y el constructor asociado.

**Tabla 17**

*Componentes principales del SDK Dominus* 

|**Componente**|**Responsabilidad**|**Constructor**|
|---|---|---|
|SqsConfig|Preparar un cliente de mensajería|NewSqsConfig(dns)|
|Sqs|Producir, consumir y confirmar mensajes|InitAPIClients(...)|
|BrokerConfig|Preparar un cliente de streaming|NewBrokerConfig(subs, dns)|
|ServerOption|Crear opciones de servidor y autenticación|NewServerOption()|
|BrokerRegister|Registrar un handler en el Broker API|NewBrokerRegister(opts)|

_Nota._ Elaboración propia a partir de la API del SDK. La tabla relaciona los objetos de configuración y operación con su responsabilidad y método de construcción.

El SDK añade la API key en metadatos gRPC. En las operaciones SQS también utiliza un valor de idempotencia, que el ejemplo genera con `uuid.New().String()`.

### Inicialización del cliente SQS

La inicialización mínima del ejemplo es:

**idempotency := uuid.New().String()**

**sqs := dominus.NewSqsConfig("127.0.0.1:5000").**

**InitAPIClients(apiKey, idempotency)**

`InitAPIClients` utiliza transporte inseguro. Es apropiado únicamente durante desarrollo o cuando la comunicación está protegida por una red confiable. Para TLS, el SDK ofrece:

**sqs := dominus.NewSqsConfig(dominusURL).**

InitAPIClientsTLSFromFile(caCertPath, serverName, apiKey, idempotency)

El certificado indicado debe ser legible y válido, y `serverName` se utiliza para verificar la identidad del servidor. La API key y el valor de idempotencia no deben estar codificados en el repositorio; deben proceder de variables de entorno o de un gestor de secretos.

### Producción de mensajes

La interfaz `Sqs` expone:

UseProducer(*dominus.ProducerRequest) (*dominus.ProducerResponse, error)

El `ProducerRequest` debe construirse conforme al contrato generado en `dominus-proto-definition`. La operación devuelve una respuesta protobuf o un error gRPC. Un productor debe registrar el identificador de la operación, tratar los errores transitorios con una política de reintento limitada y evitar duplicados mediante una idempotencia estable cuando el contrato del broker lo requiera.

Este repositorio no contiene una implementación de productor; por tanto, los nombres exactos de los campos de `ProducerRequest` deben consultarse en la versión de `dominus-proto-definition` fijada en `go.mod`.

### Consumo y confirmación

#### Solicitar un mensaje

El ejemplo crea un identificador único de worker y un grupo lógico:

**workerID := fmt.Sprintf("worker-%s", idempotency)**

**groupID := "consumer-group"**

**response, err := sqs.UseConsumer(&dominus.ConsumerRequest{**

**WorkerId: workerID,**

**GroupId: groupID,**

**})**

`UseConsumer` recibe un `ConsumerRequest` con:

- `WorkerId`: identifica la instancia que solicita el trabajo;
- `GroupId`: identifica el grupo de consumidores;
- `MessageId`: se utiliza al confirmar el mensaje, no en la solicitud inicial del ejemplo.

La respuesta expone, entre otros, `GetMessageId()`, `GetDate()` y `GetMessage()`. El consumidor debe validar que la respuesta sea utilizable antes de iniciar el procesamiento.

#### Procesar y confirmar

La confirmación se realiza con `UseAck`:

**_, err = sqs.UseAck(&dominus.ConsumerRequest{**

**MessageId: response.GetMessageId(),**

**WorkerId: workerID,**

**GroupId: groupID,**

**})**

El ACK debe ejecutarse después de completar satisfactoriamente el procesamiento del mensaje. Si el procesamiento falla, no debe enviarse una confirmación positiva sin una decisión explícita sobre reintento, descarte o envío a una cola de errores. La política exacta de redelivery debe verificarse en la documentación del servicio Dominus.

#### Flujo recomendado

**Inicializar cliente**

**|**

**Solicitar mensaje (WorkerId, GroupId)**

**|**

**¿Respuesta válida? -- no --> registrar error y aplicar reintento**

**|**

**Procesar mensaje**

**|**

**¿Procesamiento correcto? -- no --> registrar fallo y no confirmar automáticamente**

**|**

**Confirmar (MessageId, WorkerId, GroupId)**

**|**

**Registrar resultado del ACK y continuar**

El ejemplo consulta cada 15 segundos y espera otros 15 segundos antes del ACK. Es una secuencia ilustrativa, no un mecanismo de control de carga ni una garantía de exclusión. En una aplicación real conviene usar un ticker configurable, `context.Context`, límites de tiempo y métricas de latencia.

### Exposición de un servidor Broker

El proyecto también demuestra cómo registrar un servidor compatible con el Broker API:

**options := dominus.NewServerOption().InitServerOption(apiKey)**

**register := dominus.NewBrokerRegister(options)**

**server := register.RegisterHandler(&brokerSvc{})**

**listener, err := net.Listen("tcp", address)**

**if err != nil {**

**return err**

**}**

**return server.Serve(listener)**

El handler debe incrustar `UnimplementedBrokerAPIServer` y cumplir las interfaces generadas por protobuf. Para transporte seguro, las opciones se crean con:

**options := dominus.NewServerOption().**

**InitServerOptionsTLSFromFile(certFile, keyFile, apiKey)**

El servidor valida la API key mediante metadatos gRPC. La clave utilizada para el servidor debe coordinarse con la que presentan los clientes autorizados.

### Modalidades de streaming

#### Server stream

ServerStream

`ServerStream` recibe una petición inicial y envía múltiples `StreamResponseMessage` mediante `stream.Send`. Es adecuado cuando el cliente inicia una operación y el servidor devuelve una secuencia de resultados.

#### Client stream

ClientStream

`ClientStream` recibe múltiples mensajes con `stream.Recv` hasta recibir `io.EOF`. Es adecuado para cargas de datos o eventos enviados en lote por el cliente.

#### Bidirectional stream

BidirectionalStream

`BidirectionalStream` recibe y envía de forma independiente. El ejemplo responde con `ACK` a cada mensaje recibido. En todos los casos, los errores de `Recv` y `Send` deben propagarse, y `io.EOF` debe tratarse como cierre normal del stream.

Desde un cliente `Broker`, el SDK expone helpers equivalentes:

`UseStreamClientConn()`: devuelve función de envío y función de cierre;

`UseStreamServerConn()`: devuelve una función para recibir el siguiente payload;

`UseBiStreamConn()`: devuelve funciones de envío, recepción y cierre de envío.

El cliente de streaming se construye con suscriptores y endpoint:

**broker := dominus.NewBrokerConfig(**

**[]string{"subscriber-a:5000"},**

**dominusURL,**

**).InitAPIClients(apiKey)**

Para TLS se utiliza `InitAPIClientsTLSFromFile` con los parámetros del certificado, nombre del servidor y API key.

### Arranque y apagado del ejemplo

El programa espera un puerto local como primer argumento:

go run . 6000

En paralelo, inicia el servidor local y el consumidor SQS. Registra `os.Interrupt` y `SIGTERM`; al recibir una señal llama a `GracefulStop`, permitiendo finalizar las RPC en curso. Esta práctica debe conservarse en despliegues reales, complementándola con un contexto de cancelación para detener el bucle de consumo y liberar el ticker.

### Seguridad y operación

1. Sustituir la API key constante del ejemplo por configuración externa y rotarla periódicamente.
2. Preferir TLS en redes no confiables y validar el nombre del servidor.
3. No registrar el contenido completo de mensajes si puede contener información sensible.
4. Añadir límites de tiempo, reintentos con backoff y clasificación de errores gRPC.
5. Evitar `log.Fatal` en goroutines de servicio; devolver errores al supervisor para permitir apagado coordinado.
6. Detener explícitamente los tickers y cerrar recursos del cliente cuando finalice el proceso.
7. Medir mensajes solicitados, procesados, confirmados, fallidos y latencia entre consumo y ACK.
8. Probar la semántica de duplicados y redelivery del broker antes de asumir procesamiento exactamente una vez.

### Conclusión

El SDK Dominus proporciona una capa Go de acceso a servicios gRPC autenticados mediante API key. El patrón principal del ejemplo consiste en inicializar `Sqs`, identificar el worker y el grupo, solicitar un mensaje, procesarlo y confirmar su `MessageId`. La misma dependencia permite registrar servicios Broker y operar con los tres patrones de streaming gRPC. Para convertir el ejemplo en una integración productiva se requiere externalizar la configuración, habilitar TLS, controlar la cancelación y definir explícitamente las políticas de reintento, duplicación y observabilidad

# Anexo D. Guía básica de mantenimiento

Esta guía describe las actividades básicas de mantenimiento necesarias para conservar la operación del broker de mensajería desarrollado. El mantenimiento se enfoca en los componentes que permiten la publicación, consumo, confirmación y transmisión de mensajes en tiempo real, considerando el servicio gRPC, los casos de uso principales, Redis Streams, los archivos de configuración, las pruebas automatizadas y los mecanismos de observabilidad.

La puesta en marcha inicial del sistema se aborda en el anexo correspondiente, mientras que las funciones principales para el usuario se describen en el manual básico de usuario. A diferencia de esos apartados, esta guía se concentra en las actividades posteriores a la implementación: soporte, actualización de dependencias, compatibilidad de contratos, revisión de configuración y validación posterior a cambios.

El alcance corresponde a un prototipo funcional desarrollado como parte del TFM. Por ello, no se plantea como un manual operativo empresarial completo, sino como una referencia básica para realizar ajustes controlados y reducir el riesgo de afectar los flujos principales del sistema.

## Soporte y atención de incidencias

El soporte del broker debe enfocarse en incidencias relacionadas con la publicación, consumo, confirmación y transmisión de mensajes. Cuando se reporte un problema, primero se debe identificar si el fallo corresponde al cliente que consume el servicio, al contrato gRPC, a la configuración del entorno, a la conexión con Redis o a la lógica interna del broker.

Para mantener trazabilidad, cada incidencia debe registrar al menos la siguiente información:

- Descripción breve del problema detectado.
- Fecha de detección o reporte.
- Componente afectado, por ejemplo gRPC, Redis, configuración o caso de uso.
- Evidencia disponible, como logs, capturas, salida de consola o pasos de reproducción.
- Versión o rama del proyecto donde se detectó el problema.
- Estado de atención: pendiente, en análisis, corregido o validado.
- Resultado de la validación posterior a la corrección.

El soporte también debe considerar dudas de uso o configuración. Si la duda corresponde a instalación, variables de entorno o ejecución inicial, debe revisarse el anexo de puesta en marcha. Si corresponde al uso funcional del sistema, debe revisarse el manual básico de usuario.

Cuando una incidencia afecte los flujos principales del broker, se debe validar si existe una prueba automatizada que cubra ese comportamiento. Si no existe, se recomienda agregar una prueba antes o junto con la corrección, para que el mantenimiento también fortalezca la validación futura del proyecto.

## Componentes sujetos a mantenimiento

El mantenimiento debe concentrarse en los componentes que tienen impacto directo en la operación del broker. Para esta guía se consideran los siguientes elementos principales:

- **Servicio gRPC:** revisar que los métodos expuestos, contratos .proto y flujos de comunicación se mantengan compatibles con los clientes del broker.
- **Contratos** .proto**:** validar que los mensajes, servicios y campos definidos sigan representando correctamente la comunicación entre cliente y broker.
- **Casos de uso** Producer, Consumer **y** Ack**:** comprobar que la publicación, consumo y confirmación de mensajes continúen funcionando después de cualquier ajuste.
- **Flujos de streaming:** revisar los escenarios de envío desde cliente, envío desde servidor e intercambio bidireccional.
- **Redis Streams:** comprobar conexión, lectura de mensajes, grupos de consumidores y confirmación mediante XACK.
- **Configuración del entorno:** mantener actualizadas variables de entorno, puertos, credenciales, certificados y rutas de conexión.
- **Dependencias de Go:** revisar cambios en módulos del proyecto y librerías asociadas a gRPC, Redis, pruebas y observabilidad.
- **Pruebas automatizadas:** actualizar escenarios unitarios o de integración cuando cambie el comportamiento esperado del broker.
- **Observabilidad:** revisar logs, métricas y errores recurrentes para identificar posibles fallos de operación.

El servicio gRPC requiere especial atención porque define la comunicación entre clientes y broker. Cualquier cambio en métodos, mensajes o campos debe revisarse antes de integrarse, ya que puede afectar la compatibilidad con clientes existentes.

Los casos de uso Producer, Consumer y Ack deben revisarse cuando se modifique la lógica de publicación, consumo o confirmación de mensajes. Redis Streams también requiere validación cuando se ajusten conexiones, grupos de consumidores, lectura de mensajes o confirmaciones mediante XACK.

## Actualización controlada de software y dependencias

Las actualizaciones deben realizarse de forma controlada, evitando modificar varios componentes críticos al mismo tiempo. En el caso de Go, las dependencias del proyecto se gestionan mediante los archivos go.mod y go.sum. Antes de aceptar una actualización, se debe revisar la versión actual, aplicar el cambio en un entorno controlado y ejecutar las pruebas correspondientes.

Entre los elementos que deben mantenerse actualizados se encuentran:

- La versión de Go utilizada por el proyecto.
- Los módulos registrados en go.mod y go.sum.
- Las librerías asociadas a gRPC.
- Las dependencias utilizadas para conexión y operación con Redis.
- Las herramientas empleadas para pruebas automatizadas.
- Los scripts de automatización y comandos de validación.
- La configuración asociada a contenedores o entorno de ejecución, cuando aplique.

Para revisar dependencias disponibles se puede utilizar el siguiente comando:

go list -m -u all

Cuando se actualice una dependencia específica, se debe registrar el módulo modificado y la versión aplicada. Después de realizar el cambio, se recomienda ejecutar:

go mod tidy

Este comando permite limpiar dependencias no utilizadas y actualizar los archivos de control del proyecto. Posteriormente, se deben ejecutar las pruebas unitarias y de integración para confirmar que la actualización no afectó los casos de uso principales.

El procedimiento básico de actualización debe considerar estos pasos:

- Revisar la versión actual del componente o dependencia.
- Identificar el motivo de la actualización: corrección de error, mejora de seguridad, compatibilidad o nueva funcionalidad.
- Aplicar el cambio en un entorno controlado.
- Ejecutar go mod tidy cuando se modifiquen dependencias de Go.
- Ejecutar pruebas unitarias y de integración después del cambio.
- Revisar que la cobertura no disminuya de forma significativa sin justificación técnica.
- Registrar la versión actualizada, el motivo del cambio y cualquier consideración de compatibilidad.

En el caso de Redis, se debe conservar la compatibilidad con Redis Streams, grupos de consumidores y operaciones de confirmación mediante XACK. En el caso de gRPC, los cambios deben revisarse con mayor cuidado porque los contratos definen la comunicación entre clientes y broker.

## Compatibilidad de contratos y configuración

Uno de los puntos más importantes del mantenimiento es conservar la compatibilidad de los contratos .proto. Estos contratos definen los servicios, mensajes y campos utilizados en la comunicación gRPC. Por ello, no se deben eliminar o modificar campos existentes sin revisar el impacto sobre los clientes que consumen el broker.

Cuando sea necesario cambiar un contrato, el cambio debe documentarse y validarse mediante pruebas. Si se agregan nuevos campos, se debe procurar que la modificación no rompa la compatibilidad con versiones anteriores. Si el cambio afecta directamente la estructura de los mensajes o los métodos disponibles, también deben actualizarse los clientes, las pruebas y la documentación técnica correspondiente.

Para reducir riesgos en cambios de contrato, se recomienda revisar los siguientes puntos:

- No eliminar campos existentes sin analizar el impacto en clientes actuales.
- No reutilizar campos o identificadores eliminados sin una justificación técnica.
- Documentar cualquier nuevo campo, servicio o método agregado.
- Validar que los clientes puedan seguir comunicándose con el broker.
- Actualizar pruebas cuando cambie la estructura de los mensajes.
- Revisar que la documentación técnica refleje el contrato vigente.

La configuración del entorno también debe mantenerse documentada. Esto incluye puertos, variables de entorno, credenciales, certificados, rutas de conexión y parámetros asociados a Redis. Cualquier cambio en estos valores debe validarse en un entorno controlado antes de considerarlo estable.

## Validación posterior a cambios de mantenimiento

Después de aplicar un cambio de mantenimiento, se debe validar que el broker conserve su comportamiento esperado. Como mínimo, se recomienda ejecutar pruebas unitarias, pruebas de integración y medición de cobertura.

Los comandos base de validación son los siguientes:

go test -count=1 ./tests/units/...

go test -count=1 ./tests/integration/...

.\Makefile.ps1 -Target test-cover

Las pruebas unitarias permiten revisar la lógica aislada de los casos de uso. Las pruebas de integración permiten confirmar la interacción entre componentes. La cobertura permite identificar si los cambios mantienen un nivel adecuado de validación sobre el código modificado.

Después de aplicar un cambio, se recomienda comprobar lo siguiente:

- Las pruebas unitarias finalizan sin errores.
- Las pruebas de integración no reportan fallos.
- Los flujos de publicación, consumo y confirmación funcionan correctamente.
- Los flujos de streaming responden a los escenarios definidos.
- La conexión con Redis se mantiene estable.
- Los contratos .proto siguen siendo compatibles con los clientes.
- La configuración modificada está documentada.
- La cobertura se mantiene en un nivel aceptable para el alcance del proyecto.

Como criterio mínimo, el mantenimiento puede considerarse satisfactorio cuando las pruebas no reportan fallos, los flujos principales funcionan correctamente y la cobertura no disminuye de forma significativa sin una justificación técnica.

## Revisión de logs, métricas y errores recurrentes

El mantenimiento también debe considerar la revisión periódica de logs y métricas. Esta revisión permite identificar errores recurrentes, problemas de conexión, fallos en la confirmación de mensajes o comportamientos inesperados en los flujos de comunicación.

Durante la revisión se recomienda observar principalmente:

- Errores de conexión con Redis.
- Fallos de comunicación entre clientes y servicio gRPC.
- Mensajes no confirmados o errores asociados a la confirmación de mensajes.
- Errores repetidos en publicación o consumo de mensajes.
- Problemas de configuración en variables de entorno, puertos o credenciales.
- Comportamientos inesperados en los flujos de streaming.
- Cambios relevantes en métricas de uso, latencia o errores.

En caso de detectar errores repetidos, se debe registrar el escenario, revisar el componente afectado y reproducir el comportamiento en un entorno controlado. Si el error corresponde a un caso no cubierto por pruebas, se recomienda agregar una prueba nueva antes de aplicar la corrección.

## Registro, comunicación y trazabilidad de cambios

Toda actividad de mantenimiento que modifique código, configuración, dependencias o contratos debe quedar registrada. Esto permite conservar trazabilidad y facilita identificar qué cambio pudo generar un comportamiento inesperado.

El registro de cambios debe incluir, como mínimo:

- Fecha del cambio.
- Responsable de la modificación.
- Componente afectado.
- Descripción breve del ajuste.
- Motivo del cambio.
- Versión o dependencia actualizada, cuando aplique.
- Pruebas ejecutadas después del cambio.
- Resultado de la validación.

El soporte del prototipo puede gestionarse mediante el repositorio del proyecto, un tablero de incidencias o el canal definido por el equipo. En caso de llevar el broker a un entorno operativo, se recomienda definir un responsable técnico y comunicar cada actualización indicando el componente afectado, el motivo del cambio, los ajustes requeridos y las pruebas ejecutadas. Con esto se conservará la trazabilidad y se reducirá el riesgo de afectar los flujos principales durante su operación continua.

# Checklist notas de ayuda (BORRAR)

> [!danger] Retirar antes de entregar
> Esta lista, las marcas `(TBD)` y las instrucciones de plantilla no deben aparecer en la versión final. También deben regenerarse los índices después de cerrar la jerarquía de encabezados y la numeración de tablas y figuras.

- Confirmar los siguientes puntos antes de enviar y borrar esta página:
- ~~Ejemplo~~
- ~~Agregar y mezclar plantilla final para homogeneizar TFM - Daniel~~
- Sección 4 completar: Desarrollo específico de la contribución (Práctico)
- Encabezados y pie de página uniformes
- Títulos y subtítulos a máximo tres niveles 1.1.1
- Tablas y figuras: número en negrita y título en cursiva en la parte superior; nota y fuente debajo de la tabla o figura (por ejemplo, `Tabla 1` o `Figura 1`).
- Verifica la originalidad del documento asegurándose de que se citan todas las fuentes consultadas y que no existen textos de autoría ajena sin referenciar correctamente.
- Cuida la presentación del trabajo. Comprueba que los formatos como tipo y tamaño de letra, número de páginas, encabezados, justificación de párrafos, interlineado, etc., son los correctos.
- Revisa la ortografía y la redacción.
- Repasa las citas bibliográficas. Revisa que solo se usen letras consecutivas (`a`, `b`, `c`...) cuando las referencias tengan el mismo autor y el mismo año o una fecha no disponible.
- Asegúrate de que las figuras y las tablas se ven claramente.
- Comprueba que los índices se generan correctamente.

1. Ejemplo de nota al pie. [↑](#footnote-ref-0)
