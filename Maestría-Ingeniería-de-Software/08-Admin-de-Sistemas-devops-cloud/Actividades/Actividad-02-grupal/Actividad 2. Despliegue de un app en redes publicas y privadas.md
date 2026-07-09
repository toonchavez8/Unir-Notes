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

# 1. Introducción

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

Crear una arquitectura de un aplicativo en alta disponibilidad en nube pública. El aplicativo puede ser WordPress u otro aplicativo conocido por el equipo o un aplicativo trabajado en otras asignaturas del máster.

Para ello, deberemos desplegar nuestro aplicativo en nube pública con ayuda de la cuenta de AWS Academy.

# 2. Arquitectura propuesta

La arquitectura propuesta despliega WordPress en una VPC propia, con una separación clara entre la capa pública, la capa de aplicación y la capa de datos. Según Amazon Web Services (s. f.-a), una arquitectura con subredes privadas y NAT permite que los servidores internos salgan a Internet para actualizaciones o instalación de paquetes, sin quedar expuestos directamente a conexiones entrantes desde Internet.

El usuario accede al sitio mediante el DNS público del Application Load Balancer (ALB). El ALB se ubica en las subredes públicas y recibe tráfico HTTP por el puerto 80. Después envía cada petición al Target Group asociado a las instancias EC2 que ejecutan WordPress. De esta forma, el balanceador es el único punto de entrada público de la aplicación.

Las instancias EC2 se alojan en subredes privadas de aplicación. No tienen IP pública y no reciben tráfico directamente desde Internet. Su Security Group solo permite HTTP desde el Security Group del ALB. Esta decisión reduce la superficie de exposición y deja a las EC2 como una capa interna, accesible solo a través del balanceador.

La base de datos MySQL queda en subredes privadas de base de datos mediante Amazon RDS. WordPress se conecta a MySQL por el puerto 3306, pero RDS no acepta tráfico desde Internet ni desde cualquier recurso de la VPC; solo permite conexiones cuyo origen sea el Security Group de la aplicación. Amazon Web Services (s. f.-d) indica que una instancia de RDS dentro de una VPC puede controlar su acceso mediante subredes y grupos de seguridad, que es justamente el modelo aplicado en esta práctica.

El Auto Scaling Group mantiene dos instancias de WordPress en subredes privadas de aplicación. Si una instancia se detiene o queda en estado no saludable, el ASG crea otra usando el Launch Template. No se promete recuperación instantánea, pero sí se demuestra que la arquitectura no depende de una sola instancia EC2.

Para la base de datos, el diseño contempla RDS MySQL en subredes privadas y un DB Subnet Group con subredes en dos zonas de disponibilidad. AWS describe Multi-AZ como un despliegue donde RDS mantiene una instancia standby en otra zona para mejorar disponibilidad ante fallos (Amazon Web Services, s. f.-c). En el laboratorio de AWS Academy esta opción puede estar limitada por permisos o costo; por eso se documenta la restricción y se conserva el diseño preparado para dos zonas de disponibilidad.

# 3. Implementación en AWS Academy - Todos

## 3.1. Crear VPC, subredes, IGW, NAT Gateway y rutas - Fer

## 3.2. Crear Security Groups y DB Subnet Group

Para controlar la comunicación entre los componentes de la arquitectura se crearon grupos de seguridad específicos para cada capa del aplicativo. Estos grupos de seguridad funcionan como firewalls virtuales y permiten definir qué tráfico puede entrar o salir de cada recurso dentro de la VPC.

En esta práctica se definieron tres grupos de seguridad principales: uno para el Application Load Balancer, uno para las instancias EC2 y uno para la base de datos MySQL. Esta separación permite aplicar el principio de mínimo privilegio, ya que cada componente solo acepta el tráfico necesario para cumplir su función dentro de la arquitectura.

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

## 3.3. Crear RDS MySQL

Para la capa de datos se utilizó Amazon RDS con motor MySQL. RDS permite crear una base de datos administrada sin instalar manualmente MySQL en una instancia EC2. Según Amazon Web Services (s. f.-d), cuando una instancia de base de datos se despliega dentro de una VPC, se puede controlar en qué subredes queda disponible y qué recursos pueden conectarse a ella mediante Security Groups.

