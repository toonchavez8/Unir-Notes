Actividad 1. Segmentación de clientes mediante Aprendizaje No Supervisado

Objetivos

Aplicar técnicas de aprendizaje no supervisado para segmentar clientes en función de sus características demográficas y de consumo, con el fin de identificar patrones ocultos y grupos homogéneos que puedan orientar decisiones de marketing y estrategias comerciales.

Pautas de elaboración

Conjunto de datos: este _dataset_ contiene 200 registros de clientes con variables como edad, ingresos anuales y puntuación de gasto. Mall Customers Dataset (Kaggle): [https://www.kaggle.com/datasets/shwetabh123/mall-customers](https://www.kaggle.com/datasets/shwetabh123/mall-customers)

1. **Análisis exploratorio del conjunto de datos**
    - Carga del _dataset_.
    - Análisis descriptivo de las variables.
    - Identificación de posibles valores atípicos.
2. **Preprocesamiento**
    - Limpieza de datos.
    - Escalado de variables numéricas.
    - Selección de variables relevantes para el _clustering_.
3. **Aplicación de técnicas de _clustering_**
    - Entrena al menos **dos métodos distintos** (por ejemplo: _K-Means_, _DBSCAN_, _Agglomerative Clustering_).
    - Determina el número óptimo de clusters usando métodos como _Elbow Method_ o _Silhouette Score_.
4. **Visualización y análisis de los resultados**
    - Representación gráfica de los _clusters_ (2D/3D).
    - Interpretación de las características principales de cada grupo.
    - Comparación de los resultados obtenidos con cada método.
5. **Conclusiones y posibles aplicaciones**
    - Discute cómo podrían emplearse los resultados en un contexto real (segmentación de mercado, campañas personalizadas, etc.).
    - Identifica limitaciones y posibles mejoras.

Extensión y formato

**Informe final**: en formato PDF, con gráficos, interpretación de _clusters_ y discusión de resultados.

**Código fuente**: Jupyter Notebook (.ipynb) estructurado y comentado.

**Archivo comprimido (.zip)** con:

- informe.pdf
- segmentacion_clientes.ipynb
- Carpeta _figuras_ con gráficos exportados
- requirements.txt con las dependencias necesarias para instalación y uso en Python.

Rúbrica

|   |   |   |   |
|---|---|---|---|
|Segmentación de clientes mediante Aprendizaje No Supervisado|Descripción|Puntuación máxima<br><br>(puntos)|Peso<br><br>%|
|Criterio 1|Adecuado preprocesamiento y preparación de los datos|2|20%|
|Criterio 2|Correcta implementación y comparación de algoritmos de _clustering_|2.5|25%|
|Criterio 3|Análisis crítico de los resultados y conclusiones|2.5|25%|
|Criterio 4|Claridad, redacción y calidad visual del informe|2|20%|
|Criterio 5|Código reproducible, organizado y comentado|1|10%|
|||**10**|**100 %**|