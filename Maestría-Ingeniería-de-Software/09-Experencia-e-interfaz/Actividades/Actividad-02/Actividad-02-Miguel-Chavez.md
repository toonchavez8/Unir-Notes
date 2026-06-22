# Actividad 2. Metodologías Y Elementos Del Proceso De Diseño UX

**Universidad:** Universidad Internacional de La Rioja  
**Asignatura:** Experiencia e interfaz de usuario  
**Actividad:** Actividad 2. Metodologías y elementos del proceso de diseño UX  
**Proyecto:** UNIR Dev  
Miguel De Jesus Chavez Barraan
**Docente:** [Escribe el nombre del docente, si aplica]  
**Fecha:** [Escribe la fecha de entrega]

## 1. Introduccion

## 2. Contexto Del Proyecto

## 3. Brief Del Proyecto

### 3.1 Nombre Del Proyecto

Unir Dev

### 3.2 Descripcion

La Plataforma que poponmos es UNIR Dev que es orientada a estudientes profssionats de IT y proveeeedores techonologies. Nuestro Objetivo es centralizar rcuros, herramintas, tendencias, productos y servicios relacionanso con el mundo de dessarollo, technologias emeergentes apoyando a la busqueda compracion y consulta de information.

### 3.3 Puntos De Estress

Con esta applicacion buscamos eliminar la disperasion de ifnoramcion, recursos, y servicios tecnologicos que existe entre vaarios sitios. Estaa disprerson causa dificultad entre usarios para comprar opcions y que encuentren los recursos confiales y encontrar provedores relevantes.

Ademas, los proveedores tecnoloicos necesitan espacios donde peudan presentar sus productos.

### 3.4 Objetivo Del Proyecto

Dado a los puntos de streess nustro objtivo es crear un experencia organiada y facil de navegar que permita consultar los recursos tenconiologios y descrubir las tentencias recientes y conectar con productos y servicios del sector.

### 3.5 Mercado Target

La plataforma se dirige a tres públicos principales:

- **Estudiantes de UNIR:** usuarios que buscan recursos de aprendizaje, guías, tutoriales y herramientas para fortalecer sus conocimientos.
- **Profesionistas de TI:** usuarios que desean actualizarse, comparar soluciones y consultar tendencias aplicables a su trabajo.
- **Proveedores tecnológicos:** empresas o profesionales que desean promocionar productos, servicios, capacitaciones o soluciones digitales.

### 3.6 Propuesta De Valor

La plataforma de unir dev ofrece una experenica dentrada en descrubir, consultar, y guardar recursos tecnologios.. El valor principal es reunir cntenido educativo, tendencias, y srevicios en el mismmo entorno con navegacion sencilla y atraves de arquitectura de information generar un organizacion clara.

### 3.7 Funcioanlidades Principlaes

Las funcionalidades principales propuestas son:

- Buscador global de recursos, herramientas, proveedores y tendencias.
- Categorías tecnológicas destacadas.
- Sección de recursos educativos.
- Marketplace de productos y servicios.
- Filtros por tema, nivel, tipo de contenido y tecnología.
- Perfil de usuario con favoritos e historial.
- Sección de recomendaciones.
- Botones de contacto para proveedores.

## 4. Publico Objetivo

Definicion de persnas 

### 4 .1 Estudiantes De Unir

Los estudiantes necesitan una plataforma que les permita encontrar recursos confiables sobre desarrollo web y nuevas tecnologías. Este grupo valora la claridad, la organización del contenido y la posibilidad de guardar materiales para consultarlos posteriormente.

**Necesidades principales:**

- Acceder a guías y tutoriales.
- Consultar herramientas recomendadas.
- Entender tendencias tecnológicas.
- Guardar recursos para estudio posterior.

#### 4.1.1 Persona Estudiante

**Nombre:** Andrea Martínez  
**Edad:** 28 años  
**Perfil:** estudiante de maestría relacionada con tecnología.  
**Objetivo:** encontrar recursos claros para aprender sobre desarrollo web y herramientas digitales.  
**Frustración:** la información está dispersa en muchos sitios y no siempre identifica cuáles recursos son confiables.  
**Necesidad en UNIR Dev:** contar con categorías claras, buscador, recursos recomendados y favoritos.

### 4.2 Profesionistas De TI

Los profesionistas de TI buscan información actualizada, útil y aplicable a proyectos reales. Este grupo necesita comparar tecnologías, descubrir herramientas y encontrar servicios que puedan resolver necesidades laborales.

**Necesidades principales:**

- Comparar herramientas.
- Consultar tendencias actuales.
- Encontrar servicios especializados.
- Filtrar información de acuerdo con intereses concretos.

#### 4.2.1 Persona: Profesionista De TI

**Nombre:** Carlos Ríos  
**Edad:** 35 años  
**Perfil:** desarrollador web con interés en actualizarse.  
**Objetivo:** comparar herramientas y consultar tendencias aplicables a su trabajo.  
**Frustración:** pierde tiempo revisando diferentes fuentes para encontrar información útil.  
**Necesidad en UNIR Dev:** filtros, tarjetas comparables, recursos relacionados y búsqueda eficiente.

### 4.3 Proveedores Tecnológicos

Los proveedores requieren visibilidad ante usuarios interesados en tecnología. Para ellos, la plataforma debe ofrecer espacios claros para mostrar productos, servicios y datos de contacto.

**Necesidades principales:**

- Publicar productos o servicios.
- Mostrar beneficios.
- Captar usuarios interesados.
- Facilitar el contacto comercial.

