Universidad Internacional de La Rioja

Escuela Superior de Ingeniería y Tecnología

Administración de Sistemas, Virtualización, Cloud Computing y DevOps

Maestría en Ingeniería de Software y Sistemas Informáticos

Actividad 2. Despliegue de un aplicativo en alta disponibilidad en nube pública con redes públicas y privadas (grupal)

|Trabajo fin de estudio presentado por:|Maikel Barrios Insua<br><br>Daniel Campos Castañeda<br><br>Miguel de Jesús Chávez Barragán<br><br>Fernando Enrique García Castellanos<br><br>César Octavio Sánchez Contreras|
|---|---|
|Modalidad:|Por Equipo|
|---|---|
|Director/a:||
|---|---|
|Fecha:|06/30/2026|
|---|---|

[**1. Introducción - Octavio 3**](#_vqhkqqnfxopv)

[**2. Arquitectura propuesta - Miguel 4**](#_83tgq6umqukm)

[**3. Implementación en AWS Academy - todos 5**](#_aja9rxm95g7l)

[3.1. Crear VPC, subredes, IGW, NAT Gateway y rutas - fer 5](#_6ufxhb6xhr5k)

[3.2. Crear Security Groups y DB Subnet Group 5](#_q8nwb1j83nky)

[3.3. Crear RDS MySQL 8](#_rlokwfpb4ye5)

[3.4. Launch Templates, Target Groups - Maikel 9](#_qsfegwcgwovh)

[3.4.1 Launch Template para EC2 9](#_2312dggxtcf3)

[3.4.2 Target Groups 10](#_8f7v7rcnyxkf)

[3.4.3 Conexión entre ambos 10](#_xe68zr5ulklu)

[3.5. ALB y ASG - Danny 11](#_kqnhydxqapuu)

[**4. Validación de funcionamiento - Fer 11**](#_2i7u1yrg1rxn)

[**5. Riesgos, limitaciones y decisiones 11**](#_w252idnm3iw2)

[**Riesgos 11**](#_jj8bqzty6ep0)

[**Limitaciones 11**](#_fmxqfydyt6dm)

[**Decisiones 12**](#_w0q372iaw4nd)

[**6. Conclusiones - Danny 12**](#_5r5t5nbxmc6i)

[**7. Referencias 12**](#_xopawc99zimy)

## Introducción

La actividad tiene como finalidad diseñar y desplegar una arquitectura de alta disponibilidad en una nube pública utilizando los servicios disponibles en AWS Academy. A diferencia de un despliegue básico en una sola instancia, esta práctica integra diversos componentes para representar un entorno más cercano a una arquitectura productiva.

El aplicativo seleccionado para el despliegue es WordPress, ya que permite implementar una arquitectura de varias capas: una capa de presentación o frontend, ejecutada en instancias EC2 privadas; una capa de balanceo, expuesta a Internet mediante un Application Load Balancer; y una capa de datos, implementada mediante una base de datos MySQL ubicada en subredes privadas. Esta separación permite mejorar la seguridad del entorno, ya que los usuarios externos no acceden directamente a las instancias EC2 ni a la base de datos, sino únicamente al balanceador público.

La arquitectura propuesta considera la creación de una VPC con direccionamiento privado y seis subredes distribuidas en dos zonas de disponibilidad. Las subredes públicas se utilizan para los componentes que requieren comunicación directa con Internet, como el balanceador y la salida mediante NAT Gateway. Las subredes privadas alojan las instancias del aplicativo y la base de datos, reduciendo la exposición directa de los recursos internos.

Además, se contempla el uso de grupos de seguridad para controlar el tráfico permitido entre los diferentes componentes. De esta manera, el balanceador puede recibir solicitudes HTTP desde Internet, las instancias EC2 solo aceptan tráfico proveniente del balanceador y la base de datos MySQL únicamente permite conexiones desde las instancias del aplicativo. Con ello, se busca aplicar una estrategia de seguridad por capas y limitar el acceso únicamente a los servicios necesarios.

En conjunto, la actividad permite aplicar conceptos de redes en la nube, subredes públicas y privadas, balanceo de carga, autoescalado, bases de datos privadas y control de acceso mediante reglas de seguridad, integrándose en una solución cloud funcional y documentada.

**Objetivos de la actividad**

- Creación de una red (VPC) con direccionamiento privado con seis subredes, con salida a Internet, tanto las redes privadas como públicas.
- Creación de un frontend en red privada expuesto a Internet a través de un balanceador.
- Creación de un grupo de autoescalado para el frontend del aplicativo si se despliega en EC2. (Opcional: se puede sustituir las EC2 por un almacenamiento S3 para el frontend).
- Creación de una base de datos en alta disponibilidad en subredes privadas separadas del frontend.

**Descripción de la actividad**

Crear una arquitectura de un aplicativo en alta disponibilidad en nube pública. El aplicativo puede ser un Wordpress u otro aplicativo conocido por el equipo o un aplicativo trabajado en otras asignaturas del máster.

Para ello, deberemos desplegar nuestro aplicativo en nube pública con ayuda de la cuenta de AWS Academy.

## Arquitectura propuesta

La idea es que cuando un usuario abre el sitio, usa el DNS público del AWS Application Load Balancer o ALB. El ALB está en las subredes públicas y recibe tráfico HTTP por el puerto 80. Después envía la petición a una de las instancias EC2 del Target Group.

Las EC2 están en subredes privadas. No tienen IP pública y no se abren al mundo. Esto reduce la superficie de exposición: si alguien intenta entrar por SSH o por una IP directa, no debería poder hacerlo.

WordPress se conecta a RDS por el puerto 3306. La regla más importante aquí es que RDS no acepta tráfico desde Internet, ni desde cualquier IP de la VPC. Solo acepta conexiones donde su origen sea el Security Group de la aplicación.

El Auto Scaling Group mantiene dos instancias. Si falla, el grupo crea otra. No hay que prometer una recuperación perfecta en segundos, pero sí se puede demostrar que AWS detecta la instancia dañada y la reemplaza.

RDS Multi-AZ mantiene una copia standby en otra zona de disponibilidad. Si AWS Academy no permite activar Multi-AZ por permisos o costo, tendríamos que ajustar esto pero se muestra que el DB Subnet Group sí está preparado con dos subredes privadas en AZ distintas.

## Implementación en AWS Academy - todos

### Crear VPC, subredes, IGW, NAT Gateway y rutas - fer

### Crear Security Groups y DB Subnet Group

Para controlar la comunicación entre los componentes de la arquitectura se crearon grupos de seguridad específicos para cada capa del aplicativo. Estos grupos de seguridad funcionan como firewalls virtuales y permiten definir qué tráfico puede entrar o salir de cada recurso dentro de la VPC.

En esta práctica se definieron tres grupos de seguridad principales: uno para el Application Load Balancer y uno para las instancias EC2. Esta separación permite aplicar el principio de mínimo privilegio, ya que cada componente solo acepta el tráfico necesario para cumplir su función dentro de la arquitectura.

Figura X. Lista de Security Groups creados para la arquitectura.

El primer grupo de seguridad corresponde al Application Load Balancer. Este grupo permite tráfico HTTP por el puerto 80 desde Internet, utilizando como origen 0.0.0.0/0. Esta regla es necesaria porque el balanceador será el punto público de entrada al aplicativo. Los usuarios externos no se conectarán directamente a las instancias EC2, sino al DNS público del balanceador.

Figura X. Reglas de entrada del Security Group del Application Load Balancer.

El segundo grupo de seguridad corresponde a las instancias EC2 del aplicativo. A diferencia del balanceador, este grupo no permite tráfico directamente desde Internet. Su regla de entrada permite tráfico HTTP por el puerto 80 únicamente desde el Security Group del Application Load Balancer. De esta manera, las instancias EC2 permanecen en subredes privadas y solo reciben solicitudes que han pasado previamente por el balanceador.

Figura X. Reglas de entrada del Security Group de las instancias EC2 del aplicativo.

El tercer grupo de seguridad corresponde a la base de datos MySQL. Este grupo permite tráfico por el puerto 3306, correspondiente a MySQL, únicamente desde el Security Group de las instancias EC2 del aplicativo. Con esta configuración, la base de datos no queda expuesta a Internet ni acepta conexiones desde cualquier recurso de la VPC, sino solamente desde la capa de aplicación.

Figura X. Detalles del Security Group de la base de datos MySQL.

Después de los grupos de seguridad, se creó un **DB Subnet Group** para la base de datos. Este recurso agrupa las subredes privadas destinadas a la capa de datos y permite indicar a Amazon RDS en qué subredes puede desplegar la instancia de base de datos. Para esta arquitectura se seleccionaron las subredes privadas de base de datos ubicadas en distintas zonas de disponibilidad.

Figura X. DB Subnet Group configurado con subredes privadas de base de datos.

El DB Subnet Group se configuró únicamente con subredes privadas, separadas de las subredes públicas y de las subredes privadas del frontend. Esta decisión refuerza la seguridad de la arquitectura, ya que la base de datos queda aislada del acceso directo desde Internet. Además, al incluir subredes en más de una zona de disponibilidad, la arquitectura queda preparada para una configuración de alta disponibilidad en caso de que el entorno de AWS Academy permita habilitar Multi-AZ.

Con esta configuración, el flujo de comunicación queda limitado de forma controlada: los usuarios acceden al Application Load Balancer, el balanceador envía las solicitudes a las instancias EC2 privadas y estas instancias son las únicas autorizadas para conectarse a la base de datos MySQL.

### Crear RDS MySQL

Amazon nos ofrece contenedor para crear bases de datos Entrando al La función RDS se seleccionó data veces y creamos una base de datos Utilizamos el método creación estándar con el motor mysql Dado que estamos bajo un plan gratuito utilizamos el Tear gratuito Intentamos utilizando el motor dev/test. Se creó el método la instancia el identificador destinamos una contraseña seleccionamos un t 3 micro Bajamos el monto de espacio a 20 GB Y le pedimos que no se conectara a un ec dos todavía.

Asignamos la base de datos a nuestro DPC Previamente nombrado en este ejemplo Y la activamos el multi AZ. Y le dimos crear una base de datos y nos topamos con nuestra primera pared.

La pared fue que no tenemos permisos para crear una instancia de base de datos que sea de Multizona.

AWS Academy no otorga el permiso rds:CreateDBInstance, por lo que no es posible crear una instancia de Amazon RDS. Para continuar con el laboratorio sin modificar la arquitectura general, se implementará un servidor MySQL sobre una instancia EC2 ubicada en la subred privada de base de datos. De esta manera, ambas instancias de WordPress continuarán compartiendo la misma base de datos.

Regresamos nuevamente al proceso de creación utilizamos una base de datos de desarrollo prueba Micro Volvemos a configurar la la conectividad validamos los campos de Resource la BPC le asignamos la DB Subnet Grupo previamente designada le le limitamos el acceso público y validamos de que el grupo de seguridad ya estaba previamente existido y era el que habíamos creado De ahí le dimos una configuración adicional donde le dijimos que la base de datos inicial se iba a llamar WordPress para este ejemplo y nuevamente le damos crear base de datos.

Y se y se logra la creación de la base de datos correctamente vamos a la parte de la instancia para ver cuál es y nos para sacar la URL ya aquí ya no era necesario copiar el puerto porque pues solamente íbamos a utilizar nombre al host.

Y con esto la base de datos implementa dentro de nuestras subredes privadas que definimos previamente evitando el acceso directo desde el Internet las únicas instancias autorizadas para conectarse son aquellas que utilizan el grupo de seguridad mientras que el acceso a la base de datos está restringida mediante a nuestra conexión de los grupos de seguridad de la base de datos.

Esta arquitectura permite que por lo menos tengamos cualquier instancia está apuntando a esta Base de datos. Con la URL luego lo pasamos al launch template.

### Launch Templates, Target Groups - Maikel

#### 3.4.1 Launch Template para EC2

Un **Launch Template** en AWS es un recurso que encapsula la configuración necesaria para lanzar instancias EC2 de manera estandarizada y reproducible.

Su significado y utilidad en este proyecto son:

- **Definición centralizada de configuración**: Incluye AMI, tipo de instancia, claves SSH, roles IAM, scripts de inicialización (_user data_), y etiquetas.
- **Reutilización y consistencia**: Permite que todas las instancias del grupo de autoescalado (ASG) se creen con la misma configuración, evitando errores manuales.
- **Versionado**: Se pueden mantener diferentes versiones del template para evolucionar la infraestructura sin perder trazabilidad.
- **Escalado automático**: El ASG consume el Launch Template para crear nuevas instancias EC2 cuando la carga aumenta, garantizando que todas tengan la misma configuración de WordPress.

En este despliegue, el Launch Template asegura que cada instancia EC2 del frontend de WordPress se levante con la misma configuración, reforzando la estabilidad y la reproducibilidad.

#### 3.4.2 Target Groups

### 

Un **Target Group** es el recurso que define a qué destinos (instancias, IPs o Lambdas) enviará tráfico el balanceador de carga (ALB/NLB).

Su significado y utilidad en este proyecto son:

- **Enrutamiento del tráfico**: El ALB recibe las peticiones desde Internet y las distribuye a los targets registrados en el grupo (en este caso, las instancias EC2 con WordPress en subred privada).
- **Tipos de target**:
    - instance: registra directamente instancias EC2.
    - ip: registra direcciones IP privadas (común en ECS con modo awsvpc).
    - lambda: invoca funciones Lambda.
- **Health checks**: El Target Group define cómo verificar que los targets están sanos (por ejemplo, comprobando /wp-login.php o /health), y solo envía tráfico a instancias saludables.
- **Escalabilidad y resiliencia**: Al integrarse con el ASG, las nuevas instancias EC2 se registran automáticamente en el Target Group, garantizando que el balanceador siempre tenga destinos disponibles.

En este despliegue, el Target Group es clave porque el **WordPress nunca está expuesto directamente a Internet**: el ALB recibe las peticiones y las distribuye a las instancias EC2 privadas registradas en el grupo.

#### 3.4.3 Conexión entre ambos

El **Launch Template** define cómo se crean las instancias EC2.

- El **Auto Scaling Group (ASG)** usa ese Launch Template para levantar instancias según la demanda.
- El **Target Group** registra esas instancias y el **ALB** distribuye el tráfico hacia ellas.

Así se logra una arquitectura modular: configuración estandarizada (Launch Template), escalado automático (ASG), y distribución segura del tráfico (Target Group + ALB).

### ALB y ASG - Danny

## Validación de funcionamiento - Fer

## Riesgos, limitaciones y decisiones

## Riesgos

**Disponibilidad limitada**: Al no poder usar multi-AZ en la capa gratuita de AWS Academy, la base de datos queda en una sola zona de disponibilidad. Esto implica riesgo de caída total si esa zona sufre una interrupción.

**Escalabilidad restringida**: El autoescalado puede estar limitado por cuotas de la cuenta educativa, lo que reduce la capacidad de absorber picos de tráfico.

**Seguridad del balanceador**: Aunque el aplicativo está protegido en subred privada, el balanceador sí está expuesto a Internet. Si no se configuran reglas de seguridad y WAF, puede ser un vector de ataque.

**Dependencia de servicios gestionados**: Si se usa RDS o ELB, hay riesgo de sobrecostos al migrar a una cuenta comercial, ya que la capa gratuita oculta parte del costo real.

**Inconsistencia entre los diferentes aplicativos:** Al no poderse usar las réplicas de RDS, es preciso para mantener la alta disponibilidad usar un sistema de sincronización entre las instancias para mantener coherencia en los datos almacenados. Por la complejidad que requiere, no se puso en práctica este sistema de consistencia.

## Limitaciones

**Restricciones de AWS Academy**: No se permite multi-AZ en RDS ni balanceadores avanzados, lo que limita la arquitectura de alta disponibilidad real.

**Recursos reducidos**: CPU, memoria y almacenamiento son mínimos, lo que afecta el rendimiento de WordPress bajo carga.

**Sin soporte empresarial**: La capa gratuita no incluye soporte técnico avanzado, lo que obliga al equipo a resolver incidencias por sí mismo.

**Persistencia de datos**: Si se usa S3 para frontend estático, la capa gratuita puede no cubrir escenarios de replicación o versionado.

## Decisiones

**Uso de una sola AZ**: Se decidió crear dos zonas de disponibilidad y replicar el aplicativo más la base de datos asociada a cada uno, usar un balanceador con un patrón que valide la existencia de estos servicios, en caso de que uno se pierda el tráfico se enruta totalmente al siguiente.

**Balanceador de carga**: Se optó por un balanceador de carga de tipo aplicación, ubicar los aplicativos en un segmento de red privada de cada az y asignar el balanceador a un segmento de red público, así este comunica todo el tráfico de internet al aplicativo WordPress..

**Base de datos**: Se desplegó en subred privada con backups automáticos, como medida de mitigación ante fallos.

**WordPress en EC2 vs. S3**: Se eligió EC2 para mayor control y realismo, aunque se reconoce que S3 con CloudFront sería más eficiente para contenido estático.

**Documentación de mejoras futuras**: Se deja constancia de que en un entorno productivo se añadirían WAF, CloudFront y multi-AZ en la capa de serialización para cumplir con alta disponibilidad real.

## Conclusiones - Danny

## Referencias