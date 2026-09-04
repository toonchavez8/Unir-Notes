# Guion para la defensa de Dominus Broker

Duración total prevista: 25 minutos  
Participantes: 5  
Tiempo por participante: 5 minutos, incluida la transición

## Escaleta y asignación

| Bloque |      Tiempo | Tema principal                                            | Diapositivas | Responsable          |
| ------ | ----------: | --------------------------------------------------------- | -----------: | -------------------- |
| 1      |   0:00-5:00 | Problema, propósito, objetivos y alcance                  |          1-4 | ____________________ |
| 2      |  5:00-10:00 | Decisiones tecnológicas, propuesta híbrida y arquitectura |          5-7 | ____________________ |
| 3      | 10:00-15:00 | Metodología experimental e iterativa                      |         8-14 | Maikel               |
| 4      | 15:00-20:00 | Implementación, pruebas, usabilidad y ciberseguridad      |        15-17 | ____________________ |
| 5      | 20:00-25:00 | Rendimiento, conclusiones, limitaciones y trabajo futuro  |        18-20 | ____________________ |


## Idea central de la defensa

Dominus Broker es un prototipo académico que combina dos formas de comunicación entre servicios: entrega inmediata mediante streaming gRPC y mensajería asíncrona mediante Redis Streams. El trabajo demuestra que la combinación es técnicamente viable dentro de los escenarios evaluados, pero también identifica problemas que deben resolverse antes de pensar en un uso productivo.

## Bloque 1. Problema, propósito y alcance

Responsable: ____________________  
Tiempo: 5 minutos  
Diapositivas: 1 a 4

### Guion hablado

Buenos días. Somos Maikel Barrios, Daniel Campos, Miguel Chávez, Fernando García y César Sánchez. Nuestro trabajo se titula "Diseño e implementación de Dominus Broker: broker de mensajería en tiempo real basado en gRPC y Redis Streams".

El punto de partida fue un problema frecuente en los sistemas distribuidos. Hay aplicaciones que necesitan entregar eventos casi de inmediato, por ejemplo una notificación, una actualización de estado o una respuesta que se transmite de forma continua. Al mismo tiempo, hay procesos que no pueden depender de que el consumidor esté conectado en ese instante. En esos casos se necesita conservar el mensaje, permitir que el consumidor lo solicite a su propio ritmo y confirmar después que fue procesado.

Normalmente estas necesidades se resuelven con herramientas distintas. gRPC funciona bien para conexiones persistentes y streaming entre servicios. Los brokers tradicionales ofrecen colas, persistencia y desacoplamiento. El problema aparece cuando un sistema requiere ambos comportamientos y, además, debe controlar los mensajes duplicados que surgen por reintentos, pérdidas de respuesta o fallos parciales.

A partir de esa situación formulamos el propósito del trabajo: diseñar, implementar y evaluar un prototipo que reuniera comunicación en tiempo real, mensajería asíncrona con confirmación y un control de idempotencia. A ese prototipo lo llamamos Dominus Broker.

El objetivo general fue analizar la viabilidad técnica del enfoque y observar su comportamiento en escenarios representativos. Para ello planteamos objetivos concretos: comparar alternativas de mensajería, definir requisitos, diseñar una arquitectura desacoplada, implementar los dos flujos de comunicación y validar el resultado mediante pruebas funcionales, de integración, seguridad y rendimiento.

Conviene aclarar el alcance desde el principio. Dominus no intenta competir con Kafka, Pulsar, RabbitMQ o NATS como plataforma completa. Es un desarrollo práctico y acotado. Queríamos comprobar si era posible integrar, bajo un mismo contrato, un canal de baja latencia y un canal asíncrono sencillo, sin introducir una infraestructura demasiado grande para el objetivo académico.

El sistema debía permitir que varios productores publicaran mensajes, distribuir eventos a uno o más suscriptores, consumir mensajes mediante un modelo pull y confirmar el procesamiento con un ACK. También debía ofrecer un SDK, contratos tipados con Protocol Buffers, autenticación por token, soporte TLS y observabilidad básica con logs, métricas y endpoints de salud.

Hay una decisión conceptual importante. El flujo asíncrono adopta una semántica de entrega al menos una vez. Esto significa que un mensaje puede volver a aparecer después de un reintento. La idempotencia reduce el riesgo de procesarlo dos veces dentro del broker, pero no permite afirmar que cualquier efecto externo se ejecute exactamente una vez. Esa distinción será importante cuando comentemos las pruebas de seguridad.

