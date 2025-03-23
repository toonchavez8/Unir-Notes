# Primeros concepts en python
#notes #unir #python #sintaxis #conceptos


## Sintaxis

Python sigue una guía de estilo con el objetivo de que los programas sean fáciles de leer. Algunas de las normas que explicaremos aquí han sido creadas con el mismo objetivo

### Identificadores
Los identificadores son nombres que asignaremos a elementos, como funciones, variables, etc., para hacerles referencia más adelante en el código. Estos identificadores tienen que seguir las siguientes reglas:

- Pueden ser una combinación de números (0-9), letras mayúsculas (A-Z), letras minúsculas (a-z) y el símbolo de guion bajo (_). 
-  No pueden comenzar por un dígito. 
-  No pueden utilizarse símbolos especiales: @, !, #, etc. 
-  Pueden tener cualquier longitud. 

Hay que decir que Python distingue las mayúsculas de las minúsculas. Esto significa que, si tuviéramos los identificadores identificador e IDENTIFICADOR, Python los consideraría identificadores diferentes. En el siguiente bloque veremos algunos ejemplos

```python
# Identificadores correctos. 
variable = 1 
otra_variable = 'Otra' 
_mas_variables = [1, 3, 4] 
Variable_4 = True 
# Identificadores incorrectos. 
@variable = 3 
2_variable ='Está mal.’
```

### Palabras reservadas
Python, como todos los lenguajes de programación, tiene un conjunto de palabras reservadas que no se pueden utilizar como identificadores. Esta lista de palabras reservadas es la siguiente: 
`and, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield`

### Comentarios

Los comentarios son partes del código que el intérprete de Python no ejecuta. Estos comentarios nos permiten escribir aclaraciones en el código para mejorar su interpretabilidad por parte de otros desarrolladores o para nosotros mismos en un futuro. En Python hay dos sintaxis diferentes para escribir los comentarios:

- Comentarios de línea: para aquellos comentarios que solo ocupen una línea se utiliza el símbolo # al principio de la misma. 

- Comentarios de bloque: para los comentarios que ocupen más de una línea se utilizan triples comillas (simples o dobles) al principio y al final del comentario.
```python
#comment

"""
this is a comment
"""
'''
this is also a comment
'''
```


### Sangría

Una de las diferencias que tiene Python con respecto a otros lenguajes, como C o Java, es que no utiliza llaves `({,})` para diferenciar bloques de código.

En Python se utiliza la sangría de bloques, es decir, hacer una separación hacia la derecha del código que pertenece a un bloque.

Esta forma de definir los bloques de código hace que el código sea más legible. Sin embargo, al ser obligatorio, puede llevar a errores de ejecución si no se ha hecho la sangría correctamente.

```python
# Ejemplo de una sangría: 
variable = 1 
	if (variable == 1): 
	print("Aquí pongo el código a ejecutar.") 
	print("Tiene una sangría de 4 espacios.")
```

### Almacenar valores

Unas de las principales herramientas que necesitamos en cualquier lenguaje de programación son elementos que nos permitan almacenar valores para usarlos más adelante en nuestro programa.

#### Variables

A la hora de implementar nuestros programas será necesario almacenar algunos valores para consultarlos o modificarlos durante la ejecución. Para poder hacerlo utilizaremos las **variables**. Una variable es un identificador al que le asignaremos un valor y, más adelante, llamando a ese identificador podremos consultar el valor

En Python la creación de una variable se hace a través de una asignación. Haremos una asignación escribiendo el nombre de un identificador, seguido del símbolo = y el valor que deseamos almacenar en la variable:

```python
identificador = [valor]
```

A diferencia de otros lenguajes, no es necesario definir el tipo de dato que almacenará la variable.

El motivo es que Python infiere este tipo en el momento de ejecutar la asignación y le asignará el tipo de dato que mejor se adapte al valor que hayamos asignado.

Por ejemplo, si asignamos a una variable el valor ‘Hola mundo!’, esta variable será de tipo cadena de texto. Además, una misma variable puede almacenar diferentes tipos de datos durante la ejecución.

