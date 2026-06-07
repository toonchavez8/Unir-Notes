# 1. Portada

La portada puede incluir:

- Unir
- MODAM Administración de Sistemas, Virtualización, Cloud Computing y DevOps
- Actividad: Introducción a AWS. Consola AWS, Servicios EC2 y RDS
- Miguel de Jesus Chavez Barragan
- CARLOS MARTIN MARTINEZ FERRAEZ
- 06-08-2026

# 2. Introducción

Esta actividad se trata de probar y usar los servicios de aws atraves de AWS Acadamey. El processo de implmentacion y despliegue de una pagina en un Contenedor EC 2 en linux, el como implementar una pagina en un contenedor EC 2 version windows , y por ultimo usando RDS despliguar una Base de datos y hacer modificaciones a la base de datos. 

De esta manejera podriamos adquieri conocimiento de como usar EC2 y RDS. Pero EC2 que es? Ec 2 es donde corre las applicciones o paginas. Es un Servicio que te perminte crear servidores vertuales en AWS, EC 2 Signigica Elastic Compute Cloud. Termina siendo como una computadora en la nube que rentas. Y RDS es donde viven tus datos. RDS es un servicio administrado de bases de datos. Siginca que es Relational Database Services. Maneja bases de daots que son relacionales como MySQL PostgreSQL MariaDB para nombrar ualguno sin tener que instalar o administrar el servidor de dabese de datos manuelmante. 

Aprendemos atraves de la cursada y AWS Academy las bases y podemos aprovechando AWS Acadamey que nos da la herramienta con un servicio de 50 drls topado a 4 horas concurrentes activos de servicio para poder realizar la actividad y lograr nuestros objetivos.

# 3. Objetivos

Tomando en cuenta Nuesto objetivo general que es aplicar conocimientos básicos de nube pública mediante el uso de AWS Academy, EC2 y RDS podemos atterizar los 3 objetivos especificos que tenemos para realizar.

- crear una instancia Linux y desplieguar una pagina estilo Netflix
- Crear una instancia Windows y publicar un juego.
- Crear una base de datos en RDS de mysql conectarmente remotamente y realizar modificaciones. 

# 4. Desarrollo De la Actividad

Esos objetivos solo se pueden lograr una ves entrando a la plataforma de AWS Accadamy

## 4.1 Exploración De AWS Academy Y Consola

Aws Accadmy es un servicio dado pro Amazon para ayudar estudiantes de la nube como practicar en su entorno real sin precuparnos de riesgos de costos por temas de dinero y instancias ifnivitamente activas.

La plataforma cunado ingresas de da la bienvendida con muchas explaicion y aviso de conocominetos technicos para mostrate como mejor aprovechar la isntancia que esta por darte. Esta instancia se llama laboratiro. Para llegar a eso el sistema de motiva altamente que pases por su sistema de LMS

En el panel del LMS (**Learning Management System**, Sistema de administración de aprendizaje), elija el laboratorio de aprendizaje al que quiera acceder. Una ves que lo elignaas de va aparecer la opcioon de arrancar el labc **Start Lab (Comenzar laboratorio)**

Cuando el ícono del círculo en el lado derecho del enlace de AWS en la esquina superior izquierda aparece en verde, el entorno del laboratorio está listo para usarse.

Para iniciar la Consola de administración de AWS en una pestaña nueva, elija el enlace de **AWS**.

Se inicia sesión en la consola con una cuenta de AWS temporal que podrá usar durante el tiempo que el temporizador de la sesión del laboratorio esté activo.

El sistema guardará el trabajo cuando determine la sesión o caduque el temporizador de esta. El sistema tambien nos avisa del tiempo disponbile para usar el Laborotario activo y Su presupuesto de **50 USD** para la plataforma de AWS es suficiente para la mayoría de los proyectos académicos, siempre y cuando se mantenga dentro de las pautas del presupuesto.

Una ves ya dentro de la consoala principal de aws podemos valdiar Que es nuestrio REGION que fue us-east-1. Una region Una **Región de AWS** es una ubicación geográfica donde AWS tiene centros de datos.

Cada región contiene una o más **Zonas de Disponibilidad (Availability Zones)**.

Ejemplos de regiones;

- US East (N. Virginia) (`us-east-1`)
- US West (Oregon) (`us-west-2`)
- South America (São Paulo)

