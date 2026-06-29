# Clasificacion De Noticias Mediante Procesamiento De Lenguaje Natural

Nombre del estudiante:  
Matricula:  
Asignatura: Fundamentos de inteligencia artificial  
Institucion:  
Docente:  
Fecha:  

## 1. Introduccion

La clasificacion automatica de texto consiste en asignar una etiqueta a un documento a partir de su contenido. En este trabajo, cada documento es una noticia periodistica y la etiqueta corresponde a una categoria tematica. Este tipo de problema es comun en procesamiento de lenguaje natural, area que estudia metodos computacionales para analizar y representar lenguaje humano (Bird et al., 2009).

El problema no se resuelve directamente con texto crudo. Los modelos supervisados necesitan variables numericas. Por eso, el flujo de trabajo transforma cada noticia en una representacion vectorial antes de entrenar los modelos. En este caso se uso TF-IDF, sigla de term frequency-inverse document frequency. TF-IDF asigna peso a una palabra segun su frecuencia en un documento y segun que tan comun o rara es en el conjunto completo de documentos (Manning et al., 2008; Salton & Buckley, 1988).

El objetivo de la actividad fue desarrollar y comparar varios modelos supervisados capaces de clasificar noticias de AG News en cuatro categorias. La comparacion se realizo con metricas de accuracy, precision, recall y F1-score, ademas de validacion cruzada, matriz de confusion y analysis de errores.

## 2. Metodo

### 2.1 Dataset

Se utilizo el dataset AG News Classification, indicado en la actividad como fuente de datos. Este conjunto contiene noticias clasificadas en cuatro categorias: World, Sports, Business y Science/Technology. AG News tambien ha sido usado como referencia en trabajos de clasificacion de texto, por ejemplo en la evaluacion de redes convolucionales a nivel de character de Zhang et al. (2015).

Tabla 1

Categorias del problema

| Etiqueta | Clase usada en el notebook | Descripcion breve |
|---:|---|---|
| 1 | World | Noticias internacionales y politica global. |
| 2 | Sports | Noticias deportivas. |
| 3 | Business | Economia, empresas, mercado y finanzas. |
| 4 | Sci/Tech | Ciencia, tecnologia, productos y desarrollo tecnico. |

El dataset se recibio separado en dos archivos: `train.csv` y `test.csv`. El primero se uso para entrenar los modelos y el segundo para evaluar el rendimiento final.

Tabla 2

Estructura del dataset

| Conjunto | Registros | Columnas originales | Uso |
|---|---:|---|---|
| Entrenamiento | 120000 | `Class Index`, `Title`, `Description` | Ajuste de TF-IDF y entrenamiento de modelos. |
| Prueba | 7600 | `Class Index`, `Title`, `Description` | Evaluacion final del rendimiento. |

No se detectaron valores nulos en las columnas originales. Aun asi, al construir la columna textual se uso `fillna("")` para evitar errores si el dataset cambiara en otra version.

### Construccion Del Texto De Entrada

El texto de entrada se construyo uniendo el titulo y la descripción de cada noticia:

```python
train_df["text"] = train_df[TEXT_COL_1].fillna("") + " " + train_df[TEXT_COL_2].fillna("")
test_df["text"] = test_df[TEXT_COL_1].fillna("") + " " + test_df[TEXT_COL_2].fillna("")
```

Esta decision fue dado a que el titulo suele container la idea central y la descripción agrega contexto. Usar ambos campos aumenta la information disponible para el vectorizador.

Tambien se agrego un mapa de clases para que las tablas y graficas fueran legibles:

```python
CLASS_NAMES = {
    1: "World",
    2: "Sports",
    3: "Business",
    4: "Sci/Tech"
}
CLASS_ORDER = [CLASS_NAMES[label] for label in sorted(CLASS_NAMES)]
```

### Analysis Exploratorio

El primer punto revisado fue el balance de clases. El balance es importante porque un conjunto desbalanceado puede hacer que la accuracy parezca buena aunque el modelo ignore clases minoritarias.

Tabla 3

Distribucion por clase

| Clase | Entrenamiento | Prueba |
|---|---:|---:|
| World | 30000 | 1900 |
| Sports | 30000 | 1900 |
| Business | 30000 | 1900 |
| Sci/Tech | 30000 | 1900 |

Figura 1

Distribucion de noticias por clase en entrenamiento

![Distribucion de noticias por clase en entrenamiento](markdown-export/output_15_0.png)

Nota. La figura muestra que las cuatro clases tienen 30000 ejemplos en entrenamiento.

Figura 2

Distribucion de noticias por clase en prueba

