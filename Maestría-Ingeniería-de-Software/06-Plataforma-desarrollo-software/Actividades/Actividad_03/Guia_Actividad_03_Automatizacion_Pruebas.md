# Guía Paso a Paso — Actividad 3

## 1) Propósito De Esta Guía

Esta guía está diseñada para ayudarte a ejecutar la **Actividad 3** de forma organizada, con foco en **cumplir todos los criterios de la rúbrica** y generar evidencias sólidas para la memoria técnica y la presentación.

Objetivo general:

- Automatizar pruebas de aceptación (validación).
- Automatizar pruebas funcionales de interfaz web.
- Automatizar pruebas de sistema para API REST.
- Automatizar pruebas de carga.
- Documentar proceso, aprendizaje y dificultades con trazabilidad.

---

## 2) Estrategia Para Maximizar la Rúbrica

Cada prueba debe poder trazarse de esta forma:

> [!attention]
> **Requisito → Caso de prueba → Script automatizado → Ejecución → Resultado → Evidencia → Hallazgo (si aplica)**

Si esa cadena existe para cada bloque, la memoria sale fuerte y defendible.

---

## 3) Stack Recomendado

**Puedes usar otras herramientas**, pero Cada quien debe justificar el porque de cada herramienta:

- **Aceptación (validación):** Cucumber (Gherkin) + Playwright. 
- **API REST (sistema):** Postman + Newman.
- **UI funcional:** Playwright.
- **Carga:** k6.

### 3.1 Ejemplos De Justificación Breve Para El Ensayo

- Cucumber facilita traducir criterios de negocio a escenarios entendibles por perfiles no técnicos.
- Playwright da estabilidad en UI y buena evidencia visual (screenshots, video).
- Postman/Newman acelera pruebas API y genera reportes exportables.
- k6 permite definir umbrales claros del requisito no funcional (p95, errores, duración).

---

## 4) Plan De Ejecución Paso a Paso (orden recomendado)

## Paso 1 — Preparación Del Entorno Reproducible

