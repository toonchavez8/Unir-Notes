# Reporte de análisis de ciberseguridad de Dominus

## 1. Propósito y alcance

Este reporte documenta seis pruebas reproducibles de seguridad: tres sobre `dominus-broker` y tres sobre `dominus-sdk`. La selección se hizo a partir de la guía de la actividad y de los resultados conservados en `Referance/security-evidence`. No se pretende afirmar que todo el sistema sea seguro o inseguro. El alcance es más concreto: describir qué se probó, qué ocurrió en el laboratorio, dónde se encuentra el comportamiento en el código y cómo verificar una corrección.

`dominus-broker` es el backend escrito en Go. Expone una interfaz de programación de aplicaciones basada en gRPC, endpoints HTTP de salud y métricas, y utiliza Redis para memoria e idempotencia. `dominus-sdk` es la interfaz que consumen las aplicaciones cliente. Dominus no tiene una interfaz gráfica, por lo que las pruebas habituales de navegador, como Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF) o seguridad de cookies, no corresponden a esta arquitectura.

Las abreviaciones utilizadas son: SDK, *Software Development Kit*; TLS, *Transport Layer Security*; CA, *Certification Authority*; SAN, *Subject Alternative Name*; y SSRF, *Server-Side Request Forgery*. Una clave de idempotencia identifica una operación para que un reintento o una ejecución concurrente no produzca el mismo efecto más de una vez.

## 2. Casos seleccionados

| Componente | Prueba | Hallazgo o resultado principal | Estado |
|---|---|---|---|
| Backend | BE-01. Autenticación gRPC | La ausencia de `x-api-key` puede terminar el proceso. | Fallida, severidad alta |
| Backend | BE-03. Idempotencia concurrente | Varias solicitudes con la misma clave son aceptadas. | Fallida, severidad alta |
| Backend | BE-06. TLS efectivo | El laboratorio opera por HTTP y gRPC sin TLS. | Fallida, severidad alta en una red no confiable |
| SDK | CL-01. Validación TLS | La CA y el SAN se verifican, pero los errores se expresan mediante `panic`. | Control efectivo con defecto de manejo de errores |
| SDK | CL-03. Destinos | Se acepta `hostname.test/path` y no existe una allowlist separada. | Fallida, severidad media |
| SDK | CL-05. Serialización | El error de `json.Marshal` se descarta y se envía un payload vacío. | Fallida, severidad media |

## 3. Entorno evaluado

La ejecución se realizó el 10 de agosto de 2026 en un laboratorio local con Docker. Los hashes corresponden al código base identificado en `HEAD`; los tests de seguridad añadidos al directorio de trabajo también forman parte de la reproducción.

| Elemento | Versión o referencia |
|---|---|
| `dominus-broker` | rama `master`, commit `cf186ee1f6b461ecc50b51167c3bd3f22895b02e` |
| `dominus-sdk` | rama `master`, commit `a1703e393f13609bbca13721ae2b4884c762703c` |
| Go declarado por ambos módulos | 1.26.1 |
| Go observado por las herramientas | 1.26.5 |
| gRPC del broker | 1.79.3 |
| gRPC del SDK | 1.79.1 |
| Imagen | `dominus-broker:security-lab` |
| Servicios locales | gRPC `127.0.0.1:5000`, HTTP `127.0.0.1:8000`, Redis `127.0.0.1:6379` |

La variable `DOMINUS_TEST_TOKEN` representa una credencial desechable. El valor real no se repite en este documento.

```bash
EVIDENCE="$PWD/Referance/security-evidence"
export DOMINUS_TEST_TOKEN='<token-desechable-del-laboratorio>'

docker image ls dominus-broker:security-lab
docker ps --filter "name=redis" --filter "name=dominus-broker-lab"
docker logs --tail=200 dominus-broker-lab 2>&1 \
  | tee "$EVIDENCE/E21-broker-startup.txt"
```

El arranque guardado en `E21-broker-startup.txt` confirmó que el broker escuchaba en `0.0.0.0:8000` y `0.0.0.0:5000` antes de las pruebas.

