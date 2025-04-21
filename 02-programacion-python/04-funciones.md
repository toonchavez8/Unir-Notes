
# funciones

## Definicion de funciones


Las funcioens nos permiten encapusar bloques de codigo que podemos utilizarlo varias veces para no repetir codigo. Para ser esto es necessario idente ese bloque de codigo usano la sistaxes de funciones que incluye python. 

Las funciones se define con las setencia `def`. Esta palabra clave indica a python que vamos a crear un objeto ejecutable que podra ser llamado mas adelante durante la ejecucion del programa. El foramto para definir una funcion en python es:
```python
	def Nombre_Funcion(Arg1,Arg2...):
		Sentancias1
		Sentancias2
		...
		return Objeto_devolver
```

Como podemos obserar, la primera linea viene definida con la palabra reservada, `def` seguida del nombre que queremos darle a la funcion. 

Primero declaramos el numbre, luego en parentesis declaramos la lista de parametros separados por comas. Estos parametros seran valores u objetos que se necesitan para ejecutar la funcion. En el caso de que nuestra funcion no necesita parametros podemos dejarlos vacila. Al final de la declaracion usamos `:` para finalizar la linea y comentar a escribir las sentacias o bloques de codigo.

El bloque de sentancias debe tener una sangria de 4 espacios con respecto a la definicion de la funcion para que python entienda que son instruciones que pertenece al a funcion. 

En el caso de que la función tenga que devolver un valor, usaremosla palabra reservada return juntocon el identificador o la expresión que devolverá el valor.

### ejemplo Area Triangulo

Imaginemos que queremos crear una función que nos calcule el área de un triángulo. Para poder calcular el área del triángulo, la función necesita dos datos: su base y su altura. Estos dos datos serán los parámetros de la función. Por último, devolveremos el resultado del cálculo usando la sentencia return. La función para calcular el área del triángulo quedaría como se muestra a continuación:

```python
def Area_Triangulo(base, altura):
	area = (base * altura)/2
	return area
```

Para ejecutrar esta funcion solo debemos usar el nombre y insterar los parametros de la base y la altura 

```python
Area_Triangulo(6,5) #devolvera 15.0
```

## parametros

En la mayoría de las ocasiones, necesitamos introducir información a las funciones para que puedan realizar la acción que deseamos. Por este motivo, podemos declarar unos parámetros que la función usará para leer esa información. Hay que saber diferenciar entre los parámetros, que son los valores que definimos en una función, y los argumentos, que son los valores que introducimos a la función en el momento de la ejecución.

En el ejemplo anterior, cuando hemos declarado la función area_triangulo, los elementos base y altura eran los parámetros. Más adelante, cuando hemos indicado que la base era 6 y la altura 5, esos valoresson los argumentos de la función.

A la hora de llamar a una función existen dos formas para introducir los argumentos de la función:

- Argumentos por posición: los argumentos se envían en el mismo orden en el que se han definido los parámetros. Esta es la forma que hemos escogido para llamar a la función area_triangulo en el ejemplo anterior.
- Argumentos por nombre: los argumentos se envían utilizando los nombres de los parámetros que se han asignado en la función. Para ello, usaremos el nombre del parámetro, seguido del símbolo igual (=) y del argumento. En el ejemplo anterior sería de la siguiente forma:
```python
	area_triangulo(base=10, altura=4) # Devolverá 20.0
```

Cuando una función tiene definido unos parámetros, es obligatorio que, a la hora de llamarlo, la función reciba el mismo número de argumentos. En caso de que no recibiese alguno de esos argumentos,

Python devolvería un error de tipo. Sin embargo, en el momento de declarar una función, podemos asignar un valor por defecto a cada parámetro. Este valor por defecto se usará solo si no se ha indicado un argumento en el parámetro correspondiente.

Para asignar un valor por defecto a un parámetro, definiremos el nombre del parámetro, seguido por el símbolo = y el valor por defecto que le queramos dar. Por ejemplo, vamos a asignar un valor por defecto para la base y la altura en la función area_triangulo.

```python
def area_triangulo(base=10, altura=10):     
	area = (base * altura) / 2     
	return area
```

En este caso,si llamásemos a la función area_triangulo sin ningún argumento, usaría los valores por defecto que hemos indicado para calcular el área

```python
area_triangulo() # Devolverá 50.0
```

También podemos indicar únicamente uno de los parámetros. En el caso de que lo hagamos por posición, reconocerá que ese argumento es el del parámetro base; en cambio, si utilizamos los argumentos por nombre, podemos aplicarlo a cualquiera de los dos parámetros.

```python
area_triangulo(altura=20) # Devolverá 100.0
area_triangulo(20) # Devolverá 100.0
```

Muchas de las funciones que existen en Python tienen parámetros con valores por defecto. Por este motivo, es importante revisar la documentación de una función para saber cómo van a ser los argumentos de la función antes de usarla.

## Parámetros indeterminados

En algunas ocasiones, puede que necesitamos definir una función que necesite un número variable de argumentos

Para estos casos Python nos permite usar los parámetros indeterminados en las funciones. Estos parámetros nos permiten incluir tantos argumentos como queramos en el momento de la ejecución de la función.

Como pasaba con los parámetros normales, existen dos maneras de asignar los argumentos

