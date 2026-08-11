# BE-05 — Límites de payload, suscriptores y streams

## Casos

- Payloads: 1 KiB, 64 KiB, 1 MiB y 4 MiB.
- Streams: máximo conservador de 20 conexiones.
- Se registra latencia, resultado, memoria, proceso y goroutines cuando están disponibles.

## Resultado observado

- 1 KiB: aceptado, proceso vivo.
- 64 KiB: aceptado, proceso vivo.
- 1 MiB: aceptado, proceso vivo.
- 4 MiB: `ResourceExhausted`; el mensaje recibido fue `4194309` frente al máximo `4194304`, debido al framing protobuf.
- 20 streams: todos terminaron con `DeadlineExceeded` al cerrar el timeout controlado de 1.5 s; el cliente cerró todos los contextos.
- Memoria Docker del broker: aproximadamente 56.8 MiB antes y 60.01 MiB después del probe de payload; durante los 20 streams llegó aproximadamente a 245 MiB y el proceso permaneció vivo.

## Clasificación

**Aprobada con observación.** Existe un límite gRPC efectivo de 4 MiB y el broker no cayó. Los streams no entregaron respuesta al destino loopback de prueba dentro del timeout, pero fueron cerrados de forma controlada.

## Evidencia

- `E35-BE05-payloads.txt`
- `E35-BE05-streams.txt`
- `E35-BE05-stats-after.txt`

## Criterio

El objetivo es identificar límites explícitos y comportamiento controlado. Una caída del broker se registra como fallo, no como resultado deseado.
