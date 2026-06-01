# Guía Paso a Paso Para Realizar la Actividad

Este documento no es el informe final. Su objetivo es servir como una guía práctica, clara y sencilla para completar cada tarea de la actividad en AWS y, al final, ayudarte a organizar tu informe con un estilo académico simple basado en APA.

## 1. Antes De Comenzar

Antes de crear recursos en AWS, conviene preparar lo siguiente:

- Tener acceso a AWS Academy con el correo institucional.
- Entrar al laboratorio asignado y confirmar que esté activo.
- Usar siempre la misma región en AWS para no perder de vista los recursos creados.
- Tener una libreta o archivo donde anotes nombres, IP públicas, endpoint de base de datos, usuarios y contraseñas.
- Guardar capturas de pantalla de cada parte importante.

### Recomendaciones Básicas

- Usa nombres claros para cada recurso. Por ejemplo: `ec2-linux-act1`, `ec2-windows-act1` y `rds-mysql-act1`.
- No abras puertos innecesarios.
- Si el laboratorio tiene límites, elige tamaños pequeños o tipo `micro`.
- Cuando termines de trabajar, detén o elimina los recursos si el laboratorio lo permite.

## 2. Tarea 1: Explorar AWS Academy Y la Consola De AWS

### Objetivo

Conocer el entorno de AWS Academy, iniciar el laboratorio y ubicar los servicios principales que was a usar: EC2, RDS, VPC y grupos de seguridad.

### Paso a Paso

#### Paso 1. Entrar a AWS Academy

1. Abre AWS Academy desde tu navegador.
2. Inicia sesión con tu cuenta institucional.
3. Entra al curso o laboratorio donde se encuentra la actividad.

#### Paso 2. Iniciar El Laboratorio

1. Busca el botón para iniciar el laboratorio.
2. Espera a que cambie el estado a activo.
3. Cuando el laboratorio esté listo, abre la consola de AWS.

#### Paso 3. Reconocer la Consola

Una vez dentro de la consola:

1. Revisa la región que aparece en la parte superior derecha.
2. Escribe `EC2` en el buscador de servicios y entra.
3. Luego busca `RDS` y entra.
4. Observa también el servicio `VPC`, porque ahí se manejan redes, subredes, IPs y grupos de seguridad.

### Qué Debes Identificar En Esta Parte

- Qué es una región.
- Qué es una instancia EC2.
- Qué es un grupo de seguridad.
- Qué es una IP pública y una IP privada.
- Qué es una base de datos administrada en RDS.

### Evidencia Que Te Conviene Guardar

- Captura del laboratorio activo.
- Captura de la consola principal de AWS.
- Captura de la región seleccionada.
- Captura del panel de EC2.
- Captura del panel de RDS.

## 3. Tarea 2: Crear Una Web En Una Instancia EC2 Linux

### Objetivo

Crear una máquina virtual Linux en EC2, conectarte a ella, instalar un servidor web y publicar una página estática.

### Configuración Sugerida

| Elemento | Valor sugerido |
|---|---|
| Nombre de la instancia | `ec2-linux-act1` |
| Imagen | Amazon Linux |
| Tipo de instancia | Una opción `micro` disponible en el laboratorio |
| Acceso | EC2 Instance Connect o clave `.pem` |
| Puerto de administración | SSH `22` |
| Puerto web | HTTP `80` |
| Puerto opcional | HTTPS `443` |

### Paso 1. Abrir EC2

1. En la consola de AWS, busca `EC2`.
2. Entra al panel de EC2.
3. Haz clic en `Launch instance`.

### Paso 2. Configurar la Instancia Linux

1. En `Name`, escribe `ec2-linux-act1`.
2. En `Application and OS Images`, elige una imagen de Amazon Linux marcada como opción gratuita o de laboratorio.
3. En `Instance type`, selecciona una instancia pequeña, de preferencia `micro`.
4. En `Key pair`, crea una nueva clave si el laboratorio lo permite o usa una existente.
5. Descarga y guarda el archivo `.pem` en un lugar seguro.

