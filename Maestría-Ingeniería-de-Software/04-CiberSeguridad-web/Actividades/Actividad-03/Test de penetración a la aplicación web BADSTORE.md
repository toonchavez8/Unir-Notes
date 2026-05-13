
**Actividad 3 – Test de penetración a la aplicación web BadStore**

Informe técnico

**Introducción**

Este documento describe el proceso y los resultados de un test de penetración realizado sobre la aplicación web vulnerable BadStore en un entorno controlado de laboratorio. La finalidad es identificar vulnerabilidades, evidenciar su impacto y proponer medidas de mitigación.

**Objetivos de la actividad:**

- Aprender a encontrar vulnerabilidades de seguridad en una aplicación web.
- Explotar vulnerabilidades de seguridad en una aplicación web.
- Aprender a utilizar una herramienta de análisis dinámico DAST en aplicaciones web a través de un procedimiento por fases.

**Alcance y limitaciones**

• Alcance: aplicación BadStore desplegada en una máquina virtual (VM) del laboratorio.

• Fuera de alcance: explotación más allá de la demostración controlada (p. ej., persistencia, pivoting).

• Limitaciones: pruebas realizadas sin afectar a terceros y sin degradar deliberadamente la VM.

**Entorno de pruebas**

Completa esta sección con tus datos reales:

**• IP objetivo (BadStore):** 192.168.56.110 (ejemplo)

**• URL de acceso:** http://192.168.56.110/ (redirige a /cgi-bin/badstore.cgi)

**• Sistema atacante:** Kali/Parrot/VM de prácticas (indicar versión)

**• Herramientas (ejemplos):** Navegador, Burp Suite Community, OWASP ZAP, Nmap (solo enumeración), etc.

**Metodología**

Se siguió una metodología ligera basada en buenas prácticas de pentesting:

1) Reconocimiento y enumeración (servicios, rutas, funcionalidades).

2) Análisis de superficie de ataque (entradas, parámetros, cookies, roles).

3) Pruebas de vulnerabilidades (OWASP Top 10 como guía).

4) Evidencias: capturas de pantalla y registros de las pruebas.

5) Recomendaciones y plan de remediación.

**Hallazgos**

En esta sección registra cada vulnerabilidad encontrada. Incluye: descripción, evidencia, impacto, severidad y mitigación.

**Hallazgo 1 – Inyección SQL en búsqueda y registro**  
**Categoría OWASP:** A03:2021 – Inyección (SQLi)

**Ubicación:**  
• Funcionalidad de búsqueda rápida (Quick Item Search).  
• Funcionalidad de registro de usuarios (`action=register`).

**Descripción:**  
Se valida que la aplicación es vulnerable a inyección SQL debido a que no valida ni sanitiza adecuadamente la entrada del usuario y construye consultas SQL de forma dinámica mediante concatenación directa. Esto se evidencia al introducir payloads simples de inyección SQL (por ejemplo `a'='a` o comillas simples vacías), los cuales alteran el comportamiento esperado de la aplicación y devuelven resultados completos o permiten el registro exitoso sin validaciones adecuadas.  
La respuesta de la aplicación demuestra que las entradas del usuario son interpretadas directamente por la base de datos, lo que confirma la ausencia de consultas parametrizadas y controles de validación.

**Evidencia (captura):**  
Inserta aquí la imagen donde BadStore devuelve resultados completos ante la inyección SQL en la búsqueda y la pantalla de bienvenida tras el registro exitoso con datos manipulados.

**Evidencia técnica detallada:**

_Búsqueda vulnerable_  
URI afectada:  
[http://localhost/cgi-bin/badstore.cgi](http://localhost/cgi-bin/badstore.cgi)

Payload utilizado:  
`searchquery=a'='a`

Petición:

```
GET http://localhost/cgi-bin/badstore.cgi?action=search&searchquery=a'='a HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Pragma: no-cache
Cache-Control: no-cache
```

Respuesta:

```
HTTP/1.1 200 OK
Content-Type: text/html
```

Sección HTML que demuestra el resultado:  
La aplicación devuelve todos los artículos del catálogo, lo que confirma que la condición inyectada siempre evalúa como verdadera y altera la lógica de la consulta SQL.

---

_Registro vulnerable_  
URI afectada:  
[http://localhost/cgi-bin/badstore.cgi?action=register](http://localhost/cgi-bin/badstore.cgi?action=register)

Petición:

```
POST http://localhost/cgi-bin/badstore.cgi?action=register HTTP/1.1
Content-Type: application/x-www-form-urlencoded

fullname=' '&email=@' '&passwd=123&pwdhint=''&role=A
```

Respuesta:

```
HTTP/1.1 200 OK
```

Sección HTML que demuestra el resultado:  
La aplicación muestra el mensaje de bienvenida “Welcome to BadStore.net!”, confirmando que el registro fue procesado correctamente a pesar de contener entradas maliciosas con comillas simples, lo cual evidencia inyección SQL en el proceso de inserción de datos.

**Impacto potencial:**  
• Acceso no autorizado a información sensible almacenada en la base de datos.  
• Modificación o eliminación de registros.  
• Bypass de controles de autenticación y registro de usuarios con roles arbitrarios.  
• Posible escalamiento de privilegios dentro de la base de datos y de la aplicación.

**Severidad sugerida:**  
Alta.

**Recomendaciones de mitigación:**  
• Implementar consultas parametrizadas o prepared statements en todas las interacciones con la base de datos.  
• Validar, normalizar y sanitizar todas las entradas del usuario (preferentemente mediante listas blancas).  
• Implementar manejo seguro de errores para evitar la exposición de información interna o lógica de consultas SQL.  
• Aplicar el principio de mínimos privilegios a la cuenta de base de datos utilizada por la aplicación.

**Vulnerabilidad 2, SQL Injection – MySQL**

Descripción de la vulnerabilidad

En continuación del informe de vulnerabilidades de ZAP, se identificó la del tipo SQL Injection específica para MySQL.  
La aplicación BadStore construye consultas SQL de forma dinámica utilizando directamente los datos introducidos por el usuario, sin aplicar mecanismos adecuados de validación, sanitización o parametrización de las entradas.

Esta debilidad permite que caracteres especiales y fragmentos de código SQL enviados por el usuario sean interpretados directamente por el motor de base de datos MySQL, alterando la estructura original de la consulta.

Evidencia de la vulnerabilidad

La vulnerabilidad se detectó al introducir caracteres especiales (por ejemplo, comillas simples ') en el campo de búsqueda de productos. Como resultado, la aplicación devolvió un mensaje de error SQL visible al usuario, exponiendo información interna del sistema y del motor de base de datos utilizado.

![Test de penetración a la aplicación web BADSTORE](<Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/Test%20de%20penetración%20a%20la%20aplicación%20web%20BADSTORE%201.png>)Este error confirma que:

- La aplicación utiliza el motor MySQL.
- La entrada del usuario se inserta directamente en la consulta SQL.
- No existe un manejo seguro de errores, ya que se muestra información sensible al usuario final.

La consulta SQL parcial expuesta evidencia que el parámetro introducido por el usuario es evaluado directamente dentro de la cláusula WHERE, lo cual constituye una vulnerabilidad de inyección SQL.

Impacto

La explotación de esta vulnerabilidad podría permitir a un atacante:

- Manipular la lógica de las consultas SQL.
- Acceder a información sensible almacenada en la base de datos.
- Enumerar tablas, columnas o registros del sistema.
- Comprometer la confidencialidad e integridad de los datos.
- Facilitar ataques adicionales basados en la información revelada por los mensajes de error.

![Test de penetración a la aplicación web BADSTORE](<Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/Test%20de%20penetración%20a%20la%20aplicación%20web%20BADSTORE%202.png>)Aunque en esta prueba no se logró una explotación completa (por ejemplo, extracción de datos mediante UNION SELECT), la exposición del error SQL es suficiente para confirmar la existencia de la vulnerabilidad.

Clasificación según OWASP

- OWASP Top 10 2021:  
    A03 – Injection
- Tipo específico:  
    SQL Injection – MySQL

Esta vulnerabilidad corresponde a una inyección SQL dependiente del motor MySQL, diferenciándose de una inyección SQL genérica por la exposición explícita de errores y sintaxis propios de MySQL.

Recomendaciones

Para mitigar esta vulnerabilidad se recomienda:

- Implementar consultas parametrizadas (Prepared Statements).
- Validar y sanitizar estrictamente todas las entradas proporcionadas por el usuario.
- Evitar la exposición de mensajes de error detallados al usuario final.
- Aplicar el principio de mínimos privilegios en las cuentas de la base de datos.
- Implementar un manejo seguro de errores y registros internos.

**Vulnerabilidad 3, Buffer Overflow**

A continuación, se presentan tres casos documentados de vulnerabilidades de tipo BufferOverflow. Cada caso fue detectado automáticamente por el scanner y posteriormente verificado mediante análisis manual del request, response y payload utilizado.

**Caso 1:** **Buffer Overflow en Servicio SOAP (Content-Length: 2353)**

- **Descripción:** Se identificó una vulnerabilidad de Buffer Overflow en el servicio SOAP de búsqueda de productos de BADSTORE. Esta vulnerabilidad se manifiesta cuando el servidor intenta procesar un mensaje SOAP con contenido excesivamente largo, causando un desbordamiento en el búfer asignado para almacenar datos de entrada.
- **Request HTTP:**

POST [http://www.badstore.net/cgi-bin/soapsearch.cgi](http://www.badstore.net/cgi-bin/soapsearch.cgi) HTTP/1.1

Host: [www.badstore.net](https://www.badstore.net/)

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36

Pragma: no-cache

Cache-Control: no-cache

Content-Type: text/xml;charset=UTF-8

SOAPAction:

Content-Length: 2353

- **Payload del Ataque:** El payload consiste en una cadena de 2,353 caracteres compuesta por secuencias alfanuméricas aleatorias diseñadas para exceder la capacidad del búfer. A continuación se muestra un extracto representativo del payload completo:

AuxAlrjukVfNOYMREMdtcBSUkcoBfytKVDRJFOPNRvbFPixySsrQBDpsdMFORfPjZbpvDZeOwiFDZdxKEhsBtJMNxGqlcoNIuaBrsgLMQafKOZnsrYGcDXCYGeksQZtSuBHgMKUlGgJypcCDqgCZFwYxiAQRNYdPeKSGnwxHyngnTqyArtkCtRfCxJhFGJvhatupfWnjMgFADKYGpCRODyksuHJMwPjsyTHneAtQQGDfbvoGipLuSmYQCdcBwRfTRgsIebhVcfuNMYxAHCRiRCSttCpVMiSRKUGDYSlBXstTaCrxneTibhwWuapAMcJDnknoguAvByFNhYLpVKnTnEVnvHXxAmLPoMHeWnOmJFxcZRDtYuPMOvGvugyIHyjGvSPUNwokJZQnivMXrslphasysMuKBKFASLwDvKbEQEnMlbxEnPqCiJvbIHlJATvPGjbuitvqJtHwtRlnjecqDLjqVHheBUIqHKMlVfhLYNKUJCdgvIxNuvnUAnbBxiakaSqAFMjFbKfvvfuEanTdrTwVsuKimrEoqVGeJeUvrbAsGIIYVcUZBMtkjbhvGcNyVBvAkVgrSPaguyYWCropEoGlnREICOFxbTexPpeSPIHlXtACLyQnikqmwlsmwlbCakeGLQQweMnjRkLDeyPYCTKkASYrdtSAbPXqrsWsTlIegdavperOTddZPDMXIjUZqmvdKYVpTbmgRMXxSuBOkaoKGjHWiITXQfNBEZmbggUtEBYLjwrQxNDJHKdFlGKvJeYvSnpQddvAsqvOgjitdQBfdImmpJjfCKhZYsmEZNIKFXRoBWcJLsmuBHyBDBLUkRUwrbNkCZWhWKhUYnxZCYUDJsHvuEhrSZdjwIxgjMilqQWrsTkANmPOFbjRJcWxUPyymFuLYuSkrZJPHVarNufHqceZslWsmQIUwBWkrpAfIKTFEcWZFvOnKWnNdeicyfcoRdXlMFaYswGuCmLEBJHtCkttmFLgjEhcLNXGHFVHwtWPEfKctcSyMWfnxCKFxTCayiYqoQxWXCfnBqFaRTJhbkamdUPretuMAjNTaqeEmxpJVcjuYCISuqcTKcrjfYMaHghvVoZECqGWIvQLIKksviiIGceEXJNBddZkcBsEJpjITYMXSbqVLonSpPvfgtsPlXalYGABLAjbrxBRWVfsuLDEIidhtcEEUHfcFqxPSugUYkyJnuoVsanpJbDtgyLFmgPJvDjhiQFtDYBVADQFFEKBmTabrTibRlVeOGEykYXVEbMTqSvrPavJtjEiXbtXvHtodhEXlVoBvmyeAnFlZkLDIUUERDDNRgksKAcXfbqtsVmGVgtrjnIsVGuRgjJwuPBORRggxkVBdSIlAEIVPNGDdsUcfTVRIPqwCVCHYBuNIMSVcHTHEUPotQUAOdgfFkfgUHPdqoklQQgZgrLCItXKTegnSCWCrfLKewPSwgWdZJPEGJjWfxZJCTBXdrJQXPXvqelyCkCKsuOjpXXbxRGtCBRIViLpfJcrSdILYoBVtdBDJgKxCDoKxHjUNRfEEAYJWTBMjAqymkLQaaIdARksWZsbkpyaBxmyaeJJUmiCAUhahybyBtmPioFZYXFtLktZaecoukyEyoUSPTxoAiBaQXBcaRWYTXGayVgZICqrVySLmybCMQmixLXYiZTWAYjLyDCAEIegaVMZvMquRtJtaSrsVYoGcKMNepDwTIXNUdkbyCjSgJYTvZednwedyomaoGWisapEJrnlBNDGoVtgcHPvhjTitMHyljUqoDAJSnAWuIkJSyGBZqyvKNjImMJmvfuERxamqPDbkKfGAICyqJwUmRUxUBmUwWTFLfYIrKXCEAJXNVSEyaDgjGBVOkvtqfnqNPoyolNJJOSffpBfPYofQeMbKfwtyPssPgKMItlPfXjayWiKEeEvljAMVmvAONNwwZEuZqYwkXiLZOuGgoaaBtCYAvSTAQbBWCmjEMfJbwywNKHSGLfwyhRukevGqFPyNJVOieILQabggcmKEYJUTQLQLUbYBUNZdNbAFnPjFFjCVlZcfHykcfIWDodnkrrrEMZdeMxgopCZxRNCbUCQgRwrKGjMUTjmaxQRVZbu

- **Response HTTP:**

HTTP/1.1 500 Internal Server Error

Date: Fri, 23 Jan 2026 03:25:30 GMT

Server: Apache/1.3.28 (Unix) mod_ssl/2.8.15 OpenSSL/0.9.7c

SOAPServer: SOAP::Lite/Perl/0.60

Content-Length: 663

Connection: close

Content-Type: text/xml; charset=utf-8

- **Evidencia de Explotación:** La evidencia principal del buffer overflow exitoso es:
- Connection: close

El header "Connection: close" indica que el servidor cerró abruptamente la conexión debido a un error en el procesamiento. Esto es característico de un crash o fallo grave causado por el desbordamiento del búfer. Adicionalmente:

- El código HTTP 500 (Internal Server Error) confirma un fallo interno del servidor
- El Content-Length de la respuesta de error es de solo 663 bytes, indicando una respuesta de error genérica
- El servidor no pudo procesar el mensaje SOAP y devolvió un error fatal

**Caso 2:** **Buffer Overflow en Servicio SOAP (Content-Length: 2353)**

- **Descripción:**El segundo caso de Buffer Overflow fue identificado en el mismo endpoint SOAP pero con un payload ligeramente diferente de 2,328 bytes. Esta variante demuestra que la vulnerabilidad no depende de un tamaño específico sino que existe un rango de tamaños que causan el overflow, sugiriendo que el búfer tiene una capacidad entre 2,000 y 2,400 bytes aproximadamente.
- **Request HTTP:**

POST [http://www.badstore.net/cgi-bin/soapsearch.cgi](http://www.badstore.net/cgi-bin/soapsearch.cgi) HTTP/1.1

Host: [www.badstore.net](https://www.badstore.net/)

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36

Pragma: no-cache

Cache-Control: no-cache

Content-Type: text/xml;charset=UTF-8

SOAPAction:

Content-Length: 2328

- **Payload del Ataque:** Este payload utiliza un patrón diferente al Caso 1, comenzando con la secuencia "noEeouxk" y continuando con patrones alfanuméricos variados. La longitud de 2,328 bytes es 25 bytes menor que el Caso 1, pero igualmente efectiva para causar el overflow:

NoEeouxkMgSLiZVNOAuqeiaXlGQGwFvLbPAwsQtrGEIpeNYbtFUOLqFXdQxyukubsKWfWxHdQSKTMPJpsMViFyXoijLUaBvQmJHqocytQoFtunERmxkgZxcGqcisnTNgxndkCgHvDyfNHFvyvnxAKUsjYUlEJWhGGZMenGQREGVgOsRRnPfirrCduCnJuLmoxRCHVpIdSYwtcehmjOMFJeKUWMLiFwNCNrbNXKCxKJWjbFubYGpwYribBWpbGGXSvEBxwEGBFSkEuMVlwHTFaPWUyCimukLnoTdDROjvwXZtGVxOUXpICBvvRwdaeckasvxoYyiyUyKPWBZ...

(El payload completo contiene 2,328 caracteres con patrones similares continuos)

- **Response HTTP:**

HTTP/1.1 500 Internal Server Error

Date: Fri, 23 Jan 2026 03:25:30 GMT

Server: Apache/1.3.28 (Unix) mod_ssl/2.8.15 OpenSSL/0.9.7c

SOAPServer: SOAP::Lite/Perl/0.60

Content-Length: 2658

Connection: close

Content-Type: text/xml; charset=utf-8

- **Evidencia de Explotación:** Similar al Caso 1, la evidencia del overflow incluye:
- Connection: close

Sin embargo, este caso presenta una diferencia notable: el Content-Length de la respuesta de error es de 2,658 bytes, significativamente mayor que los 663 bytes del Caso 1. Esto sugiere que:

- El servidor intentó generar un mensaje de error más detallado
- La respuesta puede incluir trazas de stack o información de debugging
- El payload específico causó un tipo diferente de fallo interno
- Potencialmente hay más revelación de información en el error

**Caso 3:** **Buffer Overflow en Servicio SOAP (Content-Length: 2354)**

- **Descripción:** El tercer caso identificado utiliza un payload de 2,354 bytes, confirmando definitivamente que existe un patrón consistente de buffer overflow en el rango de 2,300-2,400 bytes. Este caso utiliza un patrón de payload completamente diferente a los dos anteriores, comenzando con "FghVHNYZ", lo que demuestra que la vulnerabilidad no depende del contenido específico del payload sino únicamente de su longitud.
- **Request HTTP:**

POST [http://www.badstore.net/cgi-bin/soapsearch.cgi](http://www.badstore.net/cgi-bin/soapsearch.cgi) HTTP/1.1

Host: [www.badstore.net](https://www.badstore.net/)

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36

Pragma: no-cache

Cache-Control: no-cache

Content-Type: text/xml;charset=UTF-8

SOAPAction:

Content-Length: 2354

- **Payload del Ataque:** Este tercer payload presenta un patrón completamente distinto, comenzando con "FghVHNYZ" y continuando con secuencias alfanuméricas diferentes a los casos anteriores:

FghVHNYZTuJsavCfoWhkDKTsbVBRqmxphWaqIXDaOnGvXkHrCiAnQhAIgJUygeBqdBgKdyHVvHYoipwaGAQSnBJbYgoJQuQJZNZWHSILHUjMqqmQRuDlytkAEMlQSnUolirvGpUopmZLrFcBvRAOGZECEGqELrrthNZHjGsrRhgZplkbbojXryrbZgAJHgPKdJMvmhxKYGoEYvmNhMIQWOWAvydaODDbRWfoIJchtrGeMUDSeCYaygmOKstIrnAYUvXMEGInpIRbPDpExdeQvQUEknoUThtqFOpKwaUqSQOcqtZLxlYnhsdHOqrGeviWhSaScITKHdxjTAWfmoVxaybAeXkOOoOGCalNvCkNeXXpqLvBMeWsNGkUBrRifcyKmcKtHceRufdObYNFpoGUbPQRcQypkcOIImbhePXtuXBaJYgNaEYFhCeRYOjafDPFxXBhcqCsRYNHeXfZWscABTwjoTMDimGJMIspeVpllGrhlHaTRPSTwFYXeITVYStjFDuBnvZaTAotfRCVMEuxFAGvoiNyxRwyWiNCYqFeoTLvHgbiLbWBrmUdHtdSjNkxPJBaruXqDYaSMuKhcQnhyZyyTPWtu...

(El payload completo contiene 2,354 caracteres con patrones similares continuos)

- **Response HTTP:**

HTTP/1.1 500 Internal Server Error

Date: Fri, 23 Jan 2026 03:25:30 GMT

Server: Apache/1.3.28 (Unix) mod_ssl/2.8.15 OpenSSL/0.9.7c

SOAPServer: SOAP::Lite/Perl/0.60

Content-Length: 663

Connection: close

Content-Type: text/xml; charset=utf-8

- **Evidencia de Explotación:** La respuesta es prácticamente idéntica al Caso 1:
- Connection: close
- HTTP 500 Internal Server Error
- Content-Length: 663 (mismo tamaño que Caso 1)

Esto sugiere que los payloads de longitudes 2,353 y 2,354 bytes causan el mismo tipo de fallo, mientras que el payload de 2,328 bytes (Caso 2) causa un fallo ligeramente diferente que genera una respuesta de error más larga (2,658 bytes).

**Conclusiones del Análisis Comparativo**

1. Existe un búfer crítico en el procesamiento SOAP con capacidad aproximada de 2,000-2,300 bytes.
2. Cualquier payload que exceda esta capacidad causa buffer overflow independientemente de su contenido.
3. El comportamiento del servidor sugiere dos posibles puntos de fallo: uno que genera respuestas de error pequeñas (663 bytes) y otro que genera respuestas más grandes (2,658 bytes).
4. La vulnerabilidad es altamente reproducible y predecible, haciéndola fácil de explotar por atacantes.
5. La solución requiere modificación del código fuente y recompilación del ejecutable backend.

**Hallazgo 4 – Falta de cabecera Anti-Clickjacking (Systemic)**

**Categoría OWASP**

**OWASP Top 10 2017 / 2021:  
****A06 – Security Misconfiguration**

**Identificadores**

- **CWE:** 1021 – Improper Restriction of Rendered UI Layers or Frames
- **WASC:** 15 – Application Misconfiguration
- **ZAP Alert ID:** 1021

**Características de Alerta**

![Test de penetración a la aplicación web BADSTORE](<Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/Test%20de%20penetración%20a%20la%20aplicación%20web%20BADSTORE%203.png>)

**Descripción**

La aplicación BadStore no implementa mecanismos de protección contra ataques de _clickjacking_, debido a la ausencia de cabeceras HTTP de seguridad destinadas a restringir la inclusión de su contenido dentro de marcos (iframe) de sitios externos.

En concreto, las respuestas HTTP generadas por el servidor no incluyen las cabeceras X-Frame-Options ni Content-Security-Policy con la directiva frame-ancestors, lo que permite que la aplicación sea incrustada sin restricciones dentro de un iframe. Esta situación expone a los usuarios a posibles ataques de ingeniería social, en los cuales un atacante podría superponer elementos visuales engañosos para inducir la ejecución de acciones no deseadas.

**Evidencia**

Durante el análisis realizado con **OWASP ZAP**, se identificó que las respuestas HTTP correspondientes a la URL afectada no contienen cabeceras de protección contra _clickjacking_. La alerta generada por la herramienta confirma explícitamente la ausencia de dichas cabeceras, clasificando la vulnerabilidad con **riesgo medio** y **confianza media**.

En particular, ZAP detectó que no están presentes las siguientes cabeceras de seguridad:

- X-Frame-Options
- Content-Security-Policy: frame-ancestors

Adicionalmente, se realizó una prueba práctica mediante la creación de un archivo HTML externo que incrusta la aplicación BadStore dentro de un iframe. Al abrir dicho archivo en el navegador, se comprobó que la aplicación se carga correctamente dentro del marco, lo que valida de forma práctica la posibilidad de explotación de esta vulnerabilidad.

<!DOCTYPE html>

<html>

<head>

<title>Clickjacking Test</title>

</head>

<body>

<h3>Prueba de Clickjacking</h3>

<iframe

src="http://www.badstore.net/cgi-bin/badstore.cgi"

width="900"

height="600"

style="opacity:0.7">

</iframe>

</body>

</html>

![Test de penetración a la aplicación web BADSTORE](<Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/Test%20de%20penetración%20a%20la%20aplicación%20web%20BADSTORE%204.png>)

**Impacto**

La explotación de esta vulnerabilidad podría permitir a un atacante:

- Ejecutar ataques de _clickjacking_ mediante la incrustación de la aplicación en sitios maliciosos.
- Inducir al usuario a realizar acciones no deseadas, como clics involuntarios o envíos de formularios.
- Facilitar ataques de ingeniería social aprovechando la interfaz legítima de la aplicación.
- Comprometer la confianza del usuario y la integridad de las acciones realizadas dentro de la aplicación.

Si bien esta vulnerabilidad no permite un compromiso directo del servidor ni de la base de datos, sí representa un riesgo relevante desde el punto de vista del usuario final y de la seguridad del lado cliente.

**Severidad sugerida**

**Media**, en concordancia con la clasificación proporcionada por **OWASP ZAP**, ya que la vulnerabilidad fue detectada mediante un **análisis pasivo**, al identificarse la ausencia de cabeceras de seguridad en las respuestas HTTP sin necesidad de enviar _payloads_ ni modificar el comportamiento de la aplicación.

No obstante, aunque se trate de un hallazgo pasivo desde el punto de vista de su detección, el impacto potencial sobre la interacción del usuario y la superficie de ataque de la aplicación justifica su clasificación como severidad media. La posibilidad de incrustar la aplicación dentro de un iframe externo habilita escenarios de ataque basados en ingeniería social y engaño visual, con consecuencias relevantes para la seguridad del usuario final.

**Recomendaciones de mitigación**

Para mitigar esta vulnerabilidad se recomienda:

- Implementar la cabecera HTTP X-Frame-Options con los valores:
    - DENY, si la aplicación no debe ser embebida en ningún sitio externo.
    - SAMEORIGIN, si únicamente se permite su inclusión desde el mismo dominio.
- Implementar la cabecera Content-Security-Policy utilizando la directiva:
    - frame-ancestors 'self';
- Aplicar estas cabeceras de forma consistente en **todas las respuestas HTTP** de la aplicación.
- Realizar revisiones periódicas de configuración de seguridad como parte del ciclo de desarrollo seguro.

**Relación con el test de penetración realizado**

Este hallazgo fue identificado durante el test de penetración llevado a cabo con **OWASP ZAP**, mediante un escaneo automatizado complementado con un ataque activo. La concordancia entre la alerta generada por la herramienta y la auditoría manual realizada confirma la validez del hallazgo y evidencia la importancia de evaluar no solo vulnerabilidades de inyección o lógica, sino también aspectos de **configuración de seguridad sistémica**.

**Conclusión del hallazgo**

La vulnerabilidad **Anti-Clickjacking (Systemic)** detectada en la aplicación BadStore pone de manifiesto una deficiencia de configuración que afecta directamente a la protección del usuario final. La ausencia de cabeceras de seguridad adecuadas permite escenarios de ataque basados en engaño visual, los cuales pueden comprometer la integridad de las acciones realizadas dentro de la aplicación.

Este hallazgo refuerza la necesidad de incorporar controles de seguridad a nivel de cabeceras HTTP como parte de una configuración segura por defecto y demuestra el valor de complementar herramientas automáticas de análisis con auditorías manuales para validar el impacto real de las vulnerabilidades detectadas.

**Resumen ejecutivo de riesgos**

Incluye un resumen en 5–10 líneas con los hallazgos más importantes y su impacto.

• Total de hallazgos: __

• Críticos: __ | Altos: __ | Medios: __ | Bajos: __

• Riesgo global (cualitativo): __

**Plan de remediación**

Prioriza acciones por impacto y esfuerzo:

• Corto plazo (quick wins): __

• Medio plazo: __

• Largo plazo: __

**Anexos**

• Capturas de pantalla numeradas (Anexo A, B, C...).

• Evidencias adicionales (logs, requests/responses).

• Referencias (OWASP, RFCs, documentación).

**Conclusión**

**Referencias bibliográficas**