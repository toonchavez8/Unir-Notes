  

Pasted markdown(1).md

File

i feel like there is missing steps to get to step 7 and on, can we rewrite it and add more indepth steps using the same style terminaligy and writing just instead of powhershell code use bash

Yes. I agree with your assessment: the original guide jumps from the baseline/tooling into the dynamic tests too quickly. For example, Step 7 starts testing immediately, while it doesn't fully walk through **preparing Bash, verifying the repositories, creating evidence directories, starting Redis/Broker, validating ports, establishing health checks, and defining checkpoints before the security tests**. 

I rewrote **Step 7 onward** much more in-depth while keeping the same terminology and academic/security-testing style, but changing the commands to **Bash**.

# What I Changed

- Converted the PowerShell-oriented commands to Bash.
    
- Added a complete **environment preparation** section before Step 7.
    
- Added explicit verification after almost every important operation.
    
- Added **checkpoints** so you know when to stop or continue.
    
- Added commands for:
    
    - repository validation
        
    - branch/commit tracking
        
    - Go/Docker versions
        
    - dependency downloads
        
    - tests and race detector
        
    - coverage
        
    - `govulncheck`
        
    - `go vet`
        
    - `gosec`
        
    - `gitleaks`
        
    - Trivy/Terraform
        
    - Docker image validation
        
- Added a proper **laboratory startup sequence**.
    
- Added creation and organization of `security-evidence`.
    
- Added disposable test-token handling.
    
- Expanded **BE-01 through BE-07** with setup → execution → verification → expected result.
    
- Expanded **CL-01 through CL-06** similarly.
    
- Added a complete **correction → regression → retest** workflow.
    
- Added a much more explicit **50-step execution order**.
    
- Added cleanup procedures.
    
- Added a final checklist so you can literally work through the assignment step by step.
    
- Kept the important distinction between **hypothesis, observed result, finding, and recommendation**.

The rewritten document is **1,714 lines**, compared with the original 648, so it is substantially more procedural.

A particularly important improvement is that the workflow now looks like:

```Python
Environment
    ↓
Repository / commit verification
    ↓
Tool/version verification
    ↓
Functional baseline
    ↓
Static analysis
    ↓
Laboratory creation
    ↓
Redis + Broker startup
    ↓
Health verification
    ↓
BE-01
    ↓
Verify broker is still alive
    ↓
BE-02
    ↓
BE-03 automated concurrency test
    ↓
BE-04 / BE-05 / BE-06 / BE-07
    ↓
SDK test environment
    ↓
CL-01 ... CL-06
    ↓
Document findings
    ↓
Fix
    ↓
Regression test
    ↓
Full retest
    ↓
Evidence
    ↓
Final report
```

That should make it much easier to **actually execute the guide from a terminal without having to guess what needs to happen between sections**.

# Revised Approach From Step 7 Onward

The original guide needs additional operational steps between the baseline and the security tests. The revised version therefore follows a strict sequence:

1. Prepare Bash and define repository paths.
    
2. Verify both repositories exist.
    
3. Record branch, commit, and local modifications.
    
4. Record Go and Docker versions.
    
5. Download dependencies.
    
6. Run normal tests.
    
7. Run the race detector.
    
8. Generate current coverage.
    
9. Run the SDK baseline.
    
10. Install and verify security tooling.
    
11. Run dependency analysis.
    
12. Run static analysis.
    
13. Run secret detection.
    
14. Review configuration and infrastructure.
    
15. Create the isolated security laboratory.
    
16. Configure disposable credentials.
    
17. Verify ports and services.
    
18. Start Redis and the broker.
    
19. Confirm `/health` before testing.
    
20. Execute each backend security test independently.
    
21. Verify the process after each negative test.
    
22. Create automated concurrency tests where manual testing is insufficient.
    
23. Test the SDK with local TLS certificates.
    
24. Record all evidence without exposing secrets.
    
25. Fix findings individually.
    
26. Add regression tests before declaring a finding resolved.
    
27. Repeat the affected dynamic test.
    
28. Repeat the complete static and functional analysis.
    
29. Compare before/after evidence.
    
30. Clean up the laboratory.
    
31. Write the final report using only observed results.

Every security test should follow the same pattern:

```Python
Prepare
→ Execute
→ Verify
→ Capture evidence
→ Interpret
→ Correct
→ Regression test
→ Retest
```

This prevents the analysis from jumping directly from a source-code hypothesis to a vulnerability claim without first establishing a reproducible laboratory result.

The **full expanded version is in the downloadable Markdown file above**. 

# [Library](https://chatgpt.com/library) /Guia_Ciberseguridad_Dominus_Bash_Expandida.md

# Guía Intensiva Para El Análisis De Ciberseguridad De Dominus

## 1. Propósito Y Criterio De la Actividad

Esta guía sirve para preparar la sección de ciberseguridad de la actividad "Pruebas de la herramienta". El análisis cubre estos components:

- `dominus-broker`: servicio backend escrito en Go que expone APIs gRPC, endpoints HTTP de salud y métricas, conexiones salientes hacia suscriptores y persistencia en Redis.
    
- `dominus-sdk`: biblioteca Go utilizada por las aplicaciones cliente para conectarse al broker, enviar metadatos de autenticación y consumir las operaciones Broker y SQS.

El entorno evaluado es local. No se presupone exposición a Internet, usuarios anónimos ni datos personales reales. Esto reduce la probabilidad de explotación remota, pero no elimina los problemas que pueden causar caída del proceso, filtración de credenciales dentro de la red local, conexiones hacia destinos no autorizados o duplicación de operaciones.

### Justificación Del SDK Como Interfaz Cliente

El proyecto no contiene una interfaz gráfica. Por esta razón, para la rúbrica se considera `dominus-sdk` como la interfaz mediante la cual otro software utilize el backend. El SDK valida direcciones, establece conexiones gRPC, agrega el token de acceso y la clave de idempotencia, serializa mensajes y presenta las operaciones que consume una aplicación. La prueba del lado cliente comprobará estos comportamientos, no aspectos visuals como XSS, formularios, cookies o DOM.

Texto sugerido para la entrega:

> Dominus no dispone de una interfaz gráfica. Su interfaz de consumo es el paquete `dominus-sdk`, que encapsula la conexión de las aplicaciones cliente con el servicio gRPC. Por ello, la prueba de seguridad de la interfaz se aplicó al SDK y se centró en validación de destinos, protección del canal TLS, envío de credenciales, control de errores y límites de tiempo. Las pruebas propias de un navegador, como XSS, CSRF o seguridad de cookies, no son aplicables a la arquitectura evaluada.

Conviene confirmar esta interpretación con el docente. Si "front-end" se entiende estrictamente como interfaz gráfica, el proyecto necesitaría una aplicación consumidora adicional; no sería correcto inventar una UI que no forma parte del alcance.

## 2. Qué Exige Realmente la Rúbrica

La rúbrica pide describir una prueba de seguridad en backend y otra en front-end. Para obtener una evidencia defendible, cada prueba debe incluir:

1. Objetivo y riesgo que se intenta detectar.
    
2. Componente y versión examinados.
    
3. Herramienta o técnica empleada.
    
4. Preparación del laboratorio.
    
5. Entradas utilizadas, sin revelar credenciales reales.
    
6. Resultado esperado.
    
7. Resultado observado.
    
8. Evidencia: salida de consola, captura, registro o prueba automatizada.
    
9. Interpretación del resultado.
    
10. Recomendación y prueba de regresión.

No basta con pegar el resultado de un escáner. La parte valiosa es explicar qué significa el resultado en esta arquitectura.

## 3. Evidencia Inicial Del Repositorio

La revisión estática inicial permite trazar el siguiente mapa:

|Elemento Evidencia en el repositorio Relevancia de seguridad|||
|---|---|---|
|Entrada del servicio|`dominus-broker/cmd/api/main.go:43-46`|Arranca el bootstrap a partir de opciones CLI.|
|Listener gRPC|`dominus-broker/internal/bootstraps/bootstraps.go:161-173`|La reflexión está activa y el servicio escucha en todas las interfaces.|
|Listener HTTP|`dominus-broker/internal/bootstraps/bootstraps.go:178-217`|Expone `/health` y `/metrics`, con token y filtro de red.|
|Autenticación gRPC|`dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go:41-55`|Compara el token en tiempo constante, pero el acceso al primer encabezado require una prueba negativa.|
|Idempotencia|`dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go:86-112`|Comprueba Redis y guarda la clave de forma asíncrona; existe una ventana de carrera documentada.|
|Autenticación HTTP|`dominus-broker/internal/infrastructure/fasthttp/middlewares/api_middleware.go:27-42`|Protege las rutas mediante `x-api-key`.|
|Restricción HTTP por red|`dominus-broker/internal/infrastructure/fasthttp/middlewares/host_allowed.go:24-34`|Usa la IP remota contra un CIDR. El nombre `allow_origins` puede confundirse con CORS.|
|Destinos de suscriptores|`dominus-broker/internal/application/usecases/stream_client/stream_client_service.go:13-32`|Las direcciones suministradas por el cliente se pasan al cliente saliente.|
|Conexiones salientes|`dominus-broker/internal/infrastructure/grpc/outbound/client_stream.go:29-79`|El broker abre conexiones gRPC y goroutines hacia los destinos recibidos.|
|Redis|`dominus-broker/internal/infrastructure/redis/cmemory/outbound.go:21-49`|Admite TLS y credenciales; la configuración de desarrollo merece revisión de privilegios.|
|Cliente sin TLS|`dominus-sdk/dominus/broker_client_factory.go:48-58` y `sqs_client_factory.go:46-56`|Existe un modo explícito con credenciales de transporte inseguras para desarrollo.|
|Cliente con TLS|`dominus-sdk/dominus/broker_client_factory.go:28-45` y `sqs_client_factory.go:26-43`|Carga una CA y valida el nombre del servidor.|
|Metadatos cliente|`dominus-sdk/dominus/interceptors.go:23-42`|Envía `x-api-key`; las llamadas unary también envían idempotencia.|
|Validación de direcciones|`dominus-sdk/dominus/rules.go:9-16` y `enum.go:33-34`|Valida el formato con una expresión regular, pero no determina si el destino está autorizado.|
|Contextos del SDK|`dominus-sdk/dominus/broker_client_conn.go:25-50` y `sqs_client_services.go:25-35`|Usa `context.Background()`, por lo que el consumidor no puede imponer cancelación o fecha límite.|
|Serialización del SDK|`dominus-sdk/dominus/broker_client_services.go:22-33` y `47-60`|El error de `json.Marshal` se descarta.|
|Contenedor|`dominus-broker/Dockerfile:27-32`|El proceso cambia a un usuario sin privilegios, lo cual es un control existente.|
|Automatización|`dominus-broker/Makefile.ps1:277-306`|Ya contempla lint, `govulncheck`, auditoría y verificación previa al despliegue.|

El inventario encontró 50 funciones `Test…` bajo `dominus-broker/tests` y ninguna en `dominus-sdk`. Este conteo describe el estado del código; no significa que las pruebas hayan pasado.

## 4. Modelo Compacto Del Sistema

```Python
flowchart LR
  U["Aplicación cliente"] -->|API Go| SDK["dominus sdk"]
  SDK -->|gRPC y metadatos| B["dominus broker"]
  B -->|Redis protocol| R["Redis"]
  B -->|gRPC saliente| S["Suscriptores"]
  O["Operador local"] -->|HTTP| M["Salud y métricas"]
  M --> B
  C["Configuración y certificados"] --> B
  C --> SDK
```

### Límites De Confianza

- Aplicación cliente → SDK: recibe cuerpos arbitrarios, destinos, token y clave de idempotencia proporcionados por la aplicación.
    
- SDK → broker: cruza una frontera de red gRPC. La autenticación depende de `x-api-key`; la confidencialidad depende de seleccionar TLS.
    
- Broker → Redis: cruza otra conexión de red y transporta mensajes, estados de consumo y claves de idempotencia.
    
- Broker → suscriptores: el broker actúa como cliente y conecta con direcciones obtenidas de una solicitud autenticada.
    
- Operador → monitor HTTP: `/health` y `/metrics` están sujetos a token y CIDR, pero revelan disponibilidad y telemetría.
    
- Sistema de archivos/configuración → procesos: certificados, token API y credenciales de Redis entran por configuración local o `APP_CONFIG`.

### Activos Que Deben Protegerse

