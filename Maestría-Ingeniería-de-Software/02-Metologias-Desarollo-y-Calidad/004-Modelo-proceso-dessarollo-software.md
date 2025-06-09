
# Modelo De Proceso De Desarrollo De Software

## Introducción

Un **modelo de proceso de desarrollo de software** es una representación simplificada de un proceso real, diseñada para que los desarrolladores la entiendan y sigan fácilmente.  
La elección adecuada del modelo es crucial: **un modelo mal elegido puede afectar la calidad del sistema**.

---

## Modelos De Procesos Descriptivos Tradicionales

- Buscan formalizar el desarrollo de software.
    
- Ejemplos:
    
    - **Rational Unified Process (RUP)**
        
    - **Microsoft Solutions Framework (MSF)**
        
    - **Métrica v.3**
        

---

## Modelos De Procesos [[Ágiles]]

- Buscan **adaptabilidad** y **flexibilidad**.
    
- Permiten libertad de implementación específica.
    
- No siempre se consideran **metodologías completas** (según algunos autores) porque dejan aspectos abiertos.
    
- Se enfocan en adaptarse al cambio rápidamente y con bajo costo.
    

---

## Modelos De Proceso Tradicionales
- Los modelos y técnicas se enfocan en definir actividades y tareas precisas para desarrollar software de calidad.
- Se establecen fechas y presupuestos concretos para lograr el objetivo.
- Se busca minimizar la incertidumbre asociada al proyecto en todo memento.
### Modelo En Cascada
![[02-Metologias-Desarollo-y-Calidad#^frame=Ifm5pa2ssU_e2IDtBEWcp]]
- Primer paradigma del desarrollo de software.
    
- Derivado de procesos de ingeniería tradicionales.
    
- Fases secuenciales:
    
    - Especificación de requisitos
        
    - Diseño de software
        
    - Implementación
        
    - Pruebas
        
- Cada fase debe **completarse** antes de pasar a la siguiente.
    

#### Ventajas

- Claridad en el advance de etapas.
    
- Este modelo es lineal
#### Inconvenientes

- **Rigidez**.
    
- **Difícil adaptación** a cambios.
    
- **No recomendado** si los requisitos no están claramente definidos desde el inicio.
    
- El cliente solo recibe el producto finalizado.
    

---

### Modelo Incremental

- Construcción progresiva de un producto funcional.
    
- **Cada incremento** agrega funcionalidades.
    

#### Ventajas

- Retroalimentación temprana.
    
- Reducción de costos de adaptación.
    
- Mejor **time to market** y retorno de inversión.
    
- Distribución del esfuerzo de análisis y documentación.
    

#### Inconvenientes

- Pérdida de visibilidad y control del proceso completo.
    
- Riesgo de **degradación estructural** si no se gestiona adecuadamente (por ejemplo, falta de refactorización).
    
- Algunas organizaciones requieren procesos más burocráticos.
    

---

### Modelo Evolutivo

- Evoluciona a partir de prototipos iniciales.
    
- Require mejorar progresivamente el software y profundizar en la comprensión de requisitos.
    

---

### Modelo En Espiral

- Propuesto por **Barry Boehm**.
    
- Combina **modelo iterativo** e **incremental**.
    
- Considera explícitamente la **gestión de riesgos**.
    

#### Cada Bucle Incluye

1. Establecimiento de objetivos.
    
2. Evaluación y reducción de riesgos.
    
3. Desarrollo y validación.
    
4. Planificación y revisión.
    

---

## Modelos Especializados
- Se aplica la reutilización, necesaria en el desarrollo de software.
- Se puede aplicar técnicas de reutilización gracias a la disponibilidad de código.
- Ayuda a reducir tiempo de desarrollo y costos.
- Aumenta la fiabilidad y seguridad al emplear components ya probados.
- En la mayoría de los proyectos software se da algún nivel de reutilización, aunque sea de manera Informal.
### Modelo Basado En Components (CBSE)

- **Component-Based Software Engineering**.
    
- Basado en la reutilización sistemática de components ya existentes.
    

#### Características De Un Componente

- Encapsula funcionalidades específicas.
    
- Se distribuye e integra de forma independiente.
    
- Sigue un estándar de composición.
    
Un componente software es un fragmento de código que encapsula un conjunto de funcionalidades Específicas y relacionadas entre sí, que se exponen a través de interfaces estandarizadas, de manera que se facilita su reutilización.
#### Ventajas

- Reducción de tiempo y costos de desarrollo.
    
- Aumento de fiabilidad y seguridad.
    

---

### Modelos De Métodos Formales

- Variación del modelo en cascada.
    
- Utilizan **lenguajes formales** (matemáticos) para especificar el sistema.
    
- Enfocados en:
    
    - Alta seguridad.
        
    - Alta fiabilidad.
        
    - Sistemas críticos.
        

#### Inconvenientes

- Consumen mucho tiempo y recursos.
    
- Requieren habilidades especializadas.
    
- Dificultan la comunicación con el cliente.
    

---

# Notas Adicionales

- **Barry Boehm** introdujo el Modelo en Espiral en 1986 para solucionar los problemas del modelo en cascada frente a proyectos de alto riesgo ([fuente](https://en.wikipedia.org/wiki/Spiral_model)).
    
- **CBSE** ganó popularidad con la expansión de tecnologías como **.NET** y **JavaBeans**.
    
- Los **modelos [[ágiles]]** (como Scrum o XP) se basan en el **Manifiesto Ágil** de 2001 ([fuente](https://agilemanifesto.org/)).
    

---

## Microtest

- ¿Qué es un modelo de proceso software?
	- Un modelo de proceso de desarrollo de software es una descripción simplificada de un proceso de desarrollo de software real.
- El modelo en espiral:
	- Es iterativo e incremental.
- Estos son algunos de los inconvenientes del modelo incremental. Selecciona dos:
	- Se pierde visibilidad y control sobre el proceso global.
	- Al tratar con organizaciones de gran tamaño, existe muchos procedimientos estrictos y burocráticos.