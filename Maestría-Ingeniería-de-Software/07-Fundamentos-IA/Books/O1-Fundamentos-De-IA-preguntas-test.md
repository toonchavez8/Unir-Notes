# Preguntas De Test

> Guía de estudio basada en `O1-Fundamentos-De-IA.md`: conserva cada pregunta y agrega la respuesta correcta con una explicación breve para repasar el concepto.

## Tema 1

1. ¿Qué impulsó la investigación y advance en el aprendizaje automático?
   - A. La búsqueda de inteligencia avanzada en computación.
   - B. La resolución de problemas de predicción complejos.
   - C. El diseño de asistentes virtuales.
   - D. Las obras de ciencia ficción.

   - **Respuesta:** B. La resolución de problemas de predicción complejos.
   - **Explicación:** El tema explica que el aprendizaje automático empezó a usarse en problemas de predicción complejos donde los modelos estadísticos clásicos no eran suficientes.

2. ¿El aprendizaje automático es?
   - A. Un algoritmo matemático que resuelve un problema.
   - B. Un algoritmo computacional inteligente.
   - C. Un proceso de inducción del conocimiento.
   - D. Un mecanismo mediante el que dotar de inteligencia a una aplicación.

   - **Respuesta:** C. Un proceso de inducción del conocimiento.
   - **Explicación:** La definición del material presenta el aprendizaje automático como un proceso de inducción del conocimiento a partir de datos.

3. Las categorías del aprendizaje automático se dividen según:
   - A. La naturaleza de los datos y la disponibilidad de estos.
   - B. La capacidad para resolver problemas complejos.
   - C. La complejidad computacional del problema formulado.
   - D. La existencia o no de una resolución humana al problema dado.

   - **Respuesta:** A. La naturaleza de los datos y la disponibilidad de estos.
   - **Explicación:** Las categorías se organizan según el tipo de datos disponibles y si existen etiquetas, interacción con el entorno o ausencia de objetivos conocidos.

4. El aprendizaje automático se divide en las siguientes categorías:
   - A. Redes neuronales y aprendizaje profundo.
   - B. Supervisado, no supervisado y por refuerzo.
   - C. Supervisado y no supervisado.
   - D. Aprendizaje profundo y procesamiento del lenguaje natural.

   - **Respuesta:** B. Supervisado, no supervisado y por refuerzo.
   - **Explicación:** El texto divide el aprendizaje automático en tres grandes paradigmas: supervisado, no supervisado y por refuerzo.

5. El aprendizaje supervisado:
   - A. Se basa en inferir una respuesta con base en los datos etiquetados previamente.
   - B. Se basa en inferir una respuesta tras una supervisión humana.
   - C. Se basa en inferir una respuesta a partir de los datos obtenidos del entorno.
   - D. Ninguna de las anteriores es correcta.

   - **Respuesta:** A. Se basa en inferir una respuesta con base en los datos etiquetados previamente.
   - **Explicación:** En el aprendizaje supervisado se aprende con ejemplos conocidos, es decir, datos con etiqueta o salida esperada.

6. El aprendizaje no supervisado:
   - A. Se basa en inferir una respuesta con base en los datos etiquetados y conocidos previamente.
   - B. Se basa en inferir una respuesta tras una supervisión humana.
   - C. Se basa en inferir una respuesta a partir de los datos obtenidos del entorno.
   - D. Se basa en inferir una respuesta con base en un conjunto de datos cuyas etiquetas no son conocidas.

   - **Respuesta:** D. Se basa en inferir una respuesta con base en un conjunto de datos cuyas etiquetas no son conocidas.
   - **Explicación:** El aprendizaje no supervisado trabaja con datos sin etiqueta conocida y busca patrones o estructuras internas.

7. El aprendizaje por refuerzo:
   - A. Se basa en inferir una respuesta con base en los datos etiquetados y conocidos previamente.
   - B. Se basa en inferir una respuesta tras una supervisión humana.
   - C. Se basa en inferir una respuesta a partir de los datos obtenidos del entorno y de las acciones tomadas.
   - D. Se basa en inferir una respuesta con base en un conjunto de datos cuyas etiquetas no son conocidas.

   - **Respuesta:** C. Se basa en inferir una respuesta a partir de los datos obtenidos del entorno y de las acciones tomadas.
   - **Explicación:** En el aprendizaje por refuerzo un agente aprende al interactuar con el entorno y recibir respuesta a sus acciones.

8. ¿Qué dos tipos de problemas resuelve el aprendizaje supervisado?
   - A. Regresión y clasificación.
   - B. Agrupamiento y clasificación.
   - C. Agrupamiento y detección de anomalías.
   - D. Detección de anomalías y regresión.

   - **Respuesta:** A. Regresión y clasificación.
   - **Explicación:** Los problemas supervisados se dividen en regresión, cuando se predicen valores continuous, y clasificación, cuando se predicen categorías.

9. ¿Qué nos muestra una matriz de confusión?
   - A. La cantidad de confusión que hay en un algoritmo.
   - B. Una relación entre las clases observadas y predichas.
   - C. Un conjunto de datos no etiquetados listos para el entrenamiento.
   - D. La capacidad de un modelo de predecir un resultado.

   - **Respuesta:** B. Una relación entre las clases observadas y predichas.
   - **Explicación:** La matriz de confusión compara las clases reales con las clases predichas y permite calcular aciertos y errores.

10. Si entrenamos un clasificador para detectar el SPAM y queremos un modelo que maximize la detección de este, entonces debemos optimizar: (spam-positive, no spam-negative)
   - A. La tasa de TP (true positive).
   - B. La tasa de FP (false positive).
   - C. La tasa de TN (true negative).
   - D. La tasa de FN (false negative).

   - **Respuesta:** A. La tasa de TP (true positive).
   - **Explicación:** Si spam es la clase positiva y se quiere detectar el máximo spam possible, interesa maximizar los verdaderos positivos.

1. Si entrenamos un clasificador para detectar el SPAM y queremos un modelo que minimice la clasificación de correos legítimos como SPAM debemos: ( spam- negative, no spam-positive)
   - A. Maximizar la tasa de TP (true positive).
   - B. Minimizar la tasa de FP (false positive).
   - C. Maximizar la tasa de TN (true negative).
   - D. Minimizar la tasa de FN (false negative).

   - **Respuesta:** D. Minimizar la tasa de FN (false negative).
   - **Explicación:** El enunciado define spam como negativo y no spam como positivo; por eso un correo legítimo marcado como spam es un falso negativo y debe minimizarse.

2. La precisión de un modelo nos indica:
   - A. Cuántas veces está en lo cierto cuando el modelo predice la clase positiva.
   - B. La proporción entre el número de predicciones correctas y el número total de predicciones.
   - C. La ratio de los ejemplos positivos correctamente clasificados.
   - D. La proporción de los ejemplos negativos correctamente clasificados.

   - **Respuesta:** A. Cuántas veces está en lo cierto cuando el modelo predice la clase positiva.
   - **Explicación:** La precisión o positive predictive value mide la proporción de predicciones positivas que realmente son positivas.

3. La especificidad de un modelo nos indica:
   - A. Cuántas veces está en lo cierto cuando el modelo predice la clase positiva.
   - B. La proporción entre el número de predicciones correctas y el número total de predicciones.
   - C. La ratio de los ejemplos positivos correctamente clasificados.
   - D. La proporción de los ejemplos negativos correctamente clasificados.

   - **Respuesta:** D. La proporción de los ejemplos negativos correctamente clasificados.
   - **Explicación:** La especificidad mide la tasa de verdaderos negativos, es decir, cuántos ejemplos negativos se clasifican correctamente.

4. Una curva ROC nos permite:
   - A. Hallar el mejor umbral para determinar cuándo un dato pertenece a una u otra categoría.
   - B. Medir la precisión de un modelo de clasificación multiclase.
   - C. Hallar el coeficiente AUC de un modelo de regresión.
   - D. Clasificar los resultados del modelo con base en la matriz de confusión.

   - **Respuesta:** A. Hallar el mejor umbral para determinar cuándo un dato pertenece a una u otra categoría.
   - **Explicación:** La curva ROC compara sensibilidad y falsos positivos para distintos umbrales, lo que ayuda a elegir el punto de decisión.

5. ¿Cuál es una característica del MSE?
   - A. Es especialmente útil cuando se trabaja con variables que tienen valores muy dispersos.
   - B. Nos permite ver si nuestro modelo subestima sistemáticamente (más error negativo) o sobreestima.
   - C. Penaliza fuertemente los errores grandes debido a su naturaleza cuadrática.
   - D. Ninguna de las anteriores es correcta.

   - **Respuesta:** C. Penaliza fuertemente los errores grandes debido a su naturaleza cuadrática.
   - **Explicación:** El MSE eleva los errores al cuadrado, por lo que los errores grandes pesan más en la métrica.

6. Las métricas para los algoritmos de agrupamiento:
   - A. Se basan en medir la distancia entre los puntos de un grupo y los del clúster más cercano.
   - B. Se basan en medir la similitud de los puntos dentro de un mismo grupo y la separación entre distintos clústeres.
   - C. Se basan en medir la distancia mínima entre distintos grupos y la máxima dentro de un mismo clúster.
   - D. Todas las anteriores son correctas.

   - **Respuesta:** D. Todas las anteriores son correctas.
   - **Explicación:** Las métricas de clustering evalúan cohesión dentro de los grupos, separación entre clústeres y distancias como las usadas por silueta o Dunn.

7. El aprendizaje automático puede beneficiar en el proceso de desarrollo software mediante:
   - A. La generación automática de código con chatbots o asistentes (por ejemplo, ChatGPT).
   - B. La generación automática de código para pruebas de software.
   - C. El diseño automático de los diagrams UML.
   - D. La redacción automática de los manuales de usuario.

   - **Respuesta:** A. La generación automática de código con chatbots o asistentes (por ejemplo, ChatGPT).
   - **Explicación:** El material relaciona el aprendizaje automático con herramientas de asistencia al desarrollo, incluidas soluciones de generación de código.

8. Cuando se habla de sesgo y discriminación en el aprendizaje automático se hace referencia a:
   - A. Los sesgos que tienen los desarrolladores que escriben código.
   - B. Los sesgos que pueden container los conjuntos de datos empleados en el entrenamiento.
   - C. La inyección de código en los modelos que los haga discriminatorios.
   - D. Las decisiones discriminatorias dentro del equipo de desarrollo.

   - **Respuesta:** B. Los sesgos que pueden container los conjuntos de datos empleados en el entrenamiento.
   - **Explicación:** El sesgo en aprendizaje automático suele venir de datos de entrenamiento no representativos o con patrones discriminatorios.

9. ¿Cuál es una característica del MPE?
   - A. Es especialmente útil cuando se trabaja con variables que tienen valores muy dispersos.
   - B. Nos permite ver si nuestro modelo subestima sistemáticamente (más error negativo) o sobreestima.
   - C. Penaliza fuertemente los errores grandes debido a su naturaleza cuadrática.
   - D. Ninguna de las anteriores es correcta.

   - **Respuesta:** B. Nos permite ver si nuestro modelo subestima sistemáticamente (más error negativo) o sobreestima.
   - **Explicación:** El MPE conserva el signo del error, por eso permite detectar sesgo de subestimación o sobreestimación.

10. ¿Cuál es una característica del RMSLE?
   - A. Es especialmente útil cuando se trabaja con variables que tienen valores muy dispersos.
   - B. Nos permite ver si nuestro modelo subestima sistemáticamente (más error negativo) o sobreestima.
   - C. Penaliza fuertemente los errores grandes debido a su naturaleza cuadrática.
   - D. Ninguna de las anteriores es correcta.

   - **Respuesta:** A. Es especialmente útil cuando se trabaja con variables que tienen valores muy dispersos.
   - **Explicación:** El RMSLE se usa en regresión cuando la variable objetivo tiene escala amplia y las diferencias relativas son importantes.

## Tema 2

1. ¿Cuál de las siguientes funciones se utilize para calcular la salida de una neurona artificial?
   - A. Función coseno.
   - B. Función signo.
   - C. Función logarítmica.
   - D. Función tangente.

   - **Respuesta:** B. Función signo.
   - **Explicación:** El texto indica que la salida de una neurona artificial puede calcularse con la función signo.

2. ¿Qué tipo de red neuronal es el perceptrón?
   - A. Una red recurrente.
   - B. Una red convolucional.
   - C. Una red de una sola capa.
   - D. Una red de autoencoders.

   - **Respuesta:** C. Una red de una sola capa.
   - **Explicación:** El perceptrón se describe como la red neuronal artificial más sencilla y está formado por una sola capa.

3. ¿Cuál es el objetivo del aprendizaje en una red neuronal simple?
   - A. Maximizar el error entre la salida obtenida y la esperada.
   - B. Seleccionar los pesos que mejor se ajusten a las entradas y salidas definidas a priori.
   - C. Utilizar funciones no supervisadas para ajustar los pesos.
   - D. Minimizar la cantidad de capas en la red.

   - **Respuesta:** B. Seleccionar los pesos que mejor se ajusten a las entradas y salidas definidas a priori.
   - **Explicación:** El aprendizaje ajusta pesos a partir de entradas y salidas esperadas para reducir el error.

4. ¿Qué nombre recibe la diferencia entre la salida obtenida y la salida esperada en una red neuronal?
   - A. Gradiente.
   - B. Error.
   - C. Peso.
   - D. Umbral.

   - **Respuesta:** B. Error.
   - **Explicación:** La diferencia entre la salida obtenida y la salida esperada se denomina error, pérdida o coste.

5. ¿Qué valor toma la tasa de aprendizaje en el ajuste de pesos de una red neuronal?
   - A. Entre 0 y 1.
   - B. Entre -1 y 1.
   - C. Mayor a 1.
   - D. Menor a 0.

   - **Respuesta:** A. Entre 0 y 1.
   - **Explicación:** La tasa de aprendizaje pondera la importancia del error y el material la define como un valor entre 0 y 1.

