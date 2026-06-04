# Guia paso a paso para probar Dominus

## 1. Proposito

Este documento explica como probar el sistema Dominus para entenderlo tecnicamente.

La guia esta pensada para avanzar en niveles:

1. Verificar que los repos estan disponibles.
2. Leer el contrato gRPC.
3. Ejecutar pruebas automatizadas.
4. Levantar Redis.
5. Levantar `dominus-broker`.
6. Probar health y metrics.
7. Probar la API tipo cola `SqsAPI`.
8. Entender como probar la parte streaming `BrokerAPI`.
9. Revisar Redis para ver el efecto real.
10. Interpretar fallos comunes.

## 2. Requisitos

Necesitas:

- Git.
- Go compatible con el `go.mod` del broker.
- Docker, recomendado para Redis local.
- PowerShell en Windows o Bash en Linux/macOS.
- `curl` para probar REST.
- `grpcurl` opcional para probar gRPC manualmente.
- Terraform opcional si quieres levantar la pila completa.

## 3. Repos involucrados

Los repos locales estan en:

- `Referance/dominus-broker`
- `Referance/dominus-sdk`
- `Referance/dominus-proto-definition`

Si no existen, ejecuta:

```bash
bash Referance/clone-dominus-deps.sh
```

## 4. Paso 1: revisar el contrato gRPC

Antes de correr nada, abre:

`Referance/dominus-proto-definition/proto/dominus.proto`

Ese archivo define dos servicios:

- `BrokerAPI`
- `SqsAPI`

`BrokerAPI` tiene:

- `ClientStream`
- `ServerStream`
- `BidirectionalStream`

`SqsAPI` tiene:

- `Producer`
- `Consumer`
- `Ack`

Esto te dice que el sistema tiene dos caras:

- streaming en tiempo real;
- cola asincrona tipo pull.

## 5. Paso 2: revisar el arranque del broker

Archivos clave:

- `Referance/dominus-broker/cmd/api/main.go`
- `Referance/dominus-broker/internal/bootstraps/bootstraps.go`
- `Referance/dominus-broker/config/config.go`

`main.go` solo parsea flags y llama a `RunApp`.

`bootstraps.go` arma todo:

- config;
- logs;
- Redis;
- gRPC;
- REST monitor;
- metricas;
- casos de uso.

`config.go` define la forma exacta del JSON que necesita el sistema.

Nota importante:

Algunas docs internas del repo mencionan carga por archivo local, pero el codigo actual de `config.NewConfig()` lee `APP_CONFIG`. Para probar manualmente, usa `APP_CONFIG`.

## 6. Paso 3: ejecutar pruebas automaticas del broker

Entra al repo:

```bash
cd Referance/dominus-broker
```

Ejecuta pruebas principales:

```bash
go test -race -count=1 ./tests/...
```

Que valida esto:

- casos de uso del broker;
- casos de uso `SqsAPI`;
- adaptadores gRPC;
- adaptadores Redis con `miniredis`;
- middlewares;
- monitor HTTP;
- integracion de flujos principales.

En Windows tambien puedes usar:

```powershell
.\Makefile.ps1 -Target test
```

Para coverage:

```powershell
.\Makefile.ps1 -Target test-cover
```

Interpretacion:

- Si falla una prueba de dependencias, revisa `go mod download`.
- Si falla una prueba de race, hay un problema de concurrencia.
- Si falla una prueba de integracion, revisa flujos gRPC, canales o Redis simulado.

## 7. Paso 4: levantar Redis local para pruebas manuales

La forma mas simple es usar Redis sin autenticacion local y ajustar `APP_CONFIG`.

Desde cualquier terminal:

```bash
docker run --name dominus-redis -p 6379:6379 -d redis:7-alpine
```

Verifica:

```bash
docker ps
```

Si ya existe:

```bash
docker start dominus-redis
```

Para detenerlo:

```bash
docker stop dominus-redis
```

Para borrarlo:

```bash
docker rm dominus-redis
```

## 8. Paso 5: preparar `APP_CONFIG`

Desde `Referance/dominus-broker`, define esta configuracion.

PowerShell:

```powershell
$env:APP_CONFIG = @'
{
  "grpc_config": {
    "port": 5000,
    "api_token": "dominus-api-key-1233464687"
  },
  "rest_config": {
    "port": 8000,
    "api_token": "dominus_example_@10102024KeyServerToken",
    "allow_origins": "0.0.0.0/0"
  },
  "cert_config": {
    "key_file": "./certs/cert.key",
    "ssl_ca_cert": "./certs/ca_cert.pem",
    "ssl_cert": "./certs/cert.pem"
  },
  "redis_config": {
    "port": 6379,
    "memory_db": 0,
    "checker_db": 1,
    "host": "localhost",
    "password": "",
    "tls": false,
    "username": "",
    "idem_potency_ex": 10,
    "stream_id": "consumer",
    "group_id": "consumer-group"
  },
  "log_config": {
    "log_mode": "cmd",
    "log_url": ""
  }
}
'@
```

Bash:

```bash
export APP_CONFIG='{
  "grpc_config": {
    "port": 5000,
    "api_token": "dominus-api-key-1233464687"
  },
  "rest_config": {
    "port": 8000,
    "api_token": "dominus_example_@10102024KeyServerToken",
    "allow_origins": "0.0.0.0/0"
  },
  "cert_config": {
    "key_file": "./certs/cert.key",
    "ssl_ca_cert": "./certs/ca_cert.pem",
    "ssl_cert": "./certs/cert.pem"
  },
  "redis_config": {
    "port": 6379,
    "memory_db": 0,
    "checker_db": 1,
    "host": "localhost",
    "password": "",
    "tls": false,
    "username": "",
    "idem_potency_ex": 10,
    "stream_id": "consumer",
    "group_id": "consumer-group"
  },
  "log_config": {
    "log_mode": "cmd",
    "log_url": ""
  }
}'
```

Por que password y username van vacios:

La imagen Redis simple no tiene ACL ni password configurados.
El `env.local.json` original usa usuario/password, pero eso requiere Redis configurado con ACL.
Para aprender el flujo, es mas simple iniciar con Redis local sin auth.

## 9. Paso 6: levantar el broker

Desde:

```bash
cd Referance/dominus-broker
```

Ejecuta:

```bash
go run ./cmd/api -banner=false
```

Si funciona, debe levantar:

- gRPC en `localhost:5000`;
- REST monitor en `http://localhost:8000`;
- Redis conectado a `localhost:6379`.

Como no hay certificados locales en `./certs`, el broker debe iniciar en modo inseguro local.

Eso esta bien para pruebas.
No es lo que se debe usar en produccion.

## 10. Paso 7: probar health check

En otra terminal:

```bash
curl -H "x-api-key: dominus_example_@10102024KeyServerToken" http://localhost:8000/health
```

Resultado esperado:

```text
Health ok
```

Si falla:

- revisa que el broker siga corriendo;
- revisa que el puerto sea `8000`;
- revisa que el header `x-api-key` sea correcto;
- revisa que `allow_origins` sea `0.0.0.0/0`.

## 11. Paso 8: probar metricas

```bash
curl -H "x-api-key: dominus_example_@10102024KeyServerToken" http://localhost:8000/metrics
```

Resultado esperado:

- salida de metricas Prometheus;
- metricas de CPU;
- metricas de memoria;
- metricas gRPC si ya hiciste llamadas gRPC.

Busca nombres como:

- `cpu_usage_percentage`
- `memory_usage_percentage`

## 12. Paso 9: instalar o verificar `grpcurl`

`grpcurl` permite llamar APIs gRPC desde terminal.

Verifica:

```bash
grpcurl --version
```

Si no lo tienes, puedes entender el sistema con los tests.
Pero para pruebas manuales de `SqsAPI`, `grpcurl` es muy util.

## 13. Paso 10: listar servicios gRPC

Dominus registra reflection, por eso puedes listar servicios:

```bash
grpcurl -plaintext -H "x-api-key: dominus-api-key-1233464687" localhost:5000 list
```

Resultado esperado:

- `dominus.BrokerAPI`
- `dominus.SqsAPI`
- servicios de reflection

Lista metodos:

```bash
grpcurl -plaintext -H "x-api-key: dominus-api-key-1233464687" localhost:5000 list dominus.SqsAPI
```

## 14. Paso 11: probar Producer

`Producer` recibe `bytes payload`.
En JSON para gRPC, los bytes se mandan como base64.

`hello dominus` en base64 es:

```text
aGVsbG8gZG9taW51cw==
```

Ejecuta:

```bash
grpcurl -plaintext \
  -H "x-api-key: dominus-api-key-1233464687" \
  -H "idempotency-header: producer-001" \
  -d "{\"payload\":\"aGVsbG8gZG9taW51cw==\"}" \
  localhost:5000 dominus.SqsAPI/Producer
```

Resultado esperado:

```json
{
  "status": "0"
}
```

Nota importante:

No reutilices `producer-001` en otra llamada.
La idempotencia del broker rechazara claves repetidas.

## 15. Paso 12: probar Consumer

Ejecuta:

```bash
grpcurl -plaintext \
  -H "x-api-key: dominus-api-key-1233464687" \
  -H "idempotency-header: consumer-001" \
  -d "{\"workerId\":\"worker-1\",\"groupId\":\"consumer-group\"}" \
  localhost:5000 dominus.SqsAPI/Consumer
```

Resultado esperado:

```json
{
  "messageId": "...",
  "date": "...",
  "message": "aGVsbG8gZG9taW51cw=="
}
```

Guarda el `messageId`.
Lo vas a necesitar para `Ack`.

## 16. Paso 13: probar Ack

Sustituye `<MESSAGE_ID>` por el valor que regreso `Consumer`.

```bash
grpcurl -plaintext \
  -H "x-api-key: dominus-api-key-1233464687" \
  -H "idempotency-header: ack-001" \
  -d "{\"workerId\":\"worker-1\",\"groupId\":\"consumer-group\",\"messageId\":\"1780546797614-0\"}" \
  localhost:5000 dominus.SqsAPI/Ack
```

Resultado esperado:

```json
{
  "messageId": "<MESSAGE_ID>",
  "date": "..."
}
```

Esto confirma que:

- el mensaje fue producido;
- Redis lo guardo;
- un worker lo consumio;
- el ack completo el ciclo.

## 17. Paso 14: inspeccionar Redis

Abre Redis CLI:

```bash
docker exec -it dominus-redis redis-cli
```

Dentro de Redis:

```text
XINFO STREAM consumer
XINFO GROUPS consumer
XPENDING consumer consumer-group
```

Que debes observar:

- el stream `consumer` existe;
- el grupo `consumer-group` existe;
- despues del ack, el pending deberia reducirse o estar en cero.

Para ver claves de idempotencia:

```text
SELECT 1
KEYS *
```

Las claves tienen prefijo relacionado con idempotencia y expiran por TTL.

## 18. Paso 15: probar duplicado de idempotencia

Repite exactamente el mismo `Producer` con:

```text
idempotency-header: producer-001
```

Resultado esperado:

- la llamada debe fallar;
- el broker debe rechazarla como duplicada.

Esto demuestra el objetivo de idempotencia.

Luego cambia a:

```text
idempotency-header: producer-002
```

La llamada debe volver a funcionar.

## 19. Paso 16: probar BrokerAPI streaming

La parte `BrokerAPI` requiere servicios suscriptores porque el broker hace llamadas outbound a cada subscriber URL.

Por eso no se prueba tan facilmente con una sola llamada `grpcurl`.

Hay tres formas de entenderla:

### Opcion A: usar pruebas de integracion

Ejecuta:

```bash
go test -race -count=1 -v ./tests/integration/broker_flow_test/...
```

Esto prueba:

- `ClientStream`;
- `ServerStream`;
- `BidirectionalStream`;
- peers simulados;
- flujo inbound y outbound.

Esta es la mejor forma de entender la parte streaming sin construir tus propios servicios suscriptores.

### Opcion B: leer los tests

Abre:

- `tests/integration/broker_flow_test/client_stream_flow_test.go`
- `tests/integration/broker_flow_test/server_stream_flow_test.go`
- `tests/integration/broker_flow_test/bidirectional_stream_flow_test.go`
- `tests/integration/broker_flow_test/helpers_test.go`

Estos archivos muestran como levantar peers y conectar el broker.

### Opcion C: crear servicios suscriptores manuales

Para una demo manual completa necesitas:

1. Un broker corriendo en `localhost:5000`.
2. Uno o mas servicios suscriptores que implementen `BrokerAPI`.
3. Un cliente que envie `StreamRequestMessage` con `subscribers`.

Esto es mas trabajo.
Para aprender primero, usa los tests de integracion.

## 20. Paso 17: probar con Terraform

Terraform levanta una pila local con:

- Dominus;
- Redis;
- Prometheus;
- Grafana;
- sidecar;
- red Docker;
- volumenes.

