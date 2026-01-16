# **1. Introducción: ¿Qué Es Git?**

**Git** es un sistema de control de versiones distribuido.  
Permite registrar los cambios en el código fuente, volver a versiones anteriores, y trabajar en equipo sin sobrescribir el trabajo de otros.

**Características clave:**

- Seguimiento de cambios (versionamiento histórico del código)
    
- Trabajo distribuido (cada usuario tiene una copia completa del repositorio)
    
- Ramas (branches) para desarrollo paralelo
    
- Fusión (merge) y resolución de conflictos

**Commando base:** todo en Git se ejecuta desde la terminal o desde clientes como Git Bash o terminales integradas en VS Code.

## **Como Guarda Git Nuestro historial**

Git no guarda los archivos completos cada vez que haces un cambio, sino que **registra las diferencias (deltas)** entre versiones.  
Esto lo hace extremadamente eficiente y rápido para manejar proyectos grandes.

### **1. Instantáneas (Snapshots), no Versiones completas**

Cada vez que haces un `commit`, Git **toma una instantánea del estado de tus archivos** y guarda referencias a esos archivos.  
Si un archivo no ha cambiado, Git **no lo vuelve a guardar**, solo crea un enlace al archivo anterior.

Imagina que es como tomar una photo del proyecto en un memento específico:

- Cada commit es una “photo” del proyecto.
    
- Git recuerda qué archivos cambiaron desde la última vez.

### **2. Estructura Interna: Objetos**

Git organiza la información en una base de datos interna llamada **objeto Git**, que contiene cuatro tipos de elementos principales:

|Tipo de Objeto|Descripción|
|---|---|
|**Blob**|Contiene el contenido de un archivo (sin nombre).|
|**Tree**|Guarda la estructura de carpetas y nombres de archivos.|
|**Commit**|Registra una versión del proyecto: author, mensaje y referencia al _tree_ correspondiente.|
|**Tag**|Marca un commit importante (por ejemplo, una versión estable).|

Cada uno de estos objetos se identifica con un **hash SHA-1**, una huella única que asegura la integridad del historial.

### **3. Cadena De commits**

Cada commit **apunta al commit anterior**, formando una cadena continua de historial.  
Por ejemplo:

```Python
A → B → C → D
```

Si haces un cambio y haces `git commit`, Git crea un nuevo nodo (D) que apunta al anterior (C).  
Esto permite moverte hacia atrás en el tiempo con commandos como:

```bash
git log
git checkout <commit_id>
```

### **4. Ventaja Del Modelo De Git**

- Permite reconstruir el historial completo sin depender del servidor.
    
- Garantiza integridad: cada cambio tiene una huella única.
    
- Facilita trabajar con ramas y fusionar sin perder el contexto.

En resumen, **Git guarda tu proyecto como una cadena de instantáneas comprimidas y verificadas**, lo que lo hace seguro, rápido y perfecto para trabajar de forma colaborativa.

---

# **2. ¿Qué Es GitLab?**

**GitLab** es una plataforma basada en Git que combina:

- Repositorios remotos
    
- Integración y entrega continua (CI/CD)
    
- Gestión de incidencias, revisiones de código, y pipelines

**Git vs GitLab:**

- Git → herramienta local de control de versiones.
    
- GitLab → servicio web que aloja repositorios Git y facilita la colaboración.

**Ejemplo:** GitHub, Bitbucket, y GitLab son servicios distintos que usan Git como base.

---

# **3. Recomendaciones De entorno**

Para mejorar tu experiencia con Git en terminal:

- **Usar Git Bash** (Windows) o una terminal con soporte de Unix.
    
- **Usar Zsh** (Z shell) — una shell avanzada que soporta autocompletado, resaltado de sintaxis y alias personalizados. 
    
- **Oh My Zsh** o **Oh My Posh** — framework que mejora Zsh y muestra información útil como:
    
    - La rama actual (`main`, `feature/login`, etc.)
        
    - Estado del repositorio (cambios, commits pendientes)
        
    - Indicadores visuals de conflictos o errores

 **Recomendación:** Instalar `oh-my-zsh` o `oh-my-posh` con el tema `agnoster` o `powerlevel10k`.

---

# **4. Configuración De Acceso SSH a GitLab**

Esto permite conectarte a GitLab sin ingresar tu usuario/contraseña cada vez.

## Pasos

1. **Generar una clave SSH**

```bash
    ssh-keygen -t RSA -C "tu_email@empresa.com"
    ```
    
    (Presiona Enter para aceptar la ruta por defecto y asigna una passphrase opcional.)
    
2. **Iniciar el agente SSH y agregar tu clave**
    
    ```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```

> [!note] add open ssh options
2. **Copiar la clave pública**
    
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    
3. **Agregarla en GitLab**  
    Entra a **GitLab → Preferences → SSH Keys → Add key** y pega tu clave pública.
    
4. **Probar conexión**
    
```bash
ssh -T git@192.168.1.221
```

 Si todo va bien, verás un mensaje de bienvenida.

---

## **5. Los 10 Commandos Más Usados En Git**

---

### **1. `git status`**

**Muestra el estado actual del repositorio.**  
Permite ver archivos modificados, en staging o sin seguimiento.

 _Ejemplo:_

```bash
git status
```

---

## **2️. `git log`**

## Historial De Commits – `git log`

### Qué Hace

Muestra el historial de confirmaciones (commits) del repositorio, incluyendo author, fecha, mensaje y cambios realizados.

### Commando Básico

```bash
git log
```

Muestra:

- Hash del commit
    
- Author y fecha
    
- Mensaje descriptivo

### Vista Compacta

```bash
git log --oneline
```

Cada commit se muestra en una sola línea.  
Ideal para una visión rápida del historial.

Consejo: combínalo con `--graph` para visualizar la estructura de ramas.

### Estructura Visual Del Proyecto

```bash
git log --oneline --graph --decorate
```

Muestra:

- Ramas y merges (`--graph`)
    
- Etiquetas y referencias (`--decorate`)

Permite entender la relación entre ramas y commits.

### Ver Cambios Realizados

```bash
git log -p
```

Muestra los cambios línea por línea (diffs) de cada commit.

Para un archivo específico:

```bash
git log -p <archivo>
```

### Filtrado De Commits

| Opción            | Ejemplo                        | Descripción                   |
| ----------------- | ------------------------------ | ----------------------------- |
| Últimos N commits | `git log -n 5`                 | Muestra los últimos 5 commits |
| Por author        | `git log --author="Miguel"`    | Filtra commits por author     |
| Por palabra clave | `git log --grep="login"`       | Busca en mensajes de commit   |
| Por fecha         | `git log --since="2025-11-01"` | Muestra desde cierta fecha    |

### Historial Global De Todas Las Ramas

```bash
git log --oneline --graph --decorate --all
```

Muestra el historial completo del repositorio, incluyendo todas las ramas locales y remotas.

---

## **3. `git add`**

El commando `git add` se utilize para **agregar archivos o cambios al área de _staging_** (zona de preparación).  
Esto significa que los cambios seleccionados quedan listos para set incluidos en el próximo _commit_, pero aún no se guardan de forma definitiva en el historial del repositorio.

Cuando se modifica, crea o elimina un archivo en el directorio de trabajo, Git lo considera un _cambio pendiente_.  
El commando `git add` permite seleccionar qué cambios serán incluidos en el siguiente commit.

### Ejemplo Básico

```bash
git add .
```

Agrega **todos los archivos modificados, nuevos o eliminados** en el proyecto al área de staging.

```bash
git add nombre_archivo
```

Agrega **un archivo específico** al área de staging.

---

### Qué Hace Realmente

- Toma una **instantánea de los cambios** actuales de los archivos seleccionados.
    
- Los mueve del **directorio de trabajo** al **área de preparación (staging area)**.
    
- El commit posterior solo incluirá los archivos que fueron agregados con `git add`.

Por ejemplo:

```bash
git add index.html
git commit -m "Actualiza la estructura del HTML"
```

Solo los cambios en `index.html` serán parte del commit, aunque haya modificaciones en otros archivos.

### Commandos Adicionales Útiles De `git add`

**1. Agregar de forma interactiva**

```bash
git add -i
```

Abre un menú interactivo que permite **elegir qué archivos o partes de archivos agregar** al staging.  
Es útil para revisar los cambios antes de incluirlos en el commit.

**2. Agregar partes específicas de un archivo**

```bash
git add -p
```

Permite **seleccionar fragmentos de código (hunks)** dentro de un archivo modificado.  
Ideal para incluir solo ciertos cambios y dejar otros pendientes.

**3. Actualizar solo los archivos ya rastreados**

```bash
git add -u
```

Agrega al staging únicamente los **archivos que ya están bajo seguimiento** (tracked) y que fueron modificados o eliminados,  
sin incluir nuevos archivos.

### Resumen De Usos Comunes

|Commando|Descripción|
|---|---|
|`git add .`|Agrega todos los cambios (nuevos, modificados y eliminados)|
|`git add <archivo>`|Agrega un archivo específico|
|`git add -p`|Agrega partes seleccionadas de un archivo|
|`git add -u`|Agrega solo archivos rastreados modificados o eliminados|
|`git add -i`|Modo interactivo para seleccionar archivos o fragmentos|

---

## **4. `git commit`**

El commando `git commit` se utilize para **guardar los cambios que han sido agregados al área de staging** en el historial local del repositorio.  
Cada _commit_ representa un punto en el tiempo del proyecto, con un mensaje descriptivo que explica los cambios realizados.  
Es el paso donde los cambios preparados con `git add` se consolidan oficialmente en la línea de tiempo del repositorio.

Un _commit_ contiene:

- Una referencia única (hash) que lo identifica.
    
- Información del author y la fecha.
    
- Un mensaje que describe los cambios.
    
- Un registro de los archivos modificados y su contenido.

### Ejemplo Básico

```bash
git commit -m "Mensaje descriptivo del cambio"
```

Este commando crea un nuevo commit con todos los archivos en el área de staging y el mensaje indicado.  
El mensaje debe set claro y conciso, explicando **qué se cambió y por qué**.

Ejemplo de buenas prácticas:

```bash
git commit -m "Corrige validación de formularios en la vista de registro"
```

### Qué Hace Realmente

1. Toma los archivos que fueron añadidos con `git add`.
    
2. Los guarda como una nueva versión en el historial del repositorio.
    
3. Asocia un mensaje de descripción para identificar el propósito de los cambios.

Una vez hecho el commit, esos cambios pasan a formar parte del historial local, pero **aún no se envían al repositorio remoto** (para eso se usa `git push`).

### Commandos Adicionales Útiles De `git commit`

**1. Crear un commit con todos los cambios sin usar `git add` previamente**

```bash
git commit -a -m "Actualiza configuración del entorno"
git commit -am "Actualiza configuración del entorno"
```

Agrega y confirma automáticamente todos los archivos modificados que ya están siendo rastreados por Git.  
No incluye archivos nuevos no agregados previamente con `git add`.

**2. Modificar el último commit**

```bash
git commit --amend
```

Permite **editar el mensaje** del último commit o **agregar archivos adicionales** que se olvidaron de incluir.  
El historial se reescribe, por lo que se debe usar con precaución si el commit ya fue compartido con otros.

**3. Realizar un commit vacío (sin cambios en archivos)**

```bash
git commit --allow-empty -m "Inicia nueva fase del proyecto"
```

Crea un commit sin modificaciones en los archivos.  
Se usa para marcar hitos, registrar eventos o ejecutar procesos automatizados (por ejemplo, un despliegue).

### Resumen De Usos Comunes

| Commando                                | Descripción                                     |
| --------------------------------------- | ----------------------------------------------- |
| `git commit -m "mensaje"`               | Crea un commit con mensaje                      |
| `git commit -a -m "mensaje"`            | Agrega y confirma todos los archivos rastreados |
| `git commit --amend`                    | Modifica el último commit                       |
| `git commit --allow-empty -m "mensaje"` | Crea un commit sin cambios en los archivos      |

En resumen, `git commit` es la acción que consolida los cambios en el historial del proyecto, permitiendo mantener un registro organizado, claro y recuperable de la evolución del código.

Sugiero instalar un paquete con node llamado Better Commits en el entorno y con un commando podemos reducir y standardizer los commits 

https://github.com/Everduin94/better-commits

```bash
npm install -g better-commits
```

### Tabla De Prefijos De Commits