![[distribucion_clases_test.png]]

Nota. La figura muestra 1900 noticias por clase en el conjunto de prueba.

Tambien se reviso la longitud del texto combinado. La longitud media fue casi igual entre entrenamiento y prueba, lo cual sugiere que ambos conjuntos tienen formatos comparables.

Tabla 4

Longitud del texto combinado

| Estadistico | Entrenamiento | Prueba |
|---|---:|---:|
| Media | 236.46 | 235.29 |
| Desviacion estandar | 66.53 | 65.30 |
| Mediana | 232 | 231 |
| Maximo | 1012 | 892 |

### Preprocesamiento Del Texto

El preprocesamiento preparo el texto para convertirlo en variables numericas. Primero se convirtio todo a minusculas. Despues se eliminaron caracteres no alfabeticos, se separo el texto en tokens, se quitaron stopwords y se aplico lematizacion.

Un token es una unidad minima de procesamiento textual, normalmente una palabra o signo separado por el tokenizador. La tokenizacion es necesaria porque muchas tecnicas de PLN operan sobre unidades discretas del texto (Bird et al., 2009). Las stopwords son palabras muy frecuentes, como articulos o preposiciones, que pueden aportar poco al tema de una noticia. La lematizacion reduce una palabra a una forma base, por ejemplo plural a singular o variantes flexionadas a una forma comun.

El codigo usado fue:

```python
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in stop_words and len(token) > 2]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)
```

El resultado de esta function es una version mas compacta del texto. Por ejemplo, una noticia sobre mercados y petroleo queda reducida a terminos como `oil`, `economy`, `stock`, `outlook` y `reuters`. La limpieza ayuda a reducir ruido, aunque tambien tiene una limitacion: al eliminar numeros se pueden perder senales utiles en noticias financieras o tecnologicas, como porcentajes, años, versiones de productos o precios.

### Representacion Vectorial

Los modelos supervisados de scikit-learn no entrenan directamente sobre cadenas de texto. Primero se require convertir cada noticia en un vector numerico. Para esto se uso TF-IDF.

TF-IDF combina dos ideas. La frecuencia de termino mide cuantas veces aparece una palabra en un documento. La frecuencia inversa de documento reduce el peso de palabras que aparecen en demasiados documentos, porque suelen set menos distintivas (Manning et al., 2008). Este enfoque ha sido clasico en recuperacion de information y clasificacion de texto (Salton & Buckley, 1988).

La configuracion fue:

```python
tfidf = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1, 2),
    min_df=3,
    max_df=0.95
)
```

Tabla 5

Parametros de TF-IDF

| Parametro | Valor | Function |
|---|---:|---|
| `max_features` | 20000 | Limita el vocabulario para controlar memoria y ruido. |
| `ngram_range` | `(1, 2)` | Usa palabras individuales y pares de palabras. |
| `min_df` | 3 | Descarta terminos presentes en menos de tres documentos. |
| `max_df` | 0.95 | Descarta terminos presentes en mas del 95% de documentos. |

Un n-grama es una secuencia de n elementos consecutivos. En este caso, unigrama significa una palabra individual y bigrama significa una secuencia de dos palabras. Los bigramas ayudan a capturar expresiones como `stock market` o `world cup`.

Despues de vectorizar, las matrices quedaron asi:

Tabla 6

Dimensions de las matrices TF-IDF

| Matriz | Forma |
|---|---|
| `X_train_tfidf` | `(120000, 20000)` |
| `X_test_tfidf` | `(7600, 20000)` |

### Modelos Supervisados

Se entrenaron tres modelos con la misma representacion TF-IDF:

1. `MultinomialNB`.
2. `LogisticRegression`.
3. `LinearSVC`.

Naive Bayes funciona como una linea base rapida para texto. Regression logistica es un modelo lineal usado con frecuencia cuando las variables son pesos numericos. LinearSVC implementa una maquina de vectors de soporte lineal; las maquinas de vectors de soporte buscan separar clases mediante margenes amplios, idea introducida formalmente por Cortes y Vapnik (1995). La implementacion se realizo con scikit-learn, una biblioteca de aprendizaje automatico documentada por Pedregosa et al. (2011).

La evaluacion incluyo validacion cruzada. En este contexto, validacion cruzada significa dividir el conjunto de entrenamiento en particiones, entrenar varias veces y medir si el rendimiento se mantiene estable. Se uso `Pipeline` para que TF-IDF se ajustara dentro de cada fold y no filtrara information.

## Resultados

### Metricas Globales

