# Despliegue De Un Aplicativo En Alta Disponibilidad En AWS Academy

## 1. Para Qué Sirve Esta Guía

Esta guía explica cómo desplegar una aplicación web en alta disponibilidad dentro de AWS Academy. La propuesta usa WordPress, EC2, un Application Load Balancer, un Auto Scaling Group y una base de datos RDS MySQL en subredes privadas.

La idea no es solo "seguir clics" en la consola. También se explica por qué se crea cada recurso, qué problema resuelve y qué evidencia conviene guardar para el PDF final de la actividad.

La arquitectura cubre los puntos principales del enunciado `mexissi06_act2_grupal.md`:

- Una VPC con direccionamiento privado.
- Seis subredes distribuidas en dos zonas de disponibilidad.
- Subredes públicas con salida a Internet por Internet Gateway.
- Subredes privadas con salida a Internet por NAT Gateway.
- Frontend en EC2 privadas, sin IP pública.
- Publicación del frontend por medio de un Application Load Balancer.
- Auto Scaling Group para mantener dos instancias del frontend.
- Base de datos RDS en subredes privadas separadas de las subredes del frontend.
- Alta disponibilidad en la base de datos mediante Multi-AZ, si AWS Academy lo permite.

## 2. Decisión De Aplicación

Para esta práctica recomiendo usar WordPress sobre EC2 y RDS MySQL.

Se podría usar Moodle, MediaWiki, Laravel o Django, pero WordPress reduce el riesgo. Se instala rápido, usa base de datos relacional y permite comprobar desde el navegador que el balanceador, las EC2 y RDS están funcionando.

| Opción | Aplicación | Base de datos | Riesgo para terminar en 4 horas | Comentario |
|---|---|---|---|---|
| 1 | WordPress | MySQL o MariaDB | Bajo | Es la opción recomendada para esta actividad. |
| 2 | MediaWiki | MySQL o MariaDB | Medio | Sirve para una demo de wiki, pero tarda más en dejarse lista. |
| 3 | Moodle | MySQL o PostgreSQL | Medio | Encaja con un contexto educativo, pero la instalación puede consumir mucho tiempo. |
| 4 | Laravel demo app | MySQL o PostgreSQL | Medio | Buena opción si el equipo ya tiene una app preparada. |
| 5 | Django demo app | PostgreSQL o MySQL | Medio | Require preparar proyecto, dependencias y variables de entorno. |

Para el informe, lo importante no es que WordPress sea una aplicación compleja. Lo importante es que permite demostrar la arquitectura: entrada por ALB, procesamiento en EC2 privadas, persistencia en RDS y recuperación ante fallo de una instancia.

## 3. Arquitectura Propuesta

### 3.1 Resumen De la Arquitectura

La arquitectura tiene tres zonas lógicas.

La primera zona es pública. Ahí estarán el Application Load Balancer, el Internet Gateway y los NAT Gateway. "Pública" no significa que todo reciba tráfico libremente; significa que esas subredes tienen ruta directa hacia Internet.

La segunda zona es privada de aplicación. Ahí estarán las instancias EC2 con WordPress. Estas instancias no tendrán IP pública. El usuario nunca entra directamente a ellas. Todo el tráfico web llega primero al ALB.

La tercera zona es privada de base de datos. Ahí estará RDS MySQL. La base de datos no debe set pública y solo debe aceptar conexiones desde el Security Group de las EC2.

### 3.2 Direccionamiento

Se usará una VPC con CIDR `10.0.0.0/16`. Dentro de ella se crean seis subredes, tres por cada zona de disponibilidad.

| Capa | Subred | CIDR | Zona de disponibilidad | Uso |
|---|---|---:|---|---|
| Pública | `public-a` | `10.0.1.0/24` | AZ A | ALB y NAT Gateway A |
| Pública | `public-b` | `10.0.2.0/24` | AZ B | ALB y NAT Gateway B |
| Privada app | `app-private-a` | `10.0.11.0/24` | AZ A | EC2 WordPress A |
| Privada app | `app-private-b` | `10.0.12.0/24` | AZ B | EC2 WordPress B |
| Privada DB | `db-private-a` | `10.0.21.0/24` | AZ A | RDS principal o standby |
| Privada DB | `db-private-b` | `10.0.22.0/24` | AZ B | RDS principal o standby |

La separación entre subredes de aplicación y base de datos ayuda a explicar mejor la arquitectura en el informe. También permite aplicar reglas de seguridad más limpias: el ALB habla con EC2, y EC2 habla con RDS.

### 3.3 Diagrama Mermaid

Este diagrama vuelve a usar `flowchart`, porque es la sintaxis más compatible en editores Markdown y visores de Mermaid.

