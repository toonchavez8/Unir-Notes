# Notas De Analysis - Actividad 1

## Datos Generales

- Actividad: Segmentacion de clientes mediante aprendizaje no supervisado.
- Fecha de trabajo: 28 de junio de 2026.
- Dataset: `Mall_Customers.csv`.
- Fuente: archivo local de clientes de centro comercial usado para la actividad.
- Archivo utilizado: `segmentacion_clientes.ipynb`.

## Exploracion Inicial

- Numero de filas: 200 clientes.
- Numero de columnas: 5 columnas.
- Columnas disponibles: `CustomerID`, `Genre`, `Age`, `Annual Income (k$)`, `Spending Score (1-100)`.
- Tipos de datos: `CustomerID`, `Age`, `Annual Income (k$)` y `Spending Score (1-100)` son numericas; `Genre` es categorica.
- Valores nulos detectados: no se detectaron valores nulos en ninguna columna.
- Duplicados detectados: no se reportan duplicados en el analysis documentado. 

## Variables Relevantes

- Variables candidatas: `Age`, `Annual Income (k$)`, `Spending Score (1-100)`, `Genre` y `CustomerID`.
- Variables seleccionadas: `Age`, `Annual Income (k$)` y `Spending Score (1-100)`.
- Variables excluidas: `CustomerID` y `Genre`.
- Justificacion de exclusion: `CustomerID` solo identifica registros y no describe comportamiento del cliente. `Genre` es categórica. Se realizo ua prueba utilizando género Pero al integrarlo, Noté que agregó una dimensión adicional de distancia Pero no entrego un valor Que defina Más que correlacionado A las otras variables Se puede separar clientes hombres y mujeres por género pero no es una variable fuerte numérica Dado eso la segmentación principal ya es bastante bien por el ingreso gasto Y por eso cuando se agrega género modelo para el modelo el modelo fragmenta los clusters Y en las sillueta no mejora y incluso en varios clustors bajo por debajo de .38

## Analysis Exploratorio

- Observaciones sobre edad: la edad promedio es 38.85 anos, con minimo de 18 y maximo de 70. La mediana es 36, por lo que la mitad de los clientes tiene 36 anos o menos.
- Observaciones sobre ingreso annual: el ingreso annual promedio es 60.56 k$, con minimo de 15 k$ y maximo de 137 k$. La mediana es 61.5 k$, muy cercana al promedio.
- Observaciones sobre spending score: el promedio es 50.20, con valores desde 1 hasta 99. Hay bastante variacion en el comportamiento de gasto.
- Posibles outliers: se observan clientes con ingresos altos y comportamientos de gasto muy bajos o muy altos. No necesariamente son errores; mas bien parecen segmentos de negocio distintos.
- Relaciones visuals observadas: el grafico de ingreso annual contra spending score muestra grupos naturales: bajo ingreso-bajo gasto, bajo ingreso-alto gasto, alto ingreso-bajo gasto, alto ingreso-alto gasto y una zona central con clientes de ingreso y gasto medios.

## Preprocesamiento

- Metodo de escalado: `StandardScaler`.
- Justificacion del escalado: K-Means y Agglomerative Clustering trabajan con distancias. Si no se escalan las variables, una columna con rango mas grande puede pesar mas que las demas aunque no sea mas importante.
- Transformaciones aplicadas: seleccion de variables numericas relevantes, creacion de `X = df[features].copy()` y estandarizacion de `Age`, `Annual Income (k$)` y `Spending Score (1-100)`.

## K-Means

- Valores de k probados: del 2 al 10.
- Metodo del code: la inercia baja con mas clusters. La caida fuerte aparece entre `k=2` y `k=4`; despues sigue bajando, pero con menor intensidad. El code puede defenderse alrededor de `k=4`, `k=5` o `k=6`.
- Silhouette scores: el mejor valor aparece con `k=6`, con `0.428417`. Para `k=5`, el valor es `0.416643`, que sigue siendo acceptable y permite una explicacion mas clara.
- Mejor k elegido: `k=5`.
- Justificacion del mejor k: aunque `k=6` tiene la mejor metrica, `k=5` produce segmentos mas faciles de interpretar y coincide bien con la estructura visual del grafico ingreso-gasto.

## Segundo Metodo

- Algoritmo: `AgglomerativeClustering`.
- Parametros: `n_clusters=5`, usando el mismo numero de clusters que K-Means para una comparacion directa.
- Metrica principal: `silhouette_score`.
- Observaciones: Agglomerative Clustering identifica una estructura parecida a K-Means, pero obtiene menor silhouette (`0.390028` frente a `0.416643` de K-Means). Sirve como comparacion, pero no supera al modelo principal.

## Interpretacion De Clusters

- Cluster 0: clientes de ingreso bajo y gasto bajo. Edad promedio aproximada de 46.25 anos, ingreso de 26.75 k$ y spending score de 18.35. Es un segmento de bajo valor inmediato; podria trabajarse con promociones basicas o estrategias de reactivacion.
- Cluster 1: clientes jovenes con ingreso bajo-medio y gasto medio-alto. Edad promedio de 25.19 anos, ingreso de 41.09 k$ y spending score de 62.24. Puede responder bien a promociones, experiencias y programas de fidelizacion.
- Cluster 2: clientes de ingreso alto y gasto alto. Edad promedio de 32.88 anos, ingreso de 86.10 k$ y spending score de 81.53. Es el segmento mas atractivo para campanas premium o beneficios exclusivos.
- Cluster 3: clientes de ingreso alto y gasto bajo. Edad promedio de 39.87 anos, ingreso de 86.10 k$ y spending score de 19.36. Tienen capacidad economica, pero no gastan mucho; conviene investigar barreras o activar ofertas mejor dirigidas.
- Cluster 4: clientes de edad mayor, ingreso medio y gasto medio. Edad promedio de 55.64 anos, ingreso de 54.38 k$ y spending score de 48.85. Es un segmento estable, adecuado para comunicacion de mantenimiento, beneficios practicos y retencion.

## Comparacion De Metodos

- Mejor metodo: K-Means.
- Ventajas de K-Means: obtiene mejor silhouette, produce clusters mas faciles de explicar y separa bien los grupos principales en el plano ingreso-gasto.
- Ventajas del segundo metodo: confirma que la estructura general no depende de un solo algoritmo. Tambien encuentra grupos parecidos, aunque con separacion promedio menor.
- Limitaciones encontradas: el dataset es pequeno, solo se usan tres variables, `Genre` queda fuera del modelo base y el silhouette no es muy alto. Eso indica que los clusters existen, pero no estan perfectamente separados.

## Conclusiones

- Hallazgo principal: K-Means con `k=5` es el modelo mas conveniente para el informe porque combina buen desempeno con interpretabilidad. Aunque `k=6` obtiene mejor silhouette, `k=5` facilita explicar los segmentos de negocio.
- Aplicacion de negocio: los segmentos permiten disenar estrategias distintas para clientes de alto valor, clientes con potential no activado, clientes jovenes con alto gasto y clientes de bajo gasto.
- Limitaciones: el analysis se basa en 200 clientes y solo tres variables. Faltan datos de compras reales, frecuencia de visita, categorias compradas, ticket promedio, canal de compra y respuesta historica a promociones.
- Mejoras futuras: probar `k=6`, evaluar DBSCAN, codificar `Genre` en una version alternativa, agregar mas variables de comportamiento y validar los segmentos con resultados reales de campanas o metricas de retencion.
