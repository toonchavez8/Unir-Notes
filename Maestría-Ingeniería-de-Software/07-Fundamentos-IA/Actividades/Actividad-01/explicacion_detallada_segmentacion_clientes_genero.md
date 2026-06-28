# Explicacion detallada del analisis de segmentacion de clientes con genero

Autor del notebook original: Miguel de Jesus Chavez Barragan  
Dataset usado: `Mall_Customers.csv`  
Archivo base analizado: `segmentacion_clientes_genero.ipynb`

Este documento explica la nueva version del notebook de segmentacion de clientes. La diferencia principal frente al analisis anterior es que ahora se procesa la columna de genero, se convierte a una variable booleana y se compara el comportamiento de los clusters con y sin esa variable.

La idea no es solo agregar una columna. La pregunta real es: si incluimos el genero en el modelo, cambia de forma util la segmentacion o solo hace que el modelo divida mas los datos sin mejorar la separacion?

## Contexto general del ejercicio

El dataset contiene 200 clientes de un centro comercial. Cada fila representa una persona y cada columna describe algun rasgo demografico o de consumo.

| Columna original | Significado |
|---|---|
| `CustomerID` | Identificador del cliente. No se usa como variable de clustering porque solo distingue registros. |
| `Genre` | Genero registrado: `Male` o `Female`. En esta version se limpia y se transforma. |
| `Age` | Edad del cliente. |
| `Annual Income (k$)` | Ingreso anual en miles de dolares. |
| `Spending Score (1-100)` | Puntuacion de gasto entre 1 y 100. |

En el notebook anterior se trabajaba principalmente con tres variables numericas:

```python
["Age", "Annual Income (k$)", "Spending Score (1-100)"]
```

En esta version se agrega una cuarta variable para ciertos modelos:

```python
"Genero_binario"
```

La conversion queda asi:

| Valor original en `Genre` | Valor en `Genero` | Valor en `Genero_binario` | Valor en `Genero_label` |
|---|---:|---:|---|
| `Female` | `True` | `1` | `Female` |
| `Male` | `False` | `0` | `Male` |

Esto permite analizar el genero de dos maneras:

- Como etiqueta legible para graficos y tablas.
- Como numero para que pueda entrar al modelo de clustering.

## Lectura corta del resultado

La comparacion final del notebook muestra estos valores:

| Metodo | Numero de clusters | Silhouette |
|---|---:|---:|
| K-Means sin genero | 6 | 0.428 |
| K-Means con genero | 10 | 0.421 |
| Agglomerative sin genero | 6 | 0.420 |
| Agglomerative con genero | 10 | 0.418 |

La lectura principal es clara: incluir genero no mejora la metrica de separacion. De hecho, el `silhouette` baja ligeramente.

El modelo con genero termina separando mucho por hombres y mujeres. Eso se ve en las tablas de mezcla: varios clusters con genero tienen proporcion `1.00` femenina o `0.00` femenina. En otras palabras, el genero si cambia la forma de agrupar, pero no necesariamente mejora la calidad del clustering.

Hay una advertencia importante: en el notebook, el mejor `k` se elige por separado para el escenario sin genero y para el escenario con genero. Por eso la comparacion no mide solo el efecto de agregar genero; tambien cambia el numero de clusters. Aun asi, sirve como evidencia practica para el reporte: al agregar genero, el modelo genera mas grupos, pero no mejora el `silhouette`.

## 1. Configuracion inicial

Codigo principal:

```python
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.display import display
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

BASE_DIR = Path.cwd()
DATASET_PATH = BASE_DIR / "Mall_Customers.csv"
FIGURES_DIR = BASE_DIR / "figuras_genero"
FIGURES_DIR.mkdir(exist_ok=True)
```

### Explicacion

```python
from pathlib import Path
```

Importa `Path`, que permite manejar rutas de archivos de forma mas limpia. En lugar de escribir rutas como texto, se construyen objetos de ruta compatibles con el sistema operativo.

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

Estas son las librerias principales del analisis:

- `pandas` lee y manipula el CSV.
- `matplotlib` crea y guarda figuras.
- `seaborn` genera graficos estadisticos mas directos.

```python
from IPython.display import display
```

Permite mostrar varias tablas dentro de una misma celda. Esto se usa despues para comparar resumentes de clusters sin tener que separar cada tabla en otra celda.

```python
from sklearn.cluster import AgglomerativeClustering, KMeans
```

Importa dos algoritmos de clustering:

- `KMeans`, que agrupa los puntos alrededor de centroides.
- `AgglomerativeClustering`, que agrupa de forma jerarquica.

```python
from sklearn.metrics import silhouette_score
```

Importa la metrica `silhouette_score`. Esta metrica evalua si los puntos de un cluster estan mas cerca de su propio grupo que de otros grupos.

```python
from sklearn.preprocessing import StandardScaler
```

Importa el estandarizador. Esto es necesario porque K-Means y Agglomerative usan distancias. Sin estandarizacion, una variable con escala mas grande puede dominar el calculo.

```python
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)
```

Define un estilo visual limpio y un tamano por defecto para las graficas.

```python
BASE_DIR = Path.cwd()
DATASET_PATH = BASE_DIR / "Mall_Customers.csv"
FIGURES_DIR = BASE_DIR / "figuras_genero"
FIGURES_DIR.mkdir(exist_ok=True)
```

