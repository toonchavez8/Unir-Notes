# Analysis Profundo Del Notebook De Clasificacion De Noticias Con PLN

## Proposito Del Documento

Este documento explica el flujo completo que aparece en `markdown-export/clasificacion_noticias_pln.md`. La idea no es repetir el notebook sin mas, sino dejar claro que hace cada bloque, por que se hizo asi y que lectura tecnica se obtiene de los resultados.

Tambien incorpora los cambios recientes del notebook: nombres reales de clases, graficas guardadas con nombres separados, seleccion automatica del mejor modelo, matriz de confusion normalizada y analysis de errores con texto original.

## Resumen Del Experimento

Se trabajo con el dataset AG News. Cada noticia tiene un titulo, una descripcion y una etiqueta tematica.

| Etiqueta | Clase |
|---:|---|
| 1 | World |
| 2 | Sports |
| 3 | Business |
| 4 | Sci/Tech |

El conjunto de entrenamiento contiene 120000 noticias y el conjunto de prueba contiene 7600. La distribucion esta balanceada: 30000 ejemplos por clase en entrenamiento y 1900 por clase en prueba. Esto ayuda bastante. Cuando las clases estan equilibradas, la accuracy no queda inflada por una categoria dominante.

El mejor modelo en el conjunto de prueba fue `LinearSVC`, con accuracy de 0.9183 y F1 ponderado de 0.9182. La validacion cruzada deja un matiz: `Logistic Regression` tiene el mejor F1 promedio interno. Yo no ignoraria ese dato. Para la entrega, `LinearSVC` se puede defender como modelo final porque gana en test, pero `Logistic Regression` queda como alternativa muy competitiva.

## 1. Configuracion Inicial

El notebook comienza importando librerias de manejo de rutas, texto, datos, graficas, aprendizaje automatico y PLN.

```python
from pathlib import Path
import re
```

`Path` permite construir rutas sin depender de escribir separadores manualmente. `re` se usa despues para limpiar texto con expresiones regulares.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

`pandas` es la herramienta central para leer y transformar los CSV. `matplotlib` y `seaborn` se usan para graficas. `numpy` aparece como apoyo numerico, aunque en este notebook no tiene tanto protagonismo directo.

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
```

Aqui se cargan las piezas de scikit-learn:

| Elemento | Uso en el notebook |
|---|---|
| `cross_val_score` | Ejecuta validacion cruzada para medir consistencia. |
| `TfidfVectorizer` | Convierte texto en variables numericas. |
| `Pipeline` | Une vectorizacion y modelo dentro de la validacion cruzada. |
| `accuracy_score` | Calcula proporcion de aciertos. |
| `precision_recall_fscore_support` | Calcula precision, recall y F1 ponderado. |
| `classification_report` | Muestra metricas por clase con nombres legibles. |
| `confusion_matrix` | Cuenta aciertos y confusiones entre clases. |
| `ConfusionMatrixDisplay` | Grafica la matriz de confusion. |
| `MultinomialNB` | Modelo base comun en texto. |
| `LogisticRegression` | Modelo lineal robusto para TF-IDF. |
| `LinearSVC` | SVM lineal, muy usado en texto de alta dimension. |

```python
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
```

NLTK se usa para stopwords, tokenizacion y lematizacion. Esta parte depende de recursos descargados localmente. Por eso se agrego `punkt_tab` en la celda de recursos.

```python
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)
```

Estas lineas fijan un estilo visual consistente. No cambian el modelo, pero ayudan a que las graficas sean legibles.

```python
BASE_DIR = Path.cwd()
FIGURES_DIR = BASE_DIR / "figuras"
FIGURES_DIR.mkdir(exist_ok=True)

