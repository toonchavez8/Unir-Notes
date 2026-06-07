# Introducción a AWS: Consola AWS, servicios EC2 y RDS

**Universidad:** UNIR  
**Asignatura:** MODAM Administración de Sistemas, Virtualización, Cloud Computing y DevOps  
**Actividad:** Introducción a AWS. Consola AWS, servicios EC2 y RDS  
**Estudiante:** Miguel de Jesús Chávez Barragán  
**Docente:** Carlos Martín Martínez Ferráez  
**Fecha:** 06-08-2026  

# Introducción

Esta actividad tiene como propósito practicar el uso inicial de Amazon Web Services mediante AWS Academy. El trabajo se desarrolla a partir de tres ejercicios principales: desplegar una página web en una instancia EC2 con Linux, publicar un juego en una instancia EC2 con Windows Server y crear una base de datos MySQL en Amazon RDS para conectarse a ella desde una herramienta externa.

Amazon EC2, cuyo nombre completo es Elastic Compute Cloud, permite crear servidores virtuales dentro de AWS. En esta actividad lo utilicé como el espacio donde corren las aplicaciones web. En términos prácticos, EC2 funciona como una computadora en la nube que se configura de acuerdo con el sistema operativo, la capacidad de cómputo, las reglas de seguridad y el tipo de acceso que se necesita.

Amazon RDS, por su parte, es un servicio administrado de bases de datos relacionales. Su nombre completo es Relational Database Service. Este servicio permite trabajar con motores como MySQL, PostgreSQL o MariaDB sin tener que instalar manualmente todo el servidor de base de datos. En la actividad se utilizó MySQL para crear una base de datos, conectarse de forma remota y validar que los cambios se reflejaran correctamente.

El entorno de AWS Academy fue importante porque permitió trabajar con servicios reales de AWS dentro de un laboratorio controlado. El presupuesto disponible de 50 USD y el límite de tiempo activo del laboratorio ayudan a practicar sin dejar recursos encendidos de forma indefinida. A partir de este entorno pude reforzar conceptos de nube pública, servidores virtuales, grupos de seguridad, acceso remoto y conectividad entre servicios.

# Objetivos

El objetivo general de la actividad es aplicar conocimientos básicos de nube pública mediante el uso de AWS Academy, Amazon EC2 y Amazon RDS.

Los objetivos específicos son los siguientes:

- Crear una instancia Linux en EC2 y desplegar una página web estilo Netflix.
- Crear una instancia Windows Server en EC2 y publicar un juego web.
- Crear una base de datos MySQL en Amazon RDS, conectarse remotamente y realizar modificaciones para comprobar su funcionamiento.

# Desarrollo de la actividad

## Exploración de AWS Academy y la consola de AWS

Para iniciar la actividad fue necesario ingresar a la plataforma de AWS Academy. Este entorno está diseñado para que estudiantes puedan practicar con servicios de nube en un ambiente real, pero con controles de presupuesto y tiempo. Esto reduce el riesgo de generar costos elevados por dejar instancias activas o por crear recursos sin seguimiento.

Al entrar al panel del LMS, que corresponde al Learning Management System, seleccioné el laboratorio de aprendizaje asignado. Desde ahí inicié el laboratorio con la opción **Start Lab**. Después de unos minutos, el ícono del círculo ubicado junto al enlace de AWS cambió a color verde, lo cual indicó que el laboratorio ya estaba listo para usarse.

**Figura 1**  
*Panel de AWS Academy con el laboratorio iniciado.*  
[Insertar captura aquí]

Después ingresé a la Consola de administración de AWS mediante el enlace **AWS**. La sesión se abrió con una cuenta temporal, válida durante el tiempo activo del laboratorio. Este punto es importante porque todo el trabajo realizado depende de que el temporizador siga activo y de que los recursos se mantengan dentro del presupuesto asignado.

Dentro de la consola validé que la región de trabajo fuera `us-east-1`, correspondiente a **US East (N. Virginia)**. Una región de AWS es una ubicación geográfica donde AWS tiene centros de datos, y cada región cuenta con una o más zonas de disponibilidad. Para esta actividad mantuve los recursos en la misma región con el fin de evitar confusiones de ubicación entre EC2, RDS y los grupos de seguridad.

**Figura 2**  
*Consola principal de AWS con la región `us-east-1` seleccionada.*  
[Insertar captura aquí]

Desde la consola exploré los servicios disponibles para la actividad. Me enfoqué principalmente en EC2 y RDS, ya que eran los servicios requeridos para desplegar las aplicaciones web y crear la base de datos.

