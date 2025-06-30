# Informe De Análisis De Riesgos Del Proyecto PennyWallet

Este informe es un **evaluación de riesgos** para el proyecto PennyWallet (**PW**), en base a la información proporcionada sobre el trasfondo de la situación para la construcción del proyecto. Se incluyen la **matriz de probabilidad e impacto** para priorizar los riesgos identificados, así como el análisis detallado de cada uno con su tipo, punto de ruptura, acciones preventivas y acciones mitigantes.

La matriz de probabilidad e impacto es una herramienta para la gestión de riesgos, pues permite visualizar y priorizar las amenazas según su probabilidad de ocurrencia y el impacto potential sobre los objetivos. En este caso, cada riesgo se califica numéricamente según la escala proporcionada (por ejemplo, _baja = 0,1_, _Muy Alta = 0,9_, etc.). Una vez asignados esos valores, **la severidad del riesgo** se obtiene multiplicando probabilidad por impacto, generando una “puntuación de gravedad”. Esta puntuación sirve para priorizar los riesgos de mayor a menor exposición. 

## Identificación De Los Riesgos

A partir de la descripción del proyecto hemos identificado cuatro riesgos principales:

·         **R1 (La complejidad algorítmica):** Riesgo de que el código desarrollado no satisfaga los requisitos debido a la complejidad algorítmica. Es un riesgo técnico crítico, ya que un error en los cálculos financieros puede comprometer el sistema completo.

·         **R2 (Calendario y temporización):** Riesgo de incumplimiento de plazo. El proyecto tiene un margen del 20% sobreestimado, pero cualquier retraso significativo puede llevar a la cancelación contractual.

·         **R3 (Disponibilidad de experto financiero):** Riesgo de falta de conocimiento experto en finanzas. Los expertos financieros de la empresa solo dedican un tiempo marginal al proyecto (salvo una persona inicialmente) y ninguno trabajó en la biblioteca original. Si surge un problema financiero complejo, puede set difícil resolverlo sin un experto disponible.

·         **R4 (Ajuste del diseño de la API):** Riesgo de que el diseño de la nueva API no sea adecuado. La biblioteca debe set reutilizable en contextos muy distintos, por lo que un mal diseño podría impedir su adaptación futura. Es un riesgo de arquitectura o de requerimientos de reutilización.

## Priorización De Riesgos (Matriz De Probabilidad E Impacto)

Se estiman para cada riesgo la probabilidad y el impacto según las escalas dadas, luego se calcula la **exposición** (producto P×I) y se asigna una prioridad. El cuadro siguente resume estos valores:

| **Riesgo**                            | **Probabilidad** | **Impacto**    | **Exposición** (P×I) | **Prioridad** |
| ------------------------------------- | ---------------- | -------------- | -------------------- | ------------- |
| **R2:** Calendario/Plazos             | Alta (0.8)       | Muy Alto (0.8) | 0.64                 | Muy Alta      |
| **R1:** Adecuación del código         | Alta (0.7)       | Muy Alto (0.8) | 0.56                 | Alta          |
| **R3:** Experto financiero disponible | Media (0.5)      | Alto (0.4)     | 0.20                 | Media         |
| **R4:** Diseño de la API              | Media (0.5)      | Medio (0.3)    | 0.15                 | Baja          |

## Análisis Detallado De Cada Riesgo

### · Riesgo R1: Adecuación Del Código (complejidad algorítmica)

o   **Tipo de riesgo:** Técnico – Esta relacionado con la complejidad de implementación de algoritmos financieros.

o   **Punto de ruptura:** Se considera crítico dado a que a los errores de por la implementation de nuevo Código o migración de algoritmos de código legacy a código nuevo en c++ podrían superan un nivel tolerable o si la librería nueva no cumple los requisitos esenciales. Por ejemplo, si alguna fórmula financiera básica (p.ej. cálculo de interés o amortización) produce resultados incorrectos durante las pruebas (p.ej. afectando la precisión en ≥5% de los casos), el proyecto podría entraría en crisis. Este umbral actúa como alarma que indica que se deben tomar medidas inmediatas.

o   **Acciones preventivas:**

- Revisiones de código y pruebas continuas desde etapas tempranas (TDD o pruebas unitarias exhaustivas).
- Modelado o prototipos previas de algoritmos complejos antes de la implementación definitiva.
- Formación o incorporación de personal con experiencia en dominios financieros similares.
- Revision exhausta con los documentos algorítmicos existentes.  

o   **Acciones mitigantes/correctivas:**

- Si se detectan errores complejos, asignar recursos extra (por ejemplo, consultoría externa en finanzas o auditoría de algoritmos) para corregir.
- Ajustar la planificación para incluir fases de depuración adicionales (por ejemplo, más tiempo para pruebas integradas antes de la entrega).
- En casos extremos, simplificar temporalmente o postergar funciones no críticas mientras se corrigen los algoritmos principales.  

### · Riesgo R2: Calendario Y Temporización

o   **Tipo de riesgo:** De planificación/cronograma – riesgo de incumplir los plazos críticos del proyecto.