## 4. Hallazgos del backend

### 4.1. BE-01: autenticación gRPC ante token ausente

#### Objetivo

Comprobar que el interceptor de autenticación rechaza una llamada gRPC cuando falta `x-api-key`, sin cerrar el servidor. También se compararon un token incorrecto y uno correcto para separar un fallo en la validación de un fallo causado por la ausencia del encabezado.

La ruta utilizada por `grpcurl list` es el stream de reflexión `/grpc.reflection.v1.ServerReflection/ServerReflectionInfo`. El mismo interceptor `ApiToken` se instala para las llamadas gRPC de streaming en `internal/bootstraps/bootstraps.go:99-103`. Por eso el defecto no está limitado a una ruta HTTP ni a una función llamada “Broker API”.

#### Riesgo

El código lee la posición cero del arreglo que devuelve `metadata.Get` sin comprobar su longitud. Cuando la metadata existe pero no contiene el encabezado, Go produce `index out of range`. El proceso termina y el servicio deja de atender HTTP y gRPC. Este patrón corresponde a una validación incorrecta de índice y puede afectar la disponibilidad (MITRE, 2026a).

#### Versión

`dominus-broker` en el commit `cf186ee1f6b461ecc50b51167c3bd3f22895b02e`, construido como `dominus-broker:security-lab`, con gRPC 1.79.3.

#### Preparación

Se comprobó que el contenedor estaba activo y que `/health` respondía antes del caso negativo. Como el endpoint HTTP también requiere token, la línea base se tomó con la credencial de laboratorio.

```bash
curl -i \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  http://127.0.0.1:8000/health \
  2>&1 | tee "$EVIDENCE/E22-BE01-health-before.txt"
```

#### Comando sin token

```bash
grpcurl -plaintext \
  127.0.0.1:5000 list \
  2>&1 | tee "$EVIDENCE/E23-BE01-no-token.txt"
```

#### Comando con token incorrecto

```bash
grpcurl -plaintext \
  -H 'x-api-key: token-invalido-de-laboratorio' \
  127.0.0.1:5000 list \
  2>&1 | tee "$EVIDENCE/E25-BE01-invalid-token.txt"
```

#### Comando con token correcto

```bash
grpcurl -plaintext \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  127.0.0.1:5000 list \
  2>&1 | tee "$EVIDENCE/E26-BE01-valid-token.txt"
```

#### Comprobación del proceso

```bash
curl -i http://127.0.0.1:8000/health \
  2>&1 | tee "$EVIDENCE/E24-BE01-health-after-no-token.txt"

docker ps --filter "name=dominus-broker-lab"
docker logs --tail=200 dominus-broker-lab
```

#### Resultado esperado

Sin token y con token incorrecto se esperaba `Unauthenticated`; con el token correcto, el listado de servicios. El proceso debía permanecer activo en los tres casos.

#### Resultado real

El token incorrecto produjo `Unauthenticated` y el correcto permitió enumerar `dominus.BrokerAPI` y `dominus.SqsAPI`. En la ejecución sin token, el log del contenedor registró un `panic`. La comprobación posterior de `/health` no pudo establecer conexión. Una repetición de `E23-BE01-no-token.txt`, realizada cuando el contenedor ya estaba detenido, registró “connection refused”; por eso el `panic` se demuestra con el log de arranque y la indisponibilidad se corrobora con el health check.

#### Evidencia

```text
Archivo: E21-broker-startup.txt
panic: runtime error: index out of range [0] with length 0
dominus-broker/internal/infrastructure/grpc/middlewares.(*middlewares).ApiToken
    /app/internal/infrastructure/grpc/middlewares/middlewares.go:48

Archivo: E24-BE01-health-after-no-token.txt
curl: (7) Failed to connect to 127.0.0.1:8000

Archivo: E25-BE01-invalid-token.txt
code = Unauthenticated desc = failed to match token

Archivo: E26-BE01-valid-token.txt
dominus.BrokerAPI
dominus.SqsAPI
grpc.reflection.v1.ServerReflection
```