6. ¿Cuál es la principal característica de las redes neuronales recurrentes?
   - A. Sus salidas alimentan las entradas formando un bucle.
   - B. Tienen múltiples capas ocultas.
   - C. Utilizan la retropropagación del error.
   - D. Se basan en arquitecturas convolucionales.

   - **Respuesta:** A. Sus salidas alimentan las entradas formando un bucle.
   - **Explicación:** Las redes recurrentes se caracterizan por retroalimentar sus salidas hacia entradas, creando ciclos.

7. ¿Qué problema presentan las redes de Hopfield?
   - A. No pueden almacenar memorias fundamentales.
   - B. Alcanzar un estado estable no siempre corresponde a una memoria fundamental.
   - C. Necesitan pocas neuronas para almacenar mucha información.
   - D. Son adecuadas para la asociación de informaciones diferentes.

   - **Respuesta:** B. Alcanzar un estado estable no siempre corresponde a una memoria fundamental.
   - **Explicación:** El texto señala que una red de Hopfield puede estabilizarse en un estado que no sea una memoria fundamental.

8. ¿Qué tipo de redes se utilizan para el reconocimiento de imágenes y patrones?
   - A. Redes autoencoders.
   - B. Redes neuronales convolucionales.
   - C. Redes recurrentes.
   - D. Redes Hopfield.

   - **Respuesta:** B. Redes neuronales convolucionales.
   - **Explicación:** Las CNN son las redes más usadas para reconocimiento de imágenes, objetos y patrones visuals.

9. ¿Qué caracteriza a las redes autoencoders?
   - A. Su capacidad para clasificar datos.
   - B. Su estructura de capas completamente conectadas.
   - C. Su uso en reducción de dimensionalidad y eliminación de ruido.
   - D. Su aplicación en redes convolucionales.

   - **Respuesta:** C. Su uso en reducción de dimensionalidad y eliminación de ruido.
   - **Explicación:** Los autoencoders comprimen la entrada en un espacio latente y pueden usarse para reducción de dimensionalidad o denoising.

10. ¿Qué es la función de activación en una red neuronal?
   - A. Un método para entrenar la red.
   - B. Un algoritmo para ajustar los pesos.
   - C. Una función que introduce la no linealidad en el modelo.
   - D. Una técnica de optimización.

   - **Respuesta:** C. Una función que introduce la no linealidad en el modelo.
   - **Explicación:** Las funciones de activación permiten que la red modele relaciones no lineales entre entradas y salidas.

1. ¿Qué tipo de función de activación es la función sigmoide?
   - A. Lineal.
   - B. No lineal.
   - C. Exponencial.
   - D. Logarítmica.

   - **Respuesta:** B. No lineal.
   - **Explicación:** La sigmoide es una función no lineal con forma de S, usada habitualmente como activación.

2. ¿En qué consistent las redes prealimentadas (feedforward)?
   - A. En tener conexiones que forman bucles.
   - B. En procesar secuencias temporales de datos.
   - C. En tener conexiones unidireccionales de las entradas a las salidas.
   - D. En utilizar autoencoders.

   - **Respuesta:** C. En tener conexiones unidireccionales de las entradas a las salidas.
   - **Explicación:** Las redes feedforward propagan la señal en una sola dirección, desde la entrada hasta la salida.

3. ¿Cuál es la ventaja principal de las redes convolucionales sobre las redes tradicionales?
   - A. Tienen menos capas.
   - B. Requieren menos datos para entrenar.
   - C. Pueden captar características espaciales y jerárquicas.
   - D. No necesitan función de activación.

   - **Respuesta:** C. Pueden captar características espaciales y jerárquicas.
   - **Explicación:** Las CNN aprenden características locales y jerárquicas, lo que las hace adecuadas para imágenes.

4. ¿Cuál es una de las características principales de las redes de Hopfield?
   - A. Son redes recurrentes con salidas que alimentan las entradas.
   - B. Utilizan retropropagación para ajustar los pesos.
   - C. Se utilizan principalmente para tareas de clasificación.
   - D. Tienen una estructura jerárquica.

   - **Respuesta:** A. Son redes recurrentes con salidas que alimentan las entradas.
   - **Explicación:** Las Hopfield son redes recurrentes monocapa donde las salidas retroalimentan a otras neuronas.

5. ¿Qué define la capacidad de una red de Hopfield para almacenar memorias?
   - A. El número de capas ocultas.
   - B. La cantidad de patrones de entrada.
   - C. El tamaño de la red (número de neuronas).
   - D. La tasa de aprendizaje.

   - **Respuesta:** C. El tamaño de la red (número de neuronas).
   - **Explicación:** La capacidad de almacenamiento de una red de Hopfield está limitada por su tamaño, es decir, por el número de neuronas y conexiones.

6. ¿Cuál de las siguientes afirmaciones sobre las redes autoasociativas es incorrecta?
   - A. Pueden recordar patrones completos a partir de fragmentos de estos.
   - B. Se basan en el principio de autoaprendizaje.
   - C. Necesitan grandes conjuntos de datos para entrenarse.
   - D. Son utilizadas para tareas de memoria asociativa.

   - **Respuesta:** C. Necesitan grandes conjuntos de datos para entrenarse.
   - **Explicación:** Las redes autoasociativas se orientan a memoria asociativa y recuperación de patrones, no a entrenamiento con grandes datasets como requisito principal.

7. ¿Qué técnica se utilize frecuentemente para ajustar los pesos en las redes neuronales?
   - A. Algoritmo genético.
   - B. Algoritmo de optimización de enjambre de partículas.
   - C. Retropropagación del error.
   - D. Análisis de components principales.

   - **Respuesta:** C. Retropropagación del error.
   - **Explicación:** La retropropagación es el método frecuente para ajustar pesos en redes neuronales multicapa.

8. ¿Qué característica de las redes convolucionales les permite procesar imágenes de manera eficiente?
   - A. La función sigmoide.
   - B. El uso de capas de pooling.
   - C. La estructura completamente conectada.
   - D. La tasa de aprendizaje variable.

   - **Respuesta:** B. El uso de capas de pooling.
   - **Explicación:** Las capas de pooling reducen la dimensionalidad y ayudan a procesar imágenes de forma eficiente.

9. ¿Cuál es la función principal de las redes neuronales recurrentes (RNN)?
   - A. Procesar datos de entrada en lotes.
   - B. Captar dependencias temporales en secuencias de datos.
   - C. Realizar clasificación de imágenes.
   - D. Reducir la dimensionalidad de datos.

   - **Respuesta:** B. Captar dependencias temporales en secuencias de datos.
   - **Explicación:** Las RNN están diseñadas para información sequential y capturan dependencias entre pasos temporales.

10. ¿Qué es una red generativa adversarial (GAN)?
   - A. Un tipo de red que clasifica los datos en múltiples categorías.
   - B. Un tipo de red que genera datos nuevos a partir de datos existentes mediante dos redes que compiten.
   - C. Un tipo de red que realiza tareas de segmentación de imágenes.
   - D. Una red que se especializa en la compresión de datos.

   - **Respuesta:** B. Un tipo de red que genera datos nuevos a partir de datos existentes mediante dos redes que compiten.
   - **Explicación:** Una GAN combina generador y discriminador, dos redes que compiten para producir datos sintéticos realistas.

## Tema 3