#### 4.3.1 Persona: Proveedor Tecnológico

**Nombre:** Laura Hernández  
**Edad:** 40 años  
**Perfil:** representante de una empresa de servicios cloud.  
**Objetivo:** promocionar servicios tecnológicos ante una audiencia interesada.  
**Frustración:** le cuesta llegar a usuarios especializados.  
**Necesidad en UNIR Dev:** perfil de proveedor, catálogo de servicios y acciones de contacto visible.

## 5. Objetivos De la Interfaz

Los objetivos UX definidos para la propuesta son los siguientes:

1. Facilitar la búsqueda de recursos tecnológicos en pocos pasos.
2. Organizar la información mediante categorías comprensibles.
3. Permitir la exploración de tendencias, herramientas y servicios.
4. Reducir la carga cognitiva del usuario mediante una interfaz clara.
5. Ofrecer filtros útiles para encontrar información específica.
6. Permitir guardar recursos mediante una sección de favoritos.
7. Facilitar el contacto con proveedores tecnológicos.
8. Mantener una navegación consistente en todas las pantallas.

## 6. Arquitectura De Information

La arquitectura de información propuesta organiza la plataforma en siete secciones principales: Inicio, Tendencias tecnológicas, Recursos, Marketplace, Comunidad, Perfil y Contacto.

```text
UNIR Dev
|
|-- Inicio
|   |-- Buscador principal
|   |-- Categorías destacadas
|   |-- Recomendaciones
|   |-- Tendencias recientes
|
|-- Tendencias tecnológicas
|   |-- Inteligencia artificial
|   |-- Desarrollo web
|   |-- Cloud computing
|   |-- Ciberseguridad
|   |-- DevOps
|
|-- Recursos
|   |-- Guías
|   |-- Tutoriales
|   |-- Cursos recomendados
|   |-- Herramientas
|   |-- Artículos
|
|-- Marketplace
|   |-- Productos
|   |-- Servicios
|   |-- Proveedores destacados
|   |-- Comparador de soluciones
|
|-- Comunidad
|   |-- Eventos
|   |-- Foros
|   |-- Casos de éxito
|   |-- Preguntas frecuentes
|
|-- Perfil
|   |-- Mis favoritos
|   |-- Historial
|   |-- Preferencias
|   |-- Alertas
|
|-- Contacto
    |-- Formulario
    |-- Soporte
    |-- Información institucional
```

La arquitectura se divide entre las principales neecesidades de los usarios. La seccion de recuros atiende a ls estudiantes que buscan aprendizaje. La seccion de tendndicas technologis primte explroar temas actuales. El MarquetePlace separa los productos y servicios cmerciales evitando mezclarlos ccn contenid educativo. La seccion de perfil permite personal personalizar la exprencia mediante favoritos, historial, prgreso, y preferencias.

Esta organizacion facilita la navgacion porque cada seccion tiene un proposito claro y reduce la posibles que el usario se pierda dentro la plataforma.

## 7. Estrategia De Navegacion Y Experiencia De Usuario

Para mantener el interés del usuario y facilitar la navegación, se proponen los siguientes elementos de interfaz:

- **Menú superior fijo:** permite acceder a las secciones principales desde cualquier pantalla.
- **Buscador global:** facilita la búsqueda directa de recursos, servicios o tendencias.
- **Categorías destacadas:** ayudan al usuario a explorar sin necesidad de conocer términos específicos.
- **Filtros laterales:** permiten ordenar resultados por tipo, nivel, tecnología o proveedor.
- **Tarjetas de contenido:** muestran información resumida y acciones claras.
- **Favoritos:** permiten guardar recursos importantes.
- **Recomendaciones:** sugieren contenidos relacionados con los intereses del usuario.
- **Migas de pan:** ayudan a entender la ubicación dentro del sitio.
- **Botones de acción claros:** guían al usuario hacia acciones como ver, guardar o contactar.

Esta estrategia busca que la experiencia sea comprensible, eficiente y útil para los distintos tipos de usuarios.

### 7.1 Flujo Para Estudiante

```text
Inicio
-> Buscador
-> Resultados
-> Filtro por tipo: Guías
-> Recurso seleccionado
-> Guardar en favoritos
```

Este flujo permite que un estudiante encuentre rápidamente una guía o tutorial y lo guarde para consultarlo después.

### 7.2 Flujo Para Profesionista De TI

```text
Inicio
-> Tendencias tecnológicas
-> Cloud computing
-> Filtro por herramientas
-> Detalle de herramienta
-> Recursos relacionados
```

Este flujo facilita la exploración de tecnologías actuales y permite revisar contenidos relacionados con una necesidad professional.

### 7.3 Flujo Para Proveedor

```text
Inicio
-> Marketplace
-> Proveedores
-> Perfil de proveedor
-> Publicar servicio
-> Vista previa
-> Publicación
```

Este flujo permite que un proveedor publique o presente sus servicios ante usuarios interesados en soluciones tecnológicas.

## 8. Wireframes

**Objetivo de la pantalla:** presentar la plataforma, permitir búsqueda rápida y mostrar categorías principales.

**Elementos principales:**

- Pantalla de inicio.  
- Pantalla de búsqueda o filtrado
- Pantalla de detalle de recurso, curso, producto o servicio.
- Pantalla de rutas de aprendizaje.
- Pantalla de contacto, registro o solicitud de información.
- Pantalla de Perfil 
- Pantalla de Marketplace

## 10. Conclusiones

## 11. Referencias