Se define la carpeta de trabajo, la ruta del dataset y una carpeta nueva para las imagenes de esta version: `figuras_genero`.

Esto separa las imagenes del analisis con genero de las imagenes del notebook anterior.

## 2. Carga del dataset

Codigo:

```python
df_raw = pd.read_csv(DATASET_PATH)
df_raw.head()
```

### Explicacion

```python
df_raw = pd.read_csv(DATASET_PATH)
```

Lee el archivo `Mall_Customers.csv` y lo guarda en un DataFrame llamado `df_raw`.

El sufijo `raw` indica que esos datos son los datos originales, todavia sin limpieza ni transformaciones. Es una buena practica conservar esa version inicial, porque permite comparar despues si alguna transformacion cambio algo de forma inesperada.

```python
df_raw.head()
```

Muestra las primeras cinco filas del dataset.

### Interpretacion

En esta etapa solo se confirma que el CSV carga correctamente y que las columnas esperadas estan presentes:

- `CustomerID`
- `Genre`
- `Age`
- `Annual Income (k$)`
- `Spending Score (1-100)`

Tambien se confirma que `Genre` todavia viene como texto (`Male` o `Female`).

## 3. Exploracion inicial del conjunto de datos

Codigo:

```python
print("Shape:", df_raw.shape)
print("Columnas:", df_raw.columns.tolist())
df_raw.info()
df_raw.describe(include="all")
```

### Explicacion

```python
print("Shape:", df_raw.shape)
```

Muestra el tamano del dataset. En este caso son 200 filas y 5 columnas.

```python
print("Columnas:", df_raw.columns.tolist())
```

Lista los nombres de las columnas. Esto ayuda a verificar que no haya errores de escritura, espacios inesperados o columnas faltantes.

```python
df_raw.info()
```

Muestra el tipo de dato de cada columna y la cantidad de valores no nulos.

```python
df_raw.describe(include="all")
```

Calcula estadisticas descriptivas tanto para variables numericas como para variables categoricas.

### Interpretacion

El dataset no presenta valores nulos en las columnas principales. Esto simplifica el preprocesamiento, porque no hay que imputar edades, ingresos, puntuaciones de gasto ni generos faltantes.

La columna `Genre` tiene dos categorias. La categoria mas frecuente es `Female`, segun el resumen descriptivo. Esto tambien se refleja despues en las proporciones de algunos clusters.

## 4. Analisis exploratorio visual

Esta seccion cambia bastante respecto al notebook anterior. Ahora no solo se mira edad, ingreso y gasto; tambien se agregan graficos donde el genero aparece como variable de comparacion.

### 4.1 Distribuciones iniciales

Codigo:

```python
numeric_cols = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
for ax, col in zip(axes.flat[:3], numeric_cols):
    sns.histplot(df_raw[col], kde=True, ax=ax, color="#4C72B0")
    ax.set_title(f"Distribucion de {col}")

sns.countplot(data=df_raw, x="Genre", ax=axes.flat[3], palette="Set2")
axes.flat[3].set_title("Distribucion de genero")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "distribuciones_iniciales.png", dpi=300)
plt.show()
```

### Explicacion

```python
numeric_cols = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
```

Define las tres variables numericas centrales del analisis.

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
```

Crea una figura con cuatro espacios: dos filas por dos columnas.

```python
for ax, col in zip(axes.flat[:3], numeric_cols):
    sns.histplot(df_raw[col], kde=True, ax=ax, color="#4C72B0")
    ax.set_title(f"Distribucion de {col}")
```

Genera histogramas para edad, ingreso anual y puntuacion de gasto. La opcion `kde=True` agrega una curva suave para ver mejor la forma de la distribucion.

```python
sns.countplot(data=df_raw, x="Genre", ax=axes.flat[3], palette="Set2")
```

El cuarto grafico muestra cuantas observaciones hay para cada genero.

```python
plt.savefig(FIGURES_DIR / "distribuciones_iniciales.png", dpi=300)
```

Guarda la imagen en la carpeta `figuras_genero`.

### Interpretacion de la imagen

Esta grafica sirve como revision inicial:

- La edad muestra la variedad demografica de los clientes.
- El ingreso anual tiene una distribucion amplia, con clientes de ingresos bajos, medios y altos.
- La puntuacion de gasto permite detectar clientes con bajo, medio y alto comportamiento de compra.
- La distribucion de genero permite saber si el dataset esta balanceado o si hay una categoria mas frecuente.

Si el genero estuviera muy desbalanceado, habria que tener cuidado: el modelo podria aprender mas sobre la proporcion de la muestra que sobre patrones reales de negocio.

### 4.2 Edad por genero

Codigo:

```python
plt.figure(figsize=(8, 6))
sns.boxplot(data=df_raw, x="Genre", y="Age", palette="Set3")
plt.title("Edad por genero")
plt.savefig(FIGURES_DIR / "edad_por_genero.png", dpi=300)
plt.show()
```

### Explicacion

El `boxplot` compara la distribucion de edad entre hombres y mujeres.

El grafico permite revisar:

- Mediana de edad.
- Rango intercuartil.
- Valores extremos.
- Diferencias visuales entre grupos.

### Interpretacion de la imagen

Este grafico responde una pregunta concreta: la edad se comporta distinto segun genero?

Si las cajas son parecidas, significa que la distribucion de edad entre hombres y mujeres no cambia demasiado. Si una caja esta mucho mas arriba o es mucho mas dispersa, podria indicar que el genero esta asociado con edad en el dataset.

Esta comparacion es importante porque el usuario pidio no comparar solo edad, sino tambien revisar si el genero impacta el reporte.

### 4.3 Ingreso anual vs puntuacion de gasto por genero

Codigo:

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df_raw,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Genre",
    palette="Set2"
)
plt.title("Ingreso anual vs puntuacion de gasto por genero")
plt.savefig(FIGURES_DIR / "ingreso_gasto_genero.png", dpi=300)
plt.show()
```

