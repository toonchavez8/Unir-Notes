# Actividad 1: Requisitos Mediante Mapeo De Historias De Usuario Y Wireframes

## Introduction

El **Spring Petclinic** es un caso de ejemplo de aplicación web que muestra cómo utilizar el stack de Spring para construir una aplicación de gestión de datos de mascotas y sus dueños.

Este ejercicio consiste en inferir los requisitos del sistema analizando la aplicación existente, estructurar los requisitos en historias de usuario mediante el “story mapping” y diseñar un wireframe de la pantalla de ficha de propietario. Así, se aborda de forma práctica la identificación de requisitos, la definición de historias de usuario y la creación de prototipos de interfaz. 

## Elección De Plataformas

Para gestionar las historias de usuario **se seleccionó Jira junto con Confluence**, aprovechando su amplia adopción en la industria y su flexibilidad. En particular, Jira es muy usado para la planificación ágil, y Confluence cuenta con complementos (por ejemplo, el plugin _Whiteboard_) que facilitan la creación de mapas de historias de usuario visuals. Esto permite estructurar y rastrear las historias de usuario y releases dentro de un espacio colaborativo. La principal ventaja es la integración con otras herramientas de desarrollo y la posibilidad de documentar el proceso; la desventaja es que require una configuración inicial (instalar el plugin, definir la épica y los releases) y cierta curva de aprendizaje en la herramienta Atlassian.

Para el diseño del **wireframe** se optó por **Figma**, una herramienta en línea orientada al diseño y prototipado colaborativo. Figma permite “visualizar ideas como wireframes y compartirlas con otros para colaborar y alinear flujos y diseños” Esta plataforma ofrece plantillas y components reutilizables, facilitando la creación rápida de pantallas en distintos niveles de fidelidad. Elegir Figma implicó adaptarse a una interfaz rica en funciones, pero la curva de aprendizaje fue razonablemente baja gracias a su usabilidad intuitiva. Como alternativa se consideró Balsamiq (más simple y centrado en wireframes esquemáticos), pero se priorizó Figma por mi previa experencia usando figma.

## Proceso De Story Mapping

### MVP

Analizando la aplicación, identificamos tres **flujos principales** que definen el Producto Mínimo Viable (MVP):

- **Navegación básica:** incluyó la vista inicial (Home) y la navegación por el menú superior.
    
- **Gestión de propietarios (dueños):** búsqueda y visualización de propietarios; listado de resultados; ficha de propietario con sus datos y mascotas; registro de nuevos propietarios.
    
- **Visualización de veterinarios:** listado de veterinarios disponibles con sus especialidades.

A partir de estos flujos se definieron las **historias de usuario esenciales** para el MVP. A continuación se muestra una tabla con las principales historias consideradas:

| Story | Persona       | Título                      | Descripción                                                                                                                          |
| ----- | ------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Usuario       | Ver la página principal     | Como usuario, quiero acceder a la página principal para conocer el sistema y sus opciones básicas.                                   |
| 2     | Recepcionista | Buscar dueños de mascotas   | Como recepcionista, quiero buscar a los dueños de mascotas por apellido para localizar rápidamente sus registros.                    |
| 3     | Recepcionista | Ver listado de dueños       | Como recepcionista, quiero ver un listado de dueños cuando la búsqueda devuelve múltiples resultados, para elegir el correcto. |
| 4     | Recepcionista | Ver perfil de dueños        | Como recepcionista, quiero ver la información completa de un dueño para consultar sus datos de contacto y mascotas registradas.      |
| 5     | Recepcionista | Registrar nuevo dueño       | Como recepcionista, quiero registrar un nuevo dueño con sus datos básicos para mantener el registro actualizado.                     |
| 6     | Usuario       | Ver listado de veterinarios | Como usuario, quiero ver el listado de veterinarios disponibles y sus especialidades para elegir al más adecuado.                    |

![[Pasted image 20251214220221.png]]