### Paso 3. Configurar Seguridad

En el grupo de seguridad agrega estas reglas de entrada:

- SSH, puerto `22`, origen `My IP` para conectarte desde tu equipo.
- HTTP, puerto `80`, origen `Anywhere` para que la web se vea desde el navegador.

Si el laboratorio te lo permite, también puedes agregar:

- HTTPS, puerto `443`, origen `Anywhere`.

### Paso 4. Lanzar la Instancia

1. Revisa el resumen.
2. Haz clic en `Launch instance`.
3. Espera a que la instancia quede en estado `Running`.
4. Confirma que pase los `Status checks`.

### Paso 5. Conectarte a la Instancia

La forma más simple para un principiante es usar `EC2 Instance Connect` si está disponible.

1. Selecciona la instancia.
2. Haz clic en `Connect`.
3. Entra a la pestaña `EC2 Instance Connect`.
4. Haz clic en `Connect`.

Si no está disponible, usa SSH con la clave `.pem`.

### Paso 6. Instalar Apache

Ya dentro de la terminal de la instancia, ejecuta:

```bash
sudo dnf install -y httpd wget unzip
sudo systemctl enable httpd
sudo systemctl start httpd
```

Si tu imagen usa `yum` en lugar de `dnf`, puedes ejecutar los mismos commandos cambiando `dnf` por `yum`.

### Paso 7. Descargar la Web Estática

Usaremos el archivo sugerido por la actividad:

```bash
mkdir -p ~/sitio-netflix
cd ~/sitio-netflix
wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/Netflix.zip
unzip Netflix.zip
```

### Paso 8. Copiar Los Archivos Al Servidor Web

```bash
sudo cp -r ./* /var/www/html/
```

Si te pregunta por reemplazar archivos, confirma. Si quieres dejar todo limpio antes de copiar, primero revisa qué archivos ya existen en `/var/www/html/`.

### Paso 9. Probar El Sitio

1. Vuelve a la consola de EC2.
2. Copia la `Public IPv4 address` de la instancia.
3. Abre en tu navegador:

```text
http://TU-IP-PUBLICA
```

Si todo salió bien, verás la página cargada.

### Qué Revisar Si no Funciona

- Que la instancia siga en estado `Running`.
- Que el grupo de seguridad tenga abierto el puerto `80`.
- Que Apache esté activo.
- Que la IP pública sea la correcta.

Para verificar Apache:

```bash
sudo systemctl status httpd
```

### Evidencia Que Te Conviene Guardar

- Captura de la configuración de la instancia.
- Captura del grupo de seguridad.
- Captura de la conexión por terminal.
- Captura de los commandos ejecutados.
- Captura del sitio web abierto en el navegador.

## 4. Tarea 3: Crear Una Web En Una Instancia EC2 Windows

### Objetivo

Crear una máquina virtual con Windows en EC2, conectarte por RDP, instalar IIS y publicar una página estática.

### Configuración Sugerida

| Elemento | Valor sugerido |
|---|---|
| Nombre de la instancia | `ec2-windows-act1` |
| Imagen | Windows Server |
| Tipo de instancia | Una opción `micro` disponible en el laboratorio |
| Acceso remoto | RDP |
| Puerto de administración | RDP `3389` |
| Puerto web | HTTP `80` |

### Paso 1. Crear la Instancia Windows

1. En EC2, haz clic en `Launch instance`.
2. En `Name`, escribe `ec2-windows-act1`.
3. Elige una imagen de `Windows Server`.
4. Selecciona una instancia pequeña, de preferencia `micro`.
5. Usa una clave existente o crea una nueva.

### Paso 2. Configurar Seguridad

Agrega estas reglas de entrada:

- RDP, puerto `3389`, origen `My IP`.
- HTTP, puerto `80`, origen `Anywhere`.

### Paso 3. Lanzar la Instancia

1. Haz clic en `Launch instance`.
2. Espera a que quede en `Running`.
3. Espera también a que pase las verificaciones de estado.