```mermaid
flowchart TB
    user["Usuario en Internet"] --> dns["DNS publico del Application Load Balancer"]

    subgraph aws["AWS Academy / Region AWS"]
      subgraph vpc["VPC 10.0.0.0/16"]
        igw["Internet Gateway"]
        alb["Application Load Balancer\nsubredes publicas A/B"]

        subgraph aza["Availability Zone A"]
          pubA["public-a\n10.0.1.0/24"]
          natA["NAT Gateway A"]
          appA["EC2 WordPress A\napp-private-a\n10.0.11.0/24"]
          dbA["RDS MySQL principal\ndb-private-a\n10.0.21.0/24"]
        end

        subgraph azb["Availability Zone B"]
          pubB["public-b\n10.0.2.0/24"]
          natB["NAT Gateway B"]
          appB["EC2 WordPress B\napp-private-b\n10.0.12.0/24"]
          dbB["RDS standby\ndb-private-b\n10.0.22.0/24"]
        end

        dns --> alb
        alb --> appA
        alb --> appB
        appA --> dbA
        appB --> dbA
        dbA <-->|"Replicacion Multi-AZ"| dbB

        pubA --> igw
        pubB --> igw
        appA --> natA --> igw
        appB --> natB --> igw
      end
    end
```

### 3.4 Cómo Se Mueve El Tráfico

Cuando un usuario abre el sitio, usa el DNS público del ALB. El ALB está en las subredes públicas y recibe tráfico HTTP por el puerto 80. Después envía la petición a una de las instancias EC2 del Target Group.

Las EC2 están en subredes privadas. No tienen IP pública y no se abren al mundo. Esto reduce la superficie de exposición: si alguien intenta entrar por SSH o por una IP directa, no debería poder hacerlo.

WordPress se conecta a RDS por el puerto 3306. La regla importante aquí es que RDS no acepta tráfico desde Internet, ni desde cualquier IP de la VPC. Solo acepta conexiones cuyo origen sea el Security Group de la aplicación.

El Auto Scaling Group mantiene dos instancias. Si una falla, el grupo crea otra. No hay que prometer una recuperación perfecta en segundos, pero sí se puede demostrar que AWS detecta la instancia dañada y la reemplaza.

RDS Multi-AZ mantiene una copia standby en otra zona de disponibilidad. Si AWS Academy no permite activar Multi-AZ por permisos o costo, no se debe inventar la evidencia. Se documenta la restricción y se muestra que el DB Subnet Group sí está preparado con dos subredes privadas en AZ distintas.

### 3.5 Trazabilidad Con El Enunciado

| Requisito del enunciado | Cómo lo cubre esta guía | Evidencia recomendada |
|---|---|---|
| Crear una VPC con seis subredes públicas y privadas | VPC `10.0.0.0/16`, dos subredes públicas, dos privadas de aplicación y dos privadas de base de datos | Captura de VPC y lista de subredes con CIDR y AZ |
| Dar salida a Internet a redes públicas y privadas | Rutas públicas hacia Internet Gateway y rutas privadas hacia NAT Gateway | Capturas de tablas de rutas, IGW y NAT Gateway |
| Crear frontend privado expuesto por balanceador | EC2 WordPress en `app-private-a` y `app-private-b`, publicadas por ALB | Capturas de ALB, Target Group y EC2 sin IP pública |
| Crear grupo de autoescalado para el frontend | Auto Scaling Group con capacidad deseada 2, mínima 2 y máxima 4 | Captura del ASG con dos instancias `InService` |
| Crear base de datos en alta disponibilidad en subredes privadas | RDS MySQL privado con DB Subnet Group en dos AZ y Multi-AZ si está disponible | Captura de RDS privado, DB Subnet Group y configuración Multi-AZ |

## 4. Plan De Trabajo Para 4 Horas

El tiempo de AWS Academy se va rápido. Este orden evita perder tiempo creando recursos que después no pueden conectarse.

| Tiempo | Trabajo | Resultado esperado |
|---:|---|---|
| 0:00 - 0:15 | Iniciar el laboratorio, elegir región y definir nombres | Todos trabajan en la misma región y con el mismo prefijo |
| 0:15 - 0:55 | Crear VPC, subredes, IGW, NAT Gateway y rutas | La red queda lista antes de crear servidores |
| 0:55 - 1:20 | Crear Security Groups y DB Subnet Group | La seguridad queda definida antes de RDS y EC2 |
| 1:20 - 2:00 | Crear RDS MySQL | La base queda lista y se copia el endpoint |
| 2:00 - 2:35 | Crear Launch Template | WordPress queda automatizado con `user data` |
| 2:35 - 3:10 | Crear Target Group, ALB y ASG | El frontend queda publicado por el balanceador |
| 3:10 - 3:35 | Validar funcionamiento | Se revisan targets, WordPress, RDS y recuperación |
| 3:35 - 4:00 | Tomar evidencias y limpiar si aplica | El equipo tiene material para el PDF |

## 5. Antes De Empezar

### 5.1 Acuerdos Del Equipo

Antes de abrir AWS, el equipo debe acordar estos datos:

- Región: por ejemplo `us-east-1`, salvo que el laboratorio indique otra.
- Prefijo de recursos: `act2-F1011`.
- Nombre de la base inicial: `wordpress`.
- Usuario RDS: `wpadmin`.
- Contraseña temporal de RDS: alfanumérica, sin caracteres raros, para evitar errores en el script de arranque.
- Responsible de guardar el endpoint de RDS.
- Responsible de tomar capturas de red, frontend, backend y pruebas.

Esto parece básico, pero evita un problema común: cada integrante crea recursos con nombres distintos y después nadie sabe qué pertenece a la entrega final.

### 5.2 Nombres Sugeridos

| Recurso            | Nombre sugerido                |
| ------------------ | ------------------------------ |
| VPC                | `act2-F1011-vpc`             |
| Internet Gateway   | `act2-F1011-igw`             |
| NAT A              | `act2-F1011-nat-a`           |
| NAT B              | `act2-F1011-nat-b`           |
| Security Group ALB | `act2-F1011-sg-alb`          |
| Security Group app | `act2-F1011-sg-app`          |
| Security Group DB  | `act2-F1011-sg-db`           |
| DB Subnet Group    | `act2-F1011-db-subnet-group` |
| RDS                | `act2-F1011-mysql`           |
| Launch Template    | `act2-F1011-lt-wordpress`    |
| Target Group       | `act2-F1011-tg-wordpress`    |
| ALB                | `act2-F1011-alb`             |
| Auto Scaling Group | `act2-F1011-asg-wordpress`   |

## 6. Paso a Paso En AWS Academy

### Paso 1. Iniciar El Laboratorio

Qué hacer:

1. Entrar a AWS Academy.
2. Abrir el módulo donde esté habilitado el Learner Lab.
3. Seleccionar `Start Lab`.
4. Esperar a que el indicador del laboratorio esté en verde.
5. Entrar a la consola con el botón `AWS`.
6. Confirmar la región que usará todo el equipo.

Por qué se hace:

AWS Academy crea credenciales temporales. Si el laboratorio no está activo, algunos servicios fallarán aunque la consola permita navegar. La región también importa: una VPC creada en una región no aparece en otra.

Qué revisar:

- El laboratorio está en estado activo.
- La consola muestra la región correcta.
- Todos los integrantes usan la misma región para evitar capturas inconsistentes.

Evidencia:

- Captura del laboratorio activo.
- Captura de la región seleccionada.

### Paso 2. Crear la VPC

Qué hacer:

1. Ir a `VPC > Your VPCs > Create VPC`.
2. Seleccionar `VPC only`.
3. Nombre: `act2-F1011-vpc`.
4. CIDR IPv4: `10.0.0.0/16`.
5. Crear la VPC.

Por qué se hace:

La VPC es la red privada donde se colocan todos los components. Usar `10.0.0.0/16` deja espacio suficiente para crear subredes separadas sin quedarse corto.

Qué revisar:

- La VPC aparece en la lista.
- El CIDR es `10.0.0.0/16`.
- No se está usando la VPC por defecto para la entrega.

Evidencia:

- Captura de la VPC con su CIDR.

### Paso 3. Crear Las Seis Subredes

Qué hacer:

1. Ir a `VPC > Subnets > Create subnet`.
2. Seleccionar la VPC `act2-F1011-vpc`.
3. Crear las seis subredes de la tabla de direccionamiento.
4. Usar dos zonas de disponibilidad. Por ejemplo, `us-east-1a` y `us-east-1b`.
5. Activar `Auto-assign public IPv4 address` solo en `public-a` y `public-b`.

Por qué se hace:

Las subredes separan responsabilidades. Las públicas reciben components que necesitan entrada o salida directa a Internet. Las privadas alojan la aplicación y la base de datos. Usar dos AZ permite mostrar alta disponibilidad.

Qué revisar:

- Hay exactamente seis subredes de la práctica.
- Cada subred tiene el CIDR correcto.
- Las subredes públicas están en AZ distintas.
- Las subredes privadas de aplicación están en AZ distintas.
- Las subredes privadas de base de datos están en AZ distintas.
- Solo las públicas tienen autoasignación de IP pública.

Evidencia:

- Captura de la lista de subredes con nombre, CIDR y AZ.

### Paso 4. Crear El Internet Gateway

Qué hacer:

1. Ir a `VPC > Internet gateways > Create internet gateway`.
2. Nombre: `act2-F1011-igw`.
3. Crear el Internet Gateway.
4. Seleccionarlo.
5. Usar `Actions > Attach to VPC`.
6. Asociarlo a `act2-F1011-vpc`.

Por qué se hace:

El Internet Gateway permite que las subredes públicas tengan salida y entrada desde Internet, siempre que las rutas y los Security Groups lo permitan. Sin IGW, el ALB no podría set público.

Qué revisar:

- El IGW aparece como `Attached`.
- Está asociado a la VPC correcta.

Evidencia:

- Captura del IGW asociado a la VPC.

### Paso 5. Crear Los NAT Gateway

Qué hacer:

1. Ir a `VPC > NAT gateways > Create NAT gateway`.
2. Crear `act2-F1011-nat-a` en `public-a`.
3. Asignar una Elastic IP nueva.
4. Crear `act2-F1011-nat-b` en `public-b`.
5. Asignar otra Elastic IP.
6. Esperar a que ambos queden en estado `Available`.

Por qué se hace:

Las EC2 privadas necesitan descargar paquetes durante el arranque, por ejemplo Apache, PHP y WordPress. Como no tienen IP pública, usan NAT Gateway para salir a Internet sin aceptar conexiones entrantes directas.

Se crea un NAT por AZ para evitar que toda la salida dependa de una sola zona. Si AWS Academy limita el presupuesto o los permisos, se puede usar un NAT temporal, pero hay que explicarlo en el informe.

Qué revisar:

- Cada NAT está en una subred pública.
- Cada NAT tiene Elastic IP.
- Ambos están en `Available`.

Evidencia:

- Captura de los NAT Gateway.
- Captura de las Elastic IP asociadas, si se ve en la consola.

### Paso 6. Crear Tablas De Rutas

Qué hacer:

Crear una tabla pública:

1. Nombre: `act2-F1011-rt-public`.
2. Asociar `public-a` y `public-b`.
3. Agregar ruta `0.0.0.0/0` hacia `act2-F1011-igw`.

Crear una tabla privada para AZ A:

1. Nombre: `act2-F1011-rt-private-a`.
2. Asociar `app-private-a`.
3. Asociar `db-private-a` si el equipo decide cumplir literalmente la salida a Internet de todas las subredes privadas.
4. Agregar ruta `0.0.0.0/0` hacia `act2-F1011-nat-a`.

Crear una tabla privada para AZ B:

1. Nombre: `act2-F1011-rt-private-b`.
2. Asociar `app-private-b`.
3. Asociar `db-private-b` si el equipo decide cumplir literalmente la salida a Internet de todas las subredes privadas.
4. Agregar ruta `0.0.0.0/0` hacia `act2-F1011-nat-b`.

Por qué se hace:

Las rutas definen por dónde sale el tráfico. Las subredes públicas salen por el IGW. Las privadas salen por NAT. Así las EC2 privadas pueden instalar software, pero no quedan expuestas con IP pública.

La base de datos RDS normalmente no necesita salida a Internet. Aun así, el enunciado pide salida a Internet en redes privadas. Para cubrirlo de forma literal, se pueden asociar las subredes de base de datos a las tablas privadas con NAT. RDS seguirá sin estar público si `Public access` está en `No` y el Security Group solo permite MySQL desde la app.

Qué revisar:

- La tabla pública tiene `0.0.0.0/0` hacia IGW.
- Las tablas privadas tienen `0.0.0.0/0` hacia el NAT de su AZ.
- Las subredes públicas no están asociadas a tablas privadas.
- Las subredes privadas no están asociadas a la tabla pública.

Evidencia:

- Captura de la tabla pública.
- Captura de cada tabla privada.
- Captura de asociaciones de subredes.

### Paso 7. Crear Security Groups

Qué hacer:

Crear `act2-F1011-sg-alb`:

| Tipo | Protocolo | Puerto | Origen |
|---|---|---:|---|
| HTTP | TCP | 80 | `0.0.0.0/0` |

Crear `act2-F1011-sg-app`:

| Tipo | Protocolo | Puerto | Origen |
|---|---|---:|---|
| HTTP | TCP | 80 | `act2-F1011-sg-alb` |

Crear `act2-F1011-sg-db`:

| Tipo | Protocolo | Puerto | Origen |
|---|---|---:|---|
| MySQL/Aurora | TCP | 3306 | `act2-F1011-sg-app` |

Dejar la salida permitida por defecto en los tres Security Groups.

Por qué se hace:

Los Security Groups controlan quién puede hablar con quién. Esta práctica debe demostrar una cadena simple:

- Internet entra al ALB por HTTP.
- El ALB entra a EC2 por HTTP.
- EC2 entra a RDS por MySQL.
- Nadie entra directo a RDS desde Internet.
- Nadie entra directo a EC2 desde Internet.

No abrir SSH a Internet. Para esta práctica no hace falta si el `user data` instala WordPress correctamente. Abrir SSH a `0.0.0.0/0` puede bajar la calidad de la evidencia de seguridad.

Qué revisar:

- `sg-app` no acepta HTTP desde `0.0.0.0/0`, solo desde `sg-alb`.
- `sg-db` no acepta MySQL desde `0.0.0.0/0`, solo desde `sg-app`.
- No hay regla SSH abierta a Internet.

Evidencia:

- Capturas de reglas inbound de los tres Security Groups.

### Paso 8. Crear El DB Subnet Group

Qué hacer:

1. Ir a `RDS > Subnet groups > Create DB subnet group`.
2. Nombre: `act2-F1011-db-subnet-group`.
3. Seleccionar la VPC `act2-F1011-vpc`.
4. Seleccionar las dos zonas de disponibilidad usadas.
5. Seleccionar `db-private-a` y `db-private-b`.
6. Crear el grupo.