TRAIN_PATH = BASE_DIR / "ag-news-classificacion/train.csv"
TEST_PATH = BASE_DIR / "ag-news-classificacion/test.csv"
```

La carpeta actual se toma como base del proyecto. Luego se definen las rutas del dataset y la carpeta donde se guardan figuras. `mkdir(exist_ok=True)` evita un error si la carpeta `figuras` todavia no existe.

## 2. Recursos De NLTK

```python
# nltk.download("stopwords")
# nltk.download("punkt")
# nltk.download("punkt_tab")
# nltk.download("wordnet")
# nltk.download("omw-1.4")
```

La celda quedo comentada para no descargar nada cada vez que se ejecuta el notebook. Aun asi, documenta que recursos hacen falta.

El cambio importante aqui fue agregar `punkt_tab`. Sin ese recurso, `word_tokenize` puede fallar en versiones recientes de NLTK con un `LookupError`.

Commando recomendado si se quiere preparar el entorno:

```powershell
.\.venv\Scripts\python.exe -m nltk.downloader stopwords punkt punkt_tab wordnet omw-1.4
```

## 3. Carga Del Dataset

```python
train_df = pd.read_csv(TRAIN_PATH)
test_df = pd.read_csv(TEST_PATH)

# train_df.head()
test_df.head()
```

Se leen los archivos `train.csv` y `test.csv`. El dataset ya viene separado, asi que no hace falta crear una particion manual con `train_test_split`.

La muestra inicial confirma que hay tres columnas:

| Columna | Significado |
|---|---|
| `Class Index` | Etiqueta numerica de la categoria. |
| `Title` | Titulo de la noticia. |
| `Description` | Resumen o descripcion. |

## 4. Exploracion Inicial

```python
print("Train shape:", train_df.shape)
print("Test shape:", test_df.shape)
print("\nColumnas train:", train_df.columns.tolist())
print("\nInfo train:")
train_df.info()
print("\nColumnas test:", test_df.columns.tolist())
print("\nInfo test:")
test_df.info()
```

Esta celda revisa tamano, columnas y tipos de datos.

| Conjunto | Filas | Columnas | Columnas |
|---|---:|---:|---|
| Entrenamiento | 120000 | 3 | `Class Index`, `Title`, `Description` |
| Prueba | 7600 | 3 | `Class Index`, `Title`, `Description` |

No hay tipos raros: la etiqueta es numerica y las otras columnas son texto.

```python
print("\n nulls Train_df:")
print("\n",train_df.isnull().sum())
print("\n nulls test_df:")
test_df.isnull().sum()
```

El resultado indica que no hay nulos en las tres columnas principales.

| Conjunto | `Class Index` | `Title` | `Description` |
|---|---:|---:|---:|
| Entrenamiento | 0 | 0 | 0 |
| Prueba | 0 | 0 | 0 |

Esto reduce problemas posteriores. Aunque no haya nulos, el codigo usa `fillna("")` al combinar textos, lo cual deja el pipeline mas resistente.

## 5. Preparacion De Texto Y Etiquetas

```python
TEXT_COL_1 = "Title"
TEXT_COL_2 = "Description"
LABEL_COL = "Class Index"
```

Se guardan los nombres de columnas en variables. Es un detalle pequeno, pero mejora la mantenibilidad.

```python
CLASS_NAMES = {
    1: "World",
    2: "Sports",
    3: "Business",
    4: "Sci/Tech"
}
CLASS_ORDER = [CLASS_NAMES[label] for label in sorted(CLASS_NAMES)]
```

Este fue uno de los cambios importantes. Antes el notebook trabajaba solo con etiquetas 1, 2, 3 y 4. Eso era correcto para entrenar, pero pobre para explicar resultados. Con `CLASS_NAMES`, las tablas y graficas ya pueden mostrar nombres reales.

`CLASS_ORDER` asegura que las graficas respeten el mismo orden: World, Sports, Business y Sci/Tech.

```python
train_df["text"] = train_df[TEXT_COL_1].fillna("") + " " + train_df[TEXT_COL_2].fillna("")
test_df["text"] = test_df[TEXT_COL_1].fillna("") + " " + test_df[TEXT_COL_2].fillna("")
```

Se une titulo y descripcion. Tiene sentido: el titulo suele concentrar el tema principal, y la descripcion aporta contexto. Usar ambos campos da mas information al modelo.

```python
train_df["label"] = train_df[LABEL_COL]
test_df["label"] = test_df[LABEL_COL]
train_df["label_name"] = train_df["label"].map(CLASS_NAMES)
test_df["label_name"] = test_df["label"].map(CLASS_NAMES)
```

`label` conserva la etiqueta numerica para entrenamiento. `label_name` agrega el nombre legible para analysis, graficas y reportes.

```python
train_df[["label", "label_name", "text"]].head()
test_df[["label", "label_name", "text"]].head()
```

Estas salidas validan que el mapeo quedo bien. Por ejemplo, la etiqueta 3 aparece como `Business` y la etiqueta 4 como `Sci/Tech`.

## 6. Distribucion De Clases

```python
train_df["label"].value_counts().sort_index()
test_df["label"].value_counts().sort_index()
```

Los conteos son:

| Clase | Entrenamiento | Prueba |
|---|---:|---:|
| World | 30000 | 1900 |
| Sports | 30000 | 1900 |
| Business | 30000 | 1900 |
| Sci/Tech | 30000 | 1900 |

El balance es perfecto. No hizo falta aplicar pesos de clase ni tecnicas de remuestreo.

### Imagen 1: Distribucion En Entrenamiento

![Distribucion de noticias por clase en entrenamiento](markdown-export/output_15_0.png)

La grafica muestra 30000 noticias por categoria. El cambio reciente se nota en el eje X: ahora aparecen nombres reales de clase, no numeros. Esto hace que el resultado sea mas facil de leer en el informe.

El codigo actualizado guarda la figura con nombre propio:

```python
plt.figure(figsize=(8, 5))
sns.countplot(data=train_df, x="label_name", order=CLASS_ORDER)
plt.title("Distribución de noticias por clase - entrenamiento")
plt.xlabel("clase")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "distribucion_clases_train.png", dpi=300)
plt.show()
```

### Imagen 2: Distribucion En Prueba

![Distribucion de noticias por clase en prueba](distribucion_clases_test.png)

![[]]

La prueba tambien esta balanceada: 1900 noticias por clase. Esto importa porque las metricas finales comparan a los modelos en un conjunto justo.

El codigo tambien guarda esta figura con un nombre distinto:

```python
plt.figure(figsize=(8, 5))
sns.countplot(data=test_df, x="label_name", order=CLASS_ORDER)
plt.title("Distribución de noticias por clase - prueba")
plt.xlabel("clase")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "distribucion_clases_test.png", dpi=300)
plt.show()
```

Antes ambas graficas se guardaban como `distribucion_clases.png`. Eso podia sobrescribir una imagen. Ya quedo corregido.

## 7. Longitud De Los Textos

```python
train_df["text_length"] = train_df["text"].str.len()
train_df["text_length"].describe()
```

| Estadistico | Entrenamiento |
|---|---:|
| count | 120000 |
| mean | 236.46 |
| std | 66.53 |
| min | 17 |
| 25% | 196 |
| 50% | 232 |
| 75% | 266 |
| max | 1012 |

```python
test_df["text_length"] = test_df["text"].str.len()
test_df["text_length"].describe()
```

| Estadistico | Prueba |
|---|---:|
| count | 7600 |
| mean | 235.29 |
| std | 65.30 |
| min | 100 |
| 25% | 196.75 |
| 50% | 231 |
| 75% | 266 |
| max | 892 |

Las medias son muy parecidas. Eso sugiere que entrenamiento y prueba tienen una estructura textual compatible.

## 8. Limpieza Y Normalizacion Del Texto

```python
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
```

Se cargan stopwords en ingles y se prepara el lematizador de WordNet.

```python
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in stop_words and len(token) > 2]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)
```

Lectura linea por linea:

| Linea | Function |
|---|---|
| `str(text).lower()` | Convierte todo a minusculas. |
| `re.sub(r"[^a-zA-Z\s]", " ", text)` | Quita puntuacion, numeros y simbolos. |
| `word_tokenize(text)` | Divide el texto en palabras. |
| Filtro de stopwords | Elimina palabras muy frecuentes y poco informativas. |
| `len(token) > 2` | Quita tokens demasiado cortos. |
| `lemmatizer.lemmatize(token)` | Reduce palabras a una forma base. |
| `" ".join(tokens)` | Devuelve el texto limpio como cadena. |

```python
train_df["clean_text"] = train_df["text"].apply(clean_text)
test_df["clean_text"] = test_df["text"].apply(clean_text)
```

La misma function se aplica a entrenamiento y prueba. Eso es correcto: no se debe limpiar cada conjunto con reglas distintas.

Un detalle para discutir en el informe: al quitar numeros se pierden senales como anos, porcentajes, versiones de productos o cifras economicas. Para una practica esta decision es acceptable, pero en un sistema mas fino convendria probar una limpieza menos agresiva.

## 9. Definicion De Entrenamiento Y Prueba

```python
X_train = train_df["clean_text"]
y_train = train_df["label"]
X_test = test_df["clean_text"]
y_test = test_df["label"]

