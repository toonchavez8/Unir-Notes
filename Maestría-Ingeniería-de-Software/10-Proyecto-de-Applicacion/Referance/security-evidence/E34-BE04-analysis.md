# BE-04 — Destinos de suscriptores

## Alcance

La prueba utiliza exclusivamente `127.0.0.1:9000`. El receptor se ejecuta dentro del mismo contenedor del broker para que loopback tenga el significado correcto.

## Caso

- Destino enviado: `127.0.0.1:9000`.
- Protocolo: gRPC `BrokerAPI/ServerStream`.
- Credenciales: token de laboratorio y clave de idempotencia efímera.
- No se probaron redes privadas, metadata endpoints, LAN ni servicios públicos.

## Resultado observado

- El cliente gRPC recibió `DeadlineExceeded` al no obtener una respuesta del destino.
- El receptor loopback capturó el prefijo `PRI * HTTP/2.0`, demostrando que el broker inició una conexión hacia `127.0.0.1:9000`.
- El broker registró varios intentos con `dial tcp 127.0.0.1:9000: connect: connection refused`.
- El proceso del broker permaneció activo.

## Clasificación

**Inconclusa para autorización de destinos.** Se confirmó el intento de conexión a loopback, pero el código no mostró una política explícita de allowlist/rechazo antes del intento. El receptor usado no implementó un servicio gRPC completo.

## Evidencia

- `E34-BE04-loopback.txt`
- `E34-BE04-observation.txt`
- `E34-BE04-broker-log.txt`

## Criterio

Debe quedar claro si el broker acepta la dirección, intenta conectar al loopback y registra correctamente el éxito o error. La política recomendada es permitir únicamente destinos explícitamente autorizados y rechazar destinos no validados antes de iniciar conexiones salientes.