El origen está en `Referance/dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go:48`:

```go
token := md.Get(enum.X_API_KEY)[0]
```

#### Recomendación

Guardar el resultado de `md.Get`, comprobar `len(values) == 0` y devolver `codes.Unauthenticated` antes de acceder al primer elemento. La corrección debe cubrir tanto el interceptor unary como el de stream, porque ambos llaman a `ApiToken`.

#### Regresión

Agregar `TestApiTokenMissingHeaderReturnsUnauthenticated`. La prueba debe construir metadata sin `x-api-key`, invocar `ApiToken`, verificar `codes.Unauthenticated` y realizar una segunda llamada válida para demostrar que el servidor sigue activo. Después se debe repetir el comando de `grpcurl` y ejecutar `go test -race ./...`.

### 4.2. BE-03: idempotencia bajo concurrencia

#### Objetivo

Verificar que veinte solicitudes simultáneas con una misma clave de idempotencia no ejecuten la operación más de una vez. Esta propiedad se usa en las operaciones unary de `dominus.SqsAPI`, como `/dominus.SqsAPI/Producer`, `/dominus.SqsAPI/Consumer` y `/dominus.SqsAPI/Ack`, porque `IdemPotency` forma parte de `ChainUnaryInterceptor` en `internal/bootstraps/bootstraps.go:93-98`.

#### Riesgo

Un cliente puede reintentar una operación cuando pierde la respuesta o alcanza un timeout. Si la comprobación y la reserva de la clave ocurren por separado, dos solicitudes pueden atravesar el middleware antes de que Redis registre alguna. El efecto puede ser una publicación, consumo o confirmación duplicada. El detector `-race` de Go identifica accesos incompatibles a memoria durante la ejecución, pero no demuestra que una secuencia distribuida sea atómica (The Go Team, s. f.).

#### Versión

`dominus-broker` en el mismo commit e imagen de BE-01. La prueba está en `Referance/dominus-broker/tests/security/idempotency_security_test.go` y usa `miniredis` 2.37.0.

#### Preparación

El test inicia Redis efímero, crea una sola clave por ronda, sincroniza veinte goroutines y repite el experimento veinte veces. Invoca directamente `IdemPotency`; así aísla la propiedad de idempotencia de la autenticación y del transporte.

#### Comandos sin token, con token incorrecto y con token correcto

No aplican a esta prueba aislada. El test no abre una ruta gRPC ni ejecuta `ApiToken`; construye un contexto con `idempotency-header` y llama al middleware directamente. Introducir casos de token aquí mezclaría dos controles distintos. La autenticación ya se examinó en BE-01.

#### Comando ejecutado

```bash
cd Referance/dominus-broker
CGO_ENABLED=1 go test -race -count=20 ./tests/security \
  2>&1 | tee ../security-evidence/E31-BE03-idempotencia.txt
```

#### Comprobación del proceso

La prueba no usa el contenedor del broker. El proceso observado es `go test`, que concluye y devuelve `FAIL` porque la invariante “exactamente una aceptación” no se cumple. Esto evita interpretar una caída del contenedor como parte de BE-03.

#### Resultado esperado

Cada ronda debía registrar una aceptación y diecinueve duplicados. No se esperaba un reporte de carrera de datos.

#### Resultado real

Todas las rondas aceptaron más de una solicitud. El mínimo observado fue 3 de 20 y el máximo 20 de 20. Las solicitudes rechazadas recibieron `Aborted: rate limit reached`, un mensaje que tampoco distingue un duplicado de un límite de tasa. No apareció un reporte `WARNING: DATA RACE`; el hallazgo es una carrera lógica reproducible.

#### Evidencia

```text
Archivo: E31-BE03-idempotencia.txt
round 0: accepted 4 of 20 concurrent requests with one idempotency key; want exactly 1
round 1: accepted 12 of 20 concurrent requests with one idempotency key; want exactly 1
round 4: accepted 3 of 20 concurrent requests with one idempotency key; want exactly 1
round 6: accepted 20 of 20 concurrent requests with one idempotency key; want exactly 1
rpc error: code = Aborted desc = rate limit reached
```