1. ¿Qué es el procesamiento del lenguaje natural (NLP)?
   - A. Un campo que estudia la programación de sistemas.
   - B. Un área interdisciplinaria que abarca varios campos relacionados con el lenguaje humano.
   - C. Una rama de la lingüística que solo estudia la semántica.
   - D. Un proceso automático para la traducción de textos.

   - **Respuesta:** B. Un área interdisciplinaria que abarca varios campos relacionados con el lenguaje humano.
   - **Explicación:** El NLP se presenta como un campo interdisciplinario donde confluyen informática, lingüística, ingeniería y ciencias cognitivas.

2. ¿Cuál de las siguientes técnicas no es un tipo de tokenización?
   - A. Tokenización por palabras.
   - B. Tokenización por frases.
   - C. Tokenización por n-gramas.
   - D. Tokenización por números.

   - **Respuesta:** D. Tokenización por números.
   - **Explicación:** El tema menciona tokenización por palabras, subpalabras, caracteres, n-gramas y frases, no por números.

3. ¿Cuál es la técnica de normalización que elimina palabras comunes, como 'el', 'de', 'y'?
   - A. Lematización.
   - B. Expansión de contracciones.
   - C. Eliminación de stopwords.
   - D. Corrección ortográfica.

   - **Respuesta:** C. Eliminación de stopwords.
   - **Explicación:** Las stopwords son palabras comunes como articulos, preposiciones y conjunciones que suelen eliminarse para reducir ruido.

4. ¿Cuál es el propósito de la lematización?
   - A. Convertir todo el texto a minúsculas.
   - B. Reducir las palabras a su forma base o lema.
   - C. Eliminar caracteres especiales y puntuación.
   - D. Corregir errores ortográficos.

   - **Respuesta:** B. Reducir las palabras a su forma base o lema.
   - **Explicación:** La lematización convierte formas como corriendo o corrió a su lema, por ejemplo correr.

5. ¿Cuál de las siguientes opciones describe mejor el etiquetado morfosintáctico (POS tagging)?
   - A. Un proceso para traducir textos.
   - B. Un proceso para asignar categorías gramaticales a las palabras.
   - C. Un proceso para corregir errores de ortografía.
   - D. Un método para eliminar stopwords.

   - **Respuesta:** B. Un proceso para asignar categorías gramaticales a las palabras.
   - **Explicación:** El POS tagging asigna a cada palabra una etiqueta gramatical, como sustantivo, verbo o adjetivo.

6. ¿Qué es el Penn Treebank?
   - A. Un conjunto de reglas ortográficas.
   - B. Un corpus anotado utilizado para el etiquetado morfosintáctico en inglés.
   - C. Un algoritmo de traducción automática.
   - D. Un diccionario de sinónimos.

   - **Respuesta:** B. Un corpus anotado utilizado para el etiquetado morfosintáctico en inglés.
   - **Explicación:** El material indica que muchos algoritmos para inglés usan el Penn Treebank como referencia de etiquetas gramaticales.

7. ¿Qué técnica de normalización se aplica para convertir un texto a minúsculas?
   - A. Expansión de contracciones.
   - B. Conversión a minúsculas.
   - C. Lematización.
   - D. Derivación.

   - **Respuesta:** B. Conversión a minúsculas.
   - **Explicación:** Lowercasing consiste precisamente en convertir todo el texto a minúsculas para reducir variabilidad.

8. ¿Qué técnica se utilize para manejar palabras como ‘tmb’ en textos informales?
   - A. Derivación.
   - B. Eliminación de stopwords.
   - C. Expansión de contracciones.
   - D. Corrección ortográfica.

   - **Respuesta:** C. Expansión de contracciones.
   - **Explicación:** La expansión de contracciones convierte abreviaturas informales como tmb en su forma completa, también.

9. ¿Cuál de los siguientes campos no está relacionado directamente con el NLP?
   - A. Informática.
   - B. Ingeniería de telecomunicaciones.
   - C. Biología molecular.
   - D. Lingüística.

   - **Respuesta:** C. Biología molecular.
   - **Explicación:** El NLP se relaciona directamente con informática, lingüística, ingeniería y áreas cognitivas, no con biología molecular.

10. ¿Cuál es una de las aplicaciones del análisis de sentimientos en NLP?
   - A. Predecir el clima.
   - B. Analizar las emociones expresadas en textos.
   - C. Calcular estadísticas matemáticas.
   - D. Mejorar la calidad del audio.

   - **Respuesta:** B. Analizar las emociones expresadas en textos.
   - **Explicación:** El análisis de sentimientos identifica subjetividad, opiniones o emociones expresadas en texto.

1. ¿Qué problema resuelve la normalización en NLP?
   - A. Elimina caracteres innecesarios y estandariza el texto.
   - B. Aumenta el tamaño del texto.
   - C. Traduce textos automáticamente.
   - D. Analiza la estructura gramatical del texto.

   - **Respuesta:** A. Elimina caracteres innecesarios y estandariza el texto.
   - **Explicación:** La normalización prepara el texto eliminando ruido y estandarizando formas antes del modelado.

2. ¿Qué técnica se utilize para agrupar palabras con significados similares?
   - A. Tokenización.
   - B. Lematización.
   - C. Conversión a minúsculas.
   - D. Expansión de contracciones.

   - **Respuesta:** B. Lematización.
   - **Explicación:** La lematización agrupa variantes morfológicas en una forma base común, lo que ayuda a tratar palabras relacionadas como una unidad.

3. ¿Qué método se emplea para dividir un texto en oraciones?
   - A. Tokenización por palabras.
   - B. Tokenización por frases.
   - C. Tokenización por caracteres.
   - D. Tokenización por n-gramas.

   - **Respuesta:** B. Tokenización por frases.
   - **Explicación:** La tokenización por frases divide el texto en unidades oracionales usando signos de puntuación u otros límites.

4. ¿Qué técnica se aplica para reducir las palabras a su raíz común?
   - A. Derivación.
   - B. Lematización.
   - C. Normalización.
   - D. Tokenización.

   - **Respuesta:** A. Derivación.
   - **Explicación:** La derivación o stemming corta sufijos para reducir palabras a una raíz común.

5. ¿Cuál es el principal desafío de aplicar modelos de NLP en idiomas diferentes al inglés?
   - A. La falta de tokenización.
   - B. La falta de caracteres especiales.
   - C. La falta de acentos y otros caracteres en el inglés.
   - D. La falta de palabras comunes.

   - **Respuesta:** C. La falta de acentos y otros caracteres en el inglés.
   - **Explicación:** El texto señala que muchos modelos se entrenan en inglés y fallan al pasar a lenguas con acentos u otros caracteres ausentes en inglés.

6. ¿Qué técnica de tokenización es más adecuada para el análisis de spam?
   - A. Tokenización por caracteres.
   - B. Tokenización por n-gramas.
   - C. Tokenización por palabras.
   - D. Tokenización por frases.

   - **Respuesta:** B. Tokenización por n-gramas.
   - **Explicación:** Los n-gramas se mencionan como útiles en tareas de análisis de texto como detección de spam.

