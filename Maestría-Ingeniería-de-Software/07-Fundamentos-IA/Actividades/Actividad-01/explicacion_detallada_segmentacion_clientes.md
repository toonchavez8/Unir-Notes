# Explicación detallada del análisis de segmentación de clientes

Autor del notebook original: Miguel de Jesus Chavez Barragan  
Dataset usado: `Mall_Customers.csv`  
Archivo base analizado: `segmentacion_clientes.md`

Este documento explica, en español, qué hace cada bloque de código del notebook, cómo lo hace, qué significa cada resultado y cómo se interpretan las imágenes generadas. El orden sigue el markdown original.

## Contexto general del ejercicio

El objetivo del notebook es aplicar aprendizaje no supervisado para segmentar clientes. En aprendizaje no supervisado no se parte de una columna objetivo, como "cliente bueno" o "cliente malo". En lugar de eso, el algoritmo busca patrones internos en los datos y agrupa observaciones parecidas.

En este caso, cada observación es un cliente de un centro comercial. El CSV contiene estas columnas:

| Columna | Significado |
|---|---|
| `CustomerID` | Identificador del cliente. Sirve para distinguir registros, pero no describe comportamiento. |
| `Genre` | Género registrado del cliente: `Male` o `Female`. |
| `Age` | Edad del cliente. |
| `Annual Income (k$)` | Ingreso anual expresado en miles de dólares. Por ejemplo, `15` significa 15 mil dólares. |
| `Spending Score (1-100)` | Puntuación de gasto de 1 a 100. Un valor alto indica mayor gasto o mayor propensión a gastar. |

El dataset tiene 200 clientes y 5 columnas. Para clustering se usan principalmente `Age`, `Annual Income (k$)` y `Spending Score (1-100)`, porque son variables numéricas con significado directo para segmentación.

## 1. Configuración inicial

Código original:

```python
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

BASE_DIR = Path.cwd()
FIGURES_DIR = BASE_DIR / "figuras"
FIGURES_DIR.mkdir(exist_ok=True)

DATASET_PATH = BASE_DIR / "Mall_Customers.csv"
DATASET_PATH
```

### Explicación línea por línea

```python
from pathlib import Path
```

Importa `Path`, una herramienta de Python para trabajar con rutas de archivos y carpetas de forma más clara que usando cadenas de texto simples. Permite escribir rutas compatibles con Windows, macOS y Linux.

```python
import numpy as np
```

Importa `numpy` con el alias `np`. `numpy` se usa para cálculo numérico, arreglos, matrices y operaciones matemáticas eficientes. Aunque en este notebook no aparece mucho código explícito con `np`, muchas librerías de ciencia de datos lo usan por debajo.

```python
import pandas as pd
```

Importa `pandas` con el alias `pd`. `pandas` permite leer el CSV, manipular tablas y calcular resúmenes estadísticos. La estructura principal de pandas es el `DataFrame`.

```python
import matplotlib.pyplot as plt
```

Importa el módulo de gráficos de `matplotlib`. El alias `plt` se usa para crear figuras, títulos, etiquetas y guardar imágenes.

```python
import seaborn as sns
```

Importa `seaborn`, una librería construida sobre matplotlib. Se usa para gráficos estadísticos más limpios, como boxplots, scatterplots y pairplots.

```python
from sklearn.preprocessing import StandardScaler
```

Importa `StandardScaler` desde scikit-learn. Esta clase estandariza variables numéricas para que tengan media 0 y desviación estándar 1. Esto es importante porque los algoritmos de clustering usan distancias; si una variable tiene escala más grande, puede dominar el cálculo.

```python
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
```

Importa tres algoritmos de clustering:

- `KMeans`: separa los datos en `k` grupos usando centroides.
- `AgglomerativeClustering`: crea grupos de forma jerárquica, fusionando puntos o grupos parecidos.
- `DBSCAN`: detecta grupos por densidad y puede marcar puntos como ruido.

En el notebook se usan `KMeans` y `AgglomerativeClustering`. `DBSCAN` se importa como alternativa, pero no se aplica.

```python
from sklearn.metrics import silhouette_score
```

Importa la métrica `silhouette_score`. Esta métrica evalúa qué tan bien separados están los clusters. Sus valores suelen estar entre -1 y 1:

- Cerca de 1: clusters compactos y bien separados.
- Cerca de 0: clusters mezclados o fronteras poco claras.
- Menor que 0: muchos puntos probablemente están en el cluster equivocado.

```python
sns.set_theme(style="whitegrid")
```

Configura el estilo visual de seaborn. `whitegrid` usa fondo blanco con una cuadrícula ligera, útil para leer valores en los gráficos.

```python
plt.rcParams["figure.figsize"] = (8, 5)
```

Define el tamaño por defecto de las figuras de matplotlib: 8 pulgadas de ancho por 5 de alto. Si un gráfico no especifica otro tamaño, usará este.

```python
BASE_DIR = Path.cwd()
```

Guarda en `BASE_DIR` la carpeta actual desde la que se está ejecutando el notebook. `cwd` significa "current working directory".

```python
FIGURES_DIR = BASE_DIR / "figuras"
```

Crea una ruta llamada `FIGURES_DIR` apuntando a una subcarpeta llamada `figuras` dentro del directorio actual.

```python
FIGURES_DIR.mkdir(exist_ok=True)
```

Crea la carpeta `figuras` si no existe. El argumento `exist_ok=True` evita un error si la carpeta ya fue creada antes.

```python
DATASET_PATH = BASE_DIR / "Mall_Customers.csv"
```

Construye la ruta completa hacia el archivo de datos `Mall_Customers.csv`.

```python
DATASET_PATH
```

Al poner una variable como última línea de una celda en Jupyter, el notebook muestra su valor.

### Resultado

```text
WindowsPath('C:/Users/FoodLovers/Documents/Unir-Notes/Maestría-Ingeniería-de-Software/07-Fundamentos-IA/Actividades/Actividad-01/Mall_Customers.csv')
```

Este resultado indica que Python encontró la ruta donde espera leer el CSV. No significa todavía que el archivo fue leído; solo muestra la ruta construida.

## 2. Carga del dataset

Código original:

```python
df = pd.read_csv(DATASET_PATH)
df.head()
```

### Explicación línea por línea

```python
df = pd.read_csv(DATASET_PATH)
```

Lee el archivo CSV ubicado en `DATASET_PATH` y lo guarda en la variable `df`. Esa variable es un `DataFrame`, es decir, una tabla con filas y columnas.