En resumen, la pregunta que guía el trabajo es la siguiente: ¿puede un broker híbrido, construido con gRPC y Redis Streams, ofrecer una base funcional para comunicación inmediata y asíncrona, con buen rendimiento y una arquitectura que sea posible probar y extender?

Para explicar cómo respondimos esa pregunta, cedo la palabra a ____________________, quien presentará las decisiones tecnológicas y la arquitectura de la solución.

### Control de tiempo

- 0:00-0:35. Presentación del equipo y del tema.
- 0:35-1:55. Problema de comunicación inmediata y asíncrona.
- 1:55-3:15. Objetivo general y objetivos específicos.
- 3:15-4:35. Alcance, capacidades previstas y precisión sobre idempotencia.
- 4:35-5:00. Pregunta guía y transición.

## Bloque 2. Decisiones tecnológicas y arquitectura

Responsable: ____________________  
Tiempo: 5 minutos  
Diapositivas: 5 a 7

### Guion hablado

Para definir la solución revisamos varias alternativas. REST es sencillo y ampliamente conocido, pero su modelo de solicitud y respuesta no es el más adecuado para flujos continuos. Kafka y Pulsar tienen capacidades maduras de streaming y persistencia, aunque implican una complejidad operativa mayor que la necesaria para este prototipo. RabbitMQ resuelve muy bien el enrutamiento y las colas, mientras que NATS JetStream ofrece mensajería ligera y consumidores pull.

La elección final no buscó declarar una tecnología ganadora. Elegimos la combinación que mejor respondía al alcance del proyecto. gRPC aporta contratos tipados mediante Protocol Buffers, comunicación sobre HTTP/2 y soporte nativo para streaming de cliente, de servidor y bidireccional. Redis Streams aporta almacenamiento temporal, grupos de consumidores y las operaciones necesarias para publicar, leer y confirmar mensajes.

Dominus se implementó en Go por su manejo de concurrencia y por su buen soporte para gRPC. También se desarrolló un SDK para que productores y consumidores no tuvieran que resolver directamente la conexión, los metadatos y la serialización en cada integración.

La propuesta tiene dos recorridos principales. En el primero, orientado al tiempo real, el productor abre un stream gRPC con BrokerAPI. El broker recibe los mensajes, identifica a los suscriptores y distribuye el mismo contenido hacia uno o varios destinos. Este flujo admite patrones como fan-in, fan-out y broadcast. La conexión permanece abierta mientras existe intercambio de mensajes y no utiliza Redis como memoria intermedia.

En el segundo recorrido, orientado al trabajo asíncrono, el productor llama a SqsAPI y ejecuta la operación Producer. El broker valida el mensaje y lo agrega a Redis Streams mediante XADD. Cuando un consumidor tiene capacidad, solicita un mensaje con Consumer; internamente se utiliza un grupo de consumidores y XREADGROUP. Después de completar el trabajo, el consumidor envía Ack y el broker confirma el mensaje mediante XACK. Si no llega la confirmación, el mensaje permanece pendiente para una posible recuperación posterior.

La idempotencia se planteó mediante una clave única por operación. Esa clave se conserva en Redis durante un tiempo configurable. La reserva debe realizarse de manera atómica con una operación equivalente a SET NX y TTL: si la clave no existe, la solicitud puede continuar; si ya existe, se identifica como repetida. Más adelante veremos que la evaluación de seguridad encontró una separación entre la comprobación y el guardado que rompe esta propiedad bajo concurrencia. Ese hallazgo no invalida el diseño, pero sí demuestra que la implementación necesita corregirse.

La arquitectura sigue el patrón de puertos y adaptadores. En el exterior están los clientes y el SDK. Después aparece la capa de entrada gRPC con BrokerAPI y SqsAPI. La capa de aplicación coordina los casos de uso. El dominio contiene los mensajes y los contratos internos. Finalmente, la infraestructura implementa Redis, las conexiones gRPC salientes, la autenticación, TLS, logs, métricas y health checks.

Esta separación tiene una ventaja práctica: los casos de uso no dependen directamente de Redis ni de una librería de transporte. Por eso pueden probarse con implementaciones simuladas y, si fuera necesario, Redis podría sustituirse sin reescribir la lógica central.

Hasta aquí hemos explicado qué construimos y por qué elegimos estas tecnologías. A continuación, ____________________ presentará la metodología utilizada para convertir la propuesta en un prototipo y evaluar su comportamiento.

