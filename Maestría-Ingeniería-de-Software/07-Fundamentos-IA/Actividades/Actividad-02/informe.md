# Informe - Actividad 2

## Clasificación de noticias mediante procesamiento de lenguaje natural

## Datos del estudiante
- Nombre:
- Matrícula:
- Asignatura:
- Fecha:

---

## 1. Introducción

En esta actividad se desarrolla un sistema de clasificación automática de noticias mediante técnicas de procesamiento de lenguaje natural y aprendizaje supervisado. El objetivo general es construir modelos capaces de asignar una categoría temática a artículos periodísticos a partir de su contenido textual.

La clasificación de texto es un problema central en inteligencia artificial aplicada al lenguaje, ya que permite organizar información, automatizar flujos documentales y mejorar sistemas de recomendación, búsqueda y análisis de contenido. Para ello, en este trabajo se emplea un dataset etiquetado de noticias periodísticas y se sigue un flujo completo que incluye exploración de datos, preprocesamiento del texto, representación vectorial, entrenamiento de modelos, evaluación de métricas y análisis de errores.

---

## 2. Objetivo

Desarrollar y comparar varios modelos supervisados para clasificar noticias en categorías temáticas, aplicando técnicas de preprocesamiento de texto, vectorización y evaluación rigurosa del rendimiento.

---

## 3. Descripción del dataset

### 3.1 Fuente de datos
- Dataset:
- Fuente:
- URL:
- Fecha de descarga:

### 3.2 Estructura del dataset
- Archivos utilizados:
- Número de registros en entrenamiento:
- Número de registros en prueba:
- Número de clases:
- Columnas incluidas:

### 3.3 Categorías del problema

Describe aquí las clases presentes en el dataset, por ejemplo:

- `World`
- `Sports`
- `Business`
- `Science/Technology`

### 3.4 Observaciones iniciales

Incluye una descripción general del dataset, su escala, utilidad y pertinencia para el problema de clasificación.

---

## 4. Análisis exploratorio del conjunto de datos

### 4.1 Carga y visualización de una muestra

Explica brevemente cómo se cargaron los archivos y qué columnas de texto se utilizaron.

### 4.2 Distribución por clase

Presenta una tabla o gráfica con la cantidad de noticias por categoría y comenta si el dataset está balanceado.

### 4.3 Longitud de los textos

Resume observaciones sobre la longitud de las noticias y su posible impacto en la clasificación.

### 4.4 Valores nulos y duplicados

Explica si se detectaron problemas de calidad de datos y cómo se manejaron.

### 4.5 Interpretación del análisis exploratorio

Redacta una síntesis técnica de lo observado antes del preprocesamiento.

---

## 5. Preprocesamiento del texto

### 5.1 Construcción del texto de entrada

Explica si se utilizó solo el título, solo la descripción o una combinación de ambos.

### 5.2 Normalización

Describe las transformaciones aplicadas, por ejemplo:

- conversión a minúsculas,
- eliminación de caracteres especiales,
- eliminación de números o símbolos,
- limpieza general.

### 5.3 Tokenización

Explica en qué consistió la tokenización y por qué fue necesaria.

### 5.4 Eliminación de stopwords

Justifica si se eliminaron y por qué.

### 5.5 Lematización

Describe el proceso de lematización aplicado y su utilidad en este contexto.

### 5.6 Resultado del preprocesamiento

Muestra ejemplos breves de texto antes y después del preprocesamiento.

---

## 6. Representación vectorial del texto

### 6.1 Método seleccionado

Indica el método usado para representar el texto, por ejemplo:

- TF-IDF
- embeddings

### 6.2 Justificación de la elección

Explica por qué ese método fue adecuado para esta actividad.

### 6.3 Configuración

Incluye parámetros relevantes como:

- número máximo de características,
- n-gramas,
- filtros por frecuencia.

### 6.4 Comentario técnico

Explica brevemente por qué un modelo supervisado necesita una representación numérica del texto.

---

## 7. Entrenamiento de modelos supervisados

### 7.1 Modelos seleccionados

Lista los modelos utilizados, por ejemplo:

- Naive Bayes
- Logistic Regression
- LinearSVC

### 7.2 Justificación de selección

Explica por qué esos modelos son adecuados para clasificación de texto.

### 7.3 División de entrenamiento y prueba

Describe cómo se definieron los conjuntos de entrenamiento y prueba.

### 7.4 Validación cruzada

Explica cómo se aplicó la validación cruzada y por qué es importante.

---

## 8. Evaluación del rendimiento

### 8.1 Métricas utilizadas

Describe brevemente:

- Accuracy
- Precision
- Recall
- F1-score

### 8.2 Resultados por modelo

Incluye una tabla comparativa con las métricas obtenidas por cada modelo.

### 8.3 Classification report

Resume el comportamiento por clase del modelo más fuerte.

### 8.4 Matriz de confusión

Incluye la matriz de confusión del modelo final y comenta cuáles clases se confundieron con más frecuencia.

---

## 9. Análisis de errores

Presenta ejemplos de noticias mal clasificadas y analiza posibles causas, por ejemplo:

- ambigüedad temática,
- vocabulario compartido entre categorías,
- textos cortos,
- insuficiencia del preprocesamiento clásico.

---

## 10. Comparación y selección del modelo final

### 10.1 Comparación global

Analiza:

- rendimiento cuantitativo,
- consistencia en validación cruzada,
- simplicidad,
- interpretabilidad,
- costo computacional.

### 10.2 Modelo seleccionado

Indica cuál fue el modelo final elegido.

### 10.3 Justificación técnica

Explica claramente por qué fue seleccionado por encima de los demás.

---

## 11. Limitaciones del trabajo

Describe limitaciones como:

- pérdida de contexto semántico con TF-IDF,
- ausencia de modelos profundos,
- dependencia del preprocesamiento clásico,
- clases potencialmente cercanas entre sí.

---

## 12. Mejoras futuras

Propón mejoras posibles, por ejemplo:

- ajuste de hiperparámetros,
- uso de embeddings preentrenados,
- uso de transformers como BERT,
- mayor análisis interpretativo de errores.

---

## 13. Conclusiones

Redacta una conclusión final integrando:

- lo realizado,
- los principales resultados,
- el modelo con mejor desempeño,
- el valor práctico de la solución,
- las limitaciones y proyección futura.

---

## 14. Referencias

- Dataset utilizado:
- Documentación consultada:
- Librerías empleadas:

