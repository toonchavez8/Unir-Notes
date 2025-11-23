FirActividad 1: Modelado de amenazas de una aplicación (grupal)

**Objetivos de la actividad**

Una amenaza a cualquier sistema es cualquier actor, agente, circunstancia o evento que tiene el potential de causarle daño a sus datos, servicios y recursos. Con la presente actividad se pretende conseguir los siguientes objetivos:

- Estudio y análisis de la arquitectura de una aplicación para poder determinar el nivel de riesgo y seguridad de las soluciones técnicas a incluir en su diseño.
- Analizar y detectar amenazas de seguridad y desarrollar técnicas para su prevención.
- Aprender a diseñar e implantar sitios, servicios y aplicaciones con garantías de seguridad.
- Facilitar la identificación de las condiciones o aquellas vulnerabilidades que, una vez eliminadas o contrarrestadas, afectan a la existencia de múltiples amenazas.
- Proporcionar información relevante sobre cuáles serían las contramedidas más eficaces para contrarrestar una possible amenaza o mitigar los efectos de la presencia de una vulnerabilidad en el diseño de una aplicación.

**Descripción de la actividad**

Este es un ejercicio práctico de modelado de amenazas, utilizando una herramienta de modelado como Threat Analysis and Modeling Tool (TAMT), de una aplicación web de tres capas para un negocio de pago electrónico de una librería, con la siguiente arquitectura lógica:

![[Pasted image 20251118065735.png]]