Un detalle importante: en el CSV los IDs aparecen como `0001`, `0002`, etc. Al leerlos con pandas, esos valores se convierten en números enteros (`1`, `2`, etc.) porque pandas infiere que la columna es numérica. Esto no afecta el análisis, porque `CustomerID` no se usa para clustering.

```python
df.head()
```

Muestra las primeras 5 filas del DataFrame. Sirve para revisar rápidamente que el archivo se cargó bien y que las columnas tienen los nombres esperados.

### Resultado

| Índice | CustomerID | Genre | Age | Annual Income (k$) | Spending Score (1-100) |
|---:|---:|---|---:|---:|---:|
| 0 | 1 | Male | 19 | 15 | 39 |
| 1 | 2 | Male | 21 | 15 | 81 |
| 2 | 3 | Female | 20 | 16 | 6 |
| 3 | 4 | Female | 23 | 16 | 77 |
| 4 | 5 | Female | 31 | 17 | 40 |

### Interpretación

Cada fila representa un cliente. En las primeras filas se ve que los ingresos anuales son bajos, entre 15 y 17 mil dólares, pero el gasto varía mucho. Por ejemplo:

- Cliente 1: ingreso 15, gasto 39.
- Cliente 2: mismo ingreso 15, pero gasto 81.
- Cliente 3: ingreso 16, gasto 6.

Esto ya sugiere que el ingreso por sí solo no explica completamente el gasto. Esa es una razón para usar clustering: buscar grupos combinando varias variables.

## 3. Exploración inicial del conjunto de datos

### 3.1 Dimensiones, columnas e información general

Código original:

```python
print("Shape:", df.shape)
print("\nColumnas:")
print(df.columns.tolist())
print("\nInfo:")
df.info()
```

### Explicación línea por línea

```python
print("Shape:", df.shape)
```

Muestra la forma del DataFrame. `df.shape` devuelve una tupla con dos valores: número de filas y número de columnas.

```python
print("\nColumnas:")
```

Imprime el texto `Columnas:`. El `\n` agrega un salto de línea antes del texto para separar visualmente la salida.

```python
print(df.columns.tolist())
```

Obtiene los nombres de las columnas con `df.columns` y los convierte a una lista con `.tolist()`. Esto facilita ver los nombres exactos, incluidos espacios, mayúsculas y paréntesis.

```python
print("\nInfo:")
```

Imprime el texto `Info:` con un salto de línea previo.

```python
df.info()
```

Muestra información técnica del DataFrame: cantidad de filas, cantidad de columnas, valores no nulos por columna, tipo de dato y memoria usada.

### Resultado

```text
Shape: (200, 5)

Columnas:
['CustomerID', 'Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']

Info:
<class 'pandas.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 5 columns):
 #   Column                  Non-Null Count  Dtype
---  ------                  --------------  -----
 0   CustomerID              200 non-null    int64
 1   Genre                   200 non-null    str
 2   Age                     200 non-null    int64
 3   Annual Income (k$)      200 non-null    int64
 4   Spending Score (1-100)  200 non-null    int64
dtypes: int64(4), str(1)
memory usage: 7.9 KB
```

### Interpretación

El dataset tiene 200 filas y 5 columnas. Hay 200 valores no nulos en cada columna, así que no aparecen datos faltantes en esta revisión inicial.

Los tipos de dato son:

- `int64` para `CustomerID`, `Age`, `Annual Income (k$)` y `Spending Score (1-100)`.
- `str` para `Genre`.

Para los algoritmos usados aquí, las variables numéricas son más directas. `Genre` podría codificarse más adelante, pero en este notebook se deja fuera del clustering principal.

### 3.2 Revisión de valores nulos

Código original:

```python
df.isnull().sum()
```

### Explicación línea por línea

```python
df.isnull()
```

Evalúa cada celda del DataFrame y devuelve `True` si el valor es nulo y `False` si no lo es.

```python
.sum()
```

Suma los valores `True` por columna. En Python, `True` cuenta como 1 y `False` como 0. Por eso el resultado indica cuántos nulos hay por columna.

### Resultado

```text
CustomerID                0
Genre                     0
Age                       0
Annual Income (k$)        0
Spending Score (1-100)    0
dtype: int64
```

### Interpretación

No hay valores nulos. Esto simplifica el preprocesamiento porque no hace falta imputar datos, eliminar filas incompletas ni crear reglas para manejar valores faltantes.

### 3.3 Estadísticas descriptivas

Código original:

```python
df.describe(include="all")
```

### Explicación línea por línea

```python
df.describe()
```

Calcula estadísticas descriptivas. Para columnas numéricas incluye conteo, media, desviación estándar, mínimo, cuartiles y máximo.

```python
include="all"
```

Indica que también se incluyan columnas no numéricas, como `Genre`. Para columnas categóricas se muestran valores como `unique`, `top` y `freq`.

### Resultado principal

| Estadística | CustomerID | Genre | Age | Annual Income (k$) | Spending Score (1-100) |
|---|---:|---|---:|---:|---:|
| count | 200 | 200 | 200 | 200 | 200 |
| unique | NaN | 2 | NaN | NaN | NaN |
| top | NaN | Female | NaN | NaN | NaN |
| freq | NaN | 112 | NaN | NaN | NaN |
| mean | 100.50 | NaN | 38.85 | 60.56 | 50.20 |
| std | 57.88 | NaN | 13.97 | 26.26 | 25.82 |
| min | 1.00 | NaN | 18.00 | 15.00 | 1.00 |
| 25% | 50.75 | NaN | 28.75 | 41.50 | 34.75 |
| 50% | 100.50 | NaN | 36.00 | 61.50 | 50.00 |
| 75% | 150.25 | NaN | 49.00 | 78.00 | 73.00 |
| max | 200.00 | NaN | 70.00 | 137.00 | 99.00 |

### Interpretación

`Genre` tiene 2 categorías. La categoría más frecuente es `Female`, con 112 registros.

En `Age`, la edad promedio es 38.85 años. La edad mínima es 18 y la máxima 70. La mediana es 36, lo cual indica que la mitad de los clientes tiene 36 años o menos.

En `Annual Income (k$)`, el ingreso anual promedio es 60.56 mil dólares. El mínimo es 15 y el máximo 137. La mediana es 61.5, muy cercana a la media, aunque hay algunos ingresos altos que se observan mejor en los gráficos.

En `Spending Score (1-100)`, el promedio es 50.20. El rango va de 1 a 99, casi todo el rango posible de la escala. Esto indica bastante variabilidad en el comportamiento de gasto.

`CustomerID` no debe interpretarse estadísticamente como una variable de negocio. Su media, mínimo o máximo solo reflejan que es un identificador consecutivo.

