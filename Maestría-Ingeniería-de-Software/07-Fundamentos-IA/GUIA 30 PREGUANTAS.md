# Guía De Estudio: Fundamentos De Inteligencia Artificial

## I. Introducción Al Aprendizaje Automático

1. **¿Qué es el aprendizaje automático?**  
    _Respuesta:_ Un proceso de inducción del conocimiento.  
    _Justificación:_ La definición clásica señala que el aprendizaje automático automatiza el método científico aplicando métodos matemáticos para extraer conocimiento de datos. De hecho, la Wikipedia en español describe que el aprendizaje automático es “por lo tanto un proceso de inducción del conocimiento”. Esto coincide con la opción C, enfatizando que ML infiere conocimiento (induce) a partir de la información disponible.
    
2. **¿En qué categorías principales se divide el aprendizaje automático?**  
    _Respuesta:_ Supervisado, no supervisado y por refuerzo.  
    _Justificación:_ Los tres enfoques fundamentales del ML son el supervisado, no supervisado y por refuerzo. La misma Wikipedia indica que **“el aprendizaje por refuerzo es el más general entre las tres categorías”**, lo que implica que las tres categorías principales del aprendizaje automático son supervisado, no supervisado y refuerzo. Esto coincide exactamente con la opción B.
    
3. **¿Cuál es la base del aprendizaje supervisado?**  
    _Respuesta:_ Inferir una respuesta con base en datos etiquetados previamente.  
    _Justificación:_ El aprendizaje supervisado se caracteriza por utilizar conjuntos de datos **etiquetados** para entrenar el modelo. Oracle lo define claramente: _“El aprendizaje supervisado es una forma de ML que utilize conjuntos de datos etiquetados para entrenar algoritmos”_. En otras palabras, el modelo infiere la respuesta apoyándose en ejemplos con etiquetas conocidas, tal como indica la opción A.
    
4. **¿Qué información proporciona una matriz de confusión?**  
    _Respuesta:_ Una relación entre las clases observadas (reales) y las predichas.  
    _Justificación:_ Una matriz de confusión es una tabla que muestra cómo se distribuyen las predicciones del modelo respecto a las clases reales. Por ejemplo, en ella las filas suelen set las clases verdaderas y las columnas las clases predichas. Como explica un recurso didáctico, **“Formalmente, una matriz de confusión es una tabla en la que… las filas representan las clases reales… y las columnas las clases predichas por el modelo”**. Esto ilustra que la matriz relaciona las etiquetas reales con las predicciones, coincidiendo con la opción B.
    
5. **En problemas de clasificación, ¿qué indica la métrica de precisión (precision)?**  
    _Respuesta:_ Cuántas veces está en lo cierto el modelo cuando predice la clase positiva.  
    _Justificación:_ La precisión (precision) mide el acierto del modelo **entre las predicciones positivas**. Es decir, de todas las veces que el modelo predice la clase positiva, qué fracción son correctas. Por ejemplo, Google Developers define la precisión como la proporción de predicciones positivas que son realmente positivas. Esto implica que precision refleja **cuán confiable es el modelo al afirmar “positivo”**, por lo que la opción A es la correcta.

## II. Fundamentos De Redes Neuronales Y Arquitecturas

1. **¿Qué tipo de red neuronal es el perceptrón?**  
    _Respuesta:_ Una red de una sola capa.  
    _Justificación:_ El perceptrón de Rosenblatt es la red neuronal más simple, compuesta esencialmente por una sola capa de salida. En la literatura se le denomina _“single-layer perceptron”_, es decir, una red feedforward con una sola capa neuronal. Por ejemplo, Wikipedia en inglés describe al _single-layer perceptron_ como _“the simplest feedforward neural network”_. Esto confirma que corresponde a una red de una sola capa, tal como indica la opción C.
    
