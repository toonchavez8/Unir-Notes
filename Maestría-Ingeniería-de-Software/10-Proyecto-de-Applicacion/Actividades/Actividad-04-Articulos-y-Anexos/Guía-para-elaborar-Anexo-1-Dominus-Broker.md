# Guía para elaborar el Anexo 1 de Dominus Broker

## Propósito de la guía

Esta guía describe cómo preparar, redactar y comprobar el Anexo 1 del TFM: la puesta en marcha de Dominus Broker en una infraestructura nueva. El resultado debe permitir que un desarrollador instale las dependencias, configure el servicio, lo ejecute en Windows o Linux y compruebe que quedó operativo.

La rúbrica concede dos puntos al Anexo 1 y exige un mínimo de dos páginas. Cumplir esa extensión no basta por sí solo. Para obtener la puntuación completa, el texto debe ser reproducible, coherente con el código actual y útil ante un fallo real de instalación.

## Criterio de revisión de las fuentes

Dominus tiene documentación de distintas fechas y algunos archivos describen comportamientos que ya cambiaron. Para evitar instrucciones obsoletas, se debe revisar la información en este orden:

1. Código que ejecuta el servicio: `cmd/api/main.go`, `config/config.go` e `internal/bootstraps/bootstraps.go`.
2. Automatización vigente: `Makefile.ps1`, `Dockerfile`, `env/entrypoint.sh` y `terraform/`.
3. Contrato del servicio: `dominus-proto-definition/proto/dominus.proto`.
4. Pruebas y evidencias de ejecución guardadas en `Referance/security-evidence/`.
5. README, documentos técnicos y guías generales.

Cuando dos fuentes se contradigan, el Anexo debe explicar la diferencia y seguir el comportamiento comprobable del código. Un ejemplo concreto es la configuración: algunas notas antiguas indican que el modo local lee un archivo directamente, pero `config.NewConfig()` exige que el JSON esté cargado en `APP_CONFIG`.

## Paso 1. Delimitar el alcance

El Anexo debe documentar la puesta en marcha del broker. No debe convertirse en un manual completo del SDK ni en una explicación extensa de arquitectura.

El alcance mínimo es el siguiente:

- obtención del código;
- requisitos técnicos;
- preparación de Redis;
- creación segura de `APP_CONFIG`;
- ejecución de Dominus Broker desde el código fuente;
- variantes para Windows y Linux;
- comprobación de `/health`, `/metrics` y la reflexión gRPC;
- prueba breve del ciclo `Producer`, `Consumer` y `Ack`;
- alternativa de despliegue con Docker y Terraform;
- detención del servicio, limpieza y diagnóstico de fallos frecuentes.

La parte `BrokerAPI` puede validarse con las pruebas de integración. Una demostración manual de sus streams necesita uno o más servicios suscriptores y corresponde a un escenario más amplio que la puesta en marcha básica.

## Paso 2. Definir al lector

El lector objetivo es un desarrollador que conoce Git, una terminal y conceptos básicos de redes, pero no ha trabajado antes con Dominus. Cada instrucción debe responder cuatro preguntas:

1. ¿Desde qué directorio se ejecuta?
2. ¿Qué comando se utiliza?
3. ¿Qué resultado confirma el éxito?
4. ¿Qué se revisa si falla?

No se deben omitir pasos con frases como "configurar de la forma habitual". Si una acción depende de una decisión local, se documentan las opciones y se indica cuál se usó en la validación.

## Paso 3. Levantar un inventario técnico

Antes de redactar, se completa una tabla de control con los valores obtenidos del repositorio.

| Elemento | Valor que debe comprobarse | Fuente principal |
|---|---|---|
| Versión de Go | `1.26.1` o compatible | `go.mod` |
| Puerto gRPC | `5000` en las plantillas | `env/template.json` |
| Puerto del monitor HTTP | `8000` en las plantillas | `env/template.json` |
| Puerto de Redis | `6379` | `env/template.json` |
| Configuración de arranque | JSON completo en `APP_CONFIG` | `config/config.go` |
| Autenticación | `x-api-key` | `internal/infrastructure/enum/enum.go` |
| Idempotencia unary | `idempotency-header` | `internal/infrastructure/enum/enum.go` |
| Comprobaciones HTTP | `/health` y `/metrics` | `monitor_api.go` |
| Servicios gRPC | `dominus.BrokerAPI` y `dominus.SqsAPI` | `dominus.proto` |

Los valores secretos no se copian al Anexo. Se sustituyen por nombres como `<TOKEN_GRPC>`, `<TOKEN_REST>` y `<CONTRASEÑA_REDIS>`.

