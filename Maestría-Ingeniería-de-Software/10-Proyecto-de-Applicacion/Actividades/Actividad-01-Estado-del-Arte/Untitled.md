# 2.3.1 Brokers De Mensajería Y Plataformas Existentes

Los Brokers de mensajería forman parte de una arquitectura distribuida moderna, esto es debido a que permiten desacoplar productores y consumidores. Usan métodos de publicación y suscripción, enrutamiento y persistencia de mensajes para garantizar la transferencia de mensajes entre sistemas.  Estos sistemas contemplan la tolerancia de fallos, promueven una estabilidad horizontal, el control del flujo y garantías de entrega de mensajes. 

Seleccionar un broker de mensajería es indispensable para implementar un sistema híbrido que combina colas de trabajo para streaming de eventos o mensajes como la que proponemos. Cada plataforma ofrece ventajas y limitaciones, particularmente en términos de rendimiento, complejidad y modelos de consumo solo para mencionar algunos. Por esa razón realizamos un análisis comparativo de distintas plataformas como brokers que están usadas en la industria para identificar la más adecuada para el desarrollo del broker híbrido.

Existe Apache Kafka que es una de las plataformas más usadas para el streaming de eventos (Apache Kafka, s. f.). Gracias a su arquitectura basada en retención de evento y presentación distribuido. Kafka streams incorpora conceptos de procesamiento con garantías de “Exactly-Once”, con esta fortaleza viene con mayor complejidad. Especialmente cuando se require de administrar clústeres, particiones, retention, replicación y ecosystem de conectores. 

Por otro lado tenemos a Rabbitmq que funciona similar a un broker pero de forma distinta. Como es un broker estilo AMQP. RabbitMQ destaca por intercambio sus colas y las claves de enrutamiento y el publicador lo confirma (RabbitMQ, s. f.). El modelo cómo se trabaja es muy ágil para colas de trabajo tiene un enrutamiento flexible y patrones de mensajería ya validados a nivel producción. Filtro del proyecto que estaremos desarrollando como propuesta rabbitmq tiene mayor madurez como broker. El centro de conocimiento no está orientado a exponer una api con grpc ni en demostrar la integración entre streaming a través de grpc y red strings no nos permitiría tener esa Unión.

Otra herramienta que existe es Apache pulsar que combina la publicación y suscripción acontecimientos y una arquitectura distribuida entre el almacenamiento y cómputo (Apache Pulsar, s. f.). Pulsar nos ofrece capacidades avanzadas como distintos tipos de suscripción y mayor persistencia. Una limitante de su arquitectura es que resulta set más compleja de lo que necesitamos para un prototipo que su objetivo es estudiar los comportamientos internos de un broker híbrido. 

Una alternativa para bajar la latencia es NATS JetStream por su forma de tener persistencia de streaming de mensajería y la forma de set comunicadores de pull y push. La documentación afirma que se incorporan consumidores con mayor seguimiento de entregas y acontecimientos y que los consumidores pueden procesar mensajes bajo demanda (NATS, s. f.). El diseño de Nats es algo que lo hace destacar por su simplicidad y el rendimiento que se ofrece, su ecosistema es menor cuando lo comparamos con otras soluciones.  

Finalmente, uno de los creadores de GRPC, google ofrece Google cloud pub/sub  su servicio de mensajería con suscripciones de pull y push. La ventaja de esta herramienta es la carga operativa de equipo dado que es una limitación para este trabajo que se oculta gran parte en una solución interna lo cual reduce mayormente el objetivo que es construir y evaluar el broker híbrido.Dado a justamente que los mecanismos internos están abstraídos por el proveedor esta solución limita la posibilidad de experimentar con los components internos que limitan o impactan en el funcionamiento de el broker de mensajería.

# 2.3.3 Patrones Fan-out Y Fan-in

Un patrón frecuente que se usa mucho en sistemas concurrentes y distribuidos es el patrón de fan out y fan in. Este patrón consiste en distribuir un evento o unidad de trabajo hacia múltiples destinos y de múltiples fuentes de orígenes hacia una eje central según describen Hohpe y Woolf (2003). Que termina haciendo una arquitectura estilo abanico de como pasan los datos de múltiples Fuentes a una fuente central aparecen integraciones empresariales y en producción procesamiento paralelo y arquitectura arquitecturas específicamente orientada a eventos (Hohpe & Woolf, 2003)

En nuestra propuesta del broker el fan out lo usaremos cuando un productor va a publicar un evento y debe llegar a varios consumidores. En este caso nuestro broker centraliza la distribución y evita que el productor tenga que gestionar más conexiones individuales con cada receptor, por esa razón este patrón es útil para las notificaciones de propagación de eventos y actualización de cachés o activación de procesos secundarios. 

Una vez que el consumidor genera una respuesta debe considerarse en su flujo de origen o el punto central en este caso ya aplicamos el fan-ín. Esta es la parte más compleja porque implicaría concurrencia el orden de llegada el cierre es de El stream y evitar errores parciales y time out exceptions por la latencia de la señal. Go, el lenguaje de programación, para este tema tiene justamente la solución mediante goRoutines y canales que permiten la ejecución concurrente y la comunicación entre flujos de forma directa ayudando a aliviar errores parciales (The Go Authors, s. f.).

Aun así, los patrones de Fan-in y Fan-out vienen con riesgos que debemos de mantener en la mente. Cada mensaje enviado es generado sin límite o un suscrito lento bloquea el flujo podemos tener temas de backpressure, el consumo de memoria o fuga de goRoutines. Por eso se debe considerar implementar límites de concurrencias y políticas de reintento.

# 2.3.4 Arquitectura Hexagonal Y Arquitectura Limpia

Se propone la implementación de la arquitectura hexagonal que también es conocida como puertos y adaptadores que fue primera vez implementada por Cockburn (2005) con la intención de encapsular las reglas de negocio los detalles externos como interfaces y servicios de infraestructura por separado. Esta visión de patrón permite que una aplicación ubicada en el centro de la arquitectura pueda set probada y conectada de distintos adaptadores sin depender de uno como núcleo. 

Martin (2017) mencionan que las dependencias deben de apuntar hacia las reglas de negocio y no depender totalmente de ellas. En un broker híbrido donde la separación permite probar que los puertos funcionan como entradas y salidas de la aplicación mientras que los adaptadores habilita que se conecten a esos puertos con la tecnología que utilicemos. Para el caso del broker esta separación nos permite tener una distribución y publicación que integra la comunicación entre streaming, redis, y la idempotencia.

# Referencias

~~*Apache Kafka. (s. f.). Apache Kafka documentation. Recuperado el 8 de junio de 2026, de https://kafka.apache.org/documentation/*~~

~~Apache Pulsar. (s. f.). *Messaging concepts*. Recuperado el 8 de junio de 2026, de https://pulsar.apache.org/docs/next/concepts-messaging/~~

~~*Cockburn, A. (2005). Hexagonal architecture. Recuperado el 8 de junio de 2026, de https://alistair.cockburn.us/hexagonal-architecture/*~~

~~*Hohpe, G., & Woolf, B. (2003). Enterprise integration patterns: Designing, building, and deploying messaging solutions. Addison-Wesley.*~~

~~Martin, R. C. (2017). *Clean architecture: A craftsman's guide to software structure and design*. Prentice Hall.~~

~~NATS. (s. f.). *JetStream consumers*. Recuperado el 8 de junio de 2026, de https://docs.nats.io/nats-concepts/jetstream/consumers~~

~~RabbitMQ. (s. f.). *Consumer acknowledgements and publisher confirms*. Recuperado el 8 de junio de 2026, de https://www.rabbitmq.com/docs/confirms~~

~~The Go Authors. (s. f.). *Documentation*. Recuperado el 8 de junio de 2026, de https://go.dev/doc/~~

Newman, S. (2021). *Building microservices* (2nd ed.). O'Reilly Media.

~~*Google Cloud. (s. f.). Pub/Sub overview. Google Cloud Documentation. Recuperado el 8 de junio de 2026, de https://cloud.google.com/pubsub/docs/overview*~~