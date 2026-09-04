# Borrador textual de la presentación

Este archivo contiene únicamente el texto propuesto para las diapositivas. Los campos de responsable son notas internas de coordinación y no deben aparecer en la versión proyectada.

## Diapositiva 1. Portada

Responsable: ____________________

Diseño e implementación de Dominus Broker  
Broker de mensajería en tiempo real basado en gRPC y Redis Streams

Maikel Barrios Insua  
Daniel Campos Castañeda  
Miguel de Jesús Chávez Barragán  
Fernando Enrique García Castellanos  
César Octavio Sánchez Contreras

Maestría en Ingeniería de Software y Sistemas Informáticos  
Septiembre de 2026

## Diapositiva 2. El problema exige dos ritmos de comunicación

Responsable: ____________________

- Algunos eventos deben entregarse de inmediato mediante conexiones persistentes.
- Otros deben esperar hasta que el consumidor tenga capacidad para procesarlos.
- Los reintentos pueden duplicar operaciones y comprometer la consistencia.
- Resolver cada necesidad con una plataforma distinta aumenta la integración y la operación.

## Diapositiva 3. La pregunta del trabajo

Responsable: ____________________

¿Es viable integrar, dentro de un mismo broker, comunicación en tiempo real, mensajería asíncrona con confirmación y control de duplicados?

Objetivo general:

Diseñar, implementar y evaluar un prototipo basado en gRPC y Redis Streams para escenarios representativos de sistemas distribuidos.

## Diapositiva 4. Alcance del prototipo

Responsable: ____________________

- Publicación, consumo y confirmación de mensajes.
- Streaming de cliente, de servidor y bidireccional.
- Fan-in, fan-out y broadcast.
- Idempotencia mediante claves con TTL.
- SDK, autenticación, TLS, logs, métricas y health checks.

Dominus no pretende sustituir a Kafka, Pulsar, RabbitMQ o NATS.

## Diapositiva 5. La selección tecnológica responde al alcance

Responsable: ____________________

| Necesidad | Decisión |
|---|---|
| Comunicación tipada y streaming | gRPC + Protocol Buffers |
| Implementación concurrente | Go |
| Cola y memoria temporal | Redis Streams |
| Integración de clientes | SDK de Dominus |
| Separación de responsabilidades | Puertos y adaptadores |

Kafka, Pulsar, RabbitMQ y NATS se utilizaron como referencias comparativas, no como objetivos de reemplazo.

## Diapositiva 6. Un broker, dos recorridos

Responsable: ____________________

Tiempo real:

Productor -> BrokerAPI -> streaming gRPC -> suscriptores

Asíncrono:

Producer -> Redis Streams -> Consumer -> procesamiento -> Ack

El canal en tiempo real prioriza la entrega inmediata.  
El canal asíncrono desacopla el ritmo de productores y consumidores.

## Diapositiva 7. Arquitectura de Dominus Broker

Responsable: ____________________

1. Clientes externos y SDK.
2. Entrada gRPC: BrokerAPI y SqsAPI.
3. Casos de uso de aplicación.
4. Entidades y puertos del dominio.
5. Adaptadores: Redis, gRPC saliente, seguridad y observabilidad.

La lógica central no depende directamente del transporte ni del almacenamiento.

## Diapositiva 8. Metodología experimental e iterativa

Responsable: ____________________

Objetivo metodológico:

Desarrollar un prototipo funcional y observar su comportamiento bajo carga, concurrencia y comunicación en tiempo real.

Analizar -> diseñar -> implementar -> experimentar -> evaluar -> ajustar

## Diapositiva 9. Análisis del problema

Responsable: ____________________

- Latencia en escenarios interactivos.
- Comunicación persistente y bidireccional.
- Reprocesamiento por reintentos.
- Difusión de eventos a varios consumidores.

Necesidad detectada:

Comunicación bidireccional + arquitectura orientada a eventos

## Diapositiva 10. Diseño de la solución

Responsable: ____________________

Modelo híbrido: tiempo real + asincronía

- gRPC: unary, server streaming, client streaming y streaming bidireccional.
- Redis Streams: publicación, consumo pull y confirmación.
- Patrones: fan-in, fan-out y broadcast.
- Control: idempotencia, TTL y recuperación de mensajes.

## Diapositiva 11. Experimentación

Responsable: ____________________

Escenario síncrono:

- Streaming gRPC.
- Broadcast y varios suscriptores.
- Múltiples productores y conexiones abiertas.