### Explicacion

El grafico de dispersion coloca:

- Ingreso anual en el eje X.
- Puntuacion de gasto en el eje Y.
- Genero como color.

### Interpretacion de la imagen

Este grafico es muy util porque la segmentacion de clientes suele depender bastante de ingreso y gasto.

La lectura esperada es:

- Si hombres y mujeres aparecen mezclados dentro de las mismas zonas, el genero no separa demasiado los grupos.
- Si hay zonas claramente dominadas por un genero, entonces el genero podria tener senal para el modelo.

En este notebook, los resultados posteriores muestran que al agregar genero los clusters se dividen por sexo, pero la metrica `silhouette` no mejora. Eso sugiere que la separacion por genero existe, pero no necesariamente produce mejores segmentos de consumo.

### 4.4 Pairplot por genero

Codigo:

```python
pairplot = sns.pairplot(df_raw, vars=numeric_cols, hue="Genre", corner=True, palette="Set2")
pairplot.savefig(FIGURES_DIR / "pairplot_genero.png", dpi=300)
plt.show()
```

### Explicacion

El `pairplot` genera varias graficas de dispersion entre las variables numericas.

```python
vars=numeric_cols
```

Indica que solo se grafican edad, ingreso y gasto.

```python
hue="Genre"
```

Colorea los puntos por genero.

```python
corner=True
```

Evita repetir graficos simetricos y deja una matriz mas compacta.

### Interpretacion de la imagen

El pairplot ayuda a revisar relaciones entre pares de variables:

- Edad vs ingreso.
- Edad vs gasto.
- Ingreso vs gasto.

Al colorear por genero, se puede ver si la separacion entre hombres y mujeres aparece de forma consistente o si solo aparece en algunas zonas.

## 5. Preprocesamiento

Esta es la seccion clave de la nueva version.

Codigo:

```python
df = df_raw.copy()
df.columns = [col.strip() for col in df.columns]
df["Genero"] = df["Genre"].str.strip().str.lower().map({"female": True, "male": False})
df["Genero_binario"] = df["Genero"].astype(int)
df["Genero_label"] = df["Genero"].map({True: "Female", False: "Male"})
df = df.drop(columns=["Genre"])
df.isnull().sum()
```

### Explicacion linea por linea

```python
df = df_raw.copy()
```

Crea una copia del dataset original. Esto protege `df_raw`, que queda como version sin modificar.

```python
df.columns = [col.strip() for col in df.columns]
```

Elimina espacios al inicio o al final de los nombres de columnas. Aunque el CSV no parece tener ese problema, esta linea hace el codigo mas robusto.

```python
df["Genero"] = df["Genre"].str.strip().str.lower().map({"female": True, "male": False})
```

Esta linea transforma el texto de genero:

1. `str.strip()` quita espacios alrededor del texto.
2. `str.lower()` convierte el texto a minusculas.
3. `map(...)` convierte `female` en `True` y `male` en `False`.

El resultado es una columna booleana.

```python
df["Genero_binario"] = df["Genero"].astype(int)
```

Convierte el booleano en entero:

- `True` pasa a `1`.
- `False` pasa a `0`.

Esto se necesita porque los algoritmos de scikit-learn esperan variables numericas.

```python
df["Genero_label"] = df["Genero"].map({True: "Female", False: "Male"})
```

Crea una etiqueta legible para graficos y tablas. Es mejor mostrar `Female` y `Male` en reportes que mostrar `1` y `0`.

```python
df = df.drop(columns=["Genre"])
```

Elimina la columna original `Genre`, porque ya fue reemplazada por versiones mas utiles.

```python
df.isnull().sum()
```

Verifica si la transformacion genero algun valor nulo.

### Interpretacion

La salida muestra cero nulos en:

- `Genero`
- `Genero_binario`
- `Genero_label`

Eso confirma que todos los valores de `Genre` fueron reconocidos correctamente. Si hubiera aparecido algun nulo en `Genero`, significaria que habia algun valor distinto a `Female` o `Male`, por ejemplo `female `, `F`, `Mujer` o una celda vacia.

## 5.1 Correlacion con genero binario

Codigo:

```python
corr_df = df[["Age", "Annual Income (k$)", "Spending Score (1-100)", "Genero_binario"]].copy()
plt.figure(figsize=(7, 5))
sns.heatmap(corr_df.corr(), annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlacion entre variables y genero binario")
plt.savefig(FIGURES_DIR / "corr_variables_genero.png", dpi=300)
plt.show()
```

### Explicacion

Aqui se calcula la matriz de correlacion entre edad, ingreso, gasto y genero binario.

Como `Genero_binario` vale `1` para mujeres y `0` para hombres, una correlacion positiva con esa columna significa que el valor tiende a ser mayor en mujeres. Una correlacion negativa significa que tiende a ser mayor en hombres.

