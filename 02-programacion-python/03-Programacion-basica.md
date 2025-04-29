# Programacion basica
#unir #notes #python #programacion #basica


## estructuras de datos
Hemos visto los tipos de datos básicos que podemos utilizar en Python para almacenar valores. Pero este tiopo de datos no son suficientes para guardar valores complejos. 

Por ejemplo
- Una lista de usarios de una pagina web

### listas

Las listas son las estructuras de datos mas usadas en python. Una lista es una estructura que nos permite tener un conjunto de objetos separados por comas.  Esta estructura de datos es **mutable**. Esto significa que podemos cambiar el tipo de valor de una lista. 

Podemos por ejemplo cambiar el orden de los elementos, eliminar elementos, agregar y transiparl Tipado.

En una lista pueden existir elementos de diferentes tipos, es decir, elementos con diferentes tipos de datos o, incluso, diferentes estructuras de datos. Sin embargo, lo normal es que todos los elementos de una lista sean del mismo tipo. Para declarar una lista, escribimos entre corchetes ([]) un conjunto de elementos separados por comas:

```python
lista=["hola",3,True]
```

Podemos crear u na lista vacia uando unicamente los corchetges sin valores o utilizando la funcion `list()`

```python
lista_vacia=[]
```

A partir de una lista que hayamos creado, podemos acceder a los elementos de la lista. Solo tenemos que indicar la posicion que el elemento dentro de la lista, indicando el indice del elemento. 

Dentro de python listas el primer elemento ocupa la posicion 0

```python
lista = [lista = [3, 'Hola', True] 
lista[2] # Devolverá el valor True]
```

podemos acceder a un conjunto de elementos de lista usando el simbolo de dos puntos `:` dentro de los corchetes. A esto se llama  un rango de indices por ejemplo para acceder a las 2 primeras posiciones de una lista

```python
lista = [3, 'Hola', True] 
lista[:2] # Devolverá [3, 'Hola']
```

Cuando usamos los rangos de indices existen unois valores por defecto cuando no indicamos su valor. El valor poppr defecto del primer indice es 0 y el valor por defecto del ultimo indice de longitud de la lista. 

#### Funciones aplicables a listas
Cuando usamos listas podemos usar un conjunto de funciones que nos permiten obtener propiedades de las listas o modificarlas

- `len()`: devuelve la longitud de una lista, retorna el numero elementos incluidos en una lista

```python
	lista=[3,"hola",true]
	len(lista) # devovera 3
```

- `index()`: devuelve ls posicion que opuca un elemento dentro de una lista
```python
	lista=[3,"hola",true]
	lista.index("hola") # devovera 1
```

- `insert()`: Inserta un elemento dentro de una lista en la posicion que le indicamos
```python
	lista=[3,"hola",true]
	lista.insert(1,"bye") 
	lista # devuelve [3,"bye",true]
```

- `append()`: inserta un elemento al final de la lista. En el caso que intenemos insertar una lista de elementos  la funcion los instertera como un elemento unico
```python
	lista=[3,"hola",true]
	lista.append([3,4]) 
	lista #nos regresa [3,"hola",true,[3,4]]
```

- `extend()`: permite agregar un conjunto de elementos en una lista. A diferencia de `append`, si intenamos agregar un a lista de elementos se agregaran cada elemento a la lista original
```python
	lista=[3,"hola",true]
	lista.extend([3,4]) 
	lista #nos regresa [3,"hola",true,3,4]
```

- `remove()`: elimina el elemento que pasamos por parámetro de la lista. En caso de que este elemento estuviese repetido, solo se eliminará la primera copia.
```python
	lista=[3,"hola",true]
	lista.extend([3,4]) 
	lista #nos regresa [3,"hola",true,3,4]
```

- `count()` : devuele el numero de veces que se encuentra un elemento  de la lista
```python
	lista=[3,"hola",true,"hola"]
	lista.count("hola") #nops devuelve 2
```

- `reverse()`: este metodo nos permite inverti la posicion de todos los elementos de la lista
```python
	lista=[3,"hola",true,"hola"]
	lista.reverse()
	lista # nos mostrara [True, 'Hola', 3]
```

