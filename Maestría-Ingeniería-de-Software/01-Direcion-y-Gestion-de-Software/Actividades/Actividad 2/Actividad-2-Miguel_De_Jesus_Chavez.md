# Informe De Análisis De Riesgos Del Proyecto PennyWallet (PW)

Este informe aplica una **evaluación de riesgos** al proyecto PennyWallet (PW), en base a la información proporcionada. Se incluyen la **matriz de probabilidad e impacto** para priorizar los riesgos identificados, así como el análisis detallado de cada uno con su tipo, punto de ruptura, acciones preventivas y acciones mitigantes.

La matriz de probabilidad e impacto es **una herramienta esencial** para la gestión de riesgos, pues permite visualizar y priorizar las amenazas según su probabilidad de ocurrencia y el impacto potencial sobre los objetivos. En este caso, cada riesgo se califica numéricamente según la escala proporcionada (por ejemplo, _Alta = 0,7_, _Muy Alta = 0,9_, etc.). Una vez asignados esos valores, **la severidad del riesgo** se obtiene multiplicando probabilidad por impacto, generando una “puntuación de gravedad”. Esta puntuación sirve para priorizar los riesgos de mayor a menor exposición. Adicionalmente, se define el **umbral de riesgo** o punto de ruptura como el nivel aceptable de variación; si se supera este umbral es imperativo activar medidas correctivas.

## Identificación De Los Riesgos

A partir de la descripción del proyecto se han identificado cuatro riesgos principales:

·         **R1 (Complejidad algorítmica):** Riesgo de que el código desarrollado no satisfaga los requisitos debido a la excesiva complejidad algorítmica. La vieja biblioteca era muy compleja y sufrió errores graves en su primera versión. Es un riesgo técnico crítico, ya que un error en los cálculos financieros puede comprometer el sistema completo.

·         **R2 (Calendario y temporización):** Riesgo de incumplimiento de plazo. El nuevo desarrollo debe concluirse justo a tiempo para iniciar un proyecto estratégico con un cliente, sin posibilidad de retrasos adicionales. El proyecto tiene un margen del 20% sobreestimado, pero cualquier retraso significativo puede llevar a la cancelación contractual.

·         **R3 (Disponibilidad de experto financiero):** Riesgo de falta de conocimiento experto en finanzas. Los expertos financieros de la empresa solo dedican un tiempo marginal al proyecto (salvo una persona inicialmente) y ninguno trabajó en la biblioteca original. Si surge un problema financiero complejo, puede set difícil resolverlo sin un experto disponible.

·         **R4 (Ajuste del diseño de la API):** Riesgo de que el diseño de la nueva API no sea adecuado. La biblioteca debe set reutilizable en contextos muy distintos, por lo que un mal diseño podría impedir su adaptación futura. Es un riesgo de arquitectura o de requerimientos de reutilización.

## Priorización De Riesgos (Matriz De Probabilidad E Impacto)

Se estiman para cada riesgo la probabilidad y el impacto según las escalas dadas, luego se calcula la **exposición** (producto P×I) y se asigna una prioridad. El cuadro siguente resume estos valores:

|**Riesgo**|**Probabilidad**|**Impacto**|**Exposición** (P×I)|**Prioridad**|
|---|---|---|---|---|
|**R1:** Adecuación del código|Alta (0.7)|Muy Alto (0.8)|0.56|Alta|
|**R2:** Calendario/Plazos|Alta (0.8)|Muy Alto (0.8)|0.64|Muy Alta|
|**R3:** Experto financiero disponible|Media (0.5)|Alto (0.4)|0.20|Media|
|**R4:** Diseño de la API|Media (0.5)|Medio (0.3)|0.15|Baja|

·         **R2 (Calendario)** presenta la exposición más alta (0.64) por la combinación de probabilidad alta y un impacto muy alto, por lo que es el riesgo más prioritario. Un retraso en los plazos puede desencadenar la cancelación del proyecto.

·         **R1 Adecuación del código** es el siguiente con exposición 0.56; es un riesgo también muy severo y de alta prioridad, pues los errores algorítmicos afectarían la funcionalidad crítica.

·         **R3 y R4** tienen exposiciones bajas (0.20 y 0.15), por lo que sus prioridades se consideran medias o bajas; sin embargo, deben monitorearse y gestionarse.