len(X_train), len(X_test)
```

| Variable | Contenido |
|---|---|
| `X_train` | Texto limpio de entrenamiento. |
| `y_train` | Etiquetas numericas de entrenamiento. |
| `X_test` | Texto limpio de prueba. |
| `y_test` | Etiquetas numericas de prueba. |

El resultado confirma 120000 registros de entrenamiento y 7600 de prueba.

## 10. Vectorizacion Con TF-IDF

```python
tfidf = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1, 2),
    min_df=3,
    max_df=0.95
)
```

| Parametro | Lectura |
|---|---|
| `max_features=20000` | Limita el vocabulario a 20000 terminos. |
| `ngram_range=(1, 2)` | Usa palabras individuales y pares de palabras. |
| `min_df=3` | Ignore terminos que aparecen en menos de 3 documentos. |
| `max_df=0.95` | Ignore terminos demasiado frecuentes. |

```python
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)
```

`fit_transform` se aplica solo sobre entrenamiento. Luego `transform` aplica el vocabulario aprendido al conjunto de prueba. Esto evita fuga de information.

Resultado:

| Matriz | Forma |
|---|---|
| `X_train_tfidf` | `(120000, 20000)` |
| `X_test_tfidf` | `(7600, 20000)` |

## 11. Entrenamiento De Modelos

Se entrenaron tres modelos:

```python
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
nb_pred = nb_model.predict(X_test_tfidf)
```

Naive Bayes sirve como modelo base. Es rapido y suele funcionar razonablemente bien en texto.

```python
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_tfidf, y_train)
lr_pred = lr_model.predict(X_test_tfidf)
```

Regression logistica es un modelo lineal fuerte con TF-IDF. `max_iter=1000` reduce el riesgo de que el entrenamiento se quede corto.

```python
svm_model = LinearSVC()
svm_model.fit(X_train_tfidf, y_train)
svm_pred = svm_model.predict(X_test_tfidf)
```

`LinearSVC` es adecuado para texto porque trabaja bien con muchas variables dispersas.

## 12. Metricas Generales

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

La function calcula accuracy, precision, recall y F1 ponderado. Como las clases estan balanceadas, estas metricas son faciles de comparar.

| Modelo | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Naive Bayes | 0.900263 | 0.899927 | 0.900263 | 0.899832 |
| Logistic Regression | 0.913684 | 0.913537 | 0.913684 | 0.913513 |
| LinearSVC | 0.918289 | 0.918251 | 0.918289 | 0.918199 |

`LinearSVC` gana en el conjunto de prueba. La diferencia frente a `Logistic Regression` no es enorme, pero si consistente.

## 13. Seleccion Automatica Del Mejor Modelo

Antes el notebook fijaba manualmente:

```python
best_model_name = "LinearSVC"
best_pred = svm_pred
```

Ahora usa:

```python
predictions = {
    "Naive Bayes": nb_pred,
    "Logistic Regression": lr_pred,
    "LinearSVC": svm_pred,
}

best_model_name = results_df.sort_values("f1_score", ascending=False).iloc[0]["modelo"]
best_pred = predictions[best_model_name]
labels = sorted(CLASS_NAMES)
target_names = [CLASS_NAMES[label] for label in labels]
```

Esto mejora el flujo porque el notebook ya no depende de una decision escrita a mano. Si otro modelo gana en otra corrida, el reporte y la matriz se actualizan con ese modelo.

```python
print(best_model_name)
print(classification_report(y_test, best_pred, labels=labels, target_names=target_names))
```

Reporte del mejor modelo:

| Clase | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| World | 0.93 | 0.91 | 0.92 | 1900 |
| Sports | 0.96 | 0.98 | 0.97 | 1900 |
| Business | 0.88 | 0.89 | 0.88 | 1900 |
| Sci/Tech | 0.90 | 0.90 | 0.90 | 1900 |
| Accuracy |  |  | 0.92 | 7600 |
| Macro avg | 0.92 | 0.92 | 0.92 | 7600 |
| Weighted avg | 0.92 | 0.92 | 0.92 | 7600 |

Sports es la clase mas fuerte. Business es la mas dificil. Esto se ve tambien en la matriz de confusion.

## 14. Matriz De Confusion

```python
labels = sorted(CLASS_NAMES)
class_names = [CLASS_NAMES[label] for label in labels]

