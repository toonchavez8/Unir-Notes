# Informe - Actividad 1

## Segmentación de clientes mediante aprendizaje no supervisado

## Datos del estudiante
- Nombre:
- Matrícula:
- Asignatura:
- Fecha:

---

## 1. Introducción

En esta actividad se desarrolla un análisis de segmentación de clientes mediante técnicas de aprendizaje no supervisado, con el objetivo de identificar grupos homogéneos a partir de características demográficas y de consumo. La segmentación de clientes es una herramienta relevante en analítica de negocio, ya que permite detectar patrones ocultos y generar estrategias diferenciadas de marketing, fidelización y posicionamiento comercial.

El trabajo se apoya en un conjunto de datos con información de clientes de un centro comercial, incluyendo variables como edad, ingreso anual y puntuación de gasto. A partir de este conjunto, se realiza un proceso completo de exploración, preprocesamiento, entrenamiento de algoritmos de clustering, análisis comparativo de resultados e interpretación de los segmentos obtenidos.

---

## 2. Objetivo

Aplicar técnicas de clustering sobre un conjunto de datos de clientes para identificar grupos con características similares, comparar al menos dos métodos diferentes de segmentación y analizar la utilidad potencial de los resultados en un contexto real de negocio.

---

## 3. Descripción del dataset

### 3.1 Fuente de datos
- Dataset:
- Fuente:
- URL:
- Fecha de descarga:

### 3.2 Estructura del dataset
- Número de registros:
- Número de columnas:
- Columnas incluidas:

### 3.3 Descripción de variables relevantes
- `CustomerID`:
- `Gender`:
- `Age`:
- `Annual Income (k$)`:
- `Spending Score (1-100)`:

### 3.4 Observaciones iniciales

Escribe aquí una descripción general del conjunto de datos, su tamaño, utilidad y posibles limitaciones.

---

## 4. Análisis exploratorio de los datos

### 4.1 Exploración inicial
- Resultado de `shape`:
- Tipos de datos:
- Valores nulos:
- Duplicados:

### 4.2 Estadística descriptiva

Resume aquí los hallazgos principales del análisis descriptivo. Comenta medias, rangos, dispersión y cualquier patrón visible en edad, ingreso y gasto.

### 4.3 Detección de valores atípicos

Explica si se identificaron outliers mediante boxplots u otros métodos y si se decidió conservarlos o tratarlos.

### 4.4 Visualizaciones principales

Incluye aquí referencia a las figuras generadas:

- Histogramas
- Boxplots
- Scatter plots
- Pairplot

### 4.5 Interpretación del análisis exploratorio

Redacta aquí una interpretación técnica breve de lo observado antes de aplicar clustering.

---

## 5. Preprocesamiento de los datos

### 5.1 Selección de variables

Indica qué variables fueron usadas para el clustering y por qué.

### 5.2 Variables excluidas

Explica qué columnas no fueron utilizadas y justifica su exclusión.

### 5.3 Escalado de variables

Describe el método de escalado aplicado y justifica por qué fue necesario.

### 5.4 Resultado del preprocesamiento

Resume el estado final de los datos antes de entrenar los modelos.

---

## 6. Aplicación del primer algoritmo de clustering

### 6.1 Algoritmo seleccionado

Indica el primer algoritmo utilizado:

- Nombre del algoritmo:
- Justificación de elección:

### 6.2 Búsqueda del número óptimo de clusters

Describe el uso de:

- método del codo,
- silhouette score,
- criterio final de selección de `k`.

### 6.3 Entrenamiento del modelo

Explica la configuración del modelo final:

- número de clusters,
- parámetros,
- observaciones.

### 6.4 Resultados obtenidos

Incluye:

- gráfica de clusters,
- resumen de tamaños,
- promedios por cluster.

### 6.5 Interpretación de los clusters

Describe qué representa cada grupo identificado.

---

## 7. Aplicación del segundo algoritmo de clustering

### 7.1 Algoritmo seleccionado

- Nombre del algoritmo:
- Justificación de elección:

### 7.2 Parámetros utilizados

Describe aquí los parámetros y decisiones principales del segundo método.

### 7.3 Resultados obtenidos

Incluye:

- visualización de clusters,
- métricas,
- diferencias con respecto al primer modelo.

### 7.4 Interpretación de resultados

Explica cómo se comportó este segundo método y si produjo segmentos útiles.

---

## 8. Comparación de algoritmos

### 8.1 Comparación cuantitativa

Incluye una tabla comparativa con:

- método,
- número de clusters,
- silhouette score,
- facilidad de interpretación,
- observaciones.

### 8.2 Comparación cualitativa

Analiza:

- claridad visual de la separación,
- estabilidad,
- sensibilidad al escalado,
- facilidad de explicación,
- utilidad práctica.

### 8.3 Modelo más adecuado

Indica cuál método fue más adecuado y por qué.

---

## 9. Aplicaciones en un contexto real

Describe cómo podrían utilizarse los clusters encontrados en escenarios reales de negocio, por ejemplo:

- segmentación de mercado,
- campañas personalizadas,
- estrategias de fidelización,
- identificación de clientes de alto valor,
- diseño de promociones específicas.

---

## 10. Limitaciones del análisis

Explica aquí las principales limitaciones del trabajo, por ejemplo:

- tamaño del dataset,
- pocas variables disponibles,
- ausencia de contexto adicional del negocio,
- sensibilidad del clustering a la selección de variables y parámetros.

---

## 11. Mejoras futuras

Propón mejoras realistas, por ejemplo:

- incluir más variables de comportamiento,
- probar PCA,
- evaluar más algoritmos,
- validar la utilidad de los clusters en un caso real.

---

## 12. Conclusiones

Redacta una conclusión final integrando:

- qué se hizo,
- qué patrones se encontraron,
- qué algoritmo funcionó mejor,
- qué aportan los resultados,
- qué limitaciones quedaron abiertas.

---

## 13. Referencias

- Dataset utilizado:
- Documentación consultada:
- Librerías empleadas:

