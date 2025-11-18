Actividad 1: Modelado de amenazas de una aplicación (grupal)
Mv 
**Objetivos de la actividad**

Una amenaza a cualquier sistema es cualquier actor, agente, circunstancia o evento que tiene el potencial de causarle daño a sus datos, servicios y recursos. Con la presente actividad se pretende conseguir los siguientes objetivos:

- Estudio y análisis de la arquitectura de una aplicación para poder determinar el nivel de riesgo y seguridad de las soluciones técnicas a incluir en su diseño.
- Analizar y detectar amenazas de seguridad y desarrollar técnicas para su prevención.
- Aprender a diseñar e implantar sitios, servicios y aplicaciones con garantías de seguridad.
- Facilitar la identificación de las condiciones o aquellas vulnerabilidades que, una vez eliminadas o contrarrestadas, afectan a la existencia de múltiples amenazas.
- Proporcionar información relevante sobre cuáles serían las contramedidas más eficaces para contrarrestar una posible amenaza o mitigar los efectos de la presencia de una vulnerabilidad en el diseño de una aplicación.

**Descripción de la actividad**

Este es un ejercicio práctico de modelado de amenazas, utilizando una herramienta de modelado como Threat Analysis and Modeling Tool (TAMT), de una aplicación web de tres capas para un negocio de pago electrónico de una librería, con la siguiente arquitectura lógica:

![mexingsof07_act1](<Maestría-Ingeniería-de-Software/05-Desarollo-Seguro-y-Auditoria/Actividades/Attachments/mexingsof07_act1%202.png>)

Utilizar la aplicación Threat Analysis and Modeling Tool (TAMT) con el propósito de analizar las amenazas de una aplicación web típica de negocio de pago electrónico de una librería (textos, libros, revistas, etc.) en formato digital con opciones de impresión. La aplicación se puede descargar [aquí](https://docs.microsoft.com/es-es/azure/security/develop/threat-modeling-tool).

**Pasos de elaboración**

1. Realizar el diagrama de flujo de datos de la aplicación (DFD) e incluirlo en la herramienta TAMT. Se propone un diagrama DFD inicial básico que el estudiante deberá mejorar para obtener la puntuación total de este apartado:

![mexingsof07_act1](<Maestría-Ingeniería-de-Software/05-Desarollo-Seguro-y-Auditoria/Actividades/Attachments/mexingsof07_act1%203.png>)

1. Una vez incluido el diagrama DFD en TAMT, realizar el análisis automático de las amenazas. Rellenar una tabla con diez amenazas obtenidas de la herramienta.

|   |   |
|---|---|
|Descripción de la amenaza|Inyección de comandos SQL|
|Objetivo|Componente de acceso a base de datos|
|Técnicas de ataque|El atacante introduce comandos SQL en el campo usuario utilizado para formar una nueva sentencia SQL.|
|Patrón ataque CAPEC|CAPEC-66: SQL Injection|
|Código CWE (si aplica)|CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')|
|Medidas de mitigación|Utilización de procedimientos parametrizados, sanitización de los meta caracteres del leguaje SQL.|
|Descripción de la amenaza||
|Objetivo||
|Técnicas de ataque||
|Patrón ataque CAPEC||
|Código CWE (si aplica)||
|Medidas de mitigación||

1. Valoración del riesgo de las amenazas con el método DREAD _(damage, reproducibility, exploitability, affected, discoverability)._ El riesgo se puede cuantificar como el resultado de multiplicar la probabilidad de que la amenaza se produzca, por el daño potencial de esta.

Cada valor se cuantifica con un valor entre 1 y 3. Rellenar la tabla con al menos diez amenazas obtenidas de la de la herramienta TAMT.

|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
||   |Prob. Ocurr. (P)|   |   |Impacto Pot. (I)|   |P|I|Riesgo|
|_Nº_|_Amenaza_|_R_|_E_|_DI_|_D_|_A_|_(R+E+DI)_|_(D+A)_|_PxI_|
|1|Inyección de comandos SQL|3|2|2|3|3|7|6|42|
|2||||||||||
|……||||||||||
|15||||||||||