2. **¿Cuál es el objetivo del aprendizaje en una red neuronal simple?**  
    _Respuesta:_ Seleccionar los pesos que mejor se ajusten a las entradas y salidas definidas a priori.  
    _Justificación:_ Entrenar una red neuronal consiste en ajustar iterativamente sus pesos para que las predicciones se acerquen a las salidas deseadas. En otras palabras, se buscan los valores de peso que mejor ajusten los datos de entrada a las salidas esperadas. Como indica Google Cloud, durante el entrenamiento “la red ajusta sus pesos… para minimizar los errores entre sus predicciones y los valores reales”. Es decir, se trata de encontrar los pesos óptimos para el conjunto de entrenamiento, tal como afirma la opción B.
    
3. **¿Cuál es la principal característica de las redes neuronales recurrentes (RNN)?**  
    _Respuesta:_ Sus salidas alimentan las entradas formando un bucle (memoria).  
    _Justificación:_ Las RNN incorporan bucles de retroalimentación, lo que les permite “recordar” información de pasos anteriores. Tienen un estado interno que se retroalimenta en cada paso temporal, actuando como una memoria. IBM describe que las RNN “crean un bucle de realimentación al pasar el estado oculto de un paso temporal al siguiente. El estado oculto actúa como una memoria que almacena información sobre entradas anteriores”. Esto confirma que su rasgo distintivo es ese bucle de memoria, como señala la opción A.
    
4. **¿Qué tipo de redes son las más utilizadas para el reconocimiento de imágenes y patrones espaciales?**  
    _Respuesta:_ Redes neuronales convolucionales (CNN).  
    _Justificación:_ Las CNN están especialmente diseñadas para procesar datos con estructura espacial, como imágenes. Sus capas convolucionales detectan automáticamente características espaciales y patrones de la imagen. Por ejemplo, IBM señala que las redes convolucionales _“se utilizan con mayor frecuencia para tareas de clasificación y visión por computadora”_, destacando su aplicación en reconocimiento de imágenes y objetos. Esto coincide con la opción B.
    
5. **¿Qué es una red generativa antagónica (GAN)?**  
    _Respuesta:_ Un sistema de dos redes (generativa y discriminativa) que compiten para crear datos nuevos.  
    _Justificación:_ Una GAN consiste en dos redes neuronales que “compiten” entre sí: el generador intenta crear muestras falsas realistas, mientras que el discriminador trata de distinguir entre datos reales y generados. IBM lo resume así: _“una GAN es un modelo… donde **dos redes neuronales** trabajan en oposición: una genera datos y la otra evalúa si los datos son reales o generados”_. Esta descripción coincide exactamente con la opción B.

## III. Procesamiento Del Lenguaje Natural (NLP)

1. **¿Qué es el procesamiento del lenguaje natural (NLP)?**  
    _Respuesta:_ Un área interdisciplinaria que permite a las máquinas procesar y entender el lenguaje humano.  
    _Justificación:_ El NLP es una rama de la IA que combina lingüística, computación y otros campos para que las máquinas entiendan el lenguaje humano. Según SAS, _“El procesamiento del lenguaje natural (NLP) es una rama de la IA que ayuda a las computadoras a entender, interpretar y manipular el lenguaje humano”_. En esencia, permite cerrar la brecha entre la comunicación humana y la comprensión de las máquinas, tal como indica la opción B.
    
2. **¿En qué consiste la técnica de tokenización?**  
    _Respuesta:_ Dividir un texto en unidades básicas como palabras, frases o símbolos.  
    _Justificación:_ La tokenización segmenta un texto en “tokens” elementales (como palabras o caracteres) para facilitar su procesamiento. Un tutorial aclara que _“Tokenizar significa dividir el texto en unidades más pequeñas que el sistema pueda manipular con mayor facilidad”_. En NLP, los tokens suelen set palabras o signos básicos. Así, la opción A describe correctamente el objetivo de la tokenización.
    
3. **¿Cuál es el propósito principal de eliminar "stopwords" en NLP?**  
    _Respuesta:_ Reducir el ruido eliminando palabras comunes (artículos, preposiciones) que no aportan significado clave.  
    _Justificación:_ Las “stopwords” son palabras muy frecuentes (por ejemplo “el”, “de”, “y”) que suelen aportar poco valor semántico. Eliminar estas palabras busca reducir el ruido en el análisis de texto. Como explica un recurso educativo, quitar stopwords ayuda a “eliminar palabras comunes que no aportan un significado significativo, reduciendo el ruido y mejorando la relevancia del análisis”. Esto coincide con la opción A.
    