cm = confusion_matrix(y_test, best_pred, labels=labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap="Blues", values_format="d")
plt.title(f"Matriz de confusión - {best_model_name}")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(FIGURES_DIR / f"matriz_confusion_{best_model_name.lower()}.png", dpi=300)
plt.show()
```

El cambio importante es `display_labels=class_names`. La matriz ya no muestra 0, 1, 2, 3; ahora muestra nombres reales de clase.

### Imagen 3: Matriz De Confusion Con Conteos

![Matriz de confusion de LinearSVC](markdown-export/output_35_0.png)

Tabla equivalente:

| Clase real | World | Sports | Business | Sci/Tech | Aciertos |
|---|---:|---:|---:|---:|---:|
| World | 1726 | 53 | 79 | 42 | 1726 |
| Sports | 17 | 1861 | 12 | 10 | 1861 |
| Business | 56 | 13 | 1684 | 147 | 1684 |
| Sci/Tech | 48 | 11 | 133 | 1708 | 1708 |

| Dato | Valor |
|---|---:|
| Total de noticias de prueba | 7600 |
| Aciertos | 6979 |
| Errores | 621 |
| Accuracy | 0.9183 |

La mayor confusion aparece entre `Business` y `Sci/Tech`:

| Confusion | Casos |
|---|---:|
| Business predicha como Sci/Tech | 147 |
| Sci/Tech predicha como Business | 133 |

Tiene sentido. Muchas noticias tecnologicas hablan de empresas, ventas, IPOs, acciones, adquisiciones o resultados financieros. Para un modelo basado en palabras, esa frontera es borrosa.

## 15. Matriz De Confusion Normalizada

```python
cm_norm = confusion_matrix(y_test, best_pred, labels=labels, normalize="true")
disp_norm = ConfusionMatrixDisplay(confusion_matrix=cm_norm, display_labels=class_names)
disp_norm.plot(cmap="Blues", values_format=".2f")
plt.title(f"Matriz de confusión normalizada - {best_model_name}")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(FIGURES_DIR / f"matriz_confusion_{best_model_name.lower()}_normalizada.png", dpi=300)
plt.show()
```

La matriz normalizada muestra proporciones por clase real. En lugar de preguntar "cuantos casos fueron mal clasificados", pregunta "que porcentaje de cada clase fue clasificado correctamente".

### Imagen 4: Matriz De Confusion Normalizada

![Matriz de confusion normalizada de LinearSVC](markdown-export/output_35_1.png)

Lectura rapida:

| Clase | Recall aproximado |
|---|---:|
| World | 0.91 |
| Sports | 0.98 |
| Business | 0.89 |
| Sci/Tech | 0.90 |

La normalizada hace mas visible que Sports es la clase mas facil. Business y Sci/Tech quedan cerca, pero con mas confusion entre ellas.

## 16. Validacion Cruzada

```python
nb_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=20000, ngram_range=(1, 2), min_df=3, max_df=0.95)),
    ("model", MultinomialNB())
])
```

Se construye un pipeline para Naive Bayes. El vectorizador queda dentro del pipeline, lo cual evita fuga de information durante validacion cruzada.

```python
lr_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=20000, ngram_range=(1, 2), min_df=3, max_df=0.95)),
    ("model", LogisticRegression(max_iter=1000))
])

