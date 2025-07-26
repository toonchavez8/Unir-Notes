Actividad 2: Ingeniería de software dirigida por modelos

Recuerda que esta actividad deberá ser completada en la plataforma. Solo tendrás un intento. Una vez que la envíes, se dará por cerrada. Tu puntuación y las respuestas correctas se mostrarán cuando finalice el periodo de entrega de la tarea.

**Descripción de la actividad**

En esta actividad, vamos a profundizar en la ingeniería dirigida por modelos, creando una serie de lenguajes específicos de dominio, los cuales definiremos de forma gráfica mediante metamodelos y haciendo uso de la herramienta Eclipse Modeling Framework (EMF).

Por ello, lo primero será instalar EMF, para hacerlo iremos a [Eclipse Foundation](https://www.eclipse.org/downloads/) y descargaremos el Eclipse Installer en nuestro equipo.

![mexissi01_act2](Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2.jpeg)

Iniciamos el instalador:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 1.jpeg>)

Bajaremos hasta seleccionar Eclipse Modeling Tools:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 2.jpeg>)

Seleccionaremos una carpeta de destino (se recomienda no ubicarlo en rutas que tengan espacios en blanco, como Archivos de Programa, mejor en C:\tools o en C:\tools\emf).

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 3.jpeg>)

Aceptaremos los acuerdos de licencia:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 4.jpeg>)

El instalador comenzará:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 5.jpeg>)

En función de la conectividad, es posible que muestre mensajes de advertencia o incluso que sea necesario repetir el proceso de instalación:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 6.jpeg>)

Una vez que ha finalizado la instalación, podemos lanzar el EFM desde el propio instalador, bien ejecutando el «eclipse.exe» que tendremos en la carpeta destino.

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 7.jpeg>)

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 8.jpeg>)

Como lo primero que nos va a pedir es un espacio de trabajo donde almacenar los proyectos, es recomendable tener una carpeta _workspace_ creada.

- Inicializamos eclipse:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 9.jpeg>)

- Seleccionamos una carpeta como espacio de trabajo:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 10.jpeg>)

- Tras unos segundos, tendremos el entorno disponible:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 11.jpeg>)

- Pulsaremos arriba a la derecha para ocultar (Hide) y tendremos la vista vacía:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 12.jpeg>)

1. Vamos a empezar a familiarizarnos con el entorno EMF.

Crea tu primer EMF Modeling Project:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 13.jpeg>)

Ponle como nombre «ListaCompra» y pulsa Finish:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 14.jpeg>)

Veremos que se ha creado el proyecto y tenemos esta visualización para poder crear metamodelos en base a ECore, la cual es una especificación similar a [Essential MoF:](https://www.eclipse.org/modeling/emft/search/concepts/EMOF.html)

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 15.jpeg>)

En el menú de la derecha, haz clic sobre Class y pulsa en el canvas blanco del medio para crear una nueva clase:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 16.jpeg>)

Denomínala «ListaCompra»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 17.jpeg>)

Haz lo mismo con otra que se llame «Producto»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 18.jpeg>)

Pulsa en la derecha en Attribute y añade un nombre y una cantidad a «Producto»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 19.jpeg>)

En la paleta de propiedades, seleccionaremos el EType como un _string_ (EString):

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 20.jpeg>)

Tras añadir el nombre, nos quedará así:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 21.jpeg>)

Añadiremos la cantidad:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 22.jpeg>)

Ya solo nos falta relacionar la lista con el producto. Para esto, seleccionaremos Composition, que está bajo Relation, pulsaremos primero en «ListaCompra» y posteriormente en «Producto»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 23.jpeg>)

Y renombramos la relación a productos:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 24.jpeg>)

Ya tenemos nuestro primer metamodelo ECore desarrollado en el EMF, el «listaCompra.ecore»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 25.jpeg>)

Sobre el canvas, con el botón derecho del ratón, pulsa Generate y luego All:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 26.jpeg>)

¿Qué es lo que ha ocurrido?

1. Nada.
2. Muestra en consola un mensaje con un error.
3. Ha creado código en mi proyecto en la carpeta src.
4. Ha creado código en mi proyecto en la carpeta src y, además, ha creado otros dos proyectos nuevos.
5. Ya has creado tu primer metamodelo para simplemente guardar la lista de la compra. Vamos a dar un paso más para crear nuestro primer modelo que es conforme al metamodelo anterior. Para ello, vamos a utilizar el proyecto «.editor» que en el paso anterior el EMF generó.

Pulsa sobre el proyecto «.editor» con el botón derecho del ratón, en el menú contextual, selecciona Run AS y Eclipse Application:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 27.jpeg>)

Al ser un _plugin_ de eclipse, podemos ejecutarlo dentro del propio eclipse. Para no tener que generar una versión e instalarla, podemos, desde una instancia de eclipse (en la que estábamos editando el metamodelo), lanzar otra segunda instancia que ejecutará ese _plugin._ Saldrá de nuevo que está arrancado el IDE, esta vez no pedirá el _workspace_, sino que guardará todo por defecto bajo una carpeta «runtime-EclipseApplication» (por ejemplo C:\tools\EMF\eclipse\runtime-EclipseApplication si lo instalaste en C:\tools\EMF).

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 28.jpeg>)

Al ser la primera ejecución, estará vacío, aunque en el título de la aplicación vemos que pone «runtime-EclipseApplication»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 29.jpeg>)

Haremos un New > Modeling Project:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 30.jpeg>)

