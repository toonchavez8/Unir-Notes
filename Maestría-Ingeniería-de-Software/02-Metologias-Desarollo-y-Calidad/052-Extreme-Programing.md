# Extreme Programming (XP) – Apuntes

## 1. Introducción

- **Iniciado**: 1996.
    
- **Ámbito**: Diversos proyectos e industrias.
    
- **Énfasis**:
    
    - Satisfacción del cliente.
        
    - Trabajo en equipo.
        
- **Característica clave**: Iteraciones cortas con pequeños incrementos del sistema.
    
- **Ventaja frente al modelo en cascada**:
    
    - Más flexible al cambio.
        
    - Detección temprana de errores.
        
    - Evita un diseño monolítico inicial.
        
- **Recomendación**: Un mes de análisis previo antes de iniciar con XP.

---

## 2. Flujo General De XP

![Esquema del modelo de proceso general de XP](https://chatgpt.com/c/Pasted%20image%2020250811120440.png)

- El cliente **redacta historias de usuario** que guían las iteraciones.
    
- Historias priorizadas para cada _release_.
    
- Cada _release_ se divide en iteraciones con:
    
    - Historias asociadas.
        
    - Tareas asignadas al equipo.
        
- **Pruebas unitarias** como punto de partida.
    
- **Programación en parejas**.
    
- **Pruebas de aceptación** definidas por el cliente.

---

## 3. Actividades Principales

1. **Planificación**
    
2. **Diseño**
    
3. **Codificación**
    
4. **Pruebas**

---

## 4. Historias De Usuario

- Escritas por el cliente.
    
- Lenguaje no técnico.
    
- Tarjetas numeradas para identificación.
    
- Contienen funcionalidades con valor para el producto.
    
- Base para pruebas de aceptación.
    
- Ayudan a estimar complejidad y tiempo.

---

## 5. Prácticas Y Herramientas Recomendadas

![Esquema de prácticas y herramientas](https://chatgpt.com/c/Pasted%20image%2020250811120604.png)

---

## 6. Fases De Planificación

- Planificación de la siguiente entrega e iteración.
    
- Cliente prioriza historias con mayor valor de negocio.
    
- Negociación entre cliente y equipo.
    
- Programadores descomponen historias en tareas.
    
- Tareas asignadas a parejas de programadores.
    
- Planificación **temporal y efímera** en tres niveles.
    
- Escalas temporales distintas según nivel.

---

## 7. Fase De Diseño

- **Orientación a objetos**.
    
- Uso de **tarjetas CRC** (Clase – Responsabilidad – Colaborador).
    
- Ejemplo: _Historia de usuario “creación de nueva cita”_.
    
- Diseño continuo, incluso durante la codificación.
    
- Principios:
    
    - Diseño simple.
        
    - Refactorización constante.

---

## 8. Fase De Codificación

- Comienza con **pruebas unitarias**.
    
- Ayudan a comprender la tarea y aclarar dudas.
    
- Programación en parejas.
    
- Integración del código en repositorio central.
    
- Ejecución de pruebas automáticas tras integración.

---

## 9. Fase De Pruebas

- **Pruebas unitarias** → validan el desarrollo.
    
- **Pruebas de aceptación** → validan implementación de la historia de usuario.

---

## 10. Valores Básicos De XP (Kent Beck)

1. Comunicación.
    
2. Simplicidad.
    
3. Retroalimentación.
    
4. Valentía.
    
5. Respeto.

---

## 11. Las Doce Prácticas Básicas De XP

1. **El juego de la planificación** – Determinar rápidamente el alcance de cada iteración combinando prioridades de negocio con factibilidad técnica.
    
**Tabla: Consideraciones en la planificación**

|Decisiones de negocio|Decisiones técnicas|
|---|---|
|**Alcance**: maximizar el valor aportado en la iteración.|**Estimaciones**: duración de la implementación de las características.|
|**Prioridad**: establecer preferencias entre características.|**Consecuencias**: impacto de las decisiones técnicas.|
|**Fechas de entrega**: memento de liberar nuevas versiones.|**Proceso y organización interna** del equipo.|
||**Planificación detallada** del orden de implementación de historias y tareas.|

1. Pequeñas entregas.
    
2. La metáfora del sistema.
    
3. Diseño simple.
    
4. Desarrollo dirigido por pruebas (TDD).
    
5. Refactorización.
    
6. Programación en parejas.
    
7. Propiedad compartida del código.
    
8. Integración continua.
    
9. Semana de 40 horas.
    
10. Uso de estándares de programación.

---

## 12. Roles En XP

- **Programador**: núcleo del proceso, habilidades comunicativas, simplicidad, coraje.
    
- **Cliente**: miembro del equipo, toma decisiones estratégicas, define pruebas de aceptación.
    
- **Entrenador**: introduce prácticas, detecta el estado del equipo, sugiere mejoras.
    
- **Jefe de proyecto**: asegura objetivos, toma decisiones importantes.
    
- **Consultor**: especialista externo que resuelve problemas puntuales.
    
- **Encargado de pruebas**: ayuda al cliente con pruebas de aceptación y define unitarias.
    
- **Rastreador**: guarda datos históricos, analiza estimaciones y esfuerzo.

---

## 13. XP Industrial (IXP)

- Adaptación de XP a **organizaciones grandes**.
    
- Mantiene espíritu minimalista y prácticas de ingeniería.
    
- Introduce 6 nuevas prácticas:
    
    - Evaluación de factibilidad.
        
    - Gestión orientada a pruebas.
        
    - Participación activa de gerencia y cliente.
        
    - Comunidad del proyecto.
        
    - Calificación del proyecto.
        
    - Retrospectivas y aprendizaje continuo.

---

## MicroTest

- ¿Cuándo se inició el primer proyecto que utilizó la programación extrema (XP)?
	- 1996
	- 6 de Marzo
- ¿Cuáles son las razones principales del éxito de la programación extrema (XP)?
	- Satisfacción del cliente.
	- Trabajo en equipo.
- ¿Qué roles principales están integrados en el equipo de trabajo de XP?
	- Los mánager.
	- Clientes y desarrolladores.
- ¿Cuál es el mecanismo fundamental de planificación en XP que involucra dialogar con el equipo de desarrollo?
	- Es vital la involucración del cliente.
	- El juego de la planificación.
- ¿Qué establece XP respecto a la participación del cliente?
	- Define el alcance de cada release.
	- Redacta el conjunto de historias de usuario.