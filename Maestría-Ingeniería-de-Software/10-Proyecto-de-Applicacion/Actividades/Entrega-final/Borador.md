

# Escaleta para la defensa de Dominus Broker

### Idea que todos deben tener presente

> **Dominus Broker es un prototipo académico de broker híbrido que combina streaming gRPC para comunicación en tiempo real y Redis Streams para comunicación asíncrona, evaluando además rendimiento, funcionalidad, usabilidad y seguridad.**

---

##  Integrante 1 — Problema, propósito y alcance

 0:00 – 5:00 | Diapositivas 1–4

### 1. Presentación

- Presentar al equipo. 
    
- Mencionar el nombre del proyecto.
    
- Explicar brevemente qué es Dominus Broker.

>  Buenos días. Somos Maikel Barrios, Daniel Campos, Miguel Chávez, Fernando García y César Sánchez. Nuestro trabajo se titula "Diseño e implementación de Dominus Broker: broker de mensajería en tiempo real basado en gRPC y Redis Streams".
### 2. Problema

Explicar que existen dos necesidades diferentes:

- Comunicación inmediata / tiempo real.
    
- Comunicación asíncrona.
    
- Mensajes que deben poder conservarse cuando el consumidor no está conectado.
    
- Necesidad de ACK y recuperación.
    
- Problema adicional de mensajes duplicados.

### 3. Propósito

- Crear un prototipo que combine ambos tipos de comunicación.
    
- Evaluar si técnicamente es viable.
    
- Incorporar control de idempotencia.

### 4. Objetivos

Mencionar de forma resumida:

- Analizar alternativas.
    
- Definir requisitos.
    
- Diseñar arquitectura.
    
- Implementar comunicación síncrona y asíncrona.
    
- Crear SDK.
    
- Realizar pruebas funcionales, integración, seguridad y rendimiento.

### 5. Alcance

Dejar claro:

- **Es un prototipo académico.**
    
- No pretende competir con Kafka, Pulsar, RabbitMQ o NATS.
    
- Busca demostrar la integración de gRPC + Redis Streams.
    
- Soporta productores, consumidores, streaming, ACK, SDK, Protobuf, autenticación, TLS y observabilidad.

### 6. Punto importante: idempotencia

Explicar brevemente:

- Se utiliza una clave única.
    
- El sistema busca evitar procesamientos duplicados.
    
- El modelo asíncrono es **at-least-once**.
    
- No se afirma `exactly-once`.

### Cierre

Terminar planteando la pregunta principal:

> ¿Es viable construir un broker híbrido que combine comunicación inmediata y asíncrona manteniendo un rendimiento y una arquitectura adecuados?

**Transición:** pasar la palabra al integrante 2.

---

# Integrante 2 — Tecnologías y arquitectura

** 5:00 – 10:00 | Diapositivas 5–7**

### 1. Alternativas consideradas

Explicar brevemente qué se evaluó:

- REST
    
- Kafka
    
- Pulsar
    
- RabbitMQ
    
- NATS JetStream
    
- gRPC
    
- Redis Streams

No es necesario explicar cada tecnología en profundidad.

### 2. ¿Por qué gRPC?

Puntos principales:

- Protocol Buffers.
    
- Contratos tipados.
    
- HTTP/2.
    
- Streaming.
    
- Comunicación bidireccional.

### 3. ¿Por qué Redis Streams?

- Persistencia temporal.
    
- Consumer Groups.
    
- Modelo pull.
    
- ACK.
    
- Mensajes pendientes.

### 4. ¿Por qué Go?

- Concurrencia.
    
- Buen soporte para gRPC.
    
- Adecuado para el tipo de servidor desarrollado.

### 5. Los dos flujos principales

**Tiempo real:**

`Productor → gRPC → Broker → Suscriptores`

- Streaming.
    
- Fan-in.
    
- Fan-out.
    
- Broadcast.
    
- Conexión persistente.
    
- No depende de Redis.

**Asíncrono:**

`Productor → Producer → Redis Streams → Consumer → Ack`

- `XADD`
    
- `XREADGROUP`
    
- `XACK`
    
- Mensajes pendientes si no hay ACK.

### 6. Idempotencia

- Clave única.
    
- TTL.
    
- Reserva en Redis.
    
- Concepto de operación atómica.
    
- Mencionar que posteriormente las pruebas encontraron un problema de concurrencia en esta parte.

### 7. Arquitectura

Explicar visualmente:

`Clientes / SDK`  
↓  
`gRPC / BrokerAPI / SqsAPI`  
↓  
`Casos de uso`  
↓  
`Dominio`  
↓  
`Infraestructura`  
↓  
`Redis / conexiones / seguridad / observabilidad`

Destacar:

- Puertos y adaptadores.
    
- Separación de responsabilidades.
    
- Facilidad para probar y sustituir infraestructura.

###  Cierre

> Ya vimos qué construimos y cómo está estructurado. Ahora vamos a explicar cómo lo desarrollamos y cómo evaluamos que funcionara.

---

# Integrante 3 — Metodología

**⏱ 10:00 – 15:00 | Diapositivas 8–14**

Este bloque debe explicar principalmente **cómo se hizo el trabajo**, no volver a explicar toda la arquitectura.

### 1. Metodología

- Experimental.
    
- Iterativa.
    
- Incremental.

Ciclo:

**Análisis → Diseño → Implementación → Experimentación → Evaluación**

### 2. Análisis del problema

Identificar los cuatro puntos principales:

- Latencia.
    
- Comunicación persistente/bidireccional.
    
- Duplicación de mensajes.
    
- Distribución a múltiples consumidores.

### 3. Diseño

- gRPC para comunicación y streaming.
    
- Redis + memoria temporal para asincronía.
    
- Fan-in.
    
- Fan-out.
    
- Broadcast.
    
- ACK.
    
- Idempotencia.
    
- TTL.

### 4. Implementación incremental

Orden general:

1. Protocol Buffers.
    
2. BrokerAPI / SqsAPI.
    
3. Casos de uso.
    
4. Redis.
    
5. SDK.
    
6. Observabilidad.
    
7. Pruebas.

### 5. Experimentación

Dos escenarios:

**Síncrono**

- Streaming.
    
- Conexiones abiertas.
    
- Varios suscriptores.

**Asíncrono**

- Producer.
    
- Consumer.
    
- ACK.
    
- Redis Streams.
    
- Consumidores a diferentes ritmos.

Herramientas:

- `ghz`
    
- Grafana
    
- Redis

### 6. Métricas

Explicar qué se midió:

- Latencia.
    
- Throughput.
    
- Consistencia.
    
- Duplicados.
    
- Idempotencia.

### 7. Comparación y limitaciones

Puntos principales:

**Ventajas**

- Streaming.
    
- Broadcast.
    
- Bidireccionalidad.
    
- Modelo pull.
    
- Arquitectura desacoplada.

**Limitaciones**

- Dependencia de Redis.
    
- No sustituye brokers consolidados.
    
- Sin replicación.
    
- Sin orden global.
    
- Sin persistencia automática del canal de tiempo real.

### 8. Posibles aplicaciones

Mencionar como escenarios potenciales:

- Notificaciones.
    
- Monitorización.
    
- IoT.
    
- Sistemas industriales.
    
- Banca digital.
    
- Servicios de IA.

**Importante:** aclarar que son **posibles escenarios futuros**, no afirmar que el prototipo ya está preparado para producción.

---

#  Integrante 4 — Implementación, pruebas y ciberseguridad

** 15:00 – 20:00 | Diapositivas 15–17**

### 1. ¿Qué se implementó?

- Servidor Go.
    
- Protobuf.
    
- Servicios gRPC.
    
- Redis Streams.
    
- SDK.
    
- Producer.
    
- Consumer.
    
- ACK.
    
- Streaming.

### 2. Pruebas unitarias

Dar las cifras exactas:

- **143 pruebas y subpruebas.**
    
- **Todas PASS.**
    
- **91.8 % de cobertura.**
    
- Casos de uso principales: **100 % de cobertura.**

### 3. Pruebas de integración

Tres escenarios:

1. gRPC → Producer → Redis.
    
2. Producer → Consumer → ACK.
    
3. Streaming bidireccional con dos suscriptores.

Resultado:

- **3/3 PASS.**

### 4. Usabilidad

Explicar desde la perspectiva de un desarrollador:

- Preparar entorno.
    
- Entender módulos.
    
- Ejecutar pruebas.
    
- Entender Producer / Consumer / ACK.
    
- SDK y documentación.

Resultado:

- Adecuado para prototipo académico.
    
- Existe curva inicial de aprendizaje.
    
- SDK, ejemplos y diagnóstico pueden mejorar.

### 5. Ciberseguridad

Aquí conviene detenerse un poco más.

#### Hallazgo 1 — Autenticación

- Falta `x-api-key`.
    
- Puede provocar un error que detenga el proceso.
    
- Token incorrecto → `Unauthenticated`.
    
- Corrección: validar antes de acceder al elemento.

#### Hallazgo 2 — Idempotencia

- 20 solicitudes simultáneas con la misma clave.
    
- Esperado: **1 aceptación + 19 duplicados**.
    
- Observado: **3–20 aceptadas**, dependiendo de la ronda.
    
- Causa: check y guardado separados.
    
- Solución: operación atómica en Redis.

#### Hallazgo 3 — TLS / SDK

- La validación criptográfica funciona.
    
- CA incorrecta → rechazo.
    
- Nombre de servidor incorrecto → rechazo.
    
- Problema: errores mediante `panic`.

#### Otros hallazgos

- Validación insuficiente de destinos.
    
- Falta de allowlist.
    
- Error de serialización JSON ignorado.
    
- Posibilidad de enviar payload vacío.

###  Mensaje clave

> Las pruebas exitosas y una cobertura alta no significan automáticamente que el sistema sea seguro o esté listo para producción.

---

#  Integrante 5 — Rendimiento, conclusiones y futuro

** 20:00 – 25:00 | Diapositivas 18–20**

### 1. Pruebas de carga

Explicar:

- Herramienta: `ghz`.
    
- Streaming bidireccional.
    
- Concurrencia de **20 a 1,000**.
    
- Tres suscriptores.
    
- Ventana de cinco minutos.
    
- También se probó el flujo asíncrono con Redis.

### 2. Resultados observados

Mantener exactamente estas cifras:

- Throughput observado: **200,000–260,000 mensajes/s**.
    
- P99: aproximadamente **10 ms**.
    
- CPU: aproximadamente **1 % → 4 %**.
    
- Memoria: aproximadamente **36 % → 42 %**.
    
- Disponibilidad observada: cercana al **100 %**.
    
- Redis: **3 consumidores**.
    
- `Pending = 0` en la captura.

### 3. ¡Cuidado con los resultados!

Aclarar que:

- El throughput puede estar agregando más de una fuente de carga.
    
- No significa que un único flujo soporte 260,000 mensajes/s.
    
- Son resultados de ventanas concretas.
    
- No representan una prueba de horas o días.
    
- No se probaron completamente:
    
    - fallos,
        
    - recuperación,
        
    - pérdida de consumidores,
        
    - fugas de memoria.

### 4. Respuesta a la pregunta inicial

Sí:

- Se construyó el broker híbrido.
    
- gRPC funciona para streaming.
    
- Redis Streams funciona para asincronía.
    
- Producer / Consumer / ACK funcionan.
    
- La arquitectura permitió separar responsabilidades.
    
- El SDK facilita la integración.

### 5. ¿Qué falta?

Prioridades:

**Seguridad / consistencia**

- Idempotencia atómica.
    
- Corregir ausencia de token.
    
- Manejo de errores.
    
- Validación de destinos.
    
- Serialización.

**Operación**

- Pruebas de larga duración.
    
- Fallos controlados.
    
- Más productores/consumidores.
    
- Diferentes tamaños de payload.
    
- Métricas separadas.

**Evolución**

- Recuperación de mensajes pendientes.
    
- TLS y credenciales.
    
- Documentación.
    
- SDK.
    
- Replicación.
    
- Alta disponibilidad.
    
- Retención de Redis.

### 6. Conclusión

La idea que debe quedar al jurado:

> **Dominus Broker demuestra que el enfoque híbrido es técnicamente viable como prototipo, pero la evaluación también permitió identificar las condiciones necesarias antes de considerar una evolución hacia producción.**

###  Cierre

> Muchas gracias. Quedamos atentos a sus preguntas.

---

# Regla para los 5 integrantes

La diferencia importante respecto al guion original es que **no necesitan memorizar párrafos**.

Cada persona solamente debe asegurarse de cubrir los puntos de su bloque.

Por ejemplo, el integrante 4 puede explicar los hallazgos de seguridad con sus propias palabras:

**Problema → evidencia → causa → solución**

Y no tiene que repetir literalmente el texto del guion.

## Cifras que TODOS deben memorizar

|Dato|Valor|
|---|--:|
|Duración total|**25 min**|
|Participantes|**5**|
|Tiempo por persona|**5 min**|
|Pruebas unitarias/subpruebas|**143**|
|Cobertura|**91.8 %**|
|Pruebas integración|**3**|
|P99|**≈10 ms**|
|Throughput observado|**200k–260k msg/s**|
|Concurrencia carga|**20–1,000**|
|Consumidores Redis|**3**|
|Pending en captura|**0**|

Estas cifras deben mantenerse consistentes durante toda la defensa, tal como ya establece el guion original.