|Prefijo|Descripción|Cuándo usarlo|
|---|---|---|
|**feat**|Nueva funcionalidad o característica.|Cuando agregas una nueva función, módulo, componente o comportamiento al proyecto.|
|**wip**|Trabajo en progreso (_Work in Progress_).|Para cambios que aún no están listos para producción, pero deseas guardar tu progreso.|
|**fix**|Corrección de errores.|Cuando solucionas un bug o comportamiento incorrecto en el código existente.|
|**docs**|Cambios en la documentación.|Cuando actualizas, agregas o corriges archivos de documentación (README, guías, comentarios, etc.).|
|**refactor**|Reestructuración del código sin cambiar su comportamiento.|Cuando mejoras la legibilidad, organización o mantenibilidad del código sin modificar su funcionalidad.|
|**perf**|Mejora de rendimiento.|Cuando optimizas el código para hacerlo más rápido o eficiente sin alterar su resultado.|
|**test**|Pruebas agregadas o modificadas.|Cuando creas, corriges o mejoras pruebas unitarias, de integración o de extremo a extremo.|
|**build**|Cambios en el sistema de construcción o dependencias externas.|Cuando modificas scripts de compilación, actualizas dependencias o cambias la configuración del entorno de build.|
|**ci**|Cambios en la integración continua.|Cuando modificas archivos de configuración o scripts relacionados con CI/CD (GitHub Actions, Jenkins, GitLab CI, etc.).|
|**chore**|Tareas menores de mantenimiento.|Cuando realizas tareas que no afectan el código fuente ni las pruebas (limpieza, actualización de metadatos, etc.).|
|**style**|Cambios de formato o estilo del código.|Cuando corriges sangrías, espacios, comillas o cualquier detalle de formato que no cambia la lógica del código.|
|**revert**|Reversión de un commit anterior.|Cuando deshaces los cambios introducidos por un commit anterior.|
|**merge**|Fusión de ramas o resolución de conflictos.|Cuando haces un merge entre ramas o resuelves conflictos de código.|
|**init**|Inicialización o configuración del proyecto.|Para el commit inicial del repositorio o cuando configuras la estructura base del proyecto.|

---

¿Quieres que te genere una **versión Markdown** lista para pegar en un README (con formato de tabla compatible con GitHub) o una **tabla en PowerPoint/PDF** para incluir en una presentación de Git?

---

## **5. `git diff`**

El commando `git diff` se utilize para **comparar los cambios entre versiones de archivos o commits**.  
Permite ver exactamente qué líneas fueron agregadas, modificadas o eliminadas en el código.  
Es una herramienta clave para revisar los cambios antes de hacer un commit o para analizar la evolución de un archivo en el historial del repositorio.

### Ejemplo Básico

```bash
git diff
```

Muestra las diferencias entre el **directorio de trabajo** y el **área de staging (staged changes)**.  
En otras palabras, enseña los cambios que todavía **no han sido agregados con `git add`**.

```bash
git diff HEAD~1
```

Compara el estado actual del proyecto con el commit anterior (`HEAD~1`).  
Esto permite visualizar qué se ha modificado desde la última confirmación.

### Qué Hace Realmente

`git diff` analiza las líneas de código y genera un resultado que indica:

- `+` para líneas agregadas
    
- `-` para líneas eliminadas
    
- Sin prefijo para líneas sin cambios

De esta forma puedes revisar el detalle de los cambios antes de incluirlos en el historial del repositorio con un commit.

### Commandos Adicionales Útiles De `git diff`

""

**1. Comparar el área de staging con el último commit**

```bash
git diff --staged
```

Muestra los cambios que **ya fueron agregados al área de staging**, comparados con el último commit.  
Sirve para revisar qué se incluirá exactamente en el próximo commit antes de confirmarlo.

**2. Comparar dos commits específicos**

```bash
git diff <commit1> <commit2>
```

Compara los cambios entre dos versiones del proyecto.  
Por ejemplo:

```bash
git diff a1b2c3d e4f5g6h
```

Mostrará las diferencias entre esos dos commits, permitiendo analizar qué cambió entre versiones.

**3. Ver diferencias en un archivo específico**

```bash
git diff <ruta/al/archivo>
```

Muestra los cambios dentro de un solo archivo.  
Es útil para revisar una modificación puntual sin distraerse con otros archivos.

### Resumen De Usos Comunes

| Commando                       | Descripción                                          |
| ------------------------------ | ---------------------------------------------------- |
| `git diff`                     | Muestra los cambios no agregados al staging          |
| `git diff --staged`            | Compara los cambios del staging con el último commit |
| `git diff HEAD~1`              | Compara el trabajo actual con el commit anterior     |
| `git diff <commit1> <commit2>` | Compara dos commits específicos                      |
| `git diff <archivo>`           | Muestra las diferencias en un archivo concreto       |

En resumen, `git diff` es una herramienta fundamental para **inspeccionar y revisar cambios de código**, ayudando a confirmar que las modificaciones sean correctas antes de agregarlas al historial del proyecto.

---

## **6. `git switch` | `git branch`**

