# **Planificación Y Estimación Ágil. Mediciones En Desarrollos ágiles**

- **Planificación ágil de proyectos software**
    
    - Se parte de una **lista de funcionalidades** que el sistema debe implementar.
        
    - Esta lista se transforma en **historias de usuario** que permiten agregar valor **de forma incremental**.
        
    - Las historias de usuario deben **priorizarse** con base en:
        
        - **Valor**: importancia para el cliente según beneficios, pérdidas, riesgos, alineación con el negocio y valor añadido.
            
            - Debe **incrementarse en cada iteración**.
                
            - Se priorizan historias de **menos tiempo, menos riesgos, mayor valor estratégico y facturación**.
                
        - **Estimación**: coste de desarrollo expresado en **unidades de tiempo/persona**.
            
- **Planning Poker**
    
    - Técnica popular de estimación en proyectos ágiles.
        
    - Se usan cartas numeradas (secuencia **Fibonacci**), una carta de **interrogación** (información insuficiente) y una de **taza de café** (descansos).
        
    - Utilize **puntos de historia** para medir el tamaño de funcionalidades o requisitos.
        
        - Cada organización define el valor de un punto, usualmente equivalente a **un día de trabajo**.
            
    - **Proceso iterativo**:
        
        - El **Product Owner** lee la historia de usuario.
            
        - El equipo realiza preguntas para entender la historia.
            
        - Cada miembro estima el esfuerzo y muestra su carta al mismo tiempo.
            
        - Si hay discrepancia, se discuten las estimaciones extremas y se vuelve a votar.
            
        - Se busca **convergencia en una estimación común**, no precisión absoluta.
            
        - Favorece **sinergia del equipo** y mejora la precisión, especialmente ante incertidumbre.
            
    - Se realiza:
        
        - Al inicio del proyecto (puede tomar 2-3 reuniones de 1–3 horas).
            
        - Al final de cada iteración (para estimar trabajo realizado y planificar el siguiente).
            
- **Otras técnicas de priorización**
    
    - **Dentro o fuera (In or Out)**:
        
        - Técnica binaria: los participantes deciden si una historia está "dentro" o "fuera".
            
        - Útil para **filtrado inicial** en workshops con muchas historias de usuario.
            
    - **MoSCoW**:
        
        - Clasificación en:
            
            - **Must**: obligatorio para el éxito.
                
            - **Should**: importante pero no indispensable.
                
            - **Could**: deseable, no urgente.
                
            - **Won’t**: descartado por ahora.
                
        - Puede set ambigua y no proporciona guías claras de clasificación.
            
    - **Técnica de los $100 / Subasta**:
        
        - Cada participante distribuye “dinero” virtual entre las historias según su prioridad.
            
        - Permite establecer una **priorización global** basada en el valor asignado.
            
    - **Quality Function Deployment (QFD)**:
        
        - Evalúa cada historia desde distintos **puntos de vista**:
            
            - Penalización por no incluirla.
                
            - Coste y riesgo técnico de implementación.
                
        - Solo se consideran historias independientes (sin dependencias previas).
            
- **Otras técnicas complementarias de priorización**
    
    - **Filtro de priorización**
        
    - **Pirámide de priorización**
        
    - **Modelo Kano**
        
    - **Clasificación de lista**
        
    - **Business value y story points**
        
    - **Urgente**
        
    - **Basados en riesgos**
        
- **Mediciones en desarrollos ágiles**
    
    - Utilizan un **cuadro de mando ágil** para centralizar métricas, gráficos y herramientas que:
        
        - Facilitan el trabajo en equipo.
            
        - Mejoran la comunicación con el cliente.
            
    - **Indicadores principales**:
        
        - **Productividad**
            
            - **Velocidad**: trabajo completado por iteración.
                
                - Permite comparar velocidad estimada vs. real.
                    
            - **Aceleración**: cambio en la velocidad del equipo.
                
                - Fórmula: _(velocidad iteración n – velocidad iteración 0) / velocidad iteración 0_
                    
        - **Progreso del proyecto**
            
            - **Gráficos de progreso**: muestran historias implementadas vs. esfuerzo total.
                
            - **RTF (funcionalidades probadas y aceptadas)**: mide funcionalidades que superan pruebas de aceptación.
                
        - **Valor entregado y retorno de inversión**
            
            - **Agile EVM** (Earned Value Management en enfoque ágil):
                
                - Mide rendimiento vs. planificación.
                    
                - Utilize puntos de historia y require planificación inicial por iteraciones.
                    
        - **Gestión de riesgos**
            
            - **Impediment backlog**: lista priorizada de incidencias que bloquean el desarrollo.
                