La ventana de carrera se encuentra en `middlewares.go:101-110`: primero consulta Redis y después inicia el guardado en otra goroutine.

```go
if ok := m.ch.CheckConsumer(ctx, keys[0]); ok {
    return nil, status.Error(codes.Aborted, enum.RATE_LIMIT_REACHED)
}

go func(key string) {
    _ = m.ch.SaveConsumer(ctx, key)
}(keys[0])
```

`SaveConsumer` ya usa `NX` y expiración en `redis/cchecker/outbound.go:54-60`, pero el middleware no utiliza el resultado de esa operación para decidir cuál solicitud puede continuar. Redis define `NX` como “guardar solo si la clave no existe”; la respuesta de esa única operación debe ser la decisión de aceptación (Redis Ltd., s. f.).

#### Recomendación

Eliminar la secuencia `CheckConsumer` seguida de un guardado asíncrono. `SaveConsumer` debe ejecutarse de forma síncrona y devolver tres estados distinguibles: clave reservada, clave existente y error de Redis. Solo la solicitud que reserva la clave puede llegar al handler. Para una clave existente se recomienda un código de duplicado documentado, no `rate limit reached`.

#### Regresión

Conservar `TestIdempotencyUnderConcurrency`, pero hacer que falle ante cualquier conteo distinto de uno. Ejecutarlo con `go test -race -count=20 ./tests/security`. También se debe agregar una prueba que simule un error de Redis y confirme la política elegida, sin imprimir usuario ni contraseña.

### 4.3. BE-06: TLS y degradación a texto plano

#### Objetivo

Comprobar el transporte efectivo de los listeners gRPC y HTTP. La revisión debía distinguir entre archivos de configuración y comportamiento real: una referencia a TLS en el código no demuestra que el proceso iniciado esté cifrando el tráfico.

#### Riesgo

El token en `x-api-key` autentica al cliente, pero no cifra la comunicación. gRPC recomienda combinar credenciales de llamada con credenciales de canal TLS para autenticar al servidor y proteger los datos intercambiados (gRPC Authors, 2024). Si el broker escucha en texto plano, un actor con visibilidad de red puede observar el token y los mensajes.

#### Versión

`dominus-broker` en el commit e imagen descritos en la sección 3. La configuración observada contiene `tls: false` para Redis y la imagen no tenía certificados disponibles en `/etc/dominus/certs`.

#### Preparación

Se reinició el broker después de BE-01 y se confirmó el puerto 5000. Se revisó la configuración y después se comparó una conexión plaintext con intentos TLS reales.

```bash
grep -RniE 'tls|plaintext|insecure|certificate|ca' . --exclude-dir=.git \
  | tee "$EVIDENCE/E32-BE06-tls-config.txt"
```

#### Comando sin token

```bash
curl -i http://127.0.0.1:8000/health
```

La respuesta `403 Forbidden` demuestra que el listener HTTP está activo en plaintext y que la autenticación sigue operando; no demuestra confidencialidad.

#### Comando con token incorrecto

```bash
curl -i \
  -H 'x-api-key: token-invalido' \
  http://127.0.0.1:8000/health
```

El resultado fue `403 Forbidden`. Este caso confirma autenticación, pero el encabezado viaja por HTTP.

#### Comando con token correcto

```bash
grpcurl -plaintext \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  127.0.0.1:5000 list
```

El listado de servicios fue exitoso por un canal sin TLS.

#### Comprobación de TLS y del proceso

```bash
grpcurl -insecure \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  127.0.0.1:5000 list

curl -k -i \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  https://127.0.0.1:8000/health

docker ps --filter "name=dominus-broker-lab"
```

#### Resultado esperado