Estos commandos se utilizan para **trabajar con ramas (branches)** en Git.  
Las ramas permiten desarrollar nuevas funcionalidades, corregir errores o probar ideas sin afectar el código principal del proyecto.  
Aunque ambos commandos están relacionados, tienen propósitos ligeramente distintos:

- `git branch` se usa principalmente para **listar, crear o eliminar ramas**.
    
- `git switch` se usa para **moverse entre ramas existentes o crear y cambiar a una nueva** de forma más simple y moderna.

### Ejemplo Básico Con `git switch`

```bash
git switch main
git switch -c nueva-rama
```

- `git switch main` cambia la rama actual a `main`.
    
- `git switch -c nueva-rama` crea una nueva rama llamada `nueva-rama` y cambia a ella inmediatamente.

### Qué Hace Realmente

- Cuando cambias de rama, Git **actualiza el árbol de trabajo** (los archivos y directorios del proyecto) para que coincidan con el estado del commit más reciente en la rama seleccionada.
    
- Crear una rama nueva significa generar un nuevo apuntador (pointer) que se basa en el commit actual, permitiendo trabajar de forma aislada.

### Commandos Útiles De `git switch`

**1. Cambiar a una rama existente**

```bash
git switch nombre-de-rama
```

Cambia el contexto actual del proyecto a la rama indicada.  
Ideal para alternar entre entornos de trabajo o funcionalidades en desarrollo.

**2. Crear y cambiar a una nueva rama**

```bash
git switch -c nombre-de-rama
```

Crea una nueva rama basada en la rama actual y cambia a ella.  
La opción `-c` significa _create_.

**3. Cambiar a una rama remota**

```bash
git switch -t origin/nombre-de-rama
```

Cambia a una rama que existe en el repositorio remoto (`origin`) y crea su copia local para trabajar en ella.

**4. Podemos crear una Rama desde un commit **

```bash
$ git switch -c fixup <commitID>
Switched to a new branch 'fixup'
```

### Commandos Útiles De `git branch`

**1. Listar todas las ramas**

```bash
git branch
```

Muestra todas las ramas locales del repositorio.  
La rama actual se indica con un asterisco `*`.

**2. Crear una nueva rama sin cambiar a ella**

```bash
git branch nombre-de-rama
```

Crea una nueva rama basada en la rama actual, pero **no cambia** a ella.  
Es útil cuando se desea preparar varias ramas antes de empezar a trabajar.

**3. Eliminar una rama local**

```bash
git branch -d nombre-de-rama
```

Elimina una rama local que ya fue fusionada.  
Si deseas forzar su eliminación, usa `-D` (mayúscula).

### Comparación Entre `git switch` Y `git branch`

|Acción|Commando con `git switch`|Commando con `git branch`|Descripción|
|---|---|---|---|
|Listar ramas|—|`git branch`|Muestra las ramas locales|
|Crear nueva rama|`git switch -c nueva-rama`|`git branch nueva-rama`|Crea una nueva rama|
|Cambiar de rama|`git switch nombre-de-rama`|`git checkout nombre-de-rama` (antes)|Cambia el contexto del proyecto|
|Crear y cambiar a una rama nueva|`git switch -c nueva-rama`|`git checkout -b nueva-rama` (antes)|Crea y cambia en un solo paso|
|Eliminar una rama|—|`git branch -d nombre-de-rama`|Borra una rama local|
|Trabajar con ramas remotas|`git switch -t origin/rama`|`git branch -r` para listar y `git checkout -t origin/rama` para cambiar|Gestiona ramas remotas|

---

En resumen, `git switch` es una forma **más moderna y sencilla** de cambiar o crear ramas, mientras que `git branch` sigue siendo útil para **gestionar y listar ramas existentes**.  
Ambos se complementan para un flujo de trabajo eficiente en proyectos con múltiples líneas de desarrollo.

---

## **7. `git merge`**

**Combina los cambios de una rama en otra.**

El commando `git merge` se utilize para **integrar el contenido de una rama en la rama actual**. Es una de las operaciones más comunes en Git, ya que permite incorporar el trabajo de diferentes ramas dentro del flujo principal del proyecto, como `main` o `develop`.

Cuando ejecutas `git merge`, Git analiza los historiales de commits de ambas ramas y los combina. Si las modificaciones no entran en conflicto, Git fusiona automáticamente los cambios. Si hay conflictos (por ejemplo, dos ramas modifican la misma línea de un archivo), se require resolverlos manualmente.

**Ejemplo básico:**

```bash
git merge feature/login
```