En el tablero de story mapping identifiqué primero los roles principales: **Dueño de mascota, Veterinario** y **Recepcionista**. A continuación fui plasmando cada historia siguiendo el formato _“Como [rol], quiero [acción], para [beneficio]”_ en notas adhesivas digitales.

![[Pasted image 20251214220202.png]]

Para mejorar la visualización, cada historia se etiquetó con el rol al que pertenece principalmente. De este modo pude ver cómo las historias se relacionan con los diferentes usuarios y entre sí. Finalmente estas historias después se registraron en **Jira** dentro de la épica denominada _“MVP: User Stories”_. 

![[Pasted image 20251214220350.png]]

![[Pasted image 20251214220504.png]]

## Version Actual

La versión actual del PetClinic (por ejemplo la 2.x) incluye muchas más funcionalidades que el MVP inicial. Al analizar el código fuente y probar la aplicación, identifiqué 32 historias de usuario potenciales. Sin embargo, varias eran similares (principios CRUD), de modo que resultaron unas **21 historias únicas** más destacables. Estas ampliaciones corresponden a los siguientes flujos principales:

![[Pasted image 20251214221119.png]]

- **Navegación mejorada:** incluye manejo de páginas de error y navegación completa entre secciones.
    
- **Gestión completa de dueños:** además de las búsquedas simples, se implementa paginación, edición de datos de dueño, validaciones de campos obligatorios, mensajes de confirmación y error para cada operación.
    
- **Gestión de mascotas:** se añaden historias para CRUD de mascotas en la ficha del dueño, incluyendo selección del tipo de mascota (perro, gato, etc.), validación de nombres únicos por dueño y edición de datos de la mascota.
    
- **Gestión de visitas:** se incorporan historias para programar nuevas visitas veterinarias de la mascota, registrar una descripción de la visita y consultar el historial de visitas anteriores de cada mascota.
    
- **Visualización de veterinarios:** el listado de veterinarios se presenta paginado (5 por página) y muestra las especialidades de cada uno; además, en versiones más avanzadas, se añade API REST y gestión de roles (usuarios autenticados).

Las demas de forma en tabla las puede ver aqui.

![[Pasted image 20251214221250.png]]

![[Pasted image 20251214221313.png]]

