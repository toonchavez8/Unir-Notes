# Análisis de ciberseguridad de Dominus

## 1. Alcance de la actividad

En esta actividad se evaluaron dos partes del sistema. La primera fue el backend `dominus-broker`, responsable de exponer los servicios HTTP y gRPC, validar tokens, gestionar operaciones concurrentes y comunicarse con Redis. La segunda fue el cliente `dominus-sdk`, que cumple el papel de interfaz de consumo de Dominus. Como Dominus no dispone de una interfaz gráfica, las aplicaciones que lo utilizan acceden al broker mediante este SDK, que construye las conexiones, agrega metadatos, serializa las solicitudes y permite invocar las operaciones remotas. Por esta razón, el análisis de la interfaz se centró en el comportamiento del SDK y no en una pantalla web.

La prueba no fue una exploración de red. Se ejecutó en un laboratorio local con Docker y las pruebas de destinos se limitaron al loopback (`127.0.0.1`). Se cubrieron los bloques BE-01 a BE-07 para el broker y CL-01 a CL-06 para el SDK, con el propósito de identificar controles efectivos, fallos observables y aspectos que requieren una segunda revisión. En el broker se revisaron autenticación, concurrencia, destinos, límites de payload, streams, TLS y Redis. En el SDK se analizaron la validación de destinos, la protección del canal TLS, el envío de credenciales, el manejo de errores, la serialización y los límites de tiempo. Las pruebas propias de un navegador, como XSS, CSRF y seguridad de cookies, no son aplicables a la arquitectura presente porque no existe una interfaz web basada en sesiones, formularios o cookies.

### Conceptos utilizados en el análisis

Para evitar ambigüedades, se utilizan las siguientes abreviaciones:

- **BE** significa *backend evaluation*. En este documento identifica las pruebas aplicadas directamente al backend `dominus-broker`.
- **CL** significa *client evaluation*. Identifica las pruebas aplicadas al cliente `dominus-sdk`, que en el alcance de esta actividad funciona como la interfaz de consumo del backend.
- **SDK** significa *Software Development Kit*. Es el conjunto de código que una aplicación cliente utiliza para conectarse al broker sin construir manualmente cada solicitud gRPC.
- **TLS** significa *Transport Layer Security*. Es el protocolo que cifra el canal y verifica la identidad del servidor mediante certificados.
- **gRPC** significa *Google Remote Procedure Call*. Es el protocolo usado por Dominus para invocar operaciones remotas y mantener algunos streams.
- **ACL** significa *Access Control List*. En Redis define qué usuarios pueden autenticarse y qué comandos o claves pueden utilizar.
- **SSRF** significa *Server-Side Request Forgery*. Es el riesgo de que un servidor sea inducido a conectarse a un destino que el atacante no debería poder alcanzar directamente.
- **TTL** significa *Time To Live*. Es el tiempo restante antes de que Redis elimine automáticamente una clave.

También es necesario precisar el concepto de idempotencia. Una operación idempotente produce el mismo efecto aunque el cliente la repita. En este laboratorio, la idempotencia se implementa mediante una clave asociada a una solicitud. Si la misma clave llega dos veces, el broker debería procesar una sola solicitud y reconocer las siguientes como duplicadas. Esto protege operaciones de publicación, consumo o suscripción frente a reintentos causados por timeouts y frente a solicitudes concurrentes.

La distinción entre backend y SDK importa porque no se puede delegar toda la seguridad en el cliente. El SDK puede rechazar un destino mal formado, pero una solicitud creada por otro cliente podría llamar directamente al broker. Por esa razón, las validaciones relacionadas con autenticación, autorización, límites e idempotencia deben repetirse en el backend, que es la frontera de confianza del sistema.

## 2. Criterio académico para interpretar los resultados

La evidencia se interpreta desde el funcionamiento que se esperaba del control, no solo desde el código de salida del comando. Por ejemplo, una respuesta `403 Forbidden` demuestra que el servidor rechazó una solicitud HTTP, pero no demuestra que el token esté cifrado. Para afirmar confidencialidad se necesita comprobar TLS; para afirmar autenticación se necesita comprobar la decisión del servidor; y para afirmar disponibilidad se necesita observar que el proceso permanece activo después de una entrada inválida.

La idempotencia se relaciona con la confiabilidad de las operaciones remotas. Un cliente puede repetir una solicitud porque perdió la respuesta, aunque el servidor ya la haya ejecutado. Si el broker no identifica el reintento mediante una clave y una operación atómica, puede publicar o procesar el mismo mensaje más de una vez. Redis ofrece la condición `NX` precisamente para crear una clave solo si no existe, mientras que `EX` permite limitar su permanencia en segundos (Redis Ltd., s. f.).

La validación de destinos se analiza como un control de confianza. El SDK recibe una dirección, pero el broker es quien abre la conexión y, por tanto, quien debe aplicar la última decisión. Si la entrada puede influir en el destino de una conexión del servidor, existe un riesgo potencial de SSRF. OWASP recomienda restringir los destinos y validar de manera explícita el formato de la dirección cuando un servidor realiza solicitudes en nombre de un cliente (OWASP Foundation, s. f.). En esta actividad no se probaron redes internas ni servicios públicos; se utilizó únicamente loopback para observar el comportamiento sin ampliar el alcance.

TLS también requiere una explicación separada. Un token válido permite identificar al cliente, pero no cifra por sí mismo el contenido de la comunicación. El canal debe usar TLS para evitar que un tercero con acceso al tráfico lea el token o modifique una solicitud. La documentación de gRPC distingue la autenticación de la protección del transporte, y la biblioteca `crypto/tls` de Go implementa la validación de certificados y nombres del servidor (gRPC Authors, s. f.; The Go Team, s. f.-b).

