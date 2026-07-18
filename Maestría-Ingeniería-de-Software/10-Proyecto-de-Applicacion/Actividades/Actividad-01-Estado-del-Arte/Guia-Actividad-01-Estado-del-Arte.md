# Guia de trabajo para la Actividad 1

## 1. Objetivo real de esta actividad

La Actividad 1 no consiste en programar todavia el sistema. Consiste en dejar justificado, con base academica y tecnica, **que proyecto van a hacer, por que tiene sentido hacerlo, que tecnologias se relacionan con el problema y cual sera su aportacion concreta**.

La entrega debe cubrir cuatro bloques obligatorios:

1. Descripcion del desarrollo practico.
2. Lista de caracteristicas del sistema.
3. Estado del arte.
4. Conclusiones del estado del arte.

Ademas, debe incluir:

- Entre 5 y 8 paginas.
- Referencias en formato APA.
- Minimo 20 referencias.
- Todas las referencias deben estar citadas en el texto.

## 2. Que pide la rubrica

Para sacar la maxima nota, el documento debe demostrar esto:

- El proyecto esta definido con claridad, no solo nombrado.
- Las caracteristicas del sistema estan concretadas y delimitadas.
- El estado del arte tiene suficiente profundidad, al menos unas 4 paginas reales.
- Las conclusiones no resumen solamente: comparan, critican y justifican la propuesta.
- Las referencias son suficientes, actuales y mejor si mezclan articulos, documentacion oficial, libros y trabajos previos relevantes.

## 3. Que hace el proyecto base del TFM

La idea central del TFM base es valida y se puede conservar:

- Construir un **broker de mensajeria hibrido**.
- Usar **gRPC** como canal de comunicacion de baja latencia.
- Soportar **mensajeria sincrona en tiempo real** mediante streaming.
- Soportar **mensajeria asincrona** con almacenamiento temporal.
- Usar **Redis** como soporte intermedio para mensajes.
- Aplicar patrones **fan-in** y **fan-out**.
- Incluir control de **idempotencia** para evitar reprocesamiento.
- Diseñar el sistema con una arquitectura desacoplada, tipo hexagonal o limpia.

Dicho de forma simple, el proyecto busca resolver este problema:

> Como combinar comunicacion en tiempo real y mensajeria desacoplada en una sola solucion, sin depender de un broker tradicional pesado y manteniendo baja latencia, control del consumo y una arquitectura mantenible.

## 4. Que deben rehacer como trabajo nuevo

Aunque la idea general puede mantenerse, el trabajo debe rehacerse como propuesta propia. Eso implica:

- Redefinir el problema con sus propias palabras.
- Delimitar mejor el alcance del sistema.
- Reescribir por completo la descripcion del proyecto.
- Rehacer el estado del arte con busqueda actual y criterio propio.
- Corregir afirmaciones demasiado fuertes o poco justificadas.
- Replantear las conclusiones a partir de la evidencia que ustedes recopilen.
- Ajustar la propuesta para que tenga una aportacion concreta y medible.

Lo que si pueden reutilizar es la **linea conceptual**:

- Broker hibrido.
- gRPC.
- Redis Streams o almacenamiento intermedio similar.
- Patrones de mensajeria.
- Idempotencia.
- Arquitectura desacoplada.

Lo que **no** conviene reutilizar tal cual:

- La redaccion.
- La estructura exacta del analisis.
- Frases de justificacion ya hechas.
- Comparativas no verificadas.
- Referencias debiles o de baja calidad como base del trabajo.

## 5. Problemas que se ven en el TFM base y que ustedes deben corregir

Del documento base salen varias alertas utiles:

- Hay secciones de plantilla sin terminar o sin limpiar.
- Algunas afirmaciones tecnicas parecen mas de blog o benchmark comercial que de fuente academica fuerte.
- Aparecen referencias que la propia consigna recomienda evitar, como Wikipedia.
- Hay mezcla de fuentes oficiales, blogs, GitHub y ejemplos comunitarios; eso sirve como apoyo, pero no debe dominar el estado del arte.
- En algunos tramos se anticipa demasiado la solucion, cuando en la Actividad 1 primero hay que justificarla.