- Argumentos por posición: se deben definir los parámetros como una lista dinámica. Para ello, a la hora de definir el parámetro, se incluirá un asterisco (`*`) antes del nombre del parámetro. Los parámetros indeterminados se recibirán por posición. A estos parámetros se les puede pasar cualquier tipo de dato en cada función. Un ejemplo de su uso sería el siguiente:
```python
def imprimir_numeros(*args):
	for numero in args:
		print(numero)
		
imprime_numeros(1, 7, 89, 46, 9394)
```
- Argumentos por nombre: para recibir varios argumentos por nombre, sin saber la cantidad, es necesario definir los parámetros como un diccionario dinámico. Para ello se usa dos asteriscos (`**`) antes del nombre del parámetro. Un ejemplo de su uso sería el siguiente:
```python
def imprime_valores(**args):
	for argumento in args:
		print(argumento, '=>', args[argumento])
imprime_valores(arg1='Hola', arg2=[2,3,4], arg3=876.98)
```
A la hora de declarar una función, podemos combinar las dos formas de declarar parámetros normales con las formas que hemos visto para declarar parámetros indeterminados.

## 4.5. Retorno de valores

Uno de los objetivos más comunes en las funciones es que realicen una operación y devuelvan el resultado de la misma. Para devolver uno o varios valores se utiliza la sentencia return. En el siguiente ejemplo tenemos una función que devuelve la potencia entre dos números

```python
def potencia(base, exponente):     
	return base ** exponente
```
Como vemos, la única instrucción que tenemos dentro de la función es una sentencia return que devuelve el resultado de la operación. Hay que tener en cuenta que la instrucción return debe ser la última instrucción para ejecutarse, ya que en ese momento Python saldrá de la función.

En Python, las funciones pueden devolver más de un valor a la vez. Para hacer esto, solo tenemos que separar por comas todos los valores que queramos devolver después de la sentencia return. En el siguiente ejemplo, la función devuelve tres objetos de diferentes tipos:

```python
def ejemplo():     
	return "Hola", 3546, [3,90]
```

Cuando devolvemos más de un valor en una función, lo que obtenemos es una tupla con todos los valores. Por este motivo, si queremos que cada uno de los resultados esté en una variable distinta, es necesario hacer un desempaquetado de la tupla. En el ejemplo anterior sería así:

```python
var1, var2, var3 = ejemplo() # Nos dará var1 = “Hola”, var2 = 3546, var3 = [3, 90]
```

## Documentar funciones

Cuando estamos desarrollando software, es muy importante documentar bien las secciones de código que vamos implementando. Esto nos permitirá recordar qué hace el código que implementamos o muestra a otros desarrolladores lo que queremos hacer. La documentación cobra mayor importancia cuando se trata de funciones. Las funciones encapsulan un comportamiento dentro de un identificador

y otros usuarios no deberían acceder al código de una función para saber qué es lo que se quiere hacer. Para poder documentar las funciones se utilizan los docstring. En Python todos los objetos cuentan con una variable por defecto llamada doc, y nos permite acceder a la documentación de dicho objeto. Para documentar una función usando los docstring, únicamente tenemos que incluir un comentario inmediatamente después de la cabecera de la función. A continuación, se muestra cómo podríamos documentar la función potencia que hemos definido antes:

```python
def potencia(base, exponente):     
	"""     
	Función que calcula la potencia de dos números.          
	Argumentos:     base ‐‐ base de la operación.     
	exponente ‐‐ exponente de la operación.     
	"""     
	return base ** exponente
```

Al documentar de esta forma las funciones, podemos usar la sentencia help() con el nombre de la función para saber la documentación que tiene. En el ejemplo anterior se vería del siguiente modo:

```python
help(potencia)
```

En la guía de estilos oficial de Python (PEP8), hay varias reglas y consejos para documentar correctamente nuestro código usando los docstring.

## Funciones incluidas en Python
Python cuenta con bastantes módulos que incluyen funciones muy útiles para desarrollar nuestros programas. A continuación, veremoslos módulos y lasfunciones más importantes.

### Módulo math
El módulo math es un módulo matemático que incluye numerosas funciones matemáticas que nos pueden ser útiles en el desarrollo de nuestros proyectos. Para utilizar estas funciones es necesario importar el módulo math al principio de nuestro código usando la sentencia import:
```python
import math
```
A continuación, enumeraremos las funciones más útiles agrupadas por tipos.
#### Funciones aritméticas

Estas funciones nos permiten realizar varias operaciones aritméticas como calcular los valores superiores o inferiores de un número, cálculos factoriales o el máximo común divisor. Las funciones más importantes son:

- **fabs (x)**: devuelve el valor absoluto de _x_.  
	   `math.fabs(-1234)` → `1234`

- **gcd (x, y)**: devuelve el máximo común divisor de _x_ e _y_.  
	   `math.gcd(34, 82)` → `2`

- **floor (x)**: devuelve el mayor entero ≤ _x_.  
	   `math.floor(245.89)` → `245`

- **ceil (x)**: devuelve el menor entero ≥ _x_.  
	   `math.ceil(245.89)` → `246`

- **factorial (x)**: calcula el factorial de _x_.  
	   `math.factorial(5)` → `120`

- **trunc (x)**: devuelve la parte entera de _x_.  
	   `math.trunc(5.7836)` → `5`

#### Funciones trigonométricas

Estasfunciones nos permiten hacer cálculostrigonométricos que relacionan loslados de los triángulos con sus ángulos. En todas estas funciones debemos tener en cuenta que se trabaja con los ángulos en radianes. Las funciones más importantes son:
