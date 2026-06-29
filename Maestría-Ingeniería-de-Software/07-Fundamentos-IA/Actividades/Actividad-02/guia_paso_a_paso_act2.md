# Guía paso a paso para la Actividad 2

## Tema de la actividad
**Clasificación de noticias mediante procesamiento de lenguaje natural**

Esta guía está pensada para ayudarte a resolver la actividad de forma sólida aunque vengas desde un nivel **junior**, y al mismo tiempo orientarte para obtener el **mayor puntaje posible** según la rúbrica.

---


## 1. Qué te están pidiendo realmente

La actividad no te pide solo entrenar un modelo. Te pide demostrar que entiendes un flujo completo de **Machine Learning aplicado a texto**:

1. Cargar y entender un dataset de noticias etiquetadas.
2. Preparar texto de forma correcta para análisis.
3. Convertir texto en números para que los modelos puedan usarlo.
4. Entrenar al menos tres modelos supervisados.
5. Evaluarlos con métricas adecuadas.
6. Analizar errores reales, no solo mostrar accuracy.
7. Elegir y justificar un modelo final.
8. Entregar código y reporte con calidad técnica y académica.

Si haces solo un notebook con `fit()` y `predict()`, te faltará una parte grande de la actividad. Para aspirar al mejor puntaje, debes mostrar:

- criterio técnico,
- orden metodológico,
- justificación de decisiones,
- interpretación de métricas,
- capacidad de comunicar resultados.

---

## 2. Entregables obligatorios

Debes entregar un `.zip` con:

- `informe.pdf`
- `clasificacion_noticias_pln.ipynb`
- carpeta `figuras/`
- `requirements.txt`

### Recomendación extra para trabajar mejor

Aunque no lo pidan como entregable, te conviene crear también:

- `notas_analisis.md`
- `metricas_modelos.csv`
- `ejemplos_errores.csv`
- `resumen_experimentos.md`

### Por qué conviene

Estos archivos te ayudan a:

- no perder hallazgos,
- justificar por qué elegiste un modelo,
- documentar pruebas y parámetros,
- redactar el informe con mayor solidez.

---

## 3. Rúbrica traducida a acciones concretas

### Criterio 1. Preprocesamiento y representación del texto (20%)
Para sacar el máximo:

- limpia el texto correctamente,
- explicas cada transformación,
- justificas tu representación vectorial,
- comparas si conviene usar TF-IDF o embeddings,
- aplicas un pipeline reproducible.

### Criterio 2. Implementación rigurosa de varios modelos supervisados (25%)
Para sacar el máximo:

- entrenas al menos tres modelos,
- defines claramente entrenamiento y prueba,
- usas validación cruzada,
- controlas parámetros básicos,
- comparas resultados con orden.

### Criterio 3. Análisis crítico de métricas y justificación de resultados (25%)
Para sacar el máximo:

- reportas Accuracy, Precision, Recall y F1-score,
- incluyes matriz de confusión,
- revisas errores frecuentes,
- explicas debilidades de los modelos,
- justificas cuál eliges y por qué.

### Criterio 4. Claridad, redacción y apoyo visual en el informe (20%)
Para sacar el máximo:

- redacta con lenguaje técnico claro,
- usa tablas y gráficas bien rotuladas,
- organiza secciones lógicas,
- evita pegar capturas sin explicación.

### Criterio 5. Código comentado, limpio y reproducible (10%)
Para sacar el máximo:

- notebook ordenado,
- celdas con flujo claro,
- comentarios breves pero útiles,
- dependencias registradas,
- misma salida al ejecutar desde cero.

---

## 4. Términos importantes que debes entender

### Procesamiento de Lenguaje Natural (PLN)
Rama de la inteligencia artificial que trabaja con texto o lenguaje humano. Aquí lo usarás para convertir noticias en una forma que un modelo pueda clasificar.

### Clasificación supervisada
Es un problema donde ya tienes ejemplos con etiqueta conocida. En este caso, cada noticia ya pertenece a una categoría:

- `World`
- `Sports`
- `Business`
- `Science/Technology`

### Etiqueta
Es la categoría correcta que el modelo debe aprender a predecir.

### Corpus
Conjunto de textos que se usarán para análisis. Aquí, el corpus son todas las noticias del dataset.

### Preprocesamiento de texto
Conjunto de pasos para limpiar y normalizar el texto antes de vectorizarlo o entrenar modelos.

### Normalización
Proceso para llevar el texto a un formato consistente, por ejemplo:

- convertir a minúsculas,
- eliminar signos innecesarios,
- limpiar caracteres especiales.

### Stopwords
Palabras muy frecuentes que a veces aportan poco significado, como "the", "and", "is". No siempre se eliminan obligatoriamente, pero suele hacerse en modelos clásicos de bolsa de palabras.

### Tokenización
Proceso de dividir el texto en piezas más pequeñas, normalmente palabras o tokens.

### Lematización
Proceso de llevar una palabra a su forma base o canónica. Por ejemplo:

- `running` -> `run`
- `studies` -> `study`

### Vectorización
Conversión de texto a números.

### TF-IDF
Técnica que representa un texto según la importancia relativa de cada palabra dentro del documento y del corpus total.

### Embeddings
Representaciones vectoriales densas de palabras o textos, donde palabras parecidas suelen estar cerca en el espacio vectorial.

### Train/Test Split
Separación del dataset en:

- entrenamiento,
- prueba.

Sirve para evaluar el modelo con datos no vistos.

### Validación cruzada
Técnica para medir si el modelo es consistente en distintos subconjuntos de entrenamiento/prueba.

### Accuracy
Porcentaje total de predicciones correctas.

### Precision
De todas las predicciones que el modelo hizo para una clase, cuántas fueron realmente correctas.

### Recall
De todos los ejemplos reales de una clase, cuántos detectó correctamente el modelo.

### F1-score
Media armónica entre Precision y Recall. Es útil cuando quieres balance entre ambas.

### Matriz de confusión
Tabla que muestra cuántos ejemplos de cada clase fueron clasificados correctamente o confundidos con otra.

### Overfitting
Cuando el modelo aprende demasiado bien el entrenamiento y luego generaliza mal en datos nuevos.

---

## 5. Qué necesitas para implementar la actividad

## Software

- Python 3.10 o superior
- Jupyter Notebook o VS Code con notebooks

## Librerías recomendadas

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `nltk`
- `spacy`
- `jupyter`

### Nota importante

Para una actividad académica como esta, la opción más segura y clara es trabajar con:

- preprocesamiento clásico,
- vectorización con `TF-IDF`,
- modelos lineales o probabilísticos.

Eso te permite explicar mejor el flujo y defender tus resultados.

