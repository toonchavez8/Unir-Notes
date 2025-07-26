# 🧠 **Notas De Estudio: Cálculo Del Camino Crítico Y Holgura**

## 🔢 ¿Qué Es El Camino Crítico?

El **Camino Crítico** (Critical Path) es la secuencia de actividades que **determina la duración mínima del proyecto**. Si alguna actividad en esta ruta se retrasa, todo el proyecto se retrasa.

---

![[Pasted image 20250625120640.png]]

## 🧮 **Cálculo Paso a paso**

1. **Fechas más tempranas**:
    
    - Se parte de la primera tarea (inicio en tiempo 0).
        
    - Se suman las duraciones hacia adelante, considerando dependencias.
        
    - Si una tarea tiene múltiples predecesoras, se elige la **fecha más tardía** de finalización de entre ellas.
        
2. **Fechas más tardías**:
    
    - Se parte de la última tarea (fin del proyecto) y se restan las duraciones hacia atrás.
        
    - Si una tarea tiene múltiples sucesoras, se elige la **fecha más temprana** de inicio entre ellas.
        
3. **Holgura (Slack)**:
    
    $$
	Holgura=Inicio mas tardio−Inicio mas temprano
$$
    - **Holgura = 0** → La tarea está en el **camino crítico**.
        

---

### 🧱 **Ruta Crítica En Este proyecto**

Según el diagrama y los datos compartidos:

```mermaid
graph TD
    T1((T1)) --> T2((T2))
    T2 --> T5((T5))
    T5 --> T8((T8))
    T8 --> T9((T9))
    T9 --> T10((T10))
    T10 --> T11((T11))

    classDef critical fill:#ffdddd,stroke:#ff0000,stroke-width:2px;
    class T1,T2,T5,T8,T9,T10,T11 critical;
```

🔴 Tareas en la **ruta crítica**: `T1 → T2 → T5 → T8 → T9 → T10 → T11`

📌 Todas tienen **holgura = 0**  
📌 Duración total del proyecto: **52 unidades de tiempo**

---

### 📊 Holgura En Otras Tareas

|Tarea|Holgura|
|---|---|
|T3|18|
|T4|24|
|T6|3|
|T7|18|

Estas tareas **pueden retrasarse** sin afectar la fecha final del proyecto, siempre y cuando no excedan su holgura.

---

### 🛠 Herramientas Mencionadas

- **Airtable**: Combina hoja de cálculo + base de datos. Útil para gestionar alcance y recursos.
    
- **Clockify**: Software de código abierto para cronogramas, tareas, y seguimiento del tiempo. Alternativa a Microsoft Project.
    

---

## 🧾 Conclusión

Este análisis te permite:

- Saber **cuáles actividades no deben retrasarse.**
    
- Identificar **holguras** para manejar recursos con más flexibilidad.
    
- Estimar la **duración total del proyecto** de forma realista.
    
- Visualizar dependencias y planificar el **seguimiento y control** del tiempo.
    

---

## MicroTest

- Elige el concepto de camino crítico entre los siguientes:
	-C. Viene determinado por la secuencia de actividades de mayor duración, Teniendo en cuenta las relaciones entre ellas.
- Cuando una actividad forma parte del camino, ¿cuánto es su holgura?:
	- Igual a 0.
- ¿Qué define la holgura?:
	- El número de periodos de tiempo que puede retrasarse una actividad sin afectar a la duración total del proyecto.