- `sort()`: ordena los elementos de una lista. Por defecto este metodo los ordena en orden creciente. Para ordenenarlo de forma decreciente, hay que incluir el parametro `.sort(reverse=True)` . Este metodo requiere de que la lista sea de elementos del mismo tipo
```python
	lista = [6, 4, 1, 9, 7, 0, 5]
	lista.sort()
	lista # Nos mostrará [0, 1, 4, 5, 6, 7, 9]
	lista.sort(reverse=True)
	lista # Nos mostrará [9, 7, 6, 5, 4, 1, 0])
```

- `pop()`: elemina y devuelve el elemento que se encuentra en la posicion que se paasa por parametro. En caso de que no se pasa ningun valor por parametro se eliminara y devolvera el ultimo elemento de la lista
```python
	lista = [6, 4, 1, 9, 7, 0, 5]
	lista.sort(1)
	lista # Nos mostrará [6, 1, 9, 7, 0, 5]
```

### Tuplas
Al igual que las listas, las tuplas son conjuntos de elementos separados por comas. Sin embargo, a diferencia de las listas, las tuplas son inmutables, es decir, no se pueden modificar una vez creadas. Un ejemplo de tupla sería el siguiente:
```python
	tupla = 'Hola', 3.4, True, 'Hola' 
	tupla
```

Hemos creado una tupla a parti de una secuencia de valores seprados por comas. El resulatado es una tupla que contiene todos los elementos. Esta operación se denomina **empaquetado de tuplas**.
Tambien disponemos metodo inverso. Si a una tupla de longitud `n` le asignamos `n` variables, cada una de las variables tendra uno de los componentes de la tupla. Esta operacion se la llama desempaquetado de tuplas.

```python
	w,x,y,z = tupla # w = 'Hola', x = 3.4, y = true, z = "Hola"
```

Para acceder a los elementos de una tupla lo haremos de la misma manera que con las listas:

```python
	tupla[1] # nos mostrara 3.4
	tupla[1:] # Nos mostrara (3.4,True, 'Hola')
```

#### Funciones aplicables a tuplas

Al igual que las listas, tenemos varios métodos que podemos usar en las tuplas. Los métodos más utilizados son los siguientes:

- `len()`: metodo que devuelve la longitud.
```python
	tupla = 'Hola', 3.4, True, 'Hola' 
	len(tupla) # Devolverá 4
```
- `count()`: número de veces que se encuentra un elemento en una tupla.
```python
	tupla.count('Hola') # Devolverá 2
```
- `index()`: devuelve la posición que ocupa un elemento dentro de una tupla. En caso de que el elemento este repetido, devolverá la primera posición donde aparece el objeto.
```python
	tupla.index('Hola') # Devolverá 0
```

### Diccionarios
La última estructura de datos que veremos en Python son los diccionarios. Los diccionarios conforman una estructura que enlaza los elementos almacenados con claves (keys) en lugar de índices, como las estructuras anteriores. Es decir, para acceder a un objeto es necesario hacerlo a través de su clave.

La mejor manera de comprender un diccionario es verlo como un conjunto de pares (clave, valor), donde las claves son únicas, es decir, no están repetidas, y nos permiten acceder al objeto almacenado. Para crear un diccionario definiremos un conjunto de elementos clave valor delimitados por llaves `{}` 

```python
diccionario = { 
	'clave1': 'Mi primer valor', 
	'clave3': 'Y, como no, mi tercer valor', 
	'clave2': 'Este es mi segundo valor' 
}
```

Si queremos acceder a uno de sus valores, necesitaremos conocer su clave y lo pondremos entre corchetes `[]`
```python
diccionario['clave1'] # Devolverá 'Mi primer valor'
```

Para crear nuevos elementos en los diccionarios usamos la misma forma de acceso a un elemento, pero asignando un nuevo valor:

```python
diccionario['clave_nueva'] = ‘nuevo valor’
```

#### Funciones aplicables a diccionarios

Dos de las funciones mas fuertes que podemos usar con diccionarios