## 4. Análisis exploratorio visual

### 4.1 Histogramas de variables numéricas

Código original:

```python
numeric_cols = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

df[numeric_cols].hist(figsize=(10, 6))
plt.tight_layout()
plt.savefig(FIGURES_DIR / "histogramas_variables.png", dpi=300)
plt.show()
```

### Explicación línea por línea

```python
numeric_cols = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
```

Crea una lista con las columnas numéricas que se van a analizar visualmente. Se excluye `CustomerID` porque no representa una característica real del cliente.

```python
df[numeric_cols]
```

Selecciona del DataFrame solo las columnas indicadas en `numeric_cols`.

```python
.hist(figsize=(10, 6))
```

Genera histogramas para cada columna seleccionada. Un histograma divide los valores en intervalos y muestra cuántos datos caen en cada intervalo.

```python
plt.tight_layout()
```

Ajusta los espacios entre subgráficos para evitar que títulos, ejes o etiquetas se encimen.

```python
plt.savefig(FIGURES_DIR / "histogramas_variables.png", dpi=300)
```

Guarda la figura en la carpeta `figuras` con el nombre `histogramas_variables.png`. `dpi=300` indica buena resolución para reporte o impresión.

```python
plt.show()
```

Muestra el gráfico en el notebook.

### Imagen generada

![Histogramas de variables numéricas](output_10_0.png)

### Interpretación de la imagen

El histograma de `Age` muestra clientes desde 18 hasta 70 años. Hay concentración importante en edades jóvenes y adultas tempranas, especialmente entre los 20 y 40 años, aunque también aparecen clientes mayores.

El histograma de `Annual Income (k$)` muestra que muchos clientes tienen ingresos entre 40 y 85 mil dólares. También hay clientes con ingresos más bajos, cerca de 15 a 30, y algunos con ingresos altos por encima de 100.

El histograma de `Spending Score (1-100)` muestra valores repartidos casi en todo el rango. Se observa una concentración cerca de 40 a 60, pero también hay clientes con gasto muy bajo y muy alto. Esto es útil para segmentación porque existen diferencias reales de comportamiento.

### 4.2 Boxplots de variables numéricas

Código original:

```python
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[numeric_cols])
plt.title("Boxplots de variables numéricas")
plt.savefig(FIGURES_DIR / "boxplots_variables.png", dpi=300)
plt.show()
```

### Explicación línea por línea

```python
plt.figure(figsize=(10, 5))
```

Crea una nueva figura de 10 pulgadas de ancho por 5 de alto.

```python
sns.boxplot(data=df[numeric_cols])
```

Crea boxplots para las columnas numéricas. Un boxplot resume la distribución de una variable con mediana, cuartiles, rango y posibles valores atípicos.

```python
plt.title("Boxplots de variables numéricas")
```

Agrega el título del gráfico.

```python
plt.savefig(FIGURES_DIR / "boxplots_variables.png", dpi=300)
```

Guarda el gráfico en la carpeta `figuras`.

```python
plt.show()
```

Muestra el gráfico.

### Imagen generada

![Boxplots de variables numéricas](output_11_0.png)

### Interpretación de la imagen

El boxplot de `Age` muestra una mediana cercana a 36 años. La caja cubre aproximadamente desde finales de los 20 hasta cerca de 49 años. No se observan valores atípicos importantes en edad.

El boxplot de `Annual Income (k$)` muestra una mediana cercana a 61.5. Aparece un punto atípico cerca de 137, lo que indica un cliente con ingreso anual bastante más alto que la mayoría.

El boxplot de `Spending Score (1-100)` tiene una mediana cercana a 50. La caja es amplia, lo que confirma que hay mucha variación en el gasto. No se observan atípicos marcados en esta variable.

Esta revisión ayuda a anticipar por qué conviene escalar las variables: sus rangos no son iguales. `Age` va de 18 a 70, `Annual Income` de 15 a 137 y `Spending Score` de 1 a 99.

### 4.3 Dispersión entre ingreso anual y puntuación de gasto

Código original:

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Annual Income (k$)", y="Spending Score (1-100)")
plt.title("Ingreso anual vs puntuación de gasto")
plt.savefig("figuras/scatter_ingreso_gasto.png", dpi=300)
plt.show()
```

### Explicación línea por línea

```python
plt.figure(figsize=(8, 6))
```

Crea una figura nueva de 8 por 6 pulgadas.

```python
sns.scatterplot(data=df, x="Annual Income (k$)", y="Spending Score (1-100)")
```

Crea un gráfico de dispersión. Cada punto representa un cliente. El eje X muestra ingreso anual y el eje Y muestra puntuación de gasto.

```python
plt.title("Ingreso anual vs puntuación de gasto")
```

Agrega el título del gráfico.

```python
plt.savefig("figuras/scatter_ingreso_gasto.png", dpi=300)
```

Guarda la imagen en la carpeta `figuras`. Aquí se usa la ruta como texto, en lugar de usar `FIGURES_DIR`. Funciona porque la carpeta `figuras` ya fue creada.

```python
plt.show()
```

Muestra el gráfico.

### Imagen generada

![Ingreso anual vs puntuación de gasto](output_12_0.png)

### Interpretación de la imagen

Este gráfico es uno de los más importantes del análisis. Muestra que los clientes no están distribuidos como una nube completamente aleatoria. Hay zonas reconocibles:

- Ingreso bajo y gasto bajo.
- Ingreso bajo y gasto alto.
- Ingreso medio y gasto medio.
- Ingreso alto y gasto bajo.
- Ingreso alto y gasto alto.

Estas zonas son candidatas naturales para clusters. Por ejemplo, los clientes de ingreso alto y gasto alto pueden ser un segmento atractivo para campañas premium. En cambio, los clientes de ingreso alto y gasto bajo podrían requerir estrategias de activación o fidelización distintas.

### 4.4 Pairplot de variables numéricas

Código original:

```python
sns.pairplot(df[numeric_cols])
plt.savefig(FIGURES_DIR / "pairplot_variables.png", dpi=300)
plt.show()
```

### Explicación línea por línea

```python
sns.pairplot(df[numeric_cols])
```

Crea una matriz de gráficos. En la diagonal aparecen histogramas de cada variable. Fuera de la diagonal aparecen gráficos de dispersión comparando cada par de variables.

```python
plt.savefig(FIGURES_DIR / "pairplot_variables.png", dpi=300)
```

Guarda el pairplot en la carpeta `figuras`.

```python
plt.show()
```

Muestra la figura.

### Imagen generada

![Pairplot de variables numéricas](output_13_0.png)

### Interpretación de la imagen

El pairplot permite revisar relaciones entre todas las variables numéricas al mismo tiempo.

La relación más clara aparece entre `Annual Income (k$)` y `Spending Score (1-100)`. Se ven regiones separadas que luego los algoritmos de clustering intentan formalizar.

La relación entre `Age` y `Spending Score` sugiere que muchos clientes jóvenes tienen puntuaciones de gasto altas o medias, mientras que clientes mayores tienden a concentrarse más en gasto medio o bajo. No es una regla absoluta, pero sí un patrón visible.

La relación entre `Age` e `Annual Income` no muestra una separación tan fuerte. Por eso edad ayuda, pero no parece ser la variable que más define los grupos visualmente.

## 5. Preprocesamiento

### 5.1 Selección de variables

Código original:

```python
features = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
X = df[features].copy()
X.head()
```

### Explicación línea por línea

```python
features = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
```

Define las columnas que se usarán para entrenar los algoritmos de clustering.

Se excluye `CustomerID` porque es un identificador. Incluirlo sería un error: el algoritmo podría interpretar que clientes con IDs cercanos son más parecidos, cuando el ID solo representa el orden del registro.

Se excluye `Genre` porque es una variable categórica. Para usarla correctamente habría que transformarla a variables numéricas, por ejemplo con one-hot encoding. El notebook mantiene el análisis base con variables numéricas directas.

```python
X = df[features].copy()
```

Crea un nuevo DataFrame llamado `X` con solo las columnas de entrada del modelo. `.copy()` crea una copia independiente para evitar efectos secundarios sobre `df`.

```python
X.head()
```

Muestra las primeras cinco filas de `X`.

### Resultado

| Índice | Age | Annual Income (k$) | Spending Score (1-100) |
|---:|---:|---:|---:|
| 0 | 19 | 15 | 39 |
| 1 | 21 | 15 | 81 |
| 2 | 20 | 16 | 6 |
| 3 | 23 | 16 | 77 |
| 4 | 31 | 17 | 40 |

### Interpretación

`X` contiene únicamente las variables que describen al cliente en términos de edad, ingreso y gasto. Esta tabla es la entrada real para los algoritmos de clustering.

### 5.2 Estandarización

Código original:

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled[:5]
```