Utilizar la aplicación Threat Analysis and Modeling Tool (TAMT) con el propósito de analizar las amenazas de una aplicación web típica de negocio de pago electrónico de una librería (textos, libros, revistas, etc.) en formato digital con opciones de impresión. La aplicación se puede descargar [aquí](https://docs.microsoft.com/es-es/azure/security/develop/threat-modeling-tool).

**Pasos de elaboración**

1. Realizar el diagrama de flujo de datos de la aplicación (DFD) e incluirlo en la herramienta TAMT. Se propone un diagrama DFD inicial básico que el estudiante deberá mejorar para obtener la puntuación total de este apartado:

![mexingsof07_act1](<Maestría-Ingeniería-de-Software/05-Desarollo-Seguro-y-Auditoria/Actividades/Attachments/mexingsof07_act1%203.png>)

1. Una vez incluido el diagrama DFD en TAMT, realizar el análisis automático de las amenazas. Rellenar una tabla con diez amenazas obtenidas de la herramienta.

|   |   |
|---|---|
|Descripción de la amenaza|Inyección de commandos SQL|
|Objetivo|Componente de acceso a base de datos|
|Técnicas de ataque|El atacante introduce commandos SQL en el campo usuario utilizado para formar una nueva sentencia SQL.|
|Patrón ataque CAPEC|CAPEC-66: SQL Injection|
|Código CWE (si aplica)|CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')|
|Medidas de mitigación|Utilización de procedimientos parametrizados, sanitización de los meta caracteres del leguaje SQL.|
|Descripción de la amenaza||
|Objetivo||
|Técnicas de ataque||
|Patrón ataque CAPEC||
|Código CWE (si aplica)||
|Medidas de mitigación||

1. Valoración del riesgo de las amenazas con el método DREAD _(damage, reproducibility, exploitability, affected, discoverability)._ El riesgo se puede cuantificar como el resultado de multiplicar la probabilidad de que la amenaza se produzca, por el daño potential de esta.

Cada valor se cuantifica con un valor entre 1 y 3. Rellenar la tabla con al menos diez amenazas obtenidas de la de la herramienta TAMT.

|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
||   |Prob. Occur. (P)|   |   |Impacto Pot. (I)|   |P|I|Riesgo|
|_Nº_|_Amenaza_|_R_|_E_|_DI_|_D_|_A_|_(R+E+DI)_|_(D+A)_|_PxI_|
|1|Inyección de commandos SQL|3|2|2|3|3|7|6|42|
|2||||||||||
|……||||||||||
|15||||||||||

```mermaid
graph TD

  

%% ====================

%% EXTERNAL ENTITIES

%% ====================

A["Browser Client<br>(Customer)"]

B["Authorization Provider<br>(Payment Gateway)"]

  

%% ====================

%% INTERNAL USERS (CORPNET)

%% ====================

AG["Agent"]

AD["Administrator"]

  

%% ====================

%% PROCESSES

%% ====================

P1["P1 – Web Server

(Frontend + API)"]

P2["P2 – Application Logic

(Session Mgmt, Products, Orders)"]

P3["P3 – Payment Processing Module"]

P4["P4 – Logging & Monitoring"]

P5["P5 – Backup & Sync Service"]

  

%% ====================

%% DATA STORES

%% ====================

DS1[("SQL Database<br>Products, Credentials, Orders")]

DS2[("NoSQL Logs<br>Event & Access Logs")]

DS3[("Backup Storage")]

DS4[("Cloud Storage (External)")]

  

%% ====================

%% TRUST BOUNDARIES

%% ====================

subgraph Internet_Boundary[Internet Boundary]

A -->|"1. Login / Browse / Purchase Requests"| P1

P1 -->|"2. Responses (HTML/JSON)"| A

end

  

subgraph CorpNet_Trust_Boundary[CorpNet Trust Boundary]

  

%% Agents/Admin

AG -->|"11. Manage Products"| P2

AD -->|"12. Database Admin Ops"| DS1

AD -->|"13. Log Analysis"| DS2

  

%% Core Flows

P1 -->|"3. API Requests"| P2

P2 -->|"4. SQL Queries"| DS1

DS1 -->|"5. Query Results"| P2

  

P2 -->|"6. Log Events"| P4

P4 -->|"7. Store Logs"| DS2

  

%% Payment Processing

P2 -->|"8. Payment Request"| P3

P3 -->|"9. Authorize Payment"| B

B -->|"10. Payment Response"| P3

P3 -->|P2

  

%% Backup

P2 -->|"14. Backup Data"| P5

P5 -->|"15. Store Backup"| DS3

DS3 -->|"16. Sync to Cloud"| DS4

end
```

![[dfd_diagram.png]]

Your DFD must include:

El objetivo principal de un DFD en el modelado de amenazas es representar cómo fluye la información a través del sistema y dónde se almacena, lo que ayuda a identificar los **límites de confianza (Trust Boundaries)** y a aplicar las categorías de amenazas **STRIDE** (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) en cada elemento.

Aquí tienes las **mejoras principales** que se pueden realizar a tu DFD para optimizar el modelado de amenazas:

## 📐 Mejoras del Diagrama de Flujo de Datos (DFD)

### 1. 🔀 Clarificación de Flujos de Datos y Procesos

El DFD actual ya incluye flujos, pero algunos son muy genéricos o no representan una acción clara.

- **Identificar procesos específicos:** Un **Proceso** (círculo) en el DFD debe representar un componente activo que transforma o dirige datos, no un servidor completo. El actual "Web Server" puede dividirse.
    
    - **Ejemplo:** En lugar de una sola flecha de "Browser Client" a "Web Server" llamada `accesoWeb_IN`, considera si hay flujos distintos para: **"Login/Autenticación"**, **"Carrito/Selección de productos"**, o **"Confirmación de Pedido"**.
        
    - **Mejora:** Divide el "Web Server" en componentes lógicos como un **"Controlador de API/Lógica de Negocio"** y un **"Motor de Autenticación/Sesión"**.
        
- **Detallar los flujos de autorización:** El flujo `AutorizaTarjeta_REQ` y `AutorizaTarjeta_ACK` es bueno, pero el proceso que los genera o recibe debe estar claro (ej: ¿es el "Web Server" o un microservicio interno de pago?).
    

### 2. 🛡️ Delimitación y Etiquetado de Límites de Confianza (Trust Boundaries)

Un DFD efectivo para modelado de amenazas debe tener **límites de confianza claros** que ayuden a separar los componentes con diferentes niveles de privilegio o que están controlados por diferentes entidades.

- **Límite Externo/Internet:** La línea roja punteada `Internet Boundary` es correcta. Todo lo que cruza ese límite debe ser tratado con el mayor escepticismo (asumiendo que es hostil).
    
- **Límite CorpNet/Interno:** El límite `CorpNet Trust Boundary` es el principal para la aplicación interna.
    
- **Añadir un Límite de Acceso a Base de Datos (DB):** Generalmente, el acceso a la base de datos es el recurso más sensible.
    
    - **Mejora:** Dibuja un nuevo límite de confianza **alrededor** de las bases de datos (`BBDD_SQL_Credenciales&Productos` y `BBDD_NoSQL_Logs`) y el proceso que las gestiona. Esto ayuda a identificar las amenazas de **Elevation of Privilege** o **Information Disclosure** que se producen si el servidor web es comprometido y puede acceder directamente a la DB sin un mecanismo de acceso estricto.
        

### 3. 💾 Clarificación de Almacenes de Datos (Data Stores)

Los almacenes de datos (carriles paralelos o similares) son puntos críticos para las amenazas de **Tampering** e **Information Disclosure**.

- **Clarificar Contenido y Acceso:**
    
    - `BBDD_SQL_Credenciales&Productos` es un buen nombre, pero es importante tener en cuenta que contiene **datos sensibles** (credenciales, información de pago/producto).
        
    - `BBDD_NoSQL_Logs` debe recibir flujos claros de los procesos que registran eventos (ej: **Web Server** y **Admin**).
        
- **Flujos de respaldo (Backup):** Los flujos `BackUpDatos_OUT` y `BackUpDatos_IN` que cruzan el límite de confianza hacia `Cloud Storage` son críticos.
    
    - **Mejora:** Asegúrate de que el DFD muestre qué **Proceso** (no solo un "Web Server" genérico) inicia el respaldo y cómo se asegura la **confidencialidad** e **integridad** de los datos que van al **Cloud Storage** (asumiendo que este Cloud Storage está fuera del límite de CorpNet).
        

### 4. 👤 Detallar Actores Externos y Entidades

- **Roles y Privilegios de Agentes/Admins:** Los actores **Agente** y **Admin** están bien, pero sus interacciones con el sistema deben ser distintas.
    
    - **`Admin`:** Debe tener interacciones con procesos de gestión y flujos de `Admin_2_BBDD` o `BBDD_2_Admin` que implican mayor privilegio (ej: Gestión de usuarios, Informes).
        
    - **`Agente`:** Sus flujos (`Agente_2_Web Server`) podrían ser para atención al cliente o gestión de pedidos, no necesariamente acceso directo a credenciales.
        
    - **Mejora:** Asegúrate de que los flujos de datos entre **Agente/Admin** y la base de datos no sean un bypass del servidor de aplicaciones (si lo son, se necesita un nuevo proceso intermedio, como un **"Servidor de Administración"**).
# **Actors**

- Customer (browser client)
    
- Store admin
    
- Store agent

| **Componente**             | **Tipo**         | **Descripción**                                                                |
| -------------------------- | ---------------- | ------------------------------------------------------------------------------ |
| **Agente**                 | Actor Externo    | Personal de la librería con privilegios de gestión de pedidos/clientes.        |
| **Admin**                  | Actor Externo    | Personal de alto nivel con privilegios de gestión de sistema/reportes.         |
| **Browser Client**         | Actor Externo    | El navegador del usuario final (cliente). Cruza el `Internet Boundary`.        |
| **Authorization Provider** | Actor Externo    | Servicio de pago externo (ej. Visa, pasarela de pago).                         |
| **Cloud Storage**          | Almacén de Datos | Almacenamiento externo para copias de seguridad. Cruza el `Internet Boundary`. |
# **Processes**

- Web server
    
- Payment authorization service (external)
    
- Authentication & session manager
    
- Product/Order management logic

| **Componente**                        | **Tipo**            | **Función Principal**                                                                                                       |
| ------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **P1: API Gateway/Frontal Web**       | Proceso             | Maneja peticiones HTTP, autenticación inicial, y enrutamiento. **Cruza el Internet Boundary** (maneja datos no confiables). |
| **P2: Servicio de Lógica de Negocio** | Proceso             | Contiene la lógica central (carritos, pedidos, inventario, precios).                                                        |
| **P3: Servicio de Pago (Interno)**    | Proceso             | Aísla la lógica de autorización de tarjetas y el secreto de comunicación con el `Authorization Provider`.                   |
| **P4: Servicio de Administración**    | Proceso **(Nuevo)** | Proceso dedicado para las interacciones de `Admin` y `Agente` (reportes, consultas de alto privilegio).                     |
# **Data Stores**

- SQL Database (products, credentials, orders)
    
- NoSQL Log database
    
- Backup storage
    
- Cloud Storage (optional, as shown in the original diagram)

# **External Entities**

- Browser client
    
- Authorization provider (credit card/payment server)

# **Data Flows**

Represent all flows:

- Login requests
    
- Product browsing
    
- Order placement
    
- Payment authorization
    
- Logs
    
- Admin operations
    
- Backup flows

Your provided images give examples, but to get **full 3 points** from rubric, you must:

# ✔ Include

- **Trust boundaries** (CorpNet, Internet boundary)
    
- **At least 10–15 data flows**
    
- **Each DB separated (SQL + NoSQL logs)**
    
- **Admin + Agent roles separated**
    
- **Payment provider clearly marked as external trust boundary**

|**Elemento Actual**|**Mejora Sugerida**|**Razón para el Modelado de Amenazas**|
|---|---|---|
|**Web Server**|Separar en: 1. **Proxy/Controlador Web** 2. **Motor de Lógica de Negocio** 3. **Servicio de Pago Interno**|Cada componente maneja diferentes datos (petición HTTP vs. lógica de negocio vs. tokens de pago) y tiene un alcance de ataque diferente.|
|**Flujos de Autorización**|Añadir un **Servicio de Pasarela de Pago** (interno) que hable con el **Authorization Provider**.|La lógica de pago debe estar aislada para proteger la clave de API/secreto que se usa para hablar con el proveedor externo.|
|**Browser Client**|Asegurar que los flujos reflejan tanto **entrada** (datos de usuario, ej: carrito) como **salida** (datos a mostrar, ej: confirmación de pedido).|Permite identificar amenazas de **Information Disclosure** (datos en el navegador) y **Tampering** (datos de entrada).|
|**Base de Datos**|Añadir un límite de confianza para la **Capa de Acceso a Datos (DAO)** que es el único proceso que puede hablar con la DB.|Ayuda a prevenir ataques de **SQL Injection** y **Elevation of Privilege** si el proceso de negocio no está diseñado correctamente.|

# 10 Amenazas

## **1. Inyección SQL**

|Campo|Contenido|
|---|---|
|**Descripción**|Un atacante manipula entradas de usuario para alterar consultas SQL ejecutadas por la aplicación.|
|**Objetivo**|SQL Database (DS1) / Módulo de acceso a datos|
|**Técnicas de ataque**|Inserción de payloads SQL en campos de login, búsqueda o parámetros de URL.|
|**CAPEC**|**CAPEC-66** (SQL Injection)|
|**CWE**|**CWE-89** – Improper Neutralization of Special Elements in SQL Commands|
|**Mitigación**|Uso estricto de _prepared statements_, validación por lista blanca, ORM seguro, privilegios mínimos en la cuenta DB.|

---

## **2. Cross-Site Scripting Reflejado (XSS-R)**

|Campo|Contenido|
|---|---|
|**Descripción**|Inyección de scripts maliciosos que se reflejan inmediatamente en la respuesta al usuario.|
|**Objetivo**|Web Server (P1) / Interfaces HTML|
|**Técnicas de ataque**|Envío de JavaScript en parámetros GET/POST que el servidor devuelve sin sanitizar.|
|**CAPEC**|**CAPEC-63** (Reflected XSS)|
|**CWE**|**CWE-79** – Improper Neutralization of Input During Web Page Generation|
|**Mitigación**|Codificación de salida (HTML encode), Content Security Policy, sanitización de entrada, rechazo de caracteres peligrosos.|

---

## **3. Cross-Site Scripting Almacenado (XSS-S)**

|Campo|Contenido|
|---|---|
|**Descripción**|Scripts maliciosos se guardan en la base de datos y afectan a múltiples usuarios.|
|**Objetivo**|SQL Database (DS1) / Web Server UI|
|**Técnicas de ataque**|Inserción de JavaScript en comentarios, reseñas o formularios almacenados.|
|**CAPEC**|**CAPEC-248** (Stored XSS)|
|**CWE**|**CWE-79**|
|**Mitigación**|Sanitización en el servidor al almacenar, escapes en la salida, CSP restrictiva, validación por lista blanca.|

---

## **4. Fuerza Bruta De credenciales**

|Campo|Contenido|
|---|---|
|**Descripción**|Intentos repetitivos para adivinar contraseñas de clientes o administradores.|
|**Objetivo**|Web Server (P1) / Autenticación|
|**Técnicas de ataque**|Automatización con scripts (Hydra, Burp Intruder).|
|**CAPEC**|**CAPEC-49** (Password Brute Forcing)|
|**CWE**|**CWE-307** – Improper Restriction of Excessive Authentication Attempts|
|**Mitigación**|Rate limiting, bloqueo temporal, MFA, detección de IPs anómalas, hashing Argon2 para contraseñas.|

---

## **5. Secuestro De Sesión (Session Hijacking)**

|Campo|Contenido|
|---|---|
|**Descripción**|Robo de cookies de sesión para hacerse pasar por un usuario legítimo.|
|**Objetivo**|Application Logic (P2) / Módulo de sesiones|
|**Técnicas de ataque**|Robo de cookie vía XSS, sniffing, o vulnerabilidades en transmisión.|
|**CAPEC**|**CAPEC-593** (Session Fixation/Session Hijacking)|
|**CWE**|**CWE-613** – Insufficient Session Expiration|
|**Mitigación**|Cookies `HttpOnly`, `Secure`, rotación de session ID en login, expiración corta, TLS obligatorio.|

---

## **6. Exposición De Datos Sensibles En tránsito**

|Campo|Contenido|
|---|---|
|**Descripción**|Intercepción de datos no cifrados transmitidos entre cliente y servidor.|
|**Objetivo**|Data Flow entre Browser (A) y P1|
|**Técnicas de ataque**|Sniffing, MITM, downgrade de TLS.|
|**CAPEC**|**CAPEC-94** (Man-in-the-Middle)|
|**CWE**|**CWE-319** – Cleartext Transmission of Sensitive Information|
|**Mitigación**|Forzar TLS 1.3, HSTS, deshabilitar HTTP, uso de certificados válidos y pinning opcional.|

---

## **7. Falsificación De Petición En Sitios Cruzados (CSRF)**

|Campo|Contenido|
|---|---|
|**Descripción**|Acciones no autorizadas realizadas por el navegador del usuario autenticado.|
|**Objetivo**|Web Server (P1) / Endpoints autenticados|
|**Técnicas de ataque**|Formularios ocultos o peticiones enviadas desde sitios externos.|
|**CAPEC**|**CAPEC-62** (Cross-Site Request Forgery)|
|**CWE**|**CWE-352** – Cross-Site Request Forgery|
|**Mitigación**|Tokens antifalsificación (synchronizer token pattern), SameSite=Lax/Strict, verificación del origen.|

---

## **8. Elevación De Privilegios Por Mala configuración**

|Campo|Contenido|
|---|---|
|**Descripción**|Un usuario con rol bajo accede a funciones administrativas por fallos en controles de autorización.|
|**Objetivo**|Application Logic (P2) / Admin API|
|**Técnicas de ataque**|Manipulación de rutas (admin=1), prueba de endpoints sin protección.|
|**CAPEC**|**CAPEC-233** (Privilege Escalation)|
|**CWE**|**CWE-269** – Improper Privilege Management|
|**Mitigación**|RBAC estricto en backend, validación de permisos por cada endpoint, separación de APIs de administración.|

---

## **9. Ataque Al Proveedor De Pago (respuesta manipulada)**

|Campo|Contenido|
|---|---|
|**Descripción**|Un atacante intercepta o falsifica la respuesta del gateway de pago para aprobar transacciones no válidas.|
|**Objetivo**|Payment Processing Module (P3)|
|**Técnicas de ataque**|Manipulación del retorno, replay, interceptación.|
|**CAPEC**|**CAPEC-172** (Protocol Manipulation)|
|**CWE**|**CWE-345** – Insufficient Verification of Data Authenticity|
|**Mitigación**|Verificación criptográfica de la respuesta (JWT/HMAC), timestamps, nonces, validación del monto y orden.|

---

## **10. Ataque a Logs (alteración O borrado)**

|Campo|Contenido|
|---|---|
|**Descripción**|Un atacante borra o modifica logs para ocultar rastros de un ataque.|
|**Objetivo**|NoSQL Log Storage (DS2)|
|**Técnicas de ataque**|Acceso directo al servidor, APIs mal protegidas.|
|**CAPEC**|**CAPEC-151** (Log Tampering)|
|**CWE**|**CWE-778** – Insufficient Logging|
|**Mitigación**|Logs inmutables, envío a SIEM externo, control de acceso estricto, write-once storage, alertas en modificación de logs.|

## Dread Map

|Threat|R|E|DI|D|A|**P (R+E+DI)**|**I (D+A)**|**Risk = P×I**|
|---|---|---|---|---|---|---|---|---|
|**1. SQL Injection**|3|3|3|3|3|**9**|**6**|**54**|
|**2. XSS Reflejado (XSS-R)**|2|3|3|2|3|**8**|**5**|**40**|
|**3. XSS Almacenado (XSS-S)**|3|3|2|3|3|**8**|**6**|**48**|
|**4. Fuerza bruta de credenciales**|2|3|3|2|2|**8**|**4**|**32**|
|**5. Secuestro de sesión**|2|3|2|3|3|**7**|**6**|**42**|
|**6. Datos sensibles en tránsito (MITM)**|2|2|2|3|3|**6**|**6**|**36**|
|**7. CSRF**|2|2|3|2|3|**7**|**5**|**35**|
|**8. Elevación de privilegios (misconfig)**|2|2|2|3|3|**6**|**6**|**36**|
|**9. Manipulación respuesta proveedor de pago**|2|3|2|3|3|**7**|**6**|**42**|
|**10. Ataque a logs (alteración / borrado)**|2|2|2|3|2|**6**|**5**|**30**|

---

1. **SQL Injection – 54**
    
2. **Stored XSS – 48**
    
3. **Session Hijacking – 42**
    
4. **Payment Manipulation – 42**
    
5. **Reflected XSS – 40**
    
6. **Sensitive Data Exposure – 36**
    
7. **Privilege Escalation – 36**
    
8. **CSRF – 35**
    
9. **Brute Force – 32**
    
10. **Log Tampering – 30**