En Windows esto puede tardar más que en Linux.

### Paso 4. Obtener la Contraseña De Windows

1. Selecciona la instancia.
2. Haz clic en `Connect`.
3. Entra a la pestaña `RDP client`.
4. Haz clic en `Get password`.
5. Sube el archivo `.pem` que usaste al crear la instancia.
6. Descifra la contraseña y guárdala.
7. Descarga el archivo `.rdp`.

Si la contraseña todavía no aparece, espera unos minutos más. En instancias Windows es normal que el proceso tarde un poco.

### Paso 5. Conectarte Por Escritorio Remoto

1. Abre el archivo `.rdp`.
2. Acepta la conexión.
3. Inicia sesión con el usuario `Administrator` o el nombre equivalente que indique la consola.
4. Escribe la contraseña descifrada.

### Paso 6. Instalar IIS

Tienes dos caminos. Para un principiante, el más claro es usar la interfaz gráfica.

#### Opción A. Instalar IIS Desde Server Manager

1. Abre `Server Manager`.
2. Haz clic en `Add roles and features`.
3. Elige `Role-based or feature-based installation`.
4. Selecciona el servidor actual.
5. Marca `Web Server (IIS)`.
6. Haz clic en `Add Features`.
7. Continúa con `Next` hasta llegar a `Install`.
8. Espera a que determine la instalación.

#### Opción B. Instalar IIS Con PowerShell

Abre PowerShell como administrador y ejecuta:

```powershell
Install-WindowsFeature -Name Web-Server -IncludeManagementTools
```

### Paso 7. Descargar la Página Web

Puedes hacerlo desde el navegador del servidor o con PowerShell. La opción con PowerShell suele set más rápida:

```powershell
Invoke-WebRequest -Uri "https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/breakout.zip" -OutFile "$env:USERPROFILE\Downloads\breakout.zip"
Expand-Archive -LiteralPath "$env:USERPROFILE\Downloads\breakout.zip" -DestinationPath "$env:USERPROFILE\Downloads\breakout" -Force
```

### Paso 8. Copiar Los Archivos Al Sitio De IIS

La carpeta por defecto del sitio web es:

```text
C:\inetpub\wwwroot
```

Puedes copiar los archivos extraídos de `breakout` a esa carpeta. Si ya existen archivos por defecto de IIS, puedes reemplazarlos.

### Paso 9. Probar El Sitio

1. Regresa a la consola de EC2.
2. Copia la IP pública de la instancia.
3. Abre en tu navegador:

```text
http://TU-IP-PUBLICA
```

Si todo salió bien, aparecerá la página publicada desde IIS.

### Qué Revisar Si no Funciona

- Que el puerto `80` esté abierto en el grupo de seguridad.
- Que IIS haya quedado instalado.
- Que los archivos estén dentro de `C:\inetpub\wwwroot`.
- Que la instancia tenga IP pública.

### Evidencia Que Te Conviene Guardar

- Captura de la instancia Windows.
- Captura del grupo de seguridad.
- Captura de la ventana `Get password`.
- Captura de la conexión por RDP.
- Captura de IIS instalado.
- Captura del sitio funcionando en el navegador.

## 5. Tarea 4: Crear MySQL En AWS RDS

### Objetivo

Crear una base de datos MySQL en Amazon RDS y conectarte a ella con una herramienta como HeidiSQL.

### Idea Importante Antes De Empezar

En esta parte debes decidir cómo te was a conectar:

- Si te conectarás desde tu computadora con HeidiSQL, la base de datos debe tener acceso público y el puerto `3306` debe estar permitido desde tu IP.
- Si te conectarás desde una instancia EC2 dentro de AWS, la base de datos puede quedar privada.

Para un principiante, la opción más simple es crearla con acceso público y restringir el acceso solo a tu IP.

### Configuración Sugerida