### Explicación línea por línea

```python
scaler = StandardScaler()
```

Crea un objeto `StandardScaler`. Este objeto aprenderá la media y desviación estándar de cada variable.

```python
X_scaled = scaler.fit_transform(X)
```

Hace dos cosas:

- `fit`: calcula la media y desviación estándar de cada columna.
- `transform`: convierte cada valor usando la fórmula:

```text
valor_estandarizado = (valor_original - media) / desviación_estándar
```

El resultado es una matriz numérica donde cada columna queda en una escala comparable.

```python
X_scaled[:5]
```

Muestra las primeras cinco filas de la matriz escalada.

### Resultado

```text
array([[-1.42456879, -1.73899919, -0.43480148],
       [-1.28103541, -1.73899919,  1.19570407],
       [-1.3528021 , -1.70082976, -1.71591298],
       [-1.13750203, -1.70082976,  1.04041783],
       [-0.56336851, -1.66266033, -0.39597992]])
```

### Interpretación

Cada fila sigue representando un cliente, pero los valores ya no están en años, miles de dólares o escala 1-100. Ahora están expresados como distancia respecto a la media de su variable.

Por ejemplo, en la primera fila:

- `-1.42456879` en edad significa que el cliente está bastante por debajo de la edad promedio.
- `-1.73899919` en ingreso significa que su ingreso está muy por debajo del promedio.
- `-0.43480148` en gasto significa que su gasto está un poco por debajo del promedio.

El escalado es necesario porque K-Means y Agglomerative Clustering dependen de distancias. Sin escalado, una variable con mayor rango podría pesar más aunque no sea más importante.

## 6. Búsqueda del número óptimo de clusters para K-Means

### 6.1 Cálculo de inercia y silhouette

Código original:

```python
k_values = range(2, 11)
inertia = []
silhouette_scores = []

for k in k_values:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    inertia.append(model.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, labels))

metrics_kmeans = pd.DataFrame({
    "k": list(k_values),
    "inertia": inertia,
    "silhouette": silhouette_scores
})
metrics_kmeans
```

### Explicación línea por línea

```python
k_values = range(2, 11)
```

Crea una secuencia de valores de `k` desde 2 hasta 10. En Python, `range(2, 11)` incluye 2 y excluye 11, por eso el último valor es 10.

No se prueba `k=1` porque con un solo cluster no hay segmentación real y no se puede calcular silhouette de forma útil.

```python
inertia = []
```

Crea una lista vacía para guardar la inercia obtenida con cada valor de `k`.

```python
silhouette_scores = []
```

Crea una lista vacía para guardar el silhouette score de cada modelo.

```python
for k in k_values:
```

Inicia un ciclo. El bloque se repite una vez por cada valor de `k`: 2, 3, 4, ..., 10.

```python
model = KMeans(n_clusters=k, random_state=42, n_init=10)
```

Crea un modelo K-Means con `k` clusters.

- `n_clusters=k`: indica cuántos grupos debe formar.
- `random_state=42`: fija la semilla aleatoria para que los resultados sean reproducibles.
- `n_init=10`: ejecuta K-Means 10 veces con diferentes inicializaciones y conserva la mejor solución según inercia.

```python
labels = model.fit_predict(X_scaled)
```

Entrena el modelo con `X_scaled` y devuelve la etiqueta de cluster asignada a cada cliente.

- `fit` ajusta los centroides.
- `predict` asigna cada punto al centroide más cercano.
- `fit_predict` hace ambas cosas en una sola llamada.

```python
inertia.append(model.inertia_)
```

Agrega a la lista `inertia` la inercia del modelo. La inercia mide la suma de distancias cuadradas entre cada punto y el centroide de su cluster.

Una inercia menor indica que los puntos están más cerca de sus centroides. Pero la inercia siempre baja cuando aumenta `k`, por eso no basta con escoger el menor valor.

```python
silhouette_scores.append(silhouette_score(X_scaled, labels))
```

Calcula el silhouette score usando los datos escalados y las etiquetas generadas. Después guarda el valor en la lista.

```python
metrics_kmeans = pd.DataFrame({
    "k": list(k_values),
    "inertia": inertia,
    "silhouette": silhouette_scores
})
```

Crea un DataFrame con tres columnas:

- `k`: número de clusters probado.
- `inertia`: compactación interna de los clusters.
- `silhouette`: separación y coherencia de los clusters.