Desde:

```bash
cd Referance/dominus-broker
```

Windows PowerShell:

```powershell
.\Makefile.ps1 -Target terraform-init
.\Makefile.ps1 -Target terraform-plan
.\Makefile.ps1 -Target terraform-apply -TerraformAutoApprove
```

Ver outputs:

```powershell
.\Makefile.ps1 -Target terraform-output
```

Destruir:

```powershell
.\Makefile.ps1 -Target terraform-destroy -TerraformAutoApprove
```

Linux/macOS:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Nota:

El provider Docker esta documentado con host Windows por defecto.
En Linux/macOS puede requerir cambiar el host del provider a:

```text
unix:///var/run/docker.sock
```

## 21. Paso 18: entender los logs

El broker usa logs JSON por consola.

Busca campos como:

- `ID`
- `Description`
- `Op`

Estos campos ayudan a identificar:

- que operacion se ejecuto;
- que fallo;
- si paso por middleware;
- si llego a Redis;
- si hubo error gRPC.

## 22. Paso 19: fallos comunes

### `APP_CONFIG is empty or not set`

No definiste `APP_CONFIG`.

Solucion:

Vuelve al paso 8.

### Redis connection error

Redis no esta corriendo o la config de usuario/password no coincide.

Solucion:

Usa Redis sin auth y el `APP_CONFIG` de esta guia, o configura ACL correctamente.

### `failed to match token`

El header `x-api-key` no coincide.

Solucion:

Para gRPC usa:

```text
dominus-api-key-1233464687
```

Para REST usa:

```text
dominus_example_@10102024KeyServerToken
```

### `idempotency not found`

Puede significar dos cosas en este codigo:

- falta el header `idempotency-header`;
- la clave ya existia y fue tratada como duplicada.

Solucion:

Manda un header nuevo por cada llamada unary:

- `producer-002`
- `consumer-002`
- `ack-002`

### Consumer no devuelve mensaje

Puede ser que:

- no produjiste antes;
- ya consumiste y ackaste;
- el consumer group no tiene mensajes nuevos;
- Redis no tiene el stream esperado.

Solucion:

Ejecuta otro `Producer` con nueva idempotency key.

### Ack falla por message ID

El `messageId` debe tener formato Redis Stream:

```text
<numero>-<numero>
```

Ejemplo:

```text
1710000000000-0
```

Usa el `messageId` exacto que retorno `Consumer`.

## 23. Paso 20: que debes entender despues de probarlo

Al terminar estas pruebas debes poder explicar:

- como se levanta el broker;
- por que Redis es necesario;
- que diferencia hay entre `BrokerAPI` y `SqsAPI`;
- por que `Producer`, `Consumer` y `Ack` son unary;
- por que `BrokerAPI` usa streaming;
- que hace `idempotency-header`;
- que hace `x-api-key`;
- como Redis Streams representa el flujo asincrono;
- por que las pruebas de integracion son importantes;
- que partes estan listas para prototipo y que partes requieren hardening.

## 24. Orden recomendado de practica

Para aprender sin perderte:

1. Lee `proto/dominus.proto`.
2. Ejecuta `go test -race -count=1 ./tests/...`.
3. Levanta Redis.
4. Levanta el broker con `APP_CONFIG`.
5. Prueba `/health`.
6. Prueba `/metrics`.
7. Llama `SqsAPI.Producer`.
8. Llama `SqsAPI.Consumer`.
9. Llama `SqsAPI.Ack`.
10. Inspecciona Redis.
11. Ejecuta `tests/integration/broker_flow_test`.
12. Lee `internal/bootstraps/bootstraps.go`.
13. Lee `doc/tradeoffs.md`.

## 25. Conclusion

La forma mas clara de entender Dominus es probar primero la parte asincrona `SqsAPI`, porque requiere solo:

- broker;
- Redis;
- grpcurl.

La parte streaming `BrokerAPI` es mas compleja porque necesita servicios suscriptores.
Por eso, para defender el sistema, conviene entenderla primero desde:

- `proto/dominus.proto`;
- los use cases de broker;
- el outbound gRPC client;
- los tests de integracion.

Con esas pruebas puedes defender el sistema desde evidencia real:

- produce mensajes;
- consume mensajes;
- confirma mensajes;
- expone health;
- expone metricas;
- aplica API key;
- aplica idempotencia;
- prueba streaming con integracion.
