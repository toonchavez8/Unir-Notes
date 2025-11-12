# **1. Introducción: ¿Qué Es Git?**

**Git** es un sistema de control de versiones distribuido.  
Permite registrar los cambios en el código fuente, volver a versiones anteriores, y trabajar en equipo sin sobrescribir el trabajo de otros.

**Características clave:**

- Seguimiento de cambios (versionamiento histórico del código)
    
- Trabajo distribuido (cada usuario tiene una copia completa del repositorio)
    
- Ramas (branches) para desarrollo paralelo
    
- Fusión (merge) y resolución de conflictos

**Commando base:** todo en Git se ejecuta desde la terminal o desde clientes como Git Bash o terminales integradas en VS Code.

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
    
- ⚙️ **Usar Zsh** (Z shell) — una shell avanzada que soporta autocompletado, resaltado de sintaxis y alias personalizados.
    
- **Oh My Zsh** — framework que mejora Zsh y muestra información útil como:
    
    - La rama actual (`main`, `feature/login`, etc.)
        
    - Estado del repositorio (cambios, commits pendientes)
        
    - Indicadores visuals de conflictos o errores

 **Recomendación:** Instalar `oh-my-zsh` con el tema `agnoster` o `powerlevel10k`.

---

#  **4. Configuración De Acceso SSH a GitLab**

Esto permite conectarte a GitLab sin ingresar tu usuario/contraseña cada vez.

## Pasos

1. **Generar una clave SSH**

```bash
    ssh-keygen -t ed25519 -C "tu_email@empresa.com"
    ```
    
    (Presiona Enter para aceptar la ruta por defecto y asigna una passphrase opcional.)
    
2. **Iniciar el agente SSH y agregar tu clave**
    
    ```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```
    
3. **Copiar la clave pública**
    
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    
4. **Agregarla en GitLab**  
    Entra a **GitLab → Preferences → SSH Keys → Add key** y pega tu clave pública.
    
5. **Probar conexión**
    
    ```bash
    ssh -T git@gitlab.com
    ```
    

 Si todo va bien, verás un mensaje de bienvenida.

---

##  **5. Los 10 comandos más usados en Git**

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

**Muestra el historial de commits.**

 _Ejemplo:_

```bash
git log --oneline --graph --decorate
```

 > [!tip] Consejo: usa `--oneline` para una vista compacta.

---

## **3️. `git add`**

**Agrega archivos al área de staging (preparación para commit).**

 _Ejemplo:_

```bash
git add .
# o git add nombre_archivo
```

---

## **4️. `git commit`**

**Guarda los cambios en el historial local del repositorio.**

 _Ejemplo:_

```bash
git commit -m "Mensaje descriptivo del cambio"
```

---

## **5️. `git diff`**

**Muestra diferencias entre versiones de archivos.**

 _Ejemplo:_

```bash
git diff
git diff HEAD~1
```

---

## **6️. `git switch`**

**Cambia entre ramas de trabajo o crea nuevas.**

 _Ejemplo:_

```bash
git switch main
git switch -c nueva-rama
```

---

## **7️. `git merge`**

**Combina los cambios de una rama en otra.**

 _Ejemplo:_

```bash
git merge feature/login
```

💡 Puede generar conflictos que deberán resolverse manualmente.

---

## **8️. `git remote`**

**Gestiona las conexiones a repositorios remotos.**

 _Ejemplo:_

```bash
git remote -v
git remote add origin git@gitlab.com:usuario/proyecto.git
```

---

## **9️. `git pull | git fetch`**

**Descarga y combina los cambios más recientes del repositorio remoto.**

 _Ejemplo:_

```bash
git pull origin main
```

---

## **10. `git push`**

**Envía tus commits locales al repositorio remoto.**

 _Ejemplo:_

```bash
git push origin feature/nueva-funcionalidad
```

---

# **6. Commando Especial: `git bisect`**

**Permite encontrar el commit exacto que introdujo un error** mediante búsqueda binaria en el historial.

 _Ejemplo:_

```bash
git bisect start
git bisect bad                # commit donde el error existe
git bisect good <commit_id>   # último commit conocido como bueno
```

Git irá saltando entre commits hasta encontrar el problemático.

🔍 **Ideal para depuración de bugs históricos.**

---

# **7. Conclusión Y Buenas prácticas**

- Usa ramas (`feature/`, `hotfix/`) para mantener tu código organizado.
    
- Haz commits pequeños y con mensajes claros.
    
- Sincroniza constantemente con `git pull` para evitar conflictos.
    
- Configura tu entorno con Zsh y Oh My Zsh para trabajar más cómodo.
    
- Usa SSH para conexiones seguras y sin contraseñas repetitivas.
