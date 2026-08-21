# Anexo 1

**Puesta en marcha de Dominus Broker**

## Objetivo y alcance

Este anexo explica cómo poner en marcha Dominus Broker en una infraestructura nueva. El procedimiento está dirigido a desarrolladores y cubre Windows y Linux. Incluye una ejecución local controlada, las comprobaciones funcionales y una ruta de despliegue con Docker y Terraform.

Dominus es un broker híbrido escrito en Go. Expone `BrokerAPI` para flujos gRPC en tiempo real y `SqsAPI` para operaciones de tipo cola sobre Redis Streams. El proceso también abre un monitor HTTP con los endpoints `/health` y `/metrics`.

La ruta principal de este anexo ejecuta Redis en Docker y el broker desde el código fuente. Esta separación permite detectar con claridad si un fallo pertenece a Redis, a la configuración o al proceso Go. El despliegue completo en contenedores se describe después.

## Topología de ejecución

La Figura 1 muestra los componentes necesarios para la puesta en marcha básica.

**Figura 1**

*Topología mínima de Dominus Broker*

```text
                         ┌────────────────────────────┐
                         │ Desarrollador o servicio  │
                         └─────────────┬──────────────┘
                                       │
                         HTTP :8000    │    gRPC :5000
                              ┌────────┴────────┐
                              │ Dominus Broker │
                              └────────┬────────┘
                                       │ Redis :6379
                              ┌────────┴────────┐
                              │ Redis Streams  │
                              │ DB 0: mensajes │
                              │ DB 1: claves   │
                              └─────────────────┘
```

*Nota.* `BrokerAPI` puede iniciar conexiones gRPC hacia servicios suscriptores. Esos servicios sólo son necesarios para probar manualmente los tres modos de streaming; no intervienen en la comprobación básica de `SqsAPI`.

## Requisitos previos

La Tabla 1 reúne las herramientas necesarias. Las versiones se deben comprobar en la terminal que se utilizará durante la instalación.

**Tabla 1**

*Herramientas para la puesta en marcha*

| Herramienta | Requisito | Uso |
|---|---|---|
| Git | Cliente con acceso a los repositorios de Dominus | Obtener el código y sus dependencias privadas |
| Go | `1.26.1` o una versión compatible con `go.mod` | Compilar, probar y ejecutar el broker |
| Docker Engine o Docker Desktop | Motor activo y accesible desde la terminal | Ejecutar Redis y, de forma opcional, el broker |
| PowerShell | 5.1 o posterior en Windows | Cargar la configuración y usar `Makefile.ps1` |
| Bash | Disponible en Linux | Cargar la configuración y ejecutar los comandos del sistema |
| `curl` | Cliente HTTP | Comprobar `/health` y `/metrics` |
| `grpcurl` | Recomendado | Consultar la reflexión gRPC y probar `SqsAPI` |
| Terraform | Opcional | Crear la pila Docker definida en `terraform/` |

Los siguientes comandos confirman que las herramientas principales están disponibles:

```text
git --version
go version
docker version
grpcurl --version
terraform version
```

`grpcurl` y Terraform son opcionales para el primer arranque. Sin `grpcurl` se puede validar gRPC mediante las pruebas de integración.

## Obtención del código

El directorio `Referance` contiene cuatro repositorios relacionados:

- `dominus-broker`, que ejecuta el servicio;
- `dominus-proto-definition`, que define los contratos gRPC;
- `dominus-sdk`, que facilita el consumo desde Go;
- `consumer-example`, que muestra un consumidor y un suscriptor.

En Linux, Git Bash o WSL se puede restaurar el conjunto con el script incluido. El comando se ejecuta desde la raíz del proyecto del TFM:

```bash
bash Referance/clone-dominus-deps.sh
```

En Windows sin Bash se clonan los repositorios con Git desde PowerShell:

```powershell
Set-Location Referance
git clone https://github.com/unir-broker-tfm/dominus-broker.git
git clone https://github.com/unir-broker-tfm/dominus-sdk.git
git clone https://github.com/unir-broker-tfm/consumer-example.git
git clone https://github.com/unir-broker-tfm/dominus-proto-definition.git
```

Si los directorios ya existen, no se vuelven a clonar. Se actualizan dentro de cada repositorio con `git pull --ff-only`, siempre que no haya cambios locales pendientes.