|   |   |
|---|---|
|Activo Objetivo||
|Token API de gRPC y HTTP|Confidencialidad e integridad|
|Credenciales de Redis|Confidencialidad|
|Contenido de mensajes y metadatos|Confidencialidad e integridad|
|Estado de ACK e idempotencia|Integridad|
|Disponibilidad del broker, Redis y clientes|Disponibilidad|
|Certificados y clave privada|Confidencialidad e integridad|
|Registros y métricas|Integridad y confidencialidad operativa|

## 5. Hipótesis De Riesgo Que Guían Las Pruebas

Estas son hipótesis, no resultados confirmados. Solo deben convertirse en hallazgos después de reproducirlas.

|   |   |   |   |
|---|---|---|---|
|ID Hipótesis Prioridad en laboratorio local Evidencia que la motiva||||
|TM-001|Una llamada gRPC sin `x-api-key` podría provocar un `panic` al acceder a `md.Get(…)[0]`, en vez de responder `Unauthenticated`.|Alta|`middlewares.go:43-53`|
|TM-002|Si faltan certificados, el broker y el SDK aceptan transporte sin TLS; el token viaja como metadato sin cifrar.|Media|`bootstraps.go:73-89`, `broker_client_factory.go:48-58`|
|TM-003|Un cliente autenticado podría hacer que el broker se conecte a destinos internos o no autorizados mediante la lista de suscriptores.|Alta|`stream_client_service.go:17-24`, `client_stream.go:29-39`|
|TM-004|Dos solicitudes simultáneas con la misma clave podrían ejecutarse antes de que la clave se guarde en Redis.|Alta|`middlewares.go:101-110`, `doc/grpc-security.md`|
|TM-005|Listas grandes de suscriptores o streams prolongados podrían consumir conexiones, goroutines y memoria sin límites de aplicación.|Media|`client_stream.go:71-79`, `stream_bidirectional_service.go:21-38`|
|TM-006|La configuración de desarrollo de Redis podría container una credencial estática y permisos demasiado amplios.|Media|`terraform/dev/redis/redis.conf:14`|
|TM-007|La reflexión gRPC facilita enumerar servicios. En local es útil; en un despliegue público ampliaría el reconocimiento.|Baja|`bootstraps.go:161-162`|
|TM-008|Las llamadas del SDK podrían quedar bloqueadas indefinidamente porque usan contextos sin fecha límite.|Media|`broker_client_conn.go:25-50`, `sqs_client_services.go:25-35`|
|TM-009|Un objeto no serializable podría producir un payload vacío porque se ignore el error de `json.Marshal`.|Media|`broker_client_services.go:24-30`, `49-55`|

## 6. Preparación Segura Del Laboratorio

### 6.1 Reglas De Operación

- Trabajar con una copia o rama de laboratorio y registrar el commit examinado.
    
- Usar tokens y certificados desechables. No utilizar credenciales de producción.
    
- Limitar las pruebas de carga a `127.0.0.1` y a un número pequeño de peticiones.
    
- No probar rangos de red, servicios ajenos ni direcciones públicas.
    
- Redactar tokens, contraseñas, cabeceras y rutas privadas antes de guardar capturas.
    
- Separar el resultado del broker del resultado del SDK. Son components con responsabilidades distintas.

### 6.2 Registrar la Línea Base

Desde Bash (Git Bash, WSL o Linux/macOS):

```Python
brokerPath="/c/Users/toonc/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/dominus-broker"
sdkPath="/c/Users/toonc/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/dominus-sdk"

git -C "$brokerPath" rev-parse HEAD
git -C "$sdkPath" rev-parse HEAD

go version
docker version
```

Guardar las salidas sin datos sensibles. Si los repositorios tienen cambios locales, anotarlo; un hash por sí solo ya no identifica todo el código evaluado.

### 6.3 Herramientas

En la inspección del equipo se detectaron:

|   |   |   |
|---|---|---|
|Herramienta Estado actual Uso previsto|||
|Go|Disponible|Tests, race detector y compilación|
|Docker|Disponible|Laboratorio aislado|
|`curl`|Disponible|Monitor HTTP|
|`govulncheck`|No detectado|Vulnerabilidades alcanzables en dependencias Go|
|`gosec`|No detectado|Reglas estáticas específicas de Go|
|`gitleaks`|No detectado|Secretos presentes o históricos|
|`grpcurl`|No detectado|Pruebas dinámicas gRPC|
|`golangci-lint`|No detectado|Calidad y patrones peligrosos|
|Trivy|No detectado|Dependencias, imagen y configuración|
|Terraform|No detectado|Validación de infraestructura local|

Instalación mínima mediante Go, revisando primero que `GOBIN` esté en `PATH`:

```Python
go install golang.org/x/vuln/cmd/ govulncheck@latest
go install github.com/securego/gosec/v2/cmd/ gosec@latest
go install github.com/fullstorydev/grpcurl/cmd/ grpcurl@latest
go install github.com/gitleaks/gitleaks/ v8@latest
```

No se debe afirmar que una herramienta fue utilizada hasta conservar su versión y su salida. Para una entrega reproducible, anotar `govulncheck -version`, `gosec -version`, `grpcurl -version` y `gitleaks version`.

## 7. Fase 1: Establecer La Línea Base Funcional

La seguridad no debe comenzar con un escáner. Primero hay que demostrar que el código evaluado compila, que sus pruebas normals pasan y que sabemos exactamente qué versión estamos ejecutando.

Esta fase establece el **punto cero**. Todo resultado de seguridad posterior debe poder compararse contra esta línea base.

### 7.0. Preparar El Entorno Bash

Todas las instrucciones de esta guía usan Bash. En Windows puede utilizarse Git Bash o WSL. Antes de continuar, comprobar:

```Python
bash --version
git --version
go version
docker version
```

Crear las variables de trabajo una sola vez:

```Python
export brokerPath='/c/Users/toonc/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/dominus-broker'
export sdkPath='/c/Users/toonc/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/dominus-sdk'

printf 'Broker: %s\n' "$brokerPath"
printf 'SDK:    %s\n' "$sdkPath"
```

> Si se utilize WSL en lugar de Git Bash, las rutas pueden necesitar el formato `/mnt/c/Users/…`.

Verificar que ambos repositorios existen:

```Python
test -d "$brokerPath" && echo "Broker OK" || echo "ERROR: broker no encontrado"
test -d "$sdkPath" && echo "SDK OK" || echo "ERROR: SDK no encontrado"
```

Si alguno falla, **detener la actividad**. No continuar cambiando rutas manualmente dentro de los commandos posteriores sin registrar la modificación.

### 7.1. Registrar Commit, Rama Y Estado Del Repositorio

Para que la evidencia sea reproducible, registrar no solamente el commit, sino también la rama y si existen cambios locales.

```Python
cd "$brokerPath"

echo "=== BROKER ==="
git branch --show-current
git rev-parse HEAD
git status --short
git diff --stat
```

Después:

```Python
cd "$sdkPath"

echo "=== SDK ==="
git branch --show-current
git rev-parse HEAD
git status --short
git diff --stat
```

Guardar la salida:

```Python
mkdir -p security-evidence
{
  echo "=== BROKER ==="
  cd "$brokerPath"
  git branch --show-current
  git rev-parse HEAD
  git status --short

  echo
  echo "=== SDK ==="
  cd "$sdkPath"
  git branch --show-current
  git rev-parse HEAD
  git status --short
} | tee security-evidence/E01-versiones-y-commits.txt
```

**Punto de control:** si `git status --short` muestra archivos modificados, esos cambios forman parte de lo que se está evaluando. No presentar después el resultado como si correspondiera exclusivamente al commit.

### 7.2. Verificar La Versión De Go Y Docker

Registrar versiones exactas:

```Python
{
  echo "=== Go ==="
  go version

  echo
  echo "=== Docker ==="
  docker version

  echo
  echo "=== Docker Compose ==="
  docker compose version 2>/dev/null || true
} | tee security-evidence/E02-versiones-herramientas.txt
```

No basta con indicar "Go instalado". La versión puede cambiar el comportamiento del compilador, dependencias o herramientas de análisis.

### 7.3. Ejecutar Las Pruebas Normals Del Broker

Primero entrar al repositorio:

```Python
cd "$brokerPath"
```

Confirmar que Go puede resolver el módulo:

```Python
go env GOMOD
go env GOPATH
go env GOMODCACHE
```

Descargar dependencias sin modificar manualmente el código:

```Python
go mod download
```

Ejecutar las pruebas normals:

```Python
go test -count=1 ./...
```

Después ejecutar el detector de carreras:

```Python
go test -race -count=1 ./...
```

Guardar ambos resultados:

```Python
go test -count=1 ./... 2>&1 | tee security-evidence/E03-go-test-broker.txt
go test -race -count=1 ./... 2>&1 | tee security-evidence/E04-go-test-race-broker.txt
```

### 7.4. Ejecutar La Cobertura Del Broker

Obtener una medición actual:

```Python
go test -coverprofile=security-evidence/broker-cover.out ./...
go tool cover -func=security-evidence/broker-cover.out \
  | tee security-evidence/E05-cobertura-broker.txt
```

Si se necesita HTML:

```Python
go tool cover \
  -html=security-evidence/broker-cover.out \
  -o security-evidence/broker-cover.html
```

La cifra documentada previamente en el repositorio no sustituye esta ejecución. La entrega debe utilizar el valor observado durante el laboratorio.

### 7.5. Ejecutar Las Pruebas Del SDK

Entrar al SDK:

```Python
cd "$sdkPath"
```

Descargar dependencias:

```Python
go mod download
```

Ejecutar pruebas:

```Python
go test -count=1 ./... 2>&1 | tee security-evidence/E06-go-test-sdk.txt
```

Y race detector:

```Python
go test -race -count=1 ./... 2>&1 | tee security-evidence/E07-go-test-race-sdk.txt
```

Si aparece:

```Python
[no test files]
```

no clasificarlo como "PASS". Significa que no existen pruebas detectables para ese paquete.

### 7.6. Punto De Decisión Antes De Continuar

No continuar con las pruebas dinámicas hasta contestar:

```Python
[ ] Broker compila.
[ ] Pruebas normales del broker terminan correctamente.
[ ] Race detector del broker termina correctamente.
[ ] SDK compila.
[ ] Pruebas del SDK fueron ejecutadas o se documentó que no existen.
[ ] Commit y cambios locales fueron registrados.
[ ] Versiones de Go y Docker fueron registradas.
```

Si una casilla falla, registrar el fallo antes de continuar.

---

## 8. Fase 2: Análisis De Dependencias, Código Y Secretos

Esta fase identifica problemas que pueden detectarse sin atacar el servicio.

El orden recomendado es:

1. Dependencias.
    
2. `go vet`.
    
3. `gosec`.
    
4. Secretos.
    
5. Infraestructura.
    
6. Revisión manual de los resultados.
    
7. Solo después, pruebas dinámicas.

### 8.1. Instalar Y Verificar Herramientas

Comprobar primero si están disponibles:

```Python
command -v govulncheck || true
command -v gosec || true
command -v grpcurl || true
command -v gitleaks || true
command -v golangci-lint || true
command -v trivy || true
command -v terraform || true
```

Si `govulncheck`, `gosec` o `grpcurl` no están disponibles y se cuenta con Go:

```Python
go install golang.org/x/vuln/cmd/ govulncheck@latest
go install github.com/securego/gosec/v2/cmd/ gosec@latest
go install github.com/fullstorydev/grpcurl/cmd/ grpcurl@latest
```

Asegurar que `$GOPATH/bin` o `$GOBIN` esté en `PATH`:

```Python
export PATH="$(go env GOPATH)/bin:$PATH"
```

Verificar:

```Python
govulncheck -version
gosec -version
grpcurl -version
```

Para herramientas que no estén disponibles, registrar explícitamente:

```Python
echo "gitleaks: $(command -v gitleaks || echo NO DISPONIBLE)"
echo "trivy: $(command -v trivy || echo NO DISPONIBLE)"
echo "terraform: $(command -v terraform || echo NO DISPONIBLE)"
```

### 8.2. Análisis De Dependencias Con `govulncheck`

Broker:

```Python
cd "$brokerPath"

govulncheck ./... 2>&1 \
  | tee security-evidence/E08-govulncheck-broker.txt
```

SDK:

```Python
cd "$sdkPath"

govulncheck ./... 2>&1 \
  | tee security-evidence/E09-govulncheck-sdk.txt
```

Para cada resultado relevante registrar:

```Python
Módulo:
Versión:
Vulnerabilidad:
Símbolo afectado:
¿Es alcanzable?:
Recomendación:
```