En las pruebas concurrentes se diferenció una carrera de datos de una carrera lógica. El detector `-race` de Go busca accesos concurrentes incompatibles a memoria; no puede decidir si una secuencia de operaciones de negocio, como comprobar y guardar una clave, es atómica. Por eso BE-03 puede no reportar una carrera de datos y aun así demostrar que la idempotencia falla (The Go Team, s. f.-a).

## 3. Preparación del laboratorio

El repositorio no contiene un `docker compose` específico para el laboratorio. Por ello se utilizó la imagen construida previamente:

```bash
docker image ls dominus-broker:security-lab
```

El escenario quedó compuesto por un contenedor Redis y el contenedor `dominus-broker-lab`, con los puertos locales `6379`, `8000` y `5000`. La información de arranque se conservó en `E21-broker-startup.txt`. El servicio informó los siguientes puntos de escucha:

```text
Rest: http://0.0.0.0:8000
Grpc: 0.0.0.0:5000
```

Las pruebas HTTP se realizaron con `curl`; las pruebas de reflexión gRPC, con `grpcurl`; y las pruebas concurrentes del backend y del SDK, con `go test`. Las salidas se capturaron mediante `tee` en la carpeta:

```text
C:\Users\Dev\repos\toonchavez8\Unir-Notes\Maestría-Ingeniería-de-Software\10-Proyecto-de-Applicacion\Referance\security-evidence
```

Se usó la extensión `.txt` para las salidas de comandos y `.md` para los análisis interpretativos. Esta separación permite distinguir la evidencia reproducible del razonamiento construido a partir de ella. Los tokens empleados fueron de laboratorio y no se incorporaron credenciales reales al documento.

## 4. Herramientas utilizadas

| Herramienta | Uso en la actividad |
|---|---|
| Docker | Aislar el broker y Redis, revisar puertos y conservar un entorno reproducible. |
| `curl` | Verificar autenticación HTTP, salud y métricas. |
| `grpcurl` | Consultar reflexión gRPC y comparar solicitudes sin token, con token inválido y con token válido. |
| Go y `go test` | Ejecutar pruebas de concurrencia, TLS, metadatos, destinos, timeout, serialización y ciclo de vida. |
| `go test -race` | Buscar carreras de datos en la prueba de idempotencia. |
| Redis CLI | Comprobar ACL, conectividad y expiración de claves. |
| `docker stats` y `docker logs` | Observar memoria, continuidad del proceso y errores durante las pruebas. |
| Certificados efímeros de prueba | Validar en el SDK una CA correcta, una CA incorrecta, un nombre incorrecto y la ausencia de CA. |

El detector de carreras se incluyó porque una operación puede parecer correcta en una prueba secuencial y fallar cuando varias solicitudes compiten por la misma clave. En este caso se utilizó como control complementario: que no aparezca una carrera de memoria no significa que la lógica de negocio sea atómica.

El criterio de análisis fue el siguiente: una prueba tiene un resultado esperado, una observación y una interpretación. Cuando la observación coincide con el criterio, se considera que el control funciona para ese escenario. Cuando difiere, se registra un hallazgo. Cuando el escenario no permite decidir si existe una política, se marca como inconcluso y no se presenta como vulnerabilidad confirmada.

## 5. Resultados del backend `dominus-broker`

### BE-01. Autenticación gRPC y manejo de solicitudes sin token

Se comenzó con la consulta de reflexión:

```bash
grpcurl -plaintext 127.0.0.1:5000 list
```

La primera solicitud no incluyó `x-api-key`. El resultado fue un `panic` con `index out of range [0] with length 0`, localizado en `middlewares.go:48`. El middleware obtiene el primer elemento de la metadata sin comprobar antes si el encabezado existe. Después del `panic`, el contenedor dejó de atender y la comprobación HTTP de salud registró conexión rechazada.

La misma prueba con un token inválido produjo `Unauthenticated` y el proceso permaneció activo. Con el token válido se listaron `dominus.BrokerAPI`, `dominus.SqsAPI` y los servicios de reflexión. Por tanto, el control de autenticación sí distingue un token correcto, pero el caso de ausencia del encabezado permite una denegación de servicio por terminación del proceso.

```text
Archivo de evidencia: E23-BE01-no-token.txt
Fragmento: panic: runtime error: index out of range [0] with length 0

Archivo de evidencia: E24-BE01-health-after-no-token.txt
Fragmento: Failed to connect to 127.0.0.1 port 8000

Archivo de evidencia: E25-BE01-invalid-token.txt
Fragmento: code = Unauthenticated desc = failed to match token

Archivo de evidencia: E26-BE01-valid-token.txt
Fragmento: dominus.BrokerAPI / dominus.SqsAPI / grpc.reflection.v1.ServerReflection
```

### BE-02. Autenticación HTTP y cabecera reenviada

La matriz de resultados fue la siguiente:

| Solicitud | Resultado |
|---|---|
| `/health` sin token | `403 Forbidden` |
| `/health` con token inválido | `403 Forbidden` |
| `/health` con token válido | `200 OK`, `Health ok` |
| `/metrics` con token válido | `200 OK`, métricas Prometheus |
| `/health` con token válido y `X-Forwarded-For` externo | `200 OK` |

El resultado muestra una diferencia importante entre los transportes: HTTP maneja correctamente la ausencia del token y devuelve una respuesta controlada, mientras que gRPC terminó el proceso en el caso equivalente. La cabecera `X-Forwarded-For` no cambió la decisión de autenticación. Esto no se interpreta como una vulnerabilidad por sí sola, porque no se encontró una política documentada que usara esa cabecera para autorizar solicitudes.

```text
Archivo de evidencia: E27-BE01-no-token.txt
Fragmento: HTTP/1.1 403 Forbidden - failed to match token

Archivo de evidencia: E28-BE02-invalid-token.txt
Fragmento: HTTP/1.1 403 Forbidden - failed to match token

Archivo de evidencia: E29-BE02-valid-health.txt
Fragmento: HTTP/1.1 200 OK - Health ok

Archivo de evidencia: E30-BE02-valid-metrics.txt
Fragmento: HTTP/1.1 200 OK - Content-Type: text/plain; charset=utf-8

Archivo de evidencia: E30-BE02-forwarded-for.txt
Fragmento: HTTP/1.1 200 OK - Health ok
```

### BE-03. Idempotencia bajo concurrencia

Se ejecutaron veinte rondas con veinte goroutines que utilizaron una misma clave de idempotencia. El comando fue:

```bash
CGO_ENABLED=1 go test -race -count=20 ./tests/security
```

La compilación necesitó CGO habilitado y un ajuste previo en el test para tratar el puerto de Redis como cadena. Una vez corregido, no se reportaron carreras de datos por parte de `-race`. Sin embargo, la prueba sí encontró una carrera lógica: en distintas rondas fueron aceptadas entre 3 y 20 solicitudes, mientras que las restantes recibieron `rpc error: code = Aborted desc = rate limit reached`.

La causa observable está en el flujo de `middlewares.go:101-109`: primero se comprueba si existe el consumidor y después se guarda de forma asíncrona en una goroutine. Dos solicitudes pueden pasar la comprobación antes de que alguna termine el guardado. En consecuencia, el detector de memoria pasa, pero el requisito funcional de “una sola aceptación por clave” no queda garantizado.

```text
Archivo de evidencia: E31-BE03-idempotencia.txt
Fragmento: accepted=20 en una ronda; en otras rondas accepted=3 y las restantes terminaron con code = Aborted desc = rate limit reached

Archivo de evidencia: E31-BE03-analysis.md
Fragmento: la prueba no reportó data races, pero no se conservó la invariante de una sola aceptación
```

La corrección recomendada es una operación atómica en Redis, por ejemplo `SET key value NX EX 10`, comprobando el resultado de `NX` antes de continuar. La respuesta del broker también debe diferenciar “clave ya procesada” de “límite de tasa alcanzado”, porque son situaciones distintas para el cliente.

### BE-04. Destinos de suscriptores

La prueba utilizó exclusivamente `127.0.0.1:9000`, con un receptor local. El broker intentó iniciar la conexión: el receptor capturó el preámbulo `PRI * HTTP/2.0` y los logs registraron intentos repetidos hacia `127.0.0.1:9000`, seguidos de `connection refused`. El proceso continuó activo.

El resultado confirma que la dirección recibida llega al componente que inicia la conexión. No demuestra por sí mismo que exista una allowlist o una política de autorización para destinos. La prueba se clasifica como inconclusa respecto al control de destinos, y no se amplió hacia direcciones privadas, de enlace local, LAN o servicios públicos porque estaban fuera del alcance seguro definido para el laboratorio.

```text
Archivo de evidencia: E34-BE04-loopback.txt
Fragmento: destino enviado: 127.0.0.1:9000

Archivo de evidencia: E34-BE04-broker-log.txt
Fragmento: connection refused hacia 127.0.0.1:9000

Archivo de evidencia: E34-BE04-observation.txt
Fragmento: se observó el preámbulo PRI * HTTP/2.0

Archivo de evidencia: E34-BE04-analysis.md
Fragmento: el intento de conexión fue confirmado; la allowlist no pudo confirmarse
```

### BE-05. Límites de payload, suscriptores y streams

Se probaron los tamaños de forma incremental:

| Payload | Resultado | Proceso |
|---:|---|---|
| 1 KiB | Aceptado; salida correcta; latencia aproximada de 0.187 s | Vivo |
| 64 KiB | Aceptado; salida correcta; latencia aproximada de 0.532 s | Vivo |
| 1 MiB | Aceptado; salida correcta; latencia aproximada de 0.207 s | Vivo |
| 4 MiB | Rechazado con `ResourceExhausted` | Vivo |

En el último caso gRPC indicó: `received message larger than max (4194309 vs. 4194304)`. Esto demuestra un límite explícito de recepción y evita concluir erróneamente que el sistema acepta cualquier tamaño. En la prueba de veinte streams, las conexiones terminaron por `DeadlineExceeded` aproximadamente a los 1.5 segundos y el proceso permaneció vivo. Se cerraron los contextos del cliente al finalizar.

La memoria observada por Docker aumentó durante la prueba de streams, pero no se observó una caída del proceso. La evidencia sirve como línea base del laboratorio, no como un estudio de rendimiento exhaustivo.

```text
Archivo de evidencia: E35-BE05-payloads.txt
Fragmento: 1 KiB, 64 KiB y 1 MiB aceptados; 4 MiB rechazado con ResourceExhausted

Archivo de evidencia: E35-BE05-streams.txt
Fragmento: streams=20; todos terminaron con DeadlineExceeded; proceso vivo

Archivo de evidencia: E35-BE05-stats-after.txt
Fragmento: memoria Docker registrada después de payloads y streams

Archivo de evidencia: E35-BE05-analysis.md
Fragmento: existe límite observable y no se observó caída del broker
```

### BE-06. TLS y degradación a texto plano

La configuración efectiva mostró listeners HTTP y gRPC en texto plano. La consulta gRPC con `-plaintext` funcionó; con `-insecure` falló porque el servidor devolvió texto plano donde el cliente esperaba un handshake TLS. La solicitud HTTPS al puerto 8000 también falló durante el handshake, mientras que HTTP respondió.