## Implementación de la página web en Linux

Para cumplir el primer objetivo, regresé al servicio EC2 y seleccioné la opción **Launch instance**. La instancia fue nombrada `ec2-linux-act1`. Como sistema operativo elegí Amazon Linux y seleccioné una instancia de tamaño pequeño, tipo micro, porque era suficiente para el ejercicio y ayudaba a mantener bajo el consumo del laboratorio.

**Figura 3**  
*Configuración inicial de la instancia Linux en EC2.*  
[Insertar captura aquí]

Durante la creación de la instancia definí un par de llaves, o **key pair**, para poder conectarme por SSH. Descargué el archivo `.pem` y lo nombré de forma similar a la instancia para mantener orden y facilitar su identificación. Este archivo es importante porque permite autenticar la conexión remota desde la terminal.

Después de lanzar la instancia, configuré las reglas del grupo de seguridad. Un grupo de seguridad en AWS funciona como un firewall virtual que define qué tráfico puede entrar o salir de una instancia. Para este caso agregué tres reglas principales:

- **SSH**, por el puerto `22`, limitado a mi dirección IP.
- **HTTP**, por el puerto `80`, abierto al público para visualizar la página.
- **HTTPS**, por el puerto `443`, abierto al público como parte de la configuración web.

**Figura 4**  
*Reglas de entrada configuradas en el grupo de seguridad de la instancia Linux.*  
[Insertar captura aquí]

La regla de SSH la limité a mi IP por seguridad, ya que ese puerto permite administrar la instancia desde la terminal. Las reglas de HTTP y HTTPS se dejaron públicas porque la intención era que el sitio pudiera visualizarse desde el navegador.

AWS ofrece distintas formas de conexión a una instancia EC2. En este caso utilicé EC2 Instance Connect y también conexión por SSH desde la terminal.

Para conectarme mediante EC2 Instance Connect seguí este flujo:

1. Seleccioné la instancia.
2. Hice clic en **Connect**.
3. Entré a la pestaña **EC2 Instance Connect**.
4. Presioné nuevamente **Connect**.

Para la conexión desde mi terminal utilicé el archivo `.pem` y el DNS público de la instancia:

```bash
chmod 400 "ec2-linux-act1.pem"
ssh -i "ec2-linux-act1.pem" ec2-user@ec2-98-86-108-89.compute-1.amazonaws.com
```

Una vez dentro de la instancia, instalé y habilité Apache con los siguientes comandos:

```bash
sudo dnf install -y httpd wget unzip
sudo systemctl enable httpd
sudo systemctl start httpd
```

Estos comandos instalan el servidor web Apache, lo configuran para iniciar automáticamente y lo ejecutan en la instancia. Después validé el estado del servicio:

```bash
sudo systemctl status httpd
```

**Figura 5**  
*Servicio Apache activo en la instancia Linux.*  
[Insertar captura aquí]

Posteriormente descargué el archivo comprimido de la página estilo Netflix y lo descomprimí en una carpeta temporal:

```bash
mkdir -p ~/sitio-netflix
cd ~/sitio-netflix
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip
unzip Netflix.zip
```

Después de validar con `ls` que los archivos se descomprimieron correctamente, los copié al directorio público de Apache:

```bash
sudo cp -r ./* /var/www/html/
```

Finalmente, regresé a la consola de AWS, copié la dirección IPv4 pública de la instancia y probé el sitio desde el navegador:

```text
http://98.86.108.89/
```

**Figura 6**  
*Página web estilo Netflix publicada desde la instancia Linux.*  
[Insertar captura aquí]

Durante este ejercicio me quedó más clara la diferencia entre una IP pública y una IP privada. La IP pública permite acceder a la instancia desde Internet cuando el grupo de seguridad lo autoriza. La IP privada se utiliza dentro de la red interna de AWS. Al inicio esto generó algo de fricción, porque una parte importante del acceso dependía de entender qué dirección debía usarse y qué puerto debía estar abierto.

También reforcé la importancia de los grupos de seguridad. Si el puerto `22` no está permitido, la conexión por SSH falla. Si el puerto `80` no está abierto, el navegador no puede acceder al sitio web. En esta parte se nota que el despliegue requiere instalar Apache y permitir el tráfico correcto hacia la instancia.

## Implementación de la página web en Windows Server

