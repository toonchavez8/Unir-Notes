# Ideas claves

Python se ha convertido en  uno de los lenguajes de programación mas populares dado a su potencia y facilidad para aprenderlo. 

- Contextualizar Python desde su historia y sus características.
- Comprender el problema de las versiones que ha existido hasta este año. 
- Conocer los pasos para instalar Python en nuestro equipo.
- Conocer las distintas herramientas existentes para programar en Python.
- Comprender el entorno de desarrollo de Jupyter Notebook.

## Que es python

Es un language de propósito general que en los últimos años se ha ido haciendo cada ves mas pop en area de data science y IA

### contexto de python

#### historia
Python fue creado en 1989 por Guido van Rossum. Guido empezó a implementar este lenguaje como pasatiempo con el objetivo de que fuera fácil de usar y aprender, pero, a la vez, que fuese un lenguaje potente

Van Rossum lo llamo `Python` en homenaje al grupo **Monty Python**.  El Desarrollo inicio en 1989 y se publico en 1991. El principal objetivo del lenguaje era que fuese facil de leer, y comprender, Que el codigo que se escribe con fuera facil de entender a comparacion de `C++` y `JAVA`

ara lograr este objetivo, el desarrollador Tim Peters creó el Zen de Python, que define un conjunto de reglas que representan la filosofía de Python.

```python
import this	
```

Siguiendo la filosofía propuesta en el Zen de Python, se creó una guía de estilo que se encuentra descrita en el Python Enhancement Proposal, abreviado como [PEP, versión 8.](https://www.python.org/dev/peps/pep-0008/)


Esta guía contiene las reglas de estilo que se aplicaron a la hora de desarrollar Python para que se sigan en el desarrollo de nuevas aplicaciones

#### Ventajas de Python
Python tiene varias propiedades que lo han convertido en un lenguaje muy potente y fácil de aprender. Estas propiedades son las siguientes:

1. **Tipado Dinamico:** `Python ` no requiere de que definamos el tipo de varialbes que inicializamos. A comparacion de `C` o `JAVA` que ellos si requiere de de tipados estatico. Cuando inicializamos una variable Python le asigna el tipo del valor que le estamos asignando.
	- **Esta propiedad hace que sea más sencillo aprender a usarlo, aunque hace que sea más difícil detectar errores asociados con los tipos de datos.**
2. **Lenguaje multiparadigma:**  `Python` permite aplicar diferentes paradigmas de programación como son la programación orientada a objetos , como `Java` o `C++`, programación imperativa, como `C`, o programación funcional, como `Haskell`.
3. **Interpretado/scripts:** Otra ventaja de que podemos usar `Python` de forma interpretanda o usando scripts.
4. **Extensions:** Python cuenta con una gran cantidad de módulos y librerías que podemos instalar para incluir nuevas funcionalidades. Sin embargo, como Python esta implementado usando C++, podemos crear nuevos módulos en C++ e incluirlo en Python

#### versiones en Python

a finales de 2008 se iba a publicar la versión 3.0. Esta nueva versión era un cambio radical con respecto las predecesoras y esto hacía que no fuera compatible con las versiones anteriores de Python. Por este motivo, se publicó la versión 2.6 como soporte para los desarrollos de la versión 2. En la versión 2.6 se incluyeron nuevas funcionalidades de la versión 3, pero adaptadas a la versión 2. Desde ese momento Python contaba con 2 versiones y las novedades las tenían que duplicar en ambas. Por ejemplo, en 2010 publicaron la versión 3.1 y la 2.7 que incluía las nuevas funcionalidades, pero adaptadas a la versión 2.

Sin embargo, desde el equipo de Python siempre han explicado que las versiones 2.6 o 2.7 eran un parche y que no iban a ser versiones funcionales en un futuro. Este hecho se hizo oficial en enero de 2020 cuando se decidió que la versión 2.7 quedaba descontinuada y que a partir de entonces solo se publicarían nuevas funcionalidades para la versión 3

## Herramientas

### Entornos de desarrollo

Como ya hemos explicado, Python es un lenguaje que podemos ejecutarlo de dos formas principalmente: usando el intérprete o usando scripts.

Tenemos  diferentes entornos de desarrollo que encontramos para programar en Python. Además, explicaremos en detalle el funcionamiento de Jupyter Notebook.

#### Modo Interactivo

**Python es un lenguaje interpretado**

Python es capaz de ir ejecutando las instrucciones según las vamos introduciendo. Por este motivo, la instalación de Python incluye el intérprete en el que podemos ejecutar instrucciones.

```bash
python
```

Usando este modo podemos conocer algunos elementos del lenguaje Python como sus clases o funciones. Además, podemos consultar la documentación del lenguaje desde el propio intérprete

Para salir del intérprete solo debemos ejecutar el comando `exit().`

#### IPython

Para mejorar el intérprete de Python, se puede instalar el paquete IPython

IPython añade más funcionalidades al intérprete de Python, como son el resaltado de errores, completado automático de variables o módulos a través del tabulador, etc. Una vez instalado, para iniciar este intérprete solo debemos ejecutar la instrucción `ipython.

Con tab despues de iniciar un nuevo comando podemos ver mas opcciones 

#### Editores de texto plano

Las dos opciones anteriores nos permiten ejecutar pequeñas instrucciones en Python y poder consultar la documentación de objetos y módulos.

para crear programas más complejos es necesario escribir scripts que contienen más instrucciones o diferentes bloques de código.

Una de las primeras opciones que se pueden utilizar para implementar estos scripts es la utilización de editores de texto plano. Existen muchos tipos de editores de texto para todos los sistemas operativos, algunos ejemplos pueden ser:

- Nano o vim
- Bloc de notas
- Sublime text 3
- Notepad++
- Viscual Code
- Vs Code

### Entornos de desarrollo avanzados

Por último, existen diferentes entornos de desarrollo avanzados orientados a Python. Estos entornos están orientados a grandes proyectos en Python y se incluyen muchas más funcionalidades como son la gestión de repositorios

Algunos de estos entornos de desarrollo pueden ejecutar en un mismo proyecto scripts y notebooks, como es el caso de PyCharm. Los entornos de desarrollo más utilizados son

- PyCharm
- Eclipse PyDev.
- Spyder

#### Jupyter Notebook

Jupyter Notebook es una aplicación web incluida en la distribución Anaconda

Esta aplicación web es una extensión de IPython, donde se añaden funcionalidades y se mejora la interfaz gráfica.

La principal característica que tiene Jupyter Notebook es la creación de celdas con objetivos específicos. Estos objetivos específicos de cada celda pueden ser: ejecutar código de Python, incluir texto en markdown o visualizar gráficos.

Para abrir Jupyter Notebook en nuestro equipo, ejecutaremos la aplicación Anaconda Navigator.

Esto hará que nuestro navegador web predeterminado abra Jupyter Notebook como una aplicación web. 

#### Navegador de archivos

La primera ventana que nos muestra Jupyter Notebook es el navegador de archivos.

A través de esta ventana podemos movernos en nuestro sistema de ficheros, crear nuevas carpetas o archivos y renombrar ficheros.

Para crear un nuevo fichero, pulsamos sobre el botón New. Una vez hecho esto, se nos desplegarán varias opciones para crear un fichero: notebook (con la versión correspondiente de Python) u otro tipo de fichero como, por ejemplo, un fichero de texto o una carpeta.

![[Pasted image 20250317083920.png]]
Esto hará que se cree un fichero del tipo seleccionado en la carpeta en la que nos encontremos en ese momento. Vamos a crear un fichero de tipo notebook y, a continuación, explicaremos la ventana que nos muestra Jupyter dentro de un notebook.

#### Vista del notebook

Cuando creamos un notebook o abrimos uno que ya existe veremos una pantalla similar a la que se muestra en la Figura 24. En la parte inferior veremos todas las celdas de nuestro notebook. Cada una de estas celdas pueden ser de los siguientes tipos:

- Código en Python.
- Texto con markdown. 
- Formato raw en la que se muestra el texto con el formato de consola. 
- Formato heading que crea una celda con formato título.

Justo encima de las celdas, tenemos un conjunto de botones que nos permiten interactuar con las celdas. A continuación, explicaremos cada uno de estos botones siguiendo el orden de izquierda a la derecha:

- Guardar: almacena en el fichero todas las celdas y guarda el estado de ejecución en el que se quedó el notebook.  
- Nueva celda: crea una nueva celda inmediatamente después de la celda que tenemos seleccionada.  
- Cortar: permite cortar una celda para pegarla en otro punto del notebook.  
- Copiar: permite copiar una celda para poder pegarla en otro punto del notebook.  
- Pegar: pegamos la celda que hemos copiado o cortado previamente inmediatamente después de la celda que tenemos seleccionada.  
- Bajar una celda: desplaza la celda seleccionada una posición hacia abajo.  
- Subir una celda: desplaza la celda seleccionada una posición hacia arriba.