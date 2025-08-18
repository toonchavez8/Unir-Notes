Actividad 3. Integración y despliegue de una aplicación web

Las tres actividades que se llevarán a cabo en la asignatura Desarrollo Web Integral tienen como objetivo:

- Desarrollar un front-end haciendo uso de HTML5, CSS3, JavaScript y React.
- Desarrollar un back-end haciendo uso de una arquitectura orientada a microservicios, donde cada microservicio expondrá una API REST haciendo uso de Java, y Spring.
- Integrar ambas partes y desplegar front-End y back-end tanto en local como de forma pública.
- Hacer uso de bases de datos relacionales y del motor de búsqueda Elasticsearch.

Ilustración 1 - Arquitectura de la aplicación a desarrollar en la asignatura. Fuente: Elaboración propia

Esta tercera actividad consiste en la integración del front-end y el back-end realizado en las actividades anteriores y su despliegue mediante contenedores Docker.

**Pautas de elaboración**

En las dos actividades anteriores hemos construido:

- El front-end de una aplicación web (hasta ahora, con datos de prueba o mock).
- El back-end encargado de dar servicio a ese front-end (con referencias a máquinas locales), que se expone a través del servidor perimetral Cloud Gateway.

En esta actividad se deberá realizar lo siguiente:

- **Integrar el front-end y el back-end_._** Para esto será necesario modificar los componentes de React que se encargaban de acceder a los datos de prueba para que ahora hagan peticiones HTTP al back-end (**siempre al servidor perimetral**). Con las siguientes consideraciones:
    - El microservicio buscador dejará de usar una base de datos relacional y **pasará a utilizar un clúster de Elasticsearch** cuyo modelo de datos será similar al que se tenía en el modelo relacional. Debes **analizar** qué campos de tu modelo de datos del microservicio buscador pueden ser text, keyword, search-as-you-type…
    - El front-end debe **beneficiarse de este cambio en la implementación del back-end** (debe permitir búsquedas que utilicen internamente campos search as you type de Elasticsearch o búsquedas full-text, así como **facets**).
- **Desplegar todos los componentes de la arquitectura en local mediante contenedores Docker, a excepción del front-end, que estará desplegado de forma local, como se ha venido haciendo.** Tenemos los siguientes componentes desarrollados:
    - Front-end: una aplicación desarrollada con JavaScript y React.
    - Back-end: servidor perimetral Cloud Gateway, servidor de registro Eureka, microservicio buscador y microservicio operador.
- **Para llegar a la máxima nota será necesario desplegar todos los componentes de la arquitectura en Internet de forma pública haciendo uso de Vercel y Railway o herramientas similares (AWS, Azure…).**

La entrega consistirá en **un único archivo ZIP** que contendrá:

- **Vídeo memoria** **obligatoria** en formato MP4 de la actividad.
- **Proyectos con el código del front-end, Eureka, Cloud Gateway y microservicios.** Un directorio por proyecto, **sin comprimir**. Se incluye todo el contenido del proyecto **sin la carpeta target y sin la carpeta node_modules.**
- En caso de ser necesario, archivos SQL con sentencias DDL y DML necesarias para disponer del mismo conjunto de datos que se ha usado durante el desarrollo.

**Extensión y formato de la vídeo memoria**

La vídeo memoria tendrá una duración aproximada de 15 minutos y deberá visitar los siguientes aspectos de tu actividad:

1. **Modificaciones realizadas en el front-end:** se describirán brevemente las modificaciones que han sido necesarias en el front-end para lograr la integración con el back-end.
2. **Modificaciones realizadas en el back-end:** se describirán brevemente las modificaciones que han sido necesarias en el back-end para lograr la integración con el front-end y las consideraciones que se hayan tenido en cuenta para migrar del modelo relacional a Elasticsearch.
3. **Despliegue local:** se mostrarán los Dockerfile de los diferentes componentes del back-end, así como las evidencias de que la aplicación se está ejecutando correctamente.
4. **Despliegue remoto:** se mostrarán los diferentes componentes del back-end y front-end desplegados de forma pública, así como las evidencias de que la aplicación se está ejecutando correctamente.
5. **Conclusiones:** añade cualquier comentario que desees, así como _feedback_.

Rúbrica
# Rúbrica de Evaluación

## Criterio 7 – Ortografía
- Penalización de **-0.25 puntos** por cada cinco faltas de acentuación.  
- Penalización de **-0.10 puntos** por cada falta de ortografía.  

---

## Rúbrica de criterios técnicos

| Criterio | Descripción | Puntos |
|----------|-------------|--------|
| **Criterio 1. Modificación del microservicio buscador para utilizar Elasticsearch** | Las modificaciones realizadas no son suficientes y el código no se ejecuta correctamente. | 0 |
| | Las modificaciones realizadas funcionan pero el modelado de los datos no es correcto. | 0.75 |
| | Las modificaciones realizadas funcionan y el modelado de los datos es correcto. | 1.13 |
| | Las modificaciones realizadas funcionan, el modelado de los datos es correcto y se han tenido en cuenta consideraciones de seguridad para trabajar con las credenciales de acceso a Elasticsearch. | 1.5 |
| **Criterio 2. Uso de Elasticsearch para realizar sugerencias, correcciones o búsquedas full-text** | No se realizan sugerencias, correcciones ni búsquedas full-text. | 0 |
| | Se realizan búsquedas full-text sobre muy pocos atributos. | 0.75 |
| | Se realizan búsquedas full-text sobre todos los atributos sobre los que tiene sentido. | 1.13 |
| | Se realizan búsquedas full-text sobre todos los atributos sobre los que tiene sentido, así como la posibilidad de implementar correcciones o sugerencias. | 1.5 |
| **Criterio 3. Uso de Elasticsearch para implementar facets** | No se utilizan facets. | 0 |
| | Se utilizan facets para un número limitado de atributos. | 0.75 |
| | Se utilizan facets para todos los atributos que lo puedan necesitar. | 1.13 |
| | Se utilizan facets para todos los atributos que lo puedan necesitar. Los rangos devueltos son adecuados y permiten un buen nivel de experiencia de búsqueda. | 1.5 |
| **Criterio 4. Integración de front-end y back-end en local** | No se realiza. | 0 |
| | Se realiza con fallos en menos de dos componentes. | 1.25 |
| | Se realiza sin fallos. | 1.88 |
| | Se realiza sin fallos y el CORS está configurado a nivel GW. | 2.5 |
| **Criterio 5. Modificación del estilo con CSS** | No se realiza. | 0 |
| | Se realiza correctamente para front o back, pero no ambos. | 1 |
| | Se realiza correctamente para front y back. | 1.5 |
| | Se realiza correctamente para front y back. El CORS está configurado a nivel GW y únicamente el GW es accesible públicamente. | 2 |
| **Criterio 6. Vídeo memoria obligatoria** | No hay vídeo memoria. | 0 |
| | Vídeo memoria demasiado corto o que no cubre todos los aspectos. | 0.5 |
| | Vídeo memoria que cubre todos los aspectos pero no entra en detalle en ellos. | 0.75 |
| | Duración adecuada y cobertura de todos los aspectos solicitados. | 1 |