No convertir automáticamente "dependencia vulnerable" en "vulnerabilidad explotable". La alcanzabilidad debe formar parte de la interpretación.

### 8.3. `go vet`

Broker:

```Python
cd "$brokerPath"
go vet ./... 2>&1 | tee security-evidence/E10-go-vet-broker.txt
```

SDK:

```Python
cd "$sdkPath"
go vet ./... 2>&1 | tee security-evidence/E11-go-vet-sdk.txt
```

Un resultado limpio significa que esta herramienta no encontró las condiciones que busca; no significa que el proyecto sea seguro.

### 8.4. `gosec`

Broker:

```Python
cd "$brokerPath"

gosec -fmt=json \
  -out=security-evidence/E12-gosec-broker.json \
  ./...
```

SDK:

```Python
cd "$sdkPath"

gosec -fmt=json \
  -out=security-evidence/E13-gosec-sdk.json \
  ./...
```

Revisar primero severidades altas y medias. Para cada una:

```Python
Archivo:
Línea:
Regla:
Código:
Flujo:
Condición necesaria:
¿Reproducible?:
Impacto:
```

No corregir todos los avisos automáticamente. Primero determinar cuáles corresponden realmente a la arquitectura.

### 8.5. Detección De Secretos

Broker:

```Python
cd "$brokerPath"

gitleaks detect \
  --source . \
  --redact \
  --report-format json \
  --report-path security-evidence/E14-gitleaks-broker.json
```

SDK:

```Python
cd "$sdkPath"

gitleaks detect \
  --source . \
  --redact \
  --report-format json \
  --report-path security-evidence/E15-gitleaks-sdk.json
```

Si se va a publicar el repositorio, revisar también historial:

```Python
gitleaks git --redact --report-format json \
  --report-path security-evidence/E16-gitleaks-history.json
```

Nunca copiar el secreto a la entrega.

### 8.6. Revisar Manualmente La Configuración

Buscar nombres relacionados con secretos y transporte:

```Python
cd "$brokerPath"

grep -RniE \
  'api[_-]?key|token|password|secret|private.?key|certificate|tls|redis' \
  env terraform config 2>/dev/null \
  | tee security-evidence/E17-revision-configuracion.txt
```

Después revisar específicamente:

```Python
env/
terraform/
config/
Dockerfile
docker-compose*.yml
README*
scripts/
```

El objetivo aquí no es solamente encontrar contraseñas. También hay que comprobar:

- si TLS puede desactivarse;
    
- si existen credenciales por defecto;
    
- si Redis está publicado;
    
- si el proceso corre como root;
    
- si existen certificados dentro de la imagen;
    
- si una configuración de desarrollo puede llegar accidentalmente a producción.

### 8.7. Infraestructura Y Contenedor

Si Trivy está disponible:

```Python
cd "$brokerPath"

trivy fs \
  --scanners vuln,secret,misconfig \
  . 2>&1 | tee security-evidence/E18-trivy-filesystem.txt
```

Revisar Terraform:

```Python
trivy config ./terraform \
  2>&1 | tee security-evidence/E19-trivy-terraform.txt
```

Si Terraform está instalado:

```Python
terraform -chdir=./terraform fmt -check -recursive
terraform -chdir=./terraform validate
```

Construir una imagen de laboratorio:

```Python
docker build -t dominus-broker:security-lab .
```

Inspeccionar el usuario:

```Python
docker image inspect dominus-broker:security-lab \
  --format ' {{json .Config.User}} '
```

Escanear la imagen:

```Python
trivy image dominus-broker:security-lab \
  2>&1 | tee security-evidence/E20-trivy-image.txt
```

El `Dockerfile` ya contiene un control positivo al cambiar a un usuario sin privilegios. No eliminar ese control durante las pruebas.

---

## 9. Fase 3: Levantar El Laboratorio Antes De Las Pruebas Dinámicas

Las pruebas dinámicas deben ejecutarse contra una instancia deliberadamente aislada.

### 9.0. Crear Directorio De Evidencias

```Python
cd "$brokerPath"

mkdir -p security-evidence
chmod 700 security-evidence
```

Confirmar:

```Python
pwd
ls -ld security-evidence
```

### 9.1. Crear Credenciales Desechables

No escribir credenciales reales en el documento.

```Python
export DOMINUS_TEST_TOKEN='token-de-laboratorio-no-productivo'
```

Comprobar solamente que existe, sin imprimirlo:

```Python
if [[ -n "${DOMINUS_TEST_TOKEN:-}" ]]; then
  echo "DOMINUS_TEST_TOKEN configurado"
else
  echo "ERROR: falta DOMINUS_TEST_TOKEN"
  exit 1
fi
```

Para limpiar al terminar:

```Python
unset DOMINUS_TEST_TOKEN
```

### 9.2. Confirmar Puertos Disponibles

Antes de iniciar:

```Python
ss -ltn 2>/dev/null | grep -E ':(5000|8000)\b' || true
```

Si `ss` no existe en Git Bash, utilizar Docker:

```Python
docker ps --format 'table {{.Names}} \t {{.Ports}} '
```

No asumir que `5000` y `8000` son correctos si la configuración del proyecto utilize otros puertos. Confirmarlos en la configuración del broker.

### 9.3. Iniciar El Laboratorio

Usar el mecanismo de arranque documentado por el repositorio. Si existe un `docker compose` de laboratorio:

```Python
docker compose up -d
```

Verificar:

```Python
docker compose ps
```

Ver logs:

```Python
docker compose logs --tail=100
```

Si el proyecto se inicia directamente con Go, utilizar el commando documentado por el repositorio y guardar stdout/stderr:

```Python
go run ./cmd/api 2>&1 | tee security-evidence/E21-broker-startup.log
```

Mantener ese proceso en una terminal separada.

### 9.4. Verificar Estado Antes De Atacar

Primero comprobar que el servicio está vivo:

```Python
curl -i http://127.0.0.1:8000/health
```

Después revisar procesos/contenedores:

```Python
docker ps
```

Si el servicio está corriendo directamente:

```Python
ps aux | grep '[d]ominus'
```

Solo continuar cuando exista una línea base clara de "broker vivo".

---

## 10. Fase 4: Pruebas Dinámicas Del Backend

Cada prueba debe seguir exactamente el mismo ciclo:

```Python
Preparar
→ Ejecutar caso positivo
→ Ejecutar caso negativo
→ Verificar proceso
→ Guardar evidencia
→ Interpretar
→ Limpiar
```

Esto evita que una prueba anterior contamine la siguiente.

### BE-01. Autenticación gRPC Ante Cabecera Ausente

**Objetivo:** comprobar que una solicitud sin `x-api-key` se rechaza correctamente y no provoca `panic`.

#### Paso 1. Confirmar Que El Broker Está Vivo

```Python
curl -fsS http://127.0.0.1:8000/health
echo
```

Guardar:

```Python
curl -i http://127.0.0.1:8000/health \
  | tee security-evidence/E22-BE01-health-before.txt
```

#### Paso 2. Ejecutar Solicitud Sin Token

```Python
grpcurl -plaintext 127.0.0.1:5000 list \
  2>&1 | tee security-evidence/E23-BE01-no-token.txt
```

#### Paso 3. Verificar Inmediatamente Que El Proceso Sigue Vivo

```Python
curl -i http://127.0.0.1:8000/health \
  | tee security-evidence/E24-BE01-health-after-no-token.txt
```

#### Paso 4. Token Incorrecto

```Python
grpcurl -plaintext \
  -H 'x-api-key: token-invalido-de-laboratorio' \
  127.0.0.1:5000 list \
  2>&1 | tee security-evidence/E25-BE01-invalid-token.txt
```

#### Paso 5. Token Correcto

```Python
grpcurl -plaintext \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  127.0.0.1:5000 list \
  2>&1 | tee security-evidence/E26-BE01-valid-token.txt
```

#### Paso 6. Criterio

Esperado:

```Python
Sin token     -> Unauthenticated
Token inválido -> Unauthenticated
Token válido   -> operación permitida según configuración
Proceso        -> permanece activo
```

Si el proceso se reinicia o muere después del caso sin token, conservar el log del broker.

No afirmar todavía "vulnerabilidad confirmada" únicamente por el código. La clasificación depende del resultado real.

### BE-02. Protección Del Monitor HTTP

Sin token:

```Python
curl -i http://127.0.0.1:8000/health \
  | tee security-evidence/E27-BE02-no-token.txt
```

Token incorrecto:

```Python
curl -i \
  -H 'x-api-key: token-invalido' \
  http://127.0.0.1:8000/health \
  | tee security-evidence/E28-BE02-invalid-token.txt
```

Token válido:

```Python
curl -i \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  http://127.0.0.1:8000/health \
  | tee security-evidence/E29-BE02-valid-health.txt
```

Métricas:

```Python
curl -i \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  http://127.0.0.1:8000/metrics \
  | tee security-evidence/E30-BE02-valid-metrics.txt
```

Si la configuración permite modificar el CIDR, repetir con una red que excluya `127.0.0.1`.

También comprobar una cabecera reenviada:

```Python
curl -i \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  -H 'X-Forwarded-For: 10.0.0.10' \
  http://127.0.0.1:8000/health
```

El objetivo es verificar que esa cabecera no sustituye indebidamente la IP remota real.

### BE-03. Idempotencia Bajo Concurrencia

Esta prueba require una prueba automatizada porque enviar manualmente diez peticiones no garantiza que lleguen simultáneamente.

Crear una prueba de laboratorio en el broker:

```Python
cd "$brokerPath"

mkdir -p tests/security
touch tests/security/idempotency_security_test.go
```

La prueba debe:

1. levantar un servidor local;
    
2. preparar Redis de laboratorio;
    
3. generar una única clave de idempotencia;
    
4. sincronizar 10–20 goroutines;
    
5. enviar las solicitudes al mismo tiempo;
    
6. contar operaciones aceptadas;
    
7. contar duplicados;
    
8. repetir la prueba;
    
9. ejecutar `-race`.

Ejemplo de ejecución:

```Python
go test -race \
  -count=20 \
  ./tests/security \
  2>&1 | tee security-evidence/E31-BE03-idempotencia.txt
```

**Criterio esperado:** exactamente una solicitud ejecuta la operación y las demás se rechazan como duplicadas.

Si más de una alcanza el handler, el resultado debe conservarse como evidencia de una condición de carrera reproducible.

### BE-04. Destinos De Suscriptores

Esta prueba debe utilizar exclusivamente loopback.

Levantar un receptor de prueba:

```Python
nc -l 127.0.0.1 9000
```

Si el protocolo require gRPC real, utilizar un servidor gRPC de prueba en lugar de `nc`.

Enviar desde el cliente una dirección como:

```Python
127.0.0.1:9000
```

Observar si el broker intenta establecer la conexión.

Registrar:

```Python
Destino enviado:
Destino aceptado/rechazado:
Conexión observada:
Política que debería aplicarse:
```

No probar:

```Python
169.254.169.254
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
IPs de la LAN
servicios públicos
```

El objetivo es demostrar el comportamiento del control, no explorar redes.

### BE-05. Límites De Payload, Suscriptores Y Streams

Registrar estado inicial:

```Python
ps -o pid,rss,vsz,comm -C dominus-broker 2>/dev/null || true
```

Si corre en Docker:

```Python
docker stats --no-stream
```

Probar tamaños:

```Python
1 KiB
64 KiB
1 MiB
4 MiB máximo para este laboratorio
```

No saltar directamente al máximo. Registrar para cada tamaño:

```Python
Payload:
Latencia:
Código:
Memoria:
Goroutines:
Proceso vivo:
```

Para streams, utilizar un máximo conservador de 20 conexiones y cerrarlas todas al terminar.

El resultado buscado no es "lograr una caída", sino identificar si existe un límite explícito y observable.

### BE-06. TLS Y Degradación A Texto Plano

Construir cuatro escenarios:

```Python
A. CA válida + nombre válido
B. CA incorrecta
C. nombre incorrecto
D. certificado ausente
```

Para A se espera conexión exitosa.

Para B y C se espera rechazo de verificación.

Para D se debe documentar si el sistema falla cerrado o cambia automáticamente a plaintext.

Comprobar además la configuración efectiva, no solamente los archivos:

```Python
grep -RniE 'tls|plaintext|insecure|certificate|ca' \
  . --exclude-dir=.git \
  | tee security-evidence/E32-BE06-tls-config.txt
```

El token no está protegido por aplicar SHA-256 al valor en el servidor. La confidencialidad durante el tránsito depende de TLS.

### BE-07. Redis Y Privilegios

Comprobar contenedores:

```Python
docker ps --format 'table {{.Names}} \t {{.Ports}} \t {{.Networks}} '
```

Identificar Redis:

```Python
docker ps --format ' {{.Names}} ' | grep -i redis
```

Inspeccionar puertos publicados:

```Python
docker port <redis-container>
```

Si no debe estar expuesto al host, no debería aparecer un puerto público innecesario.

Revisar configuración:

```Python
grep -RniE 'acl|user|password|tls|port|bind' \
  terraform env . \
  --exclude-dir=.git \
  | tee security-evidence/E33-BE07-redis-config.txt
```

Comprobar que las claves de idempotencia tienen expiración y que un error de Redis no imprime credenciales.

---

## 11. Fase 5: Pruebas De La Interfaz Cliente `dominus-sdk`

Aquí se evalúa el SDK como interfaz de consumo porque no existe una interfaz gráfica dentro del proyecto.

Crear rama de laboratorio:

```Python
cd "$sdkPath"

git switch -c security-lab-tests
```

Crear estructura:

```Python
mkdir -p dominus/security
```

La prueba debe usar servidores gRPC locales y certificados efímeros.

### CL-01. Validación TLS Del Servidor

Preparar cuatro casos:

```Python
CA válida + SAN correcto       -> éxito
CA distinta                    -> rechazo
SAN/nombre incorrecto          -> rechazo
CA inexistente                 -> error de inicialización
```

Ejecutar:

```Python
go test -v ./dominus/security \
  -run TestTLS \
  2>&1 | tee security-evidence/E34-CL01-tls.txt
```

No registrar certificados privados ni tokens en stdout.

### CL-02. Metadata De Autenticación

El servidor de prueba debe registrar solamente:

```Python
x-api-key presente: sí/no
longitud del token: N
idempotency-header presente: sí/no
```

Nunca:

```Python
valor del token
valor completo de la clave
credenciales
```

Ejecutar:

```Python
go test -v ./dominus/security \
  -run TestMetadata \
  2>&1 | tee security-evidence/E35-CL02-metadata.txt
```

### CL-03. Validación Y Autorización De Destinos

Separar dos conceptos:

```Python
Validación sintáctica = "parece una dirección"
Autorización           = "está permitido conectarse allí"
```

Probar al menos:

```Python
127.0.0.1:5000
hostname.test:5000
hostname.test:99999
hostname.test/path
loopback no autorizado
destino incluido en allowlist
destino fuera de allowlist
```

La regex del SDK no debe considerarse una política de seguridad completa.

### CL-04. Cancelación Y Tiempo Límite

Crear servidor que acepte una conexión y no responda.

La prueba debe intentar terminar en aproximadamente 1–2 segundos.

Ejecutar:

```Python
go test -v ./dominus/security \
  -run TestTimeout \
  2>&1 | tee security-evidence/E36-CL04-timeout.txt
```

Esperado:

```Python
DeadlineExceeded
conexión liberada
test termina dentro del límite
```

Si el SDK construye internamente `context.Background()` y no permite que el consumidor suministre un contexto, documentar esa limitación.

### CL-05. Error De Serialización

Crear un valor que `encoding/json` no pueda serializar, por ejemplo una función o canal.

El comportamiento correcto es:

```Python
Marshal falla
→ se devuelve error
→ no se llama Send
```

Ejecutar:

```Python
go test -v ./dominus/security \
  -run TestSerializationError \
  2>&1 | tee security-evidence/E37-CL05-serialization.txt
```

Si el error se descarta y se envía un payload vacío, documentarlo como pérdida potential de integridad.

### CL-06. Ciclo De Vida De Conexiones

Registrar antes:

```Python
ps -eLf | grep '[d]ominus' | wc -l
```

Ejecutar operaciones acotadas:

```Python
go test -v ./dominus/security \
  -run TestConnectionLifecycle \
  2>&1 | tee security-evidence/E38-CL06-connections.txt
```

Registrar después:

```Python
ps -eLf | grep '[d]ominus' | wc -l
```

La comparación debe hacerse después de permitir que las conexiones terminen normalmente. No interpretar una goroutine temporal como fuga sin verificar su ciclo de vida.

---

## 12. Fase 6: Corrección De Hallazgos Y Regresión

No corregir varios hallazgos simultáneamente. La trazabilidad debe set:

```Python
Hallazgo
→ reproducción
→ corrección
→ test de regresión
→ pruebas completas
→ nuevo resultado
```

### 12.1. Crear Una Rama De Corrección

Broker:

```Python
cd "$brokerPath"
git switch -c security/fixes
```

SDK:

```Python
cd "$sdkPath"
git switch -c security/fixes
```

### 12.2. Registrar El Hallazgo Antes De Modificar

Ejemplo:

```Python
ID: BE-01
Componente: dominus-broker
Archivo: middlewares.go
Riesgo: fallo ante metadata ausente
Resultado actual: [RESULTADO REAL]
Evidencia: E23-BE01-no-token.txt
```

### 12.3. Crear La Prueba De Regresión

La prueba debe fallar antes de la corrección y pasar después.

Ejecutar primero:

```Python
go test ./... -run 'TestNombreDeRegresion'
```

Conservar el resultado previo.

Aplicar la corrección.

Ejecutar nuevamente:

```Python
go test ./... -run 'TestNombreDeRegresion'
```

Después:

```Python
go test -race ./...
```

La regresión debe permanecer en el repositorio. No eliminarla después de comprobar que la corrección funciona.

---

## 13. Fase 7: Repetición Completa Después De Las Correcciones

Después de corregir un hallazgo, repetir como mínimo:

```Python
go test -race -count=1 ./...
govulncheck ./...
go vet ./...
gosec ./...
```

Para el SDK:

```Python
cd "$sdkPath"

go test -race -count=1 ./...
govulncheck ./...
go vet ./...
gosec ./...
```

Volver a ejecutar la prueba dinámica afectada.

Por ejemplo, después de corregir BE-01:

```Python
grpcurl -plaintext 127.0.0.1:5000 list
curl -i http://127.0.0.1:8000/health
```

Comparar:

```Python
Resultado antes:
Resultado después:
Evidencia antes:
Evidencia después:
```

No reemplazar la evidencia anterior. Conservar ambas.

---

## 14. Fase 8: Organización De Evidencias

Crear una estructura estable:

```Python
mkdir -p security-evidence/{baseline,static,dynamic,regression}
```

Mover o guardar:

```Python
baseline/
  commits
  versiones
  go-test
  race

static/
  govulncheck
  gosec
  gitleaks
  trivy

dynamic/
  BE-01
  BE-02
  BE-03
  BE-04
  BE-05
  BE-06
  BE-07
  CL-01
  CL-02
  CL-03
  CL-04
  CL-05
  CL-06

regression/
  pruebas antes
  pruebas después
```

Listar:

```Python
find security-evidence -type f -maxdepth 3 \
  | sort \
  | tee security-evidence/E39-inventario-evidencias.txt
```

Antes de entregar:

```Python
grep -RniE \
  'token-[^ ]+|password=[^ ]+|BEGIN .*PRIVATE KEY|api[_-]?key' \
  security-evidence \
  || true
```

Esta búsqueda es una revisión auxiliary. También inspeccionar manualmente capturas.

---

## 15. Selección Mínima Para La Rúbrica

Si la entrega solamente permite dos pruebas principales, seleccionar:

### Backend

`BE-01: autenticación gRPC ante token ausente, incorrecto y válido`.

Debe incluir:

```Python
Objetivo
Riesgo
Versión
Preparación
Comando sin token
Comando con token incorrecto
Comando con token correcto
Comprobación de proceso
Resultado real
Evidencia
Recomendación
Regresión
```

### Interfaz Cliente

`CL-01: rechazo de certificado o nombre TLS no confiable por dominus-sdk`.

Debe incluir:

```Python
Objetivo
Certificado utilizado
CA
SAN/serverName
Resultado esperado
Resultado real
Evidencia
Regresión
```

Como pruebas complementarias:

```Python
BE-03 -> idempotencia
BE-04 -> destinos salientes
CL-04 -> timeout
CL-05 -> serialización
```

---

## 16. Plantilla Para Documentar Cada Ejecución

Cada prueba debe producir una ficha como esta:

|   |   |
|---|---|
|Campo|Contenido|
|Identificador|BE-01, CL-01, etc.|
|Fecha|Fecha real de ejecución|
|Commit|Hash real|
|Rama|Rama real|
|Componente|Broker o SDK|
|Objetivo|Propiedad de seguridad|
|Riesgo|Impacto si falla|
|Preparación|Servicios y configuración|
|Entrada|Datos ficticios/redactados|
|Commando|Commando Bash ejecutado|
|Resultado esperado|Comportamiento seguro|
|Resultado observado|Salida real|
|Estado|Aprobada / Fallida / Inconclusa|
|Severidad|Baja / Media / Alta / Crítica|
|Evidencia|Archivo de evidencia|
|Corrección|Cambio realizado|
|Regresión|Test asociado|

### Regla Importante

Nunca escribir primero:

> "La prueba pasó."

Primero guardar:

```Python
comando
+
salida
+
estado del proceso
+
evidencia
```

Después interpretar.

---

## 17. Orden Completo Recomendado De Ejecución

Este es el orden que evita los saltos que existían en la guía original:

```Python
1. Abrir Bash
2. Definir brokerPath y sdkPath
3. Verificar directorios
4. Registrar rama y commit
5. Registrar cambios locales
6. Registrar versiones de Go/Docker
7. Descargar dependencias
8. Ejecutar go test
9. Ejecutar go test -race
10. Ejecutar cobertura
11. Ejecutar pruebas del SDK
12. Instalar herramientas faltantes
13. Verificar versiones de herramientas
14. Ejecutar govulncheck
15. Ejecutar go vet
16. Ejecutar gosec
17. Ejecutar gitleaks
18. Revisar configuración manualmente
19. Revisar Terraform/Trivy
20. Construir imagen de laboratorio
21. Crear directorio de evidencias
22. Crear token desechable
23. Verificar puertos
24. Levantar Redis
25. Levantar broker
26. Verificar /health
27. Ejecutar BE-01
28. Verificar /health después de BE-01
29. Ejecutar BE-02
30. Verificar proceso
31. Crear prueba automatizada BE-03
32. Ejecutar BE-03 con race detector
33. Ejecutar BE-04 solo con loopback
34. Ejecutar BE-05 con límites conservadores
35. Ejecutar BE-06
36. Ejecutar BE-07
37. Crear pruebas CL-01 a CL-06
38. Ejecutar pruebas del SDK
39. Registrar hallazgos
40. Crear rama de corrección
41. Crear regresión del primer hallazgo
42. Corregir
43. Ejecutar regresión
44. Ejecutar suite completa
45. Repetir prueba dinámica
46. Comparar antes/después
47. Revisar evidencias
48. Redactar únicamente resultados reales
49. Limpiar credenciales
50. Detener el laboratorio
```

### Commandos De Limpieza

Al finalizar:

```Python
unset DOMINUS_TEST_TOKEN
```

Si se utilizó Docker Compose:

```Python
docker compose down
```

Si se creó un contenedor de prueba independiente:

```Python
docker rm -f <container-name>
```

Verificar que no quedan procesos del laboratorio:

```Python
docker ps
```

Y verificar que los puertos se liberaron:

```Python
ss -ltn 2>/dev/null | grep -E ':(5000|8000)\b' || true
```

---

## 18. Criterio De Finalización

La actividad estará lista cuando:

```Python
[ ] El commit evaluado está documentado.
[ ] Los cambios locales están documentados.
[ ] Las versiones de herramientas están documentadas.
[ ] Broker compiló.
[ ] Race detector fue ejecutado.
[ ] SDK fue probado o se documentó ausencia de tests.
[ ] govulncheck fue ejecutado.
[ ] go vet fue ejecutado.
[ ] gosec fue ejecutado.
[ ] gitleaks fue ejecutado o su ausencia quedó documentada.
[ ] El laboratorio utiliza credenciales desechables.
[ ] BE-01 tiene resultado real.
[ ] BE-02 tiene resultado real.
[ ] BE-03 tiene prueba automatizada si se incluye.
[ ] CL-01 tiene resultado real.
[ ] Las capturas no contienen secretos.
[ ] Cada hallazgo apunta a archivo/línea.
[ ] Cada corrección tiene regresión.
[ ] Las pruebas fueron repetidas después de corregir.
[ ] La entrega distingue hipótesis de hechos observados.
```

La conclusión académica debe basarse exclusivamente en los resultados obtenidos.

No escribir:

> "El sistema es seguro."

Preferir:

> "En el entorno local evaluado, con el commit X y la configuración Y, las pruebas BE-01 y CL-01 produjeron los resultados Z. No se observaron [condiciones específicas] durante esta ejecución. Las limitaciones del laboratorio impiden extrapolar el resultado a una exposición pública."

---

## 19. Rutas Prioritarias Para Revisión Manual

Mantener como prioridad:

```Python
dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go
dominus-broker/internal/bootstraps/bootstraps.go
dominus-broker/internal/infrastructure/grpc/outbound/client_stream.go
dominus-broker/internal/application/usecases/stream_*
dominus-broker/internal/infrastructure/redis
dominus-broker/internal/infrastructure/fasthttp
dominus-broker/config/config.go
dominus-broker/env
dominus-broker/terraform
dominus-broker/Dockerfile
dominus-sdk/dominus/interceptors.go
dominus-sdk/dominus/*_client_factory.go
dominus-sdk/dominus/broker_client_conn.go
dominus-sdk/dominus/broker_client_services.go
dominus-sdk/dominus/rules.go
```

La revisión manual debe responder, para cada ruta:

```Python
¿Qué entrada controla este código?
¿Quién puede proporcionar esa entrada?
¿Cruza una frontera de confianza?
¿Qué validación existe?
¿Qué ocurre si falta?
¿Qué ocurre si es maliciosa?
¿Hay un límite?
¿Hay timeout?
¿Se registra información sensible?
¿Existe una prueba automatizada?
```

---

## 20. Regla Final Para La Entrega

Las hipótesis TM-001 a TM-009 siguen siendo hipótesis hasta que una ejecución reproducible las confirme.

La evidencia debe conservar la secuencia:

```Python
Código observado
→ hipótesis
→ preparación
→ comando
→ salida real
→ interpretación
→ impacto
→ corrección
→ regresión
```

Esta secuencia es especialmente importante a partir de la Fase 1 porque evita saltar directamente desde la revisión estática a una conclusión de vulnerabilidad.

La guía utilize Bash de forma consistente y cada prueba incluye ahora los pasos intermedios necesarios para llegar desde una máquina limpia hasta una evidencia reproducible.

## [Library](https://chatgpt.com/library) /Guia_Ciberseguridad_Dominus_Bash_Expandida.md

# Guía Intensiva Para El Análisis De Ciberseguridad De Dominus

## 1. Propósito Y Criterio De la Actividad

Esta guía sirve para preparar la sección de ciberseguridad de la actividad "Pruebas de la herramienta". El análisis cubre estos components:

- `dominus-broker`: servicio backend escrito en Go que expone APIs gRPC, endpoints HTTP de salud y métricas, conexiones salientes hacia suscriptores y persistencia en Redis.
    
- `dominus-sdk`: biblioteca Go utilizada por las aplicaciones cliente para conectarse al broker, enviar metadatos de autenticación y consumir las operaciones Broker y SQS.

El entorno evaluado es local. No se presupone exposición a Internet, usuarios anónimos ni datos personales reales. Esto reduce la probabilidad de explotación remota, pero no elimina los problemas que pueden causar caída del proceso, filtración de credenciales dentro de la red local, conexiones hacia destinos no autorizados o duplicación de operaciones.

### Justificación Del SDK Como Interfaz Cliente

El proyecto no contiene una interfaz gráfica. Por esta razón, para la rúbrica se considera `dominus-sdk` como la interfaz mediante la cual otro software utilize el backend. El SDK valida direcciones, establece conexiones gRPC, agrega el token de acceso y la clave de idempotencia, serializa mensajes y presenta las operaciones que consume una aplicación. La prueba del lado cliente comprobará estos comportamientos, no aspectos visuals como XSS, formularios, cookies o DOM.

Texto sugerido para la entrega:

> Dominus no dispone de una interfaz gráfica. Su interfaz de consumo es el paquete `dominus-sdk`, que encapsula la conexión de las aplicaciones cliente con el servicio gRPC. Por ello, la prueba de seguridad de la interfaz se aplicó al SDK y se centró en validación de destinos, protección del canal TLS, envío de credenciales, control de errores y límites de tiempo. Las pruebas propias de un navegador, como XSS, CSRF o seguridad de cookies, no son aplicables a la arquitectura evaluada.

Conviene confirmar esta interpretación con el docente. Si "front-end" se entiende estrictamente como interfaz gráfica, el proyecto necesitaría una aplicación consumidora adicional; no sería correcto inventar una UI que no forma parte del alcance.

## 2. Qué Exige Realmente la Rúbrica

La rúbrica pide describir una prueba de seguridad en backend y otra en front-end. Para obtener una evidencia defendible, cada prueba debe incluir:

1. Objetivo y riesgo que se intenta detectar.
    
2. Componente y versión examinados.
    
3. Herramienta o técnica empleada.
    
4. Preparación del laboratorio.
    
5. Entradas utilizadas, sin revelar credenciales reales.
    
6. Resultado esperado.
    
7. Resultado observado.
    
8. Evidencia: salida de consola, captura, registro o prueba automatizada.
    
9. Interpretación del resultado.
    
10. Recomendación y prueba de regresión.

No basta con pegar el resultado de un escáner. La parte valiosa es explicar qué significa el resultado en esta arquitectura.

## 3. Evidencia Inicial Del Repositorio

La revisión estática inicial permite trazar el siguiente mapa:

|Elemento Evidencia en el repositorio Relevancia de seguridad|||
|---|---|---|
|Entrada del servicio|`dominus-broker/cmd/api/main.go:43-46`|Arranca el bootstrap a partir de opciones CLI.|
|Listener gRPC|`dominus-broker/internal/bootstraps/bootstraps.go:161-173`|La reflexión está activa y el servicio escucha en todas las interfaces.|
|Listener HTTP|`dominus-broker/internal/bootstraps/bootstraps.go:178-217`|Expone `/health` y `/metrics`, con token y filtro de red.|
|Autenticación gRPC|`dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go:41-55`|Compara el token en tiempo constante, pero el acceso al primer encabezado require una prueba negativa.|
|Idempotencia|`dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go:86-112`|Comprueba Redis y guarda la clave de forma asíncrona; existe una ventana de carrera documentada.|
|Autenticación HTTP|`dominus-broker/internal/infrastructure/fasthttp/middlewares/api_middleware.go:27-42`|Protege las rutas mediante `x-api-key`.|
|Restricción HTTP por red|`dominus-broker/internal/infrastructure/fasthttp/middlewares/host_allowed.go:24-34`|Usa la IP remota contra un CIDR. El nombre `allow_origins` puede confundirse con CORS.|
|Destinos de suscriptores|`dominus-broker/internal/application/usecases/stream_client/stream_client_service.go:13-32`|Las direcciones suministradas por el cliente se pasan al cliente saliente.|
|Conexiones salientes|`dominus-broker/internal/infrastructure/grpc/outbound/client_stream.go:29-79`|El broker abre conexiones gRPC y goroutines hacia los destinos recibidos.|
|Redis|`dominus-broker/internal/infrastructure/redis/cmemory/outbound.go:21-49`|Admite TLS y credenciales; la configuración de desarrollo merece revisión de privilegios.|
|Cliente sin TLS|`dominus-sdk/dominus/broker_client_factory.go:48-58` y `sqs_client_factory.go:46-56`|Existe un modo explícito con credenciales de transporte inseguras para desarrollo.|
|Cliente con TLS|`dominus-sdk/dominus/broker_client_factory.go:28-45` y `sqs_client_factory.go:26-43`|Carga una CA y valida el nombre del servidor.|
|Metadatos cliente|`dominus-sdk/dominus/interceptors.go:23-42`|Envía `x-api-key`; las llamadas unary también envían idempotencia.|
|Validación de direcciones|`dominus-sdk/dominus/rules.go:9-16` y `enum.go:33-34`|Valida el formato con una expresión regular, pero no determina si el destino está autorizado.|
|Contextos del SDK|`dominus-sdk/dominus/broker_client_conn.go:25-50` y `sqs_client_services.go:25-35`|Usa `context.Background()`, por lo que el consumidor no puede imponer cancelación o fecha límite.|
|Serialización del SDK|`dominus-sdk/dominus/broker_client_services.go:22-33` y `47-60`|El error de `json.Marshal` se descarta.|
|Contenedor|`dominus-broker/Dockerfile:27-32`|El proceso cambia a un usuario sin privilegios, lo cual es un control existente.|
|Automatización|`dominus-broker/Makefile.ps1:277-306`|Ya contempla lint, `govulncheck`, auditoría y verificación previa al despliegue.|

El inventario encontró 50 funciones `Test…` bajo `dominus-broker/tests` y ninguna en `dominus-sdk`. Este conteo describe el estado del código; no significa que las pruebas hayan pasado.

## 4. Modelo Compacto Del Sistema

```Python
flowchart LR
  U["Aplicación cliente"] -->|API Go| SDK["dominus sdk"]
  SDK -->|gRPC y metadatos| B["dominus broker"]
  B -->|Redis protocol| R["Redis"]
  B -->|gRPC saliente| S["Suscriptores"]
  O["Operador local"] -->|HTTP| M["Salud y métricas"]
  M --> B
  C["Configuración y certificados"] --> B
  C --> SDK
```

### Límites De Confianza

- Aplicación cliente → SDK: recibe cuerpos arbitrarios, destinos, token y clave de idempotencia proporcionados por la aplicación.
    
- SDK → broker: cruza una frontera de red gRPC. La autenticación depende de `x-api-key`; la confidencialidad depende de seleccionar TLS.
    
- Broker → Redis: cruza otra conexión de red y transporta mensajes, estados de consumo y claves de idempotencia.
    
- Broker → suscriptores: el broker actúa como cliente y conecta con direcciones obtenidas de una solicitud autenticada.
    
- Operador → monitor HTTP: `/health` y `/metrics` están sujetos a token y CIDR, pero revelan disponibilidad y telemetría.
    
- Sistema de archivos/configuración → procesos: certificados, token API y credenciales de Redis entran por configuración local o `APP_CONFIG`.

### Activos Que Deben Protegerse

|   |   |
|---|---|
|Activo Objetivo||
|Token API de gRPC y HTTP|Confidencialidad e integridad|
|Credenciales de Redis|Confidencialidad|
|Contenido de mensajes y metadatos|Confidencialidad e integridad|
|Estado de ACK e idempotencia|Integridad|
|Disponibilidad del broker, Redis y clientes|Disponibilidad|
|Certificados y clave privada|Confidencialidad e integridad|
|Registros y métricas|Integridad y confidencialidad operativa|

## 5. Hipótesis De Riesgo Que Guían Las Pruebas

Estas son hipótesis, no resultados confirmados. Solo deben convertirse en hallazgos después de reproducirlas.

|   |   |   |   |
|---|---|---|---|
|ID Hipótesis Prioridad en laboratorio local Evidencia que la motiva||||
|TM-001|Una llamada gRPC sin `x-api-key` podría provocar un `panic` al acceder a `md.Get(…)[0]`, en vez de responder `Unauthenticated`.|Alta|`middlewares.go:43-53`|
|TM-002|Si faltan certificados, el broker y el SDK aceptan transporte sin TLS; el token viaja como metadato sin cifrar.|Media|`bootstraps.go:73-89`, `broker_client_factory.go:48-58`|
|TM-003|Un cliente autenticado podría hacer que el broker se conecte a destinos internos o no autorizados mediante la lista de suscriptores.|Alta|`stream_client_service.go:17-24`, `client_stream.go:29-39`|
|TM-004|Dos solicitudes simultáneas con la misma clave podrían ejecutarse antes de que la clave se guarde en Redis.|Alta|`middlewares.go:101-110`, `doc/grpc-security.md`|
|TM-005|Listas grandes de suscriptores o streams prolongados podrían consumir conexiones, goroutines y memoria sin límites de aplicación.|Media|`client_stream.go:71-79`, `stream_bidirectional_service.go:21-38`|
|TM-006|La configuración de desarrollo de Redis podría container una credencial estática y permisos demasiado amplios.|Media|`terraform/dev/redis/redis.conf:14`|
|TM-007|La reflexión gRPC facilita enumerar servicios. En local es útil; en un despliegue público ampliaría el reconocimiento.|Baja|`bootstraps.go:161-162`|
|TM-008|Las llamadas del SDK podrían quedar bloqueadas indefinidamente porque usan contextos sin fecha límite.|Media|`broker_client_conn.go:25-50`, `sqs_client_services.go:25-35`|
|TM-009|Un objeto no serializable podría producir un payload vacío porque se ignore el error de `json.Marshal`.|Media|`broker_client_services.go:24-30`, `49-55`|