Le pondremos un nombre, por ejemplo, «EjemploListaCompra» y pulsaremos Finish:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 31.jpeg>)

Nos crea un proyecto vacío:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 32.jpeg>)

Sobre el proyecto, haremos un New > Other:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 33.jpeg>)

En el buscador pondremos lista y seleccionaremos el Wizard siguiente:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 34.jpeg>)

Le pondremos un nombre, por ejemplo, «Supermercado1»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 35.jpeg>)

Le indicaremos el elemento raíz del modelo, en nuestro caso, la lista de la compra:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 36.jpeg>)

Tras pulsar Finish, ¿qué ha ocurrido?

1. Ha generado código sobre el proyecto bajo src.
2. Ha generado el modelo y nos muestra una visualización en modo Selection-Parent-List-Tree-Table-Tree with Columns.
3. Ha generado el modelo y nos muestra una visualización en modo Tree-Table-Tree with Columns.
4. Genera un diagrama visual con un modelo de lista de compra de ejemplo.
5. Ya solo nos queda un paso, incluir datos en el modelo. Dentro de la lista de la compra, con el botón derecho hay que seleccionar New Child y Producto:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 37.jpeg>)

En el editor inferior pondremos el nombre, por ejemplo, «Leche»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 38.jpeg>)

Hacemos este ejercicio varias veces modificando el nombre y la cantidad:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 39.jpeg>)

Intenta editar la cantidad de zumo y pon «un par de litros»:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 40.jpeg>)

¿Qué ocurre?

1. Nada.
2. Salta una excepción y se cierra eclipse.
3. Muestra un mensaje de «NumberFormatException» y no deja asignar valor.
4. Deja el valor asociado correctamente.
5. En este metamodelo solo podemos tener una lista de la compra y, además, no podemos organizarla por zonas o supermercados. ¿Cómo extenderías el metamodelo para cumplir las siguientes extensiones?

- Una lista de compra tiene sublistas.
- Incluyen una descripción del lugar.
- Cada una tiene productos como hasta ahora.

1. Se debe incluir un nuevo elemento al metamodelo sublista.
2. Se debe incluir un nuevo atributo a la lista y una composición reflexiva.
3. En metamodelos no se pueden anidar elementos de forma recursiva.
4. El modelo existente ya lo soportaba.
5. Vamos a crear el primer metamodelo propio que nos permita definir páginas web simplificadas. Crea el ecore que soporta la definición de una página web con zonas (_header,_ central, _footer)_ y elementos (_label, buton, image, link)_ como para poder generar este modelo:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 41.jpeg>)

¿Qué contiene tu metamodelo?

1. 10 clases, 2 de ellas abstractas, 7 herencias y 2 composiciones.
2. 8 clases, 0 abstractas, 3 herencias y 2 composiciones.
3. 3 clases y 2 composiciones.
4. No se puede generar el metamodelo para cumplir esa especificación.
5. Crea un nuevo metamodelo para soportar un _workflow_ de pasos simple, que permita registrar una secuencia de actividades secuencial unida por transiciones para soportar un modelo de este estilo:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 42.jpeg>)

¿Qué contiene tu metamodelo?

1. 3 clases y 1 composición.
2. 4 clases, 1 abstracta, 1 composición, 2 herencias y 2 relaciones.
3. 4 clases, 0 abstractas y 3 composiciones.
4. No se puede generar el metamodelo para cumplir esa especificación.
5. Queremos generar un metamodelo de bases de datos. Vamos a comenzar definiendo las tablas y sus columnas, de momento sin relaciones, para poder cubrir un modelo de este tipo:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 43.jpeg>)

¿Qué contiene tu metamodelo?

1. 2 clases y 1 composición.
2. 4 clases, 0 abstractas y 3 composiciones.
3. No se puede generar el metamodelo para cumplir esa especificación.
4. 4 clases, 1 abstracta, 2 composiciones y un tipo enumerado.
5. Extendemos el metamodelo de esta forma:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 44.jpeg>)

¿Es posible representar un modelo así?

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 45.jpeg>)

Donde en el préstamo tenemos:

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 46.jpeg>)

![mexissi01_act2](<Maestría-Ingeniería-de-Software/02-Metologias-Desarollo-y-Calidad/Actividades/Actividad_02/Attachments/mexissi01_act2 47.jpeg>)

1. No, ya que Foreign Key tendría que ser otra entidad separada de la columna.
2. No, ya que no puede ser Foreign Key y clave primaria a la vez.
3. Sí, el metamodelo lo soporta.
4. No, porque, aunque el metamodelo lo soportara, el modelo sería erróneo.
5. ¿Cómo extenderías el metamodelo para incluir la restricción de valor único para una columna (de momento simplemente asociado a un campo)?
6. Hay que añadir un nuevo atributo _boolean_ en Tabla.
7. Hay que añadir un nuevo elemento como ForeignKey que herede de Columna.
8. Hay que añadir un nuevo atributo _boolean_ en Columna.
9. Hay que añadir un nuevo atributo _boolean_ en Table.
10. ¿Qué tendríamos que modificar para soportar el modelado de que no podamos tener una persona que tiene el mismo nombre y teléfono, pero sí que tengamos dos personas con el mismo nombre o con el mismo teléfono?
11. Crear un nuevo elemento que se relacione con Column.
12. Crear un nuevo elemento que herede de Column.
13. Crear un nuevo elemento que herede de Foreign Key.
14. No es posible incluirlo en el metamodelo anterior.