## Paso 4. Elegir una ruta principal de ejecución

La ruta principal debe ser corta y comprobable. Para este proyecto conviene usar:

1. Redis dentro de Docker, construido con `terraform/dev/redis/Dockerfile` y su `redis.conf`.
2. Dominus Broker ejecutado desde el código fuente con `go run ./cmd/api`.
3. Configuración cargada explícitamente en `APP_CONFIG`.

Esta combinación reduce variables durante la primera instalación. Docker aporta una instancia Redis coherente con el usuario ACL del proyecto, mientras que `go run` deja visibles los errores del broker.

Después de documentar esa ruta se añade el despliegue íntegro en contenedores y la infraestructura Terraform como alternativas. No se deben mezclar las tres rutas en una sola secuencia.

## Paso 5. Preparar comandos separados por sistema operativo

La lógica debe ser la misma en ambos sistemas, aunque cambie la sintaxis.

### Windows

Se utiliza PowerShell. Los ejemplos deben incluir:

- `Set-Location` para entrar al repositorio;
- `$env:APP_CONFIG` para cargar el JSON;
- `Invoke-RestMethod` o `curl.exe` para HTTP;
- `Remove-Item Env:APP_CONFIG` al terminar.

### Linux

Se utiliza Bash. Los ejemplos deben incluir:

- `cd` para entrar al repositorio;
- `export APP_CONFIG=...` para cargar el JSON;
- `curl` para HTTP;
- `unset APP_CONFIG` al terminar.

Un bloque marcado como Bash no debe contener sintaxis de PowerShell, y viceversa. Los comandos compartidos, como `go test`, `go run`, `docker build` y `grpcurl`, pueden repetirse si eso evita dudas sobre el directorio de trabajo.

## Paso 6. Documentar la configuración sin revelar secretos

El Anexo debe mostrar la estructura completa del JSON porque `config.NewConfig()` valida los bloques de gRPC, REST y Redis al arrancar. Los secretos se dejan como marcadores.

También debe explicar estos puntos:

- `grpc_config.api_token` protege llamadas gRPC;
- `rest_config.api_token` protege `/health` y `/metrics`;
- `rest_config.allow_origins` se interpreta como un CIDR permitido por el middleware;
- `redis_config.memory_db` y `checker_db` separan mensajes y claves de idempotencia;
- `redis_config.host` es `localhost` cuando el broker corre en el host y `redis` cuando ambos procesos comparten una red Docker;
- si faltan los archivos de certificado, el código arranca con HTTP y gRPC sin TLS.

La degradación a texto plano sólo es aceptable para una práctica local aislada. La guía de producción debe exigir certificados válidos y una red que no publique Redis.

## Paso 7. Incorporar puntos de control

Cada fase termina con una comprobación observable.

| Fase | Comprobación | Resultado esperado |
|---|---|---|
| Herramientas | `go version`, `docker version`, `git --version` | Los comandos responden sin error |
| Redis | `redis-cli ... PING` | `PONG` |
| Broker | salida de arranque | REST en `8000` y gRPC en `5000` |
| Monitor | `GET /health` con token | `Health ok` |
| Métricas | `GET /metrics` con token | texto Prometheus |
| gRPC | `grpcurl ... list` | aparecen `BrokerAPI` y `SqsAPI` |
| Cola | `Producer`, `Consumer`, `Ack` | el mensaje completa el ciclo |
| Pruebas | `go test -race -count=1 ./...` | todos los paquetes terminan en `ok` |

Las comprobaciones deben incluir tanto el éxito como la conducta ante credenciales incorrectas. Un endpoint protegido que responde sin token no está correctamente desplegado.

## Paso 8. Explicar las limitaciones que afectan al despliegue

El texto debe ser directo sobre los límites encontrados en el repositorio:

- el módulo `dominus-proto-definition` puede requerir autenticación de lectura durante `go mod download` o el build de Docker;
- el `Dockerfile` actual recibe `GITHUB_TOKEN` como argumento de compilación;
- Terraform necesita valores porque no hay un archivo `.tfvars` versionado;
- el proveedor Docker de Terraform usa el named pipe de Windows y debe cambiarse al socket de Linux en ese sistema;
- la ausencia de certificados activa transporte sin TLS;
- Redis no debe publicarse en una interfaz pública;
- el tamaño gRPC efectivo observado es cercano a 4 MiB por mensaje;
- `Ack` e idempotencia reducen duplicados, pero no justifican afirmar una garantía absoluta de *exactly-once*.

Reconocer estas condiciones mejora la utilidad del Anexo. También evita presentar un prototipo académico como si ya tuviera endurecimiento de producción.

