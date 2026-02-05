
Sesiön HTTP: concepto
Una sesiån web (o HTTP) es una secuencia de peticiones y respuestas (o transacciones) asociadas al
mismo usuario.
Las aplicaciones web modernas y complejas deben mantener informaciön (o eI estado) de cada
usuario durante una secuencia de peticiones.
Las sesiones proporcionan la capacidad de establecer atributos, como permisos o informaciön de
cualquier tipo manejada por Ia aplicaciön, que se pueden utilizar en cada
una de las interacciones del usuario con la aplicaciön web hasta que
finalice su sesiön.

---
//diagrama de secuencia de usario haccia servidor web y a base de datos
Usuario
Petici6n (sin token) ->
redireccion (auth) <-
Autentificacion ->
Peticiån (con token) ->
Datos de la sesi6n <-
peticion (con token) ->

// servidor web hacia base de datos de session
Crear nuevo token
Comprobar token y verificar estado
Renovar token
destruir token

Servidor web

Base de datos sesiones

---

Sesiån HTTP: concepto
Objeto devuelto
Object
Enumeration
long
String
long
int
ServletContext
void
boolean
void
void
void
void
Método y paråmetros
getAttribute(java.lang.String name)
getAttributeNames()
getCreationTime()
getld()
getLastAccessedTime()
getMaxlnactivelnterval()
getServletContext()
invalidate()
isNew()
removeAttribute(String name)
removeValue(String name)
setAttribute(String name, Object value)
setMaxlnactivelnterval(int interval)

---

Sesion HTTP: formas de envio
Cookie (cabecera HTTP eståndar):
Cookie: id=012345; .
Paråmetro URL (URL rewriting):
https://portal.example.com/private; id=012345?...
Argumento URL (peticiön GET):
https://portaI.example.com/private?id=012345& .

Argumento cuerpo (peticiön POST):
<INPUT
Campo oculto de formulario (HTML):
<INPUT NAME-"id"

---

Propiedades de seguridad de la sesiön:
Debe contener al menos 128 bits de datos aleatorios.
Establecer tiempo måximo de inactividad y absoluto.
Debe haber un modo de terminar la sesiön: log out.
Siempre se debe comenzar una nueva sesiön después de la autenticaciön.
Implementarlo aprovechando librerias del propio framework de desarrollo.


---*