### Control de tiempo

- 0:00-1:10. Comparación de alternativas y selección tecnológica.
- 1:10-2:25. Flujo en tiempo real.
- 2:25-3:35. Flujo asíncrono y ACK.
- 3:35-4:15. Idempotencia.
- 4:15-5:00. Arquitectura y transición.

## Bloque 3. Metodología experimental e iterativa

Responsable: ____________________  
Tiempo: 5 minutos  
Diapositivas: 8 a 14  
Fuente del bloque: `metodologia_broker_mensajeria_5min.pptx`

### Guion hablado

La metodología fue experimental, iterativa e incremental. No partimos de un diseño cerrado para implementarlo de una sola vez. Trabajamos en ciclos de análisis, diseño, implementación, experimentación y evaluación. Esto permitió ajustar decisiones a partir de lo que observábamos en el prototipo.

Primero analizamos el problema. Identificamos cuatro puntos que debían comprobarse en la práctica: la latencia de los flujos interactivos, la necesidad de comunicación persistente y bidireccional, el riesgo de reprocesar mensajes y la dificultad de distribuir un evento a varios consumidores. De este análisis salió la necesidad concreta: combinar comunicación bidireccional con una arquitectura orientada a eventos.

Después diseñamos la solución híbrida. gRPC se reservó para las operaciones unary y los distintos tipos de streaming. Redis y la memoria temporal se utilizaron para el flujo asíncrono. Sobre estos mecanismos se plantearon los patrones fan-in, fan-out y broadcast, junto con el control de idempotencia, el TTL y la recuperación de mensajes.

La implementación avanzó por componentes. Primero se definieron los contratos con Protocol Buffers. Después se construyeron BrokerAPI y SqsAPI, los casos de uso, los adaptadores de Redis, el SDK y los elementos de observabilidad. Cada avance se acompañó con pruebas para evitar que los problemas aparecieran únicamente al final.

La experimentación se dividió en dos escenarios. El síncrono evaluó streaming, conexiones abiertas y distribución hacia varios suscriptores. El asíncrono evaluó la publicación y recuperación de mensajes a través de Redis. Dentro de estos escenarios probamos broadcast, múltiples productores, varios consumidores y el comportamiento de consumidores que procesan a ritmos diferentes. Para aplicar carga se utilizó ghz con configuraciones en archivos YAML, y las métricas se observaron en Grafana. Redis también se inspeccionó directamente para comprobar el estado del grupo de consumidores y los mensajes pendientes.

La evaluación se apoyó en cinco tipos de medida. La latencia indicó el tiempo entre emisión y entrega. El throughput mostró cuántos mensajes se procesaron por unidad de tiempo. La consistencia se revisó mediante los flujos de consumo y confirmación. La tasa de duplicados permitió observar los reintentos. Finalmente, las pruebas de idempotencia comprobaron si una misma clave podía ejecutar más de una vez la operación.

También realizamos una comparación crítica con la mensajería tradicional. El prototipo tiene ventajas para aplicaciones interactivas: streaming y broadcast forman parte del canal principal, la comunicación es bidireccional y Redis permite agregar un flujo pull con memoria temporal. Sin embargo, Redis añade una dependencia operativa y la solución no sustituye todos los casos cubiertos por brokers consolidados. La primera versión tampoco incluye replicación, un orden global ni persistencia automática para los mensajes del canal en tiempo real.

Los campos de aplicación considerados fueron notificaciones y eventos en tiempo real, monitorización de procesos sensibles a la latencia, IoT, sistemas industriales, banca digital y comunicación con servicios de inteligencia artificial. No afirmamos que el prototipo esté listo para todos esos entornos. Son escenarios en los que el modelo podría estudiarse después de reforzar la seguridad, la recuperación y las pruebas de larga duración.

La función de esta metodología fue conectar tres cosas: el problema planteado, las decisiones de diseño y la evidencia obtenida. Ahora ____________________ explicará qué se implementó y qué aprendimos de las pruebas funcionales, de usabilidad y de seguridad.

### Control de tiempo por diapositiva del bloque

- Diapositiva 8, metodología general: 0:00-0:35.
- Diapositiva 9, análisis del problema: 0:35-1:10.
- Diapositiva 10, diseño de la solución: 1:10-2:00.
- Diapositiva 11, experimentación: 2:00-3:00.
- Diapositiva 12, métricas: 3:00-3:35.
- Diapositiva 13, comparación y limitaciones: 3:35-4:25.
- Diapositiva 14, campos de aplicación y transición: 4:25-5:00.

