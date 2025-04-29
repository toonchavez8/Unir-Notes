
# Notas De Clase – Proceso De Desarrollo De Software

## Concepto De Proceso De Desarrollo

- Un **proceso** define **quién have qué, cuándo y cómo** para alcanzar un objetivo.
    
- En **ingeniería de software**, el objetivo es **desarrollar**, **modificar** o **ampliar** un producto de software.
    
- La aplicación de un proceso busca **mejorar** la forma de trabajar, haciéndola **más disciplinada** y **sistemática** para **prevenir** y **resolver problemas**.
    

## Definiciones De Proceso De Desarrollo De Software

- **Jacobson, booch y Rumbaugh:** Conjunto de actividades necesarias para **transformar requisitos** de usuario en un sistema de software.
    
- **Somerville:** Actividades que **conducen** a la **creación** de un producto software.
    
- **Pressman:** Conjunto de **actividades estructurales**, **acciones de ingeniería** y **tareas** asociadas al trabajo, productos generados, puntos de **aseguramiento de calidad** y evaluación de advance.
    
- **Humphrey:** Conjunto de **herramientas**, **métodos** y **prácticas** utilizadas para crear software.
    

## Artefactos

La ejecucion de cualquier tipo de proceso de desarollo de software va a generar dos tipos de artefactos

- Son **piezas de información** utilizadas o producidas en el proceso.
    
- Hay artefactos **internos** y artefactos **integrables** al cliente.
    

## Motivación Del Proceso

- Mejora de la forma de trabajar.
    
- Facilita la **prevención** de problemas.
    
- Enfocado en aspectos como:
    
    - **Calidad**.
        
    - **Tecnología del producto**.
        
    - **Inestabilidad de requisitos**.
        
    - **Complejidad de sistemas**.
        

---
Todo proceso de desarrollo de software debe definir el problema para favorecer su comprensiön y
disefiar su soluciön. Para ello, tal y como se muestra a continuaciön, se partirå de un conjunto de
Requisitos que ha de set capaz de transformarse en un producto software que los satisfaga.


# Actividades Fundamentales Del Proceso (según Somerville)

1. **Especificación del software:**
    
    - Definición y comprensión de requisitos.
        
2. **Desarrollo del software:**
    
    - Diseño y construcción.
        
3. **Validación del software:**
    
    - Asegurar que el producto cumple los requisitos.
        
4. **Evolución del software:**
    
    - Modificación ante nuevas necesidades o entornos.
        

---

# Procesos Generales
Cada actividad comprenderå, a su vez, un conjunto de tareas que deberån set realizadas por recursos concretos, no siempre necesariamente humanos. Estas tareas se podran organizar de distinta manera
En el tiempo y con diferente nivel de detalle segun las caracteristicas y la complejidad del software a Desarrollan Estas actividades se suelen complementar con Otras tareas o procesos que se aplican a Io largo de todo El desarrollo: seguimiento y control, gestiön del riesgo, aseguramiento de la calidad, revisiones técnicas,
Mediciån, gestiån de la configuracion, gestion de la reutilizaciön, etc.
## 1. Proceso De Toma De Requisitos

- Obtención, **análisis**, **especificación** y **validación** de requisitos.
    
- **Gestión de requisitos** a lo largo de todo el ciclo de vida.
    
- Proyectos son **extremadamente vulnerables** si esta etapa falla.
    
- Los requisitos deben **mantenerse** relacionados con diseño, pruebas y mantenimiento.
    

## 2. Proceso De Diseño

- Definición de **arquitectura**, **components**, **interfaces** y otras características.
    
- Produce **modelos** que son **borradores** de la solución.
    
- Estos modelos se **analizan y evalúan** para cumplir los requisitos.
    

## 3. Proceso De Construcción

- Creación detallada mediante **codificación**, **verificación**, **pruebas de unidad**, **integración** y **depuración**.
    
- Produce muchos **elementos de configuración** (archivos fuente, documentación, casos de prueba).
- Esta vinculado con el proceso de diseño de software y a las prubas de software.

## 4. Proceso De Pruebas

- **Verificación dinámica** de que el software funciona como se espera.
    
