# 🚀 Guía De Configuración - Microservicios Inventario

Esta guía te ayudará a configurar todo el entorno necesario para trabajar con nuestros 5 microservicios.

## 📋 Prerequisitos

Antes de comenzar, necesitarás acceso a los repositorios y las herramientas correctas instaladas.

---

## 📧 Paso 1: Solicitar Acceso a Los Repositorios

### 📝 Instrucciones

1. **Envía tu correo electrónico** al administrador del proyecto
2. **Espera la invitación** a la organización GitHub `Unir-F1011`
3. **Acepta la invitación** que llegará a tu correo
4. Una vez aceptada, tendrás acceso para clonar todos los repositorios

### 📂 Repositorios Del Proyecto

```bash
# Frontend (React + Vite)
https://github.com/Unir-F1011/inventario-front.git

# API Gateway (Spring Cloud Gateway)
https://github.com/Unir-F1011/cloud-gateway.git

# Servicio de Operadores (Spring Boot)
https://github.com/Unir-F1011/operator.git

# Servicio de Búsqueda (Spring Boot + Elasticsearch)
https://github.com/Unir-F1011/search.git

# Servicio de Descubrimiento (Eureka Server)
https://github.com/Unir-F1011/eureka.git
```

---

## ☕ Paso 2: Verificar E Instalar Java 23

Este proyecto **require Java 23**. Verifica tu versión actual:

### 🔍 Verificar Versión Actual

```bash
java -version
```

**✅ Resultado esperado:**

```Python
java version "23.0.2" 2025-01-21
Java(TM) SE Runtime Environment (build 23.0.2+7-58)
Java HotSpot(TM) 64-Bit Server VM (build 23.0.2+7-58, mixed mode, sharing)
```

### 📥 Instalar Java 23 (si no Lo tienes)

#### Windows

1. **Descargar Oracle JDK 23:**
   - Ve a: https://www.oracle.com/java/technologies/downloads/#java23
   - Descarga: `Windows x64 Installer`
   
2. **Instalar:**
   - Ejecuta el `.exe` descargado
   - Sigue el asistente de instalación
   - **Importante:** Selecciona "Add to PATH" durante la instalación

3. **Configurar Variables de Entorno:**

   ```bash
   # Abrir PowerShell como Administrador
   setx JAVA_HOME "C:\Program Files\Java\jdk-23" /M
   setx PATH "%PATH%;%JAVA_HOME%\bin" /M
   ```

#### MacOS

```bash
# Usando Homebrew
brew install openjdk@23
echo 'export PATH="/opt/homebrew/opt/openjdk@23/bin:$PATH"' >> ~/.zshrc
```

#### Linux (Ubuntu/Debian)

```bash
# Actualizar repositorios
sudo apt update

# Instalar OpenJDK 23
sudo apt install openjdk-23-jdk

# Configurar como default
sudo update-alternatives --config java
```

### 🔄 **IMPORTANTE - Reiniciar Después De la Instalación:**

```bash
# 1. Cierra TODAS las terminales abiertas
# 2. Reinicia tu PC completamente
# 3. Abre una nueva terminal y verifica:
java -version
```

---

## 🐳 Paso 3: Instalar Docker

Docker es necesario para ejecutar los microservicios en contenedores.

### 🔍 Verificar Si Docker Está Instalado

```bash
docker --version
docker-compose --version
```

### 📥 Instalar Docker

#### Windows

1. **Descargar Docker Desktop:**
   - Ve a: https://www.docker.com/products/docker-desktop
   - Descarga: `Docker Desktop for Windows`

2. **Instalar:**
   - Ejecuta el instalador
   - **Importante:** Habilita WSL 2 si se solicita
   - Reinicia cuando se solicite

3. **Verificar Instalación:**

   ```bash
   docker --version
   docker run hello-world
   ```

#### MacOS

1. **Descargar Docker Desktop:**
   - Ve a: https://www.docker.com/products/docker-desktop
   - Descarga para tu arquitectura (Intel o Apple Silicon)

2. **Instalar:**
   - Arrastra Docker. App a Applications
   - Ejecuta Docker Desktop desde Applications

#### Linux (Ubuntu)