Se calcularon accuracy, precision, recall y F1-score. Accuracy mide la proporcion total de aciertos. Precision mide que proporcion de las predicciones positivas de una clase fueron correctas. Recall mide que proporcion de los casos reales de una clase fueron recuperados. F1-score combina precision y recall en una sola medida, util cuando interesa equilibrar ambos tipos de error.

Tabla 7

Metricas en conjunto de prueba

| Modelo | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Naive Bayes | 0.900263 | 0.899927 | 0.900263 | 0.899832 |
| Logistic Regression | 0.913684 | 0.913537 | 0.913684 | 0.913513 |
| LinearSVC | 0.918289 | 0.918251 | 0.918289 | 0.918199 |

LinearSVC fue el mejor modelo en el conjunto de prueba. Su ventaja sobre Logistic Regression fue pequeña, pero aparece que fue la mejor en todas las metricas.

### Reporte Por Clase

El mejor modelo se eligio automaticamente a partir del F1-score:

```python
predictions = {
    "Naive Bayes": nb_pred,
    "Logistic Regression": lr_pred,
    "LinearSVC": svm_pred,
}

best_model_name = results_df.sort_values("f1_score", ascending=False).iloc[0]["modelo"]
best_pred = predictions[best_model_name]
```

Tabla 8

Reporte por clase para LinearSVC

| Clase | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| World | 0.93 | 0.91 | 0.92 | 1900 |
| Sports | 0.96 | 0.98 | 0.97 | 1900 |
| Business | 0.88 | 0.89 | 0.88 | 1900 |
| Sci/Tech | 0.90 | 0.90 | 0.90 | 1900 |

Sports fue la clase con mejor resultado, con recall de 0.98 y F1-score de 0.97. Business fue la clase mas dificil, con F1-score de 0.88.

### Matriz De Confusion

La matriz de confusion muestra como se distribuyen los aciertos y errores entre clases. Cada fila corresponde a la clase real y cada columna a la clase predicha.

Figura 3

Matriz de confusion de LinearSVC

![Matriz de confusion de LinearSVC](markdown-export/output_35_0.png)

Nota. Los valores de la diagonal son aciertos. Los valores fuera de la diagonal son errores.

Tabla 9

Matriz de confusion con conteos

| Clase real | World | Sports | Business | Sci/Tech | Aciertos |
|---|---:|---:|---:|---:|---:|
| World | 1726 | 53 | 79 | 42 | 1726 |
| Sports | 17 | 1861 | 12 | 10 | 1861 |
| Business | 56 | 13 | 1684 | 147 | 1684 |
| Sci/Tech | 48 | 11 | 133 | 1708 | 1708 |

El modelo acerto 6979 de 7600 noticias. La mayor confusion se dio entre Business y Sci/Tech: 147 noticias de Business fueron clasificadas como Sci/Tech, y 133 noticias de Sci/Tech fueron clasificadas como Business.

Figura 4

Matriz de confusion normalizada de LinearSVC

![Matriz de confusion normalizada de LinearSVC](markdown-export/output_35_1.png)

Nota. La matriz normalizada muestra proporciones por clase real. Por eso facilita comparar el recall entre clases.

La matriz normalizada confirma que Sports fue la categoria mas estable. Business y Sci/Tech quedaron cerca, pero concentran la mayor parte de las confusiones relevantes.

### Validacion Cruzada

Tabla 10

Validacion cruzada con F1 ponderado

| Modelo | CV F1 promedio | Desviacion estandar |
|---|---:|---:|
| Naive Bayes | 0.897162 | 0.008342 |
| Logistic Regression | 0.903738 | 0.007320 |
| LinearSVC | 0.897629 | 0.008769 |

Este resultado es importante. LinearSVC fue mejor en el conjunto de prueba, pero Logistic Regression obtuvo el mejor F1 promedio en validacion cruzada. Por eso, la seleccion final no debe presentarse como una victoria absoluta de LinearSVC. La diferencia real es mas matizada.

## Analysis De Errores

El notebook genero una tabla de errores con texto original, texto limpio, clase real y clase predicha. Mantener el texto original fue util porque permite entender mejor la noticia. El texto limpio muestra que recibio el modelo, pero el texto original muestra el contexto.

Tabla 11

Ejemplos de errores de clasificacion

| Caso | Clase real | Clase predicha | Lectura |
|---|---|---|---|
| HP, servidores y ganancias | Sci/Tech | Business | Tecnologia descrita con vocabulario financiero. |
| Google IPO | Sci/Tech | Business | Google apunta a tecnologia, pero IPO apunta a negocios. |
| Chavez, Venezuela y mercado petrolero | World | Business | Politica internacional mezclada con petroleo y mercado. |
| Intel y television de alta definicion | Business | Sci/Tech | Empresa y producto tecnologico en la misma noticia. |
| Juegos olimpicos India/UAE | Sports | World | Deporte con fuerte contexto geografico. |