| Story | Categoría                     | Persona       | Título                                    | Descripción                                                                                                                  |
| ----- | ----------------------------- | ------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1     | Navegación Básica             | Usuario       | Navegar por menú superior                 | Como usuario, quiero navegar por el menú superior entre secciones para acceder rápidamente a las diferentes funcionalidades. |
| 2     | Navegación Básica             | Usuario       | Visualizar página de error                | Como usuario, quiero visualizar mensajes de error apropiados cuando ocurra un problema en el sistema.                        |
| 3     | Gestión de dueños             | Recepcionista | Buscar dueños por apellido                | Como recepcionista, quiero buscar dueños por apellido con autocompletado para localizar registros rápidamente.               |
| 4     | Gestión de dueños             | Recepcionista | Ver ficha detallada de dueño              | Como recepcionista, quiero ver la ficha detallada de un dueño con todas sus mascotas para consultar información completa.    |
| 5     | Gestión de dueños             | Recepcionista | Registrar nuevo dueño                     | Como recepcionista, quiero registrar un nuevo dueño con validaciones para mantener datos correctos.                          |
| 6     | Gestión de dueños             | Recepcionista | Editar información de dueño               | Como recepcionista, quiero editar la información de un dueño existente para mantener los datos actualizados.                 |
| 7     | Gestión de dueños             | Recepcionista | Validar datos obligatorios                | Como recepcionista, quiero que el sistema valid datos obligatorios (nombre, dirección, ciudad, teléfono) al registrar.       |
| 8     | Gestión de dueños             | Recepcionista | Ver mensajes de confirmación              | Como recepcionista, quiero ver mensajes de confirmación de operaciones exitosas para saber que la acción se completó.        |
| 9     | Gestión de dueños             | Recepcionista | Ver mensajes de error                     | Como recepcionista, quiero ver mensajes de error en validaciones para corregir los datos ingresados.                         |
| 10    | Gestión de Mascotas           | Recepcionista | Registrar nueva mascota                   | Como recepcionista, quiero registrar una nueva mascota para un dueño con toda su información.                                |
| 11    | Gestión de Mascotas           | Recepcionista | Seleccionar tipo de mascota               | Como recepcionista, quiero seleccionar el tipo de mascota (cat, dog, bird, etc.) de una lista predefinida.                   |
| 12    | Gestión de Mascotas           | Recepcionista | Validar nombre único de mascota           | Como recepcionista, quiero que el sistema valid que el nombre de la mascota sea único por dueño.                             |
| 13    | Gestión de Mascotas           | Recepcionista | Ver listado de mascotas                   | Como recepcionista, quiero ver el listado de mascotas de un dueño en su ficha.                                               |
| 14    | Gestión de Mascotas           | Recepcionista | Editar información de mascota             | Como recepcionista, quiero editar la información de una mascota existente para mantener los datos actualizados.              |
| 15    | Gestión de Visitas            | Recepcionista | Registrar nueva visita                    | Como recepcionista, quiero registrar una nueva visita para una mascota para agendar citas.                                   |
| 16    | Gestión de Visitas            | Recepcionista | Añadir descripción de visita              | Como recepcionista, quiero añadir una descripción del motivo de la visita para documentar el caso.                           |
| 17    | Gestión de Visitas            | Recepcionista | Visualizar detalles de visitas históricas | Como recepcionista, quiero visualizar la fecha y descripción de cada visita histórica para consultar información pasada.     |
| 18    | Gestión de Visitas            | Recepcionista | Ver confirmación de visita agendada       | Como recepcionista, quiero ver mensajes de confirmación al agendar una visita para saber que se registró correctamente.      |
| 19    | Visualización de Veterinarios | Usuario       | Ver listado paginado de veterinarios      | Como usuario, quiero ver un listado paginado de veterinarios (5 por página) para conocer al personal disponible.             |
| 20    | Visualización de Veterinarios | Usuario       | Ver especialidades de veterinarios        | Como usuario, quiero ver las especialidades de cada veterinario para elegir al más adecuado.                                 |
| 21    | Visualización de Veterinarios | Usuario       | Navegar entre páginas de veterinarios     | Como usuario, quiero navegar entre páginas del listado de veterinarios para ver todos los disponibles.                       |

Las diferencias clave entre el MVP y la versión actual se resumen en la siguiente tabla:

|Aspecto|MVP|Versión actual|
|---|---|---|
|**Propietarios**|CRUD básico y búsqueda simple|CRUD completo con paginación, validaciones avanzadas y mensajes de feedback|
|**Mascotas**|No incluido|CRUD completo de mascotas con selección de tipo y validación de nombres|
|**Visitas**|No incluido|Gestión de visitas (registro de cita y historial por mascota)|
|**Veterinarios**|Listado simple|Listado paginado con especialidades; API REST y roles de acceso|
|**UX / Feedback**|Interfaz básica sin retroalimentación|Mensajes de confirmación y error, navegación mejorada (breadcrumbs, etc.)|
|**Validaciones**|Mínimas (formulario simple)|Validaciones exhaustivas en todos los formularios|

Estos detalles muestran que la versión actual contiene los mismos flujos básicos del MVP pero con funcionalidades adicionales (paginación, validaciones, gestión de roles, historial) para completar el sistema. Cada historia extra se añadió al plan de releases correspondiente (dentro de jira para su fácil segmentación como épica).

## Historia De Usuario Detallada

A continuación se presenta una historia de usuario detallada que representa una de las funcionalidades principales del sistema.

A continuación se presenta una historia de usuario ejemplar, con su descripción, contexto de uso y criterios de aceptación detallados en formato Gherkin.

**ID:** Scrum-15 
**Título:** Buscar propietario de mascota por apellido  
**Épica:** Gestión de Propietarios  
**Prioridad:** Alta  
**Estimación:** 5 Story Points