## Bloque 4. Implementación, pruebas y ciberseguridad

Responsable: ____________________  
Tiempo: 5 minutos  
Diapositivas: 15 a 17

### Guion hablado

La implementación dio como resultado un broker funcional compuesto por el servidor en Go, los contratos Protobuf, los servicios gRPC, el adaptador de Redis Streams y un SDK para los clientes. Los casos de uso principales fueron Producer, Consumer y Ack para el flujo asíncrono, además de streaming de cliente, de servidor y bidireccional para el canal en tiempo real.

La primera validación fue unitaria. Se ejecutaron 143 pruebas y subpruebas con el paquete testing de Go. Todas terminaron en PASS. La cobertura global instrumentada fue de 91.8 % sobre sentencias, y los casos de uso principales de ambos flujos alcanzaron 100 % de cobertura. Estas pruebas comprobaron, entre otras cosas, el rechazo de payloads vacíos, la recuperación de mensajes, la validación de identificadores y la distribución mediante streaming.

Después ejecutamos tres pruebas de integración. La primera comprobó que un mensaje enviado por gRPC atravesara Producer y quedara registrado en Redis Streams. La segunda recorrió el ciclo completo de producir, consumir y confirmar; después del ACK, el identificador dejó de aparecer como pendiente. La tercera validó el streaming bidireccional con dos suscriptores: se enviaron dos mensajes y se recibieron las cuatro respuestas esperadas. Las tres pruebas finalizaron en PASS.

La usabilidad se evaluó desde la perspectiva de un usuario técnico, porque Dominus no tiene una interfaz gráfica. Revisamos si un desarrollador podía preparar el entorno, localizar los módulos, interpretar los contratos, ejecutar las pruebas y entender el flujo Producer, Consumer y Ack. El resultado fue adecuado para un prototipo académico. La organización y las pruebas ayudan a aprender el sistema, aunque Go, gRPC y Redis Streams elevan la curva inicial. Por eso el SDK, los ejemplos y las guías de diagnóstico todavía deben mejorar.

El análisis de ciberseguridad aportó los resultados más incómodos, pero también los más útiles. Se revisaron cerca de quince puntos y el documento detalla cinco hallazgos.

El primero está en la autenticación gRPC. Una solicitud sin el encabezado `x-api-key` provoca un acceso fuera de rango y detiene el proceso. Un token incorrecto sí devuelve `Unauthenticated`, pero la ausencia del token afecta la disponibilidad. La corrección es validar que el arreglo tenga elementos antes de leer la primera posición, tanto en llamadas unary como en streaming.

El segundo hallazgo afecta la idempotencia bajo concurrencia. Se enviaron veinte solicitudes simultáneas con la misma clave. Lo esperado era una aceptación y diecinueve duplicados. Sin embargo, según la ronda, se aceptaron entre 3 y 20 solicitudes. La causa es que la comprobación y el guardado se realizan por separado, y el guardado ocurre de forma asíncrona. La solución es usar una sola reserva atómica en Redis y tomar su resultado como decisión.

En el SDK, la validación criptográfica de TLS funciona: una CA o un nombre de servidor incorrectos se rechazan. El problema es que esos errores se comunican mediante `panic` en lugar de devolverse al consumidor del SDK. También se encontró una validación deficiente de destinos, sin una allowlist separada, y un error de serialización JSON que se ignora, lo que puede enviar un payload vacío.

Estos resultados permiten una lectura equilibrada. Los flujos principales funcionan y están bien cubiertos, pero cobertura y pruebas exitosas no equivalen a seguridad ni a preparación productiva. La evaluación encontró deuda técnica concreta y propuso correcciones verificables.

Para cerrar, ____________________ presentará los resultados de carga, las limitaciones de la evidencia y las conclusiones del trabajo.

### Control de tiempo

- 0:00-0:55. Componentes implementados.
- 0:55-2:10. Pruebas unitarias y de integración.
- 2:10-2:50. Usabilidad técnica.
- 2:50-4:40. Hallazgos de ciberseguridad.
- 4:40-5:00. Lectura del resultado y transición.

## Bloque 5. Rendimiento, conclusiones y trabajo futuro

Responsable: ____________________  
Tiempo: 5 minutos  
Diapositivas: 18 a 20

### Guion hablado

