# BE-06 — TLS y degradación a texto plano

## Configuración observada en el repositorio

- `tls: false` para Redis en `env.prod.json`.
- La imagen de laboratorio no contiene certificados en `/etc/dominus/certs`.
- El arranque efectivo observado anuncia gRPC en `0.0.0.0:5000` y acepta `grpcurl -plaintext`.

## Resultado observado

- gRPC plaintext: enumeró los servicios correctamente.
- gRPC con `-insecure`: falló con `tls: first record does not look like a TLS handshake`.
- HTTPS en el monitor: falló el handshake TLS.
- HTTP en el monitor: respondió `403 Forbidden` por falta de token, confirmando que el listener efectivo es plaintext.
- No se pudieron ejecutar A–D con CA/SAN porque la imagen no contiene certificados de laboratorio.

## Clasificación

**Fallida — degradación a texto plano confirmada.** La aplicación no falló cerrada cuando TLS no estaba disponible; arrancó y expuso gRPC/HTTP sin TLS. No se debe afirmar confidencialidad del token en tránsito.

## Evidencia

- Configuración: `E32-BE06-tls-config.txt`.
- Prueba de transporte: `E32-BE06-transport.txt`.
