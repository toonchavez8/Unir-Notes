# Conceptos generales sobre sistemas operativos y nube pública

> **Aviso:** esta actividad debe completarse en la plataforma. Solo se dispone de un intento. Una vez enviada, se considerará cerrada. La puntuación y las respuestas correctas se mostrarán al finalizar el periodo de entrega.

## Objetivo

Profundizar en conceptos de sistemas operativos, virtualización, nube pública y DevOps mediante diez preguntas de opción múltiple.

## Instrucciones

Cada pregunta tiene una sola respuesta correcta y vale un punto. Debajo de cada respuesta se incluye una justificación y un ejemplo práctico para facilitar el estudio.

---

## 1. ¿Qué hace un servidor DNS?

- A. Provee direcciones IP a las redes empresariales.
- B. Mantiene usuarios en Active Directory.
- C. Proporciona acceso a Internet.
- **D. Responde a las solicitudes del host.**

### Respuesta

**D. Responde a las solicitudes del host.**

### Justificación

Un servidor DNS recibe consultas de los equipos y responde con la información necesaria para localizar un recurso. Su función más conocida es traducir nombres de dominio fáciles de recordar, como `www.ejemplo.com`, en direcciones IP, como `203.0.113.10`. El equipo necesita esa dirección para comunicarse con el servidor de destino.

La opción A describe mejor la función de DHCP, que asigna direcciones IP y otros parámetros de red. La opción B corresponde a un servicio de directorio. La opción C tampoco es correcta: el acceso a Internet depende del proveedor, el router, la puerta de enlace y el enrutamiento. DNS ayuda a encontrar servidores por nombre, pero no crea la conexión.

**Ejemplo:** al escribir `campus.unir.net` en el navegador, el equipo consulta un servidor DNS para conocer la IP asociada. Si DNS falla, todavía puede existir conexión a Internet, aunque el sitio no se abra por su nombre.

---

## 2. ¿Para qué sirve una directiva de grupo?

- A. Para crear usuarios en un dominio.
- B. Para monitorizar recursos de un dominio.
- C. Para crear un dominio y un bosque.
- **D. Para administrar la configuración de un dominio.**

### Respuesta

**D. Para administrar la configuración de un dominio.**

### Justificación

Las directivas de grupo, conocidas como GPO por *Group Policy Object*, permiten aplicar configuraciones de manera centralizada a usuarios y equipos dentro de un dominio de Active Directory. El administrador puede definir reglas de seguridad, restricciones del sistema, configuraciones del escritorio, scripts de inicio de sesión o parámetros de actualización sin configurar cada computadora por separado.

Una GPO no se usa principalmente para crear usuarios, monitorizar recursos ni construir dominios y bosques. Esas tareas se realizan con otras herramientas de administración de Active Directory y de supervisión.

**Ejemplo:** una organización puede crear una directiva que exija contraseñas de cierta longitud, bloquee la sesión después de varios intentos fallidos y desactive las memorias USB. Al vincularla con una unidad organizativa, las reglas se aplican a todos los equipos incluidos en ella.

---

## 3. En la estructura de archivos de Linux, ¿qué guarda la ruta `/etc`?

- A. Datos variables específicos del sistema que deben conservarse entre los arranques.
- **B. Archivos de configuración específicos del sistema.**
- C. Datos de ejecución de procesos iniciados desde el último arranque.
- D. Software instalado, bibliotecas compartidas y datos de programa de solo lectura.

### Respuesta

**B. Archivos de configuración específicos del sistema.**

### Justificación

El directorio `/etc` contiene archivos de configuración que afectan al sistema y a los servicios instalados. Allí suelen definirse usuarios, redes, nombres de host, tareas programadas y parámetros de aplicaciones. Son archivos de configuración, no los ejecutables de los programas.

Las demás opciones corresponden a otros directorios. Los datos variables y persistentes suelen guardarse en `/var`; los datos volátiles generados desde el último arranque se encuentran normalmente en `/run`; el software y los datos de solo lectura se distribuyen principalmente entre `/usr`, `/lib` y otros directorios relacionados.

**Ejemplo:** `/etc/hosts` asocia localmente nombres con direcciones IP, `/etc/passwd` contiene información básica de las cuentas y `/etc/ssh/sshd_config` define el comportamiento del servidor SSH.

---

## 4. ¿Para qué sirven los registros de Docker?

- A. Para controlar los contenedores en ejecución.
- **B. Para almacenar y distribuir imágenes de Docker.**
- C. Para permitir la comunicación entre dos contenedores.
- D. Para instalar hosts remotos de Docker.

### Respuesta

**B. Para almacenar y distribuir imágenes de Docker.**

### Justificación

Un registro de Docker es un repositorio de imágenes de contenedor. Permite publicar, versionar, almacenar y descargar imágenes. Docker Hub es un registro público conocido, aunque una empresa también puede operar uno privado, como Harbor o GitHub Container Registry.

El registro no controla los contenedores que ya están en ejecución. Esa tarea corresponde al motor de Docker o a un orquestador como Kubernetes. Tampoco crea la comunicación entre contenedores, pues eso se resuelve mediante redes de Docker, ni instala hosts remotos.

**Ejemplo:** un equipo construye la imagen `miempresa/api:2.4.0` y la publica con `docker push`. Después, un servidor ejecuta `docker pull miempresa/api:2.4.0` para descargar exactamente esa versión y crear un contenedor.

---

## 5. ¿Cuál no es una ventaja de la virtualización?

- **A. Uso gratuito del software que se virtualiza.**
- B. Reducción de infraestructura física.
- C. Aumento de la tolerancia a fallos.
- D. Mejora del rendimiento.

### Respuesta

**A. Uso gratuito del software que se virtualiza.**

### Justificación

Virtualizar un sistema no elimina las licencias del software. Los sistemas operativos, bases de datos y aplicaciones comerciales mantienen sus condiciones de uso aunque se ejecuten en una máquina virtual. Algunos fabricantes licencian por máquina virtual, núcleo físico, host o clúster, por lo que el costo debe revisarse caso por caso.

La virtualización sí puede reducir servidores físicos al consolidar cargas y puede mejorar la continuidad mediante migración en vivo, replicación o reinicio automático en otro nodo. La opción D necesita un matiz: una máquina virtual no supera necesariamente el rendimiento nativo del mismo hardware y el hipervisor introduce cierta sobrecarga. En el contexto de la pregunta, puede entenderse como un mejor aprovechamiento de recursos. La afirmación claramente falsa es que el software pasa a ser gratuito.

**Ejemplo:** ejecutar Windows Server o SQL Server en VMware no cancela la obligación de contar con sus licencias. El servidor físico puede aprovecharse mejor, pero las licencias siguen vigentes.

---

## 6. ¿Qué es una zona de disponibilidad?

- A. Una de varias particiones de la infraestructura global, sin aislamiento completo.
- **B. Una partición aislada de la infraestructura global.**
- C. Una partición conectada sin separación de fallos.
- D. Una partición híbrida de la infraestructura global.

### Respuesta

**B. Una partición aislada de la infraestructura global.**

### Justificación

Una zona de disponibilidad es una ubicación física aislada dentro de una región de nube. Suele estar formada por uno o más centros de datos con energía, refrigeración y conectividad redundantes. Las zonas de una región se conectan mediante redes de baja latencia, pero se separan para evitar que un fallo local afecte a todas al mismo tiempo.

La expresión "completamente aislada" debe entenderse como aislamiento operativo y de fallos, no como ausencia de comunicación. Las zonas sí están conectadas. Lo importante es que una interrupción eléctrica o un problema físico en una zona no debería inutilizar las demás.

**Ejemplo:** una aplicación puede ejecutar una instancia en la zona A y otra en la zona B detrás de un balanceador. Si la zona A falla, la instancia de la zona B puede continuar atendiendo solicitudes, siempre que los datos y las dependencias también tengan redundancia.

---

## 7. ¿Cuál no es un servicio base en la nube?

- A. Gestión de usuarios.
- B. Cómputo.
- **C. Entrega de contenidos.**
- D. Almacenamiento.

### Respuesta

**C. Entrega de contenidos.**

### Justificación

Los servicios base de una plataforma de nube son las capacidades sobre las que se construyen otras soluciones. Entre ellas se encuentran el cómputo para ejecutar cargas, el almacenamiento para conservar datos y la gestión de identidades y accesos para controlar quién utiliza los recursos.

La entrega de contenidos, normalmente implementada mediante una CDN, es un servicio de nivel superior. Utiliza infraestructura distribuida para guardar copias de archivos cerca de los usuarios y reducir la latencia, pero depende de redes, almacenamiento y seguridad.

**Ejemplo:** una máquina virtual que procesa solicitudes es cómputo; un depósito de objetos que guarda imágenes es almacenamiento; IAM controla quién puede leerlas. Una CDN copia esas imágenes en ubicaciones cercanas a los visitantes para acelerar su descarga, pero la aplicación puede funcionar sin ella.

---

## 8. ¿A qué ámbito pertenece cada VPC?

- A. A dos regiones del proveedor para conseguir disponibilidad.
- B. A dos centros de datos dentro de la misma región.
- **C. A una sola región.**
- D. Ninguna de las anteriores.

### Respuesta

**C. A una sola región.**

### Justificación

Una VPC, o nube privada virtual, es una red lógica aislada que se crea dentro de una región. En ella se pueden definir subredes en distintas zonas de disponibilidad, tablas de rutas, puertas de enlace y reglas de seguridad. Aunque abarque varias zonas, la VPC sigue perteneciendo a una sola región.

Para comunicar recursos de regiones distintas se necesitan VPC diferentes y un mecanismo de interconexión, como *VPC peering*, una red de tránsito o una VPN. Por eso una VPC no pertenece automáticamente a dos regiones ni se limita a dos centros de datos.

**Ejemplo:** una VPC creada en `us-east-1` puede tener una subred en `us-east-1a` y otra en `us-east-1b`. Ambas pertenecen a la misma VPC. Para usar recursos en `eu-west-1`, se crea otra VPC y se configura la comunicación entre las dos.

---

## 9. Los microservicios son un enfoque de arquitectura y organización para desarrollar...

- A. Software compuesto por pasarelas de comunicación independientes.
- B. Software compuesto por servidores Linux.
- **C. Software compuesto por servicios independientes que se comunican mediante API bien definidas.**
- D. Hardware y software compuestos por servicios independientes.

### Respuesta

**C. Software compuesto por servicios independientes que se comunican mediante API bien definidas.**

### Justificación

La arquitectura de microservicios divide una aplicación en servicios pequeños y con responsabilidades delimitadas. Cada servicio implementa una capacidad de negocio, puede tener su propio ciclo de despliegue y se comunica con otros mediante contratos claros, como API HTTP, gRPC o mensajería. La independencia no significa que los servicios no colaboren, sino que el acoplamiento entre ellos se mantiene controlado.

Los microservicios no tienen que ejecutarse en Linux y una pasarela de API es solo un componente posible. Tampoco se trata de dividir el hardware, sino de organizar el software por servicios.

**Ejemplo:** en una tienda en línea puede haber un servicio de catálogo, otro de pedidos y otro de pagos. Cuando se confirma una compra, pedidos se comunica con pagos mediante una interfaz definida. El equipo de pagos puede actualizar su servicio sin desplegar toda la aplicación, siempre que respete el contrato acordado.

---

## 10. ¿Cuál es el objetivo del despliegue continuo?

- A. Realizar los despliegues de forma autónoma, sin controles definidos.
- B. Realizar los despliegues mediante archivos JSON.
- C. Realizar los despliegues de forma gradual.
- **D. Realizar los despliegues de forma automatizada o casi automatizada.**

### Respuesta

**D. Realizar los despliegues de forma automatizada o casi automatizada.**

### Justificación

El despliegue continuo busca que los cambios que superan las validaciones puedan llegar a producción con poca o ninguna intervención manual. Para conseguirlo se automatizan la compilación, las pruebas, el empaquetado y la publicación. También se incorporan observabilidad y mecanismos de reversión cuando el riesgo lo exige.

La opción A es imprecisa porque "autónomo" podría interpretarse como un proceso sin supervisión ni reglas. La automatización sí opera bajo controles definidos. Los archivos JSON pueden formar parte de alguna herramienta, pero no son el objetivo. Un despliegue gradual, como *canary* o *blue-green*, es una estrategia para reducir riesgos, aunque no define por sí solo el despliegue continuo.

Conviene distinguir despliegue continuo de entrega continua. En la entrega continua, cada cambio queda listo para producción, pero una persona puede aprobar la publicación. En el despliegue continuo, los cambios que cumplen las condiciones del flujo se publican automáticamente.

**Ejemplo:** un desarrollador envía un cambio al repositorio. La canalización ejecuta las pruebas, genera la imagen, la publica en el registro y actualiza la aplicación en producción. Si la tasa de errores supera el límite configurado, la plataforma revierte la versión. El proceso está automatizado, pero no carece de control.

---

## Resumen de respuestas

| Pregunta | Respuesta correcta | Concepto principal |
| ---: | :---: | --- |
| 1 | D | Resolución de consultas DNS |
| 2 | D | Administración centralizada mediante GPO |
| 3 | B | Configuración del sistema en `/etc` |
| 4 | B | Almacenamiento y distribución de imágenes |
| 5 | A | La virtualización no elimina licencias |
| 6 | B | Aislamiento de fallos por zona |
| 7 | C | La CDN no es un servicio base |
| 8 | C | Una VPC pertenece a una región |
| 9 | C | Servicios independientes comunicados por API |
| 10 | D | Automatización del despliegue |

