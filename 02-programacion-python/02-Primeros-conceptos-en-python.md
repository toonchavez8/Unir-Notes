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

