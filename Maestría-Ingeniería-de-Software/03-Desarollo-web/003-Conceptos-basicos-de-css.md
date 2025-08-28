
### Notas de la Sesión – Lenguaje CSS

---

#### **1. Introducción a CSS**

- **CSS** (_Cascading Style Sheets_) es un lenguaje de diseño, no de programación.
    
- Permite:
    
    - Modificar el **aspecto visual** de los elementos HTML.
        
    - Controlar **layout**, colores, tamaños, formas y estilos.
        
    - Separar la estructura (HTML) del diseño (CSS) y del comportamiento (JavaScript).
        
- Versión más reciente: **CSS3**.
    
- Regulado por el **W3C Consortium**.
    

---

#### **2. Beneficios de Usar CSS**

- Separa la **estructura** (HTML), el **diseño** (CSS) y la **dinamicidad** (JavaScript).
    
- Mejora la **mantenibilidad** de la página.
    
- Permite la creación de **temas** y la modificación de estilos desde un solo archivo.
    

---

#### **3. Sintaxis de CSS**

- **Estructura básica**:
    
    ```css
    selector {
        propiedad: valor;
    }
    ```
    
- **Ejemplo**:
    
    ```css
    p {
        color: green;
        text-align: center;
    }
    ```
    
- **Elementos clave**:
    
    - **Selector**: define a qué elemento HTML se aplican los estilos.
        
    - **Propiedades**: aspectos a modificar (color, tamaño, margen, etc.).
        
    - **Valores**: configuraciones específicas para las propiedades.
        

---

#### **4. Tipos de Selectores**

1. **Selectores Simples**
    
    - Por **ID**: `#id`
        
    - Por **Clase**: `.clase`
        
    - Por **Elemento HTML**: `p`, `h1`
        
    - **Selector universal**: `*` (aplica a todos los elementos)
        
    - **Múltiples selectores**: `h1, h4, p { ... }`
        
2. **Selectores Combinados**
    
    - **Descendencia general**: `form label` (todos los `label` dentro de `form`)
        
    - **Hijo directo**: `form > label`
        
    - **Adyacente inmediato**: `h1 + p`
        
    - **Adyacente general**: `form ~ label`
        
3. **Selectores de Pseudo-Clase**
    
    - Estilos condicionales según estado del elemento.
        
    - Ejemplo:
        
        ```css
        p:hover {
            background-color: yellow;
        }
        ```
        
4. **Selectores de Atributos**
    
    - Seleccionan elementos con atributos específicos.
        
    - Ejemplo:
        
        ```css
        p[type="code"] {
            background-color: darkgrey;
        }
        ```
        

---

## MicroTest
### Question 1

**Answer:** b.  
**Why:**

- `td[estilo="abstracto"]` → selecciona un elemento `<td>` cuyo atributo `estilo` sea “abstracto”.
    
- `+ img` → selecciona solo el elemento `<img>` que esté **inmediatamente después** de ese `<td>`.
    
- `:hover` → el estilo se aplica cuando el cursor pasa sobre la imagen.
    
- Por tanto, la sentencia aplica un borde sólido de 5 píxeles de color azul oscuro solo a las imágenes **inmediatamente posteriores** a ese `<td>` cuando se pasa el cursor sobre ellas.
    

---

### Question 2

**Answer:** d.  
**Why:**

- `td[estilo="cubico"]` → selecciona un `<td>` con atributo `estilo` igual a “cubico”.
    
- `img` → selecciona todos los elementos `<img>` que estén **dentro** de dicho `<td>`.
    
- No hay `+` ni `~`, así que no es adyacente sino descendiente directo o indirecto.
    
- Por tanto, todos los `<img>` contenidos en un `<td estilo="cubico">` tendrán borde sólido de 5 píxeles azul oscuro.
    

---

### Question 3

**Answer:** c.  
**Why:**

- Para seleccionar **hijos directos**, se usa el operador `>`, pero en el enunciado está mal descrito (lo llaman "adjacent sibling selector" que es incorrecto).
    
- `+` es para elementos **adyacentes inmediatos**, no hijos.
    
- `~` es para **hermanos generales**, no hijos.
    
- Dado que ninguna opción describe correctamente que `>` es el **child selector**, la respuesta correcta es **c. Ninguna de las opciones es correcta**.