1. Clonar repositorios:
	Accede al _back-end_ en el siguiente enlace:  
	[https://github.com/spring-petclinic/spring-petclinic-rest](https://github.com/spring-petclinic/spring-petclinic-rest)

	Accede al _front-end_ en el siguiente enlace:  
	[https://github.com/spring-petclinic/spring-petclinic-angular](https://github.com/spring-petclinic/spring-petclinic-angular)

2. Levantar backend.
3. Levantar frontend.
4. Verificar backend en Swagger y frontend en navegador.

---

## Paso 2 — Definir Alcance Funcional Y Criterios De Aceptación

Seleccionar una funcionalidad concreta. Ejemplos:

- Alta de visita para una mascota existente.
- Búsqueda y edición de propietario.
- Alta de mascota asociada a propietario.

Para una historia de usuario, redactar:

- Descripción funcional.
- Criterios de aceptación medibles.
- Datos de prueba.

**Ejemplo de criterio bien definido:**

- Dado un propietario existente, cuando registro una mascota con nombre válido y fecha válida, entonces la mascota aparece en el perfil del propietario con los datos persistidos.

---

## Paso 3 — Pruebas De Aceptación (validación)

1. Crear feature en Gherkin (`Given/When/Then`).
2. Cubrir:
   - Caso feliz.
   - Al menos un caso de validación negativa.
3. Implementar steps automatizados.
4. Ejecutar y capturar resultados (pasan/fallan).
5. Si aparece bug, registrarlo con evidencia.

**Mínimo recomendado:**

- 2–3 escenarios por funcionalidad.
- 1 negativo obligatorio.

**Evidencias:**

- Archivo de escenarios.
- Salida de ejecución.
- Capturas/video.
- Registro de bug (si hay).

---

## Paso 4 — Pruebas De Sistema API REST (flujo obligatorio)

La consigna exige este flujo para una entidad:

1. Buscar entidad (no existe).
2. Crear entidad.
3. Buscar de nuevo (existe y datos correctos).
4. Editar dato.
5. Buscar de nuevo (dato cambiado).
6. Eliminar entidad.
7. Buscar de nuevo (no existe).

Implementación sugerida:

- Colección Postman con requests ordenados.
- Variables de entorno para IDs dinámicos.
- Tests post-response con validaciones de:
  - Código HTTP.
  - Campos clave.
  - Integridad de datos.
- Ejecución por Newman para reporte exportable.

**Evidencias:**

- Colección y entorno exportados.
- Reporte de Newman.
- Capturas de ejecución.

---

## Paso 5 — Pruebas Funcionales UI (interfaz web)

1. Elegir 1 formulario real del frontend.
2. Automatizar flujo de entrada de datos + submit + verificación de resultado.
3. Añadir validaciones de frontend (campo obligatorio/formato inválido, etc.).
4. Ejecutar en modo repetible.
5. Guardar screenshots y/o video del test.

**Criterio de calidad:**

- No solo hacer click: verificar contenido final y mensajes esperados.

---

## Paso 6 — Pruebas De Carga (requisito De 1000 Usuarios Y < 5s)

### 6.1 Definir Escenario Técnico

- Endpoint de consulta (lectura) sobre entidad estable.
- Carga progresiva (ramp-up) y pico de concurrencia.
- Duración suficiente para observar comportamiento.

### 6.2 Definir Umbrales

Ejemplo:

- p(95) < 5000 ms.
- tasa de error < 1%.

### 6.3 Ejecutar E Interpretar

- Correr escenario principal.
- Registrar resultados.
- Concluir explícitamente si **cumple o no cumple** el requisito no funcional.
- Si no cumple, proponer hipótesis (cuello de botella backend, DB, red, etc.).

**Evidencias:**

- Script de carga.
- Resumen de métricas.
- Capturas/reportes de ejecución.

## 5) División De Tareas Del Equipo

## Rol 1 — Coordinación Y Calidad Documental - Fer

Responsible de:

- Planificación, seguimiento y control de hitos.
- Estandarizar formato de evidencias.
- Integrar memoria final y presentación.
- Verificar cobertura completa de rúbrica.

## Rol 2 — Aceptación (validación) - Octavio

Responsible de:

- Justifican de uso de herramientas 
- Historia/s de usuario.
- Criterios de aceptación.
- Escenarios Gherkin y automatización.
- Evidencias y hallazgos de aceptación.

## Rol 3 — API REST (sistema) - Maikal

Responsible de:

- Justifican de uso de herramientas 
- Script para automatizar la ejecución de las pruebas
- Diseño de colección Postman.
- Flujo completo obligatorio de entidad.
- Variables y aserciones.
- Ejecución Newman y reporte.

## Rol 4 — UI Funcional - Danny

Responsible de:

- Justifican de uso de herramientas 
- Scripts Playwright/Cypress/selenium/Vitest para formularios.
- Casos positivos y negativos.
- Evidencias visuals de ejecución.

## Rol 5 — Carga Y Análisis De Rendimiento - Miguel

Responsible de:

- Justifican de uso de herramientas 
- Diseño de escenario k6.
- Umbrales y métricas.
- Ejecución e interpretación técnica.
- Recomendaciones de mejora.

---

## 6) Matriz Para Asegurar Cumplimiento De la Rúbrica

## Criterio 1 — Aceptación (2 pts)

Checklist:

- [ ] Caso de uso claro y acotado.
- [ ] Criterios de aceptación explícitos.
- [ ] Escenarios automatizados completos.
- [ ] Evidencias de proceso y resultados.
- [ ] Hallazgo o bug identificado (ideal).

## Criterio 2 — Funcionales UI (2 pts)

Checklist:

- [ ] Flujo web automatizado extremo a extremo.
- [ ] Validaciones positivas y negativas.
- [ ] Evidencias de ejecución (capturas/video/reportes).
- [ ] Resultados interpretados.

## Criterio 3 — Sistema API REST (2 pts)

Checklist:

- [ ] Flujo obligatorio completo (buscar/crear/buscar/editar/buscar/eliminar/buscar).
- [ ] Aserciones de estado y contenido.
- [ ] Evidencias robustas del proceso y resultado.

## Criterio 4 — Carga (1 pt)

Checklist:

- [ ] Escenario de carga reproducible.
- [ ] Umbrales definidos.
- [ ] Resultado contra requisito (cumple/no cumple).
- [ ] Evidencias de ejecución.

## Criterio 5 — Memoria Técnica Proceso Y Plataformas (2 pts)

Checklist:

- [ ] Justificación de herramientas.
- [ ] Proceso detallado por bloque.
- [ ] Trazabilidad y evidencias de ambos ejercicios/frentes.

## Criterio 6 — Aprendizaje (1 pt)

Checklist:

- [ ] Reflexión individual/grupal.
- [ ] Qué fue positivo, qué costó y cómo se resolvió.
- [ ] Qué mejorarían en un siguiente ciclo.

---

## 7) Plantilla Para la Memoria Técnica (esqueleto final)

## Portada

- Universidad, asignatura, actividad.
- Integrantes y roles.
- Fecha.

## Índice

## 1. Introducción

1.1 Contexto de la actividad  
1.2 Objetivos del trabajo grupal  
1.3 Alcance funcional y técnico

## 2. Justificación De Plataformas De Automatización

2.1 Plataforma para aceptación (validación)  
2.2 Plataforma para API REST (sistema)  
2.3 Plataforma para UI funcional  
2.4 Plataforma para carga  
2.5 Criterios de elección y comparación breve

## 3. Preparación Del Entorno

3.1 Requisitos técnicos  
3.2 Instalación de backend y frontend  
3.3 Verificación de arranque  
3.4 Gestión de datos de prueba

## 4. Pruebas De Aceptación (validación)

4.1 Caso de uso seleccionado  
4.2 Criterios de aceptación  
4.3 Escenarios automatizados (Gherkin)  
4.4 Ejecución y resultados  
4.5 Evidencias

## 5. Pruebas De Sistema (API REST)

5.1 Entidad seleccionada y justificación  
5.2 Flujo completo automatizado exigido por la actividad  
5.3 Aserciones implementadas  
5.4 Ejecución y resultados  
5.5 Evidencias

## 6. Pruebas Funcionales UI

6.1 Flujo de formulario seleccionado  
6.2 Casos positivos y negativos  
6.3 Ejecución y resultados  
6.4 Evidencias

## 7. Pruebas De Carga

7.1 Requisito no funcional objetivo  
7.2 Diseño del escenario y umbrales  
7.3 Ejecución y métricas  
7.4 Análisis de cumplimiento (cumple/no cumple)  
7.5 Evidencias

## 8. Hallazgos E Incidencias Detectadas

8.1 Bugs encontrados  
8.2 Impacto y prioridad  
8.3 Recomendaciones de mejora

## 9. Aprendizaje Y Reflexión Del Equipo

9.1 Aspectos positivos del proceso  
9.2 Aspectos más difíciles  
9.3 Lecciones aprendidas  
9.4 Mejoras para futuras iteraciones

## 10. Conclusiones

## 11. Anexos

- Capturas.
- Reportes.
- Exportables de herramientas.
- Trazabilidad criterio ↔ evidencia.

---

## 8) Plantilla De Tabla De Trazabilidad (lista Para copiar)

| Criterio rúbrica | Objetivo | Prueba automatizada | Evidencia | Resultado | Hallazgo |
|---|---|---|---|---|---|
| C1 Aceptación | Validar caso de uso | Escenario Gherkin X | Captura + reporte | OK/FAIL | Bug/No bug |
| C2 UI funcional | Verificar formulario | Test UI Y | Video + screenshot | OK/FAIL | … |
| C3 API REST | Verificar ciclo completo | Colección entidad Z | Newman report | OK/FAIL | … |
| C4 Carga | 1000 usuarios < 5s | Script k6 | Resumen métricas | Cumple/No cumple | … |

---

## 9) Guion Breve Para Presentación (máx. 10 diapositivas)

1. Titulo
2. Objetivo y alcance.
3. Plataformas elegidas y por qué.
4. Flujo de aceptación automatizado.
5. Flujo API REST completo.
6. Flujo UI funcional.
7. Escenario de carga y umbrales.
8. Resultados clave.
9. Bugs/hallazgos detectados.
10. Aprendizajes y dificultades.
11. Conclusiones y mejoras futuras.

---

## 10) Checklist Final De Entrega

- [ ] Memoria técnica completa (máx. 25 páginas, formato solicitado).
- [ ] Evidencias de proceso y resultados para los 4 bloques.
- [ ] Reflexión de aprendizaje completa.
- [ ] Revisión ortográfica final.
- [ ] Presentación lista (≤10 diapositivas).
- [ ] Archivo comprimido final con todo el material.

---

## 12) Consejo Final Para Nota Alta

- justificar decisiones,
- demostrar trazabilidad,
- analizar resultados,
- y reflexionar sobre el aprendizaje con criterio técnico.