De ahi me fui explorando para validar que acceso tenemos a la nube en este caso valid 3 servicios VPS, ec 2 y rds. 

## 4.2 Implementación De la Web En Linux

Para logar nuesto primer objetivo de desplguear en un contenedor de linux nuestra pagina lo primero que hice fue regresar al panel de ec 2 y le di Launch instance.

Con esto me fui configurando la instancia de linux, primero la nombre `ec2-linux-act1` de ahi elije que fuera de Amazon Linux en version micro. Porque micro porque es la que no nos deberia de generar un costo por el uso y si si muy pequeño.

De ahi definmos que queriamos una llave o `key pair` la descargue y la nombre igual que la instancia para maryor seguridad y encotnrabilidad. Esto me entrego un archivo `.pem` de ahi le di launch instance. 

Se creo la instancia pero todavia me faltaba generar las reglas de segudiad para que me permitiera conectarme. Aqui entre a las opcioens de grupo de seguridad. Un gurpo de seguridad es como Aws define que tipos y niveles de acceso pueden tener ciertos conciones atraves de ips y puertos. Esto nos brinde seguridad porque nos facilitre limitar quien entra y quien saca information. 

Aplique 3 reglas. Reglas de ssh, https y de http. Ssh iba al puerto 22 mientras que https al 443 y por ultimo http al puerto 80. Sssh lo deje fijado a mi ip para mayo segureidad dado que con espo podria manejar y controlar desde la terminal. Y las otras dos las de de publcias porque la intencion es liberar es puertos para usarios pudieran ingresar a ver el contenido de la pagina.

Listo. Ya tenemos puertos abiertos para ssh pero que h acemos con eso. Puedes aws nos permite tener 3 formas de conectarnos al instancia. De la cual yo determine usando 2. 

Desde instance connect se puede

1. Haz clic en `Connect`.

2. Entra a la pestaña `EC2 Instance Connect`.

3. Haz clic en `Connect`.

Por mi terminal 

Use SSH a la url de la instanca con el siguente commando con la clave `.pem`. 

```Python
chmod 400 "ec2-linux-act1.pem"
ssh -i "ec2-linux-act1.pem" ec2-user@ec2-98-86-108-89.compute-1.amazonaws.com
```

Estando dentro de la terminal de la instancia ejcute los siguentes commandos 

```Python
sudo dnf install -y httpd wget unzip  
sudo systemctl enable httpd  
sudo systemctl start httpd
```

Consto lo que me permite es tener Apache instalado y ejecutandose para despliegar manualmente el zip de Netflix

Para eso corri los siguentes commandos

```bash
mkdir -p ~/sitio-netflix
cd ~/sitio-netflix
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip
unzip Netflix.zip
```

Verificamos que este funcioando el apache 

```bash
sudo systemctl status httpd
```

Despues los valid para ver que estaban bien descompremidos con ls y al validar que si lo copie todos los archivos a `var/www/html`

```Python
sudo cp -r ./* /var/www/html/
```

Y probamos el sitio regresando a la consola de nuestra instancia.

Copiamos el public IPv4 address de la instancia y nos dio respuesta en mi navegador

```Python
http://98.86.108.89/
```

- cómo creaste la instancia,
- qué sistema operativo elegiste,
- qué puertos abriste,
- cómo te conectaste,
- cómo instalaste Apache o Nginx,
- cómo publicaste la web.

Con esto lo que me queda claro es que existe una gran diferencia entre ip public y la ip prvidada que te otroga aws, y es que la ip publica con los permismos de seguridad correctamente implementados de va permetir ingresar desde donde sea pero la ip privada no. La ip previdada solo dentrro de la red de aws y eso genero un poco de fricion al iniciar con este objetivo. 

Y r ealmente mucho tiene que ver con la configuracion que hicimos con el grupo de seguridad. Dado que fu nciona como un firewal virtual de la instancia, esta se encarga de proteger si los puertos no estan autorizados para recibir el trafcio. Por eso para conectarnos remotamente via ssh abrimos el puerto 22 y para tener acceso a ver la pagina via http o https abrimos el peurto 80/443 que por lo general suelen set Standardization. Los misos configuraciones de acceso me funcionaron en su mayoria para el siguente objetivo.

## 4.3 Implementación De la Web En Windows

Debes explicar:

- cómo creaste la instancia,
- cómo obtuviste la contraseña,
- cómo te conectaste por RDP,
- cómo instalaste IIS,
- cómo copiaste la web a `wwwroot`.
El Objetivo de implementacion en una instancia web cambia bastante. Para despliegar un juego de ladrios nuevamente iniciamos el processo de launch instance. Esta instancia la nombraos ec 2-windows-act 1 y escogimos la imagen de windows server y para evitar costos tambien nos fuimos por una instancia pequeno.

Aqui a diferencia de la instancia de linux no entramos directamente desde los grupos de seguridad sino en la misma ventana de cconfigucacion activamos los 3 checkboxes que de manera effectiva logra lo mismo. Vamos abrir el trafico de puerto 443 via https y http via el puerto 80 con origin de cualquier lugar y la diferencia grande aqui es que vamos acccepar el RDP que remote desktop via mi ip unicamente para especificar y limitar el acceso.

Al lanzar tardamos mas para ingresar pero despues deunis 10 - 15 minutos ya quedo status acctivo nuestra instancia. 

Para conectarnos al set un windows server podemo sentrar por session o RDP o una consola, yo opte por RDP. De aqui genere mi contrana desde mi `ec2-windows-act1.pem` file que nos da la clave para ingresar. Desde la pagina de acceso podemos descargar un archjivo .rdp que nos va abrir el remote desktop app. 

Al iniciar la session con nuestro usario que definimos mondamos la contrana que nos brindo aws. Y con eso estamos en una maquina virtual de window sservers.

Al istar dentro tenemos dos formars de instalr el IIS que es el windows web server, lo podemos hacer desde el server manager. Para eso segui estas instructones

1. Abre `Server Manager`.
2. Haz clic en `Add roles and features`.
3. Elige `Role-based or feature-based installation`.
4. Selecciona el servidor actual.
5. Marca `Web Server (IIS)`.
6. Haz clic en `Add Features`.
7. Continúa con `Next` hasta llegar a `Install`.

Tambien se pudo haber realizdo la instalaccion del windows server usadno el siguente commando de PowerShell

```bash
Install-WindowsFeature -Name Web-Server -IncludeManagementTools
```

Pero solo corriendo powhersell como admin

Despues aprovechando powhersell abierto podemos importar el juego de breakout

```bash
Invoke-WebRequest -Uri "https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/breakout.zip" -OutFile "$env:USERPROFILE\Downloads\breakout.zip"
Expand-Archive -LiteralPath "$env:USERPROFILE\Downloads\breakout.zip" -DestinationPath "$env:USERPROFILE\Downloads\breakout" -Force

```

Esto lo que va hacer es descargar nuestro comprimido de breakout y luego descomprimirlo y meterlo dentro neustra carpeta descargas

Y luego debemos de meter el resultado de nuestra carpeta de donde la va servir nuestro servidor mediande el commando de copiar de la terminarl 

```Python
```

Con esto luego nos podemos regresar a nuesto ec 2 para sacar la ip de nuestra instancia publica que en este caso nos arrojo http://54.162.96.197/ y podemos revisar que estaria arriba nuestra pagina.

 En este caso via windows me fui por actuar mas manual algunas cosas dado a la alta predominio de la interfas grafica que tiene para ver el flujo. Y en su mayoria puedo decir que es mas sensillo el proceso de por linea de commandos. 

Varacias veces tuve que validar la documentacion de windows para validar que el processo que estaba siguendo era correcto dado a la multiples opciones que tenemos gracias a la ampliabilidad que tiene el window server. 

Este objetivo incremento en complejidad por usar la interfas grafica pero la siguente la falta de hizo que fuera la mas senscilla.

## 4.4 Implementación De MySQL En AWS RDS

Debes explicar:

- cómo creaste la base de datos,
- qué motor seleccionaste,
- si el acceso fue público o privado,
- cómo configuraste seguridad,
- cómo te conectaste desde HeidiSQL,
- qué prueba realizaste para confirmar que funciona.

Por ultimo nuestor ultimo objetivo es crear un base de datos mysql en aws rds y connectartno mediante una herramienta externna, para esta yo elijge conectarme a traves de MySQL workbench.

Para realizar la implementacion de una base de datos de mysql la estategia era atraves de Aurora and RDS dde ahi selecione la opcion de crear con configucacion completa. AWS nos permite trabajar con varios tipos de motroes de base de datos pero nosotros selecionamos mysql

