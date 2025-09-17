# Notas De Estudio – Tema 3: Funciones Y Programación Avanzada En JavaScript

---

## 1. Funciones En JavaScript

### Definición

- Una **función** es un bloque de código reutilizable diseñado para ejecutar una operación específica.
    
- Permite centralizar el código y evitar duplicación, mejorando **legibilidad** y **mantenibilidad**.

### Tipos De Argumentos

- **Argumentos obligatorios:** Deben proporcionarse al invocar la función.
    
- **Argumentos opcionales:** Pueden omitirse al llamar la función.
    
- **Argumentos por defecto:** Tienen un valor asignado si no se proporciona uno durante la llamada.

### Funciones Flecha

- Sintaxis más concisa para declarar funciones.
    
- Ejemplo:

```javascript
const suma = (a, b) => a + b;
```

- Características:
    
    - Menos paréntesis y corchetes.
        
    - Mantienen el mismo comportamiento que funciones tradicionales.
        
    - **No tienen su propio `this`.**

---

## 2. Callbacks

### Definición

- Una **callback** es una función que se pasa como argumento a otra función.
    
- Permite ejecutar código en un **memento específico** dentro de la función receptora.

### Ejemplo

```javascript
function procesar(entrada, callback) {
    console.log('Procesando', entrada);
    callback(entrada);
}

procesar('datos', resultado => console.log('Callback ejecutado con', resultado));
```

- Explicación paso a paso:
    
    1. `procesar` recibe un string y una función callback.
        
    2. Muestra el string.
        
    3. Ejecuta el callback con el string como argumento.

---

## 3. Funciones De Orden Superior

### Definición

- Funciones que reciben **otras funciones como argumentos** o **devuelven funciones**.
    
- Comúnmente usadas en **estructuras de datos**: arrays, sets, maps.

### Ejemplos

|Método|Descripción|Ejemplo|
|---|---|---|
|`forEach`|Itera sobre elementos de un array ejecutando un callback|`[1,2,3].forEach(n => console.log(n*2))`|
|`filter`|Filtra elementos que cumplen una condición|`[1,2,3,4].filter(n => n % 2 === 0)` devuelve `[2,4]`|
|`map`|Aplica una función a cada elemento y devuelve un nuevo array|`[1,2,3].map(n => n*2)` devuelve `[2,4,6]`|

---

## 4. Objetos Literales

### Definición

- Forma **literal y directa** de crear objetos.
    
- Compuestos por propiedades y métodos.

### Ejemplo

```javascript
const persona = {
    nombre: 'ALIS',
    edad: 30,
    saludar() {
        console.log(`Hola, soy ${this.nombre}`);
    }
};
```

- `this` referencia al propio objeto.
    
- `Object.keys(persona)` devuelve `['nombre','edad','saludar']`.

---

## 5. Promesas Y Asincronía

### Promesas

- Permiten manejar **operaciones asincrónicas**.
    
- Estados:
    
    - **Resuelta** (`resolve`)
        
    - **Rechazada** (`reject`)

### Ejemplo Básico

```javascript
function operacionAsincrona() {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve('Operación completada'), 2000);
    });
}
```

### Async / Await

- Permite escribir código **asincrónico como si fuera síncrono**.

```javascript
async function ejecutarProceso() {
    const resultado = await operacionAsincrona();
    console.log(resultado);
}
```

---

## 6. Closures

### Definición

- Una **closure** es una función que "recuerda" el entorno donde fue creada.
    
- Permite **acceder a variables de una función externa desde una función interna**.

### Ejemplo: Fábrica De Funciones

```javascript
function crearContador() {
    let contador = 0;
    return function() {
        contador++;
        console.log(contador);
    }
}

const miContador = crearContador();
miContador(); // 1
miContador(); // 2
```

- Cada closure tiene su **estado independiente**.
    
- La función externa no puede acceder a variables internas de la función interna.

---

## 7. Resumen De Conceptos Clave

- Funciones: bloques de código reutilizables.
    
- Callbacks: funciones pasadas como argumentos.
    
- Funciones de orden superior: ejecutan o devuelven otras funciones.
    
- Objetos literales: colecciones de propiedades y métodos.
    
- Promesas: manejo de operaciones asincrónicas con estados `resolve` y `reject`.
    
- Async / Await: espera de promesas de manera síncrona.
    
- Closures: funciones que recuerdan su entorno, útiles como fábricas de funciones.

---