## 6. Preparación Segura Del Laboratorio

### 6.1 Reglas De Operación

- Trabajar con una copia o rama de laboratorio y registrar el commit examinado.
    
- Usar tokens y certificados desechables. No utilizar credenciales de producción.
    
- Limitar las pruebas de carga a `127.0.0.1` y a un número pequeño de peticiones.
    
- No probar rangos de red, servicios ajenos ni direcciones públicas.
    
- Redactar tokens, contraseñas, cabeceras y rutas privadas antes de guardar capturas.
    
- Separar el resultado del broker del resultado del SDK. Son components con responsabilidades distintas.

### 6.2 Registrar la Línea Base

Desde Bash (Git Bash, WSL o Linux/macOS):

```Python
brokerPath="/c/Users/toonc/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/dominus-broker"
sdkPath="/c/Users/toonc/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/dominus-sdk"

git -C "$brokerPath" rev-parse HEAD
git -C "$sdkPath" rev-parse HEAD

go version
docker version
```

Guardar las salidas sin datos sensibles. Si los repositorios tienen cambios locales, anotarlo; un hash por sí solo ya no identifica todo el código evaluado.

### 6.3 Herramientas

En la inspección del equipo se detectaron:

|   |   |   |
|---|---|---|
|Herramienta Estado actual Uso previsto|||
|Go|Disponible|Tests, race detector y compilación|
|Docker|Disponible|Laboratorio aislado|
|`curl`|Disponible|Monitor HTTP|
|`govulncheck`|No detectado|Vulnerabilidades alcanzables en dependencias Go|
|`gosec`|No detectado|Reglas estáticas específicas de Go|
|`gitleaks`|No detectado|Secretos presentes o históricos|
|`grpcurl`|No detectado|Pruebas dinámicas gRPC|
|`golangci-lint`|No detectado|Calidad y patrones peligrosos|
|Trivy|No detectado|Dependencias, imagen y configuración|
|Terraform|No detectado|Validación de infraestructura local|

Instalación mínima mediante Go, revisando primero que `GOBIN` esté en `PATH`:

```Python
go install golang.org/x/vuln/cmd/ govulncheck@latest
go install github.com/securego/gosec/v2/cmd/ gosec@latest
go install github.com/fullstorydev/grpcurl/cmd/ grpcurl@latest
go install github.com/gitleaks/gitleaks/ v8@latest
```

No se debe afirmar que una herramienta fue utilizada hasta conservar su versión y su salida. Para una entrega reproducible, anotar `govulncheck -version`, `gosec -version`, `grpcurl -version` y `gitleaks version`.

## 7. Fase 1: Establecer La Línea Base Funcional

La seguridad no debe comenzar con un escáner. Primero hay que demostrar que el código evaluado compila, que sus pruebas normals pasan y que sabemos exactamente qué versión estamos ejecutando.

Esta fase establece el **punto cero**. Todo resultado de seguridad posterior debe poder compararse contra esta línea base.

### 7.0. Preparar El Entorno Bash

Todas las instrucciones de esta guía usan Bash. En Windows puede utilizarse Git Bash o WSL. Antes de continuar, comprobar:

```Python
bash --version
git --version
go version
docker version
```

Crear las variables de trabajo una sola vez:

```Python
export brokerPath='/c/Users/toonc/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/dominus-broker'
export sdkPath='/c/Users/toonc/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/10-Proyecto-de-Applicacion/Referance/dominus-sdk'

printf 'Broker: %s\n' "$brokerPath"
printf 'SDK:    %s\n' "$sdkPath"
```

> Si se utilize WSL en lugar de Git Bash, las rutas pueden necesitar el formato `/mnt/c/Users/…`.

Verificar que ambos repositorios existen:

```Python
test -d "$brokerPath" && echo "Broker OK" || echo "ERROR: broker no encontrado"
test -d "$sdkPath" && echo "SDK OK" || echo "ERROR: SDK no encontrado"
```

Si alguno falla, **detener la actividad**. No continuar cambiando rutas manualmente dentro de los commandos posteriores sin registrar la modificación.

### 7.1. Registrar Commit, Rama Y Estado Del Repositorio

Para que la evidencia sea reproducible, registrar no solamente el commit, sino también la rama y si existen cambios locales.

```Python
cd "$brokerPath"

echo "=== BROKER ==="
git branch --show-current
git rev-parse HEAD
git status --short
git diff --stat
```

Después:

```Python
cd "$sdkPath"

echo "=== SDK ==="
git branch --show-current
git rev-parse HEAD
git status --short
git diff --stat
```

Guardar la salida:

```Python
mkdir -p security-evidence
{
  echo "=== BROKER ==="
  cd "$brokerPath"
  git branch --show-current
  git rev-parse HEAD
  git status --short

  echo
  echo "=== SDK ==="
  cd "$sdkPath"
  git branch --show-current
  git rev-parse HEAD
  git status --short
} | tee security-evidence/E01-versiones-y-commits.txt
```

**Punto de control:** si `git status --short` muestra archivos modificados, esos cambios forman parte de lo que se está evaluando. No presentar después el resultado como si correspondiera exclusivamente al commit.

### 7.2. Verificar La Versión De Go Y Docker

Registrar versiones exactas:

```Python
{
  echo "=== Go ==="
  go version

  echo
  echo "=== Docker ==="
  docker version

  echo
  echo "=== Docker Compose ==="
  docker compose version 2>/dev/null || true
} | tee security-evidence/E02-versiones-herramientas.txt
```

No basta con indicar "Go instalado". La versión puede cambiar el comportamiento del compilador, dependencias o herramientas de análisis.

### 7.3. Ejecutar Las Pruebas Normals Del Broker

Primero entrar al repositorio:

```Python
cd "$brokerPath"
```

Confirmar que Go puede resolver el módulo:

```Python
go env GOMOD
go env GOPATH
go env GOMODCACHE
```

Descargar dependencias sin modificar manualmente el código:

```Python
go mod download
```

Ejecutar las pruebas normals:

```Python
go test -count=1 ./...
```

Después ejecutar el detector de carreras:

```Python
go test -race -count=1 ./...
```

Guardar ambos resultados:

```Python
go test -count=1 ./... 2>&1 | tee security-evidence/E03-go-test-broker.txt
go test -race -count=1 ./... 2>&1 | tee security-evidence/E04-go-test-race-broker.txt
```

### 7.4. Ejecutar La Cobertura Del Broker

Obtener una medición actual:

```Python
go test -coverprofile=security-evidence/broker-cover.out ./...
go tool cover -func=security-evidence/broker-cover.out \
  | tee security-evidence/E05-cobertura-broker.txt
```

Si se necesita HTML:

```Python
go tool cover \
  -html=security-evidence/broker-cover.out \
  -o security-evidence/broker-cover.html
```

La cifra documentada previamente en el repositorio no sustituye esta ejecución. La entrega debe utilizar el valor observado durante el laboratorio.

### 7.5. Ejecutar Las Pruebas Del SDK

Entrar al SDK:

```Python
cd "$sdkPath"
```

Descargar dependencias:

```Python
go mod download
```

Ejecutar pruebas:

```Python
go test -count=1 ./... 2>&1 | tee security-evidence/E06-go-test-sdk.txt
```

Y race detector:

```Python
go test -race -count=1 ./... 2>&1 | tee security-evidence/E07-go-test-race-sdk.txt
```

Si aparece:

```Python
[no test files]
```

no clasificarlo como "PASS". Significa que no existen pruebas detectables para ese paquete.

### 7.6. Punto De Decisión Antes De Continuar

No continuar con las pruebas dinámicas hasta contestar:

```Python
[ ] Broker compila.
[ ] Pruebas normales del broker terminan correctamente.
[ ] Race detector del broker termina correctamente.
[ ] SDK compila.
[ ] Pruebas del SDK fueron ejecutadas o se documentó que no existen.
[ ] Commit y cambios locales fueron registrados.
[ ] Versiones de Go y Docker fueron registradas.
```

Si una casilla falla, registrar el fallo antes de continuar.

---

## 8. Fase 2: Análisis De Dependencias, Código Y Secretos

Esta fase identifica problemas que pueden detectarse sin atacar el servicio.

El orden recomendado es:

1. Dependencias.
    
2. `go vet`.
    
3. `gosec`.
    
4. Secretos.
    
5. Infraestructura.
    
6. Revisión manual de los resultados.
    
7. Solo después, pruebas dinámicas.

### 8.1. Instalar Y Verificar Herramientas

Comprobar primero si están disponibles:

```Python
command -v govulncheck || true
command -v gosec || true
command -v grpcurl || true
command -v gitleaks || true
command -v golangci-lint || true
command -v trivy || true
command -v terraform || true
```

Si `govulncheck`, `gosec` o `grpcurl` no están disponibles y se cuenta con Go:

```Python
go install golang.org/x/vuln/cmd/ govulncheck@latest
go install github.com/securego/gosec/v2/cmd/ gosec@latest
go install github.com/fullstorydev/grpcurl/cmd/ grpcurl@latest
```

Asegurar que `$GOPATH/bin` o `$GOBIN` esté en `PATH`:

```Python
export PATH="$(go env GOPATH)/bin:$PATH"
```

Verificar:

```Python
govulncheck -version
gosec -version
grpcurl -version
```

Para herramientas que no estén disponibles, registrar explícitamente:

```Python
echo "gitleaks: $(command -v gitleaks || echo NO DISPONIBLE)"
echo "trivy: $(command -v trivy || echo NO DISPONIBLE)"
echo "terraform: $(command -v terraform || echo NO DISPONIBLE)"
```

### 8.2. Análisis De Dependencias Con `govulncheck`

Broker:

```Python
cd "$brokerPath"

govulncheck ./... 2>&1 \
  | tee security-evidence/E08-govulncheck-broker.txt
```

SDK:

```Python
cd "$sdkPath"

govulncheck ./... 2>&1 \
  | tee security-evidence/E09-govulncheck-sdk.txt
```

Para cada resultado relevante registrar:

```Python
Módulo:
Versión:
Vulnerabilidad:
Símbolo afectado:
¿Es alcanzable?:
Recomendación:
```

No convertir automáticamente "dependencia vulnerable" en "vulnerabilidad explotable". La alcanzabilidad debe formar parte de la interpretación.

### 8.3. `go vet`

Broker:

```Python
cd "$brokerPath"
go vet ./... 2>&1 | tee security-evidence/E10-go-vet-broker.txt
```

SDK:

```Python
cd "$sdkPath"
go vet ./... 2>&1 | tee security-evidence/E11-go-vet-sdk.txt
```

Un resultado limpio significa que esta herramienta no encontró las condiciones que busca; no significa que el proyecto sea seguro.

### 8.4. `gosec`

Broker:

```Python
cd "$brokerPath"

gosec -fmt=json \
  -out=security-evidence/E12-gosec-broker.json \
  ./...
```

SDK:

```Python
cd "$sdkPath"

gosec -fmt=json \
  -out=security-evidence/E13-gosec-sdk.json \
  ./...
```

Revisar primero severidades altas y medias. Para cada una:

```Python
Archivo:
Línea:
Regla:
Código:
Flujo:
Condición necesaria:
¿Reproducible?:
Impacto:
```

No corregir todos los avisos automáticamente. Primero determinar cuáles corresponden realmente a la arquitectura.

### 8.5. Detección De Secretos

Broker:

```Python
cd "$brokerPath"

gitleaks detect \
  --source . \
  --redact \
  --report-format json \
  --report-path security-evidence/E14-gitleaks-broker.json
```

SDK:

```Python
cd "$sdkPath"

gitleaks detect \
  --source . \
  --redact \
  --report-format json \
  --report-path security-evidence/E15-gitleaks-sdk.json
```

Si se va a publicar el repositorio, revisar también historial:

```Python
gitleaks git --redact --report-format json \
  --report-path security-evidence/E16-gitleaks-history.json
```

Nunca copiar el secreto a la entrega.

### 8.6. Revisar Manualmente La Configuración

Buscar nombres relacionados con secretos y transporte:

```Python
cd "$brokerPath"

grep -RniE \
  'api[_-]?key|token|password|secret|private.?key|certificate|tls|redis' \
  env terraform config 2>/dev/null \
  | tee security-evidence/E17-revision-configuracion.txt
```

Después revisar específicamente:

```Python
env/
terraform/
config/
Dockerfile
docker-compose*.yml
README*
scripts/
```