Esto no invalida la idea del proyecto. Solo significa que ustedes deben presentar una version mas rigurosa.

## 6. Enfoque recomendado para su proyecto nuevo

Mi recomendacion es que no lo presenten solo como "otro broker", sino como una propuesta mas concreta:

**Titulo de trabajo sugerido**

Diseno y justificacion de un broker de mensajeria hibrido basado en gRPC y Redis para comunicacion en tiempo real y procesamiento asincrono controlado.

**3 propuestas de titulo mas cortas**

1. Broker hibrido con gRPC y Redis.
2. Broker de mensajeria en tiempo real con gRPC.
3. Arquitectura de broker hibrido para sistemas distribuidos.

**Aportacion que si se puede defender**

- Integrar en una misma propuesta dos modos de comunicacion:
  - streaming en tiempo real;
  - consumo asincrono pull-based.
- Reducir acoplamiento entre productores y consumidores.
- Introducir idempotencia desde el diseno.
- Evaluar si una arquitectura limpia/hexagonal mejora mantenibilidad y testabilidad.

No prometan desde la Actividad 1 cosas demasiado grandes como reemplazar Kafka, competir con brokers industriales o garantizar exactamente-once absoluto en todo contexto distribuido. Eso los expone innecesariamente.

## 7. Estructura recomendada del documento de la Actividad 1

Pueden construir la entrega con esta estructura:

### 7.1 Introduccion breve

- Presentar el problema general.
- Explicar por que hoy importa la comunicacion en tiempo real en sistemas distribuidos.
- Introducir la necesidad de combinar baja latencia, desacoplamiento y control de mensajes.

### 7.2 Descripcion del desarrollo practico

Aqui deben responder:

- Que van a construir.
- Para que sirve.
- Que problema resuelve.
- En que contexto se usaria.
- Cual sera el alcance de esta version del sistema.

Ejemplo de enfoque:

"Se propone el diseño de un broker de mensajeria hibrido que permita a servicios distribuidos intercambiar eventos en tiempo real mediante gRPC y gestionar mensajes asincronos mediante un mecanismo de persistencia temporal y consumo pull."

### 7.3 Caracteristicas del sistema

Redacten una lista cerrada, concreta y defendible. Por ejemplo:

- Publicacion de mensajes por productores.
- Suscripcion de consumidores a eventos en tiempo real.
- Streaming bidireccional o server streaming sobre gRPC.
- Almacenamiento temporal de mensajes asincronos.
- Recuperacion de mensajes por consumo pull.
- Mecanismo de acknowledgement.
- Idempotencia para evitar reprocesamiento.
- Observabilidad basica: logs, metricas y trazabilidad.
- Arquitectura desacoplada para facilitar pruebas y evolucion.

### 7.4 Estado del arte

Aqui no basta con enumerar tecnologias. Tienen que organizar el analisis por temas.

Subtemas recomendados:

1. Arquitecturas orientadas a eventos y sistemas distribuidos.
2. gRPC como mecanismo de comunicacion de alto rendimiento.
3. Brokers de mensajeria relevantes: Kafka, RabbitMQ, NATS, Pulsar, Redis Streams.
4. Patrones fan-in y fan-out.
5. Modelos de entrega: push, pull, at-least-once, idempotencia.
6. Redis como almacenamiento intermedio o base para colas/streams.
7. Arquitectura hexagonal o limpia para este tipo de sistema.
8. Trabajos relacionados o implementaciones previas similares.

En cada subtema respondan siempre:

- Que existe hoy.
- Que ventajas ofrece.
- Que limitaciones tiene.
- Que hueco deja abierto para su propuesta.

### 7.5 Conclusiones del estado del arte

Esta parte debe cerrar el razonamiento:

- Que tecnologias son mas adecuadas y por que.
- Que limitaciones tienen las soluciones actuales.
- Que decisiones de diseno justifican para su proyecto.
- Cual sera la aportacion diferenciadora de su propuesta.

La conclusion no debe decir "gRPC y Redis son buenos". Debe decir algo como:

"El analisis muestra que gRPC es adecuado para canales persistentes y baja latencia, mientras Redis Streams permite desacoplar temporalmente productores y consumidores con coste operativo moderado. Sin embargo, las soluciones revisadas no resuelven por si solas la integracion coherente entre comunicacion en tiempo real, consumo pull e idempotencia aplicada desde el diseno. Por ello se justifica el desarrollo de una propuesta hibrida con alcance academico y validacion experimental."

## 8. Plan paso a paso para hacer la actividad

### Paso 1. Fijar el alcance exacto

Antes de escribir, definan estas 6 decisiones:

- Lenguaje principal del prototipo.
- Si el almacenamiento asincrono sera Redis Streams.
- Si el sistema tendra SDK o no.
- Si el enfoque sera solo academico/prototipo o casi productivo.
- Que patrones soportara en la primera version.
- Que van a medir despues en fases futuras: latencia, throughput, resiliencia, mantenibilidad.

Si no fijan esto, el documento se vuelve ambiguo.

### Paso 2. Escribir una definicion corta del proyecto

Redacten un parrafo de 5 a 8 lineas con:

- problema;
- propuesta;
- tecnologias base;
- valor esperado.

Ese parrafo sera la base de casi todo el documento.

### Paso 3. Convertir la idea en caracteristicas

Saquen una lista de 8 a 12 caracteristicas maximo.

No mezclen aqui cosas de implementacion muy detalladas. Deben ser capacidades del sistema, no trozos de codigo.

### Paso 4. Preparar la matriz de investigacion

Antes de redactar el estado del arte, hagan una tabla de apoyo con columnas como:

- Tema.
- Fuente.
- Tipo de fuente.
- Idea clave.
- Ventaja.
- Limitacion.
- Como aporta a nuestro proyecto.

Esto les ayudara a no copiar ni improvisar.

### Paso 5. Buscar y clasificar al menos 20 fuentes

Distribucion recomendada:

- 5 a 7 fuentes academicas.
- 4 a 6 fuentes oficiales de tecnologia.
- 3 a 5 trabajos o implementaciones relacionadas.
- 2 a 4 libros, guias tecnicas o whitepapers serios.

Prioridad de calidad:

1. Articulos academicos y libros.
2. Documentacion oficial.
3. Whitepapers y guias tecnicas serias.
4. Repositorios o blogs tecnicos solo como apoyo.

Eviten que el cuerpo principal dependa de Wikipedia, Stack Overflow o blogs comparativos sin metodologia clara.

### Paso 6. Redactar el estado del arte por comparacion, no por definicion

Error comun:

- "Kafka es..."
- "RabbitMQ es..."
- "Redis es..."

Mejor enfoque:

- "Kafka prioriza throughput y durabilidad, pero introduce mayor complejidad operativa."
- "RabbitMQ ofrece enrutamiento flexible, aunque no esta orientado nativamente a streaming de baja latencia."
- "Redis Streams reduce friccion de despliegue, pero no sustituye por completo a plataformas especializadas."

Asi si hay analisis.

### Paso 7. Cerrar con una justificacion de su propuesta

La Actividad 1 debe terminar dejando claro esto:

- Por que este proyecto merece hacerse.
- Que vacio cubre.
- Por que la combinacion tecnologica elegida tiene sentido.
- Que aportacion propia van a desarrollar.

### Paso 8. Revisar la coherencia completa

Comprueben que:

- Cada caracteristica del sistema aparece luego sustentada en el estado del arte.
- Cada conclusion sale de algo ya analizado antes.
- Cada referencia citada aparece en la bibliografia.
- Cada referencia de la bibliografia fue citada en el texto.

