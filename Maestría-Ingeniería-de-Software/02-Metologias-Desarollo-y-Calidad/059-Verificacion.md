# Verificación Y Validación Del Software

## Introducción

La **verificación** y **validación** del software comprenden procesos de comprobación y análisis que garantizan:

- Cumplimiento de **especificaciones**.
- Satisfacción de las **necesidades para las que fue construido**.

## Diferencia Clave

- **Verificación:**  
  Comprueba que el software fue construido **correctamente** según especificaciones y requisitos.
- **Validación:**  
  Comprueba que el software construido es el **adecuado** para el uso previsto.

---

## Enfoques Y Momentos De Aplicación

### Verificación

- Ocurre en **todas las fases** del desarrollo:
  - Identificación de necesidades.
  - Especificación de requisitos.
  - Diseño.
  - Implementación.
  - Integración.
  - Despliegue.
- **Enfoque:** Analiza el proceso y productos intermedios.
- **Ejemplo de actividades:**
  - Revisiones.
  - Walkthroughs.
  - Inspecciones.

### Validación

- Se realiza **al final del desarrollo** o en etapas de construcción.
- **Enfoque:** Garantiza que el sistema es compatible con expectativas del cliente.
- **Ejemplo de actividades:**
  - Pruebas de caja negra.
  - Pruebas de caja gris.
  - Pruebas de caja blanca.

---

## Comparativa Rápida

| Aspecto              | Verificación                                                                 | Validación                                              |
|----------------------|-------------------------------------------------------------------------------|---------------------------------------------------------|
| **Objetivo**         | Construir el producto **correctamente**                                       | Construir el **producto correcto**                      |
| **Memento**          | Durante cada fase del desarrollo                                              | Al final o durante la construcción                      |
| **Proceso**          | Estático (no se ejecuta el código)                                            | Dinámico (se ejecuta el producto)                       |
| **Elementos**        | Planificación, requisitos, diseño, código, casos de prueba                    | Producto o sistema final                                |
| **Tipo de pruebas**  | Unitarias, integración                                                        | Aceptación, sistema                                     |
| **Preguntas clave**  | "¿Estamos construyendo correctamente el sistema?"                             | "¿Estamos construyendo el sistema correcto?"            |

---

## Relación En El Ciclo De Desarrollo

```mermaid
flowchart TD
    A[Inicio del Proyecto] --> B[Identificación de Necesidades]
    B --> C[Especificación de Requisitos]
    C --> D[Diseño del Sistema]
    D --> E[Implementación]
    E --> F[Integración]
    F --> G[Despliegue]
    
    subgraph Verificación
    B
    C
    D
    E
    F
    G
    end

    subgraph Validación
    G
    end
````

---

## Preguntas Detonantes

- **Verificación:**
    
    - ¿Estamos construyendo correctamente el sistema?
        
- **Validación:**
    
    - ¿Estamos construyendo el sistema correcto?

---

## Opiniones De Autores

- Algunos consideran que **todas las pruebas** son parte de la verificación.
    
- Otros diferencian:
    
    - **Verificación:** pruebas unitarias e integración.
        
    - **Validación:** pruebas de aceptación y de sistema.

---

## Resumen Visual De Actividades

```mermaid
mindmap
  root("Verificacion y valdacion")
    Verificación
      Objetivo:::good
      Actividades
        Revisiones
        Walkthroughs
        Inspecciones
      Proceso
        Estático
    Validación
      Objetivo:::good
      Actividades
        Pruebas Caja Negra
        Pruebas Caja Gris
        Pruebas Caja Blanca
      Proceso
        Dinámico

```

---

## MicroTest

**Pregunta 1:**  
**¿Cuál de las siguientes afirmaciones describe correctamente la validación del software?**  
**Respuesta:** d. _Confirma que el producto construido es apropiado para el uso previsto._  
**Por qué:** La validación se enfoca en comprobar que el producto final satisface las necesidades y expectativas del usuario y es útil para el propósito para el que fue diseñado.

---

**Pregunta 2:**  
**¿Cuál de las siguientes afirmaciones sobre la verificación del software es incorrecta?**  
**Respuesta:** d. _Siempre garantiza que el producto sea útil._  
**Por qué:** La verificación evalúa si el producto está construido correctamente según requisitos y especificaciones, pero no garantiza que sea útil o adecuado para el usuario final; eso es tarea de la validación.

---

**Pregunta 3:**  
**¿Cuál de las siguientes opciones no se considera una actividad de validación del software?**  
**Respuesta:** c. _Las pruebas unitarias y de integración._  
**Por qué:** Estas pruebas están más relacionadas con la verificación, ya que se centran en comprobar que los components individuales y su integración funcionan según lo especificado, no en confirmar que el producto completo sea el correcto para el usuario.

---