El broker depende de `github.com/MBI-88/dominus-proto-definition v1.3.7`. Si ese módulo es privado, la cuenta de Git debe tener permiso de lectura. La credencial se configura mediante el gestor aprobado por la organización; no debe guardarse en el repositorio, en un archivo `.tfvars` ni en una captura de terminal.

## Revisión inicial del repositorio

Los comandos de esta sección se ejecutan desde `Referance/dominus-broker`.

Windows:

```powershell
Set-Location Referance\dominus-broker
go env GOMOD
go mod download
```

Linux:

```bash
cd Referance/dominus-broker
go env GOMOD
go mod download
```

`go env GOMOD` debe devolver la ruta de `dominus-broker/go.mod`. Si `go mod download` informa que no encuentra `dominus-proto-definition`, se revisan las credenciales del repositorio privado antes de continuar.

## Preparación de Redis

El broker crea un consumer group durante el arranque y termina con error si no puede conectarse a Redis. Para que la configuración local coincida con el proyecto, Redis se construye con `terraform/dev/redis/Dockerfile`. Ese archivo utiliza Redis 7.2 y copia `redis.conf`, donde se define el usuario ACL `dominus`, la contraseña local de demostración `dominus` y dos bases lógicas.

Estas credenciales sólo se usan en un entorno local aislado. En una infraestructura compartida se deben cambiar en `redis.conf` y en el JSON del broker antes de crear las imágenes.

### Windows

Desde `Referance\dominus-broker`:

```powershell
docker build --tag dominus-redis:7.2 .\terraform\dev\redis
docker run --detach `
  --name redis `
  --publish 127.0.0.1:6379:6379 `
  dominus-redis:7.2
docker ps --filter "name=redis"
```

### Linux

Desde `Referance/dominus-broker`:

```bash
docker build --tag dominus-redis:7.2 ./terraform/dev/redis
docker run --detach \
  --name redis \
  --publish 127.0.0.1:6379:6379 \
  dominus-redis:7.2
