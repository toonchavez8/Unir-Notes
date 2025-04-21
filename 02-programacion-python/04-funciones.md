Me pat
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

En el caso de que la función tenga que devolver un valor, usaremosla palabra reservada return junto con el identificador o la expresión que devolverá el valor.