Este enfoque está basado en la matriz de riesgo descrita en la literatura de gestión de proyectos. Una vez ordenados los riesgos por exposición, se asignan recursos de acuerdo a su prioridad: los riesgos más altos (R2, R1) requieren planes de respuesta más rigurosos.

## Análisis Detallado De Cada Riesgo

A continuación se detalla el análisis de cada riesgo, incluyendo su **tipo**, **punto de ruptura** y acciones preventivas/mitigantes:

#### ·         Riesgo R1: Adecuación del código (complejidad algorítmica)

o   **Tipo de riesgo:** Técnico – relacionado con la complejidad de implementación de algoritmos financieros.

o   **Punto de ruptura:** Se considera crítico si los errores de cálculo superan un nivel tolerable o si la librería no cumple los requisitos esenciales. Por ejemplo, si alguna fórmula financiera básica (p.ej. cálculo de interés o amortización) produce resultados incorrectos más allá de una tolerancia acceptable (p.ej. afectando la precisión en ≥5% de los casos), el proyecto entraría en crisis. Este umbral actúa como alarma que indica que se deben tomar medidas inmediatas.

o   **Acciones preventivas:**

§  Revisiones de código y pruebas continuas desde etapas tempranas (TDD o pruebas unitarias exhaustivas).

§  Modelado o prototipos previas de algoritmos complejos antes de la implementación definitiva.

§  Formación o incorporación de personal con experiencia en dominios financieros similares.

§  Validación temprana con los documentos algorítmicos existentes (ej. comparar con la biblioteca antigua para casos de prueba básicos).  
  

o   **Acciones mitigantes/correctivas:**

§  Si se detectan errores complejos, asignar recursos extra (por ejemplo, consultoría externa en finanzas cuantitativas o auditoría de algoritmos) para corregir.

§  Ajustar la planificación para incluir fases de depuración adicionales (por ejemplo, más tiempo para pruebas integradas antes de la entrega).

§  En casos extremos, simplificar temporalmente o postergar funciones no críticas mientras se corrigen los algoritmos principales.  
  

#### ·         Riesgo R2: Calendario y temporización

o   **Tipo de riesgo:** De planificación/cronograma – riesgo de incumplir los plazos críticos del proyecto.

o   **Punto de ruptura:** Se define cuando se consume la holgura total estimada. Con un 20% de holgura disponible, el umbral se alcanzaría ante un retraso que supere dicho margen (p.ej., un retraso de más de X semanas, dependiendo de la duración total prevista). Siguiendo ejemplos de buenas prácticas, cualquier retraso en el cronograma que exceda los días de holgura activa medidas correctivas (por ejemplo, si el proyecto se retrasa 2 semanas sobre el buffer asignado). Esto se considera crítico porque el contrato con el cliente no permite demoras; superar el umbral implicaría casi con seguridad la cancelación del proyecto.

o   **Acciones preventivas:**

§  Desglosar el proyecto en hitos intermedios con seguimiento riguroso (comunicación diaria/semanal del progreso).

§  Aplicar metodologías ágiles o iterativas que permitan detectar retrasos tempranamente.

§  Asignar recursos adicionales en tareas críticas (p.ej. desarrolladores senior o trabajo extra en periodos puntuales) para asegurar cumplimiento de hitos.

§  Mantener la holgura de forma conservadora y revisar continuadamente la estimación (reajustando estimaciones si surgen riesgos adicionales).  
  

o   **Acciones mitigantes/correctivas:**

§  En caso de desvío, priorizar funcionalidades esenciales reduciendo alcance no crítico (p.ej., entregar mínimo viable para que el proyecto del cliente pueda iniciarse).

§  Adicionales horas extras planificadas o contratación temporal de personal para acelerar desarrollo.

§  Re-negociar entregables parciales con el cliente (si fuera possible) antes de incumplir el plazo total.

§  Activar un plan de acción rápido (por ejemplo, concentrar al equipo en resolver tareas pendientes críticas).  
  

#### ·         Riesgo R3: No disponibilidad de experto financiero

o   **Tipo de riesgo:** De recurso humano/conocimiento – riesgo asociado a la falta de dominio experto en finanzas.