Por qué se hace:

RDS necesita saber en qué subredes puede desplegar la base de datos. Si se configura Multi-AZ, AWS usará subredes de más de una zona. Por eso no se debe meter RDS en las subredes de aplicación ni en las públicas.

Qué revisar:

- El grupo tiene dos subredes.
- Las dos subredes son privadas de base de datos.
- Las subredes pertenecen a zonas distintas.

Evidencia:

- Captura del DB Subnet Group con subredes y AZ.

### Paso 9. Crear RDS MySQL

Qué hacer:

1. Ir a `RDS > Databases > Create database`.
2. Método: `Standard create`.
3. Motor: `MySQL`.
4. Template: `Free tier` si está disponible. Si no permite Multi-AZ, usar `Dev/Test`.
5. DB instance identifier: `act2-F1011-mysql`.
6. Master username: `wpadmin`.
7. Password: usar la contraseña acordada por el equipo.
8. Clase: `db.t3.micro`, `db.t4g.micro` o la menor permitida por AWS Academy.
9. Storage: tamaño mínimo permitido.
10. Multi-AZ: activar `Create a standby instance` o `Multi-AZ DB instance deployment` si la consola lo permite.
11. VPC: `act2-F1011-vpc`.
12. DB Subnet Group: `act2-F1011-db-subnet-group`.
13. Public access: `No`.
14. Security Group: `act2-F1011-sg-db`.
15. Database authentication: contraseña.
16. Initial database name: `wordpress`.
17. Crear la base de datos.
18. Esperar a que quede en `Available`.
19. Copiar el endpoint de RDS sin el puerto.

Por qué se hace:

WordPress necesita una base de datos para guardar usuarios, entradas y configuración. RDS evita instalar MySQL manualmente en EC2 y permite mostrar una base de datos administrada en subredes privadas.

El punto más importante para la rúbrica es que RDS esté en red privada y funcione con la aplicación. Multi-AZ suma la parte de alta disponibilidad. Si AWS Academy no deja usar Multi-AZ, el informe debe decirlo con claridad y mostrar la configuración más cercana: DB Subnet Group en dos AZ, RDS privado y conexión funcional desde WordPress.

Qué revisar:

- Estado `Available`.
- `Publicly accessible: No`.
- Security Group correcto.
- DB Subnet Group correcto.
- Multi-AZ habilitado, si el laboratorio lo permite.
- Endpoint copiado correctamente.

Evidencia:

- Captura general de RDS.
- Captura de conectividad y seguridad.
- Captura de Multi-AZ o nota de limitación si no está disponible.

### Paso 10. Crear El Launch Template

Qué hacer:

1. Ir a `EC2 > Launch Templates > Create launch template`.
2. Nombre: `act2-F1011-lt-wordpress`.
3. AMI: Amazon Linux 2023.
4. Tipo de instancia: `t3.micro` o `t2.micro`, según disponibilidad.
5. Key pair: `Proceed without a key pair`.
6. No seleccionar subred en el template.
7. Security Group: `act2-F1011-sg-app`.
8. En `Advanced details > User data`, pegar el script siguiente y reemplazar los valores de RDS.

```bash
#!/bin/bash
dnf update -y
dnf install -y httpd php php-mysqli php-json php-gd php-mbstring wget tar
systemctl enable --now httpd

cd /tmp
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
cp -r wordpress/* /var/www/html/
chown -R apache:apache /var/www/html
chmod -R 755 /var/www/html

cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
sed -i "s/database_name_here/wordpress/" /var/www/html/wp-config.php
sed -i "s/username_here/wpadmin/" /var/www/html/wp-config.php
sed -i "s/password_here/REEMPLAZAR_PASSWORD_RDS/" /var/www/html/wp-config.php
sed -i "s/localhost/REEMPLAZAR_ENDPOINT_RDS/" /var/www/html/wp-config.php

cat > /var/www/html/health.html <<'EOF'
ok
EOF

systemctl restart httpd
```

Por qué se hace:

El Launch Template define cómo serán las EC2 que crea el Auto Scaling Group. El `user data` instala Apache, PHP y WordPress sin entrar por SSH. Esto ahorra tiempo y deja una configuración repetible.

El archivo `/health.html` es una página simple para el health check del Target Group. Es mejor que usar `/`, porque WordPress puede redirigir o mostrar instalación incompleta durante los primeros minutos.

Qué revisar:

- El endpoint de RDS no incluye `:3306`.
- La contraseña coincide con la configurada en RDS.
- El Security Group es `sg-app`.
- No se fija una subred en el Launch Template; las subredes se eligen en el ASG.

Evidencia:

- Captura del Launch Template.
- Captura parcial del `user data`, ocultando la contraseña si aparece.

### Paso 11. Crear El Target Group

Qué hacer:

1. Ir a `EC2 > Target Groups > Create target group`.
2. Tipo: `Instances`.
3. Nombre: `act2-F1011-tg-wordpress`.
4. Protocolo: HTTP.
5. Puerto: 80.
6. VPC: `act2-F1011-vpc`.
7. Health check path: `/health.html`.
8. Crear el Target Group sin registrar instancias manualmente.

Por qué se hace:

El Target Group es la lista de instancias a las que el ALB puede enviar tráfico. No se registran instancias manualmente porque el Auto Scaling Group lo hará automáticamente.

Qué revisar:

- El Target Group usa la VPC correcta.
- El health check apunta a `/health.html`.
- Todavía puede aparecer vacío hasta crear el ASG.

Evidencia:

- Captura del Target Group y su health check.

### Paso 12. Crear El Application Load Balancer

Qué hacer:

1. Ir a `EC2 > Load Balancers > Create load balancer`.
2. Seleccionar `Application Load Balancer`.
3. Nombre: `act2-F1011-alb`.
4. Scheme: `Internet-facing`.
5. IP address type: IPv4.
6. VPC: `act2-F1011-vpc`.
7. Seleccionar `public-a` y `public-b`.
8. Security Group: `act2-F1011-sg-alb`.
9. Listener HTTP 80: reenviar a `act2-F1011-tg-wordpress`.
10. Crear el ALB.

Por qué se hace:

El ALB es el único punto de entrada público de la aplicación. Reparte las peticiones entre las EC2 privadas y permite que el usuario use un DNS público sin conocer las instancias.

Qué revisar:

- El ALB es `Internet-facing`.
- Está en las dos subredes públicas.
- Tiene el Security Group del ALB.
- El listener HTTP 80 apunta al Target Group correcto.

Evidencia:

- Captura del ALB.
- Captura del listener.
- Captura del DNS del ALB.

### Paso 13. Crear El Auto Scaling Group

Qué hacer:

1. Ir a `EC2 > Auto Scaling Groups > Create Auto Scaling group`.
2. Nombre: `act2-F1011-asg-wordpress`.
3. Launch Template: `act2-F1011-lt-wordpress`.
4. VPC: `act2-F1011-vpc`.
5. Subredes: `app-private-a` y `app-private-b`.
6. Asociar al Load Balancer existente.
7. Target Group: `act2-F1011-tg-wordpress`.
8. Health checks: habilitar ELB health checks.
9. Desired capacity: 2.
10. Minimum capacity: 2.
11. Maximum capacity: 4.
12. Política de escalado: CPU promedio de 60 %, si el laboratorio lo permite.
13. Crear el Auto Scaling Group.

Por qué se hace:

El ASG mantiene la cantidad de EC2 esperada. Si una instancia se detiene o queda no saludable, AWS crea otra usando el Launch Template. También permite demostrar que el frontend no depende de una sola máquina.

Qué revisar:

- Las subredes del ASG son privadas de aplicación, no públicas.
- La capacidad deseada es 2.
- El ASG está conectado al Target Group.
- Las instancias aparecen como `InService`.

Evidencia:

- Captura del ASG.
- Captura de instancias creadas.
- Captura del Target Group con targets `Healthy`.

### Paso 14. Validar WordPress

Qué hacer:

1. Abrir el DNS del ALB en el navegador.
2. Esperar unos minutos si aparece error 503 o si los targets siguen `initial`.
3. Completar la instalación inicial de WordPress.
4. Crear una publicación de prueba llamada `Prueba alta disponibilidad`.
5. Recargar el sitio varias veces.

Por qué se hace:

Esta prueba demuestra que el flujo completo funciona: usuario, ALB, EC2, WordPress y RDS. Si WordPress permite crear una publicación, entonces la aplicación pudo escribir en la base de datos.

Qué revisar:

- El sitio carga por el DNS del ALB.
- No se usa una IP pública de EC2.
- La publicación se guarda correctamente.

Evidencia:

- Captura del DNS del ALB en el navegador.
- Captura de WordPress funcionando.
- Captura de la publicación de prueba.

### Paso 15. Crear Una Página En WordPress

Qué hacer:

1. Abrir el DNS del ALB en el navegador.
2. Si no estás dentro del panel, entrar a `http://DNS-DEL-ALB/wp-admin`.
3. Iniciar sesión con el usuario administrador creado durante la instalación inicial de WordPress.
4. En el menú lateral, ir a `Páginas > Añadir nueva`.
5. Título sugerido: `Alta disponibilidad en AWS - F1011`.
6. En el contenido de la página, escribir un texto breve como este:

```text
Esta página fue creada por el equipo F1011 para validar el despliegue de WordPress en alta disponibilidad sobre AWS Academy.

La aplicación se publica mediante un Application Load Balancer, se ejecuta en instancias EC2 privadas dentro de un Auto Scaling Group y guarda su información en una base de datos RDS MySQL privada.
```

1. Seleccionar `Publicar`.
2. Abrir la página publicada con el botón `Ver página`.
3. Copiar la URL generada por WordPress.
4. Abrir esa URL en una ventana privada o en otro navegador para confirmar que se ve sin estar dentro del administrador.