No se encontraron certificados disponibles en la imagen del laboratorio, por lo que los escenarios de CA válida, CA incorrecta y nombre incorrecto no pudieron ejecutarse contra el broker. No se debe presentar esa ausencia como una validación positiva de TLS. El escenario de certificado ausente quedó documentado como una degradación efectiva a plaintext.

La consecuencia es relevante: el token no obtiene confidencialidad por el hecho de compararse en el servidor. Mientras el transporte sea texto plano, puede ser observado por un intermediario con acceso al tráfico.

```text
Archivo de evidencia: E32-BE06-tls-config.txt
Fragmento: configuración de tls, plaintext, insecure y certificados localizada en el repositorio

Archivo de evidencia: E32-BE06-transport.txt
Fragmento: -plaintext funcionó; -insecure falló con tls: first record does not look like a TLS handshake

Archivo de evidencia: E32-BE06-analysis.md
Fragmento: el listener efectivo del laboratorio opera en texto plano
```

### BE-07. Redis y privilegios

Redis respondió mediante el usuario de laboratorio `dominus`, con ACL habilitadas y `PONG` ante una solicitud autorizada. La configuración inspeccionada indicó base de datos 1 para idempotencia y una expiración de diez segundos. La clave de prueba `idempotency:be07-ttl-check` mostró `TTL=10` inmediatamente después de crearse. También se revisaron logs recientes con redacción de posibles valores sensibles.

El hallazgo pendiente es la exposición del puerto `6379` al host. Aunque la ACL limita las operaciones, publicar Redis innecesariamente amplía la superficie de ataque. La evidencia no permitió concluir que el diseño completo de privilegios sea suficiente para producción; por eso se clasifica como resultado parcialmente satisfactorio con riesgo de configuración.

```text
Archivo de evidencia: E33-BE07-containers.txt
Fragmento: redis publicado como 0.0.0.0:6379->6379/tcp

Archivo de evidencia: E33-BE07-redis-checks.txt
Fragmento: ACL user dominus; PONG; TTL=10

Archivo de evidencia: E33-BE07-redis-config.txt
Fragmento: configuración de ACL, usuario, puerto y expiración revisada sin copiar secretos

Archivo de evidencia: E37-BE07-analysis.md
Fragmento: ACL y expiración funcionan, pero el puerto publicado amplía la superficie de ataque
```

## 6. Resultados del cliente `dominus-sdk`

### CL-01. Validación TLS del cliente

El SDK se probó con certificados efímeros. La combinación de CA válida y nombre correcto permitió la conexión. Una CA incorrecta y un nombre incorrecto fueron rechazados. La ausencia de CA provocó un `panic` durante la inicialización del cliente, en vez de un error retornable.

El control positivo de verificación de certificados funciona, pero la reacción ante una configuración incompleta debe convertirse en un error manejable para que una aplicación consumidora pueda cerrar de forma controlada.

```text
Archivo de evidencia: E34-CL01-tls.txt
Fragmento: valid CA accepted; wrong CA rejected; wrong server name rejected; missing CA panic

Archivo de evidencia: E34-CL01-analysis.md
Fragmento: la verificación funciona, pero la configuración ausente no produce un error controlado
```

### CL-02. Metadatos y token

El servidor de prueba observó que `x-api-key` estaba presente y que su longitud era de 13 caracteres. También se observó el encabezado de idempotencia. El valor del token no se imprimió, lo que evita exponerlo innecesariamente en la evidencia.

El SDK propaga los metadatos esperados. Esta prueba no evalúa si el secreto se almacena de manera segura en la aplicación consumidora ni si el transporte real del broker está protegido por TLS; esas preguntas corresponden a la configuración de despliegue.

```text
Archivo de evidencia: E35-CL02-metadata.txt
Fragmento: x-api-key present=true length=13; idempotency-header present=true

Archivo de evidencia: E35-CL02-analysis.md
Fragmento: el servidor observó los metadatos sin registrar el valor del token
```

### CL-03. Destinos aceptados por el SDK

El SDK aceptó `127.0.0.1:5000`, rechazó `hostname.test:5000` y rechazó `hostname.test:99999`. Sin embargo, aceptó `hostname.test/path`, aunque se esperaba que una dirección de destino solo contuviera host y puerto. La validación actual permite una forma de URI más amplia de la necesaria.

El resultado no prueba una SSRF contra un servicio real, pero sí identifica una validación débil de entrada. Se recomienda analizar con `net.SplitHostPort`, validar el puerto, rechazar rutas y aplicar una allowlist explícita de destinos permitidos.

```text
Archivo de evidencia: E36-CL03-destinations.txt
Fragmento: 127.0.0.1:5000 accepted; hostname.test:5000 rejected; hostname.test:99999 rejected; hostname.test/path accepted

Archivo de evidencia: E36-CL03-analysis.md
Fragmento: se acepta una ruta donde se esperaba únicamente host y puerto
```

### CL-04. Propagación de timeout

El servidor de prueba bloqueó la respuesta y el cliente registró un timeout cercano a dos segundos. El test demostró el control externo del tiempo de espera, pero el análisis del código encontró que la conexión interna del SDK utiliza `context.Background()` en `broker_client_conn.go:26-46`. Por ello no es posible afirmar que el contexto de la operación del usuario se propague hasta cada RPC.

El resultado se considera inconcluso en cuanto al control fino de cancelación. La API debería recibir un `context.Context` en cada operación y evitar contextos globales sin deadline.

```text
Archivo de evidencia: E36-CL04-timeout.txt
Fragmento: timeout=2.0005s; sdk_context_control=not-exposed

Archivo de evidencia: E36-CL04-analysis.md
Fragmento: el timeout externo funcionó, pero no se confirmó propagación del contexto del SDK
```

### CL-05. Errores de serialización

La prueba fue diseñada para enviar un valor que no podía serializarse. La función continuó con un payload vacío y el error de `json.Marshal` apareció descartado en `broker_client_services.go:25` y `:50` mediante `payload, _ := json.Marshal(body)`.

El test se marcó como fallido de forma intencional porque se llamó al servidor con `send_error=<nil>` y `payload_length=0`. El SDK no debe convertir un error de serialización en una solicitud aparentemente válida. Debe retornar el error antes de invocar gRPC y conservar el contexto de la operación.

```text
Archivo de evidencia: E37-CL05-serialization.txt
Fragmento: send_error=<nil>; send_called=true; payload_length=0

Archivo de evidencia: E37-CL05-analysis.md
Fragmento: el error de json.Marshal fue ignorado y se envió un payload vacío
```

### CL-06. Ciclo de vida de conexiones

Se ejecutaron veinte operaciones de SQS y se comparó el número de goroutines antes y después. El incremento observado fue de aproximadamente 160 goroutines. La prueba superó el umbral conservador definido para el laboratorio. La causa probable es que el SDK crea conexiones internamente sin exponer una operación equivalente a `Close`.

Este resultado requiere una medición adicional con un perfil de larga duración para separar goroutines de trabajo legítimas de una fuga. Aun así, la ausencia de un ciclo de vida explícito es un riesgo de disponibilidad para aplicaciones que crean clientes repetidamente.

```text
Archivo de evidencia: E38-CL06-connections.txt
Fragmento: operations=20; goroutines_before=3; goroutines_after=163; delta=160

Archivo de evidencia: E38-CL06-analysis.md
Fragmento: el crecimiento superó el umbral conservador y requiere revisar el cierre de conexiones
```

## 7. Evidencia interpretada y ubicación de las correcciones

Esta sección incorpora fragmentos de las salidas guardadas en `security-evidence`. Los bloques no sustituyen los archivos completos; funcionan como una muestra verificable de lo que se observó. En cada caso se distingue entre lo que se esperaba demostrar y lo que realmente permite concluir la evidencia.

### BE-01: ausencia de token gRPC

Resultado esperado: una solicitud sin `x-api-key` debía terminar con un error controlado, preferentemente `Unauthenticated`, sin cerrar el proceso.

```text
Failed to list services: rpc error: code = Unavailable desc = connection error
...
panic: runtime error: index out of range [0] with length 0
dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go:48
```

Confirmación: el control no cumplió el resultado esperado. La solicitud llegó al middleware, pero la falta de metadata produjo un acceso fuera de rango. La evidencia posterior de salud confirmó que el broker ya no atendía solicitudes. El riesgo es de disponibilidad y no requiere conocer un token: cualquier cliente con acceso al puerto gRPC puede provocar el cierre del proceso. En términos de seguridad, es un caso de denegación de servicio por entrada no validada.

Corrección propuesta: `Referance/dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go:48`. Antes de leer el primer valor debe comprobarse que la metadata contiene `x-api-key` y que tiene al menos un valor. El middleware debe retornar `status.Error(codes.Unauthenticated, "missing api key")`. También debe agregarse una prueba de regresión que compruebe que el proceso permanece vivo después de una solicitud sin encabezado.

### BE-02: autenticación HTTP

Resultado esperado: sin token o con token inválido debía responderse `403`; con token válido, `200`.

```text
HTTP/1.1 403 Forbidden
failed to match token

HTTP/1.1 200 OK
Health ok
```

Confirmación: la autenticación HTTP sí produjo el comportamiento esperado. La misma decisión se mantuvo cuando se agregó `X-Forwarded-For: 10.0.0.10`:

```text
HTTP/1.1 200 OK
Content-Length: 9
Health ok
```

Esto confirma que la cabecera reenviada no se utilizó para saltar la autenticación en esta prueba. No confirma que la cabecera sea confiable para otras políticas; si en el futuro se usa para autorización o auditoría, debe aceptarse únicamente desde un proxy confiable y eliminarse o sobrescribirse en el borde.

Corrección y mejora: revisar el middleware HTTP que protege las rutas y agregar pruebas para token ausente, inválido, válido y cabeceras duplicadas. La corrección principal no está en BE-02, sino en unificar el manejo de errores con el middleware gRPC para evitar que ambos transportes tengan comportamientos de seguridad distintos.

### BE-03: idempotencia bajo concurrencia

Resultado esperado: de veinte solicitudes concurrentes con la misma clave, una sola debía ser aceptada y las otras diecinueve debían recibir una respuesta estable de duplicado o conflicto. `go test -race` no debía reportar carreras de memoria.

```text
round=1 accepted=20 total=20
round=2 accepted=3 total=20
rpc error: code = Aborted desc = rate limit reached
PASS: no data races reported by -race
FAIL: idempotency invariant was not preserved
```

Confirmación parcial: el detector de carreras no encontró una carrera de memoria, pero la propiedad de idempotencia falló. El número variable de aceptaciones demuestra que el problema es lógico: varias solicitudes pasan la comprobación antes de que se complete el guardado. La operación no es atómica aunque cada instrucción individual sea segura.

El riesgo es duplicar efectos de negocio, mensajes o consumo de recursos. En sistemas distribuidos, una clave de idempotencia se utiliza precisamente para que reintentos y solicitudes simultáneas no ejecuten dos veces una operación. El error `rate limit reached` tampoco expresa correctamente la causa real, por lo que el cliente no puede decidir si debe reintentar.

Corrección: `Referance/dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go:101-109` y la implementación Redis en `Referance/dominus-broker/internal/infrastructure/redis/cchecker/outbound.go`. Sustituir el patrón “check y después save” por una operación atómica `SET key value NX EX 10`. Si Redis devuelve que la clave ya existe, responder con un código de duplicado; si falla Redis, aplicar una política explícita de fail-closed o fail-safe según la criticidad de la operación. La prueba debe conservar veinte goroutines y exigir exactamente una aceptación.

### BE-04: destino loopback

Resultado esperado: el broker debía aplicar una política de destinos y, como mínimo, permitir o rechazar de forma observable `127.0.0.1:9000`.

```text
Destino enviado: 127.0.0.1:9000
PRI * HTTP/2.0
connection refused
rpc error: code = DeadlineExceeded
```

Confirmación: se confirmó el intento de conexión y que el broker siguió vivo. No se confirmó una allowlist. El rechazo observado provino de que el receptor no aceptó o no mantuvo la conexión, no de una respuesta explícita de autorización del broker. Por eso el resultado es inconcluso respecto a SSRF y control de destinos.

Corrección preventiva: localizar la validación de destino en el servicio que procesa suscripciones y hacer que la decisión ocurra antes de crear el cliente gRPC. La política debe aceptar únicamente destinos previamente autorizados, rechazar formatos ambiguos y registrar la decisión sin incluir secretos. Aunque la prueba solo utilizó loopback, la defensa debe estar en el broker y no exclusivamente en el SDK.

### BE-05: límites de payload y streams

Resultado esperado: los tamaños debían procesarse de forma incremental, con un límite explícito en 4 MiB; el broker debía permanecer vivo después de veinte streams.

```text
payload=1024       result=accepted   process_alive=true
payload=65536      result=accepted   process_alive=true
payload=1048576    result=accepted   process_alive=true
payload=4194304    result=ResourceExhausted
grpc: received message larger than max (4194309 vs. 4194304)
streams=20 result=DeadlineExceeded closed_by_client=true process_alive=true
```

Confirmación: el límite de recepción es observable y el proceso no cayó. El mensaje de error muestra que el control está aplicado en el límite gRPC, aunque el tamaño recibido incluya algunos bytes de envoltura. Los veinte streams finalizaron por timeout controlado. La memoria subió durante la prueba, por lo que conviene conservar la medición como línea base; no se debe convertir esa variación aislada en una afirmación de fuga.

Corrección o mejora: documentar el límite en el contrato del servicio y devolver un error de tamaño que el SDK pueda interpretar. Revisar también límites de concurrencia, timeouts y cancelación en el servidor. La configuración relacionada con el tamaño HTTP se localizó en `Referance/dominus-broker/internal/bootstraps/bootstraps.go:199`; debe verificarse que los límites HTTP y gRPC sean consistentes.

### BE-06: TLS y plaintext

Resultado esperado: un listener configurado con TLS debía aceptar una CA y nombre válidos y rechazar CA, nombre o certificado ausentes; el servicio no debía degradar silenciosamente a texto plano.

```text
grpcurl -plaintext ... list
dominus.BrokerAPI

grpcurl -insecure ... list
tls: first record does not look like a TLS handshake

curl https://127.0.0.1:8000/health
TLS handshake failed
```

Confirmación: el entorno real de esta prueba opera en plaintext. No fue posible ejecutar A, B y C contra el broker porque la imagen no tenía certificados configurados. Sí se confirmó D en el sentido de que, ante la ausencia de TLS, el sistema expone HTTP y gRPC sin cifrado. El riesgo es la exposición de tokens, metadatos y contenido a cualquier intermediario que pueda observar el tráfico.

Corrección: revisar la inicialización de listeners en `Referance/dominus-broker/internal/bootstraps/bootstraps.go` y la configuración de certificados de la imagen. El arranque debe fallar si el modo de producción exige TLS y falta una CA, certificado o clave. El SDK ya mostró validación de CA y nombre, pero el control solo protege el tránsito cuando el servidor realmente ofrece TLS. La prueba completa debe repetirse con cuatro escenarios documentados.

### BE-07: Redis, ACL y expiración

Resultado esperado: Redis no debía exponer un puerto público innecesario; el usuario del broker debía tener permisos limitados y las claves de idempotencia debían expirar.

```text
redis:6379 -> 0.0.0.0:6379
ACL user dominus ... on
PONG
idempotency:be07-ttl-check TTL=10
```

Confirmación parcial: la ACL funcionó y la expiración de la clave fue observable. El resultado de seguridad no es completo porque Redis sí quedó publicado en el host. La ACL reduce el impacto de un acceso, pero no elimina la superficie de ataque ni el riesgo de errores de configuración.

Corrección: retirar la publicación `6379:6379` del despliegue cuando el broker solo necesita la red interna; mantener la conexión en una red Docker privada. Revisar `terraform`, `env` y la configuración Redis para aplicar mínimo privilegio, TLS interno cuando proceda y comandos estrictamente necesarios. La configuración de expiración está relacionada con `Referance/dominus-broker/internal/infrastructure/redis/cchecker/outbound.go:55`; debe conservarse como prueba automatizada.

### CL-01: validación TLS del SDK

Resultado esperado: CA y nombre correctos debían permitir la conexión; CA incorrecta y nombre incorrecto debían rechazarla; la ausencia de configuración debía producir un error controlado.

```text
valid_ca_and_server_name=accepted
wrong_ca=rejected
wrong_server_name=rejected
missing_ca=panic during client initialization
```

Confirmación: los controles criptográficos positivos y negativos funcionaron. El resultado no fue completamente satisfactorio porque la ausencia de CA provocó `panic`, lo que puede terminar una aplicación consumidora si la configuración llega incompleta.

Corrección: en `Referance/dominus-sdk/dominus/broker_client_conn.go` y la fábrica de clientes, sustituir el `panic` por un error retornable. La aplicación debe decidir si aborta el arranque, pero el SDK no debe finalizarla de forma inesperada.

### CL-02: metadatos del SDK

Resultado esperado: el SDK debía enviar el token y la clave de idempotencia, sin imprimir sus valores.

```text
x-api-key present=true length=13
idempotency-header present=true
token_value=<not logged>
```

Confirmación: los metadatos llegaron al servidor de prueba y la evidencia evitó revelar el token. Esta prueba demuestra propagación, no confidencialidad. La confidencialidad depende de TLS y del manejo seguro del secreto en la aplicación que consume el SDK.

Corrección: conservar el filtrado de logs, documentar que el cliente requiere TLS en producción y agregar pruebas que fallen si un logger imprime el valor del token completo.

### CL-03: validación de destinos del SDK

Resultado esperado: aceptar únicamente destinos con host y puerto válidos, rechazando host no permitido, puerto fuera de rango y rutas.

```text
127.0.0.1:5000       accepted
hostname.test:5000   rejected
hostname.test:99999  rejected
hostname.test/path   accepted  <-- resultado no esperado
```

Desmentido parcial: la prueba no respalda que la validación de destino sea estricta. La aceptación de una ruta indica que el parser o la expresión regular permite más formatos que el contrato. Esto puede convertirse en riesgo de SSRF o conexión a un destino no previsto cuando el destino proviene de configuración o entrada externa.

Corrección: `Referance/dominus-sdk/dominus/broker_client_factory.go:67,72` y `sqs_client_factory.go:61`, junto con `rules.go`. Usar `net.SplitHostPort`, validar el rango 1-65535, rechazar rutas y aplicar una allowlist. Repetir la validación en el broker.

### CL-04: timeout y cancelación

Resultado esperado: cancelar el contexto del consumidor debía cancelar el RPC y liberar sus recursos.

```text
timeout=2.0005s
server_response=not_received
sdk_context_control=not-exposed
```

Confirmación limitada: se observó un timeout externo, pero el código usa `context.Background()` en `broker_client_conn.go:26-46`. Esto impide demostrar que cada operación respete el contexto del llamador. El riesgo es mantener RPCs, goroutines o conexiones más tiempo del necesario durante fallos de red.

Corrección: aceptar `context.Context` en los métodos públicos del SDK y pasarlo a `Invoke` o al método gRPC correspondiente. Los timeouts por defecto deben ser explícitos y configurables, no depender de un contexto global sin deadline.

### CL-05: serialización

Resultado esperado: si `json.Marshal` falla, el SDK debía devolver el error y no enviar una solicitud.

```text
send_error=<nil>
send_called=true
payload_length=0
FAIL: serialization error was ignored
```

Desmentido: el SDK no cumplió el resultado esperado. En `broker_client_services.go:25` y `:50` se ignora el error mediante `payload, _ := json.Marshal(body)`. El riesgo es enviar una operación vacía o inválida y ocultar la causa al consumidor, lo que puede generar pérdida silenciosa o inconsistencias.

Corrección: capturar el error, retornarlo y detener la invocación antes de construir la solicitud gRPC. Agregar una prueba que compruebe simultáneamente `send_called=false` y un error no nulo.

### CL-06: ciclo de vida de conexiones

Resultado esperado: veinte operaciones no debían producir un crecimiento desproporcionado de goroutines; el cliente debía permitir cerrar la conexión.

```text
operations=20
goroutines_before=3
goroutines_after=163
delta=160
FAIL: connection lifecycle threshold exceeded
```

Confirmación del síntoma: la prueba observó un incremento elevado. No es suficiente para afirmar por sí solo una fuga permanente, pero sí demuestra que el SDK necesita una revisión de propiedad y cierre de conexiones. El riesgo es degradación progresiva de memoria, descriptores y capacidad de atender solicitudes cuando la aplicación crea clientes repetidamente.

Corrección: `Referance/dominus-sdk/dominus/broker_client_conn.go` y `broker_client_factory.go`. Exponer un cliente reutilizable con `Close`, definir quién posee cada `ClientConn` y asegurar que los errores y timeouts liberen recursos. Repetir la prueba con varias duraciones y perfiles antes de cerrar el hallazgo.

## 8. Hallazgos priorizados

| ID | Severidad | Hallazgo | Evidencia principal |
|---|---|---|---|
| H-01 | Alta | El middleware gRPC accede al primer token sin comprobar que exista y puede terminar el broker. | `E23-BE01-no-token.txt`; `middlewares.go:48` |
| H-02 | Alta | La idempotencia se comprueba y guarda en pasos separados; bajo concurrencia se aceptan varias solicitudes para una misma clave. | `E31-BE03-idempotencia.txt`; `middlewares.go:101-109` |
| H-03 | Alta en redes no confiables | El broker opera en plaintext y el token viaja sin confidencialidad de transporte. | `E32-BE06-transport.txt` |
| H-04 | Media | El SDK descarta errores de serialización y puede enviar un payload vacío. | `E37-CL05-serialization.txt`; `broker_client_services.go:25,50` |
| H-05 | Media | El SDK no expone claramente el cierre de conexiones y la prueba observó un crecimiento elevado de goroutines. | `E38-CL06-connections.txt` |
| H-06 | Media | La validación de destinos del SDK acepta una ruta en una entrada que debería ser host:puerto. | `E36-CL03-destinations.txt`; `broker_client_factory.go:67,72` |