### Interpretacion de la imagen

Esta grafica no prueba causalidad. Solo mide asociacion lineal.

Si las correlaciones de `Genero_binario` con edad, ingreso o gasto son cercanas a cero, entonces el genero no tiene una relacion lineal fuerte con esas variables.

Esto ayuda a anticipar el resultado final: si genero no esta muy correlacionado con las variables de consumo, puede cambiar la forma de agrupar, pero no necesariamente mejorar la calidad del modelo.

## 6. Busqueda del numero optimo de clusters para K-Means

Codigo principal:

```python
features_base = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
features_gender = features_base + ["Genero_binario"]

X_base = df[features_base].copy()
X_gender = df[features_gender].copy()

scaler_base = StandardScaler()
X_base_scaled = scaler_base.fit_transform(X_base)

scaler_gender = StandardScaler()
X_gender_scaled = scaler_gender.fit_transform(X_gender)
```

### Explicacion

```python
features_base = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
```

Define las variables del modelo base, igual que en el analisis anterior.

```python
features_gender = features_base + ["Genero_binario"]
```

Define las variables del modelo extendido. Aqui se agrega genero como cuarta variable.

```python
X_base = df[features_base].copy()
X_gender = df[features_gender].copy()
```

Crea dos matrices de entrada:

- `X_base`: sin genero.
- `X_gender`: con genero.

```python
scaler_base = StandardScaler()
X_base_scaled = scaler_base.fit_transform(X_base)
```

Estandariza las variables del modelo base.

```python
scaler_gender = StandardScaler()
X_gender_scaled = scaler_gender.fit_transform(X_gender)
```

Estandariza las variables del modelo con genero.

### Por que se estandariza tambien `Genero_binario`

Esta parte es importante. `Genero_binario` solo puede valer 0 o 1, mientras edad, ingreso y gasto tienen escalas mas amplias. Al aplicar `StandardScaler`, todas las variables se ponen en una escala comparable.

Eso permite que genero tenga peso dentro del modelo. Pero tambien tiene un efecto: como genero es binario, puede empujar al algoritmo a separar hombres y mujeres con bastante fuerza.

## 6.1 Calculo de metricas sin genero

Codigo:

```python
k_values = range(2, 11)

metrics_base = []
for k in k_values:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_base_scaled)
    metrics_base.append({
        "k": k,
        "inertia": model.inertia_,
        "silhouette": silhouette_score(X_base_scaled, labels)
    })

metrics_base = pd.DataFrame(metrics_base)
metrics_base
```

### Explicacion

El codigo prueba valores de `k` desde 2 hasta 10.

Para cada valor:

- Entrena K-Means.
- Calcula las etiquetas de cluster.
- Guarda la inercia.
- Calcula el `silhouette`.

```python
random_state=42
```

Fija la semilla para que los resultados sean reproducibles.

```python
n_init=10
```

K-Means se inicializa varias veces y conserva la mejor solucion. Esto reduce el riesgo de quedarse con una mala inicializacion.

### Interpretacion

El modelo base selecciona despues `best_k_base` usando el mejor `silhouette`. En el resultado final, ese escenario queda con 6 clusters y un `silhouette` aproximado de `0.428`.

## 6.2 Metodo del codo sin genero

Codigo:

```python
plt.plot(metrics_base["k"], metrics_base["inertia"], marker="o")
plt.title("Elbow Method sin genero")
plt.xlabel("Numero de clusters (k)")
plt.ylabel("Inercia")
plt.savefig(FIGURES_DIR / "elbow_sin_genero.png", dpi=300)
plt.show()
```

### Explicacion

El metodo del codo grafica la inercia para distintos valores de `k`.

La inercia mide que tan cerca estan los puntos de sus centroides. Mientras mas clusters se agregan, la inercia baja. El problema es que siempre baja; por eso se busca el punto donde la mejora empieza a ser menor.

### Interpretacion de la imagen

El codo ayuda a justificar visualmente el numero de clusters. No siempre da una respuesta exacta, pero permite ver si hay un punto razonable donde agregar mas clusters ya no aporta tanto.

## 6.3 Silhouette sin genero

Codigo:

```python
plt.plot(metrics_base["k"], metrics_base["silhouette"], marker="o")
plt.title("Silhouette Score sin genero")
plt.xlabel("Numero de clusters (k)")
plt.ylabel("Silhouette Score")
plt.savefig(FIGURES_DIR / "silhouette_sin_genero.png", dpi=300)
plt.show()
```

### Explicacion

Este grafico muestra la calidad de separacion para cada valor de `k`.

Un `silhouette` mas alto significa que los clusters estan mejor separados y son mas compactos.

### Interpretacion

El notebook usa esta metrica para elegir automaticamente `best_k_base`.

En la comparacion final, el modelo base queda con 6 clusters. Esa seleccion es coherente con el objetivo de encontrar grupos de consumo sin forzar separacion por genero.

## 7. Entrenamiento del modelo K-Means final sin genero

Codigo:

```python
best_k_base = int(metrics_base.loc[metrics_base["silhouette"].idxmax(), "k"])
kmeans_base = KMeans(n_clusters=best_k_base, random_state=42, n_init=10)
df["cluster_kmeans_base"] = kmeans_base.fit_predict(X_base_scaled)
df[["cluster_kmeans_base"] + features_base + ["Genero_label"]].head()
```