docker ps --filter "name=redis"
```

El estado del contenedor debe ser `Up`. La conexión se comprueba sin publicar una contraseña nueva en el documento:

```text
docker exec redis redis-cli --user dominus --pass dominus PING
```

El resultado esperado es `PONG`. `redis-cli` puede mostrar una advertencia porque la contraseña aparece como argumento. Para una operación real se debe usar un mecanismo de secretos o la variable `REDISCLI_AUTH` durante la sesión.

Si el contenedor ya existe pero está detenido, se recupera con:

```text
docker start redis
```

## Configuración de Dominus Broker

El código actual no selecciona automáticamente `env.local.json` por medio del indicador `-prod`. `config.NewConfig()` lee el JSON completo desde la variable `APP_CONFIG` y detiene el proceso si la variable está vacía o si faltan los campos obligatorios.

La Tabla 2 resume los bloques de configuración.

**Tabla 2**

*Bloques de `APP_CONFIG`*

| Bloque | Campos principales | Función |
|---|---|---|
| `grpc_config` | `port`, `api_token` | Listener gRPC y secreto compartido |
| `rest_config` | `port`, `api_token`, `allow_origins` | Monitor HTTP, autenticación y CIDR permitido |
| `cert_config` | `key_file`, `ssl_ca_cert`, `ssl_cert` | Archivos usados para TLS |
| `redis_config` | host, puerto, credenciales, DB, stream y grupo | Redis Streams e idempotencia |
| `log_config` | `log_mode`, `log_url` | Salida de eventos del broker |

Para una ejecución local se parte de `env/template.json` y se guarda una copia fuera del repositorio. El siguiente contenido es un ejemplo funcional para el Redis creado en la sección anterior:

```json
{
  "grpc_config": {
    "port": 5000,
    "api_token": "cambie-esta-clave-grpc"
  },
  "rest_config": {
    "port": 8000,
    "api_token": "cambie-esta-clave-rest",
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
    "password": "dominus",
    "tls": false,
    "username": "dominus",
    "idem_potency_ex": 10,
    "stream_id": "consumer",
    "group_id": "consumer-group"
  },
  "log_config": {
    "log_mode": "cmd",
    "log_url": ""
  }
}
```

`0.0.0.0/0` permite cualquier IP en el middleware del monitor. Se mantiene para facilitar la práctica local, pero debe sustituirse por el CIDR de administración en una infraestructura compartida.

### Carga de la configuración en Windows

Desde `Referance\dominus-broker`:

```powershell
$configPath = Join-Path $env:TEMP 'dominus.runtime.json'
Copy-Item -LiteralPath '.\env\template.json' -Destination $configPath -Force
notepad $configPath
```

Se sustituye el contenido por el JSON anterior y se cambian las dos claves de ejemplo. Después se carga la variable:

```powershell
$env:APP_CONFIG = Get-Content -Raw -LiteralPath $configPath
$env:DOMINUS_GRPC_TOKEN = 'cambie-esta-clave-grpc'
$env:DOMINUS_REST_TOKEN = 'cambie-esta-clave-rest'
```

Los valores de `DOMINUS_GRPC_TOKEN` y `DOMINUS_REST_TOKEN` deben coincidir con el JSON, pero no forman parte de la configuración del broker; se usan en los comandos de comprobación.

### Carga de la configuración en Linux

Desde `Referance/dominus-broker`:

```bash
install -m 600 env/template.json /tmp/dominus.runtime.json
${EDITOR:-vi} /tmp/dominus.runtime.json
export APP_CONFIG="$(tr -d '\r\n' < /tmp/dominus.runtime.json)"
export DOMINUS_GRPC_TOKEN='cambie-esta-clave-grpc'
export DOMINUS_REST_TOKEN='cambie-esta-clave-rest'
```

Se sustituye el contenido del archivo por el JSON de ejemplo y se utilizan los mismos valores en las variables auxiliares.

## Pruebas automatizadas antes del arranque

Las pruebas detectan errores de compilación, integración y concurrencia antes de abrir los puertos del servicio. Desde la raíz de `dominus-broker` se ejecuta:

```text
go test -race -count=1 ./...
```

En Windows también está disponible el wrapper del proyecto:

```powershell
.\Makefile.ps1 -Target test
```

`-race` activa el detector de carreras de Go y `-count=1` evita reutilizar resultados almacenados. La ejecución correcta termina con `ok` en los paquetes de pruebas. Si sólo se desea revisar la parte de streaming:

```text
go test -race -count=1 -v ./tests/integration/broker_stream_flow_test/...
```

Estas pruebas crean peers controlados y ejercitan `ClientStream`, `ServerStream` y `BidirectionalStream` sin exigir servicios suscriptores externos.

## Ejecución del broker desde el código fuente

El broker se inicia desde `Referance/dominus-broker`, en la misma terminal donde se definió `APP_CONFIG`:

```text
go run ./cmd/api -banner=false
```

El indicador `-banner=false` sólo reduce la salida visual. No modifica la configuración.

Un arranque correcto muestra ambos listeners:

```text
Rest: http://0.0.0.0:8000
Grpc: 0.0.0.0:5000
```

En el ejemplo no existen certificados válidos en `./certs`, por lo que el monitor usa HTTP y gRPC acepta conexiones sin TLS. Este modo se limita al equipo local. Si Redis no está disponible, el constructor del cliente Redis produce un error y el broker no completa el arranque.

El proceso queda en primer plano. Las comprobaciones siguientes se ejecutan desde una segunda terminal.

## Validación del monitor HTTP

### Windows

```powershell
$headers = @{ 'x-api-key' = $env:DOMINUS_REST_TOKEN }
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/health' -Headers $headers
```

### Linux

```bash
curl --fail --silent --show-error \
  -H "x-api-key: ${DOMINUS_REST_TOKEN}" \
  http://127.0.0.1:8000/health
```

La respuesta esperada es:

```text
Health ok
```

El endpoint de métricas usa el mismo token.

Windows:

```powershell
Invoke-WebRequest `
  -Uri 'http://127.0.0.1:8000/metrics' `
  -Headers $headers | Select-Object -ExpandProperty Content
```

Linux:

```bash
curl --fail --silent --show-error \
  -H "x-api-key: ${DOMINUS_REST_TOKEN}" \
  http://127.0.0.1:8000/metrics
```

La salida contiene métricas Prometheus, entre ellas `cpu_usage_percentage`, `memory_usage_percentage` y contadores gRPC. Una llamada sin `x-api-key` o con un valor distinto debe ser rechazada.

## Validación de gRPC

Dominus registra la reflexión gRPC. Se puede consultar el contrato activo sin compilar un cliente.

### Windows

```powershell
grpcurl -plaintext `
  -H "x-api-key: $env:DOMINUS_GRPC_TOKEN" `
  127.0.0.1:5000 list