El objetivo aquí no es solamente encontrar contraseñas. También hay que comprobar:

- si TLS puede desactivarse;
    
- si existen credenciales por defecto;
    
- si Redis está publicado;
    
- si el proceso corre como root;
    
- si existen certificados dentro de la imagen;
    
- si una configuración de desarrollo puede llegar accidentalmente a producción.

### 8.7. Infraestructura Y Contenedor

Si Trivy está disponible:

```Python
cd "$brokerPath"

trivy fs \
  --scanners vuln,secret,misconfig \
  . 2>&1 | tee security-evidence/E18-trivy-filesystem.txt
```

Revisar Terraform:

```Python
trivy config ./terraform \
  2>&1 | tee security-evidence/E19-trivy-terraform.txt
```

Si Terraform está instalado:

```Python
terraform -chdir=./terraform fmt -check -recursive
terraform -chdir=./terraform validate
```

Construir una imagen de laboratorio:

```Python
docker build -t dominus-broker:security-lab .
```

Inspeccionar el usuario:

```Python
docker image inspect dominus-broker:security-lab \
  --format ' {{json .Config.User}} '
```

Escanear la imagen:

```Python
trivy image dominus-broker:security-lab \
  2>&1 | tee security-evidence/E20-trivy-image.txt
```

El `Dockerfile` ya contiene un control positivo al cambiar a un usuario sin privilegios. No eliminar ese control durante las pruebas.

---

## 9. Fase 3: Levantar El Laboratorio Antes De Las Pruebas Dinámicas

Las pruebas dinámicas deben ejecutarse contra una instancia deliberadamente aislada.

### 9.0. Crear Directorio De Evidencias

```Python
cd "$brokerPath"

mkdir -p security-evidence
chmod 700 security-evidence
```

Confirmar:

```Python
pwd
ls -ld security-evidence
```

### 9.1. Crear Credenciales Desechables

No escribir credenciales reales en el documento.

```Python
export DOMINUS_TEST_TOKEN='token-de-laboratorio-no-productivo'
```

Comprobar solamente que existe, sin imprimirlo:

```Python
if [[ -n "${DOMINUS_TEST_TOKEN:-}" ]]; then
  echo "DOMINUS_TEST_TOKEN configurado"
else
  echo "ERROR: falta DOMINUS_TEST_TOKEN"
  exit 1
fi
```

Para limpiar al terminar:

```Python
unset DOMINUS_TEST_TOKEN
```

### 9.2. Confirmar Puertos Disponibles

Antes de iniciar:

```Python
ss -ltn 2>/dev/null | grep -E ':(5000|8000)\b' || true
```

Si `ss` no existe en Git Bash, utilizar Docker:

```Python
docker ps --format 'table {{.Names}} \t {{.Ports}} '
```

No asumir que `5000` y `8000` son correctos si la configuración del proyecto utilize otros puertos. Confirmarlos en la configuración del broker.

### 9.3. Iniciar El Laboratorio

Usar el mecanismo de arranque documentado por el repositorio. Si existe un `docker compose` de laboratorio:

```Python
docker compose up -d
```

Verificar:

```Python
docker compose ps
```

Ver logs:

```Python
docker compose logs --tail=100
```

Si el proyecto se inicia directamente con Go, utilizar el commando documentado por el repositorio y guardar stdout/stderr:

```Python
go run ./cmd/api 2>&1 | tee security-evidence/E21-broker-startup.log
```

Mantener ese proceso en una terminal separada.

### 9.4. Verificar Estado Antes De Atacar

Primero comprobar que el servicio está vivo:

```Python
curl -i http://127.0.0.1:8000/health
```

Después revisar procesos/contenedores:

```Python
docker ps
```

Si el servicio está corriendo directamente:

```Python
ps aux | grep '[d]ominus'
```

Solo continuar cuando exista una línea base clara de "broker vivo".

---

## 10. Fase 4: Pruebas Dinámicas Del Backend

Cada prueba debe seguir exactamente el mismo ciclo:

```Python
Preparar
→ Ejecutar caso positivo
→ Ejecutar caso negativo
→ Verificar proceso
→ Guardar evidencia
→ Interpretar
→ Limpiar
```

Esto evita que una prueba anterior contamine la siguiente.

### BE-01. Autenticación gRPC Ante Cabecera Ausente

**Objetivo:** comprobar que una solicitud sin `x-api-key` se rechaza correctamente y no provoca `panic`.

#### Paso 1. Confirmar Que El Broker Está Vivo

```Python
curl -fsS http://127.0.0.1:8000/health
echo
```

Guardar:

```Python
curl -i http://127.0.0.1:8000/health \
  | tee security-evidence/E22-BE01-health-before.txt
```

#### Paso 2. Ejecutar Solicitud Sin Token

```Python
grpcurl -plaintext 127.0.0.1:5000 list \
  2>&1 | tee security-evidence/E23-BE01-no-token.txt
```

#### Paso 3. Verificar Inmediatamente Que El Proceso Sigue Vivo

```Python
curl -i http://127.0.0.1:8000/health \
  | tee security-evidence/E24-BE01-health-after-no-token.txt
```

#### Paso 4. Token Incorrecto

```Python
grpcurl -plaintext \
  -H 'x-api-key: token-invalido-de-laboratorio' \
  127.0.0.1:5000 list \
  2>&1 | tee security-evidence/E25-BE01-invalid-token.txt
```

#### Paso 5. Token Correcto

```Python
grpcurl -plaintext \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  127.0.0.1:5000 list \
  2>&1 | tee security-evidence/E26-BE01-valid-token.txt
```

#### Paso 6. Criterio

Esperado:

```Python
Sin token     -> Unauthenticated
Token inválido -> Unauthenticated
Token válido   -> operación permitida según configuración
Proceso        -> permanece activo
```

Si el proceso se reinicia o muere después del caso sin token, conservar el log del broker.

No afirmar todavía "vulnerabilidad confirmada" únicamente por el código. La clasificación depende del resultado real.

### BE-02. Protección Del Monitor HTTP

Sin token:

```Python
curl -i http://127.0.0.1:8000/health \
  | tee security-evidence/E27-BE02-no-token.txt
```

Token incorrecto:

```Python
curl -i \
  -H 'x-api-key: token-invalido' \
  http://127.0.0.1:8000/health \
  | tee security-evidence/E28-BE02-invalid-token.txt
```

Token válido:

```Python
curl -i \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  http://127.0.0.1:8000/health \
  | tee security-evidence/E29-BE02-valid-health.txt
```

Métricas:

```Python
curl -i \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  http://127.0.0.1:8000/metrics \
  | tee security-evidence/E30-BE02-valid-metrics.txt
```

Si la configuración permite modificar el CIDR, repetir con una red que excluya `127.0.0.1`.

También comprobar una cabecera reenviada:

```Python
curl -i \
  -H "x-api-key: ${DOMINUS_TEST_TOKEN}" \
  -H 'X-Forwarded-For: 10.0.0.10' \
  http://127.0.0.1:8000/health
```

El objetivo es verificar que esa cabecera no sustituye indebidamente la IP remota real.

### BE-03. Idempotencia Bajo Concurrencia

Esta prueba require una prueba automatizada porque enviar manualmente diez peticiones no garantiza que lleguen simultáneamente.

Crear una prueba de laboratorio en el broker:

```Python
cd "$brokerPath"

mkdir -p tests/security
touch tests/security/idempotency_security_test.go
```

La prueba debe:

1. levantar un servidor local;
    
2. preparar Redis de laboratorio;
    
3. generar una única clave de idempotencia;
    
4. sincronizar 10–20 goroutines;
    
5. enviar las solicitudes al mismo tiempo;
    
6. contar operaciones aceptadas;
    
7. contar duplicados;
    
8. repetir la prueba;
    
9. ejecutar `-race`.

Ejemplo de ejecución:

```Python
go test -race \
  -count=20 \
  ./tests/security \
  2>&1 | tee security-evidence/E31-BE03-idempotencia.txt
```

**Criterio esperado:** exactamente una solicitud ejecuta la operación y las demás se rechazan como duplicadas.

Si más de una alcanza el handler, el resultado debe conservarse como evidencia de una condición de carrera reproducible.

### BE-04. Destinos De Suscriptores

Esta prueba debe utilizar exclusivamente loopback.

Levantar un receptor de prueba:

```Python
nc -l 127.0.0.1 9000
```

Si el protocolo require gRPC real, utilizar un servidor gRPC de prueba en lugar de `nc`.

Enviar desde el cliente una dirección como:

```Python
127.0.0.1:9000
```

Observar si el broker intenta establecer la conexión.

Registrar:

```Python
Destino enviado:
Destino aceptado/rechazado:
Conexión observada:
Política que debería aplicarse:
```

No probar:

```Python
169.254.169.254
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
IPs de la LAN
servicios públicos
```

El objetivo es demostrar el comportamiento del control, no explorar redes.

### BE-05. Límites De Payload, Suscriptores Y Streams

Registrar estado inicial:

```Python
ps -o pid,rss,vsz,comm -C dominus-broker 2>/dev/null || true
```

Si corre en Docker:

```Python
docker stats --no-stream
```

Probar tamaños:

```Python
1 KiB
64 KiB
1 MiB
4 MiB máximo para este laboratorio
```

No saltar directamente al máximo. Registrar para cada tamaño:

```Python
Payload:
Latencia:
Código:
Memoria:
Goroutines:
Proceso vivo:
```

Para streams, utilizar un máximo conservador de 20 conexiones y cerrarlas todas al terminar.

El resultado buscado no es "lograr una caída", sino identificar si existe un límite explícito y observable.

### BE-06. TLS Y Degradación A Texto Plano

Construir cuatro escenarios:

```Python
A. CA válida + nombre válido
B. CA incorrecta
C. nombre incorrecto
D. certificado ausente
```

Para A se espera conexión exitosa.

Para B y C se espera rechazo de verificación.

Para D se debe documentar si el sistema falla cerrado o cambia automáticamente a plaintext.

Comprobar además la configuración efectiva, no solamente los archivos:

```Python
grep -RniE 'tls|plaintext|insecure|certificate|ca' \
  . --exclude-dir=.git \
  | tee security-evidence/E32-BE06-tls-config.txt
```

El token no está protegido por aplicar SHA-256 al valor en el servidor. La confidencialidad durante el tránsito depende de TLS.

### BE-07. Redis Y Privilegios

Comprobar contenedores:

```Python
docker ps --format 'table {{.Names}} \t {{.Ports}} \t {{.Networks}} '
```

Identificar Redis:

```Python
docker ps --format ' {{.Names}} ' | grep -i redis
```

Inspeccionar puertos publicados:

```Python
docker port <redis-container>
```

Si no debe estar expuesto al host, no debería aparecer un puerto público innecesario.

Revisar configuración:

```Python
grep -RniE 'acl|user|password|tls|port|bind' \
  terraform env . \
  --exclude-dir=.git \
  | tee security-evidence/E33-BE07-redis-config.txt
```

Comprobar que las claves de idempotencia tienen expiración y que un error de Redis no imprime credenciales.

---

## 11. Fase 5: Pruebas De La Interfaz Cliente `dominus-sdk`

Aquí se evalúa el SDK como interfaz de consumo porque no existe una interfaz gráfica dentro del proyecto.

Crear rama de laboratorio:

```Python
cd "$sdkPath"

git switch -c security-lab-tests
```

Crear estructura:

```Python
mkdir -p dominus/security
```

La prueba debe usar servidores gRPC locales y certificados efímeros.

### CL-01. Validación TLS Del Servidor

Preparar cuatro casos:

```Python
CA válida + SAN correcto       -> éxito
CA distinta                    -> rechazo
SAN/nombre incorrecto          -> rechazo
CA inexistente                 -> error de inicialización
```

Ejecutar:

```Python
go test -v ./dominus/security \
  -run TestTLS \
  2>&1 | tee security-evidence/E34-CL01-tls.txt
```

No registrar certificados privados ni tokens en stdout.

### CL-02. Metadata De Autenticación

El servidor de prueba debe registrar solamente:

```Python
x-api-key presente: sí/no
longitud del token: N
idempotency-header presente: sí/no
```

Nunca:

```Python
valor del token
valor completo de la clave
credenciales
```

Ejecutar:

```Python
go test -v ./dominus/security \
  -run TestMetadata \
  2>&1 | tee security-evidence/E35-CL02-metadata.txt
```

### CL-03. Validación Y Autorización De Destinos

Separar dos conceptos:

```Python
Validación sintáctica = "parece una dirección"
Autorización           = "está permitido conectarse allí"
```

