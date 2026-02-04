# Actividad 3: Automatización De Pruebas De Aceptación, Funcionales, De Sistema Y De Carga

---

## Objetivos

Con esta actividad pondrás en práctica la automatización de las pruebas de un sistema, tanto a nivel de validación (pruebas de aceptación) como de verificación (pruebas funcionales y de sistema).

Para ello, trabajaremos en grupo para generar la automatización de las pruebas sobre la solución **Pet-Clinic** con la que hemos trabajado en las actividades anteriores. Al hacer uso de las plataformas de automatización de pruebas que quieras y al justificar la decisión y aprendizaje (qué aspectos valoras mejor y cuáles han sido más difíciles), cubriremos los aspectos de pruebas de la interfaz, el _back-end_ y el rendimiento, entre otros.

---

## Descripción De la Actividad

**Pet-Clinic** es un proyecto de ejemplo clásico para aprender a programar con el _framework_ Spring de Java. Para esta práctica haremos uso de dos extensions de este para tener una arquitectura cliente servidor.

### Acceso a Repositorios

Accede al _back-end_ en el siguiente enlace:  
[https://github.com/spring-petclinic/spring-petclinic-rest](https://github.com/spring-petclinic/spring-petclinic-rest)

Accede al _front-end_ en el siguiente enlace:  
[https://github.com/spring-petclinic/spring-petclinic-angular](https://github.com/spring-petclinic/spring-petclinic-angular)

---

## Instalación Y Ejecución

Instalando Java, un cliente Git y Maven, así como Node.js, desde el repositorio GitHub anterior, tenemos las instrucciones para descargar el código, construirlo y ejecutarlo.

### Back-end

Primero lanzamos el _back-end_ con:

```Python
./mvnw spring-boot:run
```

(o `mvnw.cmd` en Windows)

Comprobamos que los servicios están activos mediante Swagger en:  
[http://localhost:9966/petclinic/swagger-ui/index.html](http://localhost:9966/petclinic/swagger-ui/index.html)

![mexingsof03_act3](Maestría-Ingeniería-de-Software/06-Plataforma-desarrollo-software/Actividades/Actividad_03/Attachments/mexingsof03_act3.jpeg)

---

### Front-end

Después lanzaremos el _front-end_ con:

```Python
ng serve
```

Comprobamos que podemos acceder al interfaz gráfico desde:  
[http://localhost:4200/petclinic/welcome](http://localhost:4200/petclinic/welcome)

![[mexingsof03_act3 1.jpeg]]

---

## Objetivo De Las Pruebas

Lo que queremos es automatizar la **verificación** (funciona bien) y la **validación** (hace lo que esperábamos) del sistema:

### Validación Y Pruebas De Aceptación

Es preciso documentar un caso de uso o funcionalidad (por ejemplo, buscar una mascota o veterinario, dar de alta una visita, etc.), definir los criterios de aceptación de esta y automatizar las pruebas mostrando las evidencias de que se cumplen.

### Verificación Mediante Pruebas De Sistema

Necesitamos set capaces de automatizar el testeo de alguna de las interfaces REST del _back-end_ para comprobar que funcionan correctamente.  
Dada una entidad, se debe reproducir una prueba que contenga este flujo de tareas:

- Buscar la entidad (no estaba)
    
- Añadir la entidad (datos de ejemplo que quieras)
    
- Volver a buscar (está y todos los datos han sido guardados bien)
    
- Editar y cambiar algún dato
    
- Volver a buscar (está y el dato ha sido modificado)
    
- Eliminar la entidad
    
- Volver a buscar (no está)

### Verificación Mediante Pruebas Funcionales

Necesitamos set capaces de automatizar el testeo de alguna de las interfaces web con las que el usuario accede a la aplicación al rellenar los datos de un formulario y comprobando los resultados.

### Verificación Mediante Pruebas De Carga

Supongamos que había un requisito no funcional de que mil personas pueden a la vez realizar una consulta de alguna de las entidades en menos de cinco segundos.  
Necesitamos automatizar las pruebas de carga del sistema para comprobar que cumplimos este requisito.

---

## En Esta Actividad Grupal Debes

- Identificar y analizar qué plataformas de testeo se adaptan a vuestra necesidad y elegir diferentes para cubrir:
    
    - Pruebas de aceptación (validación)
        
    - Pruebas de API REST
        
    - Pruebas de interfaces de usuario web
        
    - Pruebas de carga
        
- Desarrollar los _scripts_ y test automatizados utilizando esas plataformas.
    
- Obtener evidencias de las pruebas realizadas.
    
- Documentar el proceso y justificar la elección de plataforma, aprendizaje y dificultades.
    
- Preparar una presentación para compartir con el resto de los compañeros, en menos de diez diapositivas, cómo has enfocado cada una de las pruebas y qué conclusiones y aprendizaje has obtenido.

---

## Extensión Y Formato

La entrega consistirá en un único fichero comprimido que debe container lo siguiente:

- Memoria técnica del trabajo realizado que exponga el proceso, que comience con la justificación de la elección de las plataformas.  
    **Extensión máxima:** veinticinco páginas en un documento PDF, tipo de letra Georgia, tamaño 11 e interlineado 1,5.
    
- Capturas o enlaces que permitan evidenciar el trabajo realizado con las plataformas de testeo automatizado.
    
- Apartado final de conclusiones con su valoración personal de aprendizaje, qué aspectos han sido positivos en el proceso y cuáles han sido más difíciles.
    
- Si las plataformas utilizadas permiten su exportación se pueden aportar los ficheros fuente de estas, pero en todo caso es necesario incluir capturas de pantalla o enlaces en la memoria que permitan evidenciar el trabajo sin necesidad de instalar las plataformas utilizadas.
    
- Presentación para compartir la experiencia y los resultados con el resto de los compañeros.