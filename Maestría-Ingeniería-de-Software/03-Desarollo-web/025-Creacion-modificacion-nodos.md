# Notas De Estudio – Creación Y Eliminación De Elementos En El DOM

---

## 1. Introducción

- **Objetivo**: aprender cómo **crear** y **eliminar** elementos en un documento HTML de manera dinámica usando la **API del DOM**.
    
- **Ejemplo base**:
    
    - Documento HTML con:
        
        - Una lista (`<ul>`) con un identificador (`id="lista"`) pero inicialmente vacía.
            
        - Dos botones: **Añadir elemento** y **Eliminar elemento**.
            
        - Un script de JavaScript que contiene la lógica.

---

## 2. Preparación Del Entorno

### 2.1 Evento `DOMContentLoaded`

- Se utilize para asegurarse de que **todo el contenido del HTML esté cargado** antes de manipular el DOM.
    
- Sintaxis:

    ```js
    document.addEventListener("DOMContentLoaded", () => {
      // Código que accede y modifica el DOM
    });
    ```

### 2.2 Obtención De Referencias

- Se accede a los elementos HTML mediante su **id**:

    ```js
    const lista = document.getElementById("lista");
    const addBtn = document.getElementById("addElement");
    const removeBtn = document.getElementById("removeElement");
    ```

---

## 3. Creación Dinámica De Elementos

### 3.1 Método `createElement`

- Permite crear un nuevo nodo HTML desde JavaScript.
    
- Ejemplo:

    ```js
    const nuevoElemento = document.createElement("li");
    ```

### 3.2 Asignación De Contenido

- Se define el texto del elemento creado con `.textContent`:

    ```js
    nuevoElemento.textContent = "Nuevo elemento " + (lista.children.length + 1);
    ```

### 3.3 Inserción En El DOM

- Se usa el método **`appendChild`** para asociar el nuevo nodo al padre (`ul`):

    ```js
    lista.appendChild(nuevoElemento);
    ```

```mermaid
graph TD
    A[createElement('li')] --> B[Asignar texto]
    B --> C[appendChild(lista)]
    C --> D[Nuevo <li> en la lista]
```

---

## 4. Eliminación Dinámica De Elementos

### 4.1 Verificación Previa

- Antes de eliminar, se comprueba si la lista tiene elementos:

    ```js
    if (lista.children.length > 0) {
      // eliminar
    } else {
      alert("No hay más elementos para eliminar");
    }
    ```

### 4.2 Método `removeChild`

- Se elimina el **último hijo** de la lista:

    ```js
    lista.removeChild(lista.lastElementChild);
    ```

|Método|Función|
|---|---|
|`appendChild`|Inserta un nodo como último hijo|
|`removeChild`|Elimina un nodo hijo específico|
|`lastElementChild`|Obtiene el último hijo de tipo elemento|

---

## 5. Ejemplo Completo

### HTML Simplificado

```html
<ul id="lista"></ul>
<button id="addElement">Añadir elemento</button>
<button id="removeElement">Eliminar elemento</button>
```

### JavaScript

```js
document.addEventListener("DOMContentLoaded", () => {
  const lista = document.getElementById("lista");
  const addBtn = document.getElementById("addElement");
  const removeBtn = document.getElementById("removeElement");

  addBtn.addEventListener("click", () => {
    const nuevoElemento = document.createElement("li");
    nuevoElemento.textContent = "Nuevo elemento " + (lista.children.length + 1);
    lista.appendChild(nuevoElemento);
  });

  removeBtn.addEventListener("click", () => {
    if (lista.children.length > 0) {
      lista.removeChild(lista.lastElementChild);
    } else {
      alert("No hay más elementos para eliminar");
    }
  });
});
```

---

## 6. Ejecución Práctica

- Inicialmente la lista está vacía.
    
- Al pulsar **Añadir elemento**, se agregan elementos en orden sequential (`Nuevo elemento 1`, `Nuevo elemento 2`, etc.).
    
- Al pulsar **Eliminar elemento**, se eliminan en orden inverso.
    
- Si no hay elementos en la lista y se intenta eliminar, aparece una alerta.

---

## 7. Conceptos Adicionales Útiles

- **`.children`** → colección de los hijos de un elemento (solo nodos de tipo elemento, ignore texto).
    
- **`.lastElementChild`** → accede directamente al último hijo que sea un elemento.
    
- **Diferencia entre `childNodes` y `children`**:
    
    - `childNodes`: incluye nodos de texto (como saltos de línea).
        
    - `children`: solo incluye elementos HTML.

---

## Resumen De Puntos Clave

- Usar **`DOMContentLoaded`** asegura que el DOM esté listo antes de manipularlo.
    
- **`createElement` + `appendChild`** → crear y añadir elementos al DOM.
    
- **`removeChild` + `lastElementChild`** → eliminar elementos de una lista.
    
- **`.children`** devuelve solo elementos, evitando problemas con nodos de texto.
    
- Siempre verificar si existen elementos antes de intentar eliminarlos.

---