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