Por qué se hace:

Esta página sirve como evidencia funcional. No demuestra solo que Apache responde; demuestra que WordPress pudo guardar contenido en RDS y después leerlo desde el sitio público. Eso conecta directamente con el requisito de frontend funcionando y backend operativo.

Qué revisar:

- La página aparece publicada.
- La URL usa el DNS del ALB, no una IP de EC2.
- La página se puede abrir sin iniciar sesión.
- El contenido menciona al equipo `F1011` y la arquitectura usada.

Evidencia:

- Captura del editor de WordPress con la página publicada.
- Captura de la página abierta desde el DNS del ALB.
- Captura de la URL visible en el navegador.

Nota:

No es necesario cambiar los enlaces permanentes de WordPress. Si WordPress muestra una URL con `?page_id=123`, usar esa URL. Es suficiente para la práctica y evita errores de Apache con permalinks personalizados.

### Paso 16. Probar Recuperación Ante Fallo

Qué hacer:

1. Ir a `EC2 > Instances`.
2. Identificar una instancia creada por el ASG.
3. Detener una instancia.
4. Revisar el Target Group.
5. Revisar el Auto Scaling Group.
6. Confirmar que AWS crea una instancia nueva.
7. Confirmar que el sitio sigue respondiendo desde el DNS del ALB.

Por qué se hace:

La alta disponibilidad no se demuestra solo diciendo que hay dos instancias. Hay que mostrar qué pasa cuando una falla. Esta prueba permite evidenciar que el ASG detecta la pérdida y vuelve a la capacidad deseada.

Qué revisar:

- Una instancia pasa a estado detenido o terminado.
- El ASG lanza una instancia nueva.
- El Target Group vuelve a mostrar targets saludables.
- El sitio sigue accessible.

Evidencia:

- Captura antes de detener la instancia.
- Captura durante el reemplazo.
- Captura después, con dos instancias activas.
- Captura del sitio funcionando.

## 7. Notas Importantes Para no Confundirse

### 7.1 WordPress Y Archivos Locales

WordPress guarda archivos subidos en `wp-content/uploads`. En esta práctica, cada EC2 tendría su propio disco local. Eso significa que una imagen subida desde una instancia podría no verse igual si otra instancia atiende la siguiente petición.

Para esta actividad, validar con una publicación de texto. Para una arquitectura productiva, se agregaría EFS o S3 para compartir archivos entre instancias.

### 7.2 RDS Y Salida a Internet

RDS no necesita salir a Internet para que WordPress funcione. Aun así, el enunciado pide salida a Internet para redes privadas. Por eso la guía propone asociar también las subredes privadas de base de datos a tablas privadas con NAT, si el equipo quiere cumplir literalmente esa parte.

Esto no vuelve pública la base de datos. Lo que vuelve público o privado a RDS depende de `Publicly accessible` y del Security Group.

### 7.3 Si Multi-AZ no Aparece

AWS Academy puede limitar opciones de RDS por permisos, región o costo. Si no se puede activar Multi-AZ, no conviene forzarlo ni mentir en el informe.

La forma correcta de documentarlo es:

- Mostrar que RDS está en subred privada.
- Mostrar que el DB Subnet Group tiene dos AZ.
- Mostrar que WordPress funciona con RDS.
- Explicar que Multi-AZ no estuvo disponible en la cuenta de laboratorio.
- Indicar que, en una cuenta sin esa restricción, se activaría `Multi-AZ DB instance deployment`.

## 8. Guía Rápida De Replicación

Esta lista sirve para que cada integrante repita la práctica en su propia sesión.

1. Iniciar AWS Academy Learner Lab.
2. Confirmar región.
3. Crear VPC `10.0.0.0/16`.
4. Crear seis subredes.
5. Activar IP pública automática solo en `public-a` y `public-b`.
6. Crear y asociar Internet Gateway.
7. Crear NAT Gateway A y NAT Gateway B.
8. Crear tabla pública hacia IGW.
9. Crear tablas privadas hacia NAT Gateway.
10. Crear Security Groups para ALB, app y DB.
11. Crear DB Subnet Group con `db-private-a` y `db-private-b`.
12. Crear RDS MySQL privado.
13. Copiar endpoint de RDS.
14. Crear Launch Template con `user data`.
15. Crear Target Group HTTP 80 con `/health.html`.
16. Crear ALB en subredes públicas.
17. Crear ASG en subredes privadas de aplicación.
18. Esperar targets `Healthy`.
19. Abrir DNS del ALB.
20. Completar instalación de WordPress.
21. Crear publicación de prueba.
22. Crear la página `Alta disponibilidad en AWS - F1011`.
23. Abrir la página publicada desde el DNS del ALB.
24. Detener una instancia y revisar reemplazo.
25. Tomar capturas.
26. Limpiar recursos si el laboratorio queda activo.

## 9. Evidencias Mínimas Para El PDF

Cada captura debe tener una breve explicación. No basta con pegar imágenes sin contexto.