```bash
# Actualizar paquetes
sudo apt update

# Instalar dependencias
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Agregar clave GPG de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Agregar repositorio
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Instalar Docker
sudo apt install docker-ce docker-ce-cli containerd.io

# Agregar usuario al grupo docker
sudo usermod -aG docker $USER

# Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### 🔄 **IMPORTANTE - Reiniciar Después De Docker:**

```bash
# 1. Reinicia tu PC completamente
# 2. Abre Docker Desktop y espera que inicie
# 3. Verifica en terminal:
docker --version
docker-compose --version
```

---

## ✅ Verificación Final

Antes de continuar, asegúrate de que tienes todo configurado:

```bash
# Verificar Java 23
java -version

# Verificar Docker
docker --version
docker-compose --version

# Verificar Git
git --version

# Verificar acceso a GitHub (debe pedir credenciales si es la primera vez)
git ls-remote https://github.com/Unir-F1011/eureka.git
```

---

## 🎯 Siguiente Paso

Una vez completados estos pasos, estarás listo para:

- Clonar los repositorios
- Configurar el entorno de desarrollo
- Ejecutar los microservicios

**💡 Consejo:** Mantén Docker Desktop ejecutándose en segundo plano siempre que trabajes con el proyecto.

---

## 🆘 Problemas Comunes

### Java no Se Reconoce

- Verifica que `JAVA_HOME` esté configurado
- Reinicia la terminal completamente
- En Windows, ejecuta `refreshenv` en PowerShell

### Docker no Inicia

- Asegúrate de que la virtualización esté habilitada en BIOS
- En Windows, verifica que WSL 2 esté instalado
- Reinicia Docker Desktop

### Acceso Denegado a Repositorios

- Verifica que aceptaste la invitación de GitHub
- Configura tu autenticación SSH o token personal

---

## 📂 Paso 4: Clonar Los Repositorios

Una vez que tengas acceso a todos los repositorios, puedes clonarlos de dos maneras:

### 📋 **Opción 1: Clonar Repositorios Individualmente**

Clona cada repositorio uno por uno:

```bash
# 1. Crear directorio principal para el proyecto
mkdir microservicios-inventario
cd microservicios-inventario

# 2. Clonar cada repositorio individualmente
git clone https://github.com/Unir-F1011/eureka.git
git clone https://github.com/Unir-F1011/cloud-gateway.git
git clone https://github.com/Unir-F1011/search.git
git clone https://github.com/Unir-F1011/operator.git
git clone https://github.com/Unir-F1011/inventario-front.git
```

**✅ Resultado esperado:**

```Python
microservicios-inventario/
├── eureka/
├── cloud-gateway/
├── search/
├── operator/
└── inventario-front/
```

### 🚀 **Opción 2: Clonar Todos Los Repositorios De Una Vez**

Usa este script para clonar todos automáticamente:

#### Windows (PowerShell)

```powershell
# Crear directorio y navegar
mkdir microservicios-inventario; cd microservicios-inventario

# Array de repositorios
$repos = @(
    "https://github.com/Unir-F1011/eureka.git",
    "https://github.com/Unir-F1011/cloud-gateway.git", 
    "https://github.com/Unir-F1011/search.git",
    "https://github.com/Unir-F1011/operator.git",
    "https://github.com/Unir-F1011/inventario-front.git"
)

# Clonar todos los repositorios
foreach ($repo in $repos) {
    Write-Host "Clonando: $repo" -ForegroundColor Green
    git clone $repo
}

Write-Host "✅ Todos los repositorios clonados exitosamente!" -ForegroundColor Green
```

#### MacOS/Linux (Bash)

```bash
#!/bin/bash

# Crear directorio y navegar
mkdir microservicios-inventario && cd microservicios-inventario

# Array de repositorios
repos=(
    "https://github.com/Unir-F1011/eureka.git"
    "https://github.com/Unir-F1011/cloud-gateway.git"
    "https://github.com/Unir-F1011/search.git"
    "https://github.com/Unir-F1011/operator.git"
    "https://github.com/Unir-F1011/inventario-front.git"
)

# Clonar todos los repositorios
for repo in "${repos[@]}"; do
    echo "🔄 Clonando: $repo"
    git clone "$repo"
done

echo "✅ Todos los repositorios clonados exitosamente!"
```

### 🔧 **Script Automático (Copia Y Pega)**

Para mayor facilidad, aquí tienes un commando que puedes copiar y pegar directamente:

```bash
# Windows PowerShell (una sola línea)
mkdir microservicios-inventario; cd microservicios-inventario; git clone https://github.com/Unir-F1011/eureka.git; git clone https://github.com/Unir-F1011/cloud-gateway.git; git clone https://github.com/Unir-F1011/search.git; git clone https://github.com/Unir-F1011/operator.git; git clone https://github.com/Unir-F1011/inventario-front.git

