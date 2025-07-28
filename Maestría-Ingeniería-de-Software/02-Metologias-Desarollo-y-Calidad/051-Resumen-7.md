# 📌 Introducción a Scrum

- Scrum es un **marco de trabajo ágil** para el desarrollo de software.
    
- Promueve la **entrega incremental** de productos funcionales en _sprints_.
    
- Sigue los **valores del Manifiesto Ágil**: colaboración, adaptabilidad, entrega continua.

---

# 🎯 Enfoque General Y Filosofía Ágil

- Acepta cambios frecuentes en los requisitos.
    
- El cliente (**Product Owner**) establece prioridades y puede renegociar si hay cambios.
    
- Equipos autoorganizados, enfocados en entregas frecuentes.
    
- La **planificación del sprint** marca el inicio de cada iteración.

---

# 👥 Roles En Scrum

## 🐷 Roles Comprometidos ("Pigs")

- **Product Owner (PO)**: Define y prioriza el _product backlog_.
    
- **Scrum Master**: Guía el proceso, elimina impedimentos.
    
- **Equipo de desarrollo**: Multifuncional, se encarga de programar, probar, desplegar, etc.

## 🐔 Roles Informados ("Chickens")

- Clientes, contabilidad, otros stakeholders no involucrados directamente.

---

# 📆 Reuniones Scrum

- **Sprint Planning**: Define objetivo y tareas → genera el _sprint backlog_.
    
- **Daily Scrum**: 15 minutos diarios, sincronización del equipo.
    
- **Sprint Review**: Al final del sprint, se presenta el incremento a stakeholders.
    
- **Sprint Retrospective**: Mejora continua del proceso.

> 🖼️ Ver esquema detallado del modelo Scrum:  
> ![[Pasted image 20250726221651.png]]

---

# 📦 Artefactos En Scrum

- **Product Backlog**:
    
    - Lista priorizada de funcionalidades.
        
    - Evoluciona constantemente.
        
    - Redactado en lenguaje claro para el cliente.
        
    - Estimado en tamaño/duración.

> 🖼️ Representación visual:  
> ![[Pasted image 20250726221421.png]]

- **Sprint Backlog**:
    
    - Subconjunto de historias del product backlog para el sprint actual.
        
    - Se descompone en tareas menores (máx. 16h por tarea).

> 🖼️ Tabla ejemplo de tareas:  
> ![[Pasted image 20250726221436.png]]

- **Incremento**:  
    Resultado funcional entregable.

---

# 🧩 Características Del Product Backlog (según Pichler, 2010)

1. **Granularidad**: más detalle para tareas prioritarias.
    
2. **Evolutivo**: se adapta con cada entrega.
    
3. **Estimaciones abstractas**: ayudan a la priorización y planificación.
    
4. **Comprensión común del sistema por parte de los stakeholders**.

---

# 🧾 Historias De Usuario (según Kniberg, 2007)

Campos clave:

- **Identificador**: único.
    
- **Nombre**: descripción breve.
    
- **Importancia**: prioridad asignada por el PO.
    
- **Estimación inicial**: esfuerzo estimado por el equipo.
    
- **Pruebas**: criterios de validación.
    
- **Notas**: info adicional relevante.

---

# 🌀 Iteraciones Y Duración De Sprints

- Sprint: duración fija (1 a 4 semanas), operativa y desplegable.
    
- Establecer duración constante desde el inicio = mejor rendimiento.
    
- Todo lo implementado debe estar previamente en el product backlog.

---

# 📊 Gráficos De Seguimiento

- **Burndown**: trabajo restante vs tiempo.
    
- **Burnup**: trabajo completado vs total planeado.

> 🖼️ Ejemplo de gráfico burnup:  
> ![[Pasted image 20250726221549.png]]

- Scrum prefiere estos gráficos frente a los **diagrams Gantt** (modelo tradicional).

---

# ⚙️ Desarrollo Del Sprint

- El equipo decide cómo descomponer historias en tareas.
    
- Tareas: no deben superar las 16h → dividir si es necesario.
    
- Todas las actividades del ciclo (codificación, pruebas, despliegue) se hacen en paralelo.
    
- Sprint **cierra con la entrega del incremento**, salvo excepciones.

---

# 🏁 Tipos De Sprint

- **Sprint normal**: desarrolla funcionalidades nuevas.
    
- **Sprint de release**: despliegue de versión operativa.
    
- **Sprint cero**: tareas previas al inicio del desarrollo.

---

# 🤝 Equipos Grandes Y Escalado Scrum

- **Scrum of Scrums**: reunión interequipos tras el daily scrum.
    
    - Participan 1–2 representantes técnicos de cada equipo.
        
- Sincronización de sprints: todos los equipos inician y terminan al mismo tiempo.
    
- Comunicación activa entre equipos, minimiza dependencias.

---

# 🧭 Gestión Del Product Backlog En Equipos Múltiples

1. ✅ Un solo **PO** y **product backlog centralizado** (preferido).
    
2. 🟡 Un PO con varios backlogs (más complejo).
    
3. 🔴 Varios POs con varios backlogs (riesgo de descoordinación).

---

# 🧩 Gestión Modular

- Ideal: equipos trabajan en **components independientes** con bases de código distintas.
    
- Si una historia afecta a varios components → require coordinación entre equipos.

---

# 📌 Resumen Visual

> 🖼️ Modelo de desarrollo basado en sprints:  
> ![[Pasted image 20250726221651.png]]

---