El segundo objetivo consistió en crear una instancia Windows Server para desplegar un juego web. Para hacerlo regresé a EC2 y seleccioné nuevamente **Launch instance**. Nombré la instancia `ec2-windows-act1` y elegí una imagen de Windows Server. También seleccioné una instancia pequeña para mantener controlado el consumo del laboratorio.

**Figura 7**  
*Configuración inicial de la instancia Windows Server en EC2.*  
[Insertar captura aquí]

En esta instancia la configuración de acceso fue distinta porque el sistema operativo se administra principalmente mediante escritorio remoto. Durante la configuración habilité el tráfico HTTP y HTTPS, y también habilité RDP. El puerto de RDP es `3389`, y lo limité a mi IP para reducir riesgos de acceso externo.

Las reglas principales fueron las siguientes:

- **HTTP**, por el puerto `80`, abierto al público.
- **HTTPS**, por el puerto `443`, abierto al público.
- **RDP**, por el puerto `3389`, limitado a mi dirección IP.

Después de lanzar la instancia, AWS tardó alrededor de 10 a 15 minutos en dejarla completamente lista. Este tiempo de espera fue parte del proceso de inicialización de Windows Server.

Para conectarme, utilicé la opción de conexión por RDP desde la consola de EC2. Primero generé la contraseña de administrador usando el archivo `ec2-windows-act1.pem`. Después descargué el archivo `.rdp`, lo abrí con la aplicación de Escritorio remoto e ingresé con el usuario administrador y la contraseña generada por AWS.

**Figura 8**  
*Conexión por RDP a la instancia Windows Server.*  
[Insertar captura aquí]

Una vez dentro del servidor, instalé IIS, que es el servidor web de Windows. Lo hice desde la interfaz gráfica mediante **Server Manager**, siguiendo este flujo:

1. Abrir **Server Manager**.
2. Seleccionar **Add roles and features**.
3. Elegir **Role-based or feature-based installation**.
4. Seleccionar el servidor actual.
5. Marcar **Web Server (IIS)**.
6. Agregar las características solicitadas.
7. Avanzar con **Next** hasta llegar a **Install**.

**Figura 9**  
*Instalación del rol Web Server (IIS) en Windows Server.*  
[Insertar captura aquí]

También es posible instalar IIS desde PowerShell ejecutado como administrador:

```powershell
Install-WindowsFeature -Name Web-Server -IncludeManagementTools
```

Después descargué el juego de Breakout desde PowerShell y lo descomprimí en la carpeta de descargas del usuario:

```powershell
Invoke-WebRequest -Uri "https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/breakout.zip" -OutFile "$env:USERPROFILE\Downloads\breakout.zip"
Expand-Archive -LiteralPath "$env:USERPROFILE\Downloads\breakout.zip" -DestinationPath "$env:USERPROFILE\Downloads\breakout" -Force
```

Para que IIS pudiera servir el juego, copié los archivos al directorio público `wwwroot`:

```powershell
Copy-Item -Path "$env:USERPROFILE\Downloads\breakout\*" -Destination "C:\inetpub\wwwroot" -Recurse -Force
```

Después regresé a la consola de EC2, copié la IP pública de la instancia y validé el acceso desde el navegador:

```text
http://54.162.96.197/
```

**Figura 10**  
*Juego Breakout publicado desde IIS en la instancia Windows Server.*  
[Insertar captura aquí]

En esta parte el proceso fue más manual por el uso de la interfaz gráfica de Windows Server. Aunque PowerShell permite automatizar varias tareas, decidí usar la interfaz para revisar el flujo de instalación del rol de IIS y entender mejor dónde se configura cada elemento. La experiencia fue más visual, pero también tuvo más pasos que la instalación de Apache en Linux.

Este objetivo aumentó un poco la complejidad por el uso de RDP, la generación de contraseña y la instalación de IIS. Aun así, la lógica general fue parecida a la instancia Linux: crear el servidor, abrir los puertos necesarios, instalar el servicio web, copiar los archivos al directorio público y validar el acceso desde el navegador.

## Implementación de MySQL en Amazon RDS

El tercer objetivo fue crear una base de datos MySQL en Amazon RDS y conectarme a ella desde una herramienta externa. En mi caso utilicé MySQL Workbench para realizar la conexión y ejecutar pruebas.

Para iniciar, entré al servicio **Aurora and RDS** desde la consola de AWS y seleccioné la opción para crear una base de datos. AWS permite trabajar con distintos motores de bases de datos, pero para esta actividad seleccioné **MySQL**.

**Figura 11**  
*Selección del motor MySQL para la base de datos en Amazon RDS.*  
[Insertar captura aquí]