La última parte de la evaluación observó el comportamiento del broker bajo carga. Utilizamos ghz y definimos dos escenarios. El primero ejercitó `BidirectionalStream` con carga progresiva, una concurrencia de 20 a 1,000, tres suscriptores y una ventana de cinco minutos. El segundo ejercitó el productor asíncrono respaldado por Redis. Las métricas se registraron en Grafana y el estado de los consumidores se comprobó directamente en Redis.

Durante la ventana analizada, la métrica `Handled per second sum` se movió aproximadamente entre 200,000 y 260,000 mensajes por segundo. El percentil P99 de latencia permaneció alrededor de 10 milisegundos. La CPU aumentó aproximadamente de 1 % a 4 %, la memoria pasó de 36 % a 42 % y la disponibilidad observada se mantuvo cerca del 100 %. En Redis se registraron tres consumidores y un valor `Pending` igual a cero en el momento de la captura.

Estos datos respaldan la viabilidad del prototipo en el escenario probado, pero debemos interpretarlos con cuidado. La métrica de throughput puede agregar más de una fuente de carga, por lo que no podemos atribuir los 200,000 a 260,000 mensajes por segundo a un único flujo. Las capturas cubren ventanas concretas y no describen el comportamiento durante horas o días. Tampoco se realizaron pruebas completas de recuperación, pérdida de consumidores, inyección de fallos o detección de fugas de memoria.

El resultado de disponibilidad cercana al 100 % tampoco es un acuerdo de nivel de servicio. Solo describe la ejecución observada. Del mismo modo, `Pending = 0` confirma que no había backlog en la captura, pero no demuestra por sí solo que el sistema pueda recuperarse de cualquier fallo.

Con estas precauciones, podemos responder la pregunta inicial. Sí fue posible construir un broker híbrido que integra streaming gRPC y mensajería asíncrona con Redis Streams. Los flujos Producer, Consumer, Ack y streaming bidireccional funcionaron en las pruebas. La arquitectura de puertos y adaptadores permitió separar la lógica central de la infraestructura, y el SDK redujo parte de la complejidad de integración.

También quedó claro qué falta. La prioridad es hacer atómica la reserva de idempotencia y evitar que una solicitud sin token detenga el servicio. Después deben corregirse el manejo de errores del SDK, la validación y autorización de destinos y la serialización. En la capa operativa se requieren pruebas de larga duración, fallos controlados, más productores y consumidores, distintos tamaños de payload y métricas separadas por flujo.

Otras líneas de trabajo son recuperar y reasignar mensajes pendientes, reforzar TLS y la gestión de credenciales, mejorar la documentación y ampliar los ejemplos del SDK. Si el prototipo evolucionara hacia un entorno productivo, también habría que estudiar replicación, alta disponibilidad y una política de retención mejor definida para Redis.

La conclusión final es deliberadamente acotada: Dominus Broker demuestra que el enfoque híbrido es viable como prototipo y ofrece una base medible para continuar el trabajo. No demuestra todavía preparación productiva. Precisamente por eso la evaluación es útil: además de mostrar lo que funciona, identifica las condiciones necesarias para la siguiente versión.

Muchas gracias. Quedamos atentos a sus preguntas.

### Control de tiempo

- 0:00-1:15. Configuración de las pruebas de carga.
- 1:15-2:25. Resultados cuantitativos.
- 2:25-3:25. Límites de la evidencia.
- 3:25-4:40. Conclusiones y trabajo futuro.
- 4:40-5:00. Cierre.

## Reglas para el ensayo

- Ensayar con cronómetro. El objetivo es terminar cada bloque entre 4:40 y 4:55 para dejar margen a la transición.
- No leer las diapositivas. Usarlas como apoyo y mantener el detalle en este guion.
- Mantener las mismas cifras en toda la exposición: 143 pruebas unitarias, 3 pruebas de integración, 91.8 % de cobertura, P99 cercano a 10 ms y throughput observado de 200,000 a 260,000 mensajes por segundo.
- Presentar el throughput como una métrica observada posiblemente agregaddomna, no como capacidad máxima garantizada.
- No afirmar una garantía general de `exactly once`. La propuesta usa entrega al menos una vez y control de idempotencia dentro del broker.
- Si el jurado pregunta por los fallos de seguridad, responder con el hallazgo, la causa y la corrección propuesta. Evitar justificarlos o minimizarlos.
- Usar "prototipo", "escenario evaluado" y "resultado observado" cuando corresponda. Reservar "producción" para el trabajo futuro.

