# Guía paso a paso para la Actividad 1

## Tema de la actividad
**Segmentación de clientes mediante Aprendizaje No Supervisado**

Esta guía está pensada para que puedas realizar la actividad aunque seas **junior developer** y además te ayude a **maximizar el puntaje** según la rúbrica.

---

## 1. Qué te están pidiendo realmente

La actividad no solo te pide "correr un algoritmo". Te pide demostrar que sabes:

1. **Entender el dataset**.
2. **Preparar los datos correctamente**.
3. **Aplicar al menos dos algoritmos de clustering**.
4. **Comparar resultados con criterio**.
5. **Explicar qué significan los grupos encontrados**.
6. **Entregar un trabajo reproducible y bien documentado**.

Si haces solo código y gráficas, tu trabajo quedará incompleto. Para sacar el mayor puntaje, debes cubrir también:

- justificación de decisiones,
- interpretación de resultados,
- orden del notebook,
- claridad del informe,
- evidencias y notas de respaldo.

---

## 2. Entregables obligatorios

Debes entregar un `.zip` con:

- `informe.pdf`
- `segmentacion_clientes.ipynb`
- carpeta `figuras/`
- `requirements.txt`

### Recomendación extra para mejor control
Aunque no siempre lo pidan explícitamente, te conviene además guardar localmente:

- `notas_analisis.md`
- `resultados_metricas.csv`
- `resumen_clusters.csv`

Estos archivos te ayudan a justificar decisiones y a reconstruir tu trabajo si algo falla.

---

## 3. Rúbrica traducida a acciones concretas

### Criterio 1. Preprocesamiento y preparación de datos (20%)
Para sacar el máximo:

- carga correctamente el dataset,
- revisa tipos de datos,
- verifica valores nulos,
- detecta valores atípicos,
- escala variables numéricas,
- explica por qué elegiste ciertas variables para clustering.

### Criterio 2. Implementación y comparación de algoritmos (25%)
Para sacar el máximo:

- usa al menos dos métodos distintos,
- explica cómo funciona cada uno a nivel básico,
- justifica parámetros,
- usa una métrica objetiva para comparar resultados.

### Criterio 3. Análisis crítico y conclusiones (25%)
Para sacar el máximo:

- describe qué representa cada cluster,
- explica si los grupos tienen sentido de negocio,
- compara ventajas y limitaciones entre métodos,
- propone mejoras reales.

### Criterio 4. Claridad, redacción y calidad visual del informe (20%)
Para sacar el máximo:

- usa estructura limpia,
- gráficos con título, ejes y leyenda,
- redacción formal,
- tablas claras,
- conclusiones concretas.

### Criterio 5. Código reproducible, organizado y comentado (10%)
Para sacar el máximo:

- notebook en orden lógico,
- celdas separadas por etapa,
- comentarios breves pero útiles,
- mismo resultado al volver a ejecutarlo,
- `requirements.txt` correcto.

---

## 4. Términos importantes que debes entender

### Aprendizaje no supervisado
Es un tipo de aprendizaje automático donde **no existen etiquetas de salida**. El modelo busca patrones o agrupaciones por sí mismo.

### Clustering
Es la técnica que agrupa observaciones similares. En esta actividad, cada cliente debe quedar dentro de un grupo con características parecidas.

### Dataset
Conjunto de datos que vas a analizar. Aquí contiene clientes con variables como:

- edad,
- ingresos anuales,
- puntuación de gasto.

### Variable relevante
Es una columna que realmente aporta valor para formar grupos. No todas las columnas ayudan igual.

### Preprocesamiento
Conjunto de pasos para dejar los datos listos antes de entrenar modelos. Incluye limpieza, selección de variables y escalado.

### Escalado
Proceso para llevar variables numéricas a una escala comparable. Es importante porque algoritmos como **K-Means** dependen de distancias.

### Valor atípico
Dato extremadamente alejado del resto. Puede distorsionar agrupamientos.

### K-Means
Algoritmo que separa los datos en `k` grupos. Cada grupo tiene un centro llamado **centroide**. Es simple y muy común.

### DBSCAN
Algoritmo basado en densidad. Agrupa puntos que están cerca entre sí y puede detectar ruido o puntos aislados.

### Agglomerative Clustering
Método jerárquico. Empieza tratando cada punto como un cluster y luego los va uniendo.

