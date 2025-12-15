# Introduction

# Elección De Plataformas

# Proceso De Story Mapping

## MVP

Analizando las actividades principales dentro del la application de pet clinic podmos extraer y reducir las siguentes 3 interactions primarias que 

1. **Navegación básica**

2. **Gestión de dueños**

3. **Visualización de información**

Que estas 3 para mi me dan origin a un MVP con las siguientes user stories

| Story | Persona       | Título                      | Descripción                                                                                                                          |
| ----- | ------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Usuario       | Ver la página principal     | Como usuario, quiero acceder a la página principal para conocer el sistema y sus opciones básicas.                                   |
| 2     | Recepcionista | Buscar dueños de mascotas   | Como recepcionista, quiero buscar a los dueños de mascotas por apellido para localizar rápidamente sus registros.                    |
| 3     | Recepcionista | Ver listado de dueños       | Como recepcionista, quiero ver un listado de dueños cuando la búsqueda devuelve múltiples resultados, para elegir el correcto. |
| 4     | Recepcionista | Ver perfil de dueños        | Como recepcionista, quiero ver la información completa de un dueño para consultar sus datos de contacto y mascotas registradas.      |
| 5     | Recepcionista | Registrar nuevo dueño       | Como recepcionista, quiero registrar un nuevo dueño con sus datos básicos para mantener el registro actualizado.                     |
| 6     | Usuario       | Ver listado de veterinarios | Como usuario, quiero ver el listado de veterinarios disponibles y sus especialidades para elegir al más adecuado.                    |

Estos los registre dentro de la plataforma de jira lo cual me dio una oportunidad de experimentar y lograr asignar los a una epica que designe como `MVP: User Stories` de esta forma estaban categolaizaradas 

Para llegar a esas historais depues de mi analysis lo que hize fue activar el plugin de jira llamado confluisz whiteboard lo cual me permitio dentro de la misma plataforma por crear usar un template llamado story mapping

Inicie el story mapping designado cuales seriam mis personas o usarios principales para ir generando una idea de interacciones y usabilidad para esos usarios inicie con 3

1. EL Dueño de masctoa
2. El veterinario
3. El recepcionista

Estos 3 perfiles los puedo categorizar como usarios dado a que que existen pasos y user stories que van a empalmarse entre ellos. 

Despues basandome en como se definen los stories Como [rol], quiero [acción], para [beneficio]. Inicie en los postis del whiteboard a definir mis stories..

Tambien para ver que usuarios o personas se empalamn en las historias fui agregando etiquetas de a quienes les importan mas las hisotrias para 

## Version Actual

La version actual es mucho mas amplia que lo que podriamos proponer en el mvp y logre definir 32 storieas de usario en base la los que encontre, dado a que muchas son muy similar por el hecho que estamos manejando cruds varias se repetin y podemos realmente identifcar unas 21 unicas que se me hicieron interesantes, 

Aqui la mayoria de los nuevos stories aportan en una de las siguentes flujos 

1. **Navegación básica**

2. **Gestión completa de Dueños**

3. **Gestión completa de mascotas**

4. **Gestión de visitas**

5. **Visualización de veterinarios

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

### Diferencias Clave Entre MVP Y Versión Actual

| Aspecto          | MVP                          | Versión Actual                                                             |
| ---------------- | ---------------------------- | -------------------------------------------------------------------------- |
| **Propietarios** | CRUD básico, búsqueda simple | CRUD completo con paginación, validaciones avanzadas, mensajes de feedback |
| **Mascotas**     | No incluido                  | CRUD completo, tipos predefinidos, validaciones de fechas y nombres únicos |
| **Visitas**      | No incluido                  | Gestión completa de visitas con historial por mascota                      |
| **Veterinarios** | Solo visualización simple    | Listado paginado con especialidades, API REST                              |
| **UX/UI**        | Básica sin feedback          | Mensajes de confirmación y error, paginación, navegación mejorada          |
| **Validaciones** | Mínimas                      | Exhaustivas en todos los formularios                                       |

## Historia De Usuario Detallada

A continuación se presenta una historia de usuario detallada que representa una de las funcionalidades principales del sistema.

### **Historia De Usuario: Buscar Y Visualizar Propietario De Mascota**

**ID:** US-001  

**Título:** Buscar propietario de mascota por apellido  

**Epic:** Gestión de Propietarios  

**Prioridad:** Alta  

**Estimación:** 5 Story Points  

#### Descripción

**Como** recepcionista de la clínica veterinaria  

**Quiero** buscar propietarios de mascotas por su apellido  

**Para** localizar rápidamente sus registros y acceder a la información de sus mascotas y visitas programadas

#### Contexto De Uso

Esta funcionalidad se utilize principalmente en el mostrador de recepción cuando:

- Un cliente llega a la clínica para una cita

- Se necesita contactar con un propietario

- Se require consultar el historial de visitas de una mascota

- Se necesita actualizar información de contacto

#### Criterios De Aceptación

**Escenario 1: Búsqueda con un único resultado**

```gherkin

DADO que estoy en la página de búsqueda de propietarios

CUANDO ingreso "Franklin" en el campo de búsqueda de apellido

Y hago clic en el botón "Find Owner"

ENTONCES el sistema me redirige directamente a la ficha del propietario

Y puedo ver los datos completos: nombre, dirección, ciudad y teléfono

Y puedo ver todas las mascotas registradas a su nombre

Y puedo ver el historial de visitas de cada mascota

```

**Escenario 2: Búsqueda con múltiples resultados**

```gherkin

DADO que estoy en la página de búsqueda de propietarios

CUANDO ingreso "Davis" en el campo de búsqueda de apellido

Y hago clic en el botón "Find Owner"

ENTONCES el sistema muestra un listado paginado de resultados

Y cada resultado muestra: nombre completo, dirección, ciudad y teléfono

Y puedo ver un máximo de 5 propietarios por página

Y puedo navegar entre páginas si hay más de 5 resultados

Y puedo hacer clic en cualquier nombre para ver su ficha completa

```

**Escenario 3: Búsqueda sin resultados**

```gherkin

DADO que estoy en la página de búsqueda de propietarios

CUANDO ingreso "XYZ" en el campo de búsqueda de apellido

Y hago clic en el botón "Find Owner"

ENTONCES el sistema muestra un mensaje de error "not found"

Y permanezco en la página de búsqueda

Y puedo modificar mi criterio de búsqueda o registrar un nuevo propietario

```

**Escenario 4: Búsqueda vacía (mostrar todos)**

```gherkin

DADO que estoy en la página de búsqueda de propietarios

CUANDO dejo el campo de apellido vacío

Y hago clic en el botón "Find Owner" O navego directamente a /owners

ENTONCES el sistema muestra el listado completo de todos los propietarios paginado

Y puedo ver los primeros 5 propietarios

Y puedo navegar entre todas las páginas disponibles

```

**Escenario 5: Búsqueda con coincidencia parcial**

```gherkin

DADO que estoy en la página de búsqueda de propietarios

CUANDO ingreso "Dav" en el campo de búsqueda de apellido

Y hago clic en el botón "Find Owner"

ENTONCES el sistema muestra todos los propietarios cuyo apellido comienza con "Dav"

Y esto incluye "Betty Davis", "Harold Davis", etc.

Y los resultados se muestran paginado
```

# Wireframing Nuestros Stories

# Valoración De Mi Aprendizaje

# Conclusión