Para preguntar qué tipo de dato ha almacenado una variable, usaremos la función type:

```python
#Ejemplo de variable
n = 23
saludo = "Hola mundo"

type(n) #devuelve int
type(saludo) #devuelve string o str

```

#### Constantes

Una constante es un tipo de variable cuyo valor no puede ser modificado durante Introducción a la programación y al análisis de datos con Python Tema 2. Ideas clave 9 © Universidad Internacional de La Rioja (UNIR) toda la ejecución del programa. Se suele utilizar para almacenar valores que necesitaremos tener disponibles a lo largo de la ejecución

En Python no existe ninguna palabra reservada que nos permita definir una constante. Sin embargo, existen dos posibles soluciones para declarar constantes. Una de ellas es utilizar una variable, escribiendo el identificador en mayúsculas para que sepamos que esa variable no puede ser modificada.

```python
# Ejemplo de constantes:
IVA = 0.21
precio = 25

precio_final = precio + (precio * IVA)

print("El precio final es:", precio_final)
```

Otra solución muy utilizada es crear un script de Python, accesible desde nuestro proyecto, donde se almacenen todas las constantes.

importamos ese script con la instrucción import para poder llamar a esas constantes. El ejemplo anterior, usando un script de constantes, sería el siguiente:

```python

# Importamos el fichero de constantes.
import Constantes

precio = 25
precio_final = precio + (precio * Constantes.IVA)
print("El precio final es:", precio_final)
```

## Tipos de datos

Como hemos visto cuando  declaramos un elemento para alacenar un valor en python, ya sea una variable o constante no necesitamos definer el tipo de dato que se usara para guardar el valor. 

Es necesidad conocer los tipos de datos que podemos encontrar en python para saber que operadores podermos usar.

### Datos numericos

Los primeros tipos de datos que nos encontramos son los tipos numéricos. Dentro de los tipos numéricos encontramos los siguientes tipos más específicos:

- Enteros 
	- (int): 26, 0b1101 
	- (base binaria), 0x3f4a 
	- (base hexadecimal)
- Flotate
	- *(float)*: 3.14, 5.,-67.769
- complejos
	- (complex): 0.1117 j

Usando estos tipos de datos, podemos aplicar los siguientes tipos de operadores: operadores aritméticos, operadores de asignación y operadores de bits.

#### Operadores aritméticos

-  Suma (`+`)  
	Devuelve como resultado la suma de dos números.  

```python
3.13 + 6  # Devuelve 9.13
````

- Resta (`-`)
	Devuelve como resultado la resta de dos números.

```python
3.13 - 6  # Devuelve -2.87
```

- Multiplicación (`*`)
	Devuelve como resultado la multiplicación de dos números.

```python
3.13 * 10  # Devuelve 31.3
```

- División (`/`)
	Devuelve como resultado la división de dos números.

```python
3.13 / 10  # Devuelve 0.313
```

- División entera (`//`)
	Devuelve como resultado la división entera de dos números.  
	El resultado será únicamente la parte entera de la división.

```python
3 // 10  # Devuelve 0
```

- Módulo (`%`)
	Devuelve como resultado el valor del resto obtenido de la división entera entre dos números.

```python
3 % 10  # Devuelve 3
```

Exponente (`**`)
	Devuelve como resultado el valor exponencial de una base con respecto al exponente.

```python
3 ** 2  # Devuelve 9
```

#### Operadores de asignación

Los operadores de asignación permiten asignar el resultado de la operación a una variable incluyendo el símbolo `=` en el operador.  
Estos nos permiten modificar el valor de una variable sin tener que definirla en la parte derecha de la asignación.

- **Asignación simple** (`=`)  
    Asigna a la variable del lado izquierdo el valor definido en la parte derecha.
    
    ```python
    resultado = 10  # resultado vale 10
    ```
    
- **Suma y asignación** (`+=`)  
    Suma el valor de la variable con el valor definido en el lado derecho.
    
    ```python
    resultado = 10  # resultado vale 10
    resultado += 10  # resultado vale 20
    ```
    