Este commando toma los cambios de la rama `feature/login` y los fusiona en la rama actual.

---

### Qué Hace Realmente

- Fusiona los commits de una rama en otra sin perder historial.
    
- Crea un nuevo commit de tipo **"merge commit"** que documenta la unión de ambas ramas.
    
- Si existen conflictos, Git marca los archivos involucrados y require intervención manual para resolverlos antes de completar la fusión.

---

### Commandos Útiles De `git merge`

**1. Fusionar una rama específica**

```bash
git merge nombre-de-rama
```

Une los cambios de la rama indicada con la rama actual.  
Debe ejecutarse desde la rama en la que quieres recibir los cambios.

**2. Fusionar sin crear un commit automático**

```bash
git merge --no-commit nombre-de-rama
```

Realiza la fusión, pero detiene el proceso antes de crear el commit de merge, permitiéndote revisar o modificar los cambios antes de confirmarlos.

**3. Fusionar sin advance rápido (no fast-forward)**

```bash
git merge --no-ff nombre-de-rama
```

Crea siempre un nuevo commit de fusión, incluso si la fusión podría hacerse con fast-forward.  
Esto mantiene el historial de la rama fusionada visible en el registro.

### ¿Qué Es Un _fast-forward_?

Un **fast-forward** (advance rápido) ocurre cuando la rama actual no ha tenido nuevos commits desde que se creó la rama que se desea fusionar.  
En ese caso, Git **no necesita crear un nuevo commit de fusión**, simplemente **mueve el puntero** de la rama actual al último commit de la rama fusionada.

**Ejemplo:**

Supongamos que estás en la rama `main` y creas una rama `feature` desde ella.  
Si trabajas únicamente en `feature` y luego haces un merge a `main`, Git puede simplemente avanzar el puntero de `main` para que apunte al mismo commit que `feature`.

`# Ejemplo de fast-forward git checkout main git merge feature`

En este caso, Git no crea un commit adicional, porque no hay divergencia entre las ramas.

**Ventajas del fast-forward:**

- Mantiene el historial lineal y limpio.
    
- Evita commits de fusión innecesarios.

**Desventajas:**

- Se pierde la referencia visual de que los cambios provinieron de una rama independiente.
    
- Puede dificultar la lectura del historial cuando se manejan muchas ramas de desarrollo.

Por eso, cuando se quiere preservar la estructura del trabajo colaborativo o el contexto de una funcionalidad, se recomienda usar la opción `--no-ff`.

---

### Tipos De Fusiones En Git

|Tipo de merge|Descripción|Resultado|
|---|---|---|
|**Fast-forward**|Ocurre cuando la rama base no tiene commits nuevos desde que se creó la rama a fusionar. Git simplemente avanza el puntero de la rama.|No crea un commit de merge.|
|**No fast-forward (`--no-ff`)**|Crea un nuevo commit de merge, manteniendo la historia de ambas ramas separada y más clara.|Se conserva la estructura de desarrollo.|
|**Con conflictos**|Sucede cuando ambas ramas modifican las mismas líneas o archivos.|Require resolución manual antes de confirmar.|

---

### Buenas Prácticas

- Antes de fusionar, ejecutar `git fetch` o `git pull` para tener la versión más reciente del repositorio.
    
- Realizar la fusión en una rama de integración o pruebas antes de unir con `main`.
    
- Usar `--no-ff` cuando se desea mantener el historial de desarrollo de una funcionalidad completo y claro.

---

## **8️. `git remote`**

**Gestiona las conexiones a repositorios remotos.**

Permite conectar tu repositorio local con uno remoto (por ejemplo GITLAB ).  
Esto facilita sincronizar cambios, subir commits y colaborar con otros desarrolladores.

**Ejemplo básico:**

```bash
git remote -v
git remote add origin git@gitlab.com:usuario/proyecto.git
```

El commando `git remote -v` muestra los repositorios remotos configurados y sus URLs.  
El commando `git remote add` agrega un nuevo repositorio remoto con un nombre (como `origin`) y su dirección.

### Commandos Comunes De `git remote`

**1. Ver los repositorios remotos configurados**

```bash
git remote -v
```

Muestra todos los repositorios remotos y sus URLs asociadas, tanto para `fetch` (obtener) como para `push` (enviar cambios).

**2. Agregar un nuevo remoto**

```bash
git remote add nombre_remoto URL
```

Agrega un nuevo origen remoto. Por convención, el nombre más común es `origin`.

**3. Eliminar un remoto**