```

### Linux

```bash
grpcurl -plaintext \
  -H "x-api-key: ${DOMINUS_GRPC_TOKEN}" \
  127.0.0.1:5000 list
```

La lista debe contener:

```text
dominus.BrokerAPI
dominus.SqsAPI
grpc.reflection.v1.ServerReflection
```

`-plaintext` sólo corresponde al escenario local sin certificados. En una infraestructura con TLS se elimina ese indicador y se configura la CA y el nombre del servidor.

## Prueba del ciclo de mensajes

`SqsAPI` aplica `x-api-key` y exige `idempotency-header` en sus llamadas unary. Se debe usar una clave de idempotencia distinta para `Producer`, `Consumer` y `Ack`.

### Publicar un mensaje

El campo `payload` es de tipo `bytes`. En la representación JSON de gRPC se envía en Base64. El texto `hello dominus` corresponde a `aGVsbG8gZG9taW51cw==`.

Windows:

```powershell
$producerKey = "producer-$([guid]::NewGuid())"
grpcurl -plaintext `
  -H "x-api-key: $env:DOMINUS_GRPC_TOKEN" `
  -H "idempotency-header: $producerKey" `
  -d '{"payload":"aGVsbG8gZG9taW51cw=="}' `
  127.0.0.1:5000 dominus.SqsAPI/Producer
```

Linux:

```bash
producer_key="producer-$(date +%s%N)"
grpcurl -plaintext \
  -H "x-api-key: ${DOMINUS_GRPC_TOKEN}" \
  -H "idempotency-header: ${producer_key}" \
  -d '{"payload":"aGVsbG8gZG9taW51cw=="}' \
  127.0.0.1:5000 dominus.SqsAPI/Producer
```

La respuesta representa `status = 0`. Según las opciones de representación de `grpcurl`, un campo con el valor predeterminado puede aparecer como `"status": "0"` o como un objeto vacío. En ambos casos el comando debe terminar con código de salida cero.

### Consumir el mensaje

Windows:

```powershell
$consumerKey = "consumer-$([guid]::NewGuid())"
grpcurl -plaintext `
  -H "x-api-key: $env:DOMINUS_GRPC_TOKEN" `
  -H "idempotency-header: $consumerKey" `
  -d '{"workerId":"worker-1","groupId":"consumer-group"}' `
  127.0.0.1:5000 dominus.SqsAPI/Consumer
```

Linux:

```bash
consumer_key="consumer-$(date +%s%N)"
grpcurl -plaintext \
  -H "x-api-key: ${DOMINUS_GRPC_TOKEN}" \
  -H "idempotency-header: ${consumer_key}" \
  -d '{"workerId":"worker-1","groupId":"consumer-group"}' \
  127.0.0.1:5000 dominus.SqsAPI/Consumer
```

La respuesta contiene `messageId`, `date` y `message`. Se copia el valor exacto de `messageId`; su formato es similar a `1710000000000-0`.

### Confirmar el procesamiento

Se sustituye `<MESSAGE_ID>` por el identificador obtenido en el paso anterior.

Windows:

```powershell
$ackKey = "ack-$([guid]::NewGuid())"
$messageId = '<MESSAGE_ID>'
grpcurl -plaintext `
  -H "x-api-key: $env:DOMINUS_GRPC_TOKEN" `
  -H "idempotency-header: $ackKey" `
  -d "{`"workerId`":`"worker-1`",`"groupId`":`"consumer-group`",`"messageId`":`"$messageId`"}" `
  127.0.0.1:5000 dominus.SqsAPI/Ack
```

Linux:

```bash
ack_key="ack-$(date +%s%N)"
message_id='<MESSAGE_ID>'
grpcurl -plaintext \
  -H "x-api-key: ${DOMINUS_GRPC_TOKEN}" \
  -H "idempotency-header: ${ack_key}" \
  -d "{\"workerId\":\"worker-1\",\"groupId\":\"consumer-group\",\"messageId\":\"${message_id}\"}" \
  127.0.0.1:5000 dominus.SqsAPI/Ack