- **Resta y asignación** (`-=`)  
    Resta el valor de la variable con el valor definido en el lado derecho.
    
    ```python
    resultado = 10  # resultado vale 10
    resultado -= 10  # resultado vale 0
    ```
    
- **Multiplicación y asignación** (`*=`)  
    Multiplica el valor de la variable con el valor definido en el lado derecho.
    
    ```python
    resultado = 10  # resultado vale 10
    resultado *= 10  # resultado vale 100
    ```
    
- **División y asignación** (`/=`)  
    Divide el valor de la variable con el valor definido en el lado derecho.
    
    ```python
    resultado = 10  # resultado vale 10
    resultado /= 10  # resultado vale 1.0
    ```
    
- **División entera y asignación** (`//=`)  
    Realiza la división entera de la variable con el valor definido en el lado derecho.
    
    ```python
    resultado = 14  # resultado vale 14
    resultado //= 10  # resultado vale 1
    ```
    
- **Módulo y asignación** (`%=`)  
    Asigna a la variable el resto de la división entera entre su valor y el valor de la derecha.
    
    ```python
    resultado = 14  # resultado vale 14
    resultado %= 10  # resultado vale 4
    ```
    
- **Exponente y asignación** (`**=`)  
    Asigna a la variable el resultado de elevarla al valor de la derecha.
    
    ```python
    resultado = 3  # resultado vale 3
    resultado **= 2  # resultado vale 9
    ```


#### Operaciones de bits

Otra de las operaciones básicas que podemos realizar en Python con valores numéricos son las operaciones de bits.  
Estas operaciones solo se pueden aplicar a valores enteros.

- **AND** (`&`): Operador lógico *and* a nivel de bits.  
  Devuelve un número en el que cada bit es `1` si los bits correspondientes en ambos operandos son `1`, de lo contrario, `0`.

  ```python
  4 & 5  # Devuelve 4
  # 4 en binario:  100
  # 5 en binario:  101
  # -----------------
  # Resultado:      100  (4 en decimal)
```

- **OR** (`|`): Operador lógico _or_ a nivel de bits.  
    Devuelve un número en el que cada bit es `1` si al menos uno de los bits correspondientes en los operandos es `1`.
    
    ```python
    4 | 5  # Devuelve 5
    # 4 en binario:  100
    # 5 en binario:  101
    # -----------------
    # Resultado:      101  (5 en decimal)
    ```
    
- **XOR** (`^`): Operador lógico _XOR_ a nivel de bits.  
    Devuelve un número en el que cada bit es `1` si los bits correspondientes en los operandos son diferentes.
    
    ```python
    4 ^ 5  # Devuelve 1
    # 4 en binario:  100
    # 5 en binario:  101
    # -----------------
    # Resultado:      001  (1 en decimal)
    ```
    
- **Mover bits a la izquierda** (`<<`):  
    Desplaza todos los bits a la izquierda tantas posiciones como se indique en el lado derecho del operador.  
    Esto equivale a multiplicar el número por `2` elevado al número de posiciones.
    
    ```python
    4 << 1  # Devuelve 8
    # 4 en binario:   100
    # Desplazado 1 bit a la izquierda:
    # Resultado:     1000  (8 en decimal)
    
    4 << 2  # Devuelve 16
    # 4 en binario:   100
    # Desplazado 2 bits a la izquierda:
    # Resultado:    10000  (16 en decimal)
    ```
    
- **Mover bits a la derecha** (`>>`):  
    Desplaza todos los bits a la derecha tantas posiciones como se indique en el lado derecho del operador.  
    Esto equivale a dividir el número por `2` elevado al número de posiciones.
    
    ```python
    4 >> 1  # Devuelve 2
    # 4 en binario:  100
    # Desplazado 1 bit a la derecha:
    # Resultado:      10  (2 en decimal)
    
    5 >> 2  # Devuelve 1
    # 5 en binario:  101
    # Desplazado 2 bits a la derecha:
    # Resultado:      1  (1 en decimal)
    ```