### Ejemplo de `requirements.txt`

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
nltk
spacy
jupyter
```

---

## 6. Estrategia recomendada para esta actividad

Si quieres una estrategia técnicamente correcta y realista como junior, usa esta combinación:

- **Representación principal**: `TF-IDF`
- **Modelo 1**: `Multinomial Naive Bayes`
- **Modelo 2**: `Logistic Regression`
- **Modelo 3**: `LinearSVC`

### Por qué esta combinación es buena

- `Naive Bayes` es clásico y rápido en texto.
- `Logistic Regression` suele dar buen rendimiento e interpretabilidad.
- `LinearSVC` normalmente rinde muy bien en clasificación de texto.

### Qué evita esta estrategia

Evita complejidad innecesaria como:

- redes neuronales profundas,
- pipelines demasiado pesados,
- embeddings complejos difíciles de justificar en poco tiempo.

Si después quieres verte más técnico, puedes agregar una comparación breve con embeddings, pero para el mejor equilibrio entre claridad, resultado y tiempo, esta combinación es muy buena.

---

## 7. Estructura recomendada del notebook

Tu notebook debería llamarse:

`clasificacion_noticias_pln.ipynb`

Orden recomendado:

1. Título y objetivo
2. Importación de librerías
3. Carga del dataset
4. Exploración del dataset
5. Balance de clases
6. Limpieza y normalización del texto
7. Tokenización y lematización
8. División entrenamiento/prueba
9. Vectorización con TF-IDF
10. Entrenamiento de modelo 1
11. Entrenamiento de modelo 2
12. Entrenamiento de modelo 3
13. Validación cruzada
14. Evaluación de métricas
15. Matrices de confusión
16. Análisis de errores
17. Comparación de modelos
18. Selección del modelo final
19. Conclusiones

---

## 8. Paso a paso profundo para resolver la actividad

Esta sección está escrita como una receta detallada. Te dice qué hacer, dónde hacerlo, qué comandos usar y por qué.

## Paso 0. Entrar a la carpeta de la actividad

### Qué debes hacer

Trabajar dentro de:

`Actividad-02`

### Dónde hacerlo

En PowerShell.

### Comandos

```powershell
cd "C:\Users\Dev\repos\toonchavez8\Unir-Notes\Maestría-Ingeniería-de-Software\07-Fundamentos-IA\Actividades\Actividad-02"
Get-ChildItem
```

### Por qué

- `cd` te lleva a la ubicación correcta.
- `Get-ChildItem` te deja revisar qué archivos ya existen.

---

## Paso 1. Descargar el dataset y ubicarlo en la carpeta

### Qué debes hacer

Descargar el dataset desde Kaggle y poner los archivos CSV dentro de `Actividad-02`.

### Qué archivos podrías encontrar

Dependiendo del dataset, normalmente verás algo como:

- `train.csv`
- `test.csv`

o un único archivo con noticias y etiquetas.

### Por qué

Debes tener el dataset junto a tu notebook o en una subcarpeta clara para evitar errores de rutas.

### Qué registrar

- URL del dataset
- fecha de descarga
- archivos descargados
- número esperado de clases

---

## Paso 2. Crear la estructura mínima de trabajo

### Qué debes hacer

Crear carpetas y archivos de apoyo.

### Dónde hacerlo

En PowerShell, dentro de `Actividad-02`.

### Comandos

```powershell
New-Item -ItemType Directory -Path ".\figuras" -Force
New-Item -ItemType File -Path ".\notas_analisis.md" -Force
New-Item -ItemType File -Path ".\metricas_modelos.csv" -Force
New-Item -ItemType File -Path ".\resumen_experimentos.md" -Force
New-Item -ItemType File -Path ".\requirements.txt" -Force
```

### Por qué

- `figuras/` guarda imágenes exportadas.
- `notas_analisis.md` guarda observaciones y decisiones.
- `metricas_modelos.csv` te permite registrar resultados ordenados.
- `resumen_experimentos.md` te ayuda a rastrear pruebas de configuración.

---

## Paso 3. Crear y activar un entorno virtual

### Qué debes hacer

Crear un entorno virtual para aislar dependencias.

### Comandos

```powershell
`python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

### Por qué

Te evita conflictos con otras instalaciones de Python y facilita la reproducibilidad.

### Qué significa entorno virtual

Es un espacio aislado donde instalas solo los paquetes necesarios para esta actividad.

---

## Paso 4. Instalar librerías necesarias

### Qué debes hacer

Instalar los paquetes que usarás.

### Comando

```powershell
pip install pandas numpy matplotlib seaborn scikit-learn nltk spacy jupyter
```

### Por qué

- `pandas` para manejar tablas.
- `numpy` para operaciones numéricas.
- `matplotlib` y `seaborn` para visualización.
- `scikit-learn` para vectorización, modelos y métricas.
- `nltk` y `spacy` para PLN.
- `jupyter` para el notebook.

### Guardar dependencias

```powershell
pip freeze > requirements.txt
```

### Por qué

Deja registrado el entorno exacto que usaste.

---

## Paso 5. Descargar recursos de PLN

### Qué debes hacer

Descargar recursos lingüísticos necesarios para tokenización, stopwords o lematización.

### Dónde hacerlo

Puedes hacerlo en una celda de notebook o desde Python.

### Código sugerido en notebook

```python
import nltk
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")
```

### Si quieres usar spaCy para lematizar

Instala el modelo en terminal:

```powershell
python -m spacy download en_core_web_sm
```

### Por qué

Sin estos recursos, varias funciones de limpieza de texto fallarán.

### Recomendación práctica

Si quieres menos fricción, usa:

- `nltk` para stopwords y lematización,
- `TF-IDF` con modelos clásicos.

Es suficiente y más fácil de explicar.

---

## Paso 6. Abrir Jupyter Notebook

### Qué debes hacer

Iniciar Jupyter.

### Comando

```powershell
jupyter notebook
```

### Qué archivo debes crear

`clasificacion_noticias_pln.ipynb`

### Por qué

Ese es el nombre coherente con el entregable solicitado.

---

## Paso 7. Crear portada y objetivo en el notebook

### Qué debes hacer

Crear una celda Markdown con:

- título,
- nombre de la actividad,
- objetivo,
- dataset usado.

### Ejemplo

```md
# Clasificación de noticias mediante procesamiento de lenguaje natural

