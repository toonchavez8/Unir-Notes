# 📘 Notas: Diagrama De Clases En UML

Las **clases** son la base de la programación orientada a objetos (POO). Representan las características comunes de los elementos en un software. Para modelar sus atributos, operaciones y relaciones, se usan los **diagrams de clases UML** (Rumbaugh, Jacobson & Booch, 2007).

---

## 1. Estructura De Una Clase

```plaintext
+-----------------------------+
|        ClassName            |
+-----------------------------+
| - atributo1 : Tipo          |
| # atributo2 : Tipo          |
| + atributo3 : Tipo          |
+-----------------------------+
| + metodo1(par: Tipo) : Tipo |
| + metodo2()                 |
+-----------------------------+
```

- **Nombre**: sustantivo en singular, claro y significativo.
    
- **Atributos**:
    
    - Sintaxis: `visibilidad nombre: Tipo`
        
    - Visibilidad:
        
        - `+` público (se recomienda exponer con getters/setters)
            
        - `#` protegido
            
        - `-` privado
            
- **Operaciones**:
    
    - Sintaxis: `visibilidad nombre(parámetros) [: TipoRetorno]`
        
    - Parámetros: `[dirección] nombre: Tipo [= valorPorDefecto]`
        
        - `in` (entrada), `out` (salida), `inout` (entrada/salida)

---

## 2. Relaciones Entre Clases

```mermaid
classDiagram
    classA --|> classB : Inheritance
    classC --* classD : Composition
    classE --o classF : Aggregation
    classG --> classH : Association
    classI --> classJ : Link (solid)
    classK ..> classL : Dependency
    classM ..|> classN : Realization
    classO .. classP : Link (dashed)
```

### 2.1 Asociación

- **Más común**: línea continua.
    
- **Unidireccional**: flecha en un extremo.
    
- **Roles y multiplicidad**:

```mermaid
classDiagram
	direction RL
    Cliente "1" --> "*" Pedido : hace
    Pedido "0..1" --> "1" Factura : genera
```

**Multiplicidades**:

|Notación|Significado|Ejemplo|
|:-:|---|---|
|`1`|Exactamente 1|Una persona tiene un único país de origen.|
|`0..1`|Cero o uno|Un empleado puede tener un responsible (o no).|
|`0..*`|Cero o más|Una persona puede tener varias direcciones.|
|`1..*`|Uno o más|Un alumno está matriculado en ≥1 asignatura.|
|`n`|Exacto n|Un segmento tiene 2 puntos (origen y destino).|

---

### 2.2 Generalización (Herencia)

- **Relación “es-un”**: subclase hereda de superclase.
    
- Se dibuja con punta triangular hueca.

```mermaid
classDiagram
    cuentaPlazoFijo --|> cuentaBancaria
    CuentaCreditoLimitado --|> cuentaBancaria
```

---

### 2.3 Agregación

- **“Todo/parte”** conceptual, partes sobreviven al todo.
    
- Rombo hueco en la clase “todo”.

```mermaid
classDiagram
	direction RL 
    Biblioteca o-- Libro : contiene
```

---

### 2.4 Composición

- Agregación fuerte: partes mueren con el todo.
    
- Rombo relleno en la clase “todo”.

```mermaid
classDiagram
		direction RL 
    Casa *-- Habitacion : contiene
```

---

### 2.5 Dependencia

- Uso puntual: cambios en proveedor afectan cliente.
    
- Línea discontinua con flecha al cliente.

```mermaid
classDiagram
	direction RL 
    Cliente ..> Servicio : utiliza
```

---

## 3. Ejemplos En Mermaid.js

### 3.1 Clase Y Atributos

```mermaid
classDiagram
    class Persona {
        - nombre : String
        - edad   : int
        + saludar() : void
        + cumplirAnios() : void
    }
```

### 3.2 Asociación Con Multiplicidad

```mermaid
classDiagram
		direction RL 
    class Persona
    class Direccion

    Persona "1" --> "0..*" Direccion : vive en
```

### 3.3 Herencia, Agregación Y Composición

```mermaid
classDiagram
    class Vehiculo
    class Coche
    class Motor
    class Rueda

    Coche --|> Vehiculo
    Coche o-- Motor
    Coche *-- Rueda : tiene 4
```

### 3.4 Dependencia Y Realización

```mermaid
classDiagram
    class Servicio
    class Cliente
    class Interfaz

    Cliente ..> Servicio
    Cliente ..|> Interfaz
```

---

> Estas notas cubren casi todos los detalles originales y añaden ejemplos prácticos en **Mermaid.js** para facilitar la comprensión y la aplicación en tus diagrams de clases.

---

## MicroTest

- Selecciona tres opciones. Los atributos son las propiedades de las clases y para cada uno se puede indicar lo siguiente:
	- Tipo
	- Visibilidad.
	- Nombre
- La visibilidad nos indica cómo pueden relacionarse las operaciones de otras clases con el atributo. Selecciona las tres opciones correctas:
	- Público (+): puede relacionarse con otras clases.
	- Protegido (#): puede relacionarse con las clases descendientes
	- Privado (-): no puede relacionarse con otras clases.
- Las principales razones que puede haber entre dos o más clases en la orientación a objetos (OO) son:
	- **Generalización (herencia), asociación, agregación, composición y dependencia.**