El proceso inició desde `RDS > Databases > Create database`, usando el método de creación estándar y el motor MySQL. Se eligió una configuración de laboratorio, con una instancia pequeña compatible con el entorno de AWS Academy, almacenamiento reducido a 20 GB y la base inicial llamada `wordpress`. En la sección de conectividad se seleccionó la VPC creada para la práctica, el DB Subnet Group de las subredes privadas de base de datos y el Security Group destinado a MySQL.

También se revisó la opción Multi-AZ. La arquitectura ideal tendría RDS con una instancia standby en otra zona de disponibilidad, ya que AWS documenta que Multi-AZ mejora la disponibilidad de la base de datos ante mantenimiento o fallos de infraestructura (Amazon Web Services, s. f.-c). Sin embargo, en AWS Academy esta opción puede no estar disponible por restricciones del laboratorio. Por esa razón, se deja documentado que el DB Subnet Group sí quedó preparado con dos subredes privadas en zonas distintas, aunque la activación de Multi-AZ depende de los permisos del entorno.

La instancia de RDS se configuró con `Publicly accessible: No`. Esta opción es importante porque evita que la base de datos tenga exposición directa a Internet. La comunicación queda limitada al tráfico MySQL por el puerto 3306 desde el Security Group de las instancias EC2 de WordPress. Con esto, aunque el sitio sea público por medio del ALB, la base de datos permanece en una capa privada.

Una vez creada la base de datos, se copió el endpoint de RDS sin incluir el puerto `:3306`. Ese endpoint se utilizó después en el `user data` del Launch Template para que WordPress pudiera conectarse a MySQL durante su instalación. La validación funcional se realiza cuando WordPress carga desde el DNS del ALB y permite guardar contenido, porque eso confirma que las EC2 están llegando correctamente a la base de datos privada.

En caso de que AWS Academy niegue la creación de RDS o alguna configuración avanzada, la alternativa documentada consiste en mantener el mismo diseño lógico y desplegar MySQL en una EC2 privada de base de datos. No es la opción principal, porque exige administrar el motor manualmente, pero conserva la separación entre frontend y datos.

## 3.4. Launch Templates, Target Groups - Maikel

### 3.4.1 Launch Template para EC2

Un **Launch Template** en AWS es un recurso que encapsula la configuración necesaria para lanzar instancias EC2 de manera estandarizada y reproducible.

En este proyecto se usó para definir la configuración base de las instancias que ejecutan WordPress. Incluye la AMI, el tipo de instancia, el Security Group de la aplicación y el script de inicialización o `user data`. De acuerdo con Amazon Web Services (s. f.-e), los Launch Templates permiten guardar parámetros de lanzamiento y reutilizarlos al crear instancias EC2 o grupos de Auto Scaling.

El `user data` instala Apache, PHP y WordPress, crea el archivo de configuración y apunta la aplicación al endpoint de RDS. Esto evita instalar manualmente cada servidor y reduce errores cuando el ASG reemplaza una instancia. También se evita fijar una subred dentro del Launch Template, porque las subredes correctas se asignan después en el Auto Scaling Group.

La ventaja principal es la consistencia: cada EC2 creada por el ASG queda con la misma configuración de frontend y con la misma conexión a la base de datos.

### 3.4.2 Target Groups

Un **Target Group** es el recurso que define a qué destinos (instancias, IPs o Lambdas) enviará tráfico el balanceador de carga (ALB/NLB).

En esta práctica el Target Group se configuró para instancias EC2, protocolo HTTP y puerto 80. No se registraron instancias manualmente, porque esa tarea la realiza el Auto Scaling Group al crear o reemplazar servidores. El health check se configuró sobre una ruta simple, como `/health.html`, para que el balanceador pueda saber qué instancias están listas para recibir tráfico.

Según Amazon Web Services (s. f.-f), Elastic Load Balancing usa health checks para enviar solicitudes solo a destinos disponibles. Por eso el Target Group no es solo una lista de servidores; también es el punto donde se valida si una instancia puede participar en el balanceo.

En este despliegue, el Target Group permite que WordPress no esté expuesto directamente a Internet. El ALB recibe las peticiones públicas y las distribuye únicamente a las EC2 privadas que están registradas y saludables.