```

La respuesta devuelve el mismo `messageId` y una fecha de confirmación. Con esto se comprueba el recorrido `Producer` → Redis Stream → `Consumer` → `Ack`.

Para observar el estado directamente en Redis:

```text
docker exec redis redis-cli --user dominus --pass dominus XINFO STREAM consumer
docker exec redis redis-cli --user dominus --pass dominus XINFO GROUPS consumer
docker exec redis redis-cli --user dominus --pass dominus XPENDING consumer consumer-group
```

Después del `Ack`, el mensaje no debe permanecer pendiente para el grupo. Las claves de idempotencia se guardan en la DB 1 con un TTL definido por `idem_potency_ex`.

## Despliegue completo con Docker

Esta ruta ejecuta el broker y Redis en la misma red Docker. El `Dockerfile` del broker compila para Linux, copia `env/` y utiliza `env/entrypoint.sh` para cargar `APP_CONFIG` desde `env.prod.json`.

Hay tres condiciones previas:

1. el build necesita acceso de lectura a `dominus-proto-definition`;
2. el contexto debe contener el directorio `certs` porque el `Dockerfile` lo copia;
3. la configuración del contenedor debe usar `redis` como host, no `localhost`.

Para no hornear secretos en la imagen, se prepara un JSON externo y se monta sobre `/app/env/env.prod.json`. Debe tener estos cambios respecto al ejemplo local:

```json
{
  "cert_config": {
    "key_file": "/etc/dominus/certs/cert.key",
    "ssl_ca_cert": "/etc/dominus/certs/ca_cert.pem",
    "ssl_cert": "/etc/dominus/certs/cert.pem"
  },
  "redis_config": {
    "host": "redis"
  }
}
```

El archivo real debe conservar todos los bloques del JSON completo; el fragmento anterior sólo muestra los campos que cambian.

### Construcción en Windows

Desde `Referance\dominus-broker`:

```powershell
New-Item -ItemType Directory -Force -Path '.\certs' | Out-Null
$secureToken = Read-Host 'Token de lectura de GitHub' -AsSecureString
$credential = New-Object System.Net.NetworkCredential('', $secureToken)
$env:GITHUB_TOKEN = $credential.Password
docker build `
  --build-arg "GITHUB_TOKEN=$env:GITHUB_TOKEN" `
  --tag dominus-broker:local .
Remove-Item Env:GITHUB_TOKEN
```

### Construcción en Linux

Desde `Referance/dominus-broker`:

```bash
mkdir -p certs
read -rsp 'Token de lectura de GitHub: ' GITHUB_TOKEN
echo
docker build \
  --build-arg GITHUB_TOKEN="${GITHUB_TOKEN}" \
  --tag dominus-broker:local .
unset GITHUB_TOKEN
```

El `Dockerfile` actual recibe el token como build argument. Se debe evitar la salida detallada del build en evidencias académicas. Para un pipeline real conviene sustituir ese mecanismo por un secreto de BuildKit y comprobar que la credencial no quede en capas ni metadatos.

### Creación de la red y los contenedores

Los siguientes comandos son iguales en PowerShell y Bash:

```text
docker network create dominus
docker build --tag dominus-redis:7.2 ./terraform/dev/redis
docker run --detach --name redis --network dominus dominus-redis:7.2
```

Si ya se creó el contenedor Redis de la ruta local, se puede detener y retirar antes de iniciar esta variante:

```text
docker stop redis
docker rm redis
```

En Linux, suponiendo que el JSON completo se guardó en `/tmp/dominus.container.json`:

```bash
docker run --detach \
  --name dominus-broker \
  --network dominus \
  --publish 5000:5000 \
  --publish 8000:8000 \
  --env MODE=prod \
  --mount type=bind,source=/tmp/dominus.container.json,target=/app/env/env.prod.json,readonly \
  dominus-broker:local
```

En Windows se crea una copia específica para el contenedor. Debe conservar el JSON completo, usar `redis` como host y utilizar las rutas de certificados bajo `/etc/dominus/certs`:

```powershell
$containerConfigPath = Join-Path $env:TEMP 'dominus.container.json'
Copy-Item -LiteralPath $configPath -Destination $containerConfigPath -Force
notepad $containerConfigPath
```

Después de guardar esos cambios, se monta la copia en modo de sólo lectura:

```powershell
docker run --detach `
  --name dominus-broker `
  --network dominus `
  --publish 5000:5000 `
  --publish 8000:8000 `
  --env MODE=prod `
  --mount "type=bind,source=$containerConfigPath,target=/app/env/env.prod.json,readonly" `
  dominus-broker:local
```

El estado y los logs se revisan con:

```text
docker ps --filter "name=dominus-broker"
docker logs dominus-broker
```

