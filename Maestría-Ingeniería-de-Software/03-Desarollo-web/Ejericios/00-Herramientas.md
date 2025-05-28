# Herramientas Necesarias Paso a Paso

---

## 1. Node.js Y Npm

**¿Para qué sirve?**

- Node.js permite ejecutar JavaScript en tu computadora.
    
- npm (viene con Node) es el gestor de paquetes que necesitas para instalar React y librerías.

**¿Cómo instalarlo?**

1. Ve a [https://nodejs.org/](https://nodejs.org/)
    
2. Descarga la versión **LTS (recomendada)**.
    
3. Instala como cualquier programa.

**Verifica instalación:**

```bash
node -v
```

---

## 2. Visual Studio Code (VS Code)

**¿Para qué sirve?**  
Es el editor de código más usado por desarrolladores web.  
Tiene muchas extensions útiles para React y JavaScript.

**¿Cómo instalarlo?**

1. Descárgalo desde: [https://code.visualstudio.com/](https://code.visualstudio.com/)
    
2. Instala normalmente.

---

### Extensions Recomendadas

---

### 2.1 ESLint

**¿Qué hace?**  
Revisa tu código automáticamente y detecta errores o malas prácticas en JavaScript/React.

**Beneficios:**

- Evita errores comunes al programar.
    
- Te muestra advertencias en tiempo real.
    
- Mejora la calidad del código.

**Ejemplo:**  
Si olvidas un `;` o escribes `==` en vez de `===`, ESLint te avisará con una línea amarilla o roja.

> 💡 _Tip:_ Es como un corrector ortográfico… ¡pero para tu código!

---

### 2.2 Prettier

**¿Qué hace?**  
Da formato automático a tu código, para que se vea limpio, ordenado y consistente.

**Beneficios:**

- Corrige automáticamente la indentación.
    
- Ordena comillas, espacios, saltos de línea, etc.
    
- Evita discusiones sobre estilo de código.

**Ejemplo:**

Escribes esto:

```js
function hola() {console.log( "hola mundo" );}
```

Y al guardar, se convierte en:

```js
function hola() {
  console.log("hola mundo");
}
```

> 💡 _Tip:_ Trabaja muy bien junto con ESLint.

---

### 2.3 React Snippets

**¿Qué hace?**  
Permite escribir menos código usando atajos.

**Beneficios:**

- Crea estructuras completas con pocos caracteres.
    
- Ideal para components funcionales.

**Ejemplo:**  
Escribes:

```js
rafce
```

Y se convierte automáticamente en:

```jsx
import React from 'react';

const NombreDelComponente = () => {
  return NombreDelComponente;
};

export default NombreDelComponente;
```

> 💡 _Tip:_ Ideal cuando was a crear muchos components.

---

### 2.4 Simple React Snippets

**¿Qué es?**  
Extensión para escribir menos código repetitivo en React.

**¿Qué hace?**  
Proporciona atajos de teclado que completan automáticamente estructuras comunes.

**Ventajas:**

- Ahorra tiempo.
    
- Reduce errores de sintaxis.
    
- Útil tanto para principiantes como avanzados.

**Ejemplo de uso:**

```jsx
rafce
```

Se convierte automáticamente en:

```jsx
import React from 'react';

const NombreComponente = () => {
  return NombreComponente;
};

export default NombreComponente;
```

**Otros atajos útiles:**

- `rafce`: componente funcional exportado por defecto
    
- `usf`: useState + función
    
- `usee`: useEffect

---

### 2.5 TypeScript React Code Snippets

**¿Qué es?**  
Extensión similar a la anterior, pero para React con TypeScript (`.tsx`).

**¿Qué hace?**  
Inserta estructuras de código React con tipado TypeScript.

**Ventajas:**

- Ahorra tiempo escribiendo tipos de props o estados.
    
- Ideal para proyectos robustos y escalables.

**Ejemplo:**

```tsx
rcc
```

Se convierte en:

```tsx
import React, { Component } from 'react';

interface Props {}
interface State {}

class NombreComponente extends Component<Props, State> {
  render() {
    return NombreComponente;
  }
}
```

|Si usas…|Usa esta extensión|
|---|---|
|React con JavaScript|Simple React Snippets|
|React con TypeScript|TypeScript React Code Snippets|

---

### 2.6 GitHub Copilot

**¿Qué hace?**  
Copilot es una IA que te sugiere código automáticamente mientras escribes.

**Beneficios:**

- Ahorra tiempo proponiendo estructuras o funciones completas.
    
- Aprende del contexto y sugiere lo más probable.

**Ejemplo:**  
Empiezas a escribir `function calcularTotal` y Copilot te sugiere una función que suma precios.

> 💡 _Tip:_ Es muy útil, pero require suscripción después del periodo de prueba.

---

### ¿Cómo Instalar Las Extensions?

1. Abre Visual Studio Code
    
2. Ve a la pestaña de extensions (ícono de cuadrito a la izquierda)
    
3. Busca por nombre:
    
    - ESLint
        
    - Prettier
        
    - React snippets
        
    - GitHub Copilot
        
4. Haz clic en "Instalar"

---

## 3. Git Y GitHub

**¿Para qué sirve?**

- Git te permite guardar versiones de tu proyecto.
    
- GitHub es donde subirás tu proyecto para desplegarlo con Vercel.

**¿Cómo instalarlo?**

1. Ve a [https://git-scm.com/](https://git-scm.com/) y descarga la versión correspondiente.
    
2. Crea una cuenta en [https://github.com](https://github.com/)

**Verifica instalación:**

```bash
git --version
```

---

## 4. Configurar ESLint + Prettier En React

### Paso 1: Instala ESLint Y Prettier En Tu Proyecto

Abre la terminal en tu proyecto de React:

```bash
npm install --save-dev eslint prettier eslint-config-prettier eslint-plugin-prettier
```

Esto instala:

- `eslint`: detectar errores
    
- `prettier`: formateo de código
    
- `eslint-config-prettier`: desactiva reglas de ESLint que interfieren con Prettier
    
- `eslint-plugin-prettier`: convierte Prettier en regla ESLint

---

### Paso 2: Configura ESLint

Crea un archivo `.eslintrc.json` en la raíz del proyecto con el siguiente contenido:

```json
{
  "extends": [
    "react-app",
    "plugin:prettier/recommended"
  ],
  "rules": {
    "prettier/prettier": "error"
  }
}
```

---

### Paso 3: Crea Configuración De Prettier

Archivo `.prettierrc`:

```json
{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

---

### Paso 4: Configura VS Code Para Formatear Al Guardar

1. Abre VS Code
    
2. Ve a `Preferencias > Configuración` (Ctrl + ,)
    
3. Busca `Format On Save` y actívalo
    
4. Abre el archivo `settings.json` (Ctrl + Shift + P → `Preferences: Open Settings (JSON)`)
    
5. Agrega esto:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

---

### Paso 5: Prueba Tu Configuración

Escribe:

```js
function prueba() {console.log( "Hola Mundo" );}
```

Guarda (Ctrl + S)  
¡Se arregla automáticamente!

---

# Desarrollo De Un Front-End Utilizando React

---

## 🎯 Objetivo

Crear el front-end de una aplicación web usando **React**, **HTML5**, **CSS3** y **JavaScript**, con:

- Mínimo 10 components funcionales
    
- Rutas
    
- Hooks
    
- Estilos con BEM
    
- Despliegue en Vercel

---

## 1. Define la Idea De Tu Aplicación

Opciones sugeridas:

- Tienda online
    
- Biblioteca digital
    
- Plataforma de streaming
    
- Sistema de inventario

**Ejemplo elegido:** Tienda de camisetas

---

## 2. Crea El Proyecto React

```bash
npm install -g create-react-app
npm cache clean --force
```

> Cierra VS Code para que tome los nuevos ajustes

```bash
npx create-react-app nombreproyecto
cd tienda
npm start
```

Accede desde:

- Local: [http://localhost:3000](http://localhost:3000/)
    
- Red: [http://192.168.86.243:3000](http://192.168.86.243:3000/)

> 💡 _Tip:_ Ctrl + C detiene el servidor

📚 Recurso: [React Ya - Tutoriales](https://www.tutorialesprogramacionya.com/reactya/index.php?inicio=0)

---

## 3. Organiza la Estructura Del Proyecto

```bash
src/
├── components/    # Componentes reutilizables
├── pages/         # Vistas (Home, Detalle, etc.)
├── data/          # Datos de prueba (mock)
├── hooks/         # Custom hooks
```

---

## 4. Crea Los Components Funcionales (mínimo 10)

**Ejemplos:**

- Header
    
- Footer
    
- ProductCard
    
- ProductList
    
- ProductDetail
    
- Cart
    
- SearchBar
    
- CategoryFilter
    
- Checkout
    
- About

Todos deben estar hechos como funciones con JSX.

**Ejemplo: `components/Header.js`**

```jsx
const Header = () => {
  return <h1>Mi Tienda Geek</h1>;
};

export default Header;
```

---

¡Listo! Con esta guía formateada en Markdown, puedes trabajar cómodamente y compartir este documento como una referencia clara y professional. ¿Quieres que te lo convierta a PDF o lo suba a algún repositorio?