En modo de producción se esperaba que una CA y un nombre válidos permitieran la conexión, y que una CA incorrecta, un nombre incorrecto o la ausencia del certificado impidieran el arranque o la conexión. El servicio no debía cambiar automáticamente a plaintext.

#### Resultado real

`grpcurl -plaintext` enumeró los servicios. `grpcurl -insecure`, que todavía espera TLS aunque omite la verificación de confianza, recibió bytes que no correspondían a un handshake. HTTPS también falló. El broker continuó activo porque había arrancado intencionalmente con listeners sin TLS. Los escenarios de CA válida, CA incorrecta y SAN incorrecto no pudieron ejecutarse contra esta imagen; no había certificado de servidor. La conclusión comprobada es la degradación a texto plano, no una evaluación completa de la cadena de certificados del broker.

#### Evidencia

```text
Archivo: E32-BE06-transport.txt
--- plaintext gRPC ---
dominus.BrokerAPI
dominus.SqsAPI

--- TLS with insecure verification ---
tls: first record does not look like a TLS handshake

--- HTTPS monitor ---
TLS connect error

--- HTTP monitor ---
HTTP/1.1 403 Forbidden
failed to match token
```

La degradación está implementada en `Referance/dominus-broker/internal/bootstraps/bootstraps.go:73-89` para gRPC y `:207-216` para HTTP. Si los archivos no están disponibles, se añaden credenciales inseguras y se llama a `ListenAndServe`:

```go
} else {
    optsD = append(optsD, grpc.WithTransportCredentials(insecure.NewCredentials()))
}

} else {
    log.Fatal(r.ListenAndServe(fmt.Sprintf("0.0.0.0:%d", port)))
}
```

#### Recomendación

En `MODE=prod`, la ausencia de certificado, clave o CA debe impedir el arranque. Los listeners deben usar TLS 1.2 o posterior, cargar una CA confiable y verificar el nombre del servidor. Un modo plaintext puede conservarse para desarrollo, pero debe ser explícito, estar separado de producción y limitarse a loopback.

#### Regresión

Crear una prueba de arranque con cuatro escenarios: CA y SAN válidos, CA incorrecta, SAN incorrecto y certificados ausentes. El último caso debe devolver un error antes de abrir los puertos. Después se deben repetir `grpcurl` y `curl` sin opciones que desactiven la verificación.

## 5. Hallazgos del SDK

### 5.1. CL-01: validación del certificado TLS

#### Objetivo

Verificar que `dominus-sdk` autentica al servidor antes de crear un stream. La prueba cubre la cadena de confianza y el nombre del servidor. También observa cómo la API del SDK comunica un error de configuración.

La llamada evaluada es `NewBrokerConfig(...).InitAPIClientsTLSFromFile(...)`, seguida de `UseStreamServerConn()`. Esta última abre la ruta gRPC `/dominus.BrokerAPI/ServerStream` mediante `broker_client_conn.go:33-42`.

#### Versión y preparación

Se evaluó `dominus-sdk` en el commit `a1703e393f13609bbca13721ae2b4884c762703c`, con Go 1.26.1 y gRPC 1.79.1. `TestTLS` levantó un servidor gRPC en `127.0.0.1` con un puerto efímero. Los archivos se guardaron en `t.TempDir()` con permisos `0600` y se eliminaron al terminar el test.

#### Certificado utilizado

Se generó un certificado RSA de 2048 bits válido durante una hora y con uso extendido `ServerAuth`. No se utilizó un certificado de producción ni se copió la clave privada a la evidencia.

#### CA

La CA efímera usa el nombre `Dominus SDK Test CA`. Para el caso válido, firma el certificado del servidor. En el caso negativo se genera una segunda CA independiente; el cliente debe rechazar el certificado porque su firma no pertenece a la raíz configurada.

#### SAN y `serverName`

El certificado contiene el nombre DNS `localhost` y la dirección IP `127.0.0.1` como valores SAN. El caso válido configura `serverName="localhost"`; el caso negativo usa `wrong.test`.

#### Comando