| Elemento | Valor sugerido |
|---|---|
| Nombre de la base de datos | `rds-mysql-act1` |
| Motor | MySQL |
| Plantilla | Free tier o la más pequeña disponible en el laboratorio |
| Clase | Una clase `micro` disponible |
| Almacenamiento | 20 GB |
| Puerto | `3306` |
| Acceso público | `Yes` si usarás HeidiSQL desde tu PC |

### Paso 1. Entrar a RDS

1. En la consola de AWS, busca `RDS`.
2. Entra al panel de Amazon RDS.
3. Haz clic en `Create database`.

### Paso 2. Elegir El Tipo De Creación

Si quieres entender mejor las opciones, usa `Standard create`. Si quieres algo más rápido, puedes usar `Easy create`.

Para aprender más y cumplir mejor con la actividad, conviene `Standard create`.

### Paso 3. Configurar El Motor Y la Plantilla

1. En `Engine type`, selecciona `MySQL`.
2. En `Templates`, elige `Free tier` o la opción pequeña que permita el laboratorio.

### Paso 4. Configurar Identificador Y Credenciales

1. En `DB instance identifier`, escribe `rds-mysql-act1`.
2. En `Master username`, escribe un usuario como `admin`.
3. Crea una contraseña segura y anótala.

### Paso 5. Configurar Tamaño Y Almacenamiento

1. Elige una clase pequeña, por ejemplo una clase `micro` disponible.
2. Deja un almacenamiento pequeño, por ejemplo `20 GB`.
3. Si el laboratorio tiene restricciones, respeta los valores disponibles.

### Paso 6. Configurar Conectividad

1. En `Connectivity`, elige la VPC por defecto o la VPC del laboratorio.
2. En `Public access`, elige `Yes` si usarás HeidiSQL desde tu computadora.
3. Crea o selecciona un grupo de seguridad.
4. Verifica que el puerto de la base de datos sea `3306`.

### Paso 7. Configuración Adicional

1. Si aparece la opción `Initial database name`, escribe algo como `actividad1db`.
2. Para esta práctica, no es necesario activar opciones avanzadas si el laboratorio no lo pide.
3. Si el laboratorio lo permite y quieres mostrar más dominio, revisa la opción de despliegue en varias zonas, pero no es obligatoria para la parte básica.

### Paso 8. Crear la Base De Datos

1. Haz clic en `Create database`.
2. Espera a que el estado cambie a `Available`.

### Paso 9. Ajustar El Grupo De Seguridad

Si was a conectarte desde HeidiSQL en tu PC:

1. Abre el grupo de seguridad de la base de datos.
2. Agrega una regla de entrada:
   - Tipo: `MySQL/Aurora`
   - Puerto: `3306`
   - Origen: `My IP`

Esto es importante. No conviene dejar el puerto abierto para todo internet.

### Paso 10. Obtener El Endpoint

Cuando la base de datos esté disponible:

1. Entra al detalle de la instancia RDS.
2. Copia el `Endpoint`.
3. Confirma el puerto `3306`.

### Paso 11. Conectarte Con HeidiSQL

En HeidiSQL crea una nueva sesión con estos datos:

- `Hostname / IP`: el endpoint de RDS.
- `User`: el usuario maestro que creaste.
- `Password`: la contraseña configurada.
- `Port`: `3306`.

Luego prueba la conexión.

### Paso 12. Hacer Una Prueba Simple

Si la conexión funciona, ejecuta algo básico como:

```sql
SHOW DATABASES;
```

Si no creaste una base inicial, puedes crear una:

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

### Qué Revisar Si no Funciona

- Que la base de datos esté en estado `Available`.
- Que el `Endpoint` sea correcto.
- Que el puerto `3306` esté permitido.
- Que hayas usado el usuario y contraseña correctos.
- Que `Public access` esté activado si te conectas desde tu equipo.

### Evidencia Que Te Conviene Guardar

- Captura de la configuración general de RDS.
- Captura del grupo de seguridad con el puerto `3306`.
- Captura del endpoint.
- Captura de HeidiSQL conectado.
- Captura de una consulta ejecutada con éxito.

## 6. Cómo Subir El Nivel Según la Rúbrica