La salida debe indicar `MODE=prod`, confirmar que encontró el archivo y anunciar los puertos 8000 y 5000. Las comprobaciones HTTP y gRPC se repiten con los tokens del JSON montado.

## Infraestructura con Terraform

El directorio `terraform/` crea una red Docker y módulos para Dominus, Redis, Nginx sidecar, Prometheus y Grafana. Esta ruta es útil para reconstruir el entorno completo, pero requiere configuración previa.

No hay un archivo `.tfvars` versionado y las variables raíz no tienen valores predeterminados. Se crea `terraform/terraform.tfvars`, que ya coincide con el patrón ignorado por Git:

```hcl
dominus_server_file             = ".."
dominus_server_container_cpu    = "2"
dominus_server_container_memory = 1024

dominus_server_container_ports = [
  { internal = 5000, external = 5000 },
  { internal = 8000, external = 8000 }
]

redis_server_container_ports = [
  { internal = 6379, external = 6379 }
]

prometheus_server_container_ports = [
  { internal = 9090, external = 9090 }
]

grafana_server_container_ports = [
  { internal = 3000, external = 3000 }
]

sidecar_server_container_ports = [
  { internal = 80, external = 80 }
]

network_driver = "bridge"
network_name   = "dominus"
```

El token privado se pasa como variable de entorno y no se escribe en `terraform.tfvars`.

Antes de ejecutar Terraform en Linux, se cambia el proveedor de `terraform/terraform.tf` porque el archivo versionado apunta al named pipe de Windows:

```hcl
provider "docker" {
  host = "unix:///var/run/docker.sock"
}
```

Windows:

```powershell
$env:TF_VAR_dominus_server_token = '<TOKEN_DE_LECTURA>'
.\Makefile.ps1 -Target terraform-init
.\Makefile.ps1 -Target terraform-validate
.\Makefile.ps1 -Target terraform-plan
.\Makefile.ps1 -Target terraform-apply
Remove-Item Env:TF_VAR_dominus_server_token
```

Linux:

```bash
export TF_VAR_dominus_server_token='<TOKEN_DE_LECTURA>'
cd terraform
terraform init
terraform validate
terraform plan
terraform apply
unset TF_VAR_dominus_server_token
```

En Windows, `terraform/terraform.tf` ya apunta a `npipe:////.//pipe//docker_engine` y no requiere ese cambio.

La configuración Terraform actual construye el broker con el `env.prod.json` incluido en la imagen y no monta un archivo externo. Su health check y el sidecar Nginx también contienen un token de ejemplo que debe coincidir con `rest_config.api_token`; si no coincide, Dominus puede arrancar pero aparecer como `unhealthy` y Prometheus no podrá leer `/metrics`. Antes de usar esta ruta se deben parametrizar esos valores y adaptar `terraform/dev/dominus/main.tf` para montar la configuración y los certificados desde un almacén seguro. También se debe retirar la publicación de `6379`; Redis sólo necesita ser accesible dentro de la red Docker.

Los recursos creados se consultan con:

```text
terraform output
docker ps
```

En Windows puede usarse `./Makefile.ps1 -Target terraform-output`. La eliminación de esta infraestructura se realiza desde el mismo directorio con `terraform destroy`, después de revisar el plan de destrucción.

## TLS y límites operativos

El bootstrap comprueba la existencia del certificado, la clave y la CA. Cuando los tres archivos están disponibles, gRPC y el monitor se inician con TLS. Si falta alguno, el proceso continúa con gRPC inseguro y HTTP. Esta conducta facilita el desarrollo local, pero no debe interpretarse como un modo seguro de producción.

Para un despliegue conectado a otra red se deben cumplir estas condiciones:

- montar certificados válidos en las rutas de `cert_config`;
- comprobar el nombre incluido en el certificado desde los clientes;
- restringir `allow_origins` al CIDR administrativo;
- no publicar Redis al exterior;
- conservar los tokens en un gestor de secretos;
- usar tokens distintos para gRPC y el monitor;
- fijar límites de red y recursos para los streams.

Las evidencias del proyecto registran un límite gRPC cercano a 4 MiB por mensaje. Un payload en el borde puede superar el límite debido al framing de protobuf. La puesta en marcha debe probar los tamaños reales de la aplicación, no asumir que cualquier payload será aceptado.