4. **¿Qué técnica reduce las palabras a su forma base o lema (ej. "corriendo" -> "correr")?**  
    _Respuesta:_ Lematización.  
    _Justificación:_ La lematización transforma cada palabra a su lema (forma de diccionario). Diferente del stemming (que corta derivaciones de forma cruda), la lematización produce una palabra base lingüísticamente válida. Como señala IBM, la lematización “reduce las formas flexionadas de las palabras a su forma de diccionario, también conocida como ‘lema’”. Por eso es la lematización (opción B) la que lleva “corriendo” a “correr”.
    
5. **¿Qué describe mejor el etiquetado morfosintáctico (POS tagging)?**  
    _Respuesta:_ Asignar una categoría gramatical (sustantivo, verbo, etc.) a cada palabra.  
    _Justificación:_ El POS tagging consiste en etiquetar cada término con su categoría gramatical. Un curso explica: _“la tarea denominada etiquetado morfosintáctico (POS-tagging) consiste en asignar a cada palabra de un texto una categoría gramatical”_. Esto coincide exactamente con la opción B.

## IV. Python Y Frameworks Para IA

1. **¿Por qué Python es el lenguaje predominante en el desarrollo de IA?**  
    _Respuesta:_ Por su sintaxis clara y su extensa gama de bibliotecas especializadas (NumPy, Pandas, etc.).  
    _Justificación:_ Python es popular en IA principalmente por su sintaxis legible y la gran cantidad de librerías disponibles. Python facilita la programación y cuenta con potentes bibliotecas de ciencia de datos e IA. Según Real Python, _“Python se distingue por su sintaxis clara y concisa”_ y por su “extenso ecosistema de bibliotecas especializadas en IA”. Esto corresponde con la opción C.
    
2. **¿Cuál es la función principal de la biblioteca NumPy en IA?**  
    _Respuesta:_ Cálculos numéricos y manejo eficiente de arrays multidimensionales.  
    _Justificación:_ NumPy es la librería estándar de Python para operaciones matemáticas y manejo de datos numéricos en forma de arrays n-dimensionales. Permite cálculos rápidos en vectors y matrices. Tal y como señala un recurso, NumPy _“es utilizado principalmente para cálculos numéricos y operaciones matemáticas avanzadas… debido a su eficiencia en el manejo de arrays multidimensionales”_. Esto coincide con la opción B.
    
3. **¿Qué herramienta de Python es ideal para la manipulación y análisis de datos tabulares (DataFrames)?**  
    _Respuesta:_ Pandas.  
    _Justificación:_ Pandas proporciona la estructura `DataFrame` y funciones para manipular datos en tablas (similares a hojas de cálculo). Fue diseñada para facilitar el manejo de datos tabulares. Por ejemplo, la documentación indica que _“Pandas es una librería diseñada para facilitar la manipulación y el análisis de datos estructurados, especialmente en formato tabular”_. Por ello Pandas (opción B) es la herramienta idónea para DataFrames.
    
4. **¿Qué diferencia clave tiene PyTorch frente a las versiones iniciales de TensorFlow?**  
    _Respuesta:_ Utilize grafos computacionales dinámicos, facilitando la depuración.  
    _Justificación:_ PyTorch implementa grafos de cómputo dinámicos (define-by-run), lo que permite construir y modificar el grafo durante la ejecución. Esto simplifica la depuración. Como explica un experto: _“La razón es que el grafo computacional de PyTorch es dinámico… mientras que en TensorFlow es estático”_, por lo cual PyTorch resulta más fácil de debuggear. Esto es precisamente la opción B.
    