Escenario asíncrono:

- Productor y consumidor desacoplados mediante Redis.
- Consumo pull y verificación de pendientes.

Herramientas: ghz, configuraciones YAML, Grafana y Redis.

## Diapositiva 12. Criterios de evaluación

Responsable: ____________________

- Latencia: tiempo entre emisión y entrega.
- Throughput: mensajes procesados por segundo.
- Consistencia: entrega y confirmación del mensaje.
- Duplicados: reprocesamiento observado.
- Idempotencia: aceptación única por clave.

## Diapositiva 13. Comparación y límites del enfoque

Responsable: ____________________

Lo que aporta el prototipo:

- Streaming y broadcast en el canal principal.
- Comunicación bidireccional.
- Flujo asíncrono pull con Redis Streams.
- Idempotencia integrada al recorrido del mensaje.

Lo que todavía no resuelve:

- Alta disponibilidad de Redis.
- Orden global.
- Persistencia del canal en tiempo real.
- Todos los casos cubiertos por brokers consolidados.

## Diapositiva 14. Campos de aplicación posibles

Responsable: ____________________

- Monitorización de procesos sensibles a la latencia.
- IoT y sistemas industriales con conexiones persistentes.
- Notificaciones y eventos en tiempo real.
- Banca digital y servicios interactivos.
- Comunicación con servicios y modelos de inteligencia artificial.

Son campos de estudio potenciales, no despliegues productivos ya validados.

## Diapositiva 15. Componentes implementados

Responsable: ____________________

- Servidor en Go y contratos Protocol Buffers.
- BrokerAPI para streaming gRPC.
- SqsAPI para Producer, Consumer y Ack.
- Redis Streams y control de idempotencia.
- SDK para productores y consumidores.
- Autenticación, TLS, logs, métricas y health checks.

## Diapositiva 16. Los flujos principales funcionaron en las pruebas

Responsable: ____________________

143 pruebas unitarias: todas PASS  
91.8 % de cobertura global instrumentada  
100 % de cobertura en los casos de uso principales

3 pruebas de integración: todas PASS

- Producer hasta Redis Streams.
- Consumer + Ack sin mensajes pendientes.
- Streaming bidireccional: 2 mensajes x 2 suscriptores = 4 respuestas.

## Diapositiva 17. La evaluación también encontró deuda técnica

Responsable: ____________________

Usabilidad:

- Adecuada para usuarios técnicos.
- La documentación y las pruebas facilitan el aprendizaje.
- Go, gRPC y Redis elevan la curva inicial.

Ciberseguridad:

- Una solicitud gRPC sin token puede detener el proceso.
- La idempotencia no es atómica bajo concurrencia.
- TLS valida CA y SAN, pero el SDK usa `panic` para errores.
- Deben corregirse la validación de destinos y la serialización.

## Diapositiva 18. Resultados observados bajo carga

Responsable: ____________________

| Indicador | Resultado observado |
|---|---:|
| Throughput | 200,000-260,000 mensajes/s |
| Latencia P99 | Cerca de 10 ms |
| CPU | Aproximadamente 1 %-4 % |
| Memoria | Aproximadamente 36 %-42 % |
| Disponibilidad | Cerca del 100 % |
| Consumidores Redis | 3 |
| Pending en Redis | 0 |

Resultados de la ventana experimental, no garantías de producción.

## Diapositiva 19. La evidencia es favorable, pero acotada

Responsable: ____________________

- El throughput puede agregar más de una fuente de carga.
- Las ventanas de observación fueron breves.
- No hubo pruebas prolongadas ni inyección completa de fallos.
- No se validó recuperación ante pérdida de consumidores.
- Redis se evaluó sin replicación, Sentinel o Cluster.

La prueba demuestra viabilidad inicial, no capacidad máxima ni resiliencia productiva.

## Diapositiva 20. Conclusiones y siguiente versión

Responsable: ____________________

Conclusión:

Dominus integró correctamente streaming gRPC y mensajería asíncrona con Redis Streams dentro del alcance del prototipo.

Prioridades siguientes:

1. Reserva atómica de idempotencia.
2. Corrección del middleware de autenticación y del manejo de errores.
3. Pruebas prolongadas, recuperación e inyección de fallos.
4. Métricas separadas por flujo y más escenarios de carga.
5. Mejoras en SDK, ejemplos y documentación.

Dominus es una base funcional y medible para continuar el desarrollo.