## Paso 9. Usar una estructura compatible con APA 7

El Anexo debe integrarse en el documento final con la configuración exigida por la actividad: Calibri 12 e interlineado 1,5. Cuando una regla institucional difiera de una recomendación general de APA 7, se sigue la instrucción de la actividad.

La estructura propuesta es:

1. etiqueta `Anexo 1`;
2. título descriptivo en la línea siguiente;
3. objetivo y alcance;
4. arquitectura mínima de ejecución;
5. requisitos previos;
6. procedimiento de puesta en marcha;
7. validación funcional;
8. despliegue con contenedores y Terraform;
9. solución de problemas;
10. cierre y criterios de aceptación.

Para tablas y figuras:

- numerar cada elemento en el orden en que aparece;
- escribir un título breve y descriptivo;
- mencionarlo en el texto antes de insertarlo;
- añadir una nota cuando sea necesario explicar abreviaturas, origen o condiciones;
- evitar capturas recortadas que oculten el comando o el resultado.

No se añade una bibliografía si la entrega no la requiere. Tampoco se inventan citas. Los nombres de archivos y comandos del propio proyecto se tratan como evidencia técnica interna.

## Paso 10. Reunir evidencia visual

Para la versión final en Word o PDF conviene capturar, al menos:

1. las versiones de Go y Docker;
2. el contenedor Redis en estado `Up`;
3. el mensaje de arranque de Dominus;
4. la respuesta `Health ok`;
5. la lista de servicios devuelta por `grpcurl`;
6. el resultado final de las pruebas automatizadas.

Cada captura debe ocultar tokens, contraseñas, rutas personales y nombres de usuario. La figura se coloca inmediatamente después del párrafo que la explica. Una captura sin interpretación ocupa espacio, pero no demuestra que el autor comprenda el resultado.

## Paso 11. Redactar para un desarrollador

La redacción debe usar verbos concretos: crear, copiar, ejecutar, comprobar, detener. Las explicaciones largas se reservan para decisiones que cambian el comportamiento del sistema.

Se deben evitar:

- afirmaciones promocionales;
- introducciones genéricas sobre la importancia de la tecnología;
- listas repetidas con la misma idea;
- atribuciones vagas;
- conclusiones que sólo digan que el proceso fue exitoso;
- encabezados con palabras innecesarias;
- bloques de comandos sin indicar su terminal y directorio.

El tono adecuado es técnico y sobrio. Por ejemplo, "El broker necesita Redis para crear el consumer group durante el arranque" aporta más que "Redis es una tecnología crucial para el ecosistema".

## Paso 12. Ejecutar la revisión final

Antes de entregar se completa esta lista:

- [ ] El Anexo tiene más de dos páginas después de pasarlo a Calibri 12 e interlineado 1,5.
- [ ] La secuencia principal fue ejecutada en una infraestructura limpia o en un entorno equivalente.
- [ ] Windows y Linux tienen comandos propios.
- [ ] Todos los comandos indican el directorio de trabajo.
- [ ] Los puertos coinciden con el JSON mostrado.
- [ ] `APP_CONFIG` aparece como requisito obligatorio.
- [ ] Los tokens usados en HTTP y gRPC no se confunden.
- [ ] Redis usa credenciales compatibles con el JSON.
- [ ] El texto distingue el modo local sin TLS del despliegue protegido.
- [ ] La prueba de `Producer`, `Consumer` y `Ack` usa una clave de idempotencia distinta en cada llamada.
- [ ] No hay secretos reales en texto, capturas ni historial de terminal.
- [ ] Las tablas y figuras están numeradas y mencionadas en el texto.
- [ ] No se prometen garantías que el proyecto no implementa.
- [ ] La ortografía, los acentos y la terminología de Dominus son consistentes.
- [ ] No quedan frases propias de una conversación ni texto de relleno.

## Método resumido de trabajo

El método completo puede repetirse para futuras versiones del Anexo:

1. fijar la versión del código que se documentará;
2. reconstruir el arranque desde el código y la automatización;
3. comparar las guías con el comportamiento actual;
4. ejecutar la ruta más corta en Windows y Linux;
5. guardar resultados sin secretos;
6. redactar el procedimiento alrededor de esos resultados;
7. añadir la alternativa de infraestructura y sus límites;
8. aplicar el formato académico;
9. pedir a otro desarrollador que siga el texto sin ayuda;
10. corregir cualquier paso que dependa de conocimiento no escrito.

El criterio final es sencillo: un desarrollador que sólo disponga del código y del Anexo debe poder dejar Dominus Broker operativo, demostrarlo y saber dónde mirar si el proceso falla.