### Explicacion

```python
best_k_base = int(metrics_base.loc[metrics_base["silhouette"].idxmax(), "k"])
```

Busca el valor de `k` con mayor `silhouette` en el escenario sin genero.

```python
kmeans_base = KMeans(n_clusters=best_k_base, random_state=42, n_init=10)
```

Crea el modelo final con ese numero de clusters.

```python
df["cluster_kmeans_base"] = kmeans_base.fit_predict(X_base_scaled)
```

Entrena el modelo y guarda la etiqueta de cluster de cada cliente.

```python
df[["cluster_kmeans_base"] + features_base + ["Genero_label"]].head()
```

Muestra las primeras filas con el cluster asignado, las variables base y el genero como referencia.

### Interpretacion

Aunque el genero no entra al modelo base, se conserva `Genero_label` para analizar despues si cada cluster tiene mas hombres o mas mujeres.

Esto es una buena separacion de responsabilidades:

- Primero se agrupa por comportamiento y demografia numerica.
- Luego se revisa si genero aparece como caracteristica del grupo.

## 7.1 Visualizacion de K-Means sin genero

Codigo:

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="cluster_kmeans_base",
    palette="tab10"
)
plt.title("Clusters K-Means sin genero")
plt.savefig(FIGURES_DIR / "kmeans_sin_genero.png", dpi=300)
plt.show()
```

### Interpretacion de la imagen

Esta grafica muestra los clusters en el plano ingreso-gasto.

La lectura de negocio suele hacerse asi:

- Ingreso bajo y gasto bajo: clientes de bajo valor comercial inmediato.
- Ingreso bajo y gasto alto: clientes con alta afinidad pese a menor ingreso.
- Ingreso alto y gasto bajo: clientes con potencial no capturado.
- Ingreso alto y gasto alto: clientes de alto valor.
- Zonas medias: clientes promedio o de comportamiento mixto.

Como el genero no participa en este modelo, los colores representan segmentos definidos por edad, ingreso y gasto.

## 8. K-Means con genero como variable adicional

Codigo:

```python
metrics_gender = []
for k in k_values:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_gender_scaled)
    metrics_gender.append({
        "k": k,
        "inertia": model.inertia_,
        "silhouette": silhouette_score(X_gender_scaled, labels)
    })

metrics_gender = pd.DataFrame(metrics_gender)
metrics_gender
```

### Explicacion

Este bloque repite la busqueda de `k`, pero usando:

```python
["Age", "Annual Income (k$)", "Spending Score (1-100)", "Genero_binario"]
```

La intencion es validar si el genero mejora la estructura de clusters.

### Interpretacion

El modelo con genero termina eligiendo 10 clusters. Esto ya da una senal: al agregar genero, el algoritmo encuentra mas divisiones.

Eso no es automaticamente bueno. Mas clusters pueden dar una segmentacion mas detallada, pero tambien pueden fragmentar demasiado el dataset.

## 8.1 Entrenamiento y comparacion de K-Means con genero

Codigo:

```python
best_k_gender = int(metrics_gender.loc[metrics_gender["silhouette"].idxmax(), "k"])
kmeans_gender = KMeans(n_clusters=best_k_gender, random_state=42, n_init=10)
df["cluster_kmeans_genero"] = kmeans_gender.fit_predict(X_gender_scaled)

silhouette_base = silhouette_score(X_base_scaled, df["cluster_kmeans_base"])
silhouette_gender = silhouette_score(X_gender_scaled, df["cluster_kmeans_genero"])

print("Silhouette sin genero:", silhouette_base)
print("Silhouette con genero:", silhouette_gender)
```

### Resultado

```text
Silhouette sin genero: 0.4284167762892593
Silhouette con genero: 0.42076374869477745
```

### Interpretacion

El modelo sin genero tiene mejor `silhouette` que el modelo con genero.

La diferencia no es enorme, pero si va en contra de la idea de que genero mejore la segmentacion. En esta corrida, agregar genero produce una separacion ligeramente peor.

Mi lectura es esta: genero ayuda a partir los grupos por hombres y mujeres, pero no aporta suficiente informacion adicional para mejorar la estructura general de clusters.

## 8.2 Visualizacion de K-Means con genero

Codigo:

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="cluster_kmeans_genero",
    palette="Set2"
)
plt.title("Clusters K-Means con genero")
plt.savefig(FIGURES_DIR / "kmeans_con_genero.png", dpi=300)
plt.show()
```

### Interpretacion de la imagen

La grafica vuelve a usar ingreso y gasto como ejes, pero ahora los clusters fueron calculados incluyendo genero.

Hay que leerla con cuidado: como el genero no aparece como eje, puede parecer que algunos puntos cercanos pertenecen a clusters distintos. Eso pasa porque la separacion tambien ocurre en la dimension de genero.

Es decir, dos clientes con ingreso y gasto parecidos pueden quedar separados si uno es hombre y la otra es mujer.

## 8.3 Mezcla de genero por cluster

Codigo:

```python
gender_mix_base = pd.crosstab(df["cluster_kmeans_base"], df["Genero_label"], normalize="index").round(2)
gender_mix_gender = pd.crosstab(df["cluster_kmeans_genero"], df["Genero_label"], normalize="index").round(2)

display(gender_mix_base)
display(gender_mix_gender)
```

### Resultado del modelo sin genero

