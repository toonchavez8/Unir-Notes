# Notas De Analysis - Actividad 2

## Datos Generales

- Actividad: Clasificacion de noticias mediante procesamiento de lenguaje natural.
- Dataset: AG News Classification.
- Fuente indicada en la actividad: Kaggle, AG News Dataset.
- Archivos usados:
  - `ag-news-classificacion/train.csv`
  - `ag-news-classificacion/test.csv`
  - `clasificacion_noticias_pln.ipynb`
  - `metricas_modelos.csv`
  - `ejemplos_errores.csv`
- Clases:

| Etiqueta | Clase |
|---:|---|
| 1 | World |
| 2 | Sports |
| 3 | Business |
| 4 | Sci/Tech |

## Exploracion Inicial

- Registros en entrenamiento: 120000.
- Registros en prueba: 7600.
- Columnas originales: `Class Index`, `Title`, `Description`.
- Valores nulos: no se detectaron nulos en train ni en test.
- Balance de clases:

| Clase | Train | Test |
|---|---:|---:|
| World | 30000 | 1900 |
| Sports | 30000 | 1900 |
| Business | 30000 | 1900 |
| Sci/Tech | 30000 | 1900 |

El dataset esta perfectamente balanceado. Eso hace que accuracy y F1 ponderado sean metricas razonables para comparar modelos.

## Texto De Entrada

- Columna de titulo: `Title`.
- Columna de descripcion: `Description`.
- Estrategia: unir titulo y descripcion en una nueva columna `text`.
- Justificacion: el titulo resume el tema principal; la descripcion agrega contexto. Usarlos juntos da mas senales al vectorizador.

Longitud del texto combinado:

| Estadistico | Train | Test |
|---|---:|---:|
| Media | 236.46 | 235.29 |
| Desviacion estandar | 66.53 | 65.30 |
| Mediana | 232 | 231 |
| Maximo | 1012 | 892 |

Train y test tienen longitudes muy parecidas. No se ve una diferencia fuerte de formato entre ambos conjuntos.

 un mapa de clases:

```python
CLASS_NAMES = {
    1: "World",
    2: "Sports",
    3: "Business",
    4: "Sci/Tech"
}
CLASS_ORDER = [CLASS_NAMES[label] for label in sorted(CLASS_NAMES)]
```

Tambien se crearon columnas legibles:

```python
train_df["label_name"] = train_df["label"].map(CLASS_NAMES)
test_df["label_name"] = test_df["label"].map(CLASS_NAMES)
```

## Preprocesamiento

Pasos aplicados:

- Conversion a minusculas.
- Eliminacion de caracteres que no sean letras o espacios.
- Tokenizacion con `word_tokenize`.
- Eliminacion de stopwords en ingles.
- Eliminacion de tokens con longitud menor o igual a 2.
- Lematizacion con `WordNetLemmatizer`.

Codigo base:

```python
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in stop_words and len(token) > 2]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)
```

Nota importante: para que `word_tokenize` funcione con la version actual de NLTK, hace falta tener `punkt_tab`, ademas de `punkt`.

Commando de referencia:

```powershell
.\.venv\Scripts\python.exe -m nltk.downloader stopwords punkt punkt_tab wordnet omw-1.4
```

## Vectorizacion

Metodo: TF-IDF.

Parametros usados:

```python
TfidfVectorizer(
    max_features=20000,
    ngram_range=(1, 2),
    min_df=3,
    max_df=0.95
)
```

Justificacion:

- `max_features=20000`: limita memoria y ruido.
- `ngram_range=(1, 2)`: captura palabras sueltas y expresiones de dos palabras.
- `min_df=3`: descarta terminos extremadamente raros.
- `max_df=0.95`: descarta terminos demasiado frecuentes.

Dimensions:

| Matriz | Forma |
|---|---|
| `X_train_tfidf` | `(120000, 20000)` |
| `X_test_tfidf` | `(7600, 20000)` |

## Modelos Entrenados

| Modelo              | Motivo de inclusion                             |
| ------------------- | ----------------------------------------------- |
| Naive Bayes         | Linea base rapida y comun para texto.           |
| Logistic Regression | Modelo lineal fuerte con TF-IDF.                |
| LinearSVC           | Buen rendimiento en espacios de alta dimension. |

## Metricas En Conjunto De Prueba

| Modelo | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Naive Bayes | 0.900263 | 0.899927 | 0.900263 | 0.899832 |
| Logistic Regression | 0.913684 | 0.913537 | 0.913684 | 0.913513 |
| LinearSVC | 0.918289 | 0.918251 | 0.918289 | 0.918199 |

Lectura: `LinearSVC` gana en las cuatro metricas sobre el conjunto de prueba. La diferencia contra `Logistic Regression` existe, pero no es grande.

## Reporte Por Clase Del Mejor Modelo

Modelo seleccionado automaticamente por mayor F1 en test: `LinearSVC`.

| Clase | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| World | 0.93 | 0.91 | 0.92 | 1900 |
| Sports | 0.96 | 0.98 | 0.97 | 1900 |
| Business | 0.88 | 0.89 | 0.88 | 1900 |
| Sci/Tech | 0.90 | 0.90 | 0.90 | 1900 |

Sports fue la clase mas facil. Business fue la mas dificil.

## Validacion Cruzada

| Modelo | CV F1 promedio | CV std |
|---|---:|---:|
| Naive Bayes | 0.897162 | 0.008342 |
| Logistic Regression | 0.903738 | 0.007320 |
| LinearSVC | 0.897629 | 0.008769 |

Lectura: aunque `LinearSVC` gana en test, `Logistic Regression` obtiene mejor F1 promedio en validacion cruzada. Esto debe mencionarse en el informe para que la seleccion del modelo final no parezca simplista.

## Matriz De Confusion

Conteos principales para `LinearSVC`:

| Clase real | World | Sports | Business | Sci/Tech | Aciertos |
|---|---:|---:|---:|---:|---:|
| World | 1726 | 53 | 79 | 42 | 1726 |
| Sports | 17 | 1861 | 12 | 10 | 1861 |
| Business | 56 | 13 | 1684 | 147 | 1684 |
| Sci/Tech | 48 | 11 | 133 | 1708 | 1708 |

Resumen:

- Aciertos: 6979 de 7600.
- Errores: 621.
- Mayor confusion: Business contra Sci/Tech.
- Business -> Sci/Tech: 147 casos.
- Sci/Tech -> Business: 133 casos.

La matriz normalizada confirma que Sports tiene el mejor recall aproximado, 0.98. Business queda alrededor de 0.89 y Sci/Tech alrededor de 0.90.

## Errores De Clasificacion

El analysis de errores contiene:

- `texto_original`
- `texto_limpio`
- `real`
- `real_nombre`
- `predicho`
- `predicho_nombre`

Ejemplos revisados:

| Caso | Real | Predicho | Lectura |
|---|---|---|---|
| HP, servidores y earnings | Sci/Tech | Business | Tecnologia con vocabulario financiero. |
| Google IPO | Sci/Tech | Business | Producto/empresa tecnologica mezclada con bolsa. |
| Chavez, Venezuela y mercado petrolero | World | Business | Politica internacional con vocabulario economico. |
| Intel y television HD | Business | Sci/Tech | Empresa y producto tecnologico en la misma noticia. |
| Juegos olimpicos India/UAE | Sports | World | Deporte con fuerte contexto geografico. |

Patron principal: las clases Business y Sci/Tech comparten mucho vocabulario. Algunas noticias son ambiguas incluso para una persona.

## Seleccion Del Modelo Final

Modelo elegido: `LinearSVC`.

Justificacion:

- Mejor accuracy en test: 0.918289.
- Mejor F1 ponderado en test: 0.918199.
- Matriz de confusion con diagonal fuerte.
- Buen comportamiento general en las cuatro clases.

Matiz:

`Logistic Regression` tuvo mejor validacion cruzada. Si el criterio principal fuera estabilidad interna, seria una opcion muy defendible. En esta entrega se elige `LinearSVC` porque el objetivo final es clasificar correctamente el conjunto de prueba separado.

## Limitaciones

- La limpieza elimina numeros, lo cual puede quitar information util en negocios y tecnologia.
- No se optimizaron hiperparametros.
- No se probaron embeddings ni modelos neuronales.
- La frontera entre Business y Sci/Tech es naturalmente ambigua.
- El analysis depende de texto en ingles; no aplica directamente a otro idioma sin ajustar stopwords y lematizacion.

## Mejoras Futuras

- Probar conservar numeros y simbolos utiles como `%`, `$`, versiones y anos.
- Ajustar hiperparametros de `LinearSVC` y `LogisticRegression`.
- Comparar TF-IDF contra embeddings preentrenados.
- Analizar errores por par de clases, sobre todo Business/Sci-Tech.
- Guardar el modelo final con `joblib`.
- Agregar una tabla final con el nombre de la clase real y predicha en todos los errores.

## Conclusion Breve Para El Informe

El pipeline de PLN clasifica noticias de AG News con buen rendimiento. `LinearSVC` fue el mejor modelo en el conjunto de prueba, con accuracy de 0.9183 y F1 ponderado de 0.9182. La clase Sports fue la mas sencilla de clasificar. La mayor dificultad estuvo entre Business y Sci/Tech, porque ambas comparten vocabulario sobre empresas, tecnologia, mercado y productos.

La validacion cruzada muestra que `Logistic Regression` es una alternativa fuerte y estable. Por eso, la seleccion de `LinearSVC` debe explicarse como una decision basada en el resultado final de test, no como una superioridad absoluta.
