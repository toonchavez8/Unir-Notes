Actividad 1: Requisitos mediante mapeo de historias de usuario y _wireframes_

Objetivos

Con esta actividad pondrás en práctica una forma de abordar los requisitos de un sistema, utilizando las técnicas de _user story mapping_ y la creación de _wireframes_. Para ello, haremos uso de una aplicación ya desarrollada sobre la que inferiremos los requisitos principales, detallaremos alguna historia de usuario y generaremos un _mockup_ o _wireframe_ de alguna de las pantallas.

Para plasmar las historias de usuario y los _wireframes_, podrás seleccionar la plataforma que quieras, justificando tu decisión y aprendizaje (qué aspectos valoras mejor y cuáles han sido más difíciles).

Descripción de la actividad

Pet-Clinic es un proyecto de ejemplo clásico para aprender a programar con el _framework_ Spring de Java. Instalando Java, un cliente Git y Maven, desde su repositorio GitHub, podemos descargar el mismo y ejecutarlo con estos pasos:

- git clone [https://github.com/spring-projects/spring-petclinic.git](https://github.com/spring-projects/spring-petclinic.git)
- cd spring-petclinic
- ./mvnw package (mvnw.cmd package en sistemas Windows)
- java -jar target/*.jar (en la versión actual es java -jar target/spring-petclinic-2.6.0-SNAPSHOT.jar pero revisa la versión cuando lo descargues)

Accede al repositorio Git a través del siguiente enlace:  
[https://github.com/spring-projects/spring-petclinic](https://github.com/spring-projects/spring-petclinic)

Si lo prefieres, puedes usar Docker o directamente ver la versión en la nube del proyecto tal y como sale en la documentación del repositorio GitHub.

Si accedes al siguiente enlace se puede visualizar la pantalla del sistema: [http://localhost:8080/](http://localhost:8080/)

![mexingsof03_act1](Maestría-Ingeniería-de-Software/06-Plataforma-desarrollo-software/Actividades/Attachments/mexingsof03_act1.jpeg)

A nivel global, la aplicación es de acceso público (no require login) y sobre el menú superior podemos ver las funciones principales:

1. Home: ver la pantalla principal.
2. Gestor de propietarios de mascotas.

- Buscar.
    - Ver listado.
    - Ver ficha de propietario: editar ficha de propietario, añadir nueva mascota al propietario y ver ficha de mascotas asociadas (editar ficha de mascota, añadir visita de mascota a veterinario).
- Añadir.

1. Gestor de veterinarios.

- Ver listado.

1. Error (solo como muestra de cómo sacar mensajes de error, no aporta funcionalidad alguna).

Existen otras muchas versiones del sistema Pet-Clinic, que extienden tanto la parte tecnológica (cubriendo desde nuevos lenguajes para el _front-end_ como arquitecturas de microservicios) como la parte funcional (añadiendo API REST incorporando gestión de usuarios y roles).

Si quieres, puedes verlos en la comunidad Pet-Clinic, aunque para esta  
práctica puedes basarte en el proyecto simple, en el siguiente enlace:  
[https://spring-petclinic.github.io/](https://spring-petclinic.github.io/)

Tras ejecutar el sistema, podrás identificar los principales requisitos funcionales que cubre. En esta práctica, debes:

- Identificar y analizar qué plataforma de gestión de requisitos que soporte historias de usuario se adapta a tu necesidad.
- Definir con la misma tu visión de _user story mapping_ de las funcionalidades que tiene el Pet-Clinic. Ordénelas en un mapa de historias de usuario para cubrir al menos dos versiones, una que fuera un producto mínimo viable y otra la actual.
- Detallar al menos una historia de usuario con información más detallada que explique la funcionalidad desde la perspectiva del usuario.
- Identificar y analizar qué plataforma de _wireframes_ se adapta a tu necesidad.
- Diseñar un _wireframe_ de la pantalla de la ficha de un propietario de mascota (no tiene que coincidir exactamente con la que se ha desarrollado, puedes plantear tu solución).

![mexingsof03_act1](<Maestría-Ingeniería-de-Software/06-Plataforma-desarrollo-software/Actividades/Attachments/mexingsof03_act1%201.jpeg>)

- Documentar el proceso y justificar tu elección de plataformas y tu aprendizaje y dificultades.

Entrega de la actividad

La entrega consistirá en un único fichero comprimido que debe container lo siguiente:

- Memoria técnica del trabajo realizado, que exponga el proceso y comenzando por la justificación de la elección de plataformas. Extensión máxima de veinticinco páginas en un documento PDF, tipo de letra Georgia, tamaño 11 e interlineado 1,5.
- Capturas de pantalla o enlaces que permitan evidenciar el trabajo realizado con las plataformas de _user story mapping_.
- Capturas de pantalla o enlaces que permitan evidenciar el trabajo realizado con las plataformas de _wireframes_.
- Apartado final de conclusiones con tu valoración personal de aprendizaje, qué aspectos valoras mejor del proceso y cuáles han sido más difíciles.
- Si las plataformas utilizadas permiten su exportación y se pueden aportar los ficheros fuente de estas, pero en todo caso es necesario incluir o capturas de pantalla o enlaces en la memoria que permitan evidenciar el trabajo sin necesidad de instalar todas las plataformas utilizadas.

# Análisis Del Proyecto Spring PetClinic

## User Story Mapping

A continuación se presenta el mapeo de historias de usuario para el sistema Spring PetClinic, organizado en dos versiones: MVP (Producto Mínimo Viable) y versión actual completa.

### Estructura Del User Story Map

#### **VERSIÓN MVP (Producto Mínimo Viable)**

**Backbone (Actividades principales del usuario)**

1. **Navegación básica**

2. **Gestión de propietarios**

3. **Visualización de información**

**User Stories - MVP v1.0**

```Python

┌─────────────────────────────────────────────────────────────────────────┐

│                        NAVEGACIÓN BÁSICA                                 │

├─────────────────────────────────────────────────────────────────────────┤

│ ✓ Ver página principal                                                  │

│   Como usuario, quiero acceder a la página principal para conocer       │

│   el sistema y sus opciones básicas                                     │

└─────────────────────────────────────────────────────────────────────────┘

  

┌─────────────────────────────────────────────────────────────────────────┐

│                    GESTIÓN DE PROPIETARIOS                               │

├─────────────────────────────────────────────────────────────────────────┤

│ ✓ Buscar propietarios                                                   │

│   Como recepcionista, quiero buscar propietarios por apellido para      │

│   localizar rápidamente sus registros                                   │

│                                                                          │

│ ✓ Ver listado de propietarios                                           │

│   Como recepcionista, quiero ver un listado de propietarios cuando      │

│   la búsqueda devuelve múltiples resultados                             │

│                                                                          │

│ ✓ Ver ficha de propietario                                              │

│   Como recepcionista, quiero ver la información completa de un          │

│   propietario para consultar sus datos de contacto                      │

│                                                                          │

│ ✓ Registrar nuevo propietario                                           │

│   Como recepcionista, quiero registrar un nuevo propietario con         │

│   sus datos básicos (nombre, dirección, teléfono)                       │

└─────────────────────────────────────────────────────────────────────────┘

  

┌─────────────────────────────────────────────────────────────────────────┐

│                  VISUALIZACIÓN DE VETERINARIOS                           │

├─────────────────────────────────────────────────────────────────────────┤

│ ✓ Ver listado de veterinarios                                           │

│   Como usuario, quiero ver el listado de veterinarios disponibles       │

│   y sus especialidades                                                   │

└─────────────────────────────────────────────────────────────────────────┘

```

#### **VERSIÓN ACTUAL (Completa)**

**Backbone extendido**

1. **Navegación básica**

2. **Gestión completa de propietarios**

3. **Gestión completa de mascotas**

4. **Gestión de visitas**

5. **Visualización de veterinarios**

**User Stories - Versión Actual v2.0**

```Python

┌─────────────────────────────────────────────────────────────────────────┐

│                        NAVEGACIÓN BÁSICA                                 │

├─────────────────────────────────────────────────────────────────────────┤

│ ✓ Ver página principal con información de bienvenida                    │

│ ✓ Navegar por el menú superior entre secciones                          │

│ ✓ Visualizar página de error (manejo de errores)                        │

└─────────────────────────────────────────────────────────────────────────┘

  

┌─────────────────────────────────────────────────────────────────────────┐

│                 GESTIÓN COMPLETA DE PROPIETARIOS                         │

├─────────────────────────────────────────────────────────────────────────┤

│ ✓ Buscar propietarios con búsqueda vacía (mostrar todos)               │

│ ✓ Buscar propietarios por apellido con autocompletado                   │

│ ✓ Ver listado paginado de propietarios (5 por página)                   │

│ ✓ Navegar entre páginas del listado                                     │

│ ✓ Ver ficha detallada de propietario con todas sus mascotas             │

│ ✓ Registrar nuevo propietario con validaciones                          │

│ ✓ Editar información de propietario existente                           │

│ ✓ Validar datos obligatorios (nombre, dirección, ciudad, teléfono)      │

│ ✓ Ver mensajes de confirmación de operaciones exitosas                  │

│ ✓ Ver mensajes de error en validaciones                                 │

└─────────────────────────────────────────────────────────────────────────┘

  

┌─────────────────────────────────────────────────────────────────────────┐

│                   GESTIÓN COMPLETA DE MASCOTAS                           │

├─────────────────────────────────────────────────────────────────────────┤

│ ✓ Registrar nueva mascota para un propietario                           │

│ ✓ Seleccionar tipo de mascota (cat, dog, bird, etc.)                    │

│ ✓ Establecer fecha de nacimiento de la mascota                          │

│ ✓ Validar nombre único de mascota por propietario                       │

│ ✓ Validar fecha de nacimiento (no puede ser futura)                     │

│ ✓ Ver listado de mascotas de un propietario en su ficha                 │

│ ✓ Editar información de mascota existente                               │

│ ✓ Ver historial de visitas de cada mascota                              │

└─────────────────────────────────────────────────────────────────────────┘

  

┌─────────────────────────────────────────────────────────────────────────┐

│                      GESTIÓN DE VISITAS                                  │

├─────────────────────────────────────────────────────────────────────────┤

│ ✓ Registrar nueva visita para una mascota                               │

│ ✓ Establecer fecha de la visita                                         │

│ ✓ Añadir descripción del motivo de la visita                            │

│ ✓ Ver historial completo de visitas por mascota                         │

│ ✓ Visualizar fecha y descripción de cada visita histórica               │

│ ✓ Ver mensajes de confirmación al agendar visita                        │

└─────────────────────────────────────────────────────────────────────────┘

  

┌─────────────────────────────────────────────────────────────────────────┐

│                VISUALIZACIÓN DE VETERINARIOS                             │

├─────────────────────────────────────────────────────────────────────────┤

│ ✓ Ver listado paginado de veterinarios (5 por página)                   │

│ ✓ Ver nombre de cada veterinario                                        │

│ ✓ Ver especialidades de cada veterinario                                │

│ ✓ Navegar entre páginas del listado                                     │

│ ✓ Acceder a listado en formato JSON vía API REST                        │

└─────────────────────────────────────────────────────────────────────────┘

```

### Diferencias Clave Entre MVP Y Versión Actual

| Aspecto | MVP | Versión Actual |

|---------|-----|----------------|

| **Propietarios** | CRUD básico, búsqueda simple | CRUD completo con paginación, validaciones avanzadas, mensajes de feedback |

| **Mascotas** | No incluido | CRUD completo, tipos predefinidos, validaciones de fechas y nombres únicos |

| **Visitas** | No incluido | Gestión completa de visitas con historial por mascota |

| **Veterinarios** | Solo visualización simple | Listado paginado con especialidades, API REST |

| **UX/UI** | Básica sin feedback | Mensajes de confirmación y error, paginación, navegación mejorada |

| **Validaciones** | Mínimas | Exhaustivas en todos los formularios |

---

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

CUANDO ingreso "Fra" en el campo de búsqueda de apellido

Y hago clic en el botón "Find Owner"

ENTONCES el sistema muestra todos los propietarios cuyo apellido comienza con "Fra"

Y esto incluye "Franklin", "Fraser", etc.

Y los resultados se muestran paginados

```

#### Reglas De Negocio

1. **Búsqueda case-insensitive:** La búsqueda no distingue entre mayúsculas y minúsculas

2. **Búsqueda por prefijo:** El sistema busca apellidos que comiencen con el texto ingresado

3. **Redirección automática:** Si solo hay un resultado, se redirige automáticamente a la ficha

4. **Paginación:** Los listados siempre muestran 5 resultados por página

5. **Sin autenticación:** El sistema es de acceso público, no require login

#### Información Técnica

**Endpoints involucrados:**

- `GET /owners/find` - Formulario de búsqueda

- `GET /owners?page={page}&lastName={lastName}` - Procesamiento de búsqueda

- `GET /owners/{ownerId}` - Ficha detallada del propietario

**Validaciones:**

- Apellido: campo opcional, texto alfanumérico

**Datos mostrados en la ficha del propietario:**

- Información personal: nombre completo, dirección, ciudad, teléfono

- Lista de mascotas: nombre, fecha de nacimiento, tipo

- Historial de visitas por mascota: fecha, descripción

#### Interfaz De Usuario

**Elementos del formulario de búsqueda:**

- Campo de texto para apellido

- Botón "Find Owner"

- Link "Add Owner" para registrar nuevo propietario

**Elementos de la página de resultados (lista):**

- Tabla con columnas: Name, Address, City, Telephone, Pets

- Nombres clickeables que enlazan a la ficha completa

- Controles de paginación: Previous/Next

- Indicadores de página actual y total de páginas

**Elementos de la ficha del propietario:**

- Tabla con información del propietario

- Botones de acción: "Edit Owner", "Add New Pet"

- Tabla de mascotas y visitas

- Links por mascota: "Edit Pet", "Add Visit"

#### Dependencias

- **Precondiciones:**

  - Base de datos debe estar inicializada

  - Deben existir tipos de mascotas predefinidos (cat, dog, bird, etc.)

- **Postcondiciones:**

  - Ninguna (operación de solo lectura)

- **Historias relacionadas:**

  - US-002: Registrar nuevo propietario

  - US-003: Editar información de propietario

  - US-004: Visualizar ficha completa del propietario

  - US-005: Registrar mascota para propietario

#### Notas Adicionales

- La búsqueda es tolerante y permite encontrar registros con coincidencias parciales desde el inicio del apellido

- El sistema mantiene la experiencia de usuario fluida mediante redirecciones automáticas cuando es apropiado

- La paginación mejora el rendimiento cuando hay muchos registros

- No se require autenticación, lo que facilita el acceso rápido en el entorno de recepción

#### Criterios De Prueba

**Datos de prueba sugeridos:**

- Propietario único: "George Franklin"

- Propietarios múltiples con apellido "Davis"

- Apellido inexistente: "XYZ"

- Búsqueda vacía para listar todos

- Búsqueda parcial: "Fra"

**Aspectos a verificar:**

- ✓ Rendimiento de búsqueda (< 2 segundos)

- ✓ Correcta paginación con 5 elementos por página

- ✓ Enlaces funcionales en todos los resultados

- ✓ Mensajes de error claros y apropiados

- ✓ Redirección automática con un solo resultado

- ✓ Responsive design en diferentes dispositivos