```bash
git remote remove nombre_remoto
```

Elimina una conexión remota. Esto no borra el repositorio remoto, solo desvincula la referencia local.

**4. Cambiar la URL de un remoto**

```bash
git remote set-url origin nueva_URL
```

Actualiza la URL asociada a un remoto. Es útil si cambias de HTTPS a SSH o si el repositorio cambia de ubicación.

**5. Mostrar información detallada de un remoto**

```bash
git remote show origin
```

Muestra información completa del remoto, incluyendo las ramas configuradas para `fetch` y `push`, y su estado.

### Tabla De Commandos De `git remote`

| Commando                        | Descripción                                     | Uso común                                                 |
| ------------------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| `git remote -v`                 | Lista todos los repositorios remotos y sus URLs | Ver conexiones actuales                                   |
| `git remote add origin URL`     | Agrega un nuevo repositorio remoto              | Conectar un proyecto local a GitLab o GitHub              |
| `git remote remove nombre`      | Elimina un remoto configurado                   | Quitar un origen remoto no utilizado                      |
| `git remote set-url origin URL` | Cambia la URL de un remoto existente            | Actualizar conexión por cambio de protocolo o repositorio |
| `git remote show origin`        | Muestra información detallada del remoto        | Consultar ramas de seguimiento y configuración            |
|                                 |                                                 |                                                           |

---

## **9️. `git pull | git fetch`**

**Descarga y combina los cambios más recientes del repositorio remoto.**

Estos commandos permiten mantener tu repositorio local sincronizado con el remoto.  
La diferencia principal es que `git pull` **descarga y fusiona** los cambios automáticamente, mientras que `git fetch` **solo descarga** los cambios para revisarlos antes de aplicarlos.

**Ejemplo básico:**

```bash
git pull origin main
```

Descarga los últimos commits de la rama `main` del repositorio remoto `origin` y los combina con la rama actual.

### Commandos Comunes De `git pull`

**1. Actualizar la rama actual desde el remoto**

```bash
git pull
```

Descarga y fusiona los cambios de la rama remota correspondiente a la rama actual.

**2. Traer cambios de una rama específica**

```bash
git pull origin develop
```

Actualiza la rama actual con los últimos commits de la rama `develop` del remoto `origin`.

**3. Fusionar sin fast-forward**

```bash
git pull --no-ff
```

Crea un commit de fusión incluso si podría hacerse con fast-forward, preservando el historial de ramas.

---

### Commandos Comunes De `git fetch`

**1. Descargar cambios sin fusionar**

```bash
git fetch
```

Descarga todas las actualizaciones del repositorio remoto, pero **no modifica** tu rama actual.  
Permite revisar los cambios antes de integrarlos.

**2. Descargar una rama específica**

```bash
git fetch origin feature/login
```

Descarga los commits más recientes solo de la rama `feature/login`.

**3. Eliminar referencias obsoletas**

```bash
git fetch --prune
```

Limpia las ramas remotas que fueron eliminadas en el servidor.

---

### Tabla Comparativa Entre `git pull` Y `git fetch`

|Commando|Acción principal|Modifica el historial local|Ideal para|
|---|---|---|---|
|`git pull`|Descarga y fusiona automáticamente los cambios remotos|Sí|Actualizar rápidamente una rama en trabajo|
|`git fetch`|Descarga los cambios sin fusionar|No|Revisar o comparar cambios antes de aplicarlos|
|`git fetch --prune`|Descarga actualizaciones y limpia ramas obsoletas|No|Mantener el repositorio local sincronizado con el remoto|
|`git pull --no-ff`|Descarga y fusiona preservando el historial de ramas|Sí|Mantener trazabilidad clara de las ramas fusionadas|

---

## **10. `git push`**

**Envía tus commits locales al repositorio remoto.**

Este commando se utilize para **subir los cambios confirmados (commits)** desde tu repositorio local hacia un repositorio remoto (por ejemplo, GitLab o GitHub).  
Permite compartir el trabajo con otros colaboradores y mantener sincronizadas las ramas.

**Ejemplo básico:**

```bash
git push origin feature/nueva-funcionalidad
```

Envía los commits de la rama local `feature/nueva-funcionalidad` al repositorio remoto `origin`.

### Commandos Comunes De `git push`

**1. Subir cambios de la rama actual**

```bash
git push
```

Envía los commits de la rama activa al remoto configurado por defecto.  
Ideal cuando ya se estableció un seguimiento con `git push -u`.

