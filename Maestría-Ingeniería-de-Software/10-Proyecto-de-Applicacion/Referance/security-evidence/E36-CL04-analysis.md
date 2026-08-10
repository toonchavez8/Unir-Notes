# CL-04 — Cancelación y tiempo límite

## Resultado

**Inconclusa con limitación.** La operación termina por el límite externo de aproximadamente 2 segundos, pero el SDK construye internamente sus streams con `context.Background()` y no permite al consumidor suministrar un contexto.

Evidencia: `E36-CL04-timeout.txt`.

Recomendación: exponer métodos que reciban `context.Context` y propagarlo hasta `ClientStream`, `ServerStream` y `BidirectionalStream`.
