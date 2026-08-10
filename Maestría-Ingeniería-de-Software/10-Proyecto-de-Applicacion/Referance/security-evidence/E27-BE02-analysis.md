# BE-02 — Protección del monitor HTTP

## Resultados observados

- Sin `x-api-key`: `HTTP/1.1 403 Forbidden`, `failed to match token`.
- Token inválido: `HTTP/1.1 403 Forbidden`, `failed to match token`.
- Token válido: `/health` devuelve `HTTP/1.1 200 OK` y `Health ok`.
- Token válido: `/metrics` devuelve `HTTP/1.1 200 OK` y métricas Prometheus.
- El broker permaneció activo después de los casos.
- `X-Forwarded-For: 10.0.0.10` con token válido: `HTTP/1.1 200 OK`; la cabecera no alteró indebidamente la autenticación.

## Clasificación

**Aprobada para autenticación del monitor HTTP.** Los endpoints no se exponen sin token y las solicitudes autorizadas funcionan.

## Evidencia

- `E27-BE02-no-token.txt`
- `E28-BE02-invalid-token.txt`
- `E29-BE02-valid-health.txt`
- `E30-BE02-valid-metrics.txt`
- `E30-BE02-forwarded-for.txt`
