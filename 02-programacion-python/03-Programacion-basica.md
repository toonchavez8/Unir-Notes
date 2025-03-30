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

Hemos creado una tupla a parti de una secuencia de valores seprados por comas. El resulatado es una tupla que contiene todos los elementos. Esta operacion se denominba **empaquetado de tuplas** 