### 3.4.3 Conexión entre ambos

El **Launch Template** define cómo se crean las instancias EC2.

- El **Auto Scaling Group (ASG)** usa ese Launch Template para levantar instancias según la demanda.
- El **Target Group** registra esas instancias y el **ALB** distribuye el tráfico hacia ellas.

Así se logra una arquitectura ordenada: el Launch Template define la configuración, el ASG mantiene la cantidad de instancias y el Target Group conecta esas instancias con el ALB.

## 3.5. ALB y ASG - Danny

El Application Load Balancer se creó como balanceador público de tipo `Internet-facing`, ubicado en las dos subredes públicas de la VPC. Su listener HTTP en el puerto 80 reenvía el tráfico hacia el Target Group de WordPress. Según Amazon Web Services (s. f.-b), Elastic Load Balancing distribuye el tráfico entrante entre varios destinos, lo que permite mejorar disponibilidad y tolerancia a fallos en una aplicación.

El Security Group del ALB permite tráfico HTTP desde Internet, usando `0.0.0.0/0` como origen. Esta apertura solo aplica al balanceador, no a las instancias EC2. Las EC2 permanecen en subredes privadas y aceptan tráfico HTTP únicamente desde el Security Group del ALB.

Después se creó el Auto Scaling Group asociado al Launch Template `act2-F1011-lt-wordpress`. El ASG se configuró en las subredes privadas de aplicación, con capacidad deseada de 2 instancias, mínimo 2 y máximo 4. También se conectó al Target Group `act2-F1011-tg-wordpress`, para que las instancias nuevas se registren automáticamente y puedan recibir tráfico cuando pasen el health check.

Amazon Web Services (s. f.-g) indica que un Auto Scaling Group puede integrarse con un balanceador de carga para registrar instancias nuevas y retirar las que dejan de estar saludables. En la práctica, esto permite demostrar recuperación ante fallo: si una instancia se detiene, el ASG crea otra con el Launch Template y el ALB continúa enviando solicitudes solo a los targets saludables.

La validación esperada es que el Target Group muestre las dos instancias en estado `Healthy` y que WordPress cargue desde el DNS público del ALB. Esta prueba confirma que el flujo completo funciona: usuario, ALB, Target Group, EC2 privadas y RDS MySQL.

# 4. Validación de funcionamiento - Fer

# 5. Riesgos, limitaciones y decisiones

## 5.1. Riesgos

**Disponibilidad limitada**: si AWS Academy no permite activar Multi-AZ en RDS, la base de datos queda sin standby administrado en otra zona de disponibilidad. En ese caso, una falla de la zona donde está RDS afectaría a toda la aplicación.

**Escalabilidad restringida**: el autoescalado depende de las cuotas de la cuenta educativa. Aunque el ASG tenga máximo 4 instancias, el laboratorio puede limitar recursos, tipos de instancia o capacidad disponible.

**Seguridad del balanceador**: el ALB sí está expuesto a Internet. Si se migrara a producción, habría que agregar HTTPS, certificados, reglas más estrictas y posiblemente AWS WAF. En esta práctica se usó HTTP para simplificar la validación.

**Dependencia de servicios gestionados**: RDS, ALB, NAT Gateway y Auto Scaling simplifican la operación, pero en una cuenta comercial generan costos. Esta actividad se hizo en AWS Academy, por lo que no refleja por completo el costo de operación real.

**Archivos locales de WordPress**: las publicaciones se guardan en RDS, pero los archivos subidos a `wp-content/uploads` quedan en el disco local de cada EC2. Para esta práctica se validó con contenido de texto. En producción haría falta EFS o S3 para compartir archivos entre instancias.

## 5.2. Limitaciones

**Restricciones de AWS Academy**: algunas opciones pueden no estar disponibles, especialmente Multi-AZ en RDS, cuotas de EC2 o configuraciones avanzadas del balanceador. Por eso se documenta lo implementado y se aclara qué quedaría pendiente en una cuenta sin esas restricciones.

**Recursos reducidos**: las instancias pequeñas y el almacenamiento mínimo sirven para demostrar la arquitectura, pero no para una carga real de usuarios.

**Sin HTTPS**: el ALB se configuró con HTTP en el puerto 80. Para producción se requeriría HTTPS con un certificado de AWS Certificate Manager y un listener en el puerto 443.

**Persistencia de archivos**: WordPress en varias EC2 necesita almacenamiento compartido para medios. Esta práctica se concentró en demostrar balanceo, autoescalado y conexión a RDS, no en resolver la sincronización de archivos.

**Alta disponibilidad parcial**: el frontend sí queda distribuido en dos subredes privadas y protegido por ASG. La base de datos queda preparada para dos AZ mediante DB Subnet Group, pero la alta disponibilidad real de RDS depende de poder activar Multi-AZ.

## 5.3. Decisiones

**Uso de dos zonas de disponibilidad**: se trabajó con dos AZ para separar subredes públicas, privadas de aplicación y privadas de base de datos. Esto permite que el ALB y el ASG distribuyan las instancias de WordPress y que RDS quede preparado para Multi-AZ.

**Application Load Balancer**: se eligió ALB porque la aplicación usa HTTP y porque permite integrar listeners, Target Groups y health checks. El ALB queda en subredes públicas y las EC2 quedan en subredes privadas.

**Base de datos privada**: se eligió RDS MySQL en subredes privadas, con `Publicly accessible: No`, porque WordPress necesita una base relacional y no debe conectarse desde Internet.

**WordPress en EC2**: se usó EC2 en lugar de S3 porque WordPress requiere ejecución de PHP y conexión a MySQL. S3 serviría para contenido estático, pero no para esta aplicación sin rediseñar el modelo.

**Launch Template y ASG**: se decidió automatizar la creación de instancias con Launch Template y mantener dos instancias mediante ASG. Así se evita depender de servidores creados manualmente.

**Mejoras futuras**: en un entorno productivo se añadirían HTTPS, WAF, backups revisados, monitoreo, EFS o S3 para archivos de WordPress y Multi-AZ en RDS si la cuenta lo permite.

# 6. Conclusión

La práctica permitió construir una arquitectura de WordPress más cercana a un despliegue real que a una instalación en una sola máquina. El acceso público quedó concentrado en el Application Load Balancer, mientras que las instancias EC2 y la base de datos permanecieron en subredes privadas. Esta separación ayuda a reducir exposición y deja más claro el flujo de tráfico: Internet entra por el ALB, el ALB distribuye a WordPress y WordPress consulta MySQL en la capa de datos.

El uso del Launch Template y del Auto Scaling Group fue importante porque permitió crear instancias repetibles y mantener dos servidores de aplicación. La prueba de reemplazo de una instancia demuestra que la capa de frontend puede recuperarse sin intervención manual directa, aunque dentro de los límites del laboratorio.

La principal limitación estuvo en la alta disponibilidad de la base de datos. El diseño considera RDS MySQL en subredes privadas y preparado para Multi-AZ, pero AWS Academy puede restringir esa opción. Por eso la conclusión no es que se logró una alta disponibilidad completa de producción, sino que se implementó una arquitectura funcional, segmentada y preparada para crecer. En una cuenta productiva, el siguiente paso sería activar Multi-AZ en RDS, agregar HTTPS, almacenamiento compartido para archivos de WordPress y controles adicionales de seguridad.

# 7. Referencias

Amazon Web Services. (s. f.-a). *Example: VPC with servers in private subnets and NAT*. AWS Documentation. https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html

Amazon Web Services. (s. f.-b). *What is Elastic Load Balancing?* AWS Documentation. https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html

Amazon Web Services. (s. f.-c). *Multi-AZ DB instance deployments for Amazon RDS*. AWS Documentation. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html

Amazon Web Services. (s. f.-d). *Working with a DB instance in a VPC*. AWS Documentation. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html

Amazon Web Services. (s. f.-e). *Launch an instance from a launch template*. AWS Documentation. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html

Amazon Web Services. (s. f.-f). *Health checks for your target groups*. AWS Documentation. https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html

Amazon Web Services. (s. f.-g). *Use Elastic Load Balancing to distribute incoming application traffic in your Auto Scaling group*. AWS Documentation. https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html