```bash
cd Referance/dominus-sdk
go test -v ./dominus/security -run TestTLS \
  2>&1 | tee ../security-evidence/E34-CL01-tls.txt
```

#### Resultado esperado

La CA válida y el SAN correcto debían permitir la creación del stream. Una CA distinta y un `serverName` que no aparece en el SAN debían ser rechazados. Una ruta de CA inexistente debía producir un error de inicialización controlado.

#### Resultado real

La verificación criptográfica funcionó: el caso válido tuvo éxito y los dos casos de confianza incorrecta fueron rechazados. La CA inexistente también impidió la inicialización. Sin embargo, los casos negativos se comunicaron mediante `panic`. El test aparece como `PASS` porque captura ese `panic` y confirma el rechazo esperado; esto no significa que la API de manejo de errores sea adecuada.

#### Evidencia

```text
Archivo: E34-CL01-tls.txt
case=valid-ca-san result=success panic=false
case=wrong-ca result=rejected panic=true
case=wrong-san result=rejected panic=true
case=missing-ca result=initialization-error panic=true
--- PASS: TestTLS (0.51s)
```

La verificación se configura en `Referance/dominus-sdk/dominus/broker_client_factory.go:28-45`. El defecto de manejo aparece en las líneas 29-34:

```go
if _, err := os.Stat(caCertPath); err != nil {
    panic(err)
}
cred, err := credentials.NewClientTLSFromFile(caCertPath, serverName)
if err != nil {
    panic(err)
}
```

#### Recomendación

Conservar la validación de CA y SAN, pero cambiar la firma de inicialización para devolver `(Broker, error)`. Un archivo ausente, una CA inválida o un fallo de conexión no deberían terminar la aplicación consumidora. También conviene eliminar la alternativa plaintext de las rutas destinadas a producción o exigir una opción explícita para habilitarla.

#### Regresión

Modificar `TestTLS` para comprobar errores retornados en vez de recuperar `panic`. Los cuatro casos deben permanecer: éxito con CA/SAN válidos y error no nulo para CA distinta, SAN incorrecto y archivo ausente. La regresión debe ejecutarse con `go test -race -run TestTLS ./dominus/security`.

### 5.2. CL-03: validación y autorización de destinos

#### Objetivo

Comprobar si el SDK acepta únicamente destinos con el formato `host:puerto` y si distingue entre una dirección sintácticamente válida y un destino autorizado. Esta validación ocurre durante `NewBrokerConfig(...).InitAPIClients(...)`, antes de invocar una ruta gRPC.

#### Riesgo

El SDK recibe el destino del broker y la lista de suscriptores. Si una aplicación construye esos valores a partir de entrada externa, una validación demasiado amplia puede dirigir conexiones hacia ubicaciones no previstas. OWASP describe la SSRF como el abuso de una aplicación para interactuar con la red en nombre del usuario y recomienda una allowlist cuando los destinos legítimos son conocidos (OWASP Foundation, s. f.). La prueba no explotó una SSRF ni contactó redes externas; confirmó una debilidad de validación que podría participar en ese escenario.

#### Versión y preparación

Se utilizó el mismo commit del SDK indicado en CL-01. El test construyó configuraciones con cinco cadenas. No necesitó conectarse a los destinos: la aceptación o el `panic` ocurre durante la validación de la fábrica.

#### Certificado utilizado, CA y SAN/`serverName`

No aplican. CL-03 aísla la validación de direcciones y usa `InitAPIClients`, no `InitAPIClientsTLSFromFile`. Mezclar un certificado habría añadido una segunda causa de rechazo sin aportar información sobre el parser.

#### Comando

```bash
cd Referance/dominus-sdk
go test -v ./dominus/security -run TestDestinations \
  2>&1 | tee ../security-evidence/E36-CL03-destinations.txt
```

#### Resultado esperado

`127.0.0.1:5000` debía pasar la validación sintáctica. `hostname.test:99999` y `hostname.test/path` debían rechazarse. La autorización debía ser una decisión separada: que una cadena tenga formato correcto no implica que esté permitida.

#### Resultado real

`hostname.test/path` fue aceptado, aunque no tiene el formato `host:puerto`. La prueba también confirmó que el SDK carece de una allowlist independiente. `hostname.test:5000` fue rechazado por la expresión actual, un comportamiento más restrictivo que el formato gRPC general y que debería documentarse si es intencional.

#### Evidencia

```text
Archivo: E36-CL03-destinations.txt
destination=127.0.0.1:5000 accepted=true expected_syntax_accept=true
destination=hostname.test:5000 accepted=false expected_syntax_accept=false
destination=hostname.test:99999 accepted=false expected_syntax_accept=false
destination=hostname.test/path accepted=true expected_syntax_accept=false
unexpected destination validation result
authorization=not implemented as a separate allowlist
--- FAIL: TestDestinations (0.00s)
```

La ruta del defecto es:

```text
NewBrokerConfig
  -> brokerConfig.validate
     -> rules.checkURI
        -> regexp.MatchString
```

Los archivos son `Referance/dominus-sdk/dominus/broker_client_factory.go:61-74` y `rules.go:9-17`. La misma regla se usa para SQS en `sqs_client_factory.go:59-63`.

#### Recomendación

Sustituir la expresión regular como decisión única. `net.SplitHostPort` debe separar host y puerto; el puerto debe estar entre 1 y 65535; y deben rechazarse rutas, esquemas y credenciales embebidas. Después de validar la sintaxis, una allowlist debe decidir qué hosts o direcciones están autorizados. El broker debe repetir esta validación antes de iniciar conexiones salientes, porque el SDK no es una frontera de confianza.

#### Regresión

Mantener una tabla de casos válidos e inválidos. La prueba debe exigir el rechazo de `hostname.test/path`, puertos fuera de rango, destinos sin puerto y entradas con esquema. Debe agregar casos separados para “sintaxis válida y autorizada” y “sintaxis válida pero fuera de la allowlist”. El comando de regresión es `go test -race -run TestDestinations ./dominus/security`.

### 5.3. CL-05: error de serialización descartado

#### Objetivo

Comprobar que el SDK devuelve el error cuando un valor no puede convertirse a JSON y que no envía una solicitud incompleta. La ruta evaluada es `/dominus.BrokerAPI/ClientStream`, abierta por `UseStreamClientConn()`.

#### Riesgo

`json.Marshal` puede fallar con valores como funciones o canales. Si el SDK ignora ese error, el consumidor recibe `nil` y puede creer que la operación fue enviada correctamente. El broker recibe un payload vacío, lo que afecta la integridad del mensaje y dificulta el diagnóstico. MITRE clasifica la omisión del valor de retorno de una operación como CWE-252, *Unchecked Return Value* (MITRE, 2026b).

#### Versión y preparación

Se utilizó el commit del SDK descrito en CL-01. `TestSerializationError` levantó un servidor gRPC local, obtuvo la función de envío de `UseStreamClientConn()` y le pasó `func() {}`, un valor que `encoding/json` no puede serializar.

#### Certificado utilizado, CA y SAN/`serverName`

No aplican. El servidor local se creó sin TLS para aislar el comportamiento de serialización. CL-01 cubre de forma independiente la confianza del canal.

#### Comando

```bash
cd Referance/dominus-sdk
go test -v ./dominus/security -run TestSerializationError \
  2>&1 | tee ../security-evidence/E37-CL05-serialization.txt
```

#### Resultado esperado

`json.Marshal` debía fallar, la función de envío debía retornar ese error y el servidor no debía recibir ningún mensaje.

#### Resultado real

La función devolvió `nil`, llamó a `Send` y el servidor recibió un payload con longitud cero. El test se marcó como fallido de forma intencional para que el comportamiento no pase inadvertido en una suite automatizada.

#### Evidencia

```text
Archivo: E37-CL05-serialization.txt
marshal_error_input=function
send_error=<nil>
send_called=true
payload_length=0
FAIL: json.Marshal error was swallowed; Send received an empty payload
--- FAIL: TestSerializationError (0.01s)
```