| Cluster base | Female | Male |
|---:|---:|---:|
| 0 | 0.58 | 0.42 |
| 1 | 0.64 | 0.36 |
| 2 | 0.42 | 0.58 |
| 3 | 0.54 | 0.46 |
| 4 | 0.57 | 0.43 |
| 5 | 0.62 | 0.38 |

### Resultado del modelo con genero

| Cluster con genero | Female | Male |
|---:|---:|---:|
| 0 | 0.00 | 1.00 |
| 1 | 0.00 | 1.00 |
| 2 | 0.93 | 0.07 |
| 3 | 1.00 | 0.00 |
| 4 | 1.00 | 0.00 |
| 5 | 0.00 | 1.00 |
| 6 | 1.00 | 0.00 |
| 7 | 0.00 | 1.00 |
| 8 | 1.00 | 0.00 |
| 9 | 1.00 | 0.00 |

### Interpretacion

Esta es una de las tablas mas importantes del notebook.

En el modelo sin genero, los clusters tienen mezcla de hombres y mujeres. Ningun cluster queda totalmente separado por genero.

En el modelo con genero, casi todos los clusters quedan dominados por un solo genero. Eso significa que el algoritmo esta usando la variable de genero como una frontera fuerte.

Esto confirma que genero impacta el resultado, pero de una forma que puede ser discutible para negocio. Si el objetivo es entender patrones de gasto, separar por genero puede generar segmentos mas pequenos sin mejorar la separacion real de consumo.

## 9. Segundo algoritmo de clustering

Codigo:

```python
agg_base = AgglomerativeClustering(n_clusters=best_k_base)
agg_gender = AgglomerativeClustering(n_clusters=best_k_gender)

df["cluster_agg_base"] = agg_base.fit_predict(X_base_scaled)
df["cluster_agg_genero"] = agg_gender.fit_predict(X_gender_scaled)

silhouette_agg_base = silhouette_score(X_base_scaled, df["cluster_agg_base"])
silhouette_agg_gender = silhouette_score(X_gender_scaled, df["cluster_agg_genero"])

print("Silhouette Agglomerative sin genero:", silhouette_agg_base)
print("Silhouette Agglomerative con genero:", silhouette_agg_gender)
```

### Resultado

```text
Silhouette Agglomerative sin genero: 0.4201169558789579
Silhouette Agglomerative con genero: 0.4176254448686808
```

### Explicacion

El notebook aplica `AgglomerativeClustering` en dos escenarios:

- Sin genero, usando `best_k_base`.
- Con genero, usando `best_k_gender`.

Esto permite comparar si el patron observado en K-Means tambien aparece con otro algoritmo.

### Interpretacion

El resultado se repite: el escenario sin genero tiene mejor `silhouette` que el escenario con genero.

Esto refuerza la conclusion. No es solo una particularidad de K-Means; tambien en clustering jerarquico, agregar genero no mejora la separacion medida por `silhouette`.

## 9.1 Visualizacion de Agglomerative Clustering con genero

