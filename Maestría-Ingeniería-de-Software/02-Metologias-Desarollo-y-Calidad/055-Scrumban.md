# 📌 Combinación De Scrum Y Kanban (Scrumban)

## 1. Contexto

* La adopción de prácticas ágiles suele comenzar con **Scrum**, a menudo combinado con **Kanban**.
* **Razón**: ambos enfoques se complementan, aunque presenten diferencias claras.
* La integración de ambos se conoce como **Scrumban**.

---

## 2. Comparativa Scrum Vs Kanban

| **Característica**                                                  | **Scrum**                                         | **Kanban**                                   |
| ------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------- |
| Iteraciones de duración predeterminada                              | Obligatorio                                       | Opcional                                     |
| Compromiso del equipo de desarrollo con el trabajo de una iteración | Obligatorio                                       | Opcional                                     |
| Estimación                                                          | Obligatorio                                       | Opcional                                     |
| Métrica utilizada para la mejora del proceso y la planificación     | Velocidad                                         | Lead time                                    |
| Roles                                                               | Product Owner, Scrum Master, Equipo de desarrollo | Opcional, se permiten equipos especializados |
| Equipos multifuncionales                                            | Obligatorio                                       | Sin restricciones                            |
| Tamaño de las tareas                                                | Deben poder terminarse en un sprint               | Sin restricciones                            |
| Gráficos obligatorios                                               | Burndown                                          | Ninguno obligatorio                          |
| Limitaciones del WIP                                                | Implícitamente en el sprint                       | Explícitamente a partir del WIP              |
| Añadir tareas en una iteración                                      | No se permite                                     | Sí, siempre que exista capacidad             |
| Responsabilidad de las tareas en una iteración                      | Equipo específico                                 | En función del WIP                           |
| Borrado de las pizarras                                             | Finalización del sprint                           | Nunca                                        |

---

## 3. Integración: Scrumban

* **Idea principal**: aprovechar la visualización del flujo de trabajo de Kanban dentro de Scrum.
* **Cambio clave**:

  * Se adopta un modelo de **flujo continuo**.
  * Se elimina la **pila del sprint**.
  * Todas las tareas pendientes se colocan en la **columna inicial del tablero**.
* **Referencia**: Vila, J. L. (2016). [Scrumban](https://proagilist.es/blog/la-agilidad-y-gestion-agil/scrumban/).

---

## 4. Uso De Indicadores Visuals (caritas)

* Se pueden incluir en la **retrospectiva del sprint** para:

  * Mostrar de manera gráfica la satisfacción del equipo.
  * Valorar:

    * **Técnica** aplicada.
    * **Ecosistema** de trabajo.
    * **Filosofía** empleada en la iteración.

---

## 5. Ejemplo De Flujo Scrumban (Mermaid)

```mermaid
flowchart LR
    A[Tareas pendientes] --> B[En progreso]
    B --> C[En pruebas]
    C --> D[Finalizado]
```

---

## MicroTest

- ¿Qué técnica se adopta en scrumban para gestionar el proceso?
	- Modelo de proceso con flujo continuo.
	- No es necesaria la pila del sprint
- ¿Para qué se utilize la técnica del tablero y las caritas en scrum?
	- En la reunón spnnt retrospective
	- Mostrar el grado de satisfacción.
- ¿Cuáles son las prácticas ágiles comunes que se adoptan en una organización?
	- .Utilizar scrum.
	- Acompañado de kanban.
- ¿Cómo se complementan scrum y kanban al set utilizados juntos?
	- Ambos presentan aspectos diferenciados.
	- Se complementan muy bien.