7. ¿Cuál es el principal objetivo del etiquetado morfosintáctico en NLP?
   - A. Traducir textos automáticamente.
   - B. Eliminar stopwords.
   - C. Reducir el tamaño de los datos.
   - D. Asignar etiquetas gramaticales a cada palabra.

   - **Respuesta:** D. Asignar etiquetas gramaticales a cada palabra.
   - **Explicación:** El objetivo del etiquetado morfosintáctico es asignar la categoría gramatical correspondiente a cada palabra.

8. ¿Qué factor es crítico al aplicar técnicas NLP a múltiples idiomas?
   - A. Las diferencias gramaticales y semánticas entre idiomas.
   - B. El tamaño del vocabulario.
   - C. El número de palabras.
   - D. La longitud de las oraciones.

   - **Respuesta:** A. Las diferencias gramaticales y semánticas entre idiomas.
   - **Explicación:** Al trabajar con varios idiomas importan las diferencias de gramática, significado, caracteres y uso contextual.

9. ¿Cuál es el propósito principal de eliminar stopwords en el NLP?
   - A. Reducir el ruido en el análisis de texto.
   - B. Aumentar la precisión del etiquetado POS.
   - C. Incrementar la longitud del texto.
   - D. Mejorar la corrección ortográfica.

   - **Respuesta:** A. Reducir el ruido en el análisis de texto.
   - **Explicación:** Eliminar stopwords reduce palabras de bajo aporte semántico y permite centrarse en términos más relevantes.

10. ¿Qué técnica se usa para identificar el contexto semántico en un corpus?
   - A. Tokenización.
   - B. Análisis sintáctico.
   - C. Modelos de lenguaje.
   - D. Eliminación de stopwords.

   - **Respuesta:** C. Modelos de lenguaje.
   - **Explicación:** Los modelos de lenguaje capturan relaciones de contexto y significado dentro de un corpus.

## Tema 4

1. ¿Cuál es uno de los principios éticos fundamentales en la inteligencia artificial que busca evitar resultados discriminatorios?
   - A. Beneficencia.
   - B. Responsabilidad.
   - C. Sesgos y equidad.
   - D. Privacidad.

   - **Respuesta:** C. Sesgos y equidad.
   - **Explicación:** Este principio busca evitar que los sistemas perpetúen desigualdades o produzcan resultados discriminatorios.

2. ¿Qué principio ético en la IA establece que los desarrolladores deben rendir cuentas por sus decisiones y acciones?
   - A. Transparencia.
   - B. Beneficencia.
   - C. Responsabilidad.
   - D. Privacidad.

   - **Respuesta:** C. Responsabilidad.
   - **Explicación:** La responsabilidad exige que desarrolladores y operadores rindan cuentas por decisiones y acciones vinculadas a sistemas de IA.

3. ¿Por qué es importante la transparencia en los sistemas de IA?
   - A. Para reducir el costo de desarrollo.
   - B. Para generar confianza en la tecnología y permitir la auditoría de los sistemas.
   - C. Para hacer más eficiente el proceso de toma de decisiones.
   - D. Para evitar el uso de datos personales.

   - **Respuesta:** B. Para generar confianza en la tecnología y permitir la auditoría de los sistemas.
   - **Explicación:** La transparencia hace comprensibles procesos y decisiones, lo que facilita confianza, auditoría y revisión.

4. ¿Cuál de las siguientes es una fuente común de sesgo en los modelos de IA?
   - A. Código de programación abierto.
   - B. Datos de entrenamiento desbalanceados.
   - C. Actualización constante del algoritmo.
   - D. Alta complejidad en el modelo.

   - **Respuesta:** B. Datos de entrenamiento desbalanceados.
   - **Explicación:** Los datos no representativos o desbalanceados son una fuente habitual de sesgo en modelos de IA.

5. ¿Cuál es el principio ético que exige la protección de la información personal en sistemas de IA?
   - A. Privacidad.
   - B. Beneficencia.
   - C. Responsabilidad.
   - D. Equidad.

   - **Respuesta:** A. Privacidad.
   - **Explicación:** La privacidad exige proteger información personal y respetar la intimidad de los individuos.

6. ¿Qué implica el principio de beneficencia en la IA?
   - A. Que la IA debe set utilizada para promover el bienestar y minimizar los riesgos.
   - B. Que los sistemas de IA deben set siempre abiertos y accesibles al público.
   - C. Que los desarrolladores no deben rendir cuentas por sus acciones.
   - D. Que la IA no debe involucrar ninguna forma de automatización.

   - **Respuesta:** A. Que la IA debe set utilizada para promover el bienestar y minimizar los riesgos.
   - **Explicación:** La beneficencia indica que la IA debe buscar beneficio social y reducir daños potenciales.

7. ¿Cuál de las siguientes estrategias se utilize para mitigar los sesgos en los modelos de IA?
   - A. Uso exclusivo de datos históricos.
   - B. Entrenamiento con datos desbalanceados.
   - C. Auditoría de algoritmos.
   - D. Eliminación de regularizaciones en el modelo.

   - **Respuesta:** C. Auditoría de algoritmos.
   - **Explicación:** La auditoría revisa modelos sistemáticamente para detectar y corregir sesgos.

8. ¿Qué ocurrió con el sistema de contratación basado en IA de Amazon en 2018?
   - A. Fue exitoso y ampliamente adoptado.
   - B. Mostró un sesgo en contra de candidatas mujeres.
   - C. Mejoró la diversidad en la contratación.
   - D. Fue hackeado y sus datos comprometidos.

   - **Respuesta:** B. Mostró un sesgo en contra de candidatas mujeres.
   - **Explicación:** El caso citado de Amazon en 2018 se descartó porque el sistema de contratación perjudicaba a candidatas mujeres.

9. ¿Qué principio se viola cuando un sistema de IA trata de manera diferente a varios grupos de personas en función de características protegidas, como raza o género?
   - A. Privacidad.
   - B. Transparencia.
   - C. Discriminación algorítmica.
   - D. Beneficencia.

   - **Respuesta:** C. Discriminación algorítmica.
   - **Explicación:** Tratar de modo desigual a grupos protegidos por raza, género u otras características constituye discriminación algorítmica.

10. ¿Cuál es una de las técnicas mencionadas para balancear los datos en el entrenamiento de modelos de IA?
   - A. Submuestreo.
   - B. Regresión logística.
   - C. Redes neuronales.
   - D. Eliminación de características.

   - **Respuesta:** A. Submuestreo.
   - **Explicación:** El tema menciona técnicas de balanceo como sobremuestreo y submuestreo para corregir desbalances.

1. ¿Cuál es uno de los principales riesgos de la falta de transparencia en los algoritmos de IA?
   - A. Aumento de la eficiencia del sistema.
   - B. Menor costo de desarrollo.
   - C. Desconfianza pública y falta de rendición de cuentas.
   - D. Incremento en la capacidad de predicción.

   - **Respuesta:** C. Desconfianza pública y falta de rendición de cuentas.
   - **Explicación:** La opacidad dificulta entender decisiones algorítmicas, lo que reduce confianza y complica la responsabilidad.