Venian dos opciones de configuracion y me fui por Easy Create para realizar along mas rapido lo cual nos permitio avansar mas rapido. Nombramos la instancia como RDS-mysql-act 1 y usamos admin de nombre del usaruario. Cree una contrasena segura y la registre en la aws. 

Aqui intente porque no tenia la opcion de registrar la base de dato como publica pero al final despues de leer la documentacion me di cuenta que podriamos registarlo despues. Por end determine el processo de creacion de nuestro entrono de RDS en una db micro con 20 gb.

Para hacer que la base de datos de RDS fuera accessible publciacment para poder integrarlo con mysql workbench ingrese a la la isntancia y me fui a la opcion de modificar.

En modificar buscque la opcioon de conectividad y entoncre la opcion de accesso publiclo y le active que sea de publicly accessible. Con esto guarde y valid que cual fue mi modificacion. Despues fui nuevamente a terabjar con el grupo de seguridad para confirmar los niveles de acceso tenia esta instancia.

Selecione el gurpo de al ir a editar creamos una nueva regla que fuera de tipo mysql/aurora con la intencion de abrir el puerto 3306 y habilite que mi ip para mayor seguirdad que tuviera acesso. Valid que tipo de trafico y de ahi me fui a revisar las endpoints y que en seguridad ya estaba como publicamente accessible. 

Use ese endpoint que nos dio como el host name el puerto 

- **Hostname**: Your RDS endpoint
- **Port**: 3306 (or your custom port)
- **Username**: Your database username
- **Password**: Your database password
Con eso realize la coneccion y funciono

Desde MySQL workbench empeze a realizar purebas. 

```sql
SHOW DATABASES;
```

Primero para ver que bases de datos tenia luego crea otra nueva 

```sql
CREATE DATABASE actividad1db;
```

Y luego probar una tabla:

```sql
USE actividad1db;

CREATE TABLE prueba (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO prueba (nombre) VALUES ('Miguel');

SELECT * FROM prueba;
```

Y como vi que se crear quise valdiar que se estaban haciendo los cambiso directamente denrtro de aws entocnes para esto me regrese a la consola y en la consola active el cloudshell que es otra de las 3 opciones que nos da aws para conecarnaros. 

De ahi corriendo la terminarl ingrese mi cotnraena y me dio acceso nuevament confirmado que funciona. Al ingresar el mismo commando que pusimos anteirormente de Show Databases, nos muestra la nueva base dead datos llamada `actividad1db` que creamos localmente. Y al revisar la tabla que creamos podemos ver con exito nuestra entrada dentro de la paltgaforma de aws, dandondes certeza de que esta correctamente integrado. 

## 6. Conclusiones

Al terminar podemos decir que correctamente completamos los objetivos. Termiamos con dos instancias de ec2, una de linux con una pagina web de netflix montada, y otra de windows que fue un processo mas manual pero que tenemos una pagina de un juego. Por otro lado de RDS tenemos una base de datos con salida publica a una ip configurdada correctamente que localmente en mi maquina pude modificar. 

En general en todas neustras instancias pudimos abrirar puertos 22 para coenxcion remotas de ssh y para el instance connect. El puerto 80 para recibir peticiones mediante http y en la isntancia windows se abrio el puerto 3389 para conecion de escritorio remoto. En pueto 443 para salidas https que realmente no fue indepensable y por ultimo un puerto para mysql.

En proyectos pasados el trabjo de grupo de seguriadad se me habia complicado mucho pero con el repaso y leyendo la documentacion tiempo logre comprendolo mas y como es un control de trafico de entrada y salida. Cada cuando me tope con una falla de conexcion siempre era que no habia correctamente liberado o activado el puerto para que fuera de aws recibiera la conecion. 

En mi caso para RDS que me quise conectar mas de una red publica para aws conectar atraves de los endpoints que liberan aws no fue mayor tema de como menscione validar que tuvieramos el grupo adecuado y fue rapido el prceso de modifcarlo dentro de mysql workbench. 

En general senti que es muy abrumador todas las opcioens que nos permite aws de usar pero una ves que te enfoques en una sola es muchismo mas facil digerir el desplgie y awmaon con todos sus herramientes falito mucho los deplieges.

# 7. Referencias

Aquí colocas las fuentes que consultaste, en formato APA.