## Objetivo
Desarrollar y comparar varios modelos supervisados para clasificar noticias en categorías temáticas usando técnicas de PLN y representación vectorial del texto.
```

### Por qué

Esto mejora la organización del notebook y le da presentación académica.

---

## Paso 8. Importar librerías

### Qué debes hacer

Crear una celda inicial con importaciones.

### Código sugerido

```python
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score
)
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
```

### Si usarás NLTK

```python
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
```

### Por qué

Tener importaciones al inicio hace tu notebook más limpio y reproducible.

---

## Paso 9. Cargar el dataset

### Qué debes hacer

Leer el o los archivos CSV y mostrar una muestra.

### Caso A. Si el dataset viene con `train.csv` y `test.csv`

```python
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

train_df.head()
```

### Caso B. Si viene en un único CSV

```python
df = pd.read_csv("ag_news.csv")
df.head()
```

### Por qué

Necesitas confirmar:

- que el archivo carga bien,
- cómo vienen las columnas,
- si las etiquetas vienen como texto o números.

### Qué debes revisar enseguida

```python
train_df.shape
train_df.columns
train_df.info()
```

### Qué registrar en `notas_analisis.md`

- nombre de columnas,
- cantidad de registros,
- formato de etiquetas,
- posibles columnas de texto útiles.

---

## Paso 10. Entender qué texto usarás

### Qué debes hacer

Identificar qué columna o combinación de columnas representa la noticia.

En AG News suele haber algo como:

- `Class Index`
- `Title`
- `Description`

### Recomendación

Crear una columna de texto combinando título y descripción.

### Código sugerido

```python
train_df["text"] = train_df["Title"].fillna("") + " " + train_df["Description"].fillna("")
test_df["text"] = test_df["Title"].fillna("") + " " + test_df["Description"].fillna("")
```

### Por qué

El título aporta información resumida y la descripción agrega contexto. Combinarlos suele mejorar la clasificación.

### Qué hacer con la etiqueta

```python
train_df["label"] = train_df["Class Index"]
test_df["label"] = test_df["Class Index"]
```

---

## Paso 11. Hacer análisis exploratorio inicial

### Qué debes hacer

Examinar:

- muestra de noticias,
- distribución por clase,
- longitud de los textos,
- posibles nulos o duplicados.

### Código sugerido

```python
train_df[["label", "text"]].head()
```

```python
train_df["label"].value_counts()
```

```python
train_df["text_length"] = train_df["text"].str.len()
train_df["text_length"].describe()
```

```python
train_df.isnull().sum()
```

### Graficar distribución por clase

```python
plt.figure(figsize=(8, 5))
sns.countplot(data=train_df, x="label")
plt.title("Distribución de noticias por clase")
plt.savefig("figuras/distribucion_clases.png", dpi=300)
plt.show()
```

### Por qué

Esto responde directamente a la parte del enunciado que pide estadísticas de distribución y revisión de balanceo.

### Qué debes comentar

- si las clases están balanceadas o no,
- si hay textos muy cortos o muy largos,
- si hay nulos o anomalías.
## Paso 12. Crear una función de limpieza de texto

### Qué debes hacer

Definir una función que normalice cada noticia.

### Código sugerido

```python
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words and len(t) > 2]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)
```

### Por qué se hace cada parte

- `lower()`: evita tratar `Market` y `market` como palabras distintas.
- regex `[^a-zA-Z\s]`: elimina signos y caracteres no alfabéticos.
- `word_tokenize`: separa palabras.
- filtro de `stop_words`: elimina palabras demasiado frecuentes.
- `len(t) > 2`: quita tokens muy cortos poco informativos.
- lematización: reduce variantes morfológicas.

### Qué debes mencionar en el informe

No digas solo “limpié el texto”. Explica exactamente qué transformaciones aplicaste.

---

## Paso 13. Aplicar la limpieza al dataset

### Qué debes hacer

Crear una nueva columna con el texto limpio.

### Código sugerido

```python
train_df["clean_text"] = train_df["text"].apply(clean_text)
test_df["clean_text"] = test_df["text"].apply(clean_text)
```

### Qué revisar

```python
train_df[["text", "clean_text"]].head()
```

### Por qué

Debes verificar visualmente que la limpieza realmente hizo lo esperado y no destruyó demasiado el contenido.

### Qué guardar como evidencia

- ejemplos antes/después,
- explicación del pipeline de limpieza.

---

## Paso 14. Separar entrenamiento y prueba

### Qué debes hacer

Si ya tienes `train.csv` y `test.csv`, puedes usar esa separación directamente.

Si tienes un solo archivo, crea una partición tú mismo.

### Caso con un único CSV

```python
X_train, X_test, y_train, y_test = train_test_split(
    df["clean_text"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)
```

### Caso con train/test ya separados

```python
X_train = train_df["clean_text"]
y_train = train_df["label"]
X_test = test_df["clean_text"]
y_test = test_df["label"]
```

### Por qué

- separar entrenamiento y prueba evita evaluar sobre datos ya vistos,
- `stratify` conserva la proporción de clases.

---

## Paso 15. Vectorizar texto con TF-IDF

### Qué debes hacer

Transformar el texto limpio en una matriz numérica.

### Código sugerido

```python
tfidf = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1, 2),
    min_df=3,
    max_df=0.95
)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)
```

### Qué significa cada parámetro

- `max_features=20000`: limita vocabulario para controlar tamaño.
- `ngram_range=(1, 2)`: usa unigramas y bigramas.
- `min_df=3`: ignora palabras extremadamente raras.
- `max_df=0.95`: ignora términos demasiado frecuentes.

### Por qué usar TF-IDF

Es una técnica clásica, fuerte y muy adecuada para clasificación de texto con modelos lineales.

### Qué debes explicar

Que el modelo no entiende texto directamente: primero necesitas convertirlo a representación numérica.

---

## Paso 16. Entrenar el primer modelo: Naive Bayes

### Qué debes hacer

Entrenar `MultinomialNB`.

### Código sugerido

```python
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
nb_pred = nb_model.predict(X_test_tfidf)
```

### Por qué

Es uno de los modelos clásicos más usados en texto y suele ser un buen baseline.

### Qué significa baseline

Es un modelo de referencia inicial con el que luego comparas modelos más fuertes.

---

## Paso 17. Entrenar el segundo modelo: Logistic Regression

### Código sugerido

```python
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_tfidf, y_train)
lr_pred = lr_model.predict(X_test_tfidf)
```

### Por qué

Suele rendir muy bien en texto y además es relativamente interpretable.

### Qué debes cuidar

`max_iter=1000` evita problemas de convergencia frecuentes.

---

## Paso 18. Entrenar el tercer modelo: LinearSVC

### Código sugerido

```python
svm_model = LinearSVC()
svm_model.fit(X_train_tfidf, y_train)
svm_pred = svm_model.predict(X_test_tfidf)
```

### Por qué

`LinearSVC` suele dar resultados muy competitivos en clasificación de texto de alta dimensionalidad.

---

## Paso 19. Evaluar métricas de cada modelo

### Qué debes hacer

Calcular Accuracy, Precision, Recall y F1-score.

### Función sugerida

```python
def evaluate_model(name, y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        average="weighted"
    )
    
    return {
        "modelo": name,
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }
```

### Usarla

```python
results = []
results.append(evaluate_model("Naive Bayes", y_test, nb_pred))
results.append(evaluate_model("Logistic Regression", y_test, lr_pred))
results.append(evaluate_model("LinearSVC", y_test, svm_pred))

results_df = pd.DataFrame(results)
results_df
```

### Guardar resultados

```python
results_df.to_csv("metricas_modelos.csv", index=False)
```

### Por qué

Así dejas una comparación clara, exportable y fácil de convertir en tabla para el informe.

---

## Paso 20. Generar classification report

### Qué debes hacer

Ver el detalle por clase.

### Código sugerido

```python
print(classification_report(y_test, svm_pred))
```

### Por qué

El reporte por clase te deja ver si un modelo funciona mejor en unas categorías que en otras.

### Qué debes observar

- si alguna clase tiene menor recall,
- si alguna clase se confunde más que otras,
- si el rendimiento está balanceado.

---

## Paso 21. Crear matrices de confusión

### Qué debes hacer

Generar una matriz de confusión para cada modelo o al menos para el mejor.

### Código sugerido

```python
cm = confusion_matrix(y_test, svm_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")
plt.title("Matriz de confusión - LinearSVC")
plt.savefig("figuras/matriz_confusion_linearsvc.png", dpi=300)
plt.show()
```

### Por qué

La matriz de confusión muestra exactamente dónde se equivoca el modelo.

### Qué debes explicar

No pongas solo la imagen. Comenta qué clases se confunden y por qué podría pasar.

---

## Paso 22. Usar validación cruzada

### Qué debes hacer

Aplicar validación cruzada sobre el conjunto de entrenamiento para comparar consistencia.

### Recomendación

Hazlo con pipelines para que el TF-IDF se entrene correctamente dentro de cada fold.

### Código sugerido

```python
nb_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=20000, ngram_range=(1, 2), min_df=3, max_df=0.95)),
    ("model", MultinomialNB())
])

lr_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=20000, ngram_range=(1, 2), min_df=3, max_df=0.95)),
    ("model", LogisticRegression(max_iter=1000))
])

svm_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=20000, ngram_range=(1, 2), min_df=3, max_df=0.95)),
    ("model", LinearSVC())
])
```

### Ejecutar validación cruzada

```python
cv_nb = cross_val_score(nb_pipeline, X_train, y_train, cv=5, scoring="f1_weighted")
cv_lr = cross_val_score(lr_pipeline, X_train, y_train, cv=5, scoring="f1_weighted")
cv_svm = cross_val_score(svm_pipeline, X_train, y_train, cv=5, scoring="f1_weighted")
```

### Ver resultados

```python
print("NB CV mean:", cv_nb.mean())
print("LR CV mean:", cv_lr.mean())
print("SVM CV mean:", cv_svm.mean())
```

### Por qué

La validación cruzada mide estabilidad. No basta con que un modelo salga bien una vez.

---

## Paso 23. Analizar errores reales

### Qué debes hacer

Encontrar ejemplos mal clasificados y revisarlos manualmente.

### Código sugerido

```python
errores_svm = pd.DataFrame({
    "text": X_test.values,
    "real": y_test.values,
    "predicho": svm_pred
})

errores_svm = errores_svm[errores_svm["real"] != errores_svm["predicho"]]
errores_svm.head(20)
```

### Guardar errores

```python
errores_svm.to_csv("ejemplos_errores.csv", index=False)
```

### Qué debes buscar

- noticias ambiguas,
- clases semánticamente cercanas,
- textos demasiado cortos,
- términos que podrían pertenecer a varias categorías.

### Por qué

Esta parte da mucha profundidad técnica al informe. Demuestra que no te quedaste solo con métricas.

---

## Paso 24. Comparar formalmente los modelos

### Qué debes hacer

Construir una tabla comparativa final.

### Qué debe incluir

- modelo,
- accuracy,
- precision,
- recall,
- F1-score,
- promedio de validación cruzada,
- observaciones.

### Ejemplo de redacción

> LinearSVC presentó el mejor equilibrio entre rendimiento global y consistencia en validación cruzada, mientras que Naive Bayes destacó por su rapidez y simplicidad, aunque con menor precisión en clases más ambiguas.

### Por qué

Esta tabla será una de las piezas más importantes del informe.

---

## Paso 25. Elegir el modelo final y justificarlo

### Qué debes hacer

Seleccionar un modelo final con base en:

- rendimiento,
- consistencia,
- interpretabilidad,
- costo computacional.

### Cómo justificar bien

No digas solo “elegí el que tuvo mayor accuracy”. Debes considerar:

- si también tuvo buen F1,
- si fue estable en validación cruzada,
- si sus errores fueron razonables,
- si su complejidad tiene sentido para el problema.

### Ejemplo de justificación

> Se seleccionó LinearSVC como modelo final debido a que obtuvo el mejor F1-score ponderado y mostró un comportamiento consistente en validación cruzada. Además, su desempeño fue especialmente sólido en clases con vocabulario técnico y periodístico distintivo, manteniendo un equilibrio adecuado entre calidad predictiva y costo computacional.

---

## Paso 26. Redactar conclusiones en el notebook

### Qué debes hacer

Crear una celda Markdown final con:

- resumen del proceso,
- mejor modelo,
- principales hallazgos,
- limitaciones,
- mejoras futuras.

### Por qué

Esto cierra el trabajo con criterio y claridad.

### Limitaciones razonables que puedes mencionar

- preprocesamiento clásico puede perder contexto semántico,
- TF-IDF no capta significado profundo,
- posibles diferencias sutiles entre categorías generan confusión,
- no se usaron modelos transformadores.

### Mejoras futuras

- probar embeddings de palabras o de documentos,
- usar BERT o modelos tipo transformer,
- ajustar hiperparámetros,
- ampliar análisis interpretativo de errores.

---

## Paso 27. Preparar el informe PDF

### Estructura recomendada

1. Introducción
2. Objetivo
3. Descripción del dataset
4. Análisis exploratorio
5. Preprocesamiento del texto
6. Representación vectorial
7. Modelos entrenados
8. Evaluación de resultados
9. Análisis de errores
10. Selección del modelo final
11. Conclusiones
12. Limitaciones y mejoras futuras

### Qué no debe faltar

- tablas de métricas,
- gráficas de distribución,
- matrices de confusión,
- ejemplos de errores,
- justificación del modelo final.

---

## Paso 28. Verificar reproducibilidad

### Qué debes hacer

Reiniciar el notebook y ejecutarlo completo.

### Dentro de Jupyter

- `Kernel -> Restart & Run All`

### Por qué

Te asegura que no dependes de variables viejas en memoria y que la entrega funciona de principio a fin.

---

## Paso 29. Preparar la entrega final

### Qué debes incluir en el `.zip`

- `informe.pdf`
- `clasificacion_noticias_pln.ipynb`
- carpeta `figuras/`
- `requirements.txt`

### Qué conviene conservar aunque no lo entregues

- `notas_analisis.md`
- `metricas_modelos.csv`
- `ejemplos_errores.csv`
- `resumen_experimentos.md`

### Por qué

Es tu respaldo técnico y te ayuda si luego debes corregir o reutilizar el trabajo.

---

## 9. Qué deberías registrar para el resguardo de notas

Para sacar mejor puntaje, no improvises. Documenta tu proceso.

## Registra siempre

- fuente del dataset,
- fecha de descarga,
- columnas disponibles,
- formato de etiquetas,
- balance de clases,
- nulos y duplicados,
- estrategia de limpieza,
- decisiones sobre stopwords,
- método de lematización,
- configuración de TF-IDF,
- modelos entrenados,
- parámetros relevantes,
- resultados de test,
- resultados de validación cruzada,
- ejemplos de errores,
- justificación del modelo final.

## Plantilla sugerida para `notas_analisis.md`

```md
# Notas de análisis

