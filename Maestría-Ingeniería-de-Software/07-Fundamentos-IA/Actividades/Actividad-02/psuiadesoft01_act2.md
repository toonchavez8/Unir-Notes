Actividad 2. Clasificación de noticias mediante procesamiento de lenguaje natural

Objetivos

Desarrollar un modelo de aprendizaje supervisado capaz de clasificar artículos de prensa en diferentes categorías temáticas utilizando técnicas de Procesamiento de Lenguaje Natural (PLN).

Pautas de elaboración

Conjunto de datos: este _dataset_ contiene más de 120 000 artículos de noticias, cada uno etiquetado en una de las cuatro categorías: _World_, _Sports_, _Business_ y _Science/Technology_. AG News Dataset (Kaggle) [https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset)

1. **Análisis exploratorio del conjunto de datos**
    - Carga y visualización de una muestra del _dataset_.
    - Estadísticas de distribución por clase.
    - Detección de posibles problemas de balanceo.
2. **Preprocesamiento del texto**
    - Normalización (minúsculas, eliminación de caracteres especiales y _stopwords_).
    - Tokenización y lematización.
    - Representación vectorial del texto (TF-IDF, _embeddings_ preentrenados como Word2Vec o GloVe).
3. **Entrenamiento de modelos supervisados**
    - Entrenar al menos **tres modelos diferentes** (por ejemplo: _Naive Bayes_, _Logistic Regression_, _SVM_, _Random Forest_).
    - Utilizar validación cruzada para evaluar consistencia de resultados.
4. **Evaluación del rendimiento**
    - Calcular _Accuracy_, _Precision_, _Recall_, _F1-score_ y matriz de confusión.
    - Analizar los errores más frecuentes (ejemplos mal clasificados).
    - Opcional: generación de curvas ROC para cada clase (One-vs-Rest).
5. **Justificación y selección del modelo final**
    - Elegir el modelo más adecuado según los resultados y la interpretabilidad.
    - Proponer posibles mejoras futuras.
6. **Informe final**
    - Incluir gráficos, visualizaciones de métricas y conclusiones técnicas.

Extensión y formato

**Informe final**: en PDF, con redacción técnica y visualizaciones.

**Código fuente**: Jupyter Notebook (.ipynb) estructurado y comentado.

**Archivo comprimido (.zip)** con:

- informe.pdf
- clasificacion_noticias_pln.ipynb
- Carpeta _figuras_ con gráficos exportados
- requirements.txt con las dependencias necesarias para su instalación y uso en Python.

Rúbrica

|   |   |   |   |
|---|---|---|---|
|Clasificación de noticias mediante procesamiento de lenguaje natural|Descripción|Puntuación máxima<br><br>(puntos)|Peso<br><br>%|
|Criterio 1|Adecuado preprocesamiento y representación del texto|2|20%|
|Criterio 2|Implementación rigurosa de varios modelos supervisados|2,5|25%|
|Criterio 3|Análisis crítico de métricas y justificación de resultados|2,5|25%|
|Criterio 4|Claridad, redacción y apoyo visual en el informe|2|20%|
|Criterio 5|Código comentado, limpio y reproducible|1|10%|
|||**10**|**100 %**|