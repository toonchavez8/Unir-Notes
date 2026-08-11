# BE-07 — Redis y privilegios

## Casos

- Contenedores y puertos publicados.
- Usuario ACL de laboratorio `dominus`.
- Configuración de Redis y expiración de claves de idempotencia.
- Revisión de que no se impriman credenciales en logs.

## Resultado observado

- Redis tiene el puerto `6379` publicado al host.
- El usuario ACL `dominus` existe y `PING` devuelve `PONG`.
- La configuración usa DB 1 y expiración de 10 segundos.
- La operación de laboratorio `be07-ttl-check` creó `idempotency:be07-ttl-check`; inmediatamente después Redis devolvió `TTL=10` segundos.
- La revisión de logs detectó líneas que podrían contener términos relacionados con credenciales; fueron marcadas y redactadas en la evidencia, sin copiar valores.

## Clasificación

**Inconclusa con hallazgos.** La ACL y el TTL funcionan, pero Redis está expuesto al host. Se recomienda no publicar `6379` y usar una red interna.

## Evidencia

- `E33-BE07-containers.txt`
- `E33-BE07-redis-config.txt`
- `E33-BE07-redis-checks.txt`