# macOS/Linux (una sola línea)
mkdir microservicios-inventario && cd microservicios-inventario && git clone https://github.com/Unir-F1011/eureka.git && git clone https://github.com/Unir-F1011/cloud-gateway.git && git clone https://github.com/Unir-F1011/search.git && git clone https://github.com/Unir-F1011/operator.git && git clone https://github.com/Unir-F1011/inventario-front.git
```

### 🔍 **Verificar Que Todo Se Clonó Correctamente**

```bash
# Listar directorios clonados
ls -la
```

**✅ Deberías ver:**

```Python
📁 microservicios-inventario/
├── 📁 eureka/                    # Servicio de descubrimiento
├── 📁 cloud-gateway/            # API Gateway  
├── 📁 search/                   # Servicio de búsqueda
├── 📁 operator/                 # Servicio de operadores
└── 📁 inventario-front/         # Frontend React
```

### 🚨 **Troubleshooting Del Clonado**

#### Error: "Permission denied"

```bash
# Configurar credenciales de Git (primera vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"

# Si usas token personal en lugar de contraseña
git config --global credential.helper store
```

#### Error: "Repository not found"

- ✅ Verifica que aceptaste la invitación de GitHub
- ✅ Confirma que tu usuario tiene acceso a la organización `Unir-F1011`
- ✅ Prueba acceder a cada repo en el navegador primero

#### Error: "Could not Resolve hostname"

- ✅ Verifica tu conexión a internet
- ✅ Intenta con SSH en lugar de HTTPS:

```bash
# Ejemplo con SSH
git clone git@github.com:Unir-F1011/eureka.git
```

---

## ⚙️ Paso 5: Configurar Variables De Entorno

Cada microservicio necesita variables de entorno específicas para funcionar correctamente.

### 🔍 **Encontrar Archivos De Ejemplo**

En cada repositorio verás archivos de muestra:

```bash
📁 search/
├── 📄 .env                    # Variables de producción
├── 📄 test.env               # Variables de prueba/ejemplo
└── 📄 .env.example          # Plantilla (si existe)
```

### 📋 **Variables Disponibles**

**Opción 1:** Usa las variables que compartió **Michael en WhatsApp**  
**Opción 2:** Crea tus propias variables basándote en `test.env`

### 🔧 **Configurar Variables Por Servicio**

#### 1. **Servicio Search:**

```bash
cd search
# Copia el archivo de ejemplo
cp test.env .env

# Edita con tus datos
notepad .env  # Windows
nano .env     # Linux/macOS
```

**Ejemplo de variables para Search (. Env):**

```properties
# Elasticsearch Configuration
ELASTICSEARCH_HOST=unir-search-3107723626.us-east-1.bonsaisearch.net
ELASTICSEARCH_USER=v5fjxazmfs
ELASTICSEARCH_PWD=nixw3719am

# Eureka Configuration
EUREKA_URL=http://ms-eureka:8761/eureka
SERVER_PORT=8081
SERVER_NAME=ms-search
```

#### 2. **Otros Servicios:**

```bash
# Operator
cd ../operator
cp test.env .env
# Editar las variables necesarias

# Cloud Gateway
cd ../cloud-gateway
cp test.env .env
# Editar las variables necesarias

# Eureka (si tiene variables)
cd ../eureka
# Revisar si necesita .env
```

### 📝 **Variables Importantes a Configurar:**

| Servicio | Variables Clave |
|----------|----------------|
| **Eureka** | `SERVER_PORT`, `EUREKA_HOSTNAME` |
| **Cloud Gateway** | `EUREKA_URL`, `SERVER_PORT` |
| **Search** | `ELASTICSEARCH_*`, `EUREKA_URL` |
| **Operator** | `DATABASE_URL`, `EUREKA_URL` |
| **Frontend** | `VITE_API_URL`, `VITE_GATEWAY_URL` |

### ⚠️ **IMPORTANTE:**

- **NO subas archivos `.env` a Git** (ya están en `.gitignore`)
- **Usa las credenciales de WhatsApp** para producción
- **Crea copias de respaldo** de tus archivos `.env`

---

## 🐳 Paso 6: Ejecutar Los Contenedores

Los microservicios deben ejecutarse en un **orden específico** para que funcionen correctamente.

### 📋 **Orden De Ejecución:**

```Python
1. 🔧 Eureka (Service Discovery)  ← Primero
2. 🌐 Cloud Gateway              ← Segundo  
3. 🔍 Search + 👤 Operator       ← Tercero (paralelo)
4. 🎨 Frontend                   ← Último
```

### 🚀 **Ejecución Paso a Paso:**

#### **Paso 1: Iniciar Eureka (Service Discovery)**

```bash
cd eureka

# Compilar el proyecto
./mvnw clean package -DskipTests
# esto falla por tema de las versiones

# Construir imagen Docker
docker build -t ms-eureka .

# Ejecutar contenedor
docker run -d -p 8761:8761 --name ms-eureka ms-eureka

# Verificar que está funcionando
curl http://localhost:8761
```

**✅ Espera 30-60 segundos** hasta que Eureka esté completamente iniciado.

#### **Paso 2: Iniciar Cloud Gateway**

```bash
cd ../cloud-gateway

# Compilar
./mvnw clean package -DskipTests

# Construir imagen
docker build -t cloud-gateway .

# Ejecutar (conectado a Eureka)
docker run -d -p 8080:8080 --name cloud-gateway 
```

#### **Paso 3: Iniciar Servicios De Negocio (Paralelo)**

**Search Service:**

```bash
cd ../search

# Compilar
./mvnw clean package -DskipTests

# Construir imagen
docker build -t ms-search .

# Ejecutar con variables de entorno
docker run -d -p 8081:8081 --name ms-search 
```

**Operator Service:**

```bash
cd ../operator

# Compilar
./mvnw clean package -DskipTests

# Construir imagen  
docker build -t ms-operator .

# Ejecutar
docker run -d -p 8082:8082 --name ms-operator 
```

#### **Paso 4: Iniciar Frontend**

```bash
cd ../inventario-front

# Construir imagen
docker build -t inventario-front .

# Ejecutar contenedor
docker run -d -p 5050:5050 --name inventario-front inventario-front
```

### 🔍 **Verificar Que Todo Funciona:**

```bash
# Verificar contenedores ejecutándose
docker ps

# Verificar logs si hay problemas
docker logs ms-eureka
docker logs cloud-gateway
docker logs ms-search
docker logs ms-operator
docker logs inventario-front

# Probar endpoints
curl http://localhost:8761    # Eureka Dashboard
curl http://localhost:8080    # Gateway
curl http://localhost:5050    # Frontend
```

### 🌐 **URLs De Acceso:**

| Servicio | URL | Descripción |
|----------|-----|-------------|
| **Eureka Dashboard** | http://localhost:8761 | Panel de servicios registrados |
| **API Gateway** | http://localhost:8080 | Punto de entrada a APIs |
| **Frontend** | http://localhost:5050 | Aplicación web principal |
| **Search Service** | http://localhost:8081 | API de búsqueda directa |
| **Operator Service** | http://localhost:8082 | API de operadores directa |

### 🧹 **Commandos De Limpieza:**

Si necesitas reiniciar todo:

```bash
# Parar todos los contenedores
docker stop ms-eureka cloud-gateway ms-search ms-operator inventario-front

# Eliminar contenedores
docker rm ms-eureka cloud-gateway ms-search ms-operator inventario-front

# Limpiar imágenes (opcional)
docker rmi ms-eureka cloud-gateway ms-search ms-operator inventario-front
```

### 🆘 **Troubleshooting:**

#### Servicios no Se Registran En Eureka

- Verifica que Eureka esté completamente iniciado (espera 1-2 minutos)
- Revisa las URLs de Eureka en las variables de entorno
- Comprueba los logs: `docker logs <servicio>`

#### Frontend no Carga

- Verifica que el Gateway esté funcionando en puerto 8080
- Revisa las variables de entorno del frontend
- Comprueba que Nginx esté sirviendo correctamente: `docker logs inventario-front`

#### Errores De Compilación Java

- Verifica que estés usando Java 23: `java -version`
- Limpia el proyecto: `./mvnw clean`
- Revisar dependencias en `pom.xml`

---

## 🎉 ¡Felicidades

Si llegaste hasta aquí, ya tienes todo el stack de microservicios funcionando:

✅ Java 23 configurado  
✅ Docker instalado y funcionando  
✅ Repositorios clonados  
✅ Variables de entorno configuradas  
✅ Todos los servicios ejecutándose  

**🚀 Tu aplicación está lista en:** http://localhost:5050



## cambios Entrega tres

### local

1. 