2. ¿Qué objetivo persigue la implementación de principios éticos en la IA?
   - A. Maximizar los beneficios comerciales.
   - B. Asegurar que la IA se desarrolle de manera justa y segura.
   - C. Acelerar la adopción de la IA en todas las industrias.
   - D. Reducir la cantidad de datos necesarios para entrenar modelos.

   - **Respuesta:** B. Asegurar que la IA se desarrolle de manera justa y segura.
   - **Explicación:** Los principios éticos guían el desarrollo para proteger derechos, promover equidad y minimizar riesgos.

3. ¿Qué estrategia se recomienda para mejorar la equidad en los sistemas de IA?
   - A. Utilizar solo datos recientes.
   - B. Entrenar el modelo con datos variados y representativos.
   - C. Evitar el uso de datos sensibles.
   - D. Aumentar la complejidad del modelo.

   - **Respuesta:** B. Entrenar el modelo con datos variados y representativos.
   - **Explicación:** La equidad mejora cuando los datos representan adecuadamente a la población afectada por el sistema.

4. ¿Qué principio ético en la IA está directamente relacionado con la protección de los datos personales?
   - A. Equidad.
   - B. Beneficencia.
   - C. Privacidad.
   - D. Transparencia.

   - **Respuesta:** C. Privacidad.
   - **Explicación:** La protección de datos personales se corresponde directamente con el principio de privacidad.

5. ¿Cuál es el rol de la explicabilidad en la ética de la IA?
   - A. Hacer que la IA sea más eficiente.
   - B. Permitir que los usuarios entiendan y confíen en las decisiones de la IA.
   - C. Aumentar la velocidad de procesamiento.
   - D. Reducir los costos de implementación.

   - **Respuesta:** B. Permitir que los usuarios entiendan y confíen en las decisiones de la IA.
   - **Explicación:** La explicabilidad permite comprender cómo y por qué el sistema llegó a una decisión, aumentando confianza y control.

6. ¿Cuál es un desafío común en la implementación de principios éticos en la IA?
   - A. Falta de datos.
   - B. Dificultad para definir y medir principios, como la equidad y la transparencia.
   - C. Alta velocidad de procesamiento.
   - D. Uso de algoritmos complejos.

   - **Respuesta:** B. Dificultad para definir y medir principios, como la equidad y la transparencia.
   - **Explicación:** La implementación ética es difícil porque conceptos como equidad o transparencia pueden set complejos de operacionalizar.

7. ¿Cuál de los siguientes es un enfoque para mitigar el sesgo en modelos de IA?
   - A. Aumentar la cantidad de datos sesgados.
   - B. Eliminar todas las variables sensibles del modelo.
   - C. Incorporar técnicas de fairness durante el entrenamiento del modelo.
   - D. Evitar la supervisión humana en el entrenamiento.

   - **Respuesta:** C. Incorporar técnicas de fairness durante el entrenamiento del modelo.
   - **Explicación:** Los algoritmos fairness-aware introducen ajustes durante el entrenamiento para reducir sesgos entre grupos.

8. ¿Qué es un modelo de caja negra en el contexto de la IA?
   - A. Un modelo cuya estructura y funcionamiento es completamente transparente.
   - B. Un sistema de IA cuya toma de decisiones es opaca y difícil de interpretar.
   - C. Un algoritmo que es más rápido, pero menos preciso.
   - D. Un sistema de IA utilizado exclusivamente para propósitos de investigación.

   - **Respuesta:** B. Un sistema de IA cuya toma de decisiones es opaca y difícil de interpretar.
   - **Explicación:** Un modelo de caja negra produce decisiones difíciles de explicar o auditar internamente.

9. ¿Cuál es uno de los objetivos principales de la ética en la IA?
   - A. Maximizar el rendimiento técnico.
   - B. Asegurar que los sistemas de IA respeten los derechos humanos.
   - C. Incrementar la cantidad de datos recolectados.
   - D. Reducir los costos de desarrollo de la IA.

   - **Respuesta:** B. Asegurar que los sistemas de IA respeten los derechos humanos.
   - **Explicación:** La ética en IA busca que los sistemas respeten derechos fundamentales, equidad, seguridad y bienestar.

10. ¿Cuál de las siguientes opciones es un reto para la ética de la IA en aplicaciones militares?
   - A. La mejora de la precisión en el campo de batalla.
   - B. La autonomía de las decisiones tomadas por sistemas de armas basados en IA.
   - C. El aumento de la velocidad en la toma de decisiones.
   - D. El uso exclusivo de IA para misiones de reconocimiento.

   - **Respuesta:** B. La autonomía de las decisiones tomadas por sistemas de armas basados en IA.
   - **Explicación:** En aplicaciones militares, la autonomía de armas con IA plantea riesgos graves sobre responsabilidad y daño humano.

## Tema 5

1. ¿Cuál es una de las principales razones por las que Python es popular en el desarrollo de IA?
   - A. Es el lenguaje más rápido.
   - B. Tiene una sintaxis compleja.
   - C. Posee una amplia gama de bibliotecas especializadas.
   - D. Es un lenguaje orientado a la web.

   - **Respuesta:** C. Posee una amplia gama de bibliotecas especializadas.
   - **Explicación:** Python es popular en IA por su sintaxis accessible y su ecosistema de bibliotecas como NumPy, Pandas, Scikit-learn, TensorFlow y PyTorch.

2. ¿Qué estructura de datos en Python se utilize para almacenar datos en pares clave-valor?
   - A. Lista.
   - B. Tupla.
   - C. Conjunto.
   - D. Diccionario.

   - **Respuesta:** D. Diccionario.
   - **Explicación:** Los diccionarios de Python almacenan datos como pares clave-valor.

3. ¿Cuál es la función de la biblioteca NumPy en proyectos de IA?
   - A. Manejar datos en formato JSON.
   - B. Manipular arrays multidimensionales.
   - C. Crear aplicaciones web.
   - D. Realizar pruebas unitarias.

   - **Respuesta:** B. Manipular arrays multidimensionales.
   - **Explicación:** NumPy proporciona soporte para arrays y matrices multidimensionales junto con operaciones numericas eficientes.

4. ¿Cuál de las siguientes es una biblioteca para la visualización de datos en Python?
   - A. TensorFlow.
   - B. PyTorch.
   - C. Matplotlib.
   - D. Scikit-learn.

   - **Respuesta:** C. Matplotlib.
   - **Explicación:** Matplotlib se usa para visualizacion de datos; TensorFlow, PyTorch y Scikit-learn tienen otros fines principales.

5. ¿Qué paradigma de programación es esencial en Python para la modularidad y reutilización del código en IA?
   - A. Programación funcional.
   - B. Programación estructurada.
   - C. Programación orientada a objetos.
   - D. Programación procedural.

   - **Respuesta:** C. Programación orientada a objetos.
   - **Explicación:** La POO permite organizar el codigo de forma modular y reutilizable en proyectos de IA.

6. ¿Qué hace el método `forward` en una clase de PyTorch?
   - A. Inicializa los parámetros del modelo.
   - B. Ejecuta la pasada hacia adelante en la red neuronal.
   - C. Optimiza los hiperparámetros.
   - D. Calcula la función de pérdida.

   - **Respuesta:** B. Ejecuta la pasada hacia adelante en la red neuronal.
   - **Explicación:** En PyTorch, forward define como fluye la entrada por la red para obtener la salida.