Codigo:

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="cluster_agg_genero",
    palette="Set1"
)
plt.title("Agglomerative Clustering con genero")
plt.savefig(FIGURES_DIR / "agg_con_genero.png", dpi=300)
plt.show()
```

### Interpretacion de la imagen

La imagen muestra los clusters jerarquicos calculados con genero.

Igual que en K-Means con genero, algunos puntos pueden verse cercanos en ingreso y gasto, pero quedar en grupos diferentes por la dimension adicional de genero.

## 10. Resumen e interpretacion de clusters

Esta seccion resume los clusters con promedios y tamanos. Aqui se vuelve mas facil convertir el analisis tecnico en lectura de negocio.

## 10.1 Resumen K-Means sin genero

Resultado:

| Cluster | Age | Annual Income (k$) | Spending Score (1-100) | Size | Female share |
|---:|---:|---:|---:|---:|---:|
| 0 | 56.33 | 54.27 | 49.07 | 45 | 0.58 |
| 1 | 26.79 | 57.10 | 48.13 | 39 | 0.64 |
| 2 | 41.94 | 88.94 | 16.97 | 33 | 0.42 |
| 3 | 32.69 | 86.54 | 82.13 | 39 | 0.54 |
| 4 | 25.00 | 25.26 | 77.61 | 23 | 0.57 |
| 5 | 45.52 | 26.29 | 19.38 | 21 | 0.62 |

### Interpretacion

Los clusters base conservan una lectura de negocio bastante limpia:

| Cluster | Perfil probable |
|---:|---|
| 0 | Clientes mayores, ingreso medio y gasto medio. |
| 1 | Clientes jovenes, ingreso medio y gasto medio. |
| 2 | Clientes de ingreso alto y bajo gasto. Segmento con potencial de activacion. |
| 3 | Clientes de ingreso alto y alto gasto. Segmento de alto valor. |
| 4 | Clientes jovenes, ingreso bajo y alto gasto. Segmento sensible a promociones o experiencias. |
| 5 | Clientes de ingreso bajo y bajo gasto. Segmento de bajo valor inmediato. |

La columna `female_share` permite ver la presencia femenina en cada cluster. Los valores estan entre 0.42 y 0.64, asi que los grupos no estan completamente dominados por un genero.

Esto sugiere que, cuando no se fuerza genero en el modelo, los segmentos se forman principalmente por ingreso, gasto y edad.

## 10.2 Resumen K-Means con genero

Resultado:

| Cluster | Age | Annual Income (k$) | Spending Score (1-100) | Genero_binario | Size |
|---:|---:|---:|---:|---:|---:|
| 0 | 58.85 | 48.69 | 39.85 | 0.00 | 26 |
| 1 | 25.25 | 41.25 | 60.92 | 0.00 | 24 |
| 2 | 41.21 | 26.07 | 20.14 | 0.93 | 14 |
| 3 | 32.19 | 86.05 | 81.67 | 1.00 | 21 |
| 4 | 54.15 | 54.23 | 48.96 | 1.00 | 26 |
| 5 | 38.47 | 85.89 | 14.21 | 0.00 | 19 |
| 6 | 27.96 | 57.36 | 47.12 | 1.00 | 25 |
| 7 | 33.28 | 87.11 | 82.67 | 0.00 | 18 |
| 8 | 25.46 | 25.69 | 80.54 | 1.00 | 13 |
| 9 | 43.79 | 93.29 | 20.64 | 1.00 | 14 |

### Interpretacion

Aqui se ve el efecto directo de incluir genero.

Clusters con `Genero_binario = 0.00` son masculinos. Clusters con `Genero_binario = 1.00` son femeninos. El cluster 2 queda casi femenino (`0.93`).

El modelo ya no solo separa por comportamiento de consumo; tambien separa por genero.

Ejemplos claros:

- Cluster 3: mujeres, ingreso alto y gasto alto.
- Cluster 7: hombres, ingreso alto y gasto alto.
- Cluster 5: hombres, ingreso alto y gasto bajo.
- Cluster 9: mujeres, ingreso alto y gasto bajo.
- Cluster 8: mujeres jovenes, ingreso bajo y gasto alto.
- Cluster 1: hombres jovenes, ingreso medio-bajo y gasto medio-alto.

Esta segmentacion puede ser util si el reporte quiere hablar de genero como criterio de perfilamiento. Pero si el objetivo principal es segmentar comportamiento de gasto, hay que justificar por que se acepta una segmentacion mas fragmentada y con menor `silhouette`.

## 10.3 Resumen Agglomerative sin genero

Resultado:

| Cluster | Age | Annual Income (k$) | Spending Score (1-100) | Size | Female share |
|---:|---:|---:|---:|---:|---:|
| 0 | 27.38 | 57.51 | 45.84 | 45 | 0.60 |
| 1 | 56.40 | 55.29 | 48.36 | 45 | 0.53 |
| 2 | 32.69 | 86.54 | 82.13 | 39 | 0.54 |
| 3 | 43.89 | 91.29 | 16.68 | 28 | 0.50 |
| 4 | 44.32 | 25.77 | 20.27 | 22 | 0.59 |
| 5 | 24.81 | 25.62 | 80.24 | 21 | 0.62 |

### Interpretacion

El clustering jerarquico sin genero produce perfiles parecidos al K-Means base:

- Jovenes de ingreso medio y gasto medio.
- Mayores de ingreso medio y gasto medio.
- Ingreso alto y gasto alto.
- Ingreso alto y gasto bajo.
- Ingreso bajo y gasto bajo.
- Jovenes de ingreso bajo y gasto alto.

Las proporciones de genero vuelven a estar mezcladas. Eso confirma que los patrones principales salen de ingreso, gasto y edad, no de genero.

## 10.4 Resumen Agglomerative con genero

Resultado:

| Cluster | Age | Annual Income (k$) | Spending Score (1-100) | Genero_binario | Size |
|---:|---:|---:|---:|---:|---:|
| 0 | 56.55 | 50.03 | 41.34 | 0.0 | 29 |
| 1 | 38.83 | 86.39 | 11.67 | 0.0 | 18 |
| 2 | 24.57 | 39.22 | 59.65 | 0.0 | 23 |
| 3 | 54.08 | 53.24 | 49.52 | 1.0 | 25 |
| 4 | 27.96 | 57.36 | 47.12 | 1.0 | 25 |
| 5 | 33.28 | 87.11 | 82.67 | 0.0 | 18 |
| 6 | 32.19 | 86.05 | 81.67 | 1.0 | 21 |
| 7 | 44.60 | 92.33 | 21.60 | 1.0 | 15 |
| 8 | 25.46 | 25.69 | 80.54 | 1.0 | 13 |
| 9 | 41.54 | 26.54 | 20.69 | 1.0 | 13 |

### Interpretacion

El patron se repite: el algoritmo separa clusters por genero.

La segmentacion jerarquica con genero parece crear pares de grupos equivalentes, por ejemplo:

- Hombres con ingreso alto y gasto alto.
- Mujeres con ingreso alto y gasto alto.
- Hombres con ingreso alto y gasto bajo.
- Mujeres con ingreso alto y gasto bajo.

Esto puede ser interesante para marketing si se quieren comparar estrategias por genero, pero no demuestra que genero mejore la agrupacion global.

## 11. Comparacion de algoritmos

Codigo:

```python
comparison = pd.DataFrame([
    {
        "Metodo": "K-Means sin genero",
        "Numero_clusters": df["cluster_kmeans_base"].nunique(),
        "Silhouette": silhouette_base,
        "Observacion": "Referencia base"
    },
    {
        "Metodo": "K-Means con genero",
        "Numero_clusters": df["cluster_kmeans_genero"].nunique(),
        "Silhouette": silhouette_gender,
        "Observacion": "Valida el impacto del genero"
    },
    {
        "Metodo": "Agglomerative sin genero",
        "Numero_clusters": df["cluster_agg_base"].nunique(),
        "Silhouette": silhouette_agg_base,
        "Observacion": "Referencia jerarquica base"
    },
    {
        "Metodo": "Agglomerative con genero",
        "Numero_clusters": df["cluster_agg_genero"].nunique(),
        "Silhouette": silhouette_agg_gender,
        "Observacion": "Jerarquico con variable de genero"
    }
]).round(3)

