### Interpretacion de la matriz de
  correlacion

  La matriz muestra que `Genero_binario`
  casi no tiene correlacion lineal con las
  variables principales del analisis:

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

  ### Relacion con K-Means

  La grafica de K-Means sin genero muestra
  que los clusters se organizan
  principalmente por ingreso anual y
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
  dimensiones. Dos clientes pueden tener
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
