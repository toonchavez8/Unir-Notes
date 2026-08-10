# CL-01 — Validación TLS del servidor

## Resultado

**Aprobada.** Con certificados efímeros:

- CA válida y SAN `localhost`: conexión aceptada.
- CA distinta: rechazada.
- Nombre de servidor incorrecto: rechazado.
- CA inexistente: error de inicialización.

Evidencia: `E34-CL01-tls.txt`.

No se escribieron claves privadas ni tokens en la salida.