### Elbow Method
Método para estimar cuántos clusters conviene usar en K-Means. Busca el punto donde mejorar deja de aportar tanto.

### Silhouette Score
Métrica que indica qué tan bien separado está cada cluster. En general, **más alto es mejor**.

### Interpretación de clusters
No basta con obtener grupos. Debes explicar qué significa cada uno, por ejemplo:

- clientes jóvenes con alto gasto,
- clientes de ingreso alto pero bajo consumo,
- clientes conservadores con gasto medio.

---

## 5. Herramientas que necesitas

## Software

- Python 3.10+ o similar
- Jupyter Notebook o VS Code con notebooks

## Librerías recomendadas

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `scipy` (opcional, útil para análisis jerárquico)

### Ejemplo de `requirements.txt`

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
jupyter
```

---

## 6. Estructura recomendada del notebook

Nombra tu archivo como:

`segmentacion_clientes.ipynb`

Orden sugerido:

1. Portada o título
2. Objetivo
3. Carga de librerías
4. Carga del dataset
5. Exploración inicial
6. Limpieza y preprocesamiento
7. Selección de variables
8. Escalado
9. Entrenamiento con método 1
10. Elección de número de clusters
11. Visualización de resultados
12. Entrenamiento con método 2
13. Comparación de métodos
14. Interpretación de clusters
15. Conclusiones

---

## 7. Paso a paso para resolver la actividad

Esta sección está escrita asumiendo que empiezas prácticamente desde cero. La idea es que sigas los pasos en orden y entiendas **qué hacer**, **dónde hacerlo** y **por qué hacerlo**.

## Paso 0. Preparar tu carpeta de trabajo

### Qué debes hacer

Trabaja dentro de la carpeta:

`Actividad-01`

### Dónde hacerlo

En una terminal de PowerShell, ubicada en la raíz del proyecto o directamente en `Actividad-01`.

### Comandos

Si estás en la raíz del repositorio:

```powershell
cd "C:\Users\Dev\repos\toonchavez8\Unir-Notes\Maestría-Ingeniería-de-Software\07-Fundamentos-IA\Actividades\Actividad-01"
Get-ChildItem
```

### Por qué

- `cd` te mueve a la carpeta correcta.
- `Get-ChildItem` te deja confirmar qué archivos ya existen.

### Qué deberías tener o crear

Al final, esta carpeta debería contener algo parecido a:

- `psuiadesoft01_act1.md`
- `segmentacion_clientes.ipynb`
- `requirements.txt`
- `notas_analisis.md`
- carpeta `figuras/`
- el archivo del dataset, por ejemplo `Mall_Customers.csv`

---

## Paso 1. Descargar el dataset y colocarlo en la carpeta correcta

### Qué debes hacer

Descarga el dataset desde Kaggle y colócalo dentro de `Actividad-01`.

### Dónde hacerlo

- La descarga la haces en el navegador.
- El archivo lo copias o mueves a la carpeta `Actividad-01`.

### Qué buscar

Normalmente el archivo viene con nombre similar a:

- `Mall_Customers.csv`

### Por qué

Si el dataset queda en la misma carpeta del notebook, luego será mucho más fácil cargarlo con una ruta simple y evitar errores de archivos no encontrados.

### Qué debes registrar en tus notas

- URL del dataset
- fecha de descarga
- nombre exacto del archivo
- número de registros esperado

### Ejemplo de nota

> Dataset descargado desde Kaggle el 18 de junio de 2026. Archivo utilizado: `Mall_Customers.csv`.

---

## Paso 2. Crear la estructura mínima de archivos

### Qué debes hacer

Crear los archivos y carpetas base de la actividad.

### Dónde hacerlo

En PowerShell, dentro de `Actividad-01`.

### Comandos

```powershell
New-Item -ItemType Directory -Path ".\figuras" -Force
New-Item -ItemType File -Path ".\notas_analisis.md" -Force
New-Item -ItemType File -Path ".\requirements.txt" -Force
```

### Por qué

- `figuras/` almacenará todos los gráficos exportados.
- `notas_analisis.md` te servirá para registrar decisiones y observaciones.
- `requirements.txt` permite reproducir tu entorno y suma puntos en organización.

---

## Paso 3. Crear y activar un entorno virtual de Python

### Qué debes hacer

Crear un entorno virtual para instalar librerías sin afectar otras instalaciones de Python.

### Dónde hacerlo

En PowerShell, dentro de `Actividad-01`.

### Comandos

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

### Por qué

- `python -m venv .venv` crea un entorno aislado.
- `Activate.ps1` activa ese entorno.
- `python --version` confirma que Python responde correctamente.

### Qué significa "entorno virtual"

Es un espacio aislado donde instalas librerías específicas para este proyecto. Así evitas conflictos con otros proyectos o versiones globales.

### Qué debes comprobar

Cuando se active, normalmente verás algo como `(.venv)` al inicio de la línea de la terminal.

---

## Paso 4. Instalar las librerías necesarias

### Qué debes hacer

Instalar todas las dependencias que vas a usar en la actividad.

### Dónde hacerlo

En PowerShell, con el entorno virtual activado.

### Comando

```powershell
pip install pandas numpy matplotlib seaborn scikit-learn scipy jupyter
```

### Por qué

Cada librería cubre una parte distinta:

- `pandas`: lectura y manipulación de datos.
- `numpy`: operaciones numéricas.
- `matplotlib`: gráficos base.
- `seaborn`: gráficos más claros y bonitos.
- `scikit-learn`: algoritmos de clustering y escalado.
- `scipy`: útil para métodos jerárquicos.
- `jupyter`: para trabajar con notebooks.

### Qué hacer después

Guardar las dependencias instaladas:

```powershell
pip freeze > requirements.txt
```

### Por qué

Esto genera la lista exacta de paquetes instalados. Le demuestra al profesor que tu trabajo es reproducible.

---

## Paso 5. Abrir Jupyter Notebook

### Qué debes hacer

Iniciar Jupyter para crear tu notebook.

### Dónde hacerlo

En PowerShell, dentro de `Actividad-01`, con el entorno activado.

### Comando

```powershell
jupyter notebook
```

### Por qué

Esto abrirá una interfaz en el navegador donde podrás crear y ejecutar `segmentacion_clientes.ipynb`.

### Qué archivo debes crear

Crea un notebook llamado:

`segmentacion_clientes.ipynb`

### Por qué ese nombre

Es el nombre solicitado por la actividad y evita confusiones al entregar.

---

## Paso 6. Crear la primera sección del notebook

### Qué debes hacer

En el notebook, crea una celda Markdown con:

- título,
- nombre de la actividad,
- objetivo,
- nombre del alumno si lo necesitas.

### Qué escribir

Ejemplo:

```md
# Segmentación de clientes mediante aprendizaje no supervisado