5. **¿Qué biblioteca proporciona herramientas esenciales para aprendizaje automático "clásico" (regresión, SVM, k-NN)?**  
    _Respuesta:_ Scikit-learn.  
    _Justificación:_ Scikit-learn es la librería de referencia en Python para algoritmos de ML clásicos como regresión lineal, máquinas de soporte vectorial, k-NN, árboles, etc. Su documentación official indica que incluye “módulos esenciales para la clasificación, la regresión, [y más]”. En consecuencia, Scikit-learn (opción C) es la que agrupa esas herramientas clásicas.

## V. Diseño Y Gestión De Proyectos De IA

1. **¿Cuál es el primer paso fundamental en el diseño de un proyecto práctico de IA?**  
    _Respuesta:_ Identificación y definición clara del problema.  
    _Justificación:_ El primer paso siempre es entender y formular el problema a resolver. IBM destaca que _“el primer paso es identificar los problemas u oportunidades que [la IA] puede abordar”_. Definir claramente el problema permite orientar todo el proyecto, por lo que la opción B es la correcta.
    
2. **¿Qué técnica se utilize para evitar que un modelo “memorice” los datos de entrenamiento (overfitting)?**  
    _Respuesta:_ Uso de capas de Dropout o técnicas de regularización.  
    _Justificación:_ Para prevenir el sobreajuste se aplican métodos de regularización. En redes neuronales es común usar **Dropout** (apagar aleatoriamente neuronas) y penalizaciones L1/L2. Como señala un material didáctico, técnicas como **Dropout** y regularización L1/L2 permiten “mejorar la generalización de los modelos y prevenir el sobreajuste”. Esto coincide con la opción B.
    
3. **¿Para qué sirve la validación cruzada (cross-validation)?**  
    _Respuesta:_ Para evaluar la robustez y capacidad de generalización del modelo en diferentes particiones de datos.  
    _Justificación:_ La validación cruzada divide el dataset en múltiples particiones para entrenar y validar el modelo repetidamente, proporcionando una estimación más fiable de su rendimiento en datos nuevos. Como explica Ultralytics, es “un procedimiento estadístico de remuestreo robusto… para evaluar el rendimiento de modelos” y asegurar la capacidad de generalización a nuevos datos. En resumen, se usa para comprobar cuán robusto es el modelo al variar los datos, coincidiendo con la opción B.
    
4. **¿Qué debe hacerse después de entrenar un modelo para verificar su rendimiento real?**  
    _Respuesta:_ Evaluarlo con un conjunto de datos de prueba (test) no vistos durante el entrenamiento.  
    _Justificación:_ Después del entrenamiento se debe comprobar el modelo en un conjunto independiente de datos nunca usados antes. Según Ultralytics, probar un modelo implica verificarlo con datos “nunca antes vistos” para ver cómo funciona en condiciones realistas. En otras palabras, se utilize un conjunto de prueba ajeno al entrenamiento, tal como indica la opción B.
    
5. **¿Qué herramienta se menciona para la gestión de tareas y colaboración en equipos de desarrollo?**  
    _Respuesta:_ Jira.  
    _Justificación:_ Entre las opciones de gestión de proyectos para equipos técnicos, Jira es la más enfocada en desarrollo de software. El blog de Slack lo describe: _“Jira es una herramienta potente y flexible diseñada especialmente para equipos de desarrollo… [con] seguimiento de problemas, planificación ágil e informes detallados”_. Esto confirma la opción C.

## VI. Ética En la Inteligencia Artificial

1. **¿Cuál es el principio ético que busca evitar que la IA perpetúe desigualdades sociales?**  
    _Respuesta:_ Sesgos y equidad.  
    _Justificación:_ El principio asociado a la justicia social en IA es la equidad (fairness). Por ejemplo, la UNESCO establece como principio fundamental la **equidad y no discriminación**, recomendando que los actores de IA “promuevan la justicia social, salvaguarden la equidad y luchen contra todo tipo de discriminación”. Esto implica evitar que los sesgos históricos se reproduzcan, justamente la opción C.
    
2. **¿Qué implica el principio de transparencia en los sistemas de IA?**  
    _Respuesta:_ Que los procesos y decisiones de los algoritmos deben set comprensibles y auditable.  
    _Justificación:_ La transparencia exige entender cómo funcionan los modelos de IA. Por ejemplo, una fuente de gobernanza señala que _“las decisiones de IA deben set comprensibles para que los usuarios y reguladores puedan ver cómo se generan los resultados”_. En otras palabras, los procedimientos y decisiones internas deben poder set revisados y entendidos, tal como indica la opción B.
    
3. **¿Cuál es una fuente común de sesgo en los modelos de IA?**  
    _Respuesta:_ Datos de entrenamiento desbalanceados o que reflejan prejuicios históricos.  
    _Justificación:_ Gran parte del sesgo algorítmico proviene de los propios datos con los que se entrena el modelo. IBM advierte que los modelos _“absorben los sesgos de la sociedad que pueden estar incrustados en las montañas de datos con los que se entrenan”_, y que “la recopilación de datos con sesgos históricos que reflejen desigualdad social puede resultar perjudicial”. Esto corresponde con la opción B.
    
4. **¿Qué principio exige que la IA se utilice para promover el bienestar y minimizar daños?**  
    _Respuesta:_ Beneficencia.  
    _Justificación:_ El principio ético de **beneficencia** (para el “bien mayor”) estipula que la IA debe desarrollarse con fines beneficiosos. Ethics Unwrapped define el Principio de Beneficencia afirmando que “la IA debe desarrollarse y aplicarse para mejorar el bienestar de nuestro planeta y su gente”. Esto corresponde a la opción A.
    
5. **¿A qué se refiere el término "modelo de caja negra"?**  
    _Respuesta:_ Un sistema cuya toma de decisiones interna es opaca y difícil de interpretar por humanos.  
    _Justificación:_ Un “modelo de caja negra” es aquel cuyos procesos internos no se pueden examinar fácilmente. Por ejemplo, IBM describe que _“los usuarios no saben cómo un modelo de caja negra toma las decisiones que toma”_. Esto significa que, aunque se vean las entradas y salidas, el funcionamiento interno permanece oculto, como indica la opción B.

## Referencias

- **Wikipedia:** _Aprendizaje automático_.
- **Oracle (Cloud AI):** _¿Qué es el aprendizaje supervisado?_.
- Juan Barrios: _Matriz de confusión y sus métricas_.
- Google Developers (Clasificación): _Precisión y Recall_.
- **Wikipedia:** _Perceptrón_ (feedforward single-layer perceptron).
- Google Cloud: _¿Qué es una red neuronal?_.
- IBM Developer (NLP): _¿Qué son las redes neuronales recurrentes?_.
- IBM Developer: _¿Qué son las redes neuronales convolucionales?_.
- IBM (Think): _¿Qué es una GAN?_.
- SAS: _¿Qué es NLP?_ (definición general).
- TutorialesProgramaciónYA: _Tokenización en NLP_.
- OpenWebinars: _Stopwords en NLP_.
- IBM (Think): _Stemming vs Lematización_.
- Programación en Python (Google Sites): _Etiquetado morfosintáctico (POS)_.
- Real Python: _¿Por qué Python para IA?_.
- Pontia: _Introducción a NumPy_.
- ProjectPythia: _¿Qué es Pandas?_.
- StackOverflow Blog: _Ventajas de PyTorch (grafos dinámicos)_.
- IBM (Think): _¿Qué es Scikit-learn?_.
- IBM Cloud Blog: _Introducción a proyectos de IA_.
- Curso AI – UCEL (online): _Overfitting y regularización_.
- Ultralytics (YOLO Docs): _Cross-Validation en ML_.
- Ultralytics (YOLO Docs): _Pruebas de modelos_.
- Blog Slack ES: _7 mejores herramientas de gestión de proyectos_.
- UNESCO: _Recomendación sobre ética de la IA (Equidad)_.
- BigID Blog: _Principios de gobernanza de IA (Transparencia)_.
- IBM (Think): _¿Qué es el sesgo de IA?_.
- Ethics Unwrapped (UT Austin): _Principio de Beneficencia en IA_.
- IBM (Think): _¿Qué es la IA de caja negra?_.