- Las pruebas deben empezar desde **etapas tempranas** del ciclo de vida.
    
- Planificación y diseño de pruebas ayudan a:
    
    - Detectar **descuidos**.
        
    - Corregir **incoherencias** de diseño.
        
    - Evitar **omisiones** y **ambigüedades**.
        

## 5. Proceso De Mantenimiento

- Empieza **después** de la implementación y entrega.
    
- Incluye:
    
    - **Modificaciones** por defectos encontrados.
        
    - Adaptaciones a **cambios de entorno**.
        
    - Satisfacción de **nuevos requisitos**.
        
- Actividades de mantenimiento:
    
    - **Antes** de la entrega: planificación, capacidad de mantenimiento, determinación logística para las actividades de transición.
        
    - **Después** de la entrega: cambios, capacitación, soporte, ampliación con otro sistema de software.
        

## 6. Proceso De Gestión De Calidad

- Conjunto de procesos para **garantizar la calidad** del software, servicios y procesos de ciclo de vida.
    
- Involucra:
    
    - Definir procesos.
        
    - Definir requisitos de calidad.
        
    - Medir y retroalimentar.
        


---

## 📝Microtest

- ¿Qué define un proceso?
	- Un proceso define quién está haciendo qué, cuándo y cómo para alcanzar un determinado objetivo.
- El objetivo principal del proceso de desarrollo de software es:
	- Mejorar la forma de trabajar a la hora de desarrollar software, favoreciendo la prevención y resolución de posibles problemas que puedan surgir.
- ¿Qué es un artefacto software?
	- Pieza de información que se produce o se necesita en un proceso de desarrollo de software.

## Lectura Accional: [La Crisis Del Software](https://www.youtube.com/watch?v=KwbUPqPlc3E&t=15s)
### La Crisis del Software: Un Resumen

El video discute la crisis del software, un término acuñado a finales de la década de 1960 para describir las dificultades en el desarrollo de proyectos de software grandes y complejos.

* **Orígenes de la Crisis:** La crisis surgió a medida que los proyectos de software se volvieron cada vez más complejos, lo que llevó a problemas como:
    * Excesos de costos [00:01:14]
    * Retrasos en el cronograma [00:01:14]
    * Mala calidad del software [00:01:14]
    * Software no confiable [00:07:45]

* **Figuras y Eventos Clave:**
    * **Edger Dijkstra:** Un destacado científico de la computación que habló sobre la crisis en una reunión del Comité de Ciencia de la OTAN en 1968 [00:00:27]. Criticó a la industria y destacó la diferencia entre adaptarse a los problemas cambiantes y simplemente corregir errores [00:00:35].
    * **Conferencia de 1968 sobre Ingeniería de Software:** Marcó la primera admisión abierta de la crisis del software [00:03:39].
    * **Fred Brooks:** Autor de "El mítico hombre-mes" (1975), que discutió las falacias de agregar mano de obra a proyectos de software retrasados [00:05:14].

* **Errores Comunes en el Desarrollo de Software:**
    * **El mítico hombre-mes:** La idea errónea de que agregar más personas a un proyecto tardío hará que termine antes [00:04:04].
    * **Pruebas inadecuadas:** Omitir o reducir las pruebas para acelerar los plazos del proyecto, lo que puede tener consecuencias graves [00:08:12].

* **Consecuencias en el Mundo Real:** El video cita varios ejemplos de fallas de software que tuvieron repercusiones significativas:
    * **Therac-25:** Una máquina de radioterapia que causó muertes y lesiones debido a errores de software [00:09:36].
    * **Fallo del misil Patriot:** Un error de software provocó el fallo en la interceptación de un misil Scud, lo que resultó en bajas [00:09:54].
    * **Apagón del noreste de 2003:** Un problema de software en el sistema de alarma contribuyó a un corte de energía generalizado [00:10:17].
    * **Accidentes del Boeing 737 MAX:** El mal funcionamiento del software en el sistema MCAS provocó accidentes aéreos fatales [00:10:39].

* **Estado Actual:** El video concluye preguntando si la crisis del software es cosa del pasado o un problema continuo [00:11:11].