7. ¿Cuál de los siguientes bloques de código en Python maneja excepciones?
   - A. if-else .
   - B. for-loop .
   - C. try-except .
   - D. while-loop .

   - **Respuesta:** C. try-except .
   - **Explicación:** Los bloques try-except permiten capturar y manejar excepciones en Python.

8. ¿Cuál es una ventaja de usar PyTorch sobre TensorFlow?
   - A. Mejor soporte en producción.
   - B. Uso de grafos computacionales estáticos.
   - C. Facilidad de depuración con grafos dinámicos.
   - D. Mayor soporte de dispositivos móviles.

   - **Respuesta:** C. Facilidad de depuración con grafos dinámicos.
   - **Explicación:** PyTorch usa grafos computacionales dinamicos, lo que facilita la depuracion y la experimentacion.

9. ¿Qué biblioteca se utilize para manipular y analizar datos en Python?
   - A. NumPy.
   - B. Pandas.
   - C. Matplotlib.
   - D. TensorFlow.

   - **Respuesta:** B. Pandas.
   - **Explicación:** Pandas es la biblioteca enfocada en manipulacion y analysis de datos tabulares.

10. ¿Cuál es una característica principal de TensorFlow?
   - A. Autograd.
   - B. Grafos computacionales.
   - C. TorchScript.
   - D. Optimización de hardware.

   - **Respuesta:** B. Grafos computacionales.
   - **Explicación:** TensorFlow se caracteriza por construir modelos mediante grafos computacionales optimizables y desplegables.

1. ¿Cuál es la función de la biblioteca Scikit-learn?
   - A. Visualizar datos.
   - B. Manejar arrays multidimensionales.
   - C. Automatizar tareas repetitivas.
   - D. Proveer herramientas de aprendizaje automático.

   - **Respuesta:** D. Proveer herramientas de aprendizaje automático.
   - **Explicación:** Scikit-learn ofrece herramientas y algoritmos para aprendizaje automatico.

2. ¿Qué función de TensorFlow facilita la construcción de redes neuronales de manera más simple?
   - A. TFX.
   - B. Keras.
   - C. PyTorch.
   - D. Matplotlib.

   - **Respuesta:** B. Keras.
   - **Explicación:** Keras es una API de alto nivel integrada en TensorFlow que simplifica la construccion de redes neuronales.

3. ¿Qué estructura de control en Python permite iterar sobre elementos de una lista?
   - A. if-else .
   - B. for-loop .
   - C. while-loop .
   - D. switch-case .

   - **Respuesta:** B. for-loop .
   - **Explicación:** Un bucle for permite iterar sobre elementos de listas u otras colecciones en Python.

4. ¿Qué paradigma de programación utilize PyTorch para construir modelos de IA?
   - A. Programación estructurada.
   - B. Programación orientada a objetos.
   - C. Programación procedural.
   - D. Programación funcional.

   - **Respuesta:** B. Programación orientada a objetos.
   - **Explicación:** En PyTorch los modelos suelen definirse como clases que heredan de nn.Module, un enfoque propio de POO.

5. ¿Qué librería de Python es especialmente útil para cálculos numéricos?
   - A. Pandas.
   - B. NumPy.
   - C. Seaborn.
   - D. Keras.

   - **Respuesta:** B. NumPy.
   - **Explicación:** NumPy esta orientada a calculos numericos y operaciones vectorizadas sobre arrays.

6. ¿Qué función tiene `optimizer.step()` en PyTorch?
   - A. Define la arquitectura del modelo.
   - B. Calcula el gradiente.
   - C. Actualiza los parámetros del modelo.
   - D. Inicializa el modelo.

   - **Respuesta:** C. Actualiza los parámetros del modelo.
   - **Explicación:** Despues de calcular gradientes, optimizer.step() aplica la actualizacion de parametros.

7. ¿Qué herramienta de TensorFlow es parte de su ecosistema completo para machine learning?
   - A. TorchScript.
   - B. Autograd.
   - C. TFX.
   - D. PyTorch.

   - **Respuesta:** C. TFX.
   - **Explicación:** TensorFlow Extended forma parte del ecosistema de TensorFlow para pipelines completos de machine learning.

8. ¿Qué hace el método `sum` en Python cuando se aplica a una lista?
   - A. Suma todos los elementos de la lista.
   - B. Concadena los elementos de la lista.
   - C. Ordena los elementos de la lista.
   - D. Elimina duplicados de la lista.

   - **Respuesta:** A. Suma todos los elementos de la lista.
   - **Explicación:** La function sum aplicada a una lista numerica devuelve la suma de sus elementos.

9. ¿Qué biblioteca de Python proporciona soporte para arrays multidimensionales?
   - A. Seaborn.
   - B. Pandas.
   - C. Matplotlib.
   - D. NumPy.

   - **Respuesta:** D. NumPy.
   - **Explicación:** NumPy proporciona soporte para arrays multidimensionales eficientes.

10. ¿Qué hace el método `dropna()` en Pandas?
   - A. Añade valores nulos a un dataframe.
   - B. Elimina filas con valores nulos en un dataframe.
   - C. Llena valores nulos en un dataframe.
   - D. Duplica un dataframe.

   - **Respuesta:** B. Elimina filas con valores nulos en un dataframe.
   - **Explicación:** dropna() elimina registros con valores nulos y se usa en limpieza de datos con Pandas.

## Tema 6

1. ¿Cuál es el primer paso en el diseño de un proyecto práctico de IA?
   - A. Recolección de datos.
   - B. Identificación del problema.
   - C. Selección de algoritmos.
   - D. Implementación del modelo.

   - **Respuesta:** B. Identificación del problema.
   - **Explicación:** El primer paso en un proyecto practico de IA es definir claramente el problema que se quiere resolver.

2. ¿Qué herramienta se menciona para el preprocesamiento de datos en Python?
   - A. Scikit-learn.
   - B. Numpy.
   - C. Pandas.
   - D. TensorFlow.

   - **Respuesta:** C. Pandas.
   - **Explicación:** El ejemplo de preprocesamiento usa Pandas para cargar, limpiar y estructurar datos.

3. ¿Qué técnica se menciona para reducir el sobreajuste en redes neuronales?
   - A. Batch normalization.
   - B. Dropout.
   - C. Data augmentation.
   - D. Cross-validation.

   - **Respuesta:** B. Dropout.
   - **Explicación:** Dropout se menciona como tecnica para reducir el sobreajuste en redes neuronales.

4. ¿Cuál es una práctica recomendada para la colaboración efectiva en equipos de desarrollo de software?
   - A. Evitar el uso de herramientas de gestión.
   - B. Comunicación clara y continua.
   - C. Trabajar de manera independiente.
   - D. Ignorar la documentación.

   - **Respuesta:** B. Comunicación clara y continua.
   - **Explicación:** La guia destaca que la comunicacion efectiva es la base de la colaboracion en equipos de IA.

5. ¿Qué framework se menciona como herramienta para la implementación de modelos de deep learning?
   - A. Hadoop.
   - B. PyTorch.
   - C. Spark.
   - D. H2O.

   - **Respuesta:** B. PyTorch.
   - **Explicación:** PyTorch se menciona como framework para implementar modelos de deep learning junto con TensorFlow.

6. ¿Qué se debe hacer después de entrenar un modelo de IA para asegurarse de su correcto funcionamiento?
   - A. Desplegarlo directamente en producción.
   - B. Evaluarlo con datos de prueba.
   - C. Reiniciar el entrenamiento.
   - D. Ignorar los datos de prueba.

   - **Respuesta:** B. Evaluarlo con datos de prueba.
   - **Explicación:** Despues de entrenar, el modelo debe evaluarse con datos no vistos para comprobar su funcionamiento.

7. ¿Cuál es un ejemplo de problema práctico en desarrollo de software que se puede resolver con IA?
   - A. Optimización de recursos en la nube.
   - B. Clasificación automática de errores en logs.
   - C. Generación automática de código.
   - D. Mejora del rendimiento de bases de datos.

   - **Respuesta:** B. Clasificación automática de errores en logs.
   - **Explicación:** El tema usa la clasificacion automatica de errores en logs como ejemplo de problema de software abordable con IA.

8. ¿Qué es lo que asegura un diseño adecuado de proyectos prácticos de IA?
   - A. Que sean escalables y estén alineados con los objetivos del negocio.
   - B. Que sean fáciles de entender por todos.
   - C. Que utilicen siempre TensorFlow.
   - D. Que se hagan rápidamente.

   - **Respuesta:** A. Que sean escalables y estén alineados con los objetivos del negocio.
   - **Explicación:** Un diseño adecuado busca que el proyecto sea viable, escalable y conectado con objetivos reales.

9. ¿Qué implica la recolección y preparación de datos en un proyecto de IA?
   - A. Recopilación de cualquier tipo de datos disponibles.
   - B. Uso exclusivo de datos ya preprocesados.
   - C. Recolección y estructuración de datos relevantes para el problema.
   - D. Uso de datos generados sintéticamente.

   - **Respuesta:** C. Recolección y estructuración de datos relevantes para el problema.
   - **Explicación:** La preparacion de datos implica obtener datos relevantes, limpiarlos y estructurarlos para entrenar y evaluar el modelo.

10. ¿Qué técnica se menciona para evaluar la generalización de un modelo de IA?
   - A. Data augmentation.
   - B. Regularización L2.
   - C. Validación cruzada.
   - D. Normalización de datos.

   - **Respuesta:** C. Validación cruzada.
   - **Explicación:** La validacion cruzada evalua el rendimiento en distintas particiones y ayuda a estimar la generalizacion.

1. ¿Qué herramienta se menciona para la gestión de proyectos y tareas en un equipo de desarrollo?
   - A. GitHub.
   - B. Trello.
   - C. Jira.
   - D. Confluence.

   - **Respuesta:** C. Jira.
   - **Explicación:** El material menciona Jira como herramienta para gestionar tareas y responsabilidades del equipo.

2. ¿Cuál es el objetivo de la evaluación del modelo en un proyecto de IA?
   - A. Verificar la exactitud del modelo en datos de prueba.
   - B. Probar todos los posibles modelos existentes.
   - C. Implementar el modelo en producción.
   - D. Recolectar más datos para mejorar el modelo.

   - **Respuesta:** A. Verificar la exactitud del modelo en datos de prueba.
   - **Explicación:** La evaluacion comprueba el rendimiento del modelo en datos de prueba o validacion mediante metricas.

3. ¿Qué opción describe una práctica incorrecta en la implementación de modelos de IA?
   - A. Evaluar el modelo en datos no vistos.
   - B. Usar frameworks, como TensorFlow o PyTorch.
   - C. Entrenar el modelo sin pruebas de evaluación.
   - D. Implementar redes neuronales simples para tareas de clasificación.

   - **Respuesta:** C. Entrenar el modelo sin pruebas de evaluación.
   - **Explicación:** Entrenar sin evaluar con datos no vistos es incorrecto porque no permite saber si el modelo generaliza.

4. ¿Qué es esencial para el éxito en la implementación de modelos de IA en aplicaciones del mundo real?
   - A. Precisión y eficiencia del modelo.
   - B. Rapidez en el desarrollo del código.
   - C. Uso de librerías exclusivas de Python.
   - D. Evitar la colaboración en equipo.

   - **Respuesta:** A. Precisión y eficiencia del modelo.
   - **Explicación:** En aplicaciones reales importan tanto el rendimiento predictivo como la eficiencia operativa del modelo.

5. ¿Qué se recomienda hacer en caso de que un modelo de IA no funcione correctamente con nuevos datos?
   - A. Desplegar el modelo tal como está.
   - B. Realizar ajustes y optimización.
   - C. Cambiar el lenguaje de programación.
   - D. Ignorar los nuevos datos.

   - **Respuesta:** B. Realizar ajustes y optimización.
   - **Explicación:** Si el modelo falla con datos nuevos, se recomienda diagnosticar, ajustar hiperparametros, regularizar o recopilar mas datos.

6. ¿Qué técnica se menciona como parte del proceso de ajuste y optimización de un modelo?
   - A. Selección de algoritmos.
   - B. Data augmentation.
   - C. Uso de técnicas de regularización.
   - D. Diseño de interfaces gráficas.

   - **Respuesta:** C. Uso de técnicas de regularización.
   - **Explicación:** La regularizacion, como L2 o dropout, forma parte del ajuste y optimizacion del modelo.

7. ¿Qué problema común en modelos de deep learning puede set mitigado por la capa dropout ?
   - A. Subentrenamiento.
   - B. Overfitting.
   - C. Subestimación de parámetros.
   - D. Ruido en los datos.

   - **Respuesta:** B. Overfitting.
   - **Explicación:** Dropout ayuda a prevenir el sobreajuste al reducir la dependencia de neuronas especificas durante el entrenamiento.

8. ¿Qué fase sigue al entrenamiento del modelo en el desarrollo de proyectos de IA?
   - A. Recolección de más datos.
   - B. Evaluación del modelo.
   - C. Despliegue del modelo.
   - D. Documentación del proceso.

   - **Respuesta:** B. Evaluación del modelo.
   - **Explicación:** Tras el entrenamiento sigue la evaluacion con datos de prueba o validacion.

9. ¿Cuál es una característica clave de la implementación de modelos en PyTorch?
   - A. Simplicidad del proceso.
   - B. Control detallado sobre el entrenamiento.
   - C. Uso limitado en la industria.
   - D. Require menos datos que TensorFlow.

   - **Respuesta:** B. Control detallado sobre el entrenamiento.
   - **Explicación:** PyTorch ofrece un proceso mas explicito y granular, util cuando se necesita control detallado.

10. ¿Qué se debe hacer para mejorar la robustez de un modelo de IA?
   - A. Cambiar el framework.
   - B. Utilizar un optimizador con menor tasa de aprendizaje.
   - C. Recolectar más datos.
   - D. Usar un solo algoritmo en todo el proyecto.

   - **Respuesta:** C. Recolectar más datos.
   - **Explicación:** El material menciona la recoleccion de mas datos como una forma de mejorar la robustez cuando el modelo no generaliza bien.