```python
metrics_kmeans
```

Muestra la tabla de métricas.

### Resultado

| k | inertia | silhouette |
|---:|---:|---:|
| 2 | 389.386189 | 0.335472 |
| 3 | 295.212246 | 0.357793 |
| 4 | 205.225147 | 0.403958 |
| 5 | 168.247580 | 0.416643 |
| 6 | 133.868421 | 0.428417 |
| 7 | 117.011555 | 0.417232 |
| 8 | 103.873292 | 0.408207 |
| 9 | 93.092891 | 0.417693 |
| 10 | 82.385154 | 0.406554 |

### Interpretación

La inercia baja conforme aumenta `k`, lo cual es esperado. Con más clusters, cada centroide cubre menos puntos y las distancias internas se reducen.

El silhouette score sube desde `k=2` hasta `k=6`, donde alcanza el valor más alto: `0.428417`. Después fluctúa. El valor de `k=5` es `0.416643`, que está cerca del máximo y produce una segmentación más simple.

Esto plantea una decisión práctica:

- `k=6` tiene la mejor métrica silhouette en esta tabla.
- `k=5` tiene una interpretación de negocio más clara y coincide con la estructura visual típica del gráfico ingreso-gasto.

El notebook elige `best_k = 5`, una decisión razonable si se prioriza interpretabilidad.

### 6.2 Método del codo

Código original:

```python
plt.plot(metrics_kmeans["k"], metrics_kmeans["inertia"], marker="o")
plt.title("Elbow Method")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Inercia")
plt.savefig(FIGURES_DIR / "elbow_method.png", dpi=300)
plt.show()
```

### Explicación línea por línea

```python
plt.plot(metrics_kmeans["k"], metrics_kmeans["inertia"], marker="o")
```

Crea una gráfica de línea con `k` en el eje X e inercia en el eje Y. `marker="o"` dibuja un círculo en cada punto medido.

```python
plt.title("Elbow Method")
```

Agrega el título del gráfico.

```python
plt.xlabel("Número de clusters (k)")
```

Etiqueta el eje X.

```python
plt.ylabel("Inercia")
```

Etiqueta el eje Y.

```python
plt.savefig(FIGURES_DIR / "elbow_method.png", dpi=300)
```

Guarda la gráfica.

```python
plt.show()
```

Muestra la gráfica.

### Imagen generada

![Método del codo](output_19_0.png)

### Interpretación de la imagen

El método del codo busca el punto donde la reducción de inercia empieza a ser menos pronunciada. En la gráfica, la caída es fuerte de `k=2` a `k=4`. Después la curva sigue bajando, pero con menor intensidad.

El "codo" visual puede defenderse alrededor de `k=4`, `k=5` o `k=6`. No hay un único punto perfecto. Por eso se usa también silhouette score.

### 6.3 Silhouette score por número de clusters

Código original:

```python
plt.plot(metrics_kmeans["k"], metrics_kmeans["silhouette"], marker="o")
plt.title("Silhouette Score por número de clusters")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Silhouette Score")
plt.savefig(FIGURES_DIR / "silhouette_scores.png", dpi=300)
plt.show()
```

### Explicación línea por línea

```python
plt.plot(metrics_kmeans["k"], metrics_kmeans["silhouette"], marker="o")
```

Crea una gráfica de línea con `k` en el eje X y silhouette score en el eje Y.

```python
plt.title("Silhouette Score por número de clusters")
```

Agrega el título.

```python
plt.xlabel("Número de clusters (k)")
```

Etiqueta el eje X.

```python
plt.ylabel("Silhouette Score")
```

Etiqueta el eje Y.

```python
plt.savefig(FIGURES_DIR / "silhouette_scores.png", dpi=300)
```

Guarda la imagen.

```python
plt.show()
```

Muestra la gráfica.

### Imagen generada

![Silhouette Score por número de clusters](output_20_0.png)

### Interpretación de la imagen

La gráfica muestra que el mejor valor se alcanza con `k=6`. Sin embargo, `k=5`, `k=7` y `k=9` están relativamente cerca.

El valor de silhouette para `k=5` no es perfecto, pero sí aceptable para un dataset pequeño y con clusters parcialmente superpuestos. Además, `k=5` permite interpretar los grupos de forma más sencilla:

- Bajo ingreso y bajo gasto.
- Bajo o medio ingreso y gasto medio-alto.
- Alto ingreso y alto gasto.
- Alto ingreso y bajo gasto.
- Clientes de edad mayor con gasto medio.

## 7. Entrenamiento del modelo K-Means final

### 7.1 Ajuste final del modelo

Código original:

```python
best_k = 5

kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df["cluster_kmeans"] = kmeans.fit_predict(X_scaled)
df[["cluster_kmeans"] + features].head()
```

### Explicación línea por línea

```python
best_k = 5
```

Define que el modelo final usará 5 clusters. Esta variable se usa para no escribir el número directamente en varias partes del código.

```python
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
```

Crea el modelo K-Means final con 5 clusters.

```python
df["cluster_kmeans"] = kmeans.fit_predict(X_scaled)
```

Entrena el modelo con los datos escalados y agrega al DataFrame original una nueva columna llamada `cluster_kmeans`.

Cada cliente recibe una etiqueta numérica de cluster. Es importante entender que esas etiquetas son nombres arbitrarios. El cluster `0` no es "mejor" ni "menor" que el cluster `1`; solo es una etiqueta.

```python
df[["cluster_kmeans"] + features].head()
```

Muestra las primeras cinco filas con la etiqueta de cluster y las variables usadas para entrenar.

`["cluster_kmeans"] + features` une dos listas. El resultado es:

```python
["cluster_kmeans", "Age", "Annual Income (k$)", "Spending Score (1-100)"]
```

### Resultado

| Índice | cluster_kmeans | Age | Annual Income (k$) | Spending Score (1-100) |
|---:|---:|---:|---:|---:|
| 0 | 1 | 19 | 15 | 39 |
| 1 | 1 | 21 | 15 | 81 |
| 2 | 0 | 20 | 16 | 6 |
| 3 | 1 | 23 | 16 | 77 |
| 4 | 1 | 31 | 17 | 40 |

### Interpretación

Los primeros clientes se asignan principalmente a los clusters `1` y `0`.

El cliente con índice 2 tiene ingreso bajo y gasto muy bajo, por eso cae en un grupo diferente al cliente con índice 1, que tiene ingreso bajo pero gasto alto. Esto muestra la lógica central del clustering: no agrupa solo por ingreso, sino por la combinación de edad, ingreso y gasto.

### 7.2 Visualización de clusters K-Means

Código original:

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="cluster_kmeans",
    palette="tab10"
)
plt.title("Clusters obtenidos con K-Means")
plt.savefig(FIGURES_DIR / "kmeans_clusters.png", dpi=300)
plt.show()
```

### Explicación línea por línea

```python
plt.figure(figsize=(8, 6))
```

Crea una figura nueva.

```python
sns.scatterplot(
```

Inicia la llamada a `scatterplot`.

```python
data=df,
```

Indica que los datos vienen del DataFrame `df`.

```python
x="Annual Income (k$)",
```

Usa el ingreso anual en el eje X.

```python
y="Spending Score (1-100)",
```

Usa la puntuación de gasto en el eje Y.

```python
hue="cluster_kmeans",
```

Colorea los puntos según el cluster asignado por K-Means.

```python
palette="tab10"
```

Usa la paleta de colores `tab10`, útil para categorías discretas.

```python
)
```

Cierra la llamada a `scatterplot`.

```python
plt.title("Clusters obtenidos con K-Means")
```

Agrega el título.

```python
plt.savefig(FIGURES_DIR / "kmeans_clusters.png", dpi=300)
```

Guarda la imagen.

```python
plt.show()
```

Muestra la imagen.

### Imagen generada

![Clusters obtenidos con K-Means](output_23_0.png)

### Interpretación de la imagen

K-Means separa los clientes en cinco grupos visibles:

| Cluster | Lectura visual | Interpretación de negocio |
|---:|---|---|
| 0 | Ingreso bajo y gasto bajo | Clientes con bajo poder adquisitivo o bajo interés de compra. |
| 1 | Ingreso bajo/medio y gasto medio-alto | Clientes jóvenes o activos con gasto relativamente alto pese a ingresos menores. |
| 2 | Ingreso alto y gasto alto | Segmento premium: buen ingreso y alta disposición a gastar. |
| 3 | Ingreso alto y gasto bajo | Clientes con capacidad económica, pero bajo gasto registrado. |
| 4 | Zona media, gasto medio | Clientes más moderados, con comportamiento estable o promedio. |

El gráfico usa solo ingreso y gasto en los ejes, aunque el modelo también usó edad. Por eso algunos puntos pueden parecer mezclados en 2D, pero estar separados en el espacio de tres variables.

## 8. Segundo algoritmo de clustering

### 8.1 Agglomerative Clustering y comparación de silhouette

Código original:

```python
agg = AgglomerativeClustering(n_clusters=best_k)
df["cluster_agg"] = agg.fit_predict(X_scaled)

silhouette_kmeans = silhouette_score(X_scaled, df["cluster_kmeans"])
silhouette_agg = silhouette_score(X_scaled, df["cluster_agg"])

print("Silhouette K-Means:", silhouette_kmeans)
print("Silhouette Agglomerative:", silhouette_agg)
```

### Explicación línea por línea

```python
agg = AgglomerativeClustering(n_clusters=best_k)
```

Crea un modelo de clustering jerárquico aglomerativo con 5 clusters.

Este algoritmo empieza considerando cada punto como su propio grupo y después va fusionando los grupos más parecidos hasta llegar al número de clusters solicitado.

```python
df["cluster_agg"] = agg.fit_predict(X_scaled)
```

Entrena el modelo jerárquico y guarda las etiquetas de cluster en una nueva columna llamada `cluster_agg`.

```python
silhouette_kmeans = silhouette_score(X_scaled, df["cluster_kmeans"])
```

Calcula el silhouette score para las etiquetas generadas por K-Means.

```python
silhouette_agg = silhouette_score(X_scaled, df["cluster_agg"])
```

Calcula el silhouette score para las etiquetas generadas por Agglomerative Clustering.

```python
print("Silhouette K-Means:", silhouette_kmeans)
```

Imprime el puntaje de K-Means.

```python
print("Silhouette Agglomerative:", silhouette_agg)
```

Imprime el puntaje del modelo jerárquico.

### Resultado

```text
Silhouette K-Means: 0.41664341513732767
Silhouette Agglomerative: 0.39002826186267214
```

### Interpretación

K-Means obtiene un silhouette score mayor que Agglomerative Clustering:

- K-Means: `0.4166`
- Agglomerative: `0.3900`

La diferencia no es enorme, pero K-Means tiene mejor separación promedio de clusters en este análisis. Por esa razón, si se debe elegir un modelo principal, K-Means es la opción más fuerte en este notebook.

### 8.2 Visualización de Agglomerative Clustering

Código original:

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="cluster_agg",
    palette="Set2"
)
plt.title("Clusters obtenidos con Agglomerative Clustering")
plt.savefig(FIGURES_DIR / "agglomerative_clusters.png", dpi=300)
plt.show()
```

### Explicación línea por línea

```python
plt.figure(figsize=(8, 6))
```

Crea una nueva figura.

```python
sns.scatterplot(
```

Inicia un gráfico de dispersión.

```python
data=df,
```

Usa `df` como fuente de datos.

```python
x="Annual Income (k$)",
```

Coloca ingreso anual en el eje X.

```python
y="Spending Score (1-100)",
```

Coloca puntuación de gasto en el eje Y.

```python
hue="cluster_agg",
```

Colorea cada punto según el cluster asignado por el algoritmo jerárquico.

```python
palette="Set2"
```

Usa la paleta `Set2`, que ofrece colores suaves para categorías.

```python
)
```

Cierra la llamada al gráfico.

```python
plt.title("Clusters obtenidos con Agglomerative Clustering")
```

Agrega el título.

```python
plt.savefig(FIGURES_DIR / "agglomerative_clusters.png", dpi=300)
```

Guarda la imagen.

```python
plt.show()
```

Muestra el gráfico.

### Imagen generada

![Clusters obtenidos con Agglomerative Clustering](output_26_0.png)

### Interpretación de la imagen

Agglomerative Clustering también identifica cinco grupos parecidos a los de K-Means:

- Un grupo de ingreso alto y gasto alto.
- Un grupo de ingreso alto y gasto bajo.
- Un grupo de ingreso bajo y gasto bajo.
- Un grupo de ingreso bajo/medio con gasto alto o medio.
- Un grupo central de ingreso medio y gasto medio.

La diferencia es que el algoritmo jerárquico divide algunas zonas centrales de manera distinta. Visualmente, algunos puntos del centro quedan repartidos de forma menos limpia que en K-Means. Esto coincide con su silhouette score más bajo.

## 9. Resumen e interpretación de clusters

### 9.1 Resumen de K-Means