## Objetivo
Aplicar técnicas de clustering para identificar grupos homogéneos de clientes a partir de variables demográficas y de consumo.
```

### Por qué

Esto da orden académico al notebook y mejora la presentación.

---

## Paso 7. Importar librerías

### Qué debes hacer

Crear una celda de código al inicio del notebook para importar las librerías.

### Código sugerido

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score
```

### Por qué

Necesitas cargar desde el inicio todas las herramientas que usarás. Además, esto hace que el notebook sea más limpio y fácil de revisar.

---

## Paso 8. Cargar el dataset

### Qué debes hacer

Leer el archivo CSV en una variable, por ejemplo `df`.

### Código sugerido

```python
df = pd.read_csv("Mall_Customers.csv")
df.head()
```

### Por qué

- `pd.read_csv(...)` carga el dataset.
- `df.head()` muestra las primeras filas y te permite comprobar que la lectura fue correcta.

### Si falla

Si aparece un error de archivo no encontrado, revisa:

- si el CSV está en la misma carpeta que el notebook,
- si el nombre del archivo está bien escrito,
- si incluye mayúsculas, espacios o guiones distintos.

---

## Paso 9. Explorar la estructura básica de los datos

### Qué debes hacer

Crear varias celdas para revisar dimensiones, columnas, tipos de datos y valores faltantes.

### Código sugerido

```python
df.shape
```

```python
df.columns
```

```python
df.info()
```

```python
df.isnull().sum()
```

```python
df.describe()
```

### Por qué

Cada instrucción responde algo distinto:

- `df.shape`: cuántas filas y columnas hay.
- `df.columns`: nombres exactos de las columnas.
- `df.info()`: tipos de datos y valores no nulos.
- `df.isnull().sum()`: cuántos faltantes tiene cada columna.
- `df.describe()`: resumen estadístico.

### Qué debes anotar en `notas_analisis.md`

- número de filas,
- número de columnas,
- columnas del dataset,
- si hay nulos o no,
- primeras observaciones.

---

## Paso 10. Hacer análisis exploratorio visual

### Qué debes hacer

Generar gráficos para entender el comportamiento de las variables.

### Código sugerido para histogramas

```python
df.hist(figsize=(10, 6))
plt.tight_layout()
plt.savefig("figuras/histogramas.png", dpi=300)
plt.show()
```

### Código sugerido para boxplots

```python
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]])
plt.title("Boxplots de variables numéricas")
plt.savefig("figuras/boxplots_variables.png", dpi=300)
plt.show()
```

### Código sugerido para dispersión

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Annual Income (k$)", y="Spending Score (1-100)")
plt.title("Ingreso anual vs puntuación de gasto")
plt.savefig("figuras/scatter_ingreso_gasto.png", dpi=300)
plt.show()
```

### Por qué

- Los histogramas te muestran distribución.
- Los boxplots te ayudan a detectar outliers.
- El scatter plot te deja ver si ya hay grupos visuales.

### Qué debes escribir en el informe

No pongas solo la imagen. Debes acompañarla con interpretación, por ejemplo:

> Se observa una dispersión considerable entre ingreso anual y puntuación de gasto, lo que sugiere la posible existencia de segmentos diferenciados de clientes.

---

## Paso 11. Decidir qué columnas usarás para clustering

### Qué debes hacer

Elegir las variables con las que vas a formar los grupos.

### Recomendación segura

Usa:

- `Age`
- `Annual Income (k$)`
- `Spending Score (1-100)`

### Qué hacer con `CustomerID`

No lo uses para clustering.

### Por qué

`CustomerID` es un identificador, no una característica del cliente. Si lo usas, podrías dañar la calidad del agrupamiento.

### Qué hacer con `Gender`

Puedes:

- excluirla para simplificar,
- o codificarla si quieres enriquecer el análisis.

### Recomendación como junior

Primero exclúyela y trabaja con las tres variables numéricas principales. Es más fácil de justificar y explicar.

### Código sugerido

```python
features = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
X = df[features].copy()
X.head()
```

---

## Paso 12. Escalar los datos

### Qué debes hacer

Aplicar escalado a las variables numéricas.

### Código sugerido

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Por qué

K-Means y otros algoritmos basados en distancia comparan cercanía numérica entre puntos. Si una variable tiene valores mucho más grandes que otra, dominará el resultado.

### Qué significa `StandardScaler`

Transforma los datos para que queden aproximadamente centrados en 0 y con desviación estándar cercana a 1.

### Qué debes registrar

- variables escaladas,
- método de escalado,
- justificación.

---

## Paso 13. Buscar el mejor número de clusters para K-Means

### Qué debes hacer

Probar varios valores de `k` y medir resultados.

### Código sugerido

```python
inertia = []
silhouette_scores = []
k_values = range(2, 11)

for k in k_values:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    inertia.append(model.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, labels))
```

### Por qué

- `inertia_` te sirve para el método del codo.
- `silhouette_score` te sirve para medir separación entre clusters.

### Qué significa `random_state=42`

Fija una semilla para que obtengas resultados reproducibles. Eso ayuda mucho en trabajos académicos.

### Graficar el método del codo

```python
plt.figure(figsize=(8, 5))
plt.plot(list(k_values), inertia, marker="o")
plt.title("Elbow Method")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Inercia")
plt.savefig("figuras/elbow_method.png", dpi=300)
plt.show()
```

### Graficar silhouette

```python
plt.figure(figsize=(8, 5))
plt.plot(list(k_values), silhouette_scores, marker="o")
plt.title("Silhouette Score por número de clusters")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Silhouette Score")
plt.savefig("figuras/silhouette_kmeans.png", dpi=300)
plt.show()
```

### Qué debes hacer después

Elegir un `k` razonable, normalmente el que combine:

- buen silhouette score,
- un codo visible,
- clusters interpretables.

### Qué debes explicar

No digas solo "elegí 5". Di por qué.

---

## Paso 14. Entrenar el modelo final K-Means

### Qué debes hacer

Entrenar K-Means con el valor final de `k`.

### Código sugerido

```python
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df["cluster_kmeans"] = kmeans.fit_predict(X_scaled)
```

### Por qué

Esto asigna a cada cliente un número de cluster, que luego usarás para analizar e interpretar grupos.

### Qué debes revisar

```python
df[["CustomerID", "cluster_kmeans"]].head()
```

### Por qué

Te confirma que ya se asignó un cluster a cada fila.

---

## Paso 15. Visualizar los clusters de K-Means

### Qué debes hacer

Crear una gráfica coloreada por cluster.

### Código sugerido

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
plt.savefig("figuras/kmeans_clusters.png", dpi=300)
plt.show()
```