- `list()`: devuelve una lista de todas las claves incluidas en un diccionario. Si queremos la lista ordenada usarnos la función `sorted` en lugar de `list`
```python
	list(diccionario) # Devolverá ['clave1', 'clave3', 'clave2'] 
	sorted(diccionario) # Devolverá ['clave1', 'clave2', 'clave3']
```
- `in`: es palabra reservada que comprueba si una clave se encuentra en el diccionario
```python
	'clave3' in diccionario # Devolverá True
```

### conjuntos

Los conjuntos son colecciones no ordenadas. Además los conjuntos no contiene repetición de elementos se eliminan todos los elementos duplicados. Para crear un conjunto podemos indicar un conjunto de objetos separados por comas y delimitados por `{}`

```python
conjunto = {'audi', 'mercedes', 'seat', 'ferrari', 'ferrari', 'renault'}
```

Para crear un conjunto vacío podemos crearlo usando las llaves insertar ningún valor o la función `set()`

```python
conjunto = set()
conjunto #Nos mostrara {}
```

Al no ser una lista ordenada no podemos acceder a sus elements a traves de su índice; nos devolverá un error de tipo

#### Funciones aplicables a conjuntos

A continuación, veremos algunas de las operaciones soportadas por los conjuntos de Python

-  `union()`: operación matemática para obtener la union de dos conjuntos
```python
	conjunto1 = {1,2,3}
	conjunto2 = {3,4,5}
	conjunto1.union(conjunto2) #Devolvera {1,2,3,4,5}
```
- `intersection()`: operación matemática para obtener la intersección de dos conjuntos
```python
	conjunto1 = {1, 2, 3} 
	conjunto2 = {3, 4, 5} 
	conjunto1.intersection(conjunto2) # Devolverá {3}
```
- `diffrence()`: operación matemática para obtener la diferencia del conjunto original con respecto al conjunto que se pasa por parámetro es decir los elementos del primer conjunto que no están en el segundo
```python
	conjunto1 = {1, 2, 3} 
	conjunto2 = {3, 4, 5} 
	conjunto1.difference(conjunto2) # Devolverá {1, 2}
```
- `in`: comprueba si un elemento se encuentra dentro de un conjunto
```python
	1 in conjunto1 # Devolverá True
```
- `len()`: devuelve la longitud
```python
	len(conjunto1) # Devolverá 3
```

## Ejecuciones condiciones

La mayoría de las ocasiones los programas que haremos no tendrán una ejecución lineal sino que habría bifurcaciones dependiendo del resultado que obtengamos de algunas  evaluaciones. Para poder hacer esta bifurcación en la ejecución de nuestro programa es necesario utilizar las ejecuciones condiciones.

### Expresión `if`
Las expressions `if` nos permiten ejecutar un bloque de instrucciones únicamente si la expresión lógica que hemos puesto devuelve `true`. Para escribir una sentencia `if` se sigue la siguiente estructura:
```python
if(EXPRESION_LOGICA):
	sentencia_1
	sentencia_2
```

Un ejemplo del uso de una setencia `if` seria podriamos usar un print de escribir un valor de 1 al 10. A continuacion comprobamos si el numero es mayor que 5 y si es asi imprimimos un mensaje:

```python
print("Escribe un numero del 1 al 10")
number = int(input())
if (number>5):
	print("Soy mayor que 5!")
```

### Expresión `else`
Si queremos ejecutar otro bloque de instrucciones cuando no se cumple la condición del `if` usaremos la expresión `else`. Esta expresión debe ir siempre después del bloque de instrucciones del `if`

```python
if(expresion_logica)
	sentencia_1
	sentencia_2
else:
	sentencia_1
	sentencia_2
```

Podemos ampliar el ejemplo antenrio para que, en el caso de que para que el numero no sea mayor que 5 mostremos otro mensaje al usario. Para ello, incluiremos un bloque `else` después del bloque `if`
```python
print("Escribe un numero de 1 al 10")

number int(input())
if (number > 5):
	print("soy mayor que 5")
else:
	print("Soy manor o igual que 5")
```


### Expression `elif`