El patron principal esta en la frontera Business/Sci-Tech. Esto no parece un error trivial del modelo. Varias noticias mezclan empresa, mercado, producto y tecnologia. En esos casos, incluso una lectura humana puede depender del criterio editorial usado por el dataset.

## Seleccion Del Modelo Final

El modelo final seleccionado fue LinearSVC.

La razon principal es su rendimiento en el conjunto de prueba: accuracy de 0.9183 y F1-score ponderado de 0.9182. Tambien mostro una diagonal fuerte en la matriz de confusion y un comportamiento razonable en todas las clases.

Quien seria una segunda opción seria Logistic Regression. En validación cruzada, este modelo obtuvo el mejor F1 promedio. Por eso, Logistic Regression seria una opcion defendible si el criterio principal fuera estabilidad interna. En esta actividad se eligio LinearSVC porque el conjunto de prueba separado funciono como evaluacion final.

## Limitaciones

El trabajo tiene algunas limitaciones. Primero, la limpieza elimina numeros, lo cual puede quitar information util en noticias de negocios y tecnologia. Segundo, TF-IDF representa documentos por pesos de terminos, pero no entiende significado contextual. Dos noticias con palabras parecidas pueden recibir vectors parecidos aunque el sentido editorial sea distinto. Tercero, no se ajustaron hiperparametros de manera exhaustiva. Por ultimo, no se probaron embeddings ni modelos basados en transformers.

Un embedding es una representacion densa de una palabra o documento en un espacio vectorial, donde palabras semanticamente cercanas tienden a quedar cerca entre si (Mikolov et al., 2013). Un transformer es una arquitectura de aprendizaje profundo basada en mecanismos de atencion, disenada para modelar relaciones entre elementos de una secuencia sin depender de recurrencia (Vaswani et al., 2017). Ambas alternativas podrian capturar relaciones semanticas mas complejas que TF-IDF.

## Mejoras Futuras

Para mejorar el flujo, convendria probar una limpieza menos agresiva que conserve numeros, porcentajes y simbolos financieros. Tambien seria util ajustar hiperparametros de Logistic Regression y LinearSVC, sobre todo el parametro `C`. Otra mejora seria comparar TF-IDF con embeddings preentrenados o modelos transformer. Finalmente, se podria guardar el modelo final con `joblib` para reutilizarlo sin volver a entrenar.

## Conclusiones

El flujo implementado cumple con los requisitos de la actividad. Se realizo exploracion del dataset, preprocesamiento textual, representacion vectorial, entrenamiento de tres modelos, validacion cruzada, calculo de metricas, matriz de confusion y analysis de errores.

El dataset esta balanceado, lo que facilita una comparacion justa entre modelos. LinearSVC fue el mejor modelo en el conjunto de prueba, con accuracy de 0.9183 y F1-score ponderado de 0.9182. Sports fue la clase mas facil de clasificar, mientras que Business y Sci/Tech concentraron la mayor confusion.

La lectura final debe set cuidadosa: LinearSVC gana en prueba, pero Logistic Regression muestra mejor F1 promedio en validacion cruzada. En terminos practicos, LinearSVC es una buena seleccion final para esta entrega, siempre que se reconozca que la diferencia con Logistic Regression es reducida.

## Referencias

Anand, A. (s. f.). *AG News classification dataset*. Kaggle. https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset

Bird, S., Klein, E., & Loper, E. (2009). *Natural language processing with Python*. O'Reilly Media. https://www.nltk.org/book/

Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning, 20*, 273-297. https://doi.org/10.1007/BF00994018

Manning, C. D., Raghavan, P., & Schutze, H. (2008). *Introduction to information retrieval*. Cambridge University Press. https://nlp.stanford.edu/IR-book/

Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). *Efficient estimation of word representations in vector space*. arXiv. https://arxiv.org/abs/1301.3781

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825-2830. https://jmlr.org/papers/v12/pedregosa11a.html

Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval. *Information Processing & Management, 24*(5), 513-523. https://doi.org/10.1016/0306-4573(88)90021-0

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*. https://arxiv.org/abs/1706.03762

Zhang, X., Zhao, J., & LeCun, Y. (2015). Character-level convolutional networks for text classification. *Advances in Neural Information Processing Systems, 28*. https://arxiv.org/abs/1509.01626