Si quieres acercarte a la puntuación más alta, no basta con crear recursos. También debes demostrar que entiendes lo siguiente:

### En EC2

- Diferencia entre IP pública e IP privada.
- Qué hace un grupo de seguridad.
- Qué puertos abriste y por qué.
- Qué almacenamiento usa la instancia.
- Cómo conectarte a Linux y Windows.

### En RDS

- Diferencia entre acceso público y acceso privado.
- Qué significa conectarte desde una red pública.
- Qué significa conectarte desde una red privada.
- Qué es alta disponibilidad o despliegue Multi-AZ.

### Explicación Simple

- `Pública`: te conectas desde fuera de AWS, por ejemplo desde tu laptop con HeidiSQL.
- `Privada`: te conectas desde una instancia EC2 dentro de la misma VPC.
- `Alta disponibilidad`: la base de datos tiene una réplica o infraestructura distribuida para reducir fallos, si el servicio y el laboratorio lo permiten.

## 7. Guía Simple Para Redactar Tu Informe En Formato APA

Esta parte no es el informe final, sino una guía para que sepas cómo debería verse.

### Regla Importante

La actividad pide `Calibri 11` e `interlineado 1.5`. Aunque APA 7 suele usar otras convenciones de espaciado, aquí conviene seguir lo que pide la actividad y aplicar APA sobre todo en:

- redacción formal,
- citas dentro del texto,
- referencias finales,
- títulos claros,
- presentación ordenada de figuras y tablas.

### Formato General Sugerido

| Elemento | Recomendación |
|---|---|
| Fuente | Calibri 11 |
| Interlineado | 1.5 |
| Márgenes | 2.54 cm en todos los lados |
| Alineación | Texto alineado a la izquierda |
| Numeración | Número de página en encabezado o pie |
| Lenguaje | Formal, claro y sin expresiones coloquiales |

### Estructura Recomendada Del Informe

#### 1. Portada

La portada puede incluir:

- Universidad.
- Asignatura.
- Título de la actividad.
- Nombre del estudiante: Miguel Chavez.
- Nombre del docente.
- Fecha de entrega.

#### 2. Introducción

Aquí explicas, en uno o dos párrafos:

- de qué trata la actividad,
- qué servicios de AWS se usarán,
- por qué es importante conocer EC2 y RDS.

#### 3. Objetivos

Puedes separar:

- objetivo general,
- objetivos específicos.

Ejemplo simple:

- Objetivo general: aplicar conocimientos básicos de nube pública mediante el uso de AWS Academy, EC2 y RDS.
- Objetivos específicos: crear una instancia Linux, crear una instancia Windows, publicar dos páginas web y desplegar una base de datos MySQL en RDS.

#### 4. Desarrollo De la Actividad

Esta será la parte más grande del informe. Conviene dividirla por tareas.

##### 4.1 Exploración De AWS Academy Y Consola

Debes explicar:

- cómo entraste al laboratorio,
- cómo abriste la consola,
- qué servicios identificaste,
- qué región usaste.

##### 4.2 Implementación De la Web En Linux

Debes explicar:

- cómo creaste la instancia,
- qué sistema operativo elegiste,
- qué puertos abriste,
- cómo te conectaste,
- cómo instalaste Apache o Nginx,
- cómo publicaste la web.

##### 4.3 Implementación De la Web En Windows

Debes explicar:

- cómo creaste la instancia,
- cómo obtuviste la contraseña,
- cómo te conectaste por RDP,
- cómo instalaste IIS,
- cómo copiaste la web a `wwwroot`.

##### 4.4 Implementación De MySQL En AWS RDS

Debes explicar:

- cómo creaste la base de datos,
- qué motor seleccionaste,
- si el acceso fue público o privado,
- cómo configuraste seguridad,
- cómo te conectaste desde HeidiSQL,
- qué prueba realizaste para confirmar que funciona.

#### 5. Resultados

Aquí resume qué lograste:

- instancia Linux funcionando,
- instancia Windows funcionando,
- sitio web Linux publicado,
- sitio web Windows publicado,
- base de datos MySQL creada y accessible.

#### 6. Conclusiones

Redacta dos o tres párrafos sobre:

- qué aprendiste,
- qué dificultades encontraste,
- por qué AWS facilita el despliegue de infraestructura y servicios.

#### 7. Referencias

Aquí colocas las fuentes que consultaste, en formato APA.

#### 8. Anexos

Puedes poner:

- capturas de pantalla,
- commandos usados,
- datos técnicos adicionales.

## 8. Modelo Simple De Cómo Puede Verse Tu Informe

Puedes usar esta estructura como base:

```text
Portada

Introducción

Objetivos
Objetivo general
Objetivos específicos

Desarrollo de la actividad
4.1 Exploración de AWS Academy y consola
4.2 Implementación de la web en Linux
4.3 Implementación de la web en Windows
4.4 Implementación de MySQL en AWS RDS

Resultados

Conclusiones

Referencias

Anexos
```

## 9. Recomendaciones De Redacción

Para que el informe se vea más académico:

- Usa oraciones claras y directas.
- Evita frases como `estuvo fácil`, `me salió mal`, `se veía padre`.
- Prefiere frases como `se configuró`, `se implementó`, `se verificó`, `se observó`.
- Explica cada captura con una o dos líneas.
- No pegues imágenes sin contexto.

### Ejemplos De Redacción Simple

En lugar de escribir:

`Entré a AWS y moví varias cosas hasta que apareció la máquina.`

Conviene escribir:

`Se ingresó a la consola de AWS y se creó una instancia EC2 con sistema operativo Linux para alojar una página web estática.`

En lugar de escribir:

`La base jaló bien en HeidiSQL.`

Conviene escribir:

`La conexión a la base de datos MySQL en Amazon RDS se verificó correctamente mediante HeidiSQL.`

## 10. Cómo Citar En Formato APA De Manera Simple

### Cita Narrativa

Ejemplo:

`Amazon Web Services (s. f.) indica que una instancia EC2 puede lanzarse desde la consola de administración.`

### Cita Parentética

Ejemplo:

`La conexión a instancias Linux puede realizarse mediante EC2 Instance Connect (Amazon Web Services, s. f.).`

## 11. Ejemplos Simples De Referencias APA

Puedes usar modelos como estos y luego ajustarlos con la información final que realmente hayas consultado:

- Amazon Web Services. (s. f.). *Introducción a Amazon EC2*. AWS Documentation. https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/EC2_GetStarted.html
- Amazon Web Services. (s. f.). *Conectarse a la instancia de Linux con EC2 Instance Connect*. AWS Documentation. https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html
- Amazon Web Services. (s. f.). *Conexión a la instancia de Windows mediante un cliente RDP*. AWS Documentation. https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/connect-rdp.html
- Amazon Web Services. (s. f.). *Creación de una instancia de base de datos MySQL y conexión a ella*. AWS Documentation. https://docs.aws.amazon.com/es_es/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html
- Microsoft. (s. f.). *Installing the Web Server Role*. Microsoft Learn. https://learn.microsoft.com/en-us/iis/web-hosting/web-server-for-shared-hosting/installing-the-web-server-role

## 12. Lista Final De Comprobación

Antes de empezar tu informe final, revisa esto:

- Ya entré a AWS Academy y al laboratorio.
- Ya identifiqué la región correcta.
- Ya creé la instancia Linux.
- Ya publiqué la web en Linux.
- Ya creé la instancia Windows.
- Ya publiqué la web en Windows con IIS.
- Ya creé la base de datos MySQL en RDS.
- Ya probé la conexión a la base de datos.
- Ya guardé capturas de cada paso importante.
- Ya tengo datos suficientes para redactar el informe final.

## 13. Cierre

Si sigues esta guía en orden, tendrás todos los elementos necesarios para completar la actividad y luego redactar un informe más sólido. Lo ideal es hacer primero la práctica completa, guardar evidencia y después escribir el informe con calma.
