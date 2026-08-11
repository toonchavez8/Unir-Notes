# BE-01 — Autenticación gRPC ante cabecera ausente

## Resultado observado

La solicitud sin `x-api-key` no fue rechazada con `Unauthenticated`. El broker produjo:

```text
panic: runtime error: index out of range [0] with length 0
dominus-broker/internal/infrastructure/grpc/middlewares.(*middlewares).ApiToken
.../middlewares.go:48
```

Después del `panic`, el puerto `5000` dejó de aceptar conexiones.

## Casos posteriores

- Token gRPC inválido: `Unauthenticated`, evidencia `E25-BE01-invalid-token.txt`.
- Token gRPC válido: se enumeraron `dominus.BrokerAPI`, `dominus.SqsAPI` y los servicios de reflection, evidencia `E26-BE01-valid-token.txt`.
- Después de ambos casos el contenedor permaneció `Up`.

## Clasificación

**Fallida — severidad alta.** La ausencia de credenciales provoca una caída del proceso y permite una denegación de servicio mediante una entrada no autenticada.

## Evidencia

- `E21-broker-startup.txt`: arranque y panic del broker.
- `E23-BE01-no-token.txt`: intento de consulta sin token y conexión rechazada después de la caída.

## Resultado esperado

La solicitud sin token debe devolver `Unauthenticated` y el proceso debe permanecer activo.

## Recomendación

Validar que la metadata `x-api-key` exista y contenga al menos un valor antes de acceder a su primer elemento. Añadir una prueba de regresión que invoque el método sin metadata y compruebe que el proceso permanece vivo.
