# Notas De Estudio – Objetos Literales En JavaScript

## 1. Definición De Objeto Literal

- **Objeto literal:** Es la forma más básica y directa de definir un objeto en JavaScript.
    
- Se escribe literalmente entre llaves `{}`, con pares **clave: valor**.
    
- Puede container:
    
    - **Propiedades** (atributos con valores primitivos como cadenas, números, booleanos, etc.).
        
    - **Métodos** (funciones almacenadas como propiedades del objeto).

### Ejemplo

```js
let persona = {
  nombre: "Alis",
  edad: 30,
  saludar: function () {
    console.log("Hola, soy " + this.nombre);
  }
};
```

---

## 2. Components De Un Objeto Literal

|Componente|Descripción|Ejemplo|
|---|---|---|
|**Propiedad**|Atributo que almacena un valor.|`nombre: "Alis"`|
|**Método**|Una función dentro del objeto.|`saludar: function(){…}`|
|**`this`**|Referencia al propio objeto donde se encuentra.|`this.nombre`|

---

## 3. Uso De `this` En Objetos Literales

- `this` hace referencia al **propio objeto** donde se utilize.
    
- Permite acceder a otras propiedades del mismo objeto desde dentro de un método.

```js
saludar: function () {
  console.log("Hola, soy " + this.nombre);
}
```

➡ En este caso, `this.nombre` equivale a `persona.nombre`.

---

## 4. Acceso a Propiedades Y Métodos

Existen dos formas principales:

1. **Notación punto**

```js
console.log(persona.nombre); // "Alis"
persona.saludar(); // "Hola, soy Alis"
```

1. **Métodos del objeto global `Object`**

- `Object.keys(objeto)` devuelve un array con las claves del objeto.

```js
console.log(Object.keys(persona)); 
// ["nombre", "edad", "saludar"]
```

---

## 5. Diagrama De Relación (MermaidJS)

```mermaid
graph TD
  A[Objeto Literal persona] --> B[nombre: "Alis"]
  A --> C[edad: 30]
  A --> D[saludar()]
  D --> E["this.nombre → 'Alis'"]
```

---

## 6. Ejecución Paso a Paso Del Ejemplo

1. Se imprime el valor de `persona.nombre` → **"Alis"**.
    
2. Se ejecuta el método `persona.saludar()` → **"Hola, soy Alis"**.
    
3. Se muestran las claves con `Object.keys(persona)` → **["nombre", "edad", "saludar"]**.

---

## Resumen De Puntos Clave

- Un **objeto literal** se define con `{ clave: valor }`.
    
- Puede container **propiedades** y **métodos**.
    
- La palabra clave **`this`** referencia al propio objeto.
    
- Se accede a propiedades/métodos con **`.`** o funciones como `Object.keys()`.
    
- Son la base para trabajar con **estructuras complejas** en JavaScript.

---

## MicroTest

1. Un objeto literal puede estar compuesto por:
    
    - **La respuesta:** b. Cualquier tipo de dato válido en JavaScript.
        
    - **Justificación:** En un objeto literal se pueden incluir tipos primitivos (string, number, boolean, null, undefined, symbol, bigint) y tipos complejos (objetos, arrays, funciones). El transcript menciona que una propiedad puede set una función, lo cual confirma que no está limitado a tipos básicos.

---

1. Si una propiedad de un objeto es una función, se dice que es:
    
    - **La respuesta:** d. Un método.
        
    - **Justificación:** Cuando una función está asociada a un objeto como propiedad, se le denomina **método**. En el transcript, “saludar” es una función dentro del objeto, por lo que se considera un método del objeto.

---

1. El método `Object.keys(object)` devuelve:
    
    - **La respuesta:** a. Un array con todas las propiedades de un objeto.
        
    - **Justificación:** `Object.keys()` retorna un arreglo con las claves enumerables propias del objeto, incluyendo propiedades que sean funciones (métodos). El transcript indica que al ejecutar `Object.keys(objeto)` aparecen `nombre`, `edad` y `saludar`, lo que demuestra que incluye todos los atributos sin excluir métodos ni valores `null` o `undefined`.
      
      