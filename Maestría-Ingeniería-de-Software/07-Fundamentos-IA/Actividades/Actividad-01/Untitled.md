# Interpretacion De la Matriz De

  correlacion

  La matriz muestra que `Genero_binario`

  casi no tiene correlacion lineal con las

  variables principales del analysis:

  - Con `Age`: `-0.06`
  - Con `Annual Income (k$)`: `-0.06`
  - Con `Spending Score (1-100)`: `0.06`

  Como `Genero_binario` vale `1` para

  mujeres y `0` para hombres, estos valores

  indican que el genero no esta fuertemente

  asociado, de forma lineal, ni con la edad,

  ni con el ingreso, ni con la puntuacion de

  gasto. La relacion es practicamente

  neutra.

  La correlacion mas visible de la matriz no

  es con genero, sino entre `Age` y

  `Spending Score (1-100)`, con `-0.33`.

  Esto sugiere que, en este dataset, los

  clientes de mayor edad tienden a tener una

  puntuacion de gasto menor. No es una

  relacion perfecta, pero si es mas fuerte

  que cualquier relacion observada con

  genero.

  Tambien se observa que `Annual Income

  (k$) ` casi no se correlaciona con

  `Spending Score (1-100)` (`0.01`). Esto es

  importante porque significa que ingreso y

  gasto no crecen juntos de forma lineal.

  Por eso el clustering puede encontrar

  grupos interesantes: hay clientes con

  ingreso alto y bajo gasto, ingreso alto y

  alto gasto, ingreso bajo y alto gasto,

  etc.

  Y conectado con K-Means:

# Relacion Con K-Means

  La grafica de K-Means sin genero muestra

  que los clusters se organizan

  principalmente por ingreso annual y

  puntuacion de gasto. Se distinguen grupos

  claros:

  - Clientes de ingreso alto y gasto alto.
  - Clientes de ingreso alto y gasto bajo.
  - Clientes de ingreso bajo y gasto alto.
  - Clientes de ingreso bajo y gasto bajo.
  - Clientes de ingreso medio y gasto medio.

  Algunos clusters aparecen visualmente

  superpuestos en el plano ingreso-gasto,

  especialmente los grupos centrales. Esto

  ocurre porque el modelo tambien usa `Age`,

  aunque la grafica solo muestra dos

  dimensions. Dos clientes pueden tener

  ingreso y gasto parecidos, pero quedar en

  una relacion lineal fuerte con la

  variables de consumo.

  Sin embargo, al incluir genero en

  el algoritmo puede usarlo como un

  dimension adicional de distancia.

  el genero no este correlacionado

  otras variables, al estar estanda

  puede separar clientes hombres y

  sugiere que genero no tiene una r

  fuerte con las variables numerica

  grafica de K-Means sin genero mue

  la segmentacion principal ya se e

  bastante bien por ingreso, gasto

  Por eso, cuando se agrega genero,

  modelo fragmenta mas los clusters

  `silhouette` no mejora.

  si genero no esta muy correlacion

  las variables de consumo, puede c

  composicion de los clusters, pero

  necesariamente mejorar la calidad

  segmentacion.

# Resumen

Este informe presenta un analysis de segmentacion de clientes a partir del conjunto de datos `Mall_Customers.csv`, que contiene information demografica y de consumo de 200 clientes de un centro comercial. El objetivo fue identificar grupos homogeneos mediante aprendizaje no supervisado y comparar dos algoritmos de clustering: K-Means y Agglomerative Clustering. El analysis siguio una secuencia completa de exploracion, preprocesamiento, estandarizacion, busqueda del numero optimo de clusters, entrenamiento de modelos, visualizacion e interpretacion de resultados.

La segmentacion se realizo principalmente con las variables `Age`, `Annual Income (k$)` y `Spending Score (1-100)`. Los resultados muestran que existen patrones de consumo claros, especialmente en combinaciones de ingreso y gasto. K-Means obtuvo un desempeno superior al metodo jerarquico en terminos de silhouette score, lo que lo convierte en el modelo mas adecuado para esta actividad. Aun asi, el valor de silhouette no es perfecto, lo que indica que algunos clientes quedan en zonas intermedias o presentan comportamientos solapados.

La interpretacion de los clusters sugiere segmentos utiles para negocio, como clientes de alto ingreso y alto gasto, clientes con alto ingreso pero bajo gasto, clientes jovenes con gasto elevado y clientes de menor gasto. Estos perfiles pueden orientar campanas de marketing, promociones y estrategias de fidelizacion.

**Palabras clave:** segmentacion de clientes, clustering, K-Means, Agglomerative Clustering, silhouette score, analysis exploratorio.