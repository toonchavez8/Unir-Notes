# CL-03 — Validación y autorización de destinos

## Resultado

**Fallida / incompleta.** La validación acepta `hostname.test/path`, aunque no es un destino gRPC válido con formato host:puerto. También acepta `127.0.0.1:5000`, pero el SDK no implementa una allowlist que distinga sintaxis de autorización.

Casos rechazados: `hostname.test:5000` y `hostname.test:99999`.

Evidencia: `E36-CL03-destinations.txt`.

Recomendación: parsear con `net/url`/`net.SplitHostPort`, validar rango de puerto y aplicar una allowlist explícita antes de crear conexiones.