La expresión `elif` nos permite evaluar más condiciones dentro de una estructura `if`, para ejecutar diferentes bloques de instrucciones según el caso. Si se incluye un bloque `else`, las instrucciones dentro de este bloque se ejecutarán **solo si** todas las expresiones lógicas de los bloques `if` y `elif` han devuelto `False`.

Se puede añadir más de un bloque `elif`, y estos deben colocarse **después** del bloque `if` y **antes** del bloque `else`.

```python
if (EXPRESION_LOGICA):
	codigo_1
elif (EXPRESION_LOGICA):
	codigo_2
else:
	codigo_resto
```

Vamos a aplicar esta expresión en nuestro ejemplo anterior

Para ello, comprobaremos también si el valor introducido por el usuario es 5 y, si es así, mostraremos otro mensaje:
```python
print("Escribe un número de 1 a 10") 
number = int(input()) 
if (number > 5): 
	print("¡Soy mayor que 5!") 
elif (number == 5): 
	print("Soy el número 5") 
else: 
	print("Soy menor o igual que 5")
```

### Ejecuciones iterativas

En esta sección vamos a explicar las dos expresiones que existen en Python para ejecutar varias veces un conjunto de instrucciones. Esas expresiones son la sentencia `while` y la sentencia `for`. Además, veremos otras sentencias que se pueden utilizar en los bucles para modificar el flujo de ejecución y, por último, veremos el uso de iteradores que nos permiten recorrer todos los elementos de objetos como las listas

#### `While loop`

La primera instrucción que vamos a explicar en las iteraciones es while. Esta instrucción repite un bloque de código mientras se cumpla una condición definida por nosotros. Esa condición, al igual que pasaba con if, viene dada en forma de expresión lógica. El bloque de instrucciones de la instrucción while dejará de ejecutarse cuando esa expresión lógica devuelva un False. El formato de escritura de while es el siguiente:

``` python
while (expresion_logica):
	sentencia_1
	sentencia_2
```
Por ejemplo, imaginemos que queremos imprimir una secuencia de números desde el número 5 hasta el número 0. Esto lo podríamos hacer con un bloque while, al cual, mientras el número que estamos imprimiendo sea mayor que 0, le restaremos una unidad y lo imprimiremos:

``` python
numero = 5 
fin = 0 

while(numero > fin): 
	numero -= 1 
	print(numero)
```

A la instrucción while se la puede incluir la sentencia else. A diferencia de las ejecuciones condicionales, el bloque de instrucciones de la sentencia else se ejecutará siempre cuando acabe de ejecutarse las iteraciones en while. En este caso, escribiríamos la sentencia else a continuación de las instrucciones del bloque while.

``` python
while (EXPRESION_LOGICA): 
	sentencia_1 
	sentencia_2 
	... 
else: 
	sentencia_1 
	sentencia_2 
	...
```

En el ejemplo anterior, podemos imprimir un mensaje al usuario para indicarle que hemos acabado de imprimir números. Para ello, incluimos un bloque else después del bloque while con la instrucción que imprimirá el mensaje

```python
numero = 5
fin = 0

while(numero > fin):
	numero -= 1
	print(numero)
else:
	print("Ya he acabado")
```

Esta es la forma más sencilla de crear sentencias iterativas. Normalmente, la instrucción while se utiliza para hacer búsquedas de elementos o ejecutar un conjunto de acciones hasta que ocurre un evento. En ambos casos, no se sabe exactamente cuántas ejecuciones tenemos que hacer y depende de la evaluación de una expresión lógica.

#### `for loop`

La segunda forma de crear secuencias iterativas es con la instrucción for. Esta permite recorrer un conjunto de elementos (por ejemplo, listas) en cualquier sentido y con cualquier paso. La forma general de crear una sentencia for es la siguiente:

```python
for VARIABLE in OBJETO: 
	sentencia_1 
	sentencia_2
else: 
	sentencia_1 
	sentencia_2
```

En la instrucción for declaramos una variable a la que, en cada iteración del bucle, se le asignará el valor de uno de los elementos contenidos en `OBJETO`.

Como pasaba en la sentencia while, podemos incluir una sentencia else que ejecutará sus instrucciones cuando hayan finalizado todas las iteraciones del bucle `for`

