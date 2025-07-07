# Plan de Organización del Congreso con Scrum

## 1. Formación del Equipo Scrum

1. **Asignar roles**
    - **Product Owner (PO):** Representa los intereses de la organización (ej. General Chair).
	    - Maikal
    - **Scrum Master (SM):** Facilita el proceso Scrum y elimina impedimentos.
	    - Danny
    - **Scrum Team:** Grupo multidisciplinar (2–6 personas) encargado de ejecutar las tareas (hotel, catering, audiovisuales, registro, fotógrafo, logística, etc.). 3
	    - Miguel
	    - Fernando
	    - Octavio
2. **Kick-off inicial** (1–2 horas)
    - El PO presenta visión, objetivos y alcance del congreso.
    - Definir el “producto”: la organización completa (sede, servicios, protocolo, logística).
    - Acordar herramientas (tablero digital, canal de comunicación, repositorio de documentos).

## 2. Elaboración del Product Backlog

1. **Generación de ítems (Brainstorming)**
    - Reunión de equipo para listar todas las actividades necesarias.
    - Capturar ideas en un tablero (Jira, Trello, Miro, etc.).
2. **Conversión a Historias de Usuario**
    - Formato: _Como [rol], quiero [actividad] para [beneficio]._
    - Definir criterios de aceptación (DoD) para cada historia.
    - Ejemplos:
        1. **HU1 Acreditaciones**
            - Como _Asistente_, quiero recibir mi acreditación impresa al llegar, para acceder sin esperas.
            - **Criterios:** Impresión ≤ 2 min/usuario; kioscos operativos.
        2. **HU2 Salas AV**
            - Como _Organización_, quiero reservar y equipar 4 salas con sonido y vídeo, para ejecutar 3 sesiones simultáneas y una principal.
            - **Criterios:** ≥2 micrófonos, 1 proyector + pantalla, altavoces en cada sala.
        3. **HU3 Coffee‑breaks**
            - Como _Organización_, quiero contratar coffee‑breaks diarios para ofrecer 2 pausas de 20 min.
            - **Criterios:** Opciones veganas, sin gluten y señalización de alérgenos.
        4. **HU4 Cena Gala**
            - Como _Organización_, quiero organizar cena de gala en espacio emblemático, para una experiencia memorable.
            - **Criterios:** Menú vegetariano/vegano, capacidad confirmada para 200 personas.
        5. **HU5 Kit Ponentes**
            - Como _Ponente_, quiero recibir un kit local de bienvenida, como recuerdo de la ciudad.
            - **Criterios:** Entrega al inicio de la charla, obsequio empaquetado.
        6. **HU6 Burndown Chart**
            - Como _SM_, quiero un burndown chart actualizado diario, para medir avance y detectar retrasos.
            - **Criterios:** Gráfico diario tras cada daily.
3. **Estimación de esfuerzo**
    - Usar Planning Poker o T‑shirt sizing.
    - Asignar puntos de historia.
4. **Priorización**
    - Método MoSCoW (Must, Should, Could, Won’t) o valor vs complejidad.
    - PO valida y ajusta según ROI.
5. **Product Backlog**

| ID  | Historia           | Puntos | Prioridad |
| --- | ------------------ | ------ | --------- |
| HU1 | Acreditaciones     | 3      | Must      |
| HU2 | Salas AV           | 8      | Must      |
| HU3 | Coffee‑breaks      | 5      | Should    |
| HU4 | Cena de gala       | 8      | Could     |
| HU5 | Kit ponentes       | 2      | Should    |
| HU6 | Burndown chart     | 3      | Must      |
| HU7 | Fotógrafo suplente | 5      | Could     |
| HU8 | Menú sin alérgenos | 3      | Must      |

## 3. Release Plan y Sprint Planning

1. **Estructura de sprints**
    - 3 sprints de 2 semanas cada uno.
2. **Release Plan**
    - **Sprint 1 (Infraestructura básica):** Reserva de sede, contrato AV, registro online.
    - **Sprint 2 (Servicios y Protocolo):** Catering, coffee‑breaks, acreditaciones, protocolo.
    - **Sprint 3 (Comunicación y Cierre):** Fotografía, kits ponentes, boletines, feedback.
3. **Sprint Planning**
    - Selección de historias según prioridad y capacidad.
    - Descomposición en tareas (4–8 h c/u) con estimaciones en horas.
    - Definir Sprint Goal.

### Sprint Backlogs