**2. Subir una rama específica**

```bash
git push origin main
```

Envía los cambios locales de la rama `main` al remoto `origin`.  
Se usa comúnmente para sincronizar el trabajo principal del proyecto.

**3. Establecer seguimiento entre ramas**

```bash
git push -u origin develop
```

Envía la rama `develop` al remoto y crea un enlace de seguimiento entre la rama local y la remota.  
Esto permite que futuros `git pull` y `git push` se ejecuten sin especificar el remoto ni la rama.

**4. Eliminar una rama remota**

```bash
git push origin --delete feature/old-branch
```

Elimina una rama en el repositorio remoto.  
Útil cuando una rama ya fue fusionada o no se necesita más.

**5. Forzar el envío de cambios**

```bash
git push --force
```

Sobrescribe los cambios remotos con la versión local.  
Debe usarse con precaución, ya que puede eliminar commits de otros colaboradores.

### Tabla De Commandos De `git push`

|Commando|Descripción|Uso común|
|---|---|---|
|`git push`|Envía los commits de la rama actual al remoto configurado|Sincronizar rápidamente la rama activa|
|`git push origin main`|Envía una rama específica al remoto|Subir cambios a la rama principal|
|`git push -u origin nombre_rama`|Crea una rama remota y establece su seguimiento|Configurar nueva rama remota|
|`git push origin --delete nombre_rama`|Elimina una rama remota|Limpiar ramas ya fusionadas o antiguas|
|`git push --force`|Fuerza la actualización del remoto|Reescribir historial (con precaución)|

---

# **6. Commando Especial: `git bisect`**

**Permite encontrar el commit exacto que introdujo un error** utilizando un proceso de búsqueda binaria sobre el historial de commits.  
Este commando es muy útil cuando un proyecto ha comenzado a fallar y se desconoce en qué memento exacto se introdujo el error.

**Ejemplo básico:**

```bash
git bisect start
git bisect bad                # commit donde el error existe
git bisect good <commit_id>   # último commit conocido como bueno
```

Git seleccionará un punto intermedio entre ambos commits (el bueno y el malo) y te pedirá probar si el error está presente o no.  
Deberás ejecutar tus pruebas o revisar el comportamiento del código, y luego marcar el resultado:

```bash
git bisect good   # si el commit funciona correctamente
git bisect bad    # si el commit falla
```

Este proceso se repetirá automáticamente hasta que Git determine el **commit exacto que introdujo el error**.  
Finalmente, puedes salir del modo bisect con:

```bash
git bisect reset
```

## Commandos Comunes De `git bisect`

**1. Iniciar el proceso de búsqueda**

```bash
git bisect start
```

Comienza una sesión de búsqueda binaria para identificar el commit con error.

**2. Marcar el commit con error**

```bash
git bisect bad
```

Indica el commit actual como defectuoso.

**3. Marcar un commit funcional**

```bash
git bisect good <commit_id>
```

Indica que ese commit no contiene el error, estableciendo el punto de referencia “bueno”.

**4. Automatizar el proceso con pruebas**

```bash
git bisect run <script_de_pruebas>
```

Permite ejecutar automáticamente un script que determine si un commit es “bueno” o “malo”.  
Ideal para proyectos con pruebas automatizadas.

**5. Finalizar la sesión**

```bash
git bisect reset
```

Regresa el repositorio al estado original antes de iniciar `git bisect`.

## Tabla De Commandos De `git bisect`

|Commando|Descripción|Uso común|
|---|---|---|
|`git bisect start`|Inicia una sesión de búsqueda binaria|Comenzar el análisis del error|
|`git bisect bad`|Marca el commit actual como defectuoso|Indicar el punto donde aparece el bug|
|`git bisect good <commit_id>`|Define el último commit sin error|Establecer el límite inferior de la búsqueda|
|`git bisect run <script>`|Automatiza la verificación de commits|Usar pruebas automáticas para detectar errores|
|`git bisect reset`|Finaliza la búsqueda y restaura el estado original|Salir del modo bisect y continuar trabajando|

---

# **7. Conclusión Y Buenas prácticas**

- Usa ramas (`feature/`, `hotfix/`) para mantener tu código organizado.
    
- Haz commits pequeños y con mensajes claros.
    
- Sincroniza constantemente con `git pull` para evitar conflictos.
    
- Configura tu entorno con Zsh y Oh My Zsh para trabajar más cómodo.
    
- Usa SSH para conexiones seguras y sin contraseñas repetitivas.