## 9. Lista de preguntas que ustedes deben poder contestar

Si no pueden responder estas preguntas, todavia no esta madura la actividad:

- Que problema concreto resuelve el broker propuesto?
- Por que gRPC y no REST para el canal principal?
- Por que Redis y no solo memoria local?
- Que diferencia habra entre el modo sincrono y el asincrono?
- Que significa consumo pull en su propuesta?
- Que problema ataca la idempotencia?
- Que aporta una arquitectura limpia o hexagonal en este caso?
- Contra que alternativas van a justificar su decision?
- Cual es la novedad o aporte academico de su trabajo?

## 10. Propuesta de reparto de trabajo para 5 personas

Si el proyecto sera entre 5 personas, este reparto les da mas orden y reduce duplicidad:

**Persona 1. Coordinacion y planteamiento**

- Definicion del problema.
- Redaccion de la descripcion del desarrollo practico.
- Control del alcance del documento.
- Integracion final de todas las secciones.

**Persona 2. gRPC y comunicacion en tiempo real**

- Investigacion sobre gRPC, HTTP/2, Protobuf y streaming.
- Ventajas y limites frente a REST o HTTP API.
- Redaccion del bloque de comunicacion sincrona o tiempo real.

**Persona 3. Brokers y patrones de mensajeria**

- Investigacion sobre Kafka, RabbitMQ, NATS y Pulsar.
- Analisis de patrones fan-in, fan-out, pub/sub y pull.
- Tabla comparativa de soluciones.

**Persona 4. Redis, idempotencia y mensajeria asincrona**

- Investigacion sobre Redis Streams, consumer groups y acknowledgements.
- Analisis del modelo pull y del control de duplicados.
- Redaccion del bloque de persistencia temporal e idempotencia.

**Persona 5. Arquitectura, referencias y calidad academica**

- Investigacion sobre arquitectura hexagonal y clean architecture.
- Revision de formato APA.
- Verificacion de citas dentro del texto.
- Revision de coherencia academica y redaccion final.

**Cierre conjunto**

- Unificar tono y estilo.
- Eliminar repeticiones entre secciones.
- Verificar que toda conclusion salga de evidencia ya citada.
- Confirmar que el documento final parezca escrito como una sola propuesta.

## 11. Estructura minima de paginas recomendada

Para entrar bien en 5 a 8 paginas:

- 0.5 pagina: introduccion.
- 0.5 a 1 pagina: descripcion del desarrollo practico y caracteristicas.
- 4 a 5 paginas: estado del arte.
- 1 pagina: conclusiones del estado del arte.
- referencias aparte, segun formato de entrega.

## 12. Checklist final antes de entregar

- El proyecto esta descrito en un parrafo claro y propio.
- Hay lista concreta de caracteristicas.
- El estado del arte compara, no solo define.
- Hay minimo 20 referencias.
- No dependen de Wikipedia como fuente central.
- Todas las referencias estan citadas.
- Las conclusiones justifican el proyecto.
- No hay secciones plantilla, texto de relleno ni titulos falsos.
- El documento se siente nuevo, coherente y defendible.

## 13. Lista inicial de investigacion: fuentes y ligas recomendadas

La siguiente lista esta pensada como base de trabajo para la Actividad 1. No significa que deban citar todo, sino que desde aqui pueden seleccionar las fuentes mas utiles y construir su bibliografia final.

### 13.1 Fuentes oficiales sobre gRPC

1. gRPC Core concepts, architecture and lifecycle  
   https://grpc.io/docs/what-is-grpc/core-concepts/
2. gRPC Performance Best Practices  
   https://grpc.io/docs/guides/performance/
3. Microsoft Learn: Comparacion entre gRPC y HTTP API  
   https://learn.microsoft.com/es-es/aspnet/core/grpc/comparison?view=aspnetcore-10.0

### 13.2 Fuentes oficiales sobre Redis y Redis Streams

4. Redis Streams como caso de uso de streaming  
   https://redis.io/docs/latest/develop/use-cases/streaming/
5. Redis XREADGROUP  
   https://redis.io/docs/latest/commands/xreadgroup/
6. Redis Pub/Sub  
   https://redis.io/docs/latest/develop/pubsub/
7. Redis Message Broker Pattern for Microservices  
   https://redis.io/solutions/message-broker-pattern-for-microservices-interservice-communication/

### 13.3 Fuentes oficiales sobre Kafka

8. Apache Kafka Introduction  
   https://kafka.apache.org/documentation/
9. Kafka Streams Core Concepts y exactly-once  
   https://kafka.apache.org/10/streams/core-concepts/

### 13.4 Fuentes oficiales sobre RabbitMQ

10. RabbitMQ AMQP Concepts  
    https://www.rabbitmq.com/tutorials/amqp-concepts
11. RabbitMQ Tutorials  
    https://www.rabbitmq.com/tutorials
12. RabbitMQ Exchanges  
    https://www.rabbitmq.com/docs/next/exchanges

### 13.5 Fuentes oficiales sobre NATS y JetStream

13. NATS Overview  
    https://docs.nats.io/nats-concepts/overview
14. What is NATS  
    https://docs.nats.io/nats-concepts/what-is-nats
15. JetStream  
    https://docs.nats.io/nats-concepts/jetstream
16. JetStream Consumers  
    https://docs.nats.io/nats-concepts/jetstream/consumers

### 13.6 Fuentes oficiales sobre Pulsar

17. Apache Pulsar Overview  
    https://pulsar.apache.org/
18. Pulsar Architecture Overview  
    https://pulsar.apache.org/docs/next/concepts-architecture-overview/
19. Pulsar Messaging Concepts  
    https://pulsar.apache.org/docs/2.3.0/concepts-messaging/

### 13.7 Fuentes sobre arquitectura de software

20. Alistair Cockburn: Hexagonal Architecture, articulo original  
    https://alistair.cockburn.us/hexagonal-architecture
21. Robert C. Martin: The Clean Architecture Dependency Rule  
    https://www.informit.com/articles/article.aspx?p=2832399
22. Clean Architecture, referencia editorial del libro  
    https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494319

### 13.8 Fuentes sobre observabilidad

23. OpenTelemetry Signals  
    https://opentelemetry.io/docs/concepts/signals/
24. Prometheus Overview  
    https://prometheus.io/docs/introduction/overview/
25. Grafana Dashboards Overview  
    https://grafana.com/docs/grafana/latest/dashboards/

### 13.9 Fuentes academicas o tecnicas complementarias

26. Implementing Cross-Platform Business Logic in Mobile Applications using Hexagonal Architecture  
    https://www.researchgate.net/publication/370682044_Implementing_Cross-Platform_Business_Logic_in_Mobile_Applications_using_Hexagonal_Architecture
27. Hexagonal-Driven Development  
    https://www.researchgate.net/publication/345808730_Hexagonal-Driven_Development
28. A Brief Introduction to Redis  
    https://arxiv.org/pdf/2203.06559

### 13.10 Como usar esta lista

- Usen primero las fuentes oficiales para definir conceptos.
- Usen las fuentes academicas para reforzar argumentacion y lenguaje de investigacion.
- Si una fuente es muy comercial, usenla como apoyo tecnico, no como justificacion principal.
- Para la bibliografia final, conviene equilibrar documentacion oficial, articulos tecnicos y referencias academicas.

## 14. Recomendacion practica final

La mejor forma de hacerlo bien no es "copiar y mejorar" el TFM base, sino usarlo como **mapa conceptual**.

Usen del TFM base solo estas tres cosas:

- la idea del problema;
- la familia de tecnologias;
- la direccion de la solucion.

Rehagan desde cero estas cuatro:

- el planteamiento;
- la argumentacion;
- el estado del arte;
- las conclusiones.

Si trabajan asi, el resultado sera nuevo, consistente y mucho mas facil de defender en el TFM completo.