### Por qué

Una visualización clara te ayuda a explicar si los grupos realmente se separan bien.

---

## Paso 16. Aplicar el segundo algoritmo

### Opción recomendada para ti

Usa **Agglomerative Clustering** porque es más fácil de comparar con K-Means.

### Código sugerido

```python
agg = AgglomerativeClustering(n_clusters=5)
df["cluster_agg"] = agg.fit_predict(X_scaled)
```

### Por qué

Este algoritmo agrupa de forma jerárquica y te da una segunda perspectiva del mismo problema.

### Visualización

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
plt.savefig("figuras/agglomerative_clusters.png", dpi=300)
plt.show()
```

### Qué debes medir

```python
silhouette_kmeans = silhouette_score(X_scaled, df["cluster_kmeans"])
silhouette_agg = silhouette_score(X_scaled, df["cluster_agg"])

print("Silhouette K-Means:", silhouette_kmeans)
print("Silhouette Agglomerative:", silhouette_agg)
```

### Por qué

Necesitas una base objetiva para comparar métodos.

---

## Paso 17. Crear tablas resumen por cluster

### Qué debes hacer

Calcular promedios y tamaños por grupo.

### Código sugerido para K-Means

```python
resumen_kmeans = df.groupby("cluster_kmeans")[features].mean()
tam_kmeans = df["cluster_kmeans"].value_counts().sort_index()

resumen_kmeans["size"] = tam_kmeans
resumen_kmeans
```

### Opcional: guardar la tabla

```python
resumen_kmeans.to_csv("resumen_clusters_kmeans.csv")
```

### Por qué

Sin esta tabla, interpretar clusters se vuelve muy superficial. Necesitas evidencias numéricas, no solo gráficas.

---

## Paso 18. Interpretar cada cluster en lenguaje de negocio

### Qué debes hacer

Leer la tabla resumen y describir qué representa cada grupo.

### Cómo pensarlo

Pregúntate:

- ¿son jóvenes o mayores?
- ¿gastan mucho o poco?
- ¿tienen ingresos altos o bajos?
- ¿qué estrategia comercial tendría sentido para ellos?

### Ejemplo de redacción

> El cluster 0 agrupa clientes relativamente jóvenes, con ingreso medio y alto nivel de gasto. Este segmento podría responder bien a promociones frecuentes, programas de fidelización y campañas orientadas a consumo impulsivo.

### Por qué

La actividad no termina en el algoritmo. El valor real está en convertir resultados numéricos en conclusiones útiles.

---

## Paso 19. Comparar formalmente ambos métodos

### Qué debes hacer

Construir una tabla comparativa.

### Código sugerido

```python
comparacion = pd.DataFrame({
    "Metodo": ["K-Means", "Agglomerative"],
    "Numero_clusters": [
        df["cluster_kmeans"].nunique(),
        df["cluster_agg"].nunique()
    ],
    "Silhouette": [
        silhouette_kmeans,
        silhouette_agg
    ]
})

comparacion
```

### Qué debes comentar

- cuál tuvo mejor silhouette,
- cuál fue más fácil de interpretar,
- cuál produjo grupos más coherentes visualmente.

### Por qué

Esto responde directamente a la parte de la rúbrica que exige comparación de algoritmos.

---

## Paso 20. Escribir conclusiones dentro del notebook

### Qué debes hacer

Agregar una celda Markdown final con tus conclusiones.

### Qué debe responder

- qué método funcionó mejor,
- cuántos grupos útiles encontraste,
- qué perfiles de clientes aparecieron,
- cómo podrían usarse esos resultados,
- qué limitaciones tuvo el análisis.

### Ejemplo breve

```md
## Conclusiones

K-Means ofreció la segmentación más clara e interpretable para este conjunto de datos, especialmente al trabajar con cinco grupos. Los clusters encontrados muestran perfiles diferenciados de clientes según edad, ingreso y nivel de gasto, lo cual puede ser útil para campañas de marketing segmentadas. Sin embargo, el análisis está limitado por el tamaño del dataset y por la cantidad reducida de variables disponibles.
```

### Por qué

Las conclusiones muestran que entendiste el problema, no solo que ejecutaste código.

---

## Paso 21. Preparar el informe PDF

### Qué debes hacer

Crear tu informe final en Word, Google Docs, Markdown o el medio que prefieras, y exportarlo como PDF.

### Qué incluir

1. Introducción
2. Objetivo
3. Dataset
4. Análisis exploratorio
5. Preprocesamiento
6. K-Means
7. Segundo algoritmo
8. Comparación
9. Interpretación de clusters
10. Conclusiones
11. Limitaciones y mejoras

### Por qué

Aunque el notebook tenga todo el análisis, el PDF es el entregable formal que más influye en claridad y presentación.

---

## Paso 22. Revisar reproducibilidad

### Qué debes hacer

Cerrar el notebook, volver a abrirlo y ejecutar todo desde cero.

### Dónde hacerlo

En Jupyter Notebook.

### Acción dentro de Jupyter

Usa:

- `Kernel -> Restart & Run All`

### Por qué

Esto confirma que el trabajo corre completo sin errores y en orden. Si falla aquí, el profesor también podría tener problemas al revisarlo.

---

## Paso 23. Preparar la entrega final

### Qué debes hacer

Comprimir los archivos requeridos en un `.zip`.

### Qué incluir

- `informe.pdf`
- `segmentacion_clientes.ipynb`
- carpeta `figuras/`
- `requirements.txt`

### Recomendación extra

Aunque no lo entregues, conserva también:

- `notas_analisis.md`
- `resumen_clusters_kmeans.csv`
- tablas auxiliares

### Por qué

Eso te sirve como respaldo si después debes corregir, defender o reutilizar el trabajo.

---

## 8. Qué deberías registrar para el resguardo de notas

Para maximizar el puntaje, guarda evidencia de tu proceso. Eso te ayuda a redactar bien y a defender decisiones.

## Registra siempre

- objetivo del análisis,
- dataset usado y fuente,
- columnas originales,
- columnas eliminadas y motivo,
- presencia o ausencia de nulos,
- presencia o ausencia de outliers,
- variables seleccionadas,
- técnica de escalado usada,
- valores de `k` probados,
- métricas obtenidas,
- parámetros de cada algoritmo,
- interpretación de cada cluster,
- conclusiones finales.

## Plantilla sugerida para `notas_analisis.md`

```md
# Notas de análisis

## Dataset
- Fuente:
- Fecha de descarga:
- Registros:
- Columnas:

## Limpieza
- Nulos encontrados:
- Duplicados:
- Outliers detectados:
- Columnas eliminadas:

## Variables para clustering
- Variables elegidas:
- Justificación:

## Escalado
- Método usado:
- Motivo:

## K-Means
- Valores de k probados:
- Mejor k:
- Silhouette score:
- Observaciones:

## Segundo método
- Algoritmo:
- Parámetros:
- Métrica o criterio:
- Observaciones:

## Interpretación
- Cluster 0:
- Cluster 1:
- Cluster 2:

## Conclusión
- Mejor método:
- Aplicación real:
- Limitaciones:
```

---

## 9. Ejemplos de qué deberías obtener

## Ejemplo de tablas

Debes sacar algo similar a:

### Tabla descriptiva

| Variable | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Age | 38.8 | 13.9 | 18 | 70 |
| Annual Income (k$) | 60.6 | 26.3 | 15 | 137 |
| Spending Score (1-100) | 50.2 | 25.8 | 1 | 99 |

### Resumen por cluster

| Cluster | Tamaño | Edad promedio | Ingreso promedio | Gasto promedio |
|---|---:|---:|---:|---:|
| 0 | 39 | 25.3 | 26.3 | 78.4 |
| 1 | 45 | 43.1 | 55.2 | 49.0 |
| 2 | 23 | 32.0 | 88.5 | 17.4 |

Los números exactos pueden cambiar, pero esta es la idea del tipo de evidencia que debes presentar.

## Ejemplo de figuras

Debes tener como mínimo:

- distribución de variables,
- detección de outliers,
- método del codo,
- clusters con K-Means,
- clusters con segundo método.

## Ejemplo de observaciones valiosas

- "El escalado fue necesario para evitar que la variable de ingreso dominara la distancia euclidiana."
- "K-Means generó grupos más fáciles de interpretar visualmente."
- "DBSCAN permitió identificar posibles puntos de ruido, aunque dependió mucho de la elección de parámetros."
- "Los segmentos hallados podrían apoyar campañas diferenciadas según nivel de gasto."

---

## 10. Estructura recomendada del informe PDF

Tu `informe.pdf` puede seguir esta estructura:

1. **Introducción**
2. **Objetivo**
3. **Descripción del dataset**
4. **Análisis exploratorio**
5. **Preprocesamiento**
6. **Aplicación de K-Means**
7. **Aplicación del segundo método**
8. **Comparación de resultados**
9. **Interpretación de clusters**
10. **Conclusiones**
11. **Limitaciones y trabajo futuro**

### Qué no debe faltar

- tablas,
- figuras,
- interpretación,
- comparación,
- redacción formal,
- referencias al dataset.

---

## 11. Estrategia para sacar el mayor puntaje posible

## Haz esto sí o sí

- usa **dos algoritmos**,
- justifica cada decisión importante,
- incluye métricas y no solo gráficas,
- interpreta cada cluster en lenguaje de negocio,
- mantén notebook limpio y ordenado,
- exporta todas las figuras,
- redacta un informe visualmente profesional.

## Errores que te bajan puntos

- no escalar variables,
- usar solo un algoritmo,
- no justificar el número de clusters,
- poner gráficas sin análisis,
- no comparar métodos,
- no comentar el código,
- entregar notebook desordenado,
- conclusiones genéricas sin relación con resultados.

---

## 12. Propuesta de plan de trabajo

Si quieres hacerlo sin perderte, sigue este orden:

### Día 1

- descargar dataset,
- explorar columnas,
- hacer análisis descriptivo,
- detectar outliers y nulos.

### Día 2

- preparar variables,
- escalar datos,
- entrenar K-Means,
- calcular elbow y silhouette.

### Día 3

- entrenar segundo algoritmo,
- comparar resultados,
- generar gráficas finales,
- guardar métricas y tablas.

### Día 4

- redactar informe,
- revisar notebook,
- exportar PDF y figuras,
- preparar `.zip`.

---

## 13. Checklist final antes de entregar

- `segmentacion_clientes.ipynb` abre sin errores.
- Todas las celdas corren en orden.
- El notebook explica cada etapa.
- Hay mínimo dos algoritmos.
- Está justificado el número de clusters o parámetros.
- Existen métricas comparativas.
- Hay interpretación de cada cluster.
- El informe PDF está bien redactado.
- La carpeta `figuras/` contiene los gráficos usados.
- `requirements.txt` permite reproducir el entorno.
- El `.zip` contiene exactamente lo solicitado.

---

## 14. Recomendación final como junior developer

Tu mejor estrategia no es hacer algo demasiado complejo. Tu mejor estrategia es hacer un trabajo:

- correcto,
- claro,
- justificable,
- reproducible,
- bien presentado.

Para esta actividad, una combinación como **K-Means + Agglomerative Clustering** suele ser la ruta más segura para un resultado sólido y fácil de explicar. Si ya te sientes más cómodo con parámetros y validación, entonces **K-Means + DBSCAN** puede hacer que tu análisis se vea más maduro técnicamente.

Si quieres aspirar al máximo puntaje, piensa así:

> No solo debo mostrar resultados. Debo demostrar criterio técnico, orden, interpretación y capacidad de comunicar lo que hice.

---

## 15. Siguiente paso recomendado

Empieza creando estos archivos:

- `segmentacion_clientes.ipynb`
- `requirements.txt`
- carpeta `figuras/`
- `notas_analisis.md`

Y dentro del notebook avanza exactamente con la estructura de la sección 6 de esta guía.