En la configuración utilicé la opción **Easy Create** para avanzar de forma más directa. Nombré la instancia `RDS-mysql-act1`, definí el usuario administrador como `admin` y generé una contraseña segura. También configuré la base de datos con una instancia pequeña y almacenamiento de 20 GB, suficiente para las pruebas de la actividad.

Al inicio no tenía visible la opción para crear la base de datos como pública. Después de revisar la configuración disponible, decidí crear el entorno y modificar después la conectividad. Una vez creada la instancia de RDS, entré a la opción **Modify**, busqué el apartado de conectividad y activé la opción **Publicly accessible**.

**Figura 12**  
*Configuración de acceso público en la instancia RDS.*  
[Insertar captura aquí]

Después revisé el grupo de seguridad asociado a la base de datos. Agregué una regla de entrada de tipo **MySQL/Aurora**, que utiliza el puerto `3306`, y limité el origen a mi IP. Esta configuración permite conectarme desde mi equipo local sin exponer el puerto a cualquier dirección.

La configuración de conexión usada en MySQL Workbench fue la siguiente:

- **Hostname:** endpoint de la instancia RDS.
- **Port:** `3306`.
- **Username:** usuario administrador de la base de datos.
- **Password:** contraseña configurada para RDS.

**Figura 13**  
*Conexión exitosa desde MySQL Workbench hacia Amazon RDS.*  
[Insertar captura aquí]

Para validar la conexión ejecuté primero una consulta para listar las bases de datos:

```sql
SHOW DATABASES;
```

Después creé una base de datos nueva:

```sql
CREATE DATABASE actividad1db;
```

Luego creé una tabla de prueba e inserté un registro:

```sql
USE actividad1db;

CREATE TABLE prueba (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO prueba (nombre) VALUES ('Miguel');

SELECT * FROM prueba;
```

**Figura 14**  
*Creación de la base de datos, tabla y registro de prueba en MySQL Workbench.*  
[Insertar captura aquí]

Para confirmar que los cambios estaban aplicados en la base de datos remota, regresé a la consola de AWS y utilicé CloudShell como otra forma de conexión. Desde ahí ingresé nuevamente con las credenciales de la base de datos y ejecuté consultas para validar que `actividad1db` existiera y que la tabla tuviera el registro insertado.

```sql
SHOW DATABASES;
USE actividad1db;
SELECT * FROM prueba;
```

**Figura 15**  
*Validación de la base de datos desde AWS CloudShell.*  
[Insertar captura aquí]

Este ejercicio fue útil para entender mejor la relación entre el endpoint de RDS, el puerto `3306`, el grupo de seguridad y la herramienta cliente. En mi caso, el principal punto de revisión fue asegurar que la base de datos estuviera marcada como públicamente accesible y que el grupo de seguridad permitiera conexiones desde mi IP.

# Conclusiones

Al finalizar la actividad se cumplieron los tres objetivos planteados. Se creó una instancia EC2 con Linux y se publicó una página web estilo Netflix mediante Apache. También se creó una instancia EC2 con Windows Server, se instaló IIS y se publicó un juego web. Finalmente, se creó una base de datos MySQL en Amazon RDS, se habilitó el acceso necesario y se realizaron pruebas desde MySQL Workbench y CloudShell.

El trabajo me ayudó a comprender mejor la importancia de los grupos de seguridad. En cada servicio, los problemas de conexión estuvieron relacionados con puertos, direcciones IP o permisos de acceso. Para Linux fue necesario abrir el puerto `22` para SSH y el puerto `80` para HTTP. Para Windows Server fue necesario habilitar el puerto `3389` para RDP. Para RDS fue indispensable permitir el puerto `3306` desde mi IP.

También pude distinguir con más claridad la función de cada servicio. EC2 se utilizó para ejecutar servidores web y publicar contenido. RDS se utilizó para administrar una base de datos relacional sin instalar manualmente MySQL en una máquina virtual. Esta separación ayuda a entender cómo se organizan los componentes de una arquitectura básica en la nube.

En general, AWS puede sentirse abrumador por la cantidad de opciones disponibles. Sin embargo, al enfocarme en un servicio y en un objetivo concreto, el proceso fue más fácil de digerir. La práctica con AWS Academy permitió trabajar con servicios reales, cometer errores controlados y corregir configuraciones hasta lograr que cada recurso funcionara correctamente.

# Referencias

[Pendiente de integrar en la segunda pasada.]