Código original:

```python
summary_kmeans = df.groupby("cluster_kmeans")[features].mean().round(2)
summary_kmeans["size"] = df["cluster_kmeans"].value_counts().sort_index()
summary_kmeans
summary_kmeans.to_csv("resumen_clusters_kmeans.csv")
```

### Explicación línea por línea

```python
summary_kmeans = df.groupby("cluster_kmeans")[features].mean().round(2)
```

Agrupa los datos por `cluster_kmeans`, selecciona las variables usadas en el modelo y calcula el promedio de cada variable dentro de cada cluster.

`.round(2)` redondea los resultados a dos decimales para que sean más fáciles de leer.

```python
summary_kmeans["size"] = df["cluster_kmeans"].value_counts().sort_index()
```

Agrega una columna llamada `size` con el número de clientes en cada cluster.

- `value_counts()` cuenta cuántas veces aparece cada etiqueta de cluster.
- `sort_index()` ordena los clusters por número de etiqueta.

```python
summary_kmeans
```

Muestra el resumen en el notebook. En el markdown exportado no aparece la tabla porque la siguiente línea también se ejecutó en la misma celda y el último valor evaluado fue `to_csv`.

```python
summary_kmeans.to_csv("resumen_clusters_kmeans.csv")
```

Guarda el resumen de K-Means en un archivo CSV llamado `resumen_clusters_kmeans.csv`.

### Resultado esperado del resumen K-Means

Con las etiquetas que aparecen en la gráfica del notebook, el resumen interpretativo de K-Means queda así:

| cluster_kmeans | Age | Annual Income (k$) | Spending Score (1-100) | size |
|---:|---:|---:|---:|---:|
| 0 | 46.25 | 26.75 | 18.35 | 20 |
| 1 | 25.19 | 41.09 | 62.24 | 54 |
| 2 | 32.88 | 86.10 | 81.53 | 40 |
| 3 | 39.87 | 86.10 | 19.36 | 39 |
| 4 | 55.64 | 54.38 | 48.85 | 47 |

### Interpretación de los clusters K-Means

Cluster `0`: clientes de ingreso bajo y gasto bajo.  
Promedian 46.25 años, 26.75 mil dólares de ingreso anual y 18.35 de puntuación de gasto. Es un segmento pequeño de 20 clientes. Puede representar compradores sensibles al precio, con bajo consumo o baja afinidad con el centro comercial.

Cluster `1`: clientes jóvenes con gasto medio-alto.  
Promedian 25.19 años, 41.09 mil dólares de ingreso anual y 62.24 de gasto. Es el grupo más grande, con 54 clientes. Aunque no tienen los ingresos más altos, gastan por encima del promedio. Puede ser útil para promociones, experiencias, programas de lealtad o productos accesibles.

Cluster `2`: clientes de alto valor.  
Promedian 32.88 años, 86.10 mil dólares de ingreso y 81.53 de gasto. Tiene 40 clientes. Este grupo es atractivo porque combina alto ingreso y alta puntuación de gasto. Puede responder bien a campañas premium, membresías, recomendaciones personalizadas y beneficios exclusivos.

Cluster `3`: clientes con alto ingreso y bajo gasto.  
Promedian 39.87 años, 86.10 mil dólares de ingreso y 19.36 de gasto. Tiene 39 clientes. Es un segmento con potencial económico, pero baja conversión o baja frecuencia de gasto. Puede requerir estrategias de activación, ofertas específicas o análisis adicional para entender por qué no gastan más.

Cluster `4`: clientes mayores con comportamiento medio.  
Promedian 55.64 años, 54.38 mil dólares de ingreso y 48.85 de gasto. Tiene 47 clientes. Es un grupo estable, de ingreso medio y gasto cercano al promedio. Puede funcionar bien con campañas de mantenimiento, comunicación clara y beneficios prácticos.

### 9.2 Resumen de Agglomerative Clustering

Código original:

```python
summary_agg = df.groupby("cluster_agg")[features].mean().round(2)
summary_agg["size"] = df["cluster_agg"].value_counts().sort_index()
summary_agg.to_csv(FIGURES_DIR / "resumen_clusters_agg.csv")
summary_agg
```

### Explicación línea por línea

```python
summary_agg = df.groupby("cluster_agg")[features].mean().round(2)
```

Agrupa los datos por las etiquetas generadas por Agglomerative Clustering y calcula los promedios de edad, ingreso y gasto.

```python
summary_agg["size"] = df["cluster_agg"].value_counts().sort_index()
```

Agrega el tamaño de cada cluster.

```python
summary_agg.to_csv(FIGURES_DIR / "resumen_clusters_agg.csv")
```

Guarda el resumen en un CSV dentro de la carpeta `figuras`.

```python
summary_agg
```

Muestra el resumen en el notebook.

### Resultado

| cluster_agg | Age | Annual Income (k$) | Spending Score (1-100) | size |
|---:|---:|---:|---:|---:|
| 0 | 26.56 | 47.36 | 56.79 | 66 |
| 1 | 56.40 | 55.29 | 48.36 | 45 |
| 2 | 32.69 | 86.54 | 82.13 | 39 |
| 3 | 43.89 | 91.29 | 16.68 | 28 |
| 4 | 44.32 | 25.77 | 20.27 | 22 |

### Interpretación de los clusters jerárquicos

Cluster `0`: clientes jóvenes o adultos jóvenes con ingreso medio y gasto medio-alto.  
Es el grupo más grande, con 66 clientes. Tiene edad promedio 26.56, ingreso 47.36 y gasto 56.79.

Cluster `1`: clientes mayores con ingreso y gasto medios.  
Tiene 45 clientes, edad promedio 56.40, ingreso 55.29 y gasto 48.36. Es parecido al cluster medio de K-Means.

Cluster `2`: clientes de alto ingreso y alto gasto.  
Tiene 39 clientes, ingreso promedio 86.54 y gasto 82.13. Es el segmento más valioso comercialmente.

Cluster `3`: clientes de alto ingreso y bajo gasto.  
Tiene 28 clientes, ingreso promedio 91.29 y gasto 16.68. Es un grupo con capacidad económica, pero baja puntuación de gasto.

Cluster `4`: clientes de bajo ingreso y bajo gasto.  
Tiene 22 clientes, ingreso promedio 25.77 y gasto 20.27. Representa un segmento de bajo consumo.

## 10. Comparación de algoritmos

Código original:

```python
comparison = pd.DataFrame([
    {
        "Metodo": "K-Means",
        "Numero_clusters": df["cluster_kmeans"].nunique(),
        "Silhouette": silhouette_kmeans,
        "Observacion": "Simple y fácil de interpretar"
    },
    {
        "Metodo": "Agglomerative",
        "Numero_clusters": df["cluster_agg"].nunique(),
        "Silhouette": silhouette_agg,
        "Observacion": "Útil para comparación jerárquica"
    }
])
comparison
```

### Explicación línea por línea

```python
comparison = pd.DataFrame([
```

Crea un DataFrame a partir de una lista de diccionarios. Cada diccionario será una fila de la tabla.

```python
{
    "Metodo": "K-Means",
    "Numero_clusters": df["cluster_kmeans"].nunique(),
    "Silhouette": silhouette_kmeans,
    "Observacion": "Simple y fácil de interpretar"
},
```

Define la fila para K-Means.

- `"Metodo": "K-Means"` nombra el algoritmo.
- `df["cluster_kmeans"].nunique()` cuenta cuántos clusters distintos generó.
- `"Silhouette": silhouette_kmeans` agrega la métrica calculada.
- `"Observacion": "Simple y fácil de interpretar"` resume su ventaja principal.

```python
{
    "Metodo": "Agglomerative",
    "Numero_clusters": df["cluster_agg"].nunique(),
    "Silhouette": silhouette_agg,
    "Observacion": "Útil para comparación jerárquica"
}
```

Define la fila para Agglomerative Clustering.

```python
])
```

Cierra la lista y la creación del DataFrame.

```python
comparison
```

Muestra la tabla comparativa.

### Resultado

| Método | Número de clusters | Silhouette | Observación |
|---|---:|---:|---|
| K-Means | 5 | 0.416643 | Simple y fácil de interpretar |
| Agglomerative | 5 | 0.390028 | Útil para comparación jerárquica |

### Interpretación

Ambos algoritmos usan 5 clusters, así que la comparación es justa en términos de número de grupos.

K-Means obtiene mejor silhouette score. Esto significa que, en promedio, sus clusters están un poco mejor separados y sus puntos están algo más cerca de su propio grupo que de otros grupos.

Agglomerative Clustering sigue siendo útil porque confirma que la estructura general de los datos no depende de un solo algoritmo. Aunque cambia algunos puntos de grupo, vuelve a encontrar segmentos parecidos: alto ingreso-alto gasto, alto ingreso-bajo gasto, bajo ingreso-bajo gasto y grupos centrales.

## 11. Conclusiones del análisis

El algoritmo con mejor resultado fue K-Means, con silhouette score de `0.416643`, frente a `0.390028` de Agglomerative Clustering.

La segmentación principal puede resumirse en cinco perfiles:

| Segmento | Perfil | Posible acción de negocio |
|---|---|---|
| Bajo ingreso, bajo gasto | Clientes con baja compra o bajo potencial inmediato. | Ofertas básicas, descuentos selectivos, campañas de bajo costo. |
| Jóvenes con gasto medio-alto | Clientes que gastan aunque no tengan ingresos altos. | Promociones, experiencias, fidelización, productos aspiracionales accesibles. |
| Alto ingreso, alto gasto | Clientes de mayor valor comercial. | Beneficios premium, trato personalizado, preventas, membresías. |
| Alto ingreso, bajo gasto | Clientes con potencial no capturado. | Campañas de reactivación, recomendaciones personalizadas, análisis de barreras de compra. |
| Ingreso y gasto medios, edad mayor | Clientes estables. | Comunicación de mantenimiento, beneficios prácticos, retención. |

### Qué significa el resultado para negocio

El análisis permite pasar de una base de clientes general a grupos con comportamientos distintos. Esto puede ayudar a diseñar campañas más precisas. No todos los clientes deben recibir la misma promoción: un cliente de alto ingreso y bajo gasto necesita una estrategia distinta a un cliente joven que ya gasta con frecuencia.

### Limitaciones

El dataset es pequeño: solo 200 clientes. Esto sirve para practicar y obtener una segmentación inicial, pero no necesariamente representa todos los patrones reales de un negocio.

Solo se usaron tres variables para entrenar: edad, ingreso y puntuación de gasto. Variables como frecuencia de visita, categorías compradas, fecha de última compra, ticket promedio o canal de compra podrían mejorar mucho el análisis.

La variable `Genre` no se usó. Podría incluirse en una versión futura, pero habría que codificarla correctamente y revisar si aporta valor real o introduce sesgos.

El silhouette score no es muy alto. Esto indica que los clusters existen, pero no están perfectamente separados. En términos prácticos, algunos clientes están en zonas intermedias.

### Mejoras futuras

Una mejora directa sería probar `k=6`, porque obtuvo el mejor silhouette score en la búsqueda. Después habría que comparar si ese sexto grupo tiene sentido de negocio o si solo divide artificialmente un segmento existente.

También convendría probar DBSCAN, aunque este dataset parece tener grupos con densidades y formas que podrían requerir ajuste cuidadoso de parámetros como `eps` y `min_samples`.

Otra mejora sería generar perfiles más completos por cluster, incluyendo distribución de género, edades mínimas y máximas, medianas y proporciones. Los promedios ayudan, pero pueden ocultar variación interna.

Por último, si este análisis se usara en una empresa real, habría que validar los segmentos con resultados de campañas o métricas posteriores: conversión, retención, gasto real y respuesta a promociones.

## Glosario breve de conceptos

`DataFrame`: tabla de datos en pandas, parecida a una hoja de cálculo.

`Clustering`: técnica de aprendizaje no supervisado que agrupa observaciones parecidas.

`K-Means`: algoritmo que crea `k` grupos alrededor de centroides. Cada punto se asigna al centroide más cercano.

`Centroide`: punto central de un cluster. En K-Means representa el promedio de los puntos asignados al grupo.

`Agglomerative Clustering`: algoritmo jerárquico que empieza con muchos grupos pequeños y los va fusionando.

`StandardScaler`: técnica de estandarización que transforma variables para que tengan media 0 y desviación estándar 1.

`Inercia`: suma de distancias cuadradas entre los puntos y sus centroides. Menor inercia significa clusters más compactos, pero siempre baja al aumentar `k`.

`Silhouette score`: métrica que compara qué tan cerca está un punto de su propio cluster frente a otros clusters. Valores más altos indican mejor separación.

`Histograma`: gráfico que muestra la distribución de una variable.

`Boxplot`: gráfico que muestra mediana, cuartiles, rango y posibles valores atípicos.

`Scatterplot`: gráfico de dispersión donde cada punto representa una observación.

`Pairplot`: matriz de gráficos que compara varias variables entre sí.