El defecto aparece dos veces en `Referance/dominus-sdk/dominus/broker_client_services.go`, para client stream y bidirectional stream:

```go
// Línea 25
payload, _ := json.Marshal(body)

// Línea 50
payload, _ := json.Marshal(body)
```

#### Recomendación

Capturar el error y devolverlo antes de llamar a `Send`:

```go
payload, err := json.Marshal(body)
if err != nil {
    return fmt.Errorf("serialize broker payload: %w", err)
}
```

El mismo cambio debe aplicarse a `UseStreamClientConn` y `UseBiStreamConn`. El error debe conservar la causa con `%w` y no debe registrar el contenido completo del payload.

#### Regresión

Actualizar `TestSerializationError` para exigir `send_error != nil`, `send_called == false` y ausencia de mensaje en el canal del servidor. Agregar un caso válido que confirme que un objeto serializable todavía llega con su contenido. Ejecutar `go test -race -run TestSerializationError ./dominus/security`.

## 6. Priorización de correcciones

El orden propuesto parte del impacto observado y de la facilidad con la que un cliente puede alcanzar el defecto.

1. Corregir BE-01. Una solicitud sin token no debe terminar el proceso.
2. Corregir BE-03. La clave de idempotencia debe reservarse de forma atómica antes de ejecutar una operación SQS.
3. Hacer obligatorio TLS en producción para cerrar BE-06.
4. Propagar el error de serialización de CL-05 y evitar el envío vacío.
5. Separar sintaxis y autorización de destinos para CL-03, tanto en el SDK como en el broker.
6. Sustituir los `panic` de inicialización TLS de CL-01 por errores retornables.

Después de cada cambio se debe ejecutar primero la regresión asociada, después la suite del componente y finalmente las herramientas estáticas:

```bash
go test -race -count=1 ./...
go vet ./...
govulncheck ./...
gosec ./...
```

La evidencia nueva debe guardarse junto a la anterior, con una etiqueta `before` y `after`. Reemplazar el archivo original impediría comprobar que el defecto existía antes de la corrección.

## 7. Conclusión

Las seis pruebas permiten ubicar problemas concretos sin extrapolar más allá del laboratorio. En el backend, la ausencia de token puede cerrar el proceso, la idempotencia acepta múltiples solicitudes concurrentes y la configuración efectiva usa texto plano. En el SDK, la verificación de certificados funciona, pero comunica fallos mediante `panic`; la validación de destinos acepta una forma no prevista; y la serialización descarta un error antes de enviar un mensaje vacío.

La evidencia también muestra controles que sí operaron: un token incorrecto fue rechazado, un token correcto permitió la operación, una CA ajena no fue aceptada y un SAN incorrecto impidió la conexión. Estos resultados no compensan los hallazgos, pero ayudan a acotar la corrección. El trabajo pendiente no consiste en reemplazar toda la autenticación o toda la capa TLS, sino en corregir los puntos donde el comportamiento seguro se rompe y conservar una regresión para cada uno.

## 8. Referencias

gRPC Authors. (2024). *Authentication*. gRPC. https://grpc.io/docs/guides/auth/

MITRE. (2026a). *CWE-129: Improper validation of array index*. Common Weakness Enumeration. https://cwe.mitre.org/data/definitions/129.html

MITRE. (2026b). *CWE-252: Unchecked return value*. Common Weakness Enumeration. https://cwe.mitre.org/data/definitions/252.html

OWASP Foundation. (s. f.). *Server-side request forgery prevention cheat sheet*. OWASP Cheat Sheet Series. https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html

Redis Ltd. (s. f.). *SET*. Redis Documentation. https://redis.io/docs/latest/commands/set/

The Go Team. (s. f.). *Data race detector*. The Go Programming Language. https://go.dev/doc/articles/race_detector

Universidad Internacional de La Rioja. (2026). *Guía intensiva para el análisis de ciberseguridad de Dominus* [Guía de laboratorio no publicada].