#### Sprint 1 – Infraestructura

**Goal:** Tener sede y registro operativo.

| Tarea                                    | HU  | Est. (h) |
| ---------------------------------------- | --- | -------- |
| Firmar contrato con la sede              | HU2 | 8        |
| Contratar AV para salas y sala principal | HU2 | 16       |
| Configurar registro online               | HU1 | 12       |
| Diseñar/imprimir acreditaciones          | HU1 | 6        |
| Actualizar burndown chart diario         | HU6 | diario   |

#### Sprint 2 – Servicios y Protocolo

**Goal:** Provisión de catering y plan de bienvenida.

| Tarea                                | HU  | Est. (h) |
| ------------------------------------ | --- | -------- |
| Seleccionar proveedores coffee‑break | HU3 | 10       |
| Validar menú y restricciones         | HU3 | 8        |
| Reservar cena de gala                | HU4 | 12       |
| Crear guión de bienvenida y clausura | HU5 | 6        |
| Refinamiento inter-sprint            | —   | 2        |

#### Sprint 3 – Comunicación y Cierre

**Goal:** Cobertura fotográfica y cierre de entregables.

|Tarea|HU|Est. (h)|
|---|---|---|
|Contratar fotógrafo suplente|HU7|6|
|Empaquetar kits ponentes|HU5|4|
|Generar burndown chart y reporte final|HU6|4|
|Ajustes y revisión de feedback en platforma|—|8|

## 4. Ejecución del Sprint

- **Daily Scrum (15 min):** ¿Ayer? ¿Hoy? Impedimentos.
- **Burndown Chart:** Actualización diaria.
- **Gestión de impedimentos:** SM los aborda y documenta.

## 5. Revisión y Retrospectiva

1. **Sprint Review:** Demo de entregables y recogida de feedback.
2. **Retrospective:** Analizar qué salió bien, mal y proponer mejoras.

## 6. Manejo de Riesgos e Imprevistos

- **Insuficiencia de salas:** Crear HU adicional y plan B.
- **Fotógrafo enfermo:** HU7 para fotógrafo suplente.
- **Sprint incompleto:** Mover historias y ajustar alcance.
- **Restricciones alimentarias:** HU8 para menús especiales.
- **Refinamiento continuo:** 1–2 sesiones por sprint para ajustar PB.

## 7. Cierre del Proyecto

1. **Revisión Final:** Validación de todos los entregables.
2. **Retrospectiva de Proyecto:** Lecciones aprendidas y documento de buenas prácticas.
3. **Handoff:** Transferir al equipo operativo con cronograma y contactos.

## 8. Evidencias de Reuniones y Mejoras

| Reunión          | Evidencia                       | Mejora añadida                                      |
| ---------------- | ------------------------------- | --------------------------------------------------- |
| Kick-off         | Acta con asistentes y objetivos | Vídeo introducción para ausentes                    |
| Sprint Planning  | Captura tablero sprint inicial  | Incluir “Definition of Ready” para tareas complejas |
| Daily (cada día) | Registro de impedimentos        | Checklist móvil para seguimiento rápido             |
| Sprint Review    | Vídeo demo + acta de feedback   | Encuesta anónima en vivo                            |
| Retrospective    | Mapa de calor “bien/mal”        | Votación online anónima de acciones de mejora       |

## 9. Reflexión del Aprendizaje

- **Bien:**
    - Validación rápida de sede y AV.
    - Daily meetings anticiparon falta de salas y activaron plan B.
- **Mal:**
    - Subestimación de menú de gala y confirmación de alergias.
    - Retraso en contratación de fotógrafo, generando brecha de cobertura.
- **Haré diferente:**
    1. Incluir HU específica de “Gestión de alergias y dietas” desde Sprint 1.
    2. Mantener pool alternativo de proveedores validados.
    3. Añadir “spike” de riesgos en cada Sprint Planning.

### Resumen de Artefactos y Ceremonias

|Artefacto/Ceremonia|Frecuencia|Responsable|
|---|---|---|
|Product Backlog|Continuo|PO|
|Sprint Planning|Inicio de cada sprint|PO, SM, Team|
|Daily Scrum|Diario|Team|
|Burndown Chart|Diario|SM/Team|
|Sprint Review|Fin de sprint|Team, PO|
|Sprint Retrospective|Fin de sprint|SM, Team|
|Sprint Refinement|1–2 por sprint|PO, Team|
|Release Plan|Antes de Sprint 1|PO, SM, Team|