**Descripción:**  
Como **recepcionista** de la clínica veterinaria,  
quiero **buscar propietarios de mascotas por su apellido**  
para **localizar rápidamente sus registros y consultar la información de sus mascotas y visitas programadas**.
![[Pasted image 20251214221544.png]]

**Contexto de uso:**  
Esta funcionalidad se utilize principalmente en el mostrador de recepción cuando:

- Un cliente llega a la clínica para una cita y se necesita acceder a sus datos.
    
- Se require contactar con un propietario por teléfono o correo.
    
- Se desea consultar el historial de visitas de una mascota.
    
- Es necesario actualizar los datos de contacto del propietario.

**Criterios de aceptación:**

**Escenario 1: Búsqueda con un único resultado**

```gherkin
DADO que estoy en la página de búsqueda de propietarios
CUANDO ingreso "Franklin" en el campo de búsqueda de apellido
Y hago clic en el botón "Find Owner"
ENTONCES el sistema me redirige directamente a la ficha del propietario
Y puedo ver los datos completos del dueño (nombre, dirección, ciudad y teléfono)
Y puedo ver todas las mascotas registradas a su nombre y el historial de visitas de cada una

```

**Escenario 2: Búsqueda con múltiples resultados**

```Gherkin
DADO que estoy en la página de búsqueda de propietarios
CUANDO ingreso "Davis" en el campo de búsqueda de apellido
Y hago clic en el botón "Find Owner"
ENTONCES el sistema muestra un listado paginado de resultados
Y cada resultado muestra nombre completo, dirección, ciudad y teléfono del propietario
Y se muestran hasta 5 propietarios por página
Y puedo navegar a otras páginas del listado
Y puedo hacer clic en cualquier nombre para ver la ficha completa correspondiente
```

**Escenario 3: Búsqueda sin resultados**

```Gherkin
DADO que estoy en la página de búsqueda de propietarios
CUANDO ingreso "XYZ" en el campo de búsqueda de apellido
Y hago clic en el botón "Find Owner"
ENTONCES el sistema muestra un mensaje de error "not found"
Y permanezco en la página de búsqueda
Y puedo modificar mi criterio o registrar un nuevo propietario
```

**Escenario 4: Búsqueda vacía (mostrar todos)**

```Gherkin
DADO que estoy en la página de búsqueda de propietarios
CUANDO dejo el campo de apellido vacío
Y hago clic en el botón "Find Owner" O navego directamente a /owners
ENTONCES el sistema muestra el listado completo de todos los propietarios paginado
Y se ven los primeros 5 propietarios
Y puedo navegar entre todas las páginas disponibles del listado
```

**Escenario 5: Búsqueda con coincidencia parcial**

```Gherkin
DADO que estoy en la página de búsqueda de propietarios
CUANDO ingreso "Dav" en el campo de búsqueda de apellido
Y hago clic en el botón "Find Owner"
ENTONCES el sistema muestra todos los propietarios cuyo apellido comienza con "Dav"
Y esto incluye nombres como "Betty Davis", "Harold Davis", etc.
Y los resultados se muestran paginados
```

Los escenarios anteriores definen el comportamiento esperado del sistema para la historia **US-001**. Cada criterio de aceptación detalla las condiciones de búsqueda, los resultados esperados (único, múltiples, ninguno) y la interacción del usuario con la interfaz.

## Wireframing De la Pantalla De Propietario

Para el diseño del wireframe utilicé la plataforma **Figma**. En esta herramienta realicé el wireframe de la **pantalla de ficha de propietario**, cuyo objetivo es mostrar la información detallada de un cliente de manera clara y estructurada.

La pantalla incluye campos como **nombre**, **dirección**, **ciudad** y **teléfono**, así como una sección dedicada a la **lista de mascotas asociadas** al propietario. Para cada mascota se muestra información relevante como **nombre**, **tipo** y **fecha de nacimiento**. Además, se definieron botones de acción clave: **“Editar datos del dueño”**, **“Agregar nueva mascota”** y **“Registrar visita”** para cada mascota, facilitando la interacción y el flujo de trabajo del usuario.

