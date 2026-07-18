![TFM_v1](Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1.png)

Universidad Internacional de La Rioja

Escuela Superior de Ingeniería y Tecnología

Máster Universitario en Ingeniería de Software y Sistemas

Diseño e implementación de un Broker de mensajería híbrido para arquitecturas orientadas a eventos en tiempo real.

|                                        |                          |
| -------------------------------------- | ------------------------ |
| Trabajo fin de estudio presentado por: | Maikel Barrios Insua     |
| Tipo de trabajo:                       | Trabajo de fin de Máster |
| Director/a:                            |                          |
| Fecha:                                 |                          |

Resumen

Este proyecto propone el diseño e implementación de un **Broker de mensajería en tiempo real** que integra capacidades síncronas y asíncronas sobre el protocolo gRPC, orientado a sistemas distribuidos modernos. La solución explota los tres modelos de comunicación nativos de gRPC: llamadas unarias (request-response), streaming servidor-cliente y streaming bidireccional, permitiendo flujos de datos eficientes, persistentes y de baja latencia entre productores y consumidores.

El componente central del sistema es el Broker, encargado de orquestar la comunicación, enrutar mensajes y gestionar patrones avanzados como **fan-in** (agregación de múltiples fuentes hacia un consumidor) y **fan-out** (distribución de mensajes hacia múltiples suscriptores). Estos patrones habilitan escenarios típicos de procesamiento en tiempo real, como agregación de eventos, broadcasting y pipelines de procesamiento concurrente.

Como valor diferencial, el sistema incorpora un modelo híbrido que combina comunicación síncrona con capacidades asíncronas. Para ello, se integra Redis como capa de almacenamiento en memoria, utilizada exclusivamente para persistencia temporal de mensajes dentro de una **cola transaccional**. Esta cola opera bajo un enfoque _pull-based_, donde los consumidores solicitan activamente los mensajes mediante gRPC, garantizando control sobre el consumo, backpressure y desacoplamiento entre productores y consumidores.

A diferencia de Brokers tradicionales, la lógica de enrutamiento, persistencia y control de flujo reside principalmente en el Broker, mientras que Redis actúa como soporte de almacenamiento volátil, optimizando latencia sin introducir complejidad adicional de infraestructura. Este enfoque permite mantener consistencia operativa y simplicidad arquitectónica.

En conjunto, el sistema demuestra cómo la convergencia de gRPC, patrones de mensajería avanzados y almacenamiento en memoria permite construir plataformas de mensajería altamente eficientes, escalables y adaptadas a escenarios de procesamiento en tiempo real.

**Palabras clave**: gRPC, Redis, Comunicación asíncrona, Sistemas distribuidos, Fan-in/Fan-out

Abstract

This project presents the design and implementation of a **real-time messaging Broker** that integrates both synchronous and asynchronous communication using the gRPC protocol. The system leverages the three core interaction models supported by gRPC: unary calls (request-response), server streaming, and bidirectional streaming, enabling efficient, low-latency, and persistent communication between distributed components.

At its core, the Broker is responsible for message orchestration, routing, and coordination, supporting advanced messaging patterns such as **fan-in** (aggregation of multiple producers into a single consumer) and **fan-out** (distribution of messages to multiple consumers). These patterns enable scalable real-time processing scenarios, including event aggregation, broadcasting, and concurrent data pipelines.

As a key contribution, the system introduces a hybrid communication model that extends beyond traditional synchronous RPC by incorporating asynchronous capabilities. This is achieved through the integration of Redis as an in-memory persistence layer, used to implement a **transactional message queue**. The queue follows a _pull-based_ consumption model, where clients explicitly request messages via gRPC, allowing fine-grained control over consumption rates, backpressure handling, and decoupling between producers and consumers.

Unlike conventional messaging systems, the Broker centralizes routing logic, flow control, and message lifecycle management, while Redis is utilized solely as a high-performance transient storage mechanism. This design minimizes infrastructure complexity while maintaining strong performance characteristics.

Overall, the proposed system demonstrates how combining gRPC, advanced messaging patterns, and in-memory data storage can enable the development of scalable, efficient, and flexible real-time messaging platforms suitable for modern distributed architectures.

**Keywords**: gRPC, Redis, Async Communication, Distributed Systems, Fan-in/Fan-out

Índice de contenidos

[Índice de figuras 7](#_Toc227818948)

[1. Introducción 9](#_Toc227818949)

[1.1. Justificación del Trabajo 11](#_Toc227818950)

[1.2. Planteamiento de la Solución 12](#_Toc227818951)

[1.3. Estructura de la Memoria 13](#_Toc227818952)

[2. Contexto y Estado del Arte 14](#_Toc227818953)

[2.1. Antecedentes 16](#_Toc227818954)

[2.1.1. gRPC 16](#_Toc227818955)

[2.1.2. Brokers de mensajería relevantes 16](#_Toc227818956)

[2.1.3. Patrones de mensajería 18](#_Toc227818957)

[2.1.4. Cola transaccional con pull sobre gRPC 18](#_Toc227818958)

[2.1.5. Redis como memoria intermedia de mensajes 19](#_Toc227818959)

[2.1.6. Arquitectura Hexagonal (puertos y adaptadores) 19](#_Toc227818960)

[2.2. Trabajos Relacionados 20](#_Toc227818961)

[2.3. Conclusiones del Estado del Arte 21](#_Toc227818962)

[3. Objetivos y Metodología de Trabajo 26](#_Toc227818963)

[3.1. Objetivo Principal 26](#_Toc227818964)

[3.2. Objetivos Específicos 26](#_Toc227818965)

[3.3. Metodología de Trabajo 27](#_Toc227818966)

[3.3.1. Análisis Del Problema 27](#_Toc227818967)

[3.3.2. Diseño de la solución 28](#_Toc227818968)

[3.3.3. Implementación 28](#_Toc227818969)

[3.3.4. Experimentación 28](#_Toc227818970)

[3.3.5. Evaluación de Resultados 29](#_Toc227818971)

[3.3.6. Análisis Comparativo 29](#_Toc227818972)

[4. Desarrollo del Proyecto 30](#_Toc227818973)

[4.1. Análisis 30](#_Toc227818974)

[4.1.2 Requisitos funcionales 30](#_Toc227818975)

[4.1.3 Requisitos no funcionales 30](#_Toc227818976)

[4.1.4 Arquitectura del Sistema 31](#_Toc227818977)

[4.1.5 Vision general 31](#_Toc227818978)

[4.1.6 Modelo de Comunicación 32](#_Toc227818979)

[4.1.7 Diseño del Broker 32](#_Toc227818980)

[4.1.8 Modelo de Datos comunicación Síncrona 33](#_Toc227818981)

[4.1.9 Modelo de Datos comunicación Asíncrona 33](#_Toc227818982)

[4.1.10 Estrategia de Concurrencia 33](#_Toc227818983)

[4.1.11 Estrategia de Escalabilidad 34](#_Toc227818984)

[4.1.12 Estrategia de Resiliencia 34](#_Toc227818985)

[4.1.13 Consideraciones de Rendimiento 35](#_Toc227818986)

[4.2. Implementación 35](#_Toc227818987)

[4.2.1 Elección de la arquitectura del Broker 35](#_Toc227818988)

[4.2.2 Implementación del contrato de mensajería mediante Protocol Buffers 39](#_Toc227818989)

[4.2.3 Implementación del flujo de comunicación en el Broker 41](#_Toc227818990)

[4.2.4 Gestión de la comunicación concurrente, comunicación síncrona. 51](#_Toc227818991)

[4.2.5 Evitando la duplicación de mensajes, comunicación asíncrona. 58](#_Toc227818992)

[4.2.6 Uso de memoria persistente, comunicación asíncrona. 61](#_Toc227818993)

[4.2.7 Sistema de logs y telemetría 64](#_Toc227818994)

[4.3. Evaluación 64](#_Toc227818995)

[4.3.1. “Título 3” del menú de estilos 65](#_Toc227818996)

[4.3.2. “Título 3” del menú de estilos 65](#_Toc227818997)

[5. Conclusiones y Trabajo Futuro 66](#_Toc227818998)

[5.1. Conclusiones 66](#_Toc227818999)

[5.2. Líneas de Trabajo Futuro 66](#_Toc227819000)

[Referencias bibliográficas 67](#_Toc227819001)

[Anexo A. Título Anexo 70](#_Toc227819002)

Índice de figuras

[_Figura 1. Esquema general_ 31](#_Toc227819003)

[_Figura 2. Arquitectura del Broker_ 38](#_Toc227819004)

[_Figura 3. Estructura de directorios_ 38](#_Toc227819005)

[_Figura 4. Diagrama de componentes_ 53](#_Toc227819006)

[_Figura 5. Diagrama de comunicación_ 54](#_Toc227819007)

[_Figura 6. Diagrama de componentes_ 63](#_Toc227819008)

[_Figura 7. Diagrama de comunicación_ 63](#_Toc227819009)

[Figura 8. “Figuras” del menú de estilos. (Elaboración propia) 65](#_Toc227819010)

Índice de tablas

[Tabla 1. Comparaciones entre las soluciones presentadas y la propuesta. 24](#_Toc227819011)

[Tabla 3. “Tablas” del menú de estilos 64](#_Toc227819012)

# Introducción

En los últimos años, la evolución de las arquitecturas distribuidas ha estado fuertemente influenciada por la necesidad de construir sistemas altamente escalables, resilientes y capaces de procesar grandes volúmenes de información en tiempo real. En este contexto, las arquitecturas orientadas a eventos (Event-Driven Architectures, EDA) se han consolidado como un paradigma dominante, permitiendo desacoplar componentes, mejorar la tolerancia a fallos y facilitar la escalabilidad horizontal mediante el uso de Brokers de mensajería como elemento central de comunicación.

Los Brokers de mensajería tradicionales, tales como los basados en modelos publish/subscribe o colas persistentes, han demostrado ser efectivos para la comunicación asíncrona entre servicios. Sin embargo, estos sistemas han sido diseñados históricamente bajo paradigmas donde la prioridad era la durabilidad y la entrega eventual de mensajes, más que la comunicación en tiempo real con baja latencia. Esto genera una brecha en escenarios donde se requiere simultáneamente alta capacidad de procesamiento, baja latencia y flujos continuos de datos.

Por otro lado, los sistemas modernos, especialmente en dominios como fintech, sistemas de trading, procesamiento de eventos en streaming o plataformas de integración distribuida, demandan cada vez más capacidades de comunicación en tiempo real. En este contexto, los enfoques tradicionales basados en HTTP/REST presentan limitaciones estructurales, dado que operan bajo un modelo request-response que no está optimizado para flujos continuos de información ni para mantener conexiones persistentes eficientes. Para simular comportamientos en tiempo real, estos sistemas suelen recurrir a mecanismos adicionales como polling o WebSockets, introduciendo complejidad y sobrecarga en la arquitectura.

Frente a estas limitaciones, gRPC emerge como una alternativa moderna para la comunicación entre servicios, especialmente en entornos de microservicios. Este framework, basado en HTTP/2 y en la serialización binaria mediante Protocol Buffers, permite reducir significativamente la latencia y mejorar el throughput en comparación con enfoques tradicionales basados en JSON sobre HTTP/1.1. Diversos estudios y benchmarks indican que gRPC puede alcanzar mejoras de rendimiento de entre 7 y 10 veces en transmisión de datos frente a REST, debido a su eficiencia en serialización y al uso de conexiones persistentes multiplexadas.

Además, una de las características diferenciales más relevantes de gRPC es su soporte nativo para múltiples modelos de comunicación, incluyendo streaming bidireccional, lo que permite el intercambio continuo de mensajes entre cliente y servidor sin necesidad de establecer nuevas conexiones por cada interacción. Esta capacidad lo posiciona como una tecnología especialmente adecuada para escenarios de comunicación en tiempo real y flujos de datos continuos, donde la latencia y la eficiencia en el uso de recursos son factores críticos.

No obstante, a pesar de sus ventajas, gRPC ha sido tradicionalmente utilizado como un mecanismo de comunicación síncrona entre servicios, mientras que los Brokers de mensajería han dominado el ámbito de la comunicación asíncrona. Esta separación conceptual entre comunicación síncrona de alto rendimiento y mensajería desacoplada introduce complejidad en el diseño de sistemas, obligando a combinar múltiples tecnologías para cubrir ambos casos de uso.

Adicionalmente, uno de los desafíos más relevantes en sistemas distribuidos basados en eventos es la gestión de la idempotencia y la garantía de procesamiento único de mensajes. En entornos donde pueden producirse reintentos, duplicaciones o fallos parciales, asegurar que un mensaje sea procesado exactamente una vez se convierte en un requisito fundamental para mantener la consistencia del sistema. Sin embargo, esta lógica suele implementarse a nivel de aplicación, generando duplicidad de esfuerzos y aumentando la complejidad del sistema.

En este contexto, soluciones como Redis han demostrado ser altamente eficaces como mecanismos de almacenamiento en memoria para gestionar estados temporales, deduplicación de mensajes y control de idempotencia, gracias a su baja latencia y alto rendimiento. Su uso como capa complementaria en sistemas de mensajería permite introducir garantías adicionales sin penalizar significativamente el rendimiento global.

## Justificación del Trabajo

En este contexto, surge la necesidad de explorar enfoques que permitan integrar, de forma coherente, los distintos modelos de comunicación requeridos por los sistemas distribuidos modernos. En particular, resulta relevante abordar la brecha existente entre la comunicación en tiempo real de baja latencia y los mecanismos de mensajería asíncrona con garantías de consistencia.

Las soluciones actuales suelen especializarse en uno de estos aspectos. Por un lado, los protocolos modernos como gRPC ofrecen capacidades avanzadas de comunicación, incluyendo streaming bidireccional y conexiones persistentes eficientes, lo que los convierte en una opción idónea para escenarios en tiempo real. Sin embargo, carecen de mecanismos nativos para el desacoplamiento entre productores y consumidores, así como de soporte para persistencia o gestión de mensajes.

Por otro lado, los Brokers de mensajería tradicionales proporcionan modelos robustos de comunicación asíncrona, basados en colas o sistemas publish/subscribe, con capacidades de persistencia y tolerancia a fallos. No obstante, estos sistemas no están optimizados para escenarios de comunicación en tiempo real, donde la latencia y la inmediatez en la entrega de eventos son factores críticos.

Adicionalmente, la gestión de la idempotencia —es decir, la garantía de que un mensaje sea procesado una única vez— constituye un desafío recurrente en sistemas distribuidos. Esta lógica suele implementarse en capas superiores de la aplicación, aumentando la complejidad y generando duplicidad de responsabilidades dentro de la arquitectura.

En este contexto, el presente trabajo propone un enfoque híbrido que busca reducir esta fragmentación tecnológica mediante el diseño de un Broker de mensajería que integra tres capacidades fundamentales: comunicación en tiempo real basada en gRPC, soporte para mensajería asíncrona mediante almacenamiento en memoria utilizando Redis, y un mecanismo integrado de idempotencia para garantizar la consistencia en el procesamiento de eventos.

## Planteamiento de la Solución

La propuesta introduce un modelo dual de comunicación. Por un lado, se habilita un canal de distribución en tiempo real basado en streaming, que permite la propagación inmediata de eventos hacia múltiples consumidores mediante patrones de broadcast y fan-out. Por otro lado, se incorpora un mecanismo asíncrono basado en persistencia temporal en Redis, donde los consumidores pueden recuperar mensajes mediante un esquema de consulta (polling), permitiendo desacoplar los ritmos de producción y consumo.

Este enfoque no solo permite cubrir distintos escenarios de comunicación dentro de un mismo sistema, sino que también reduce la necesidad de integrar múltiples tecnologías independientes, simplificando la arquitectura y mejorando la mantenibilidad. De esta manera, el Broker propuesto se posiciona como una solución intermedia entre los sistemas de comunicación síncrona de alto rendimiento y los Brokers de mensajería tradicionales, aportando un equilibrio entre latencia, flexibilidad y consistencia.

Además, para reducir la fricción de su uso, se propone el desarrollo de un SDK, el cual permite operar el bróker con mínimo esfuerzo, dejando así fuera problemas técnicos de implementación como es el caso de la duplicación de mensajes.

## Estructura de la Memoria

El presente documento se organiza de la siguiente manera:

- En el **Capítulo 2**, se analiza el contexto y estado del arte, abordando en profundidad las arquitecturas orientadas a eventos, los Brokers de mensajería, los protocolos de comunicación como gRPC y los mecanismos de control de idempotencia.
- En el **Capítulo 3**, se definen los objetivos del trabajo y la metodología empleada, detallando el enfoque seguido para el diseño, implementación y evaluación del sistema propuesto.
- En el **Capítulo 4**, se desarrolla la solución propuesta, incluyendo el análisis del sistema, su arquitectura, la implementación del Broker y del SDK, así como las pruebas realizadas para evaluar su rendimiento.
- Finalmente, en el **Capítulo 5**, se presentan las conclusiones del trabajo y se proponen posibles líneas de investigación futura derivadas de los resultados obtenidos.

# Contexto y Estado del Arte

En los últimos años las arquitecturas de microservicios en tiempo real han recurrido a protocolos ligeros como **gRPC** y a Brokers de mensajería rápidos (Kafka, NATS, Redis Streams, etc.) para lograr alta escalabilidad y baja latencia. gRPC, basado en HTTP/2 y Protocol Buffers, facilita comunicación binaria eficiente y multilenguaje (Microsoft Learn, 2026). En paralelo, soluciones como Apache Kafka, NATS JetStream o Redis Streams ofrecen _throughput_ del orden de millones de mensajes por segundo con latencias desde sub-milisegundos (NATS/Redis) hasta decenas de milisegundos (Kafka/RabbitMQ) (Onidel Cloud, 2025) (sanj.dev, 2025). Estos sistemas soportan distintos niveles de garantía: Kafka y Pulsar brindan _exactly-once_ mediante transacciones e idempotencia, mientras RabbitMQ y NATS suelen ofrecer al menos una vez (con opciones de deduplicación) (sanj.dev, 2025) (Onidel Cloud, 2025). En este contexto, la idea de un Broker en tiempo real con **fan-in/fan-out vía gRPC**, cola transaccional “pull” y Redis como almacén intermedio busca combinar baja latencia con consistencia. Nuestro estudio del estado del arte (2019–2024) muestra que:  
- **gRPC** aporta streaming bidireccional y serialización compacta (Protocol Buffers) (Microsoft Learn, 2026) (gRPC, 2024), ideal para comunicaciones de baja latencia en microservicios (Microsoft Learn, 2026).  
- **Brokers de mensajería** relevantes incluyen Apache Kafka, RabbitMQ, Apache Pulsar, NATS JetStream y Redis Streams. Cada uno destaca en distintos escenarios: Kafka domina throughput (≥1M msg/s) sacrificando algo de latencia (Onidel Cloud, 2025); NATS JetStream ofrece latencia sub-milisegundo con throughput muy alto (Onidel Cloud, 2025) (sanj.dev, 2025); RabbitMQ sobresale en enrutamientos complejos pero a menor escala (∼10–100k msg/s) (Onidel Cloud, 2025). Redis Streams, aunque más simple, permite un _Broker_ embebido en Redis, con rendimiento sub-ms y grupos de consumidores para paralelismo (Redis, 2026).  
- **Patrones Fan-in/Fan-out**: fan‑out difunde mensajes a múltiples destinos en paralelo, sin esperar respuesta (Wikipedia, 2022); fan‑in agrega flujos paralelos de vuelta a uno solo (Microsoft Learn, 2026). Estos patrones facilitan paralelización de tareas (procesamiento distribuido y agregación).  
- **Colas transaccionales con pull**: implementan entrega _exactly-once_ atómica, donde el consumidor extrae (“pull”) mensajes explícitamente bajo transacción, garantizando revertir en fallo (Microsoft Learn, 2026). Son comunes en JMS o en colas en la nube (ej. Service Bus). En gRPC esto equivaldría a exponer una llamada de “GetMessage” sobre un stream, con ACK manual.  
- **Redis como memoria de mensajes**: Redis Streams se emplea como cola intermedia en arquitecturas event-driven. Permite persistencia ligera y almacenamiento in-memory con latencia milimétrica (Redis, 2026). Sus grupos de consumo garantizan procesamiento _exactamente una vez_ mediante ack y reenvío automático de mensajes pendientes (Redis, 2026). Por ejemplo, el _blog_ de Redis indica que Streams funciona como Broker _asíncrono_, inmutable y de muy alto rendimiento (millones de eventos/s) (Redis, 2026).

En los últimos años ambas arquitecturas han ganado relevancia en entornos de microservicios, DDD y sistemas _cloud-native_. La **Arquitectura Hexagonal** (Ports & Adapters, Cockburn 2005) centra el _core_ de negocio en el núcleo rodeado de **puertos** (interfaces) y **adaptadores** externos, promoviendo desacoplamiento, modularidad y testeo independiente (Bonin M. , 2020). Por su parte, la **Arquitectura Limpia** (Clean Architecture, Martin 2012/2017) extiende estos principios en capas concéntricas (Entidades, Casos de Uso, Adaptadores e Infraestructura) bajo la regla de dependencias hacia el interior (Jayaraman, S. & Prasad, M., 2024). Estudios recientes destacan que ambos enfoques facilitan la escalabilidad y el desarrollo basado en dominio; por ejemplo, AWS (2022) recomienda la arquitectura hexagonal para proyectos empresariales por su enfoque en el dominio y facilidad de pruebas (Oruc, F., Goby, D., Kunce, D. & Ploski, M, 2022). No obstante, expertos advierten que en proyectos pequeños pueden caer en _sobreingeniería_: demasiadas capas o interfaces innecesarias añaden complejidad (Fowler, 2003). En este informe se analiza en profundidad la evolución, conceptos, casos de uso, ventajas/desventajas y recomendaciones prácticas de ambas arquitecturas, con comparativas, diagramas y referencias de los últimos 5 años.

En síntesis, la integración propuesta (gRPC + Broker fan-in/out + cola pull + Redis) busca combinar los puntos fuertes de cada tecnología: los patrones pub/sub y pull de Brokers clásicos, con la eficiencia de gRPC y la memoria veloz de Redis. El informe desarrolla estos componentes, arquitectura hexagonale de referencia, comparativas de soluciones, retos de consistencia y monitoreo, además de ejemplos reales y recomendaciones para investigación.

## Antecedentes

### gRPC

gRPC es un framework open-source RPC de alto desempeño que usa HTTP/2 para transporte y Protocol Buffers para serialización (Microsoft Learn, 2026). Emplea canales (Channel) y _stubs_ generados a partir de definiciones .proto. Soporta cuatro modos de RPC: unario (request-respuesta), streaming de servidor, streaming de cliente y _bidireccional_ (Microsoft Learn, 2026). Según Microsoft, gRPC es idóneo para microservicios con exigencia de baja latencia y rendimiento (Microsoft Learn, 2026). Los mensajes gRPC se transmiten en formato binario compacto (Protobuf) (Microsoft Learn, 2026), lo que reduce el ancho de banda y la latencia frente a JSON/HTTP tradicional. Además, HTTP/2 permite multiplexar múltiples llamadas sobre la misma conexión y priorizarlas, mejorando la eficiencia. gRPC garantiza el orden de entrega de mensajes dentro de cada llamada RPC (gRPC, 2024), aunque no impone orden global entre múltiples llamadas concurrentes.

### Brokers de mensajería relevantes

**Apache Kafka** (Apache 2.0): un sistema de streaming distribuido basado en registros inmutables. Destaca en _throughput_ masivo (superior a 1M msg/s por Broker con tuning) (Onidel Cloud, 2025), a costa de latencias típicas en el orden de 10–50 ms (Onidel Cloud, 2025). Kafka almacena mensajes en tópicos particionados, soporta replicación para durabilidad, y ofrece _exactly-once_ mediante productores idempotentes y transacciones de consumición (Onidel Cloud, 2025). Su madurez es alta, con ecosistema amplio (Kafka Streams, Connect) y amplio uso en industria. Sin embargo, no provee gRPC nativo; se accede vía librerías propias o _APIs_ REST.

**Apache Pulsar** (Apache 2.0): similar a Kafka pero con arquitectura segmentada (Brokers + BookKeeper). En benchmarks recientes Pulsar supera significativamente a Kafka en rendimiento (hasta ~2.5× throughput y 100× menor latencia en P99.99 según StreamNative) (2022 Benchmark Report, 2022). Ofrece colas y streams, replicación multizone y también _exactly-once_. A partir de la versión 2.7 Pulsar puede exponer una interfaz gRPC mediante un **plugin oficial** (gRPC protocol handler) (cbornet, 2022), facilitando integración. Pulsar puede enrutarse a Redis o usarse con su propio back-end de BookKeeper. Su licencia es Apache 2.0.

**RabbitMQ** (MPL 1.1): Broker clásico AMQP con extensiones (MQTT, STOMP). Su fortaleza es el enrutamiento sofisticado: soporta exchanges _direct_, _fanout_, _topic_, _header_, permitiendo patrones fan-out, filtros y priorización. La latencia suele ser moderada (~5–20 ms bajo carga típica) (Onidel Cloud, 2025) y el throughput está en decenas de miles de msg/s por nodo (Onidel Cloud, 2025). RabbitMQ ofrece _at-least-once_ (ack manual) y, mediante mecanismos externos, _exactly-once_ (por ejemplo, con deduplicación en cliente) (sanj.dev, 2025). No soporta gRPC nativo (AMQP), pero hay conectores/plugins que exponen APIs HTTP/gRPC. RabbitMQ no se basa en pull, sino que empuja mensajes a consumidores conectados.

**NATS / JetStream** (Apache 2.0): sistema ligero de mensajería _pub/sub_ originalmente en memoria. NATS básico ofrece latencias **sub-milisegundo** y throughput extremo (decenas de millones msg/s en escenario _fire-and-forget_) (Onidel Cloud, 2025). Su módulo persistente JetStream añade cola con respaldo en disco, transacciones y orden, manteniendo rendimiento alto (1–2M msg/s persistente (Index, 2026)). JetStream admite _exactly-once_ al menos en la interfaz (mensajes reenviados tras fallo) pero no garantiza automáticamente duplicados; el cliente debe manejar ids. NATS es minimalista, en Go, y no implementa gRPC por defecto (protocolo propio); sin embargo, su bajo overhead facilita su uso en entornos de microservicios.

**Redis Streams** (BSD-3): no es un Broker dedicado sino una estructura de datos de Redis para colas/streams. Como _log_ append-only en memoria/disk, Streams puede operar como un Broker ligero (millones msgs/s, latencia sub-ms) (Redis, 2026). Soporta grupos de consumo (consumer groups), donde múltiples consumidores leen cooperativamente y confirman con _XACK_, logrando semántica _exactly-once_ a nivel de stream (Redis, 2026). Redis no usa modelo _push_, sino que el consumidor _pull_ con XREADGROUP en Polling o _blocking_. Redis carece de un enrutamiento complejo, pero su integración nativa con gRPC se lograría escribiendo directamente a la base Redis en servicios gRPC o usando gRPC-Redis bridges (hoop.dev, 2025). Redis Streams puede servir como “memoria intermedia” muy veloz entre productor y consumidor (Redis, 2026).

En resumen, cada Broker tiene fortalezas distintas (ver tabla comparativa abajo) y licencias variadas (Kafka/Pulsar/NATS Apache-2.0, RabbitMQ MPL, Redis BSD).

### Patrones de mensajería

Los patrones **fan-out** y **fan-in** son comunes en arquitecturas concurrentes. _Fan-out_ entrega un mensaje a múltiples destinos paralelamente, sin esperar respuesta (Wikipedia, 2022). Es equivalente a un broadcast o pub/sub; p. ej., un Exchange _fanout_ de RabbitMQ encola una copia a cada cola ligada. _Fan-in_ es el reverso: múltiples productores envían a un único consumidor, como en la agregación de resultados de tareas paralelas. Por ejemplo, Azure Durable Functions lo describe como “ejecutar múltiples actividades en paralelo y luego agregar los resultados” (Microsoft Learn, 2026). En un Broker con fan-out vía gRPC, un servicio gRPC usaría streaming server-side para enviar datos a todos los clientes suscritos. En la práctica, se implementa guardando el stream de cada cliente y escribiendo en todos ellos cuando llega un evento (Stack Overflow, 2019). Así, gRPC permite implementaciones de fan-out mediante llamadas bidireccionales (véase más en _Implementaciones_).

### Cola transaccional con pull sobre gRPC

Una cola transaccional asegura que la entrega de mensajes sea atómica con otro estado (p. ej. base de datos). En este modelo, el consumidor _extrae_ (pull) mensajes bajo una transacción: recibe un mensaje, realiza operaciones, y luego hace _commit_ o _rollback_. Si ocurre un error antes del commit, el mensaje se reencola, garantizando integridad (Microsoft Learn, 2026). Tradicionalmente se ve en JMS transaccional o MSMQ: “Message Queuing mueve el mensaje de una cola a otra, exactamente una vez, mediante transacción” (Microsoft Learn, 2026). En gRPC esto equivale a exponer un método RPC como GetMessage() que devuelve un stream o bloquea hasta haber un mensaje. El consumidor llamaría repetidamente a este RPC, procesaría el mensaje y confirmaría con otro RPC (Acknowledge) o bien dejaría expirar la llamada para rollback. Así se puede simular _pull_ y transaccionalidad. Algunos frameworks (e.g. Azure Service Bus, JMS) permiten recibir mensajes con confirmación manual; aquí habría que implementar esa lógica en el servidor gRPC y el Broker subyacente.

### Redis como memoria intermedia de mensajes

Redis se usa frecuentemente como **cache / buffer** en sistemas de mensajería por su alta velocidad. En particular, **Redis Streams** ofrece funcionalidades tipo Broker: es un log inmutable que almacena mensajes, con operaciones eficientes de append/read (Redis, 2026). Según Redis Labs, Streams puede procesar millones de puntos de datos por segundo con latencia <1 ms (Redis, 2026). Los **grupos de consumidores** de Streams permiten repartir una misma secuencia entre varios consumidores: cada mensaje es asignado a un consumidor y debe confirmarse (XACK) para no volver a entregarse. Esto garantiza _exactamente una vez_ en la práctica, ya que un mensaje pendiente (por caída) queda a la espera de nuevo consumo (Redis, 2026). En un diseño de gRPC + Broker, Redis podría actuar como almacén intermedio: por ejemplo, los servicios gRPC escriben mensajes a Redis Streams, y el Broker o consumidores los leen desde allí. Redis además es un datastore en memoria, lo que lo hace útil como búfer volátil entre productores y el backend persistente. En arquitecturas reales (p.ej. sistemas de chat o LLM), se usa Redis Streams para “push streaming”: el servidor produce tokens a Redis y el consumidor los lee en tiempo real (Redis, 2026). En síntesis, usar Redis como memoria intermedia combina la rapidez _in-memory_ con la semántica de cola (durable y transaccional) (Microsoft Learn, 2026).

### 2.1.6. Arquitectura Hexagonal (puertos y adaptadores)

La idea central es aislar la lógica de negocio en un núcleo central y exponer únicamente puertos (interfaces) hacia el exterior, conectados a adaptadores concretos (Jayaraman, 2024). Cada puerto define una API abstracta; los adaptadores (por ejemplo, controladores REST, repositorios de BD, clientes de otros servicios) implementan esos puertos. De este modo, el dominio no depende de detalles externos (bases de datos, UI, librerías), sino que estos se inyectan hacia el núcleo (Inversión de Control). Cockburn sugiere “crear la aplicación para que funcione sin interfaz de usuario ni base de datos, de modo que pueda probarse y desplegarse independientemente” (Bonin M. , 2020). Esto garantiza flexibilidad: el núcleo permanece inalterado al cambiar la UI, BD u otros servicios. El flujo típico es: Adaptador externo → Puerto → Lógica de negocio → Puerto → Adaptador (actor primario guía al primario, luego secundario, en una cadena de llamadas). El desacoplo resultante favorece la prueba de unidades en el dominio sin dependencias externas (Jayaraman, 2024).

Ventajas: Modularidad y escalabilidad independiente de UI/BD (Jayaraman, 2024), facilita TDD y CI/CD al poder probar/desplegar componentes aisladamente (Jayaraman, 2024). Permite postergar decisiones técnicas (p.ej. elección de base de datos) sin impactar el dominio (Bonin M. , 2020).

Desventajas: Introduce complejidad adicional (más capas y proyectos) (Bonin M. , 2020) y costo de mantenimiento de adaptadores. Algunos autores (Fowler 2003) advierten que puede ocultar la asimetría entre proveedor y consumidor de servicios, dado que todos los adaptadores se tratan simétricamente [16]. También puede ser sobre ingeniería si el dominio no cambia con frecuencia [6]

## Trabajos Relacionados

**AMQP-Message-Broker** (Go): implementa un Broker inspirado en RabbitMQ usando gRPC y Redis Streams (muhammadharis, 2019). Soporta exchanges _Fanout_ y _Direct_ (enrutamiento por key) (muhammadharis, 2019), y utiliza Redis Streams como backend de mensajería. Este ejemplo prueba la factibilidad de un Broker gRPC personalizado con colas transaccionales en Redis.

**Risala** (Go): Broker educativo basado en gRPC. La versión 1.0 permite publicar, consumir y ackear mensajes vía gRPC; en su roadmap incluye exchange _Fanout_ (ya implementado) y _Topic_ (melyouz, 2024). Ilustra cómo construir colas transaccionales pull: el consumidor realiza streaming RPC y el servidor mantiene pendientes y retransmite si falla el ACK.

**BullMQ** (Node.js) y **Cola** (Ruby): son librerías de colas transaccionales que usan Redis. Permiten push/pull de mensajes, retries y confirmaciones atómicas usando transacciones de Redis (MULTI/EXEC). No usan gRPC directamente, pero se podrían exponer sus APIs mediante gRPC para integrar con microservicios.

**Apache Ignite/Geode**: no son Brokers pero usan memoria distribuida (incl. Redis API) como colas transaccionales. Proyectos como **Redisson** (Java) implementan colas transaccionales en Redis.

**Implementación gRPC integrada**: en el ámbito de soluciones comerciales, algunos productos (e.g. Google Cloud Pub/Sub, AWS gRPC SDK) ofrecen APIs gRPC para colas nativas en la nube. También hay _gateways_ gRPC para Kafka (como o frameworks como gRPC-Kafka bridge), aunque menos difundidos.

**Empresarial / Cloud:** Amazon Web Services (2022) presenta una guía _prescriptiva_ que promueve la adopción de la **arquitectura hexagonal** en proyectos empresariales, señalando que al centrarse en el dominio facilita la gestión de la complejidad y permite un desarrollo ágil (DDDesign, TDD) (Oruc, F., Goby, D., Kunce, D. & Ploski, M, 2022). El libro de Martin (2017) y múltiples plantillas empresariales (por ejemplo, la solución _CleanArchitecture_ de Jason Taylor en ASP.NET Core) demuestran la popularidad de Clean Architecture en entornos de microservicios y API empresariales (jasontaylordev, 2026).

**Open Source / Ejemplos prácticos:** Netflix publicó un artículo y ejemplo de implementación hexagonal en un microservicio de catálogo; su repositorio [zevolution/netflix-hexagonal-architecture] muestra cómo cambiar de proveedor GitHub a GitLab simplemente intercambiando adaptadores, sin alterar la lógica central (zevolution, 2021). En el mundo Java/Spring, Baeldung (2022) ejemplifica una API de registro de usuario siguiendo capas Clean: “usaremos sus capas originales – entidades, casos de uso, adaptadores y frameworks” (Gilvan Ornelas & Bruno Fontana, 2024). Muchas plantillas _onion/Clean_ existen en repositorios públicos para distintos lenguajes (e.g. Swift, Go, Java, .NET) evidenciando su adopción.

## Conclusiones del Estado del Arte

**Consistencia y orden:** Los Brokers distribuidos deben decidir orden de entrega y consistencia. Kafka y Pulsar garantizan orden dentro de cada partición (topic), pero no orden global. NATS JetStream garantiza orden _por sujeto_. RabbitMQ garantiza orden FIFO por cola. Al usar patrones fan-in/out, es clave diseñar claves de partición o routing para preservar orden cuando importe (p.ej. usar un topic de Kafka con una sola partición para orden total). Redis Streams conserva orden dentro de cada stream. El reto es balancear orden versus paralelismo: más particiones/consumidores mejor throughput pero potencial perdida de orden secuencial.

**Semánticas de entrega:** Como referencia, NATS y RabbitMQ ofrecen al menos una vez por defecto (requieren ACK). Kafka y Pulsar permiten _exactly-once_ total mediante transacciones (productor-consumidor). Exactly-once implica sobrecarga (coordinación 2PC) y suele reducir throughput. Por ejemplo, Kafka sin transacciones es más rápido. En muchas aplicaciones críticas se prefiere _at-least-once_ con idempotencia en el consumidor. Se debe evaluar si la lógica de la aplicación (y la base de datos de destino) puede tolerar duplicados o requiere full exactly-once.

**Escalabilidad:** La escalabilidad horizontal se logra con particiones/clusters. Kafka escala añadiendo Brokers y particiones. NATS suele formar un cluster mesh o uso de _leaf nodes_. RabbitMQ clústeres y federación. Redis Streams escala con clúster Redis (limitado por CPU/mem). Al diseñar fan-out via gRPC, hay que prever conexiones concurrentes: gRPC maneja bien cientos de conexiones mediante multiplexación HTTP/2, pero miles de streams pueden requerir load balancing (e.g. Envoy con _gRPC proxy_). Diagramas de escalamiento deben contemplar replicación de Brokers y particiones de topics.

**Monitoreo en tiempo real:** Es crítico monitorear latencia end-to-end, throughput y backlog. Herramientas como Prometheus/Grafana o soluciones Cloud (Datadog) permiten recolectar métricas de Brokers. Por ejemplo, Datadog Data Streams Monitoring mide latencia de extremo a extremo y detecta bloqueos en la cola. Se recomiendan métricas clave: tasa de mensajes publicados/consumidos, latencias p50/p99, profundidad de cola (lag del consumidor), TPS, errores de entrega, CPU/memoria de nodos. Sistemas observables integrar exportadores: Kafka usa JMX (o JMX a Prometheus), RabbitMQ expone plugin Prometheus, NATS tiene métricas Prometheus nativas. También deben trazarse flujos transaccionales (OpenTelemetry/Jaeger) para diagnosticar cuellos de botella. La monitorización en tiempo real debe detectar productores/consumidores caídos, mensajes estancados o variaciones de latencia.

**Tolerancia y disponibilidad:** Se debe planear _alta disponibilidad_: réplicas de Brokers (Kafka Replication Factor, NATS JetStream RAFT, RabbitMQ quorum queues), mecanismos de failover, y reinicios suaves. El uso de Redis como buffer añade otro punto de falla (aunque Redis Cluster o Sentinel mitigan riesgos). Consistencia en caso de partición de red (split-brain) y recuperación de estado son desafíos adicionales.

**Costo y complejidad:** En general, Kafka/Pulsar con transacciones son más complejos de operar (consumen memoria/disk, Zookeeper/KRaft) que opciones ligeras (NATS, Redis). Debe evaluarse el tradeoff entre rendimiento y simplicidad operacional.

Según se plantea en el estado del arte, la arquitectura hexagonal tiene un importante atractivo para poder separar y controlar los flujos sin acoplamiento, permitiendo una limpieza y claridad para testear la solución y obtener una cobertura de casos de prueba aceptable según los estándares de la industria. Algunas de sus características según su autor, Alistair Cockburn:

**Ventajas:**

Modularidad y escalabilidad independiente de UI/BD, facilita TDD y CI/CD al poder probar/desplegar componentes aisladamente (Jayaraman, 2024). Permite _postergar decisiones técnicas_ (p.ej. elección de base de datos) sin impactar el dominio (Bonin M. , 2020).

  
**Desventajas:**

Introduce complejidad adicional (más capas y proyectos) (Bonin M. , 2020) y costo de mantenimiento de adaptadores. Algunos autores (Fowler 2003) advierten que puede _ocultar la asimetría_ entre proveedor y consumidor de servicios, dado que todos los adaptadores se tratan simétricamente (Wikipedia, 2022). También puede ser sobre ingeniería si el dominio no cambia con frecuencia.

Tabla 1. Comparaciones entre las soluciones presentadas y la propuesta.

|**Criterio**|**gRPC (puro)**|**Apache Kafka**|**RabbitMQ**|**NATS**|**Propuesta (gRPC + Redis)**|
|---|---|---|---|---|---|
|**Modelo de comunicación**|Síncrono (RPC) + Streaming|Asíncrono (log distribuido)|Asíncrono (colas / pub-sub)|Pub/Sub ligero|**Híbrido (streaming + async)**|
|**Soporte tiempo real**|Excelente|Limitado|Bueno|Muy bueno|**Excelente (nativo)**|
|**Latencia**|Muy baja|Media|Media|Muy baja|**Muy baja**|
|**Streaming bidireccional**|Sí (nativo)|No|No|Limitado|**Sí (nativo)**|
|**Broadcast de eventos**|Manual|Parcial (topics)|Parcial|Sí|**Nativo (fan-out + streaming)**|
|**Patrones fan-in / fan-out**|Limitado|Sí|Sí|Sí|**Sí (optimizados)**|
|**Persistencia de mensajes**|No|Alta (durable)|Alta|Opcional|**Media (Redis)**|
|**Idempotencia**|No nativa|Compleja (configuración)|Externa|Limitada|**Integrada (Redis)**|
|**Modelo de consumo**|Push|Pull|Push/Pull|Push|**Push + Pull (dual)**|
|**Escalabilidad**|Alta|Muy alta|Alta|Muy alta|**Alta**|
|**Complejidad operativa**|Baja|Alta|Media|Baja|**Media**|
|**Casos de uso principales**|RPC entre servicios|Event streaming masivo|Integración de sistemas|Mensajería ligera|**Eventos en tiempo real + resiliencia**|

# Objetivos y Metodología de Trabajo

Este capítulo es el puente entre el estudio del dominio y la contribución a realizar. Según el tipo concreto de trabajo, el bloque se puede organizar de distintas formas, pero los siguientes elementos deberían estar presentes con mayor o menor detalle.

## Objetivo Principal

Diseñar, implementar y validar un Broker de mensajería distribuido que habilite comunicación en tiempo real mediante streaming sobre gRPC, complementado con un mecanismo asincrónico basado en Redis, permitiendo la ejecución eficiente de patrones de mensajería tipo broadcast, fan-in y fan-out, y garantizando la idempotencia en el procesamiento de eventos en entornos concurrentes.

Este objetivo persigue demostrar que es posible construir una alternativa híbrida a los Brokers tradicionales, optimizada para escenarios donde la baja latencia y la comunicación en tiempo real son requisitos críticos, sin renunciar a mecanismos de resiliencia y recuperación propios de sistemas asincrónicos

## Objetivos Específicos

Para alcanzar el objetivo principal, se plantean los siguientes objetivos específicos:

- **Analizar** las limitaciones de los sistemas de mensajería tradicionales en escenarios que requieren comunicación en tiempo real y alta concurrencia.
- **Evaluar** el uso de streaming sobre gRPC como mecanismo de comunicación eficiente frente a modelos basados exclusivamente en colas.
- **Diseñar** una arquitectura de Broker híbrido que combine comunicación síncrona en tiempo real y mecanismos asincrónicos de respaldo.
- **Definir** e implementar patrones de mensajería tipo broadcast, fan-in y fan-out sobre conexiones persistentes utilizando streaming bidireccional.
- **Establecer** un modelo de gestión de mensajes asincrónicos basado en Redis que permita la recuperación de mensajes no procesados mediante un enfoque pull.
- **Implementar** un prototipo funcional del Broker utilizando el lenguaje Go, integrando gRPC como núcleo de comunicación y Redis como sistema de soporte para la asincronía.
- **Desarrollar** un SDK que abstraiga la complejidad de interacción con el Broker, facilitando su integración en sistemas externos.
- **Validar** el comportamiento del sistema bajo condiciones de carga, evaluando su capacidad de manejar múltiples productores y consumidores concurrentes.
- **Evaluar** la idempotencia en el procesamiento de mensajes, asegurando la correcta gestión de duplicados en escenarios distribuidos.

## Metodología de Trabajo

La metodología adoptada en este trabajo se basa en un enfoque experimental e iterativo, orientado a la construcción y validación de un sistema software distribuido. Este enfoque permite no solo desarrollar la solución propuesta, sino también evaluar su comportamiento en condiciones cercanas reales de uso.

El proceso metodológico se estructura en las siguientes fases:

### Análisis Del Problema

En esta fase se identifican y analizan las limitaciones presentes en los sistemas de mensajería tradicionales, particularmente en lo relativo a:

- Latencias asociadas a sistemas basados en colas.
- Dificultades para implementar comunicación en tiempo real.
- Complejidad en la gestión de idempotencia en sistemas distribuidos.
- Limitaciones en la implementación eficiente de patrones de difusión masiva (broadcast).

Este análisis permite justificar la necesidad de una solución alternativa basada en comunicación persistente y orientada a eventos.

### Diseño de la solución

Se define la arquitectura del sistema propuesto, basada en un modelo híbrido que combina:

- Comunicación en tiempo real mediante streaming sobre gRPC.
- Mecanismos asincrónicos utilizando Redis como almacenamiento en memoria.

En esta fase se especifican:

- Los tipos de interacción soportados (unary, streaming de servidor y streaming bidireccional).
- Los patrones de mensajería implementados (fan-in, fan-out y broadcast).
- El modelo de gestión de mensajes asincrónicos mediante consultas al Broker.
- La estrategia de idempotencia para evitar el reprocesamiento de eventos.

Asimismo, se definen los componentes principales del sistema, así como sus responsabilidades e interacciones.

### Implementación

Se desarrolla un prototipo funcional del Broker utilizando el lenguaje Go, seleccionado por su eficiencia en la gestión de concurrencia.

La implementación incluye:

- Servicios gRPC que gestionan las conexiones y el flujo de mensajes.
- Integración con Redis para almacenamiento temporal y recuperación de mensajes.
- Mecanismos de control de idempotencia.
- Desarrollo de un SDK que encapsula la lógica de comunicación para los clientes.

Se adopta un enfoque modular que facilite la extensibilidad y mantenibilidad del sistema.

### Experimentación

Se diseñan escenarios de prueba orientados a evaluar el comportamiento del sistema bajo condiciones de carga y concurrencia. Entre los escenarios considerados se incluyen:

- Envío de mensajes en modo broadcast a múltiples consumidores simultáneos.
- Simulación de múltiples productores enviando eventos concurrentemente (fan-in).
- Evaluación del comportamiento del sistema en presencia de consumidores intermitentes.
- Uso del mecanismo asincrónico para recuperación de mensajes no procesados.

Para la ejecución de las pruebas se utilizan herramientas de generación de carga y scripts personalizados.

### Evaluación de Resultados

Los resultados obtenidos se analizan utilizando métricas clave, tales como:

- Latencia en la entrega de mensajes.
- Capacidad de procesamiento (throughput).
- Consistencia en la entrega de mensajes.
- Tasa de duplicados y efectividad de la idempotencia.

Estos resultados permiten determinar la viabilidad del sistema propuesto y su adecuación para escenarios de mensajería en tiempo real.

### Análisis Comparativo

Finalmente, se realiza un análisis comparativo conceptual entre la solución propuesta y sistemas de mensajería tradicionales, identificando:

- Ventajas en términos de latencia y comunicación en tiempo real.
- Limitaciones frente a soluciones consolidadas.
- Casos de uso donde la propuesta ofrece mayor valor.

Este análisis permite posicionar la contribución del trabajo dentro del contexto actual de tecnologías de mensajería distribuida.

# Desarrollo del Proyecto

En este capítulo se describe el proceso de desarrollo del sistema propuesto, detallando las decisiones de diseño, la arquitectura adoptada y los componentes principales que conforman la solución. El objetivo es definir una base técnica sólida que permita la implementación de un sistema de mensajería eficiente, escalable y resiliente, orientado a escenarios de alta concurrencia.

Se abordan aspectos como el modelo de comunicación, la organización de los componentes, los mecanismos de distribución de mensajes y las estrategias utilizadas para garantizar el rendimiento y la tolerancia a fallos.

## Análisis

### 4.1.2 Requisitos funcionales

El sistema debe:

- Permitir la **publicación de mensajes** por parte de múltiples productores.
- Soportar el enrutamiento **mensajes** hacia a uno o múltiples subscritores (**modelo síncrono**).
- Soportar la entrega de mensajes a los consumidores, gestionando la no duplicación de entrega de mensajes (**modelo asíncrono**).
- Garantizar la **entrega de mensajes** a los consumidores.
- Permitir el manejo de diferentes patrones de comunicación:
    - publicación/suscripción (pub/sub), modelo “**push**”
    - productor/consumidor, comunicación asíncrona modelo “**pull**”.
- Gestionar múltiples conexiones concurrentes de manera eficiente.

### 4.1.3 Requisitos no funcionales

- Escalabilidad horizontal: capacidad de agregar nodos sin degradar el rendimiento.
- Baja latencia en la entrega de mensajes.
- Alto throughput bajo carga concurrente.
- Resiliencia ante fallos parciales del sistema.
- Eficiencia en el uso de recursos (CPU, memoria, conexiones).
- Observabilidad (métricas, logs, trazabilidad).

### 4.1.4 Arquitectura del Sistema

El sistema se basa en una arquitectura distribuida orientada a eventos, donde los componentes principales interactúan a través de un Broker de mensajería central.

### 4.1.5 Vision general

La arquitectura está compuesta por:

- **Productores (Producers)**: generan y envían mensajes.
- **Broker de Mensajería**: núcleo del sistema, responsable de:
    - recepción de mensajes
    - enrutamiento
    - distribución
- **Consumidores (Consumers)**: reciben mensajes según sus suscripciones. ![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%201.png>)

_Figura 1. Esquema general_

### 4.1.6 Modelo de Comunicación

Se adopta un modelo basado en **gRPC**, que permite:

- Comunicación eficiente sobre HTTP/2.
- Soporte nativo para **streaming bidireccional**.
- Reducción de overhead en comparación con REST/JSON.

Se definen dos tipos principales de interacción:

- **Unary**: envío puntual de mensajes, usado en el modelo asíncrono. Con esta interacción, se implementa la comunicación asíncrona donde los consumidores hacen peticiones al Broker.
- **Binary**: comunicación en tiempo real que se utiliza para implementar las siguientes funcionalidades:
    - **Server Streaming**: el productor envía un mensaje inicial para abrir el canal de comunicación, después solo recibe mensajes de sus consumidores.
    - **Bidirectional Streaming**: productores y consumidores se comunican indistintamente sin esperar confirmación del mensaje enviado.
    - **Client Streaming**: el productor envía a sus consumidores mensajes sin esperar respuesta de estos.

### 4.1.7 Diseño del Broker

El Broker es el componente central y su diseño se basa en:

- Gestión de conexiones concurrentes
- Sistema de enrutamiento por atributo especial del modelo de datos en el mensaje (real time conmunication)
- Colas internas en memoria (in-memory queues). Funcionalidad usada en el modelo de comunicación asíncrono donde interviene una memoria como componente externo al Broker.

### 4.1.8 Modelo de Datos comunicación Síncrona

Modelo de datos para la comunicación síncrona:

- **Subscribers**: arreglo de direcciones donde deben estar los futuros consumidores del mensaje que se envía.
- **Payload**: cuerpo del mensaje, el formato queda a decisión del productor del mensaje

Este diseño permite:

- Flexibilidad en el contenido
- Facilidad de serialización (Protobuf)
- Eficiencia en transmisión

### 4.1.9 Modelo de Datos comunicación Asíncrona

En este modelo de dato interviene la memoria externa. El mensaje que recibe el Broker consta de:

- **Payload**: cuerpo del mensaje definido por el productor

El mensaje que se envía a la memoria para persistencia y que es recibido por los consumidores está compuesto por:

- **Message**: atributo que captura el “Payload” enviado por el productor.
- **MessageId**: identificador del mensaje adicionado por el Broker.
- **CreatedAt**: fecha de creación o entrada del mensaje, adicionada por el Broker.

Este diseño permite:

- Identificación del mensaje por medio del Id para una búsqueda/eliminación precisa.
- Etiquetar el mensaje con la fecha en la que entro al Broker, para logs.

### 4.1.10 Estrategia de Concurrencia

El sistema está diseñado para operar en entornos altamente concurrentes.

Se utilizan:

- **Goroutines** para procesamiento paralelo
- **Canales (channels)** para comunicación interna
- Pools de workers para controlar carga

Se busca evitar:

- Bloqueos innecesarios
- Contención de recursos
- Cuellos de botella en el dispatcher

### 4.1.11 Estrategia de Escalabilidad

Se comparten dos niveles:

Escalabilidad Vertical

- Optimización del uso de recursos
- Manejo eficiente de memoria y conexiones

Escalabilidad Horizontal

- Posibilidad de múltiples instancias del Broker
- Uso potencial de balanceadores de carga
- Diseño desacoplado que permite distribución futura

### 4.1.12 Estrategia de Resiliencia

El sistema incorpora mecanismos básicos para tolerancia a fallos:

- Manejo de desconexiones de clientes
- Reintentos controlados
- Aislamiento de fallos por conexión

Futuras mejoras pueden incluir:

- Persistencia de mensajes
- Replicación entre nodos
- Garantías de entrega (at-least-once, exactly-once)

### 4.1.13 Consideraciones de Rendimiento

Se prioriza:

- Minimizar la serialización/deserialización
- Uso eficiente de conexiones persistentes (gRPC)
- Reducción de copias de memoria

Además, el sistema será evaluado mediante:

- pruebas de carga
- medición de latencia
- análisis de throughput

## Implementación

Comenzamos este apartado con las decisiones de diseño tomadas, seguiremos dando solución a los requisitos funcionales mencionados antes y seguidamente veremos los requisitos no funcionales.

### 4.2.1 Elección de la arquitectura del Broker

Actualmente, contamos con varias arquitecturas que nos brindan ventajas y desventajas, algunas de estas son:

**Arquitectura en Capas (Layered/N-tier)**

Estructura típica

- Controller / API
- Service / Application
- Domain (a veces mezclado)
- Infrastructure (DB, external services)

**Ventajas**

- Muy conocida → **onboarding rápido**
- Fácil de implementar en scaffolding
- Buena para CRUD-heavy systems
- Baja fricción con frameworks (Spring, .NET, etc.)

**Desventajas**

- Acoplamiento vertical fuerte (controller → service → repo)
- Dominio suele degradarse a “anémico”
- Difícil testear sin infraestructura real
- Evolución hacia microservicios suele requerir refactorización

**Arquitectura Hexagonal (Ports & Adapters)**

Estructura típica

- Domain (core puro)
- Application (use cases)
- Ports (interfaces)
- Adapters (DB, HTTP, messaging, etc.)

**Ventajas**

- Alto desacoplamiento → **infraestructura reemplazable**
- Testabilidad extrema (mock de puertos)
- Dominio bien protegido

**Desventajas**

- Mayor complejidad inicial
- Más boilerplate (interfaces, adapters)
- Curva de aprendizaje más alta
- Overengineering si el sistema es simple

**Clean Architecture**

Estructura típica

- Entities
- Use Cases
- Interface Adapters
- Frameworks & Drivers

**Ventajas**

- Separación de responsabilidades muy clara
- Independencia total de frameworks
- Altamente testeable
- Escalable a nivel organizacional

**Desventajas**

- Verbosidad alta
- Puede ralentizar desarrollo inicial
- Difícil de mantener si el equipo no sigue disciplina estricta

Basado en los ejemplos anteriores y las características provistas por (Martin, 2017), se decide tomar la Clean Architecture como guía para el desarrollo del Broker. Cabe destacar, que la elección fundamentalmente fue hecha por el desacople que brinda este tipo de arquitectura, su funcionalidad para ser testeada, y como bien se describe en el libro del autor, la separación de la lógica de negocio de la lógica tecnológica.

![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%202.png>)

_Figura 2. Arquitectura del Broker_

![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%203.png>)

_Figura 3. Estructura de directorios_

### 4.2.2 Implementación del contrato de mensajería mediante Protocol Buffers

En el contexto del sistema propuesto, uno de los pilares fundamentales para garantizar la interoperabilidad, consistencia y evolución controlada de la comunicación entre componentes es la definición de un contrato de datos formal. Para este propósito, se adopta **Protocol Buffers (Protobuf)** como mecanismo de serialización estructurada, permitiendo definir de manera explícita los mensajes intercambiados entre el Broker de mensajería y los consumidores a través del SDK.

#### 4.2.2.1 Definición del contrato

El contrato de comunicación se materializa mediante un conjunto de archivos .proto, donde se especifican todos los mensajes y estructuras necesarias para la transmisión y recepción de eventos dentro del sistema. Estos archivos constituyen la única fuente de verdad (_single source of truth_) respecto al modelo de datos distribuido.

#### 4.2.2.2 Centralización del contrato en un repositorio compartido

Con el objetivo de evitar inconsistencias entre productores y consumidores, el contrato Protobuf se mantiene en un repositorio independiente, versionado y accesible tanto por el Broker como por el SDK.

Este enfoque introduce varias ventajas clave:

- **Consistencia contractual:** Todos los componentes consumen exactamente la misma definición de mensajes.
- **Versionado controlado:** Cambios en el contrato siguen una estrategia explícita (por ejemplo, versionado semántico).
- **Reutilización:** El SDK y el Broker importan el contrato sin duplicación de definiciones.
- **Desacoplamiento:** Permite evolucionar los componentes de forma independiente, siempre que respeten la compatibilidad del contrato.

El repositorio actúa como artefacto compartido que puede ser integrado mediante mecanismos como submódulos, paquetes versionados o dependencias gestionadas (por ejemplo, mediante gestores de paquetes específicos del lenguaje).

#### 4.2.2.3 Generación de código y tipado fuerte

A partir de los archivos .proto, se genera código automáticamente en los lenguajes objetivo (por ejemplo, Go para el Broker). Este proceso permite disponer de estructuras fuertemente tipadas que representan los mensajes definidos, reduciendo errores en tiempo de ejecución y mejorando la robustez del sistema.

La generación del código aporta:

- Validación estructural en tiempo de compilación
- Serialización y deserialización eficiente
- Compatibilidad multiplataforma
- Reducción de ambigüedades en la interpretación de datos

#### 4.2.2.4 Estrategia de evolución del contrato

Dado que el sistema está diseñado para operar en entornos distribuidos y potencialmente heterogéneos, se adopta una estrategia de evolución compatible hacia atrás (_backward compatibility_). Esto implica:

- Uso de identificadores de campo inmutables
- Adición de nuevos campos como opcionales
- Evitar la reutilización de tags eliminados
- Uso de valores por defecto seguros

Estas prácticas garantizan que distintas versiones del sistema puedan coexistir sin interrupciones en la comunicación.

#### 4.2.2.5 Integración con el Broker y el SDK

El Broker utiliza las estructuras generadas para validar, enrutar y procesar los mensajes entrantes y salientes, asegurando que cumplen con el contrato definido. Por su parte, el SDK abstrae la complejidad de serialización, proporcionando a los clientes una interfaz simplificada para interactuar con el sistema de mensajería.

Este modelo refuerza el principio de **contrato explícito en arquitecturas distribuidas**, reduciendo el acoplamiento implícito y facilitando la observabilidad, trazabilidad y gobernanza de los flujos de datos.

### 4.2.3 Implementación del flujo de comunicación en el Broker

La implementación del Broker se fundamenta en un modelo de procesamiento desacoplado, orientado a eventos, donde los componentes del sistema interactúan exclusivamente a través de contratos bien definidos, respetando los principios de la Arquitectura Limpia.

El flujo de comunicación se estructura en torno a las siguientes etapas:

- Recepción del mensaje (Inbound Adapter).
- Orquestación del caso de uso (Application layer).
- Validación y enriquecimiento (Domain layer). Caso asíncrono.
- Entrega del mensaje (Outbound Adapter).
- Gestión de errores y reintentos.

Cada una de estas etapas esta implementada en una capa especifica, garantizando independencia de framework, testabilidad y bajo acoplamiento.

#### 4.2.3.1 Configuración del sistema

El sistema implementa un modelo de configuración estructurado por ámbitos, donde cada componente de infraestructura o capacidad del sistema define su propia sección de configuración fuertemente tipada.

A diferencias de enfoques planos basados en variables globales o estructuras monolíticas, este deseño permite:

- Aislamiento de responsabilidades de configuración
- Alta cohesión por componente
- Facilidad de evolución y extensión
- Validación tipada en tiempo de inicialización.

Dentro de este enfoque, configuraciones como “RedisConfig” no son entidades aisladas, sino subestructuras especializadas dentro de un agregado mayor de configuración del sistema.

El sistema consta de los siguientes apartados de configuración:

- GrpcConfig
    - En esta sección, se tienen: el puerto de escucha para la comunicación gRPC, el token que se envía en cada comunicación como validación de comunicación segura entre sistemas.
- RestConfig
    - Al igual que en la sección anterior, esta subestructura contiene campos semejantes para la escucha de la comunicación usando el protocolo HTTP, la cual es usada para la trazabilidad y el monitoreo. Cuenta con un campo adicional el cual es usado para permitir o denegar rangos de redes.
- CertFonfig
    - Esta subestructura, tiene una relevancia adicional, ya que permite si sus campos son cargados con la información esperada, hace de la comunicación del Broker sea segura, usando la capa TSL.
    - Consta de los siguientes campos:
        - KeyFile: debe contener la ruta donde se almacene la clave del certificado.
        - SslCaCert: debe contener la ruta donde se almacene el ca del certificado.
        - SslCert: debe contener la ruta donde se encuentra el certificado.
- RedisConfig
    - Esta subestructura contiene todos los atributos de configuración necesarios y mínimos para formalizar una comunicación con la memoria externa donde se persistirán los mensajes para la comunicación asíncrona.
    - Sus campos son:
        - Port: puerto de escucha de solicitudes de entrada
        - MemoryDB: este campo define la partición o base de datos en memoria que Redis debe crear para persistir los mensajes asíncronos.
        - CheckerDB: este campo define la partición o base de datos en memoria que Redis creará para gestionar la no duplicación de mensajes por medio del “idempotency”.
        - IdemPotencyEx: este campo define cuanto tiempo se mantendrá un identificador de un consumidor o productor en memoria.
        - Host: ruta donde se encontrará la memoria
        - Password: credencial para poder interactuar de forma segura con la memoria.
        - Username: nombre el usuario que se usará en cada comunicación.
        - StreamID: atributo que define el identificador del stream para la comunicación con la memoria.
        - GroupID: define el nombre o identificador del grupo donde los consumidores harán las búsquedas de nuevos mensajes.
        - Tls: este campo define si la comunicación será segura usando TLS o no.
- LogConfig
    - Esta subestructura contiene los atributos requeridos para definir como el componente de logs va a funcionar.
    - LogMode: define como será la operación de logs, se definen dos tipos: en consola y transmitiendo la comunicación hacia un servicio externo.
    - LogUrl: si la configuración se define en el campo anterior hacia un sistema externo, entonces este campo define la URI donde se encontrará ese sistema.
- Config
    - Esta es la estructura padre que contiene a todas las anteriores.

El sistema hace uso de un módulo o librería muy común que gestiona la carga de esta estructura, ya sea el caso de un archivo **.json** o de las variables de entorno, este módulo se llama **viper**. Para este caso, se decide que la carga de variables solo sea por medio de las variables de entorno, por lo que previamente, estas estructuras deben ser llevadas al ambiente donde se dese usar el Broker.

Antes de llevar las estructuras a sus futuros receptores, estas pasan un proceso mínimo de validación, lo que permite que no se levante el sistema sin al menos tener identificados sus puertos y llaves de seguridad.

#### 4.2.3.2 Bootstraps

Este directorio no forma en si mismo una capa de la Arquitectura Limpia, pero es muy útil y recomendado su uso para gestionar todo el engranaje de las capas. En este paso de configuración es donde se implementa y valida que todas las capas del sistema tienen la configuración mínima requerida para su funcionamiento.

Consta de cuatro funciones que tienen definida sus responsabilidades, estas son:

- gRPCServer: gestiona toda la configuración de los actores que participan en la comunicación síncrona y asíncrona que usan el framework gRPC.
- restServer: gestiona toda la configuración del controlador para el uso de la telemetría y monitoreo del sistema.
- monitoring: gestiona la configuración y define el tipo de métricas que se usarán en el sistema.
- RunApp: función que arranca el sistema y hace llamado a las funciones anteriores, hace función de la una tubería, donde se engrana cada proceso.

#### 4.2.3.3 Implementación del caso de uso Broker

El caso de uso del Broker constituye el núcleo de la comunicación síncrona en tiempo real dentro del sistema. Su responsabilidad principal es orquestar el flujo de mensajes entre los productores (controladores de entrada) y los consumidores (suscriptores), habilitando patrones de distribución como _fan-in_ y _fan-out_ de forma eficiente y desacoplada.

**Responsabilidad y alcance**

A diferencia de otros casos de uso dentro de la arquitectura, este componente no implementa lógica de negocio ni manipula entidades de dominio. Su función es estrictamente operativa y se centra en:

- Recibir mensajes desde la capa de entrada (controladores)
- Validar su conformidad estructural (basado en el contrato Protobuf)
- Orquestar su distribución hacia múltiples suscriptores
- Coordinar la comunicación con el cliente encargado de gestionar los canales de conexión

Este diseño responde al principio de separación de responsabilidades, donde el _broker use case_ actúa como un _application service_ especializado en mensajería en tiempo real.

**Flujo de comunicación**

El flujo gestionado por este caso de uso puede describirse en las siguientes etapas:

- **Recepción del mensaje:**  
    El controlador recibe una solicitud externa y la transforma en un mensaje estructurado según el contrato definido en el Data transfer Object que es utilizado por él caso de uso.
- **Delegación al caso de uso:**  
    El mensaje es transferido al caso de uso del Broker sin introducir lógica adicional de negocio, manteniendo la capa de entrada lo más delgada posible.
- **Orquestación (fan-in / fan-out):**
    - _Fan-in:_ múltiples productores pueden enviar eventos concurrentemente hacia el Broker.
    - _Fan-out:_ el Broker distribuye el mensaje a todos los suscriptores interesados, según criterios previamente definidos (por ejemplo, tópicos o canales).
- **Delegación al cliente de comunicaciones:**  
    El caso de uso no gestiona directamente las conexiones de red. En su lugar, delega esta responsabilidad a un cliente especializado que abstrae la gestión de canales.
- **Entrega a subscriptores:**  
    El cliente se encarga de transmitir el mensaje a los consumidores finales, garantizando la entrega en tiempo real.

**Desacoplamiento mediante cliente de comunicación**

Un aspecto clave en esta implementación es la introducción de un cliente (adaptador) responsable de la comunicación con los suscriptores. Este componente encapsula:

- Gestión de conexiones activas
- Serialización/deserialización final
- Manejo de errores de transporte
- Control de sesiones o canales

El caso de uso interactúa con este cliente a través de una interfaz, lo que permite:

- Sustituir el mecanismo de transporte sin afectar la lógica de orquestación
- Facilitar pruebas unitarias mediante mocks
- Mantener la independencia respecto a frameworks o protocolos específicos

**Ausencia de lógica de dominio**

Es importante destacar que este caso de uso no depende de entidades de dominio ni ejecuta reglas de negocio. Esto lo posiciona como un componente transversal dentro de la arquitectura, enfocado exclusivamente en la infraestructura de comunicación.

Esta decisión de diseño aporta:

- Mayor simplicidad en la implementación
- Alta reutilización del componente
- Reducción del acoplamiento con el dominio
- Mayor facilidad de escalado horizontal

**Rol dentro de la arquitectura limpia**

Dentro del esquema de arquitectura limpia, el caso de uso del Broker se ubica en la capa de aplicación, actuando como intermediario entre:

- **Capa de entrada:** controladores que reciben solicitudes externas
- **Capa de infraestructura:** cliente de comunicación que gestiona los canales

Este posicionamiento refuerza su rol como coordinador del flujo de datos, sin comprometer la independencia de las capas internas del sistema.

**Servicios utilizados en el caso de uso Broker**

Para poder completar el funcionamiento del caso de uso Broker, se implementa la lógica de cada servicio que este caso de uso tendrá, estos servicios son:

- Servicio de comunicación cliente (Client Stream)
- Servicio de comunicación servidor (Server Stream)
- Servicio de comunicación bidireccional (Bidirectional Stream)

Cada uno de estos servicios tiene su interfaz de entrada (DTO) definida en el archivo dto.go, y a su vez hacen uso de la interfaz de conexión con el cliente que crea la conexión con los subscriptores.

#### 4.2.3.4 Implementación del caso de uso Sqs

El caso de uso Sqs es responsable de gestionar la comunicación asíncrona dentro del sistema, permitiendo desacoplar temporalmente a productores y consumidores mediante el uso de una memoria intermedia. En esta arquitectura, dicha memoria se implementa utilizando Redis, el cual actúa como mecanismo de persistencia efímera y buffer de mensajes.

A diferencia del caso de uso del _Broker_, este componente sí interactúa directamente con entidades de dominio, ya que los mensajes que se transmiten representan eventos o comandos con significado dentro del contexto del negocio.

**Responsabilidad y alcance**

El caso de uso Sqs cumple un rol dual dentro del sistema:

- **Producción de mensajes:** recibe solicitudes desde la capa de entrada, construye entidades de dominio que representan el mensaje y las persiste en Redis.
- **Consumo de mensajes:** recupera mensajes almacenados y los entrega a los consumidores cuando estos los solicitan.

**Sus responsabilidades específicas incluyen**:

- Transformar entradas externas en entidades de dominio válidas
- Persistir dichas entidades en la memoria intermedia
- Orquestar la recuperación de mensajes
- Coordinar la comunicación con el cliente de acceso a Redis

Este enfoque permite implementar un patrón de _message queue_ simplificado, alineado a las necesidades del sistema.

**Flujo de comunicación**

El flujo del caso de uso puede dividirse en dos operaciones principales:

**Publicación (write path):**

- El controlador recibe una solicitud externa.
- Se construye una entidad de dominio que encapsula el mensaje, incluyendo su semántica de negocio.
- El caso de uso valida la integridad de la entidad.
- Se delega al cliente de Redis la persistencia del mensaje en la estructura correspondiente.
- Se confirma la operación al productor.

**Consumo (read path):**

- Un consumidor solicita mensajes disponibles.
- El caso de uso interactúa con el cliente de Redis para recuperar mensajes pendientes.
- Los mensajes son deserializados y reconstruidos como entidades de dominio.
- Se entregan al consumidor respetando el orden y las reglas definidas.
- Opcionalmente, se eliminan o marcan como procesados.

Este modelo desacopla completamente los tiempos de producción y consumo, permitiendo mayor resiliencia ante picos de carga.

**Uso de entidades de dominio**

Una característica distintiva de este caso de uso es la utilización explícita de entidades de dominio para representar los mensajes. Estas entidades encapsulan:

- Estructura del mensaje
- Validaciones de integridad
- Reglas asociadas al negocio
- Identificadores y metadatos relevantes

Esto asegura que cualquier dato persistido en Redis cumple con las invariantes del sistema, evitando la propagación de estados inconsistentes.

**Integración con Redis como memoria intermedia**

Redis se utiliza como mecanismo de almacenamiento de baja latencia, adecuado para escenarios de mensajería asíncrona. Dependiendo de los requisitos, pueden emplearse distintas estructuras:

- **Listas:** para colas FIFO simples
- **Streams:** para procesamiento más avanzado con grupos de consumidores
- **Pub/Sub:** en escenarios híbridos (aunque menos persistentes)

Para el caso en cuestión se utiliza expresamente el mecanismo **Stream,** el cual permite crear un grupo de consumidores donde se guardarán temporalmente estos mensajes asociados a un _stream id._

El acceso a Redis se encapsula mediante un cliente especializado, el cual abstrae:

- Operaciones de lectura/escritura
- Serialización de datos
- Manejo de errores de conexión

El caso de uso interactúa con este cliente mediante interfaces, manteniendo la independencia respecto a la tecnología concreta.

**Orquestación y desacoplamiento**

El caso de uso actúa como orquestador entre:

- **Capa de entrada:** controladores que reciben solicitudes de productores y consumidores
- **Dominio:** entidades que modelan los mensajes
- **Infraestructura:** cliente Redis que gestiona la persistencia

Este diseño permite:

- Cambiar la tecnología de almacenamiento sin afectar la lógica del caso de uso
- Testear el comportamiento mediante mocks del cliente Redis
- Mantener una clara separación entre lógica de negocio y detalles técnicos

**Consideraciones de consistencia y concurrencia**

En escenarios asíncronos, es fundamental considerar:

- **Consistencia eventual:** los mensajes pueden no ser consumidos inmediatamente
- **Procesamiento concurrente:** múltiples consumidores pueden acceder a la cola
- **Idempotencia:** evitar efectos duplicados en caso de reintentos
- **Orden de mensajes:** especialmente relevante en colas FIFO

Redis ofrece primitivas que permiten abordar estos desafíos, aunque su correcta utilización depende del diseño del caso de uso.

**Rol dentro de la arquitectura limpia**

Dentro de la arquitectura limpia, este caso de uso se ubica en la capa de aplicación, con dependencias hacia:

- Entidades de dominio (núcleo del sistema)
- Interfaces de infraestructura (cliente Redis)

A diferencia del Broker síncrono, aquí existe una relación directa con el dominio, lo que refuerza su carácter de componente orientado a la lógica de negocio y no únicamente a la infraestructura.

**Servicios utilizados en el caso de uso Sqs**

Para completar la implementación del caso de uso Sqs, se utilizan los siguientes servicios:

- Producer. Este servicio se encarga de recibir el mensaje del productor y enviarlo a la memoria por medio de la interfaz del cliente.
- Consumer. Recibe peticiones del consumidor y busca mensajes en la memoria externa, retorna estos mensajes al consumidor.
- Ack. Este servicio tiene la responsabilidad de marcar un mensaje como leído, una vez que un consumidor envía una confirmación a este caso de uso, el sistema se conecta con la memoria y le comunica que el mensaje ya puede ser eliminado.

Al igual que en el caos de uso anterior, éste tiene sus interfaces de entrada en el archivo dto.go y hace uso de la interfaz cliente para conectar con la memoria externa.

### 4.2.4 Gestión de la comunicación concurrente, comunicación síncrona.

La comunicación síncrona en tiempo real del sistema se fundamenta en un modelo altamente concurrente, donde la coordinación entre productores y consumidores se resuelve mediante primitivas nativas de Go: **goroutines**, **channels** y **sync.WaitGroup**. Este enfoque permite implementar de forma eficiente el patrón **fan-in / fan-out**, garantizando tanto la distribución de mensajes (broadcast) como la agregación de flujos concurrentes.

Adicionalmente, se incorpora el patrón **Worker Pool**, que permite controlar la presión de carga (backpressure), limitar el paralelismo efectivo y asegurar un consumo ordenado y estable frente a picos de tráfico.

Por otro lado, en casos de fallas o perdida de la conexión con alguno de los subscriptores, se activa un patrón de reintentos de conexión. Este enfoque ayuda a reconectar con el subscriptor y reanudar el envío de mensajes. No mantiene memoria de mensajes perdidos, el enfoque es comunicación en tiempo real, por lo que mensajes pasados carecen de importancia.

#### 4.2.4.1 Modelo de concurrencia adoptado

El sistema articula su modelo sobre tres pilares:

- **Fan-out (distribución):** un mensaje entrante es propagado a múltiples consumidores suscritos.
- **Fan-in (agregación):** múltiples fuentes de mensajes convergen en un único flujo de salida.
- **Worker Pool:** conjunto de trabajadores que envían los mensajes recibidos por los productores a los subscriptores.

A nivel de implementación:

- Las **goroutines** encapsulan unidades de trabajo independientes.
- Los **channels** actúan como mecanismos de comunicación y sincronización (message passing).
- Los **WaitGroup** permiten coordinar la finalización de múltiples ejecuciones concurrentes, evitando condiciones de carrera o terminaciones prematuras.

Este diseño elimina la necesidad de locks explícitos en la mayoría de los casos, favoreciendo un modelo basado en comunicación en lugar de memoria compartida.

A continuación, se presenta dos esquemas de como ocurre la interacción con el sistema en este escenario.

![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%204.png>)

_Figura 4. Diagrama de componentes_

![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%205.png>)

_Figura 5. Diagrama de comunicación_

#### 4.2.4.2 Caso StreamClient (Proveedor -> Sistema -> Subscriptores)

En este escenario, el sistema actúa como intermediario entre un proveedor que emite eventos y múltiples subscriptores interesados.

**Flujo**

- El sistema recibe un mensaje desde el proveedor.
- Se extrae un atributo obligatorio del payload (subscribers), el cual define la segmentación de los subscriptores.
- Se resuelve dinámicamente el conjunto de subscriptores asociados.
- Se ejecuta un **fan-out concurrente**, enviando el mensaje a cada subscriptor mediante goroutines independientes.

**Consideraciones técnicas**

- Cada envío se realiza en una goroutine distinta para evitar bloqueos entre consumidores.
- Se puede emplear un WaitGroup para garantizar la entrega completa antes de cerrar el ciclo de procesamiento.
- En escenarios de alta carga, el envío se delega a un **Worker Pool**, evitando la creación descontrolada de goroutines.

**Implicaciones**

- Baja latencia en la propagación.
- Aislamiento entre consumidores (fallos en uno no afectan al resto).
- Escalabilidad horizontal natural.

#### 4.2.4.3 Caso StreamServer (Subscriptores -> Sistema -> Productor)

Este flujo invierte la dirección de la comunicación: múltiples subscriptores envían mensajes hacia el sistema, el cual debe consolidarlos y transmitirlos a un único productor.

**Flujo**

- Cada subscritor emite mensajes de manera independiente.
- El sistema recibe estos mensajes de forma concurrente.
- Los mensajes se insertan en un buffer channel compartido.
- El servicio asociado en esta operación devuelve los mensajes al productor, mediante la lectura del buffer channel donde los workers escriben los mensajes.

**Implementación clave**

- El **buffer channel** desacopla la velocidad de producción de los subscriptores respecto al consumo del productor.
- El patrón **fan-in** se materializa al consolidar múltiples entradas en un único canal de salida
- Los workers permiten:
    - Controlar el throughput
    - Evitar saturación del productor
    - Aplicar políticas de reintentos o backoff si es necesario

**Implicaciones**

- Tolerancia a ráfagas de mensajes.
- Control explícito del flujo (backpressure).
- Orden relativo no garantizado (dependiendo de la concurrencia).

#### 4.2.4.4 Caso StreamBidirectional (Comunicación bidireccional)

Este es el escenario más complejo, donde se combinan simultáneamente los patrones de **fan-in** y **fan-out**, permitiendo comunicación en doble sentido entre proveedor y subscriptores.

**Flujo unificado**

- Entrada desde proveedor → distribución a subscriptores (**fan-out**).
- Entrada desde subscriptores → agregación y envío al productor (**fan-in**).

Ambos flujos coexisten y se ejecutan en paralelo.

**Estrategia de implementación**

- Se definen **channels** independientes por dirección
    - Canal de entrada desde el proveedor.
    - Canal de entrada desde subscriptores.
- Se lanzan **goroutines** dedicadas para cada flujo.
- Se utilizan **select statements** para multiplexar eventos y gestionar múltiples canales simultáneamente.
- Los **WaitGroup** coordinan el ciclo de vida completo de la sesión bidireccional.

**Complejidades abordadas**

- **Sincronización cruzada:** evitar bloqueos entre flujos opuestos.
- **Gestión de cierre:** propagación correcta de señales de finalización **(close(channel))**.
- **Backpressure bidireccional:** control de carga en ambos sentidos.

**Integración del patrón Worker Pool**

El uso del Worker Pool es transversal a los tres casos:

- En **fan-out**, limita la cantidad de envíos concurrentes.
- En **fan-in**, regula el consumo de mensajes agregados.
- En **bidireccional**, permite balancear carga entre ambos flujos.

**Beneficios**

- Prevención de **goroutine leaks**.
- Control de recursos (CPU, memoria).
- Mejor predictibilidad bajo carga.

#### 4.2.4.5 Conclusión técnica

El sistema implementa un modelo de concurrencia robusto y composable, donde los patrones **fan-in/fan-out** y **Worker Pool** se combinan con las primitivas de Go para ofrecer:

- Alta eficiencia en I/O concurrente.
- Escalabilidad natural.
- Bajo acoplamiento entre componentes.
- Control fino del flujo de datos.

La separación clara entre los distintos tipos de streaming (Cliente, Server y Bidireccional) permite adaptar las estrategias de concurrencia a cada caso de uso, maximizando rendimiento sin comprometer mantenibilidad ni claridad arquitectónica.

### 4.2.5 Evitando la duplicación de mensajes, comunicación asíncrona.

En el contexto de la comunicación asíncrona, donde el sistema interactúa con la capa de persistencia basada en **Redis**, se introduce un problema clásico en sistemas distribuidos: la **duplicación de mensajes**. Este fenómeno puede originarse por reintentos, fallos de red, procesamiento concurrente o garantías de entrega _at-least-once_.

Para mitigar este problema, el sistema implementa un mecanismo de **idempotencia**, cuyo objetivo es asegurar que una misma operación lógica no sea procesada más de una vez, independientemente de cuántas veces sea recibida.

#### 4.2.5.1 Estrategia de idempotencia

La solución se basa en la generación y validación de un **identificador único de idempotencia (idempotency key)**, gestionado de forma coordinada entre el SDK cliente y el Broker.

#### 4.2.5.2 Rol del SDK

El **SDK** es responsable de:

- **Generar o recibir** un idempotency key único por cada operación (mensaje).
- Garantizar que dicho identificador sea:
    - Determinístico.
    - Único por contexto de productor/consumidor.
- Inyectar este identificador dentro del mensaje enviado al sistema.

Este diseño delega en el cliente la responsabilidad de unicidad, lo cual es consistente con arquitecturas distribuidas donde el origen del evento tiene mayor contexto semántico.

#### 4.2.5.3 Middleware de idempotencia en el Broker

En el lado del Broker, la validación se implementa mediante un **middleware en la capa de infraestructura**, alineado con los principios de arquitectura limpia (cross-cutting concern).

**Flujo de validación**

- El mensaje entrante contiene un idempotency key.
- El middleware intercepta la petición antes de su procesamiento.
- Se consulta una **base de datos secundaria en Redis**, dedicada exclusivamente a la gestión de idempotencia.
- Se evalúan dos escenarios:
    - Caso A: El identificador no existe
        1. Se registra el idempotency key en Redis.
        2. Se asocia un TTL (Time-To-Live) previamente configurado.
        3. Se permite el flujo normal del mensaje hacia su procesamiento.
    - Caso B: El identificador ya existe
        1. Se considera que el mensaje es un duplicado.
        2. El middleware bloquea el procesamiento redundante.
        3. Se procede a la reinyección controlada de la petición.

#### 4.2.5.4 Uso de partición dedicada en Redis

Para evitar interferencias con otros datos del sistema, se emplea una **segunda partición o base de datos lógica dentro de Redis**, cuya única responsabilidad es la gestión de claves de idempotencia.

**Ventajas del enfoque**

- **Aislamiento funcional:** separación clara respecto a colas, eventos o estados de negocio.
- **Optimización de acceso:** estructura de datos simple (key-value).
- **Gestión automática del ciclo de vida:** gracias al TTL.

#### 4.2.5.5 Gestión del ciclo de vida del idempotency key

El sistema delega en Redis la expiración automática de los identificadores:

- Cada clave se almacena con un TTL definido en función del caso de uso.
- Redis elimina la clave una vez expirada el tiempo.
- Esto permite:
    - Evitar crecimiento indefinido de memoria.
    - Reutilización eventual de claves.
    - No duplicación del consumo de mensajes.

**Consideraciones**

- Un TTL demasiado corto puede permitir duplicados tardíos.
- Un TTL demasiado largo incrementa el consumo de memoria.
- La configuración debe alinearse con:
    - Ventanas de reintento.
    - SLAs del sistema.
    - Naturaleza del dominio (eventos críticos vs. tolerantes).

#### 4.2.5.6 Implicaciones arquitectónicas

La implementación de idempotencia introduce varias propiedades deseables:

- **Consistencia eventual controlada.**
- **Resiliencia ante reintentos.**
- **Protección frente a duplicación en sistemas distribuidos.**
- **Desacoplamiento entre origen y procesamiento.**

A su vez, mantiene la simplicidad operativa al apoyarse en capacidades nativas de Redis, evitando la necesidad de mecanismos más complejos como logs de deduplicación persistentes o coordinadores distribuidos.

**Conclusión técnica**

El mecanismo de idempotencia implementado actúa como una capa de protección esencial en la comunicación asíncrona. Al combinar:

- Generación de claves únicas en el SDK
- Validación mediante middleware
- Persistencia efímera en Redis con TTL

El sistema logra garantizar que cada mensaje sea procesado **exactamente una vez desde el punto de vista lógico**, incluso en presencia de condiciones adversas propias de sistemas distribuidos

### 4.2.6 Uso de memoria persistente, comunicación asíncrona.

En el contexto de la comunicación asíncrona, el sistema incorpora una capa de memoria persistente basada en Redis como mecanismo intermedio para desacoplar productores y consumidores. Esta integración permite gestionar flujos de mensajes de forma eficiente, garantizando durabilidad temporal, orden y disponibilidad de los datos mientras son procesados.

El sistema interactúa con Redis a través de un cliente especializado encapsulado dentro de la capa de infraestructura, respetando los principios de la arquitectura limpia. Este cliente es responsable de abstraer los detalles de conexión, serialización y manejo de estructuras de datos, exponiendo interfaces alineadas con los casos de uso del dominio. En este escenario, Redis se utiliza principalmente mediante su estructura de **streams**, la cual está diseñada para modelar flujos de eventos de manera append-only.

Desde el punto de vista operativo, el flujo típico consiste en la publicación de mensajes por parte de un productor hacia un stream determinado, seguido por el consumo de estos mensajes a través de grupos de consumidores. Este patrón permite distribuir la carga de procesamiento, asegurar que cada mensaje sea procesado al menos una vez y facilitar la recuperación ante fallos mediante mecanismos como el _pending entries list_.

El uso de Redis como backbone para la comunicación asíncrona presenta varios beneficios clave:

- **Baja latencia**: al operar principalmente en memoria, Redis ofrece tiempos de acceso extremadamente bajos, lo que lo hace adecuado para sistemas que requieren alta capacidad de respuesta.
- **Modelo de streams robusto**: los streams permiten mantener un historial ordenado de eventos, con control preciso sobre offsets y consumo, similar a sistemas de mensajería más complejos.
- **Escalabilidad horizontal**: mediante particionamiento y clustering, Redis puede adaptarse a incrementos en la carga de mensajes sin degradar significativamente el rendimiento.
- **Manejo de consumidores**: la funcionalidad de _consumer groups_ facilita la distribución del trabajo y el procesamiento concurrente de mensajes.
- **Persistencia configurable**: aunque es un sistema en memoria, Redis permite configurar distintos niveles de persistencia (RDB, AOF), logrando un equilibrio entre rendimiento y durabilidad.

En conjunto, Redis actúa como un componente clave en la orquestación de la comunicación asíncrona, proporcionando una solución ligera pero potente para la gestión de eventos en sistemas distribuidos.

A continuación, se muestra un diagrama del esquema de comunicación que tiene el sistema al interactuar con Redis.

![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%206.png>)

_Figura 6. Diagrama de componentes_

![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%207.png>)

_Figura 7. Diagrama de comunicación_

### 4.2.7 Sistema de logs y telemetría

El sistema de observabilidad se implementa en la capa de infraestructura, desacoplado de la lógica de dominio y de aplicación, y orientado a proveer capacidades de trazabilidad, diagnóstico y monitoreo sin contaminar el flujo de negocio.

**Estrategia de Logging**

El módulo de logging está diseñado para ser utilizado exclusivamente en los puntos de entrada/salida del sistema:

- Controladores gRPC
- Middlewares
- Cliente (únicamente en escenarios de fallo dentro del flujo síncrono, como desconexiones)

Para el resto de las capas, se sigue una estrategia de propagación de errores:  
los errores se transmiten hacia arriba hasta el controlador correspondiente, donde se realiza la traducción a códigos gRPC adecuados. Esto garantiza que la lógica de dominio permanezca libre de preocupaciones de observabilidad.

El modulo de logs soporta 2 mecanismos de salida:

- **Salida por consola (actual)**  
    Implementación activa mediante feature flag, utilizada principalmente en entornos de desarrollo y pruebas.
- **Exportación a sistema externo (extensible)**  
    A través de un cliente desacoplado, permite enviar logs a un sistema centralizado (por ejemplo, un stack de observabilidad). Esta opción permanece desacoplada mediante configuración, facilitando su activación sin impacto en el resto del sistema.

Esta aproximación permite flexibilidad operativa sin introducir acoplamiento innecesario en capas superiores.

**Telemetría y Monitoreo**

Para la instrumentación del sistema, se adopta un enfoque basado en métricas y trazas, soportado por herramientas estándar del ecosistema.

En el entorno de pruebas —provisionado mediante Docker y Terraform— se despliega un stack compuesto por:

- Prometheus: recolección de métricas
- Grafana: visualización y análisis

La integración con Prometheus se realiza mediante un controlador HTTP en la capa de infraestructura, cuya única responsabilidad es exponer el endpoint de métricas. Este componente no participa en la lógica de negocio, manteniendo el principio de responsabilidad única.

El sistema utiliza OpenTelemetry como mecanismo de instrumentación, junto con su integración para Prometheus, lo que permite:

- Generación de métricas de desempeño
- Recolección de información de trazabilidad
- Observación del comportamiento del sistema bajo diferentes condiciones de carga

Esta instrumentación habilita la validación del sistema en entornos controlados, facilitando la detección de cuellos de botella, errores de integración y problemas de rendimiento.

**Estructura del Log**

El sistema define una estructura de log estandarizada, orientada a facilitar la trazabilidad y el diagnóstico de errores. Esta estructura se materializa como un objeto serializable en formato JSON, permitiendo su interoperabilidad con sistemas externos de observabilidad.

![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%208.png>)

_Figura 8. Estructura del Log_

Cada uno de sus campos cumple una responsabilidad específica:

- **ID**  
    Identificador único utilizado para el seguimiento y la trazabilidad de una comunicación. Permite correlacionar eventos dentro de un mismo flujo, especialmente útil en escenarios distribuidos.
- **Description**  
    Contiene el mensaje de error asociado al evento. Su propósito es proveer contexto claro y directo sobre la naturaleza del fallo.
- **Op**  
    Representa el nombre detallado del método u operación donde ocurrió el error. Este campo facilita la localización precisa del punto de fallo dentro del sistema.

Esta estructura uniforme permite mantener consistencia en la generación de logs, independientemente del mecanismo de salida configurado (consola o sistema externo), y simplifica su procesamiento posterior en herramientas de análisis y monitoreo.

## Evaluación

Texto

Esto no tiene nada que ver con la estructura, si no con el formato.

A continuación, se indica con un ejemplo cómo deben introducirse los títulos y las fuentes en Tablas y Figura. Nota que no se introducen del mismo modo en ambos tipos de recursos.

Ejemplo de nota al pie[[1]](#footnote-1).

Tabla 3. “Tablas” del menú de estilos

|   |   |   |   |
|---|---|---|---|
|||ESPAÑA|ARAGÓN|
|Alumnado con Necesidades Específicas de Apoyo Educativo|Alumnado con Necesidades Educativas Especiales|141.426|3.642<br><br>(2,58 %)|
|Alumnado con Altas Capacidades Intelectuales|6.834<br><br>(4,83 %)|97<br><br>(1,42 %)|

Adaptación de MECD, 2013

![TFM_v1](<Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/Attachments/TFM_v1%209.png>)

Figura 9. “Figuras” del menú de estilos. (Elaboración propia)

### “Título 3” del menú de estilos

### “Título 3” del menú de estilos

#### "Título 4" del menú de estilos

#### "Título 4" del menú de estilos

# Conclusiones y Trabajo Futuro

Este último bloque es habitual en todos los tipos de trabajos y presenta el resumen final de tu trabajo y debe servir para informar del alcance y relevancia de tu aportación.

## Conclusiones

Suele estructurarse empezando con un resumen del problema tratado, de cómo se ha abordado y de por qué la solución sería válida.

Es recomendable que incluya también un resumen de las contribuciones del trabajo, en el que relaciones las contribuciones y los resultados obtenidos con los objetivos que habías planteado para el trabajo, discutiendo hasta qué punto has conseguido resolver los objetivos planteados.

## Líneas de Trabajo Futuro

Finalmente, se suele dedicar una última sección a hablar de líneas de trabajo futuro que podrían aportar valor añadido al TFM realizado. La sección debería señalar las perspectivas de futuro que abre el trabajo desarrollado para el campo de estudio definido. En el fondo, debes justificar de qué modo puede emplearse la aportación que has desarrollado y en qué campos.

Referencias bibliográficas

2022 Benchmark Report. (2022). _Comparing Apache Pulsar vs. Apache Kafka._ Obtenido de https://streamnative.io/blog/apache-pulsar-vs-apache-kafka-2022-benchmark

Bonin, M. (2020). _Estándar de Arquitectura Hexagonal._ Sensedia Blog.

Bonin, M. (2020). _Estándar de Arquitectura Hexagonal._ Obtenido de https://www.sensedia.com.es/post/uso-del-patron-de-arquitectura-hexagonal#:~:text=,%28Alistair%20Cockburn

cbornet. (2022). _GitHub - cbornet/pulsar-grpc._ Obtenido de https://github.com/cbornet/pulsar-grpc

Datadog. (2025). _Monitorización de colas de Kafka_. Obtenido de https://docs.datadoghq.com/es/tracing/guide/monitor-kafka-queues/

Fowler, M. (2003). _Patterns of Enterprise Application Architecture._ Addison-Wesley.

Gilvan Ornelas & Bruno Fontana. (2024). _Clean Architecture with Spring Boot_. Obtenido de https://www.baeldung.com/spring-boot-clean-architecture#:~:text=In%20this%20article%2C%20we%E2%80%99ll%20create,cases%2C%20interface%20adapters%2C%20and%20frameworks%2Fdrivers

gRPC. (2024). _Core concepts, architecture and lifecycle_. Obtenido de https://grpc.io/docs/what-is-grpc/core-concepts/

hoop.dev. (2025). _What Redis gRPC Actually Does and When to Use It._ Obtenido de https://hoop.dev/blog/what-redis-grpc-actually-does-and-when-to-use-it/

Index. (2026). _RabbitMQ vs NATS vs Kafka: Message Broker Comparison 2026._ Obtenido de https://www.index.dev/skill-vs-skill/backend-kafka-vs-rabbitmq-vs-nats

jasontaylordev. (2026). _CleanArchitecture_. Obtenido de https://github.com/jasontaylordev/cleanarchitecture

Jayaraman, S. & Prasad, M. (2024). _Designing Hexagonal Architectures for Scalable Web Services._ Journal of Multidisciplinary Innovation and Research Methodology.

Jayaraman, S. (2024). _Designing Hexagonal Architectures for Scalable Web Services._ Obtenido de https://www.researchgate.net/publication/388385384_Designing_Hexagonal_Architectures_for_Scalable_Web_Services

Martin, R. C. (2017). _Clean Architecture: A Craftsman’s Guide to Software Structure and Design._ Prentice Hall.

melyouz. (2024). _gRPC based Message Broker written in Go for self learning purpose._ Obtenido de https://github.com/melyouz/risala

Microsoft Learn. (2026). _Comparación entre los servicios gRPC y las API HTTP._ Obtenido de https://learn.microsoft.com/es-es/aspnet/core/grpc/comparison?view=aspnetcore-10.0

Microsoft Learn. (2026). _Fan-out/fan-in scenarios in Durable Functions - Azure - Azure Durable._ Obtenido de https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-fan-in-fan-out

Microsoft Learn. (2026). _Message Queue Server transaccional - Win32 apps._ Obtenido de https://learn.microsoft.com/es-es/windows/win32/cossdk/transactional-message-queuing

muhammadharis. (2019). _My implementation of an AMQP Message Broker done in Go using gRPC and Redis Streams._ Obtenido de https://github.com/muhammadharis/AMQP-Message-Broker

Onidel Cloud. (2025). _Oniel_. Obtenido de https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks

Oruc, F., Goby, D., Kunce, D. & Ploski, M. (2022). _Construyendo arquitecturas hexagonales sobre AWS (Guía prescriptiva)._ Amazon Web Services.

Redis. (2026). _Message Broker Pattern for Microservices Interservice Communication_. Obtenido de https://redis.io/solutions/message-Broker-pattern-for-microservices-interservice-communication/

Redis. (2026). _Stream LLM Output to Browser in Real-Time with Redis Streams_. Obtenido de https://redis.io/tutorials/howtos/solutions/streams/streaming-llm-output/

sanj.dev. (2025). _NATS vs Apache Kafka vs RabbitMQ: Messaging Showdown_. Obtenido de https://sanj.dev/post/nats-kafka-rabbitmq-messaging-comparison

Stack Overflow. (2019). _.Net - gRPC Push and Fan-Out._ Obtenido de https://stackoverflow.com/questions/45107411/grpc-push-and-fan-out

Streamnative. (2022). _Apache Pulsar vs. Apache Kafka 2022 Benchmark._ Obtenido de https://streamnative.io/blog/apache-pulsar-vs-apache-kafka-2022-benchmark

Wikipedia. (2022). _Fan-out (software)_. Obtenido de https://en.wikipedia.org/wiki/Fan-out_(software)

zevolution. (2021). _netflix-hexagonal-architecture_. Obtenido de https://github.com/zevolution/netflix-hexagonal-architecture

1. Título Anexo

1. Ejemplo de nota al pie. [↑](#footnote-ref-1)