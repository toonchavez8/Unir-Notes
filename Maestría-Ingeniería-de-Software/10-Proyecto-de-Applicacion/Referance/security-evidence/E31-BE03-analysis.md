# BE-03 — Idempotencia bajo concurrencia

## Prueba implementada

Archivo: `Referance/dominus-broker/tests/security/idempotency_security_test.go`

- Redis efímero mediante `miniredis`.
- 20 rondas.
- 20 goroutines por ronda.
- Una única clave `idempotency-header` compartida por ronda.
- Criterio: exactamente una solicitud aceptada.
- Ejecución prevista con `go test -race`.

## Hipótesis

El middleware ejecuta `CheckConsumer` y después inicia `SaveConsumer` en una goroutine separada. Esa secuencia puede permitir que varias solicitudes observen la clave como inexistente antes de que la primera escritura termine.

## Resultado observado

La ejecución `go test -race -count=20 ./tests/security` terminó con `FAIL`.

- En las 20 rondas se aceptaron múltiples solicitudes con la misma clave.
- El conteo observado varió entre 3 y 20 solicitudes aceptadas de 20.
- Las restantes devolvieron `Aborted: rate limit reached`.
- No se reportó una carrera de datos del runtime; el fallo es lógico y reproducible.

## Clasificación

**Fallida — severidad alta.** El patrón `CheckConsumer` seguido de `SaveConsumer` asíncrono permite que varias solicitudes superen la comprobación antes de que la clave sea persistida. Debe utilizarse una operación atómica de reserva (`SET NX`) como decisión de aceptación, no una comprobación separada.