- **Herramientas de apoyo**
    
    - Existen múltiples herramientas digitales para planificación y gestión de proyectos ágiles.
        
    - **Atlassian Jira** es la más utilizada y recomendada.

| Clasificación                     | Indicador                                         | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Productividad                    | Velocidad                                         | Cantidad de trabajo que el equipo de desarrollo puede realizar en una iteración del proyecto. Se debe indicar la ratio con la cual el equipo convierte historias de usuario en incrementos potencialmente entregables. Así, se va viendo la velocidad estimada y la velocidad real que tiene el equipo. Una vez conocida la velocidad del equipo de desarrollo, esta se puede utilizar para estimar en la siguiente iteración del proyecto. Además, con el histórico de la velocidad del equipo, se puede ir ajustando la estimación del proyecto para que sea más realista. |
|                                  | Aceleración                                       | Tasas de crecimiento, o de decrecimiento, de las velocidades del equipo de desarrollo respecto a un período de referencia en base a la siguiente fórmula: <br> **= (velocidad iteración (n) – velocidad iteración (0)) / velocidad iteración (0)**                                                                                                                                                                                                                                                                |
| Progreso del proyecto            | Gráficos de progreso                              | Gráfico que refleja el advance del equipo de desarrollo hasta un memento concreto. Se suele medir el número de historias que se llevan implementadas hasta ese memento, en relación al esfuerzo total que hace falta para poder terminar el proyecto. Permite apreciar lo que falta para implementar el sistema en su totalidad.                                                                                                                                                                                |
|                                  | Funcionalidades probadas y aceptadas (RTF)        | Cantidad de funcionalidades que han superado las pruebas de aceptación. Este indicador favorece también la agilidad y la productividad del equipo de desarrollo. Para que realmente sea útil, es importante que las historias de usuario se definan con un buen nivel de granularidad. Además, siempre que se vayan añadiendo más funcionalidades al proyecto se deberán volver a aplicar las pruebas de aceptación a todas las funcionalidades ya implementadas.                                                      |
| Valor entregado y retorno inversión | EVM-Ágil (AgileEVM)                            | Adaptación de la técnica tradicional de gestión de proyectos conocida como _Earned Value Management_ (EVM), que mide el rendimiento del proyecto en relación a una línea base, es decir, en relación con lo que se había planificado. Con el uso de esta técnica, se trata de identificar las posibles desviaciones entre lo estimado y lo presupuestado. EVM-Ágil dará a conocer el retorno y el riesgo y su velocidad haciendo uso, en este caso, de los puntos de historia como la medida a utilizar para realizar los cálculos. Por tanto, para poder hacer uso de esta técnica, será necesario realizar una planificación inicial de las iteraciones que incluya el uso de historias de usuario y que se debe incluir en cada iteración y el valor que se le da a cada historia de usuario. |
| Gestión de riesgos               | Impediment backlog                                | Herramienta que muestra la lista priorizada de incidencias abiertas, con el objetivo de solventar los problemas que están impidiendo un progreso adecuado del desarrollo de las funcionalidades en cada iteración.                                                                                                                                                                                                                                                                                              |

## MicroTest

- ¿Cuál de las siguientes no es una característica del planning poker?
	- Utilize cartas con valores numéricos aleatorios.
- ¿Cuál de las siguientes afirmaciones es falsa?
	- La planificaciån påker require la participaciön de todos los miembros del equipo de desarrollo.
- ¿Cuál es el objetivo de utilizar el quality function deployment para priorizar historias de usuario?
	- Obtener una valoración global de cada historia de usuario que permita priorizarla dentro del conjunto.
- ¿Cuál de las siguientes opciones no es una métrica utilizada comúnmente en proyectos ágiles
	- Puntos de Historia
- ¿Cuál es la recomendación general sobre la herramienta más utilizada y recomendada para la planificación y gestión de proyectos ágiles de desarrollo de software?