Podemos hacer el mismo ejemplo que en la sentencia while. Para ello creamos una lista con los números que queremos imprimir. Con la instrucción for recorremos cada uno de esos números y los imprimimos. Al final, mostraremos un mensaje indicando que hemos acabado:

```python
list_numeros = [5, 4, 3, 2, 1, 0]
for numero in list_numeros:
	print(numero)
else:
	print("Ya acabo!")
```

Esta forma de asignación también se puede hacer con cadenas de texto. En este caso, a la variable se le irá asignando cada uno de los caracteres de la cadena en cada paso del bucle:

```python
texto = 'Hola mundo'
for caracter in texto:
	print(caracter)
```

Además, como es lógico, la variable puede tener un tipo de dato diferente en cada vuelta del bucle

```python
lista = ['texto', 5, (23, 56)]

for elemento in lista:
	print(elemento)

```

En las sentencias for, una forma de recorrer un objeto, como una lista, es a través de sus índices. El objetivo es que la variable tenga como valor en cada paso la posición de la lista que estamos visitando. Para poder hacer esto, en Python se utiliza la instrucción range. Esta instrucción nos devuelve un rango de números desde un número inicial hasta uno final, y con la separación entre números que hayamos seleccionado. Su estructura es una de las siguientes:

```python
# Secuencia de números de 0 a NUMERO_FINAL con paso 1
 range(NUMERO_FINAL) 
 # Secuencia de números de NUMERO_INICIAL a NUMERO_FINAL con paso 1 
 range(NUMERO_INICIAL, NUMERO_FINAL) 
 # Secuencia de números de NUMERO_INICIAL a NUMERO_FINAL con paso PASO 
 range(NUMERO_INICIAL, NUMERO_FINAL, PASO)
```

Los rangos se pueden utilizar directamente como objeto en el bucle for. Sin embargo, para poder imprimir todos los índices que nos ha generado un rango, es necesario encapsular el rango en una lista.

A continuación, vemos un ejemplo del uso de rangos. En este ejemplo solo queremos mostrar los caracteres que ocupan una posición par en la cadena «Hola mundo», podríamos hacerlo así:

```python
cadena = 'Hola mundo'

# Comenzamos en 0, hasta la longitud de la cadena y con paso = 2
for i in range(0, len(cadena), 2):
	print(cadena[i])
```


#### Sentancias extras

A las estructuras de iteración que hemos visto antes podemos incluir otras sentencias que permiten modificar la ejecución de los bucles. Estas sentencias se pueden utilizar tanto en los bucles while como en los bucles for

- `break`: esta sentencia rompe la ejecucion del bucle en el momento en que se ejecute
```python
	numeros = list (range(10))
	
	for n in numeros:
		if (n == 5):
			print('rompemos el bulce!')
			break
		print(n)
# La secuencia de ejecución sería: 0, 1, 2, 3, 4, Rompemos el bucle!
```

- `continue`: esta instrucción permite saltarnos una iteración del bucle sin que se rompa la ejecución final.
```python
	numeros = list (range(10))
	
	for n in numeros:
		if (n == 5):
			print('rompemos el bulce!')
			continue
		print(n)
# La secuencia de ejecución sería: 0, 1, 2, 3, 4, Me salto una vuelta, 6, 7, 8, 9
```

#### Iteradores
Otra forma de recorrer los elementos de un objeto en Python es utilizando iteradores. Un iterador es un objeto que, al aplicarlo sobre otro objeto iterable, como son las cadenas de texto o los conjuntos, nos permite obtener el siguiente elemento por visitar.

Para crear un iterador sobre un objeto usamos la instrucción iter(OBJETO) y se lo asignamos a una variable. Una vez creado, podemos visitar los elementos del OBJETO con la función next() y pasando por parámetro el identificador del iterador. Veremos esto en un ejemplo
```python
cadena = 'Hola'
iterador = iter(cadena)
next(iterador) # Devolverá 'H' 
next(iterador) # Devolverá 'o' 
next(iterador) # Devovlerá 'l' 
next(iterador) # Devolverá 'a'
```