### H-01. Fallo de autenticación gRPC con ausencia de metadata

La evidencia exacta es el `panic` de `E23-BE01-no-token.txt`, seguido por la indisponibilidad registrada en `E24-BE01-health-after-no-token.txt`. El impacto es una denegación de servicio provocada por una solicitud sin credenciales. La corrección debe validar la existencia del encabezado y devolver `Unauthenticated` sin indexar una colección vacía. También debe existir una prueba automatizada para metadata ausente, metadata vacía y múltiples valores.

### H-02. Idempotencia no atómica

La evidencia muestra variación en el número de solicitudes aceptadas y ausencia de carreras de memoria. Esto distingue un defecto de sincronización de un data race tradicional. La corrección debe mover la decisión a una operación atómica en Redis y hacer que el resultado de esa operación determine si el mensaje continúa.

### H-03. Transporte sin TLS

El broker acepta explícitamente plaintext y rechaza el intento TLS. El impacto es exposición de tokens, metadatos y mensajes. La solución debe configurar TLS en HTTP y gRPC, verificar CA y nombre del servidor, y fallar al arrancar cuando falta un certificado requerido. Si se mantiene plaintext solo para desarrollo, debe quedar limitado a loopback mediante configuración separada.

### H-04. Error de serialización oculto

El SDK envía una solicitud con longitud cero después de que `json.Marshal` falla. Esto puede provocar mensajes inválidos, pérdida silenciosa de datos o comportamiento diferente entre operaciones. La corrección es devolver el error de serialización y no llamar al broker.

### H-05. Ciclo de vida de conexiones

El crecimiento observado no basta por sí solo para afirmar una fuga permanente, pero sí justifica una revisión. El SDK debería compartir conexiones cuando corresponda, documentar quién es su propietario y exponer `Close` o un mecanismo equivalente. La prueba debe repetirse con varias duraciones y perfiles de goroutines.

### H-06. Validación de destinos

La aceptación de `hostname.test/path` indica que la expresión de validación no modela exactamente el formato permitido. El arreglo debe validar estructura, rango de puerto, esquema si aplica y política de destinos. En el broker debe existir una defensa independiente del SDK, porque el cliente no es una frontera de confianza.

## 9. Recomendaciones para una siguiente iteración

1. Corregir primero el `panic` gRPC y agregar pruebas de regresión para todas las formas de metadata ausente.
2. Implementar idempotencia atómica con `SET NX EX`, conservar la expiración y devolver un código específico para duplicados.
3. Habilitar TLS obligatorio en ambos listeners, con validación de CA, nombre y presencia de certificados durante el arranque.
4. Eliminar la exposición de Redis al host cuando no sea necesaria; mantenerlo en una red interna y aplicar el principio de mínimo privilegio en ACL.
5. Hacer que el SDK propague `context.Context`, deadlines y cancelación a cada RPC.
6. Propagar todos los errores de serialización, conexión y cierre en lugar de descartarlos.
7. Endurecer la validación de destinos en cliente y servidor, usando allowlists y rechazo de rutas o formatos ambiguos.
8. Definir el ciclo de vida de las conexiones y medir goroutines, memoria y latencia con pruebas de duración controlada.
9. Evitar que logs y métricas contengan tokens, payloads completos o valores de Redis; conservar únicamente identificadores y longitudes cuando sean necesarios.
10. Integrar BE-01 a BE-07 y CL-01 a CL-06 en CI, incluyendo `go test -race`, análisis estático y pruebas que verifiquen que un error de autenticación no termina el proceso.

## 10. Limitaciones y pruebas inconclusas

La prueba TLS completa del broker no pudo ejecutarse porque la imagen utilizada no contenía certificados configurados. Se comprobó la degradación a texto plano, pero no se validaron cuatro combinaciones reales de CA y nombre contra ese listener. BE-04 solo utilizó loopback y confirmó el intento de conexión; no se puede concluir que exista una allowlist completa. La prueba de payloads se realizó mediante `grpcurl` porque el probe Go adicional quedó condicionado por la descarga de un módulo privado.

Estas limitaciones no invalidan los hallazgos observados. Indican qué controles deben probarse nuevamente después de habilitar TLS, completar la política de destinos y estabilizar las dependencias del entorno.

## 11. Conclusión

El laboratorio demostró controles funcionales en autenticación HTTP, validación de certificados del SDK, límites de payload, expiración de idempotencia y propagación básica de metadatos. También reveló riesgos que tienen prioridad de corrección: el `panic` de gRPC ante una solicitud sin token, la idempotencia no atómica bajo concurrencia y el uso de plaintext en el broker.

En el SDK, los problemas más claros fueron el descarte de errores de serialización, la validación incompleta de destinos y la falta de un ciclo de vida explícito para conexiones. La evidencia permite sostener estas conclusiones sin extrapolar resultados de pruebas inconclusas. El siguiente ciclo debe centrarse en cerrar los fallos de disponibilidad y transporte, y después repetir las pruebas con TLS y una política de destinos verificable.

## 12. Bibliografía

Dominus Broker. (2026). *Guía de ciberseguridad Dominus Bash expandida* [Documento interno]. Repositorio Unir-Notes.

gRPC Authors. (s. f.). *Authentication*. gRPC. https://grpc.io/docs/guides/auth/

OWASP Foundation. (s. f.). *Server-side request forgery prevention cheat sheet*. https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html

Redis Ltd. (s. f.). *SET command*. Redis Documentation. https://redis.io/docs/latest/commands/set/

The Go Team. (s. f.-a). *Data race detector*. Go. https://go.dev/doc/articles/race_detector

The Go Team. (s. f.-b). *Package tls*. Go Packages. https://pkg.go.dev/crypto/tls