## Dataset
- Fuente:
- Fecha de descarga:
- Archivos:
- Número de clases:
- Columnas:

## Exploración
- Nulos:
- Duplicados:
- Balance de clases:
- Longitud promedio de texto:

## Preprocesamiento
- Minúsculas:
- Eliminación de caracteres:
- Stopwords:
- Tokenización:
- Lematización:
- Observaciones:

## Vectorización
- Método:
- Parámetros:
- Justificación:

## Modelos
- Modelo 1:
- Modelo 2:
- Modelo 3:

## Métricas
- Accuracy:
- Precision:
- Recall:
- F1:
- Validación cruzada:

## Errores
- Clases más confundidas:
- Posibles causas:

## Selección final
- Modelo elegido:
- Justificación:
- Limitaciones:
- Mejoras futuras:
```

---

## 10. Ejemplos de qué deberías obtener

## Ejemplo de tabla de distribución por clase

| Clase | Cantidad |
|---|---:|
| World | 30000 |
| Sports | 30000 |
| Business | 30000 |
| Science/Technology | 30000 |

Los números exactos pueden variar según la versión del dataset, pero la idea es identificar si las clases están equilibradas.

## Ejemplo de tabla de métricas

| Modelo | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Naive Bayes | 0.89 | 0.89 | 0.89 | 0.89 |
| Logistic Regression | 0.91 | 0.91 | 0.91 | 0.91 |
| LinearSVC | 0.92 | 0.92 | 0.92 | 0.92 |

Los valores son ilustrativos. Tus resultados reales pueden cambiar.

## Ejemplo de observaciones valiosas

- "La combinación de título y descripción mejoró la riqueza semántica del texto de entrada."
- "La eliminación de stopwords redujo ruido sin perder información temática relevante."
- "LinearSVC mostró mejor separación entre categorías periodísticas con vocabulario especializado."
- "Las mayores confusiones ocurrieron entre `World` y `Business`, posiblemente por noticias de economía internacional."

---

## 11. Estructura recomendada del informe PDF

Tu `informe.pdf` puede seguir esta estructura:

1. Introducción
2. Objetivo
3. Descripción del dataset
4. Análisis exploratorio
5. Preprocesamiento
6. Vectorización del texto
7. Modelos supervisados entrenados
8. Evaluación con métricas
9. Matriz de confusión y análisis de errores
10. Comparación de modelos
11. Selección del modelo final
12. Conclusiones
13. Limitaciones y mejoras

### Qué deben ver claramente tus profesores

- que entiendes el problema,
- que justificaste las decisiones,
- que mediste bien el rendimiento,
- que sabes interpretar errores,
- que elegiste un modelo final con base técnica.

---

## 12. Errores comunes que te pueden bajar puntos

- entrenar modelos sin explicar preprocesamiento,
- usar una sola métrica,
- no revisar balance de clases,
- no usar validación cruzada,
- no analizar errores,
- no justificar la elección del modelo final,
- mostrar tablas sin interpretación,
- no dejar el notebook reproducible.

---

## 13. Estrategia para sacar el mayor puntaje posible

## Haz esto sí o sí

- usa al menos tres modelos,
- usa `TF-IDF` con parámetros explicados,
- aplica validación cruzada,
- reporta varias métricas,
- incluye matriz de confusión,
- analiza ejemplos mal clasificados,
- justifica el modelo final,
- presenta figuras limpias y tablas comparativas.

## Qué enfoque suele ser más seguro

Para un trabajo fuerte y defendible:

- `TF-IDF + Naive Bayes`
- `TF-IDF + Logistic Regression`
- `TF-IDF + LinearSVC`

Eso suele darte un análisis serio, claro y con buen rendimiento.

---

## 14. Plan de trabajo recomendado

### Día 1

- descargar dataset,
- revisar columnas y etiquetas,
- analizar distribución por clase,
- preparar estructura de archivos.

### Día 2

- implementar limpieza de texto,
- crear texto combinado,
- aplicar tokenización y lematización,
- revisar ejemplos antes/después.

### Día 3

- vectorizar con TF-IDF,
- entrenar los tres modelos,
- calcular métricas base.

### Día 4

- aplicar validación cruzada,
- generar matrices de confusión,
- analizar errores.

### Día 5

- redactar informe,
- revisar notebook,
- exportar figuras,
- preparar `.zip`.

---

## 15. Checklist final antes de entregar

- `clasificacion_noticias_pln.ipynb` corre sin errores.
- Las importaciones están completas.
- El dataset carga correctamente.
- Se explica el preprocesamiento del texto.
- Hay representación vectorial justificada.
- Se entrenan al menos tres modelos.
- Se usa validación cruzada.
- Se reportan Accuracy, Precision, Recall y F1-score.
- Existe al menos una matriz de confusión.
- Hay análisis de errores reales.
- El modelo final está justificado.
- El PDF tiene buena redacción y apoyo visual.
- `requirements.txt` está incluido.
- La carpeta `figuras/` contiene los gráficos usados.

---

## 16. Recomendación final como junior developer

No intentes impresionar con demasiada complejidad si todavía no dominas bien el flujo. Para sacar una buena calificación, es mejor hacer un trabajo:

- metodológicamente correcto,
- claro,
- bien explicado,
- reproducible,
- con análisis crítico real.

En esta actividad, un enfoque clásico y bien ejecutado suele ser más fuerte académicamente que una solución más sofisticada pero mal explicada.

La lógica correcta es esta:

> No basta con que el modelo acierte. Debo demostrar que entiendo cómo preparé el texto, cómo evalué los modelos, por qué uno funciona mejor y qué limitaciones tiene mi solución.

---

## 17. Siguiente paso recomendado

Empieza creando:

- `clasificacion_noticias_pln.ipynb`
- `requirements.txt`
- carpeta `figuras/`
- `notas_analisis.md`

Y sigue exactamente la estructura de las secciones 7 y 8 de esta guía.
