
---

# 📚 Notas De Clase: Gestión Del Alcance Y Del Cronograma

---

## 📌 1. ¿Qué Es El Alcance En Gestión De Proyectos?

El **alcance** se divide en dos partes:

|Tipo de Alcance|Definición|
|---|---|
|**Alcance del producto**|Características y funciones del producto, servicio o resultado del proyecto.|
|**Alcance del proyecto**|Todo el trabajo requerido para entregar el producto. Incluye el alcance del producto.|

🔹 **Importancia**: Un buen control del alcance asegura el cumplimiento de expectativas y el éxito del proyecto.

---

## 📋 2. Requisitos Del Proyecto

Los **requisitos** pueden clasificarse en:

- 🏢 **Requisitos de negocio**: Necesidades y deseos de la organización.
    
- 🛠 **Requisitos técnicos**: Funcionalidades que hacen possible cumplir los objetivos.

Todos son **igualmente importantes** y deben set **satisfechos para completar el proyecto con éxito**.

---

## ⚙️ 3. Procesos De la Gestión Del Alcance

Según la **guía del PMBOK**, los procesos relacionados con el alcance son:

1. **Planificar la gestión del alcance**
    
2. **Recopilar requisitos**
    
3. **Definir el alcance**
    
4. **Crear la EDT (WBS)**
    
5. **Validar el alcance**
    
6. **Controlar el alcance**

---

## 🧩 4. Tipos De Entregables

Los entregables pueden set:

|Nivel|Ejemplos|
|---|---|
|**Contrato / oferta**|Propuestas, facturación, pedidos.|
|**Ejecución del proyecto**|Diseños, listas de materiales, manuales.|
|**Gestión del proyecto**|Acta de constitución, plan del proyecto, informes, métricas, cronograma.|

Cada entregable puede set **tangible o intangible**.

---

## ⏱️ 5. Gestión Del Tiempo (Cronograma)

**Objetivo**: Asegurar la finalización del proyecto a tiempo, controlando duración, dependencias y recursos.

---

## 🛠 Procesos De Gestión Del Cronograma

|Proceso|Descripción|
|---|---|
|**Planificar gestión del cronograma**|Definir políticas, herramientas y documentación necesaria.|
|**Definir actividades**|Identificar acciones necesarias para completar el proyecto.|
|**Secuenciar actividades**|Establecer el orden lógico y dependencias entre tareas.|
|**Estimar recursos**|Determinar tipo y cantidad de recursos necesarios para cada actividad.|
|**Estimar duración**|Cuánto tiempo tomará cada actividad, según recursos asignados.|
|**Desarrollar cronograma**|Integrar toda la información para crear la línea base del cronograma.|
|**Controlar cronograma**|Comparar advances reales con el plan y gestionar los cambios.|

---

## 📊 Herramientas De Apoyo

1. **Diagrama de Gantt**  
    Muestra fechas de inicio y fin de cada tarea, útil para seguimiento visual.
    
2. **Ruta Crítica (CPM - Critical Path Method)**  
    Identifica las tareas sin margen de retraso (**holgura = 0**) que **determinan la duración del proyecto**.

    ```mermaid
    graph TD
      A[Definir actividades] --> B[Secuenciar actividades]
      B --> C[Estimar recursos]
      C --> D[Estimar duración]
      D --> E[Desarrollar cronograma]
      E --> F[Controlar cronograma]
    
      classDef critical fill:#ffdddd,stroke:#ff0000,stroke-width:2px;
      class A,B,C,D,E,F critical;
    ```

---

## 📌 Conclusión

Una gestión adecuada del alcance y del cronograma permite:

✅ Entregar el producto correcto  
✅ Cumplir los tiempos comprometidos  
✅ Controlar desviaciones y gestionar cambios  
✅ Mejorar la comunicación entre el equipo y los interesados