o   **Punto de ruptura:** el punto de ruptura define cuando se consume la holgura total estimada. Con un 20% de holgura disponible, el umbral se alcanzaría ante un retraso que supere el margen (p.ej., un retraso de más de X semanas, dependiendo de la duración total prevista). Esto se considera crítico porque el contrato con el cliente no permite demoras; superar el umbral implicaría la cancelación del proyecto.

o   **Acciones preventivas:**

- Desglosar el proyecto en hitos intermedios con seguimiento riguroso (comunicación diaria/semanal del progreso).
- Aplicar metodologías ágiles o iterativas que permitan detectar retrasos tempranamente.
- Asignar recursos adicionales en tareas críticas (p.ej. desarrolladores senior o trabajo extra en periodos puntuales) para asegurar cumplimiento de los hitos.

o   **Acciones mitigantes/correctivas:**

- En caso de desvío, priorizar funcionalidades esenciales reduciendo alcance no crítico (p.ej., entregar mínimo viable para que el proyecto del cliente pueda iniciarse).
- Adicionales horas extras planificadas o contratación temporal de personal para acelerar desarrollo.
- Activar un plan de acción rápido (por ejemplo, concentrar al equipo en resolver tareas pendientes críticas).  

### · Riesgo R3: No Disponibilidad De Experto Financiero

o   **Tipo de riesgo:** De recurso humano/conocimiento – riesgo asociado a la falta de un experto en finanzas.

o   **Punto de ruptura:** Ocurre cuando surge un problema financiero complejo (por ejemplo, la creación de cuentas contables) que el equipo no puede resolver sin un experto especializado. Actualmente este es un tema que en mi experiencia puede generar retrasos porque el no tener fielmente las reglas de negocio para los procesos financieros para los clientes y que puede set un incumplimiento de los requerimientos

o   **Acciones preventivas:**

- Capturar el conocimiento del experto disponible en documentación detallada (transformar conocimiento en especificaciones claras).
- Realizar sesiones de capacitación interna para el equipo de desarrollo en conceptos financieros básicos relevantes.
- Planificar la possible contratación o asignación de un experto externo o consultoría temporal en caso necesario.
- Asegurar que la única persona experta trabaje estrechamente con el equipo en la fase inicial para transferir conocimiento y revisar las primeras versiones del MVP.  

o   **Acciones mitigantes/correctivas:**

- Si surge un problema mayor sin experto disponible, buscar soporte en instituciones externas.
- Dividir components de riesgo hacia un área de menor prioridad hasta conseguir apoyo (p.ej., aislar la lógica financiera compleja y concentrarse primero en la parte técnica que pueda soportar la lógica financiera).
- Reprogramar temporalmente el plan (dentro del margen del 20%) para dedicar más tiempo a análisis o pruebas con expertos externos antes de continuar.

### · Riesgo R4: Problemas En El Diseño De la API

o   **Tipo de riesgo:** De diseño/arquitectura – riesgo de que la API diseñada no sea suficientemente genérica o flexible para reutilización en contextos variados.

o   **Punto de ruptura:** Se identifica cuando la nueva librería no puede adaptarse a un caso de uso previsto del proyecto del cliente, o que require reescritura extensiva. Por ejemplo, si al integrar la API en un nuevo escenario se necesita modificar código central, indicando que el diseño actual no satisface el requerimiento de reutilización.

o   **Acciones preventivas:**

- Realizar un diseño inicial mediante consultas a futuros usuarios o proyectos que usarán la API para asegurar cubrir distintos casos.
- Utilizar principios de diseño modular y de patrones (p.ej., interfaces claras, extensibilidad) para facilitar la reutilización.
- Planificar iteraciones de prototipado de la API y pruebas de integración con módulos de ejemplo para verificar su flexibilidad.  

o   **Acciones mitigantes/correctivas:**

- Si se detectan limitaciones en la API, introducir abstracciones o adaptadores para acomodar casos no previstos.  
- Permitir cierta personalización (parámetros configurables) en la versión final si se confirman necesidades específicas no previstas.
- Documentar claramente las limitaciones encontradas y planificar una possible segunda versión o parche futuro que mejore la flexibilidad, dedicando tiempo del desarrollo a reestructurar aquellas partes críticas.

## Conclusión

En base al análisis anterior, **la prioridad máxima recae en R2 y R1**, pues una falla en plazos o en precisión algorítmica puede comprometer el proyecto completo. Los riesgos R3 y R4 son de prioridad media-baja según su exposición, pero también requieren monitoreo y medidas oportunas. La **matriz de probabilidad-impacto** ha servido para ordenar estos riesgos de acuerdo a su exposición. Para cada riesgo se han propuesto acciones **preventivas** que tratan de evitar su ocurrencia y acciones **mitigantes/correctivas** para minimizar el impacto en caso de materializarse. El establecimiento de fuentes de riesgo permite saber cuándo pasar a la fase de acción inmediata. Siguiendo este plan de gestión de riesgos, el equipo puede asignar recursos y monitorear continuamente el advance, garantizando así que los riesgos más críticos reciban la atención necesaria para la protección del proyecto.