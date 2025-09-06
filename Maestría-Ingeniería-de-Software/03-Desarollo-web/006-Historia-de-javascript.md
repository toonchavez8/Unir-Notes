# Notas De Estudio: Introducción a JavaScript Y Entorno De Desarrollo

## 1. Historia Y Evolución De JavaScript

### Definición

**JavaScript** es un lenguaje de programación dinámico utilizado principalmente para agregar **interactividad** a páginas web y aplicaciones modernas.

### Breve Historia

- **1995:** Creado por **Brendan Eich** en la compañía Netscape.  
- Nombres originales: **Mocha → LiveScript → JavaScript** (estrategia de co-branding con Java).  
- Diferencias con Java: Aunque comparten nombre, no tienen relación técnica directa.  

### Evolución

- Inicialmente diseñado para **interactividad en navegadores web**.  
- Hoy en día, se utilize en:
  - **Aplicaciones web**
  - **Aplicaciones móviles**
  - **Videojuegos**
  - **Servidores (Node.js)**

- **2009:** Lanzamiento de **Node.js**, que permitió ejecutar JavaScript fuera del navegador.  
- **ECMAScript:** Estandarización de JavaScript para garantizar compatibilidad entre navegadores.  
  - **ES6 (2015):** Introdujo **clases, módulos, funciones flecha**, mejorando la estructura y mantenibilidad del lenguaje.

### Relevancia

JavaScript es uno de los lenguajes de programación más **populares y ampliamente usados**, esencial para el desarrollo frontend moderno.

---

## 2. Entorno De Desarrollo Para JavaScript

### Intérprete

- **Node.js**: Permite ejecutar JavaScript fuera del navegador.  
- Instalación: Descarga gratuita desde la página official de Node.js.

### Entornos De Desarrollo (IDE)

| IDE | Descripción | Comentarios |
|-----|-------------|-------------|
| **WebStorm** | IDE de JetBrains para desarrollo JavaScript | Pago, pero gratuito para estudiantes UNIR mediante Student Pack |
| **Visual Studio Code** | Editor ligero y gratuito | Alternativa recomendada si no se desea usar WebStorm |

### Crear Un Proyecto En WebStorm

1. Abrir WebStorm.  
2. Ir a `File → New → Project`.  
3. Seleccionar **Node.js** como base del proyecto.  
4. Asegurarse de que el **Intérprete de Node.js** esté instalado y configurado.  
5. Hacer click en **Create** para generar el proyecto.  

**Ejemplo de proyecto:**  
- Nombre: `Programación Global`  
- Contendrá diferentes aspectos de programación en JavaScript a lo largo del tema.

---

## 3. Conceptos Clave De JavaScript

### Características

- **Lenguaje dinámico:** Los tipos de datos pueden cambiar durante la ejecución.  
- **Orientado a objetos:** Con soporte de **clases** y **objetos** (ES6).  
- **Interactividad web:** Manejo de eventos, manipulación del DOM, animaciones.  
- **Multiplataforma:** Funciona en navegadores, servidores (Node.js) y otras plataformas.

### Diagrama Simple De Flujo De Ejecución

```Python

[Código JS en archivo .js]  
│  
▼  
[Intérprete Node.js]  
│  
▼  
[Ejecuta código y devuelve resultados]

```

### Relevancia Del Entorno

- Configurar correctamente el **IDE** y **Node.js** permite:
  - Ejecutar scripts de JavaScript localmente.  
  - Probar funcionalidades sin depender de un navegador.  
  - Desarrollar aplicaciones web y backend con un mismo lenguaje.

---

## 4. Resumen Del Tema

- **JavaScript**: Lenguaje dinámico para interactividad web y aplicaciones modernas.  
- **Node.js**: Permite ejecutar JavaScript fuera del navegador.  
- **IDE recomendados**: WebStorm (professional) o VS Code (gratuito).  
- **ES6**: Mejora la estructura y mantenibilidad con clases, módulos y funciones flecha.  
- Configurar un **proyecto Node.js** es el primer paso para comenzar a programar en JavaScript de manera professional.

---

## MicroTest

1. ¿Qué IDEs pueden set adecuados (dadas las facilidades que integran) para trabajar con JavaScript?
    
    - **La respuesta:** b. Las opciones A) y C) son correctas.
        
    - **Justificación:** En el transcript se mencionan **JetBrains WebStorm** y **Visual Studio Code** como entornos adecuados para trabajar con JavaScript, por lo que ambas son válidas. IntelliJ IDEA no se menciona.
        
2. El IDE que utilizaremos nos permite:
    
    - **La respuesta:** d. Ejecutar y depurar código JavaScript siempre que instalemos un intérprete en nuestra máquina.
        
    - **Justificación:** El transcript indica que para trabajar con JavaScript se necesita tener Node.js instalado en la máquina para ejecutar y depurar código desde el IDE.
        
3. Un código que se ejecuta de la misma forma en el intérprete local (Node JS) y en el navegador se denomina:
    
    - **La respuesta:** c. Isomórfico.
        
    - **Justificación:** El término **isomórfico** en programación se refiere a código que puede ejecutarse tanto en el servidor (Node.js) como en el navegador sin cambios.