`SqsAPI` incluye `Ack` y claves de idempotencia con TTL. Estos mecanismos reducen duplicados, pero el despliegue no debe anunciar una garantía absoluta de *exactly-once*. Los reintentos, la reserva de claves y el tratamiento de mensajes pendientes necesitan una política explícita en la aplicación consumidora.

## Solución de problemas

**Tabla 3**

*Diagnóstico de fallos frecuentes*

| Síntoma | Causa probable | Comprobación y corrección |
|---|---|---|
| `APP_CONFIG is empty or not set` | La variable no existe en esa terminal | Volver a cargar el JSON y ejecutar el broker en la misma sesión |
| `RedisConfig.Host empty` o `RedisConfig.Port empty` | JSON incompleto o clave con nombre incorrecto | Comparar el archivo con `config/config.go` y mantener `redis_config` en la raíz |
| Error `WRONGPASS` o autenticación Redis | Usuario y contraseña no coinciden con `redis.conf` | Comprobar `dominus`/`dominus` en local o actualizar ambos archivos |
| `connection refused` en `6379` | Redis está detenido o el host es incorrecto | Ejecutar `docker ps`; usar `localhost` desde el host y `redis` desde la red Docker |
| `failed to match token` | Se usó un token incorrecto | Distinguir `grpc_config.api_token` de `rest_config.api_token` |
| `idempotency not found` | Falta `idempotency-header` | Añadir una clave no vacía a cada llamada unary |
| `rate limit reached` | La clave de idempotencia ya fue utilizada | Generar una clave nueva o esperar el TTL configurado |
| `invalid message id` | `Ack` no recibió el ID exacto de Redis Stream | Copiar `messageId` de la respuesta de `Consumer` |
| `ResourceExhausted` | El mensaje supera el límite gRPC | Reducir el payload o configurar límites coordinados en cliente y servidor |
| Fallo al descargar `dominus-proto-definition` | Falta acceso al módulo privado | Revisar la autenticación Git sin imprimir el token |
| El build Docker falla al copiar `certs` | El directorio no está en el contexto | Crear `certs/` o proporcionar los certificados antes del build |
| Terraform solicita variables | No existe `terraform.tfvars` | Crear el archivo local mostrado y pasar el token mediante `TF_VAR_...` |
| Terraform no conecta con Docker en Linux | El proveedor usa el named pipe de Windows | Cambiar `host` a `unix:///var/run/docker.sock` |

## Detención y limpieza

El broker ejecutado con `go run` se detiene con `Ctrl+C`. Después se eliminan las variables de la sesión.

Windows:

```powershell
Remove-Item Env:APP_CONFIG -ErrorAction SilentlyContinue
Remove-Item Env:DOMINUS_GRPC_TOKEN -ErrorAction SilentlyContinue
Remove-Item Env:DOMINUS_REST_TOKEN -ErrorAction SilentlyContinue
```

Linux:

```bash
unset APP_CONFIG DOMINUS_GRPC_TOKEN DOMINUS_REST_TOKEN
```

Los contenedores locales se detienen y retiran por nombre:

```text
docker stop dominus-broker redis
docker rm dominus-broker redis
```

Si sólo se ejecutó Redis, se aplica el comando únicamente a `redis`. Las imágenes y volúmenes no se eliminan automáticamente porque pueden reutilizarse. Terraform mantiene su propio estado y sus recursos se retiran con `terraform destroy` desde `terraform/`.

## Criterios de aceptación

La instalación se considera operativa cuando se cumplen todos los puntos siguientes:

- Redis responde `PONG` con el usuario configurado.
- Dominus arranca sin `panic` y mantiene abiertos los puertos 5000 y 8000.
- `/health` responde `Health ok` con un token válido.
- `/health` y `/metrics` rechazan un token incorrecto.
- La reflexión gRPC muestra `dominus.BrokerAPI` y `dominus.SqsAPI`.
- `Producer` publica un payload no vacío.
- `Consumer` devuelve el mensaje y un `messageId` válido.
- `Ack` confirma ese mismo identificador.
- Las pruebas con `-race -count=1` terminan sin fallos.
- No se han guardado tokens ni contraseñas reales en el repositorio o en las evidencias.

El cumplimiento de estos criterios demuestra que el broker, Redis, la autenticación y el flujo asíncrono básico funcionan como una unidad. La validación de rendimiento, tolerancia a fallos y streams con suscriptores reales requiere un entorno de pruebas posterior.