display(comparison)
comparison.to_csv(FIGURES_DIR / "comparacion_algoritmos_genero.csv", index=False)
```

### Resultado

| Metodo | Numero_clusters | Silhouette | Observacion |
|---|---:|---:|---|
| K-Means sin genero | 6 | 0.428 | Referencia base |
| K-Means con genero | 10 | 0.421 | Valida el impacto del genero |
| Agglomerative sin genero | 6 | 0.420 | Referencia jerarquica base |
| Agglomerative con genero | 10 | 0.418 | Jerarquico con variable de genero |

### Interpretacion

El mejor resultado del notebook es K-Means sin genero.

La incorporacion de genero no mejora el `silhouette`. En ambos algoritmos, el resultado con genero queda ligeramente por debajo.

La diferencia principal es que los modelos con genero usan 10 clusters, mientras que los modelos sin genero usan 6. Esto produce una segmentacion mas granular, pero no necesariamente mejor.

## 12. Conclusiones del analisis

### Conclusion tecnica

El genero fue procesado correctamente:

- `Female` se convirtio en `True`.
- `Male` se convirtio en `False`.
- Se creo `Genero_binario` para modelado.
- Se creo `Genero_label` para visualizaciones y reportes.

Al incluir genero en el clustering, los modelos tienden a separar los grupos por sexo. Esto se ve de forma muy clara en las tablas de mezcla de genero por cluster.

Sin embargo, la metrica `silhouette` baja ligeramente:

- K-Means: de `0.428` a `0.421`.
- Agglomerative: de `0.420` a `0.418`.

Por lo tanto, con estos datos, genero impacta la composicion de los clusters, pero no mejora la calidad global de la segmentacion.

### Conclusion de negocio

La segmentacion sin genero es mas limpia si el objetivo es entender patrones generales de consumo.

La segmentacion con genero es util si el reporte quiere comparar perfiles masculinos y femeninos dentro de segmentos parecidos. Por ejemplo:

- Mujeres de ingreso alto y gasto alto.
- Hombres de ingreso alto y gasto alto.
- Mujeres de ingreso alto y gasto bajo.
- Hombres de ingreso alto y gasto bajo.

Pero esa lectura debe presentarse como una seccion complementaria, no como reemplazo automatico del modelo base.

### Recomendacion

Para el informe final, conviene presentar dos niveles:

1. Modelo principal: K-Means sin genero, porque tiene mejor `silhouette` y segmentos mas faciles de explicar.
2. Analisis complementario: comparacion por genero dentro de cada cluster y modelo con genero como prueba de sensibilidad.

Asi se cumple el objetivo de validar si genero impacta el reporte, sin forzar la conclusion de que genero mejora el clustering.

## Limitaciones

El dataset es pequeno: solo 200 clientes. Eso limita la estabilidad de cualquier conclusion por genero.

Tambien hay una limitacion metodologica: el modelo con genero usa 10 clusters porque el mejor `silhouette` se eligio de forma independiente. Para medir de forma mas estricta el impacto de genero, tambien convendria comparar ambos escenarios con el mismo numero de clusters, por ejemplo `k = 6`.

Otra limitacion es que `Genero_binario` representa una variable categorica como si fuera numerica. Para K-Means esto puede funcionar como aproximacion, pero no es ideal en todos los casos. En datasets mas grandes se podria probar clustering con distancias mixtas o metodos pensados para variables categoricas.

## Mejoras futuras

Se podrian agregar estas mejoras:

- Comparar sin genero y con genero usando el mismo `k`.
- Probar una codificacion one-hot de genero en lugar de booleano convertido a entero.
- Revisar estabilidad de clusters con distintas semillas.
- Agregar visualizaciones por cluster y genero usando barras apiladas.
- Crear una tabla final de recomendaciones comerciales por segmento.
- Evaluar si genero tiene relacion estadistica con gasto usando pruebas adicionales, no solo clustering.

## Glosario breve

| Concepto | Explicacion |
|---|---|
| Clustering | Tecnica de aprendizaje no supervisado que agrupa observaciones parecidas. |
| K-Means | Algoritmo que separa datos en `k` grupos usando centroides. |
| Agglomerative Clustering | Algoritmo jerarquico que va fusionando observaciones o grupos similares. |
| Silhouette | Metrica que evalua separacion y cohesion de clusters. Mas alto suele ser mejor. |
| Inercia | Suma de distancias internas respecto a los centroides en K-Means. |
| Estandarizacion | Transformacion para poner variables en escala comparable. |
| Variable booleana | Variable con dos valores: `True` o `False`. |
| `Genero_binario` | Version numerica del genero: `1` para `Female`, `0` para `Male`. |
| `female_share` | Proporcion de mujeres dentro de un cluster. |