o   **Punto de ruptura:** Ocurre cuando surge un problema financiero complejo (por ejemplo, un cálculo de gran envergadura o un matiz regulatorio) que el equipo no puede resolver sin un experto especializado. Dado que solo un experto está inicialmente disponible, el umbral se cruzaría si ese único recurso deja el proyecto o se ve desbordado antes de solucionar un problema crítico. En tal caso, la calidad del producto o el cumplimiento de requisitos financieros estaría comprometido.

o   **Acciones preventivas:**

§  Capturar el conocimiento del experto disponible en documentación detallada (transformar know-how en especificaciones claras).

§  Realizar sesiones de capacitación interna para el equipo de desarrollo en conceptos financieros básicos relevantes.

§  Planificar la possible contratación o asignación de un experto externo o consultoría temporal en caso necesario.

§  Asegurar que la única persona experta trabaje estrechamente con el equipo en la fase inicial para transferir conocimiento y revisar las primeras versiones del código.  
  

o   **Acciones mitigantes/correctivas:**

§  Si surge un problema mayor sin experto disponible, buscar soporte en instituciones externas (consultores financieros, entidades académicas o proveedores de outsourcing) para resolver dudas puntuales.

§  Derivar components de riesgo hacia un área de menor prioridad hasta conseguir apoyo (p.ej., aislar la lógica financiera compleja y concentrarse primero en la parte técnica).

§  Reprogramar temporalmente el plan (dentro del margen del 20%) para dedicar más tiempo a análisis o pruebas con expertos externos antes de continuar.

§  Utilizar herramientas de validación numérica (simuladores, software existente) para contrastar resultados cuando no haya experto que valid manualmente.  
  

#### ·         Riesgo R4: Problemas en el diseño de la API (reutilización)

o   **Tipo de riesgo:** De diseño/arquitectura – riesgo de que la API diseñada no sea suficientemente genérica o flexible para reutilización en contextos variados.

o   **Punto de ruptura:** Se identifica cuando se comprueba que la nueva librería no puede adaptarse a un caso de uso previsto del proyecto del cliente, o que require reescritura extensiva. Por ejemplo, si al integrar la API en un nuevo escenario se necesita modificar código central, se habría cruzado el umbral, indicando que el diseño actual no satisface el requerimiento de reutilización.

o   **Acciones preventivas:**

§  Realizar un diseño inicial mediante consultas a futuros usuarios o proyectos que usarán la API para asegurar cubrir distintos casos.

§  Utilizar principios de diseño modular y de patrones (p.ej., interfaces claras, extensibilidad) para facilitar la reutilización.

§  Hacer revisiones de diseño con distintos stakeholders (desarrolladores de otros proyectos, arquitectos, etc.) antes de implementarla totalmente.

§  Planificar iteraciones de prototipado de la API y pruebas de integración con módulos de ejemplo para verificar su flexibilidad.  
  

o   **Acciones mitigantes/correctivas:**

§  Si se detectan limitaciones en la API, introducir abstracciones o adaptadores para acomodar casos no previstos (por ejemplo, cambios en la interfaz o variantes de configuración).  
  

§  Permitir cierta personalización (parámetros configurables) en la versión final si se confirman necesidades específicas no previstas.

§  Documentar claramente las limitaciones encontradas y planificar una possible segunda versión o parche futuro que mejore la flexibilidad, dedicando tiempo del desarrollo a reestructurar aquellas partes críticas.

## Conclusión

En base al análisis anterior, **la prioridad máxima recae en R2 y R1**, pues una falla en plazos o en precisión algorítmica puede comprometer el proyecto completo. Los riesgos R3 y R4 son de prioridad media-baja según su exposición, pero también requieren monitoreo y medidas oportunas. La **matriz de probabilidad-impacto** ha servido para ordenar estos riesgos de acuerdo a su exposición. Para cada riesgo se han propuesto acciones **preventivas** que tratan de evitar su ocurrencia (o reducir su probabilidad) y acciones **mitigantes/correctivas** para minimizar el impacto en caso de materializarse. El establecimiento de **umbrales de riesgo** (puntos de ruptura) permite saber cuándo pasar a la fase de acción inmediata). Siguiendo este plan de gestión de riesgos, el equipo puede asignar recursos y monitorear continuamente el advance, garantizando así que los riesgos más críticos reciban la atención necesaria para la protección del proyecto.