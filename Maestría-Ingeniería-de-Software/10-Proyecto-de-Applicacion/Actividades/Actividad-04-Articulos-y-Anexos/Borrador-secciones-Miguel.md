# Borrador de las secciones de Miguel

Documento de referencia: `TFM_Unir-F1011-Servicio_Mensajeria-Gdocs.docx`.

## 1. Resumen

Este trabajo presenta el diseño, la implementación y la evaluación de Dominus Broker, un broker de mensajería híbrido para sistemas distribuidos. La propuesta combina la comunicación en tiempo real mediante gRPC con un flujo asíncrono basado en Redis Streams. El objetivo fue desarrollar un prototipo que permitiera publicar, consumir y confirmar mensajes, además de controlar los duplicados mediante claves de idempotencia.

El broker se implementó en Go con una arquitectura de puertos y adaptadores. El contrato de comunicación se definió con Protocol Buffers y se desarrolló un SDK para facilitar la conexión de productores y consumidores. La solución también incluye autenticación mediante token, soporte para TLS, endpoints de salud, métricas y registros de ejecución.

La evaluación incluyó pruebas unitarias y de integración, una revisión de usabilidad técnica, un análisis de ciberseguridad y pruebas de carga. Se ejecutaron 143 pruebas unitarias y 3 pruebas de integración, todas con resultado PASS. La cobertura global instrumentada fue del 91,8 %. Durante la prueba de rendimiento se observaron entre 200 000 y 260 000 mensajes por segundo, una latencia P99 cercana a 10 ms, un uso de CPU de aproximadamente entre el 1 % y el 4 %, y una disponibilidad próxima al 100 % en la ventana analizada. El análisis de seguridad también reveló problemas que deben corregirse: una vulnerabilidad de disponibilidad en el middleware de autenticación y una condición de carrera en el control de idempotencia. En consecuencia, el prototipo demuestra que la propuesta es viable para los escenarios evaluados, aunque todavía necesita correcciones y pruebas más amplias antes de utilizarse en producción.

**Palabras clave:** broker de mensajería; gRPC; Redis Streams; idempotencia; sistemas distribuidos.

## 2. Abstract

This work presents the design, implementation, and evaluation of Dominus Broker, a hybrid messaging broker for distributed systems. The proposal combines real-time communication through gRPC with an asynchronous flow based on Redis Streams. The objective was to develop a prototype that could publish, consume, and acknowledge messages, while also using idempotency keys to control duplicate requests.

The broker was implemented in Go using a ports-and-adapters architecture. The communication contract was defined with Protocol Buffers, and a client SDK was developed to simplify the connection of producers and consumers. The solution also includes token-based authentication, TLS support, health endpoints, metrics, and execution logs.

The evaluation included unit and integration tests, a technical usability review, a cybersecurity analysis, and load tests. A total of 143 unit tests and 3 integration tests were executed, all with a PASS result. Overall instrumented coverage reached 91.8%. During the performance test, the system processed approximately 200,000 to 260,000 messages per second, with a P99 latency close to 10 ms, CPU usage between approximately 1% and 4%, and nearly 100% availability during the observed window. The security analysis also found issues that require correction: an availability vulnerability in the authentication middleware and a race condition in the idempotency control. The prototype therefore shows that the proposal is feasible for the evaluated scenarios, but further corrections and testing are required before production use.

**Keywords:** messaging broker; gRPC; Redis Streams; idempotency; distributed systems.

## 3. Índice de figuras

La página se debe completar después de actualizar los campos en Word.

| Figura | Título                                                             | Página |
| -----: | ------------------------------------------------------------------ | -----: |
|      1 | Diagrama de componentes de la capa de persistencia basada en Redis |    ___ |
|      2 | Diagrama de contexto general del sistema                           |    ___ |
|      3 | Secuencia de cola asíncrona con Producer, Consumer y Ack           |    ___ |
|      4 | Diagrama de clases de Broker/gRPC Streaming                        |    ___ |
|      5 | Diagrama de clases de SQS/Message Management                       |    ___ |
|      6 | Secuencia de fan-out en tiempo real                                |    ___ |
|      7 | Estados del mensaje asíncrono                                      |    ___ |
|      8 | Actividad de idempotencia                                          |    ___ |
|      9 | Evidencia de ejecución de pruebas unitarias                        |    ___ |
|     10 | Verificación de pruebas superadas y ausencia de fallos             |    ___ |
|     11 | Ejecución de pruebas de integración del flujo SQS                  |    ___ |
|     12 | Ejecución de pruebas de integración del flujo de streaming         |    ___ |
|     13 | Panel de Grafana durante la evaluación de rendimiento              |    ___ |
|     14 | Segunda ventana del panel de Grafana                               |    ___ |
|     15 | Continuidad de las métricas durante la ejecución                   |    ___ |
|     16 | Valores finales registrados durante la carga                       |    ___ |
|     17 | Entradas almacenadas en Redis Streams                              |    ___ |

## 4. Índice de tablas

La página se debe completar después de actualizar los campos en Word.

| Tabla | Título | Página |
|---:|---|---:|
| 1 | Comparación de tecnologías de mensajería | ___ |
| 2 | Elementos previstos para la capa de persistencia | ___ |
| 3 | Módulos de pruebas unitarias | ___ |
| 4 | Pruebas de integración ejecutadas | ___ |
| 5 | Resumen de hallazgos del análisis de ciberseguridad | ___ |
| 6 | Escenarios y parámetros de las pruebas de rendimiento | ___ |
| 7 | Valores iniciales y finales de CPU, memoria y disponibilidad | ___ |
| 8 | Indicadores principales y evidencia de rendimiento | ___ |
| 9 | Objetivos preliminares de nivel de servicio | ___ |
| 10 | Comparación de tecnologías de mensajería del artículo | ___ |
| 11 | Módulos de pruebas unitarias del artículo | ___ |
| 12 | Pruebas de integración ejecutadas en el artículo | ___ |
| 13 | Hallazgos del análisis de ciberseguridad del artículo | ___ |
| 14 | Requisitos y herramientas de ejecución | ___ |
| 15 | Configuración del broker y Redis | ___ |
| 16 | Flujo de verificación y evidencias | ___ |
| 17 | Incidencias y resultados de las pruebas de seguridad | ___ |

## Observaciones para pasarlo a Word

- Elimina las tablas y figuras de ejemplo de la plantilla antes de generar los índices. De lo contrario, aparecerán duplicados como `Tabla 1` y `Figura 1`.
- Usa el mismo formato en todos los rótulos: `Figura n. Título` y `Tabla n. Título`.
- Revisa las referencias cruzadas. En la sección de integración se menciona la «Tabla 2», pero la tabla de pruebas de integración aparece como `Tabla 4` en la numeración actual.
- Después de insertar el texto y corregir los rótulos, selecciona cada índice en Word y elige **Actualizar toda la tabla**.