| Evidencia | Qué demuestra |
|---|---|
| AWS Academy activo | Que se usó la cuenta del laboratorio |
| VPC | Que existe una red propia con CIDR privado |
| Seis subredes | Que se separaron capas públicas, app y DB |
| Internet Gateway | Que las subredes públicas pueden salir a Internet |
| NAT Gateway | Que las subredes privadas tienen salida controlada |
| Tablas de rutas | Que el tráfico sale por el componente correcto |
| Security Groups | Que ALB, EC2 y RDS tienen reglas separadas |
| DB Subnet Group | Que RDS usa subredes privadas en dos AZ |
| RDS | Que la base es privada y está disponible |
| Launch Template | Que el despliegue de WordPress está automatizado |
| Target Group | Que las instancias están saludables |
| ALB | Que el sitio se publica por un balanceador |
| ASG | Que hay dos instancias y capacidad deseada 2 |
| WordPress funcionando | Que la aplicación carga desde Internet |
| Publicación de prueba | Que WordPress escribe en RDS |
| Página de WordPress `Alta disponibilidad en AWS - F1011` | Que el contenido publicado se puede leer desde el DNS del ALB |
| Reemplazo de instancia | Que el ASG recupera capacidad |

## 10. Criterios De Aceptación

El despliegue se puede considerar terminado cuando se cumple lo siguiente:

- La VPC propia existe y usa `10.0.0.0/16`.
- Hay seis subredes con los CIDR definidos en esta guía.
- Las subredes públicas tienen ruta `0.0.0.0/0` hacia el Internet Gateway.
- Las subredes privadas de aplicación tienen ruta `0.0.0.0/0` hacia NAT Gateway.
- Las subredes privadas de base de datos tienen ruta privada hacia NAT si el equipo decidió cubrir literalmente la salida a Internet de todas las redes privadas.
- El ALB es público y está en `public-a` y `public-b`.
- Las EC2 están en `app-private-a` y `app-private-b`.
- Las EC2 no tienen IP pública.
- El Target Group muestra dos targets saludables.
- El ASG mantiene capacidad deseada 2.
- RDS está en subredes privadas.
- RDS tiene `Publicly accessible: No`.
- RDS solo acepta MySQL desde el Security Group de la aplicación.
- WordPress carga desde el DNS del ALB.
- WordPress puede crear contenido, lo que prueba conexión con RDS.
- Existe una página publicada en WordPress con el nombre del equipo `F1011`.
- La página publicada se puede abrir desde el DNS del ALB sin entrar al panel de administración.
- Se documentó Multi-AZ o la restricción de AWS Academy.

## 11. Problemas Frecuentes Y Solución

| Problema | Causa probable | Qué revisar |
|---|---|---|
| El ALB muestra 503 | No hay targets saludables | Revisar Target Group, health check `/health.html` y Security Group de EC2 |
| Las EC2 no instalan WordPress | No tienen salida a Internet | Revisar ruta privada hacia NAT Gateway |
| WordPress no conecta con RDS | Endpoint, usuario, contraseña o SG incorrectos | Revisar `wp-config.php`, endpoint sin puerto y regla 3306 |
| RDS no aparece como privado | Se marcó acceso público | Revisar `Publicly accessible: No` |
| No aparece Multi-AZ | Restricción de AWS Academy | Documentar la limitación y mostrar DB Subnet Group en dos AZ |
| La página publicada muestra 404 | Se cambiaron los enlaces permanentes o Apache no permite reescritura | Usar la URL simple de WordPress con `?page_id=123` o guardar de nuevo los enlaces permanentes en modo básico |
| El sitio cambia al recargar | Las dos EC2 no comparten archivos locales | Validar con texto; para producción usar EFS o S3 |
| No se puede borrar la VPC | Aún quedan recursos asociados | Eliminar primero ASG, ALB, RDS, NAT, EIP y subredes |

## 12. Limpieza De Recursos

Si el laboratorio queda activo, limpiar recursos en este orden:

1. Auto Scaling Group, marcando que determine instancias.
2. Application Load Balancer.
3. Target Group.
4. RDS.
5. NAT Gateway.
6. Elastic IP liberadas.
7. Launch Template.
8. Security Groups personalizados.
9. Route Tables personalizadas.
10. Subredes.
11. Internet Gateway.
12. VPC.

Este orden evita errores por dependencias. Por ejemplo, no se puede borrar una VPC si todavía tiene subredes, interfaces de red, NAT Gateway o un RDS asociado.

## 13. Referencias

Amazon Web Services. (s. f.). *Example: VPC with servers in private subnets and NAT*. AWS Documentation. https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html

Amazon Web Services. (s. f.). *Use Elastic Load Balancing to distribute incoming application traffic in your Auto Scaling group*. AWS Documentation. https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html

Amazon Web Services. (s. f.). *Multi-AZ DB instance deployments for Amazon RDS*. AWS Documentation. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html

Amazon Web Services. (s. f.). *Working with a DB instance in a VPC*. AWS Documentation. https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html