Probar al menos:

```Python
127.0.0.1:5000
hostname.test:5000
hostname.test:99999
hostname.test/path
loopback no autorizado
destino incluido en allowlist
destino fuera de allowlist
```

La regex del SDK no debe considerarse una política de seguridad completa.

### CL-04. Cancelación Y Tiempo Límite

Crear servidor que acepte una conexión y no responda.

La prueba debe intentar terminar en aproximadamente 1–2 segundos.

Ejecutar:

```Python
go test -v ./dominus/security \
  -run TestTimeout \
  2>&1 | tee security-evidence/E36-CL04-timeout.txt
```

Esperado:

```Python
DeadlineExceeded
conexión liberada
test termina dentro del límite
```

Si el SDK construye internamente `context.Background()` y no permite que el consumidor suministre un contexto, documentar esa limitación.

### CL-05. Error De Serialización

Crear un valor que `encoding/json` no pueda serializar, por ejemplo una función o canal.

El comportamiento correcto es:

```Python
Marshal falla
→ se devuelve error
→ no se llama Send
```

Ejecutar:

```Python
go test -v ./dominus/security \
  -run TestSerializationError \
  2>&1 | tee security-evidence/E37-CL05-serialization.txt
```

Si el error se descarta y se envía un payload vacío, documentarlo como pérdida potential de integridad.

### CL-06. Ciclo De Vida De Conexiones

Registrar antes:

```Python
ps -eLf | grep '[d]ominus' | wc -l
```

Ejecutar operaciones acotadas:

```Python
go test -v ./dominus/security \
  -run TestConnectionLifecycle \
  2>&1 | tee security-evidence/E38-CL06-connections.txt
```

Registrar después:

```Python
ps -eLf | grep '[d]ominus' | wc -l
```

La comparación debe hacerse después de permitir que las conexiones terminen normalmente. No interpretar una goroutine temporal como fuga sin verificar su ciclo de vida.

---

## 12. Fase 6: Corrección De Hallazgos Y Regresión

No corregir varios hallazgos simultáneamente. La trazabilidad debe set:

```Python
Hallazgo
→ reproducción
→ corrección
→ test de regresión
→ pruebas completas
→ nuevo resultado
```

### 12.1. Crear Una Rama De Corrección

Broker:

```Python
cd "$brokerPath"
git switch -c security/fixes
```

SDK:

```Python
cd "$sdkPath"
git switch -c security/fixes
```

### 12.2. Registrar El Hallazgo Antes De Modificar

Ejemplo:

```Python
ID: BE-01
Componente: dominus-broker
Archivo: middlewares.go
Riesgo: fallo ante metadata ausente
Resultado actual: [RESULTADO REAL]
Evidencia: E23-BE01-no-token.txt
```

### 12.3. Crear La Prueba De Regresión

La prueba debe fallar antes de la corrección y pasar después.

Ejecutar primero:

```Python
go test ./... -run 'TestNombreDeRegresion'
```

Conservar el resultado previo.

Aplicar la corrección.

Ejecutar nuevamente:

```Python
go test ./... -run 'TestNombreDeRegresion'
```

Después:

```Python
go test -race ./...
```

La regresión debe permanecer en el repositorio. No eliminarla después de comprobar que la corrección funciona.

---

## 13. Fase 7: Repetición Completa Después De Las Correcciones

Después de corregir un hallazgo, repetir como mínimo:

```Python
go test -race -count=1 ./...
govulncheck ./...
go vet ./...
gosec ./...
```

Para el SDK:

```Python
cd "$sdkPath"

go test -race -count=1 ./...
govulncheck ./...
go vet ./...
gosec ./...
```

Volver a ejecutar la prueba dinámica afectada.

Por ejemplo, después de corregir BE-01:

```Python
grpcurl -plaintext 127.0.0.1:5000 list
curl -i http://127.0.0.1:8000/health
```

Comparar:

```Python
Resultado antes:
Resultado después:
Evidencia antes:
Evidencia después:
```

No reemplazar la evidencia anterior. Conservar ambas.

---

## 14. Fase 8: Organización De Evidencias

Crear una estructura estable:

```Python
mkdir -p security-evidence/{baseline,static,dynamic,regression}
```

Mover o guardar:

```Python
baseline/
  commits
  versiones
  go-test
  race

static/
  govulncheck
  gosec
  gitleaks
  trivy

dynamic/
  BE-01
  BE-02
  BE-03
  BE-04
  BE-05
  BE-06
  BE-07
  CL-01
  CL-02
  CL-03
  CL-04
  CL-05
  CL-06

regression/
  pruebas antes
  pruebas después
```

Listar:

```Python
find security-evidence -type f -maxdepth 3 \
  | sort \
  | tee security-evidence/E39-inventario-evidencias.txt
```

Antes de entregar:

```Python
grep -RniE \
  'token-[^ ]+|password=[^ ]+|BEGIN .*PRIVATE KEY|api[_-]?key' \
  security-evidence \
  || true
```

Esta búsqueda es una revisión auxiliary. También inspeccionar manualmente capturas.

---

## 15. Selección Mínima Para La Rúbrica

Si la entrega solamente permite dos pruebas principales, seleccionar:

### Backend

`BE-01: autenticación gRPC ante token ausente, incorrecto y válido`.

Debe incluir:

```Python
Objetivo
Riesgo
Versión
Preparación
Comando sin token
Comando con token incorrecto
Comando con token correcto
Comprobación de proceso
Resultado real
Evidencia
Recomendación
Regresión
```

### Interfaz Cliente

`CL-01: rechazo de certificado o nombre TLS no confiable por dominus-sdk`.

Debe incluir:

```Python
Objetivo
Certificado utilizado
CA
SAN/serverName
Resultado esperado
Resultado real
Evidencia
Regresión
```

Como pruebas complementarias:

```
BE-03 -> idempotencia
BE-04 -> destinos salientes
CL-04 -> timeout
CL-05 -> serialización
```

---

## 16. Plantilla Para Documentar Cada Ejecución

Cada prueba debe producir una ficha como esta:

|   |   |
|---|---|
|Campo|Contenido|
|Identificador|BE-01, CL-01, etc.|
|Fecha|Fecha real de ejecución|
|Commit|Hash real|
|Rama|Rama real|
|Componente|Broker o SDK|
|Objetivo|Propiedad de seguridad|
|Riesgo|Impacto si falla|
|Preparación|Servicios y configuración|
|Entrada|Datos ficticios/redactados|
|Comando|Comando Bash ejecutado|
|Resultado esperado|Comportamiento seguro|
|Resultado observado|Salida real|
|Estado|Aprobada / Fallida / Inconclusa|
|Severidad|Baja / Media / Alta / Crítica|
|Evidencia|Archivo de evidencia|
|Corrección|Cambio realizado|
|Regresión|Test asociado|

### Regla Importante

Nunca escribir primero:

> "La prueba pasó."

Primero guardar:

```
comando
+
salida
+
estado del proceso
+
evidencia
```

Después interpretar.

---

## 17. Orden Completo Recomendado De Ejecución

Este es el orden que evita los saltos que existían en la guía original:

```
1. Abrir Bash
2. Definir brokerPath y sdkPath
3. Verificar directorios
4. Registrar rama y commit
5. Registrar cambios locales
6. Registrar versiones de Go/Docker
7. Descargar dependencias
8. Ejecutar go test
9. Ejecutar go test -race
10. Ejecutar cobertura
11. Ejecutar pruebas del SDK
12. Instalar herramientas faltantes
13. Verificar versiones de herramientas
14. Ejecutar govulncheck
15. Ejecutar go vet
16. Ejecutar gosec
17. Ejecutar gitleaks
18. Revisar configuración manualmente
19. Revisar Terraform/Trivy
20. Construir imagen de laboratorio
21. Crear directorio de evidencias
22. Crear token desechable
23. Verificar puertos
24. Levantar Redis
25. Levantar broker
26. Verificar /health
27. Ejecutar BE-01
28. Verificar /health después de BE-01
29. Ejecutar BE-02
30. Verificar proceso
31. Crear prueba automatizada BE-03
32. Ejecutar BE-03 con race detector
33. Ejecutar BE-04 solo con loopback
34. Ejecutar BE-05 con límites conservadores
35. Ejecutar BE-06
36. Ejecutar BE-07
37. Crear pruebas CL-01 a CL-06
38. Ejecutar pruebas del SDK
39. Registrar hallazgos
40. Crear rama de corrección
41. Crear regresión del primer hallazgo
42. Corregir
43. Ejecutar regresión
44. Ejecutar suite completa
45. Repetir prueba dinámica
46. Comparar antes/después
47. Revisar evidencias
48. Redactar únicamente resultados reales
49. Limpiar credenciales
50. Detener el laboratorio
```

### Comandos De Limpieza

Al finalizar:

```
unset DOMINUS_TEST_TOKEN
```

Si se utilizó Docker Compose:

```
docker compose down
```

Si se creó un contenedor de prueba independiente:

```
docker rm -f <container-name>
```

Verificar que no quedan procesos del laboratorio:

```
docker ps
```

Y verificar que los puertos se liberaron:

```
ss -ltn 2>/dev/null | grep -E ':(5000|8000)\b' || true
```

---

## 18. Criterio De Finalización

La actividad estará lista cuando:

```
[ ] El commit evaluado está documentado.
[ ] Los cambios locales están documentados.
[ ] Las versiones de herramientas están documentadas.
[ ] Broker compiló.
[ ] Race detector fue ejecutado.
[ ] SDK fue probado o se documentó ausencia de tests.
[ ] govulncheck fue ejecutado.
[ ] go vet fue ejecutado.
[ ] gosec fue ejecutado.
[ ] gitleaks fue ejecutado o su ausencia quedó documentada.
[ ] El laboratorio utiliza credenciales desechables.
[ ] BE-01 tiene resultado real.
[ ] BE-02 tiene resultado real.
[ ] BE-03 tiene prueba automatizada si se incluye.
[ ] CL-01 tiene resultado real.
[ ] Las capturas no contienen secretos.
[ ] Cada hallazgo apunta a archivo/línea.
[ ] Cada corrección tiene regresión.
[ ] Las pruebas fueron repetidas después de corregir.
[ ] La entrega distingue hipótesis de hechos observados.
```

La conclusión académica debe basarse exclusivamente en los resultados obtenidos.

No escribir:

> "El sistema es seguro."

Preferir:

> "En el entorno local evaluado, con el commit X y la configuración Y, las pruebas BE-01 y CL-01 produjeron los resultados Z. No se observaron [condiciones específicas] durante esta ejecución. Las limitaciones del laboratorio impiden extrapolar el resultado a una exposición pública."

---

## 19. Rutas Prioritarias Para Revisión Manual

Mantener como prioridad:

```
dominus-broker/internal/infrastructure/grpc/middlewares/middlewares.go
dominus-broker/internal/bootstraps/bootstraps.go
dominus-broker/internal/infrastructure/grpc/outbound/client_stream.go
dominus-broker/internal/application/usecases/stream_*
dominus-broker/internal/infrastructure/redis
dominus-broker/internal/infrastructure/fasthttp
dominus-broker/config/config.go
dominus-broker/env
dominus-broker/terraform
dominus-broker/Dockerfile
dominus-sdk/dominus/interceptors.go
dominus-sdk/dominus/*_client_factory.go
dominus-sdk/dominus/broker_client_conn.go
dominus-sdk/dominus/broker_client_services.go
dominus-sdk/dominus/rules.go
```

La revisión manual debe responder, para cada ruta:

```
¿Qué entrada controla este código?
¿Quién puede proporcionar esa entrada?
¿Cruza una frontera de confianza?
¿Qué validación existe?
¿Qué ocurre si falta?
¿Qué ocurre si es maliciosa?
¿Hay un límite?
¿Hay timeout?
¿Se registra información sensible?
¿Existe una prueba automatizada?
```

---

## 20. Regla Final Para La Entrega

Las hipótesis TM-001 a TM-009 siguen siendo hipótesis hasta que una ejecución reproducible las confirme.

La evidencia debe conservar la secuencia:

```
Código observado
→ hipótesis
→ preparación
→ comando
→ salida real
→ interpretación
→ impacto
→ corrección
→ regresión
```

Esta secuencia es especialmente importante a partir de la Fase 1 porque evita saltar directamente desde la revisión estática a una conclusión de vulnerabilidad.

La guía utiliza Bash de forma consistente y cada prueba incluye ahora los pasos intermedios necesarios para llegar desde una máquina limpia hasta una evidencia reproducible.