Antes de iniciar el diseño visual, comencé extrayendo los **requerimientos** y planteando **propuestas iniciales** en un archivo en formato Markdown. Este documento me sirvió como guía para definir los **criterios de aceptación** y delimitar claramente el alcance y los objetivos del diseño de esta historia de usuario.

![[Pasted image 20251215161634.png]]

Posteriormente, en mi tableta realicé **varias versiones de bocetos** explorando distintas disposiciones y jerarquías de información. Este proceso iterativo me permitió refinar el diseño y asegurar que cumpliera con los requerimientos previamente definidos.

![[Pasted image 20251215162710.png]]

Una vez definido el boceto final, lo llevé a **Figma**, donde comencé a construir el wireframe de manera digital, respetando la estructura y decisiones tomadas durante la etapa de bocetaje.

![[Pasted image 20251215164913.png]]

Para la elaboración del wireframe se utilize **formas básicas de formulario** (inputs, etiquetas y contenedores) . El resultado es un diseño **esquemático**, sin estilos visuals finales, enfocado en la distribución de la información y la funcionalidad. Finalmente, el wireframe fue **exportado como imagen PNG** para su inclusión en la documentación correspondiente.

![[Pasted image 20251215165756.png]]

## Valoración Del Aprendizaje

| Aspecto                   | Lo que aprendí                                                                                                                                     | Dificultades/Observaciones                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Herramientas de mapeo     | Conocí el uso de Jira y Confluence para planificar historias de usuario. Aprendí a crear épicas, y historias en Jira.                              | Require familiarizarse con la interfaz; configurar plugins (Whiteboard) consumió tiempo, Tambien es abrumador.                |
| Story Mapping             | Comprendí cómo estructurar las historias en flujos (navegación, dueños, etc.) y priorizar para un MVP. Visualicé mejor el alcance de cada release. | Fue un reto inicial identificar todas las historias clave; también alinear qué historias correspondían a cada rol.            |
| Herramienta de wireframes | Ya conocia figma, lo que me apoyo para realizar el dieño                                                                                           | La mayor dificultad fue la distribución de elementos en la pantalla y asegurar que no faltaran campos críticos en el diseño.  |
| Documentación del proceso | Comprendí la importancia de justificar elecciones y plasmar el trabajo (capturas, enlaces, evidencias).                                            | Sintetizar la información de forma clara requirió esfuerzo (especialmente al completar la memoria con limitación de páginas). |

Cada uno de estos aspectos contribuyó al aprendizaje general. Por ejemplo, la práctica con Jira reforzó mi entendimiento de la gestión ágil de requerimientos, mientras que el uso de Figma mejoró mis habilidades de diseño de interfaces. Las dificultades señaladas motivan a profundizar en el uso de estas herramientas.

## Conclusión

En esta actividad se aplicaron técnicas de ingeniería de requisitos al caso práctico de Spring PetClinic. Se utilizó **story mapping** para descomponer el sistema en funcionalidades mínimas (MVP) y en un conjunto más amplio (versión actual), cumpliendo así con los criterios de la rúbrica al plantear dos releases. Se definieron historias de usuario detalladas (incluyendo criterios de aceptación) que representan las interacciones clave del usuario con la aplicación. Por otro lado, se diseñó un **wireframe** de la pantalla de la ficha de propietario utilizando la plataforma Figma, justificando dicha elección por su facilidad de uso colaborativo y sus recursos de diseño.

La memoria técnica (documento adjunto) expone el proceso completo: selección de plataformas, historia de usuario mapping y creación de wireframes, junto con las capturas que evidencian el trabajo realizado. En conjunto, se logró estructurar de forma clara los requisitos del sistema y generar un prototipo visual que respalda las funcionalidades definidas. La experiencia mostró la importancia de planificar con métodos ágiles (como user story mapping) y de comunicar los hallazgos a través de documentación ordenada. La actividad reforzó mi comprensión sobre cómo abordar requisitos en proyectos de software y resaltó tanto las ventajas de las herramientas elegidas como los aspectos a mejorar para futuros desarrollos.