svm_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=20000, ngram_range=(1, 2), min_df=3, max_df=0.95)),
    ("model", LinearSVC())
])
```

Se repite el mismo esquema para regression logistica y SVM lineal.

```python
cv_nb = cross_val_score(nb_pipeline, X_train, y_train, cv=5, scoring="f1_weighted")
cv_lr = cross_val_score(lr_pipeline, X_train, y_train, cv=5, scoring="f1_weighted")
cv_svm = cross_val_score(svm_pipeline, X_train, y_train, cv=5, scoring="f1_weighted")
```

Resultados:

| Modelo | CV F1 promedio | CV std |
|---|---:|---:|
| Naive Bayes | 0.897162 | 0.008342 |
| Logistic Regression | 0.903738 | 0.007320 |
| LinearSVC | 0.897629 | 0.008769 |

La validacion cruzada favorece a `Logistic Regression`. Este resultado no invalida la seleccion de `LinearSVC`, pero si obliga a escribir una conclusion mas honesta: `LinearSVC` gana en test; `Logistic Regression` luce mas estable en validacion cruzada.

## 17. Analysis De Errores

Antes se guardaba solo el texto limpio. Ahora el notebook conserva texto original, texto limpio, etiqueta real y etiqueta predicha con nombres.

```python
errors_df = pd.DataFrame({
    "texto_original": test_df["text"].values,
    "texto_limpio": X_test.values,
    "real": y_test.values,
    "real_nombre": y_test.map(CLASS_NAMES).values,
    "predicho": best_pred,
    "predicho_nombre": pd.Series(best_pred).map(CLASS_NAMES).values
})

errors_df = errors_df[errors_df["real"] != errors_df["predicho"]]
errors_df.head(20)
```

Este cambio mejora mucho la interpretacion. El texto limpio sirve para ver que recibio el modelo, pero el texto original permite entender la noticia como lector.

Ejemplos representativos:

| Texto original resumido | Real | Predicho | Lectura |
|---|---|---|---|
| `Storage, servers bruise HP earnings…` | Sci/Tech | Business | Tecnologia descrita con vocabulario financiero. |
| `Some People Not Eligible to Get in on Google IPO…` | Sci/Tech | Business | Google puede apuntar a tecnologia, pero IPO apunta a negocios. |
| `Venezuela Prepares for Chavez Recall Vote… oil market` | World | Business | Politica internacional mezclada con petroleo y mercado. |
| `Intel to delay product aimed for high-definition TV…` | Business | Sci/Tech | Empresa y producto tecnologico se mezclan. |
| `Olympic history for India, UAE…` | Sports | World | Deporte con paises y contexto internacional. |

El patron mas claro no es un fallo absurdo del modelo. Es una zona gris del dataset: algunas noticias se pueden leer como tecnologia y negocios al mismo tiempo.

## 18. Comparacion Final

```python
final_comparison = results_df.merge(cv_results, on="modelo", how="left")
final_comparison
```

Tabla final:

| Modelo | Accuracy | Precision | Recall | F1-score | CV F1 promedio | CV std |
|---|---:|---:|---:|---:|---:|---:|
| Naive Bayes | 0.900263 | 0.899927 | 0.900263 | 0.899832 | 0.897162 | 0.008342 |
| Logistic Regression | 0.913684 | 0.913537 | 0.913684 | 0.913513 | 0.903738 | 0.007320 |
| LinearSVC | 0.918289 | 0.918251 | 0.918289 | 0.918199 | 0.897629 | 0.008769 |

Seleccion propuesta:

`LinearSVC` queda como modelo final porque obtiene el mejor rendimiento en prueba. Su ventaja sobre regression logistica es pequena, pero aparece en accuracy, precision, recall y F1 del test.

La salvedad es importante: si se prioriza estabilidad por validacion cruzada, `Logistic Regression` tiene un argumento fuerte. Para este trabajo, yo reportaria ambos datos y elegiria `LinearSVC` por rendimiento final.

## Relacion Con la Rubrica

| Criterio | Evidencia |
|---|---|
| Preprocesamiento y representacion | Limpieza, stopwords, lematizacion y TF-IDF con unigramas/bigramas. |
| Varios modelos supervisados | Naive Bayes, Logistic Regression y LinearSVC. |
| Analysis critico de metricas | Metricas generales, reporte por clase, validacion cruzada y matrices de confusion. |
| Claridad visual | Graficas con nombres de clase y matrices con etiquetas legibles. |
| Reproducibilidad | Rutas centralizadas, carpeta de figuras, exportacion de metricas y errores. |

## Mejoras Ya Implementadas

| Mejora | Estado | Impacto |
|---|---|---|
| Mostrar nombres reales de clases | Implementada | El reporte ya dice World, Sports, Business y Sci/Tech. |
| Elegir mejor modelo automaticamente | Implementada | El notebook usa el mayor `f1_score`. |
| Guardar figuras con nombres separados | Implementada | Evita sobrescribir distribucion train/test. |
| Agregar matriz normalizada | Implementada | Facilita comparar recall por clase. |
| Mantener texto original en errores | Implementada | El analysis de errores es mas claro. |

## Mejoras Futuras

Estas no son necesarias para que la entrega cumpla, pero harian el trabajo mas fuerte:

| Mejora | Motivo |
|---|---|
| Probar limpieza conservando numeros | En noticias de negocios y tecnologia, numeros y versiones pueden importar. |
| Revisar hiperparametros | `C` en Logistic Regression y LinearSVC podria mejorar resultados. |
| Usar matriz normalizada en porcentaje real | Visualmente seria mas claro mostrar 91%, 98%, etc. |
| Guardar tambien el modelo final | Permitiria reutilizarlo sin volver a entrenar. |
| Revisar errores por pares de clase | Ayudaria a estudiar mejor Business vs Sci/Tech. |

## Conclusion Para El Informe

El experimento cumple el objetivo de clasificar noticias con tecnicas de PLN. El dataset esta balanceado, no presenta nulos y tiene una estructura consistente entre entrenamiento y prueba.

El pipeline combina titulo y descripcion, limpia el texto, elimina stopwords, aplica lematizacion y representa los documentos con TF-IDF. Con esa representacion se entrenaron Naive Bayes, Logistic Regression y LinearSVC.

`LinearSVC` fue el mejor modelo en el conjunto de prueba, con accuracy de 0.9183 y F1 ponderado de 0.9182. La clase Sports fue la mas sencilla de clasificar. La mayor confusion estuvo entre Business y Sci/Tech, algo razonable porque ambas categorias comparten mucho vocabulario sobre empresas, productos, mercado y tecnologia.

La validacion cruzada muestra que `Logistic Regression` tiene el mejor F1 promedio interno. Por eso, la conclusion no debe vendor a `LinearSVC` como una victoria absoluta. Es el mejor en test, pero regression logistica queda como una alternativa cercana y estable.
