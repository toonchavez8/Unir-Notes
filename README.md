
**# 📚 UNIR - Maestría en Ingeniería de Software

Este espacio está diseñado para organizar todas las notas, materiales y actividades relacionadas con la **Maestría en Ingeniería de Software** en **UNIR**.

---

# 🧭 Índice General

## 🏫 Maestría-Ingeniería-de-Software

- [[01-Direccion-y-Gestion-de-Software|📘 Dirección y Gestión de Proyectos de Software]]
- [[02-Metologías-Desarrollo-y-Calidad|🧪 Metodologías de Desarrollo y Calidad]]

## 🧠 01-modam-softskills

Notas del módulo de habilidades blandas aplicadas al contexto professional:

- [[01-inteligencia-emocional|🧠 Inteligencia Emocional]]
- [[02-liderazgo-competencias-directivas|👥 Liderazgo y competencias directivas]]
- [[03-Comunicacion-feedback|💬 Comunicación y Feedback]]
- [[04-Gestion-Trabajo-en-Equipo|🤝 Trabajo en equipo]]
- [[05-Gestion-del-tiempo|⏰ Gestión del tiempo]]
- [[06-toma-de-decisiones|🧩 Toma de decisiones]]
- [[07-Tecnicas-creatividad|🎨 Técnicas de creatividad]]
- [[08-Seguridad-psicológica-gestión-del-conflicto|🛡️ Seguridad psicológica]]
- [[09-Motivacion-resiliencia-cambio|🔥 Motivación y resiliencia]]
- [[10-Gestión-complejidad|🌐 Gestión de la complejidad]]

## 💻 02-programacion-python

Notas del módulo de fundamentos de programación:

- [[01-Introduccion|🧾 Introducción a Python]]
- [[02-Primeros-conceptos-en-python|🔡 Conceptos básicos]]
- [[03-Programacion-basica|🧱 Programación básica]]
- [[04-funciones|🔁 Funciones]]

---

# ✍️ Uso De Obsidian

Este repositorio está diseñado para usarse con [Obsidian](https://obsidian.md), una herramienta de notas basada en Markdown que permite:

- 🧠 Interconectar conceptos mediante enlaces tipo `[[Nombre de nota]]`.
- 🗂️ Organizar el conocimiento con carpetas y etiquetas.
- 🔎 Buscar fácilmente entre los apuntes.
- 🔁 Sincronizar en la nube (si se configura con Obsidian Sync o Git).
- 🧩 Integrar visualizaciones con [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin).

## 🛠 Plugins Recomendados

- **Excalidraw**: Para esquemas visuals.
- **Calendar**: Para gestionar sesiones de estudio.
- **Dataview**: Para mostrar metainformación como tablas dinámicas.
- **Advanced Tables**: Mejor soporte para tablas Markdown.

---

# 📁 Organización

```text
📁 Maestría-Ingeniería-de-Software
 ├─ 01-Direccion-y-Gestion-de-Software
 └─ 02-Metologías-Desarrollo-y-Calidad

📁 01-modam-softskills
📁 02-programacion-python
📁 Excalidraw (Diagramas visuales)
📁 Unir-Notes (Notas compartidas y resumenes)
**
```

## Prompt for MicroTest

```test
Te voy a pasar un micro examen, quiero que solo respondas con la pregunta respuesta y la justifacion de porque. siguiendo el siguente formanto

no incluyas divisdores de ---

1.la pregunta
	- La respuesta: 
	- Justifacion:
	  
```

```text
Quiero que actúes como un asistente académico experto en la materia del transcript que te voy a pasar. Tu tarea es tomar este transcript y generar **notas de estudio**, siguiendo estas indicaciones:

1. Organiza las notas por **secciones y subtítulos** según los temas tratados en el transcript.

2. Incluye **definiciones claras** de los conceptos mencionados, explicando su relevancia y contexto para que pueda aprender mejor.

3. Si es necesario, incluye **MermaidJs** para ilustrar relaciones entre conceptos o jerarquías.

4. Si hay datos que se pueden organizar mejor en **tablas**, hazlo para facilitar la comprensión.

5. Mantén las notas **claras, concisas y fáciles de revisar**, como si fueran apuntes de clase.

6. Si hay ejemplos en el transcript, inclúyelos y **explica paso a paso** cómo funcionan.

7. Agrega información adicional relevante de manera breve que ayude a profundizar en los conceptos.

8. Al final, incluye un pequeño **resumen de los puntos clave** para repasar rápidamente.

9: no respondas con nada que no sea las notas.

10: No agregues Emojis, no es necesario mensionar el nombre del profesor

11: Agrega addicionalmente un espacio para MicroTest que sea un H2 vacia

if the transcript is in English then create the notes in english
El transcript es el siguiente:

```

## Prompt for Notes from Educative

```text
You are an academic study-notes assistant. I will paste content (from Educative.io or similar) and you must return study notes in English. For each paragraph in the source:

1. Provide a short heading (1–6 words) that captures the paragraph's main idea.
2. Write a 1–3 sentence simplified summary focused on the most important points.
3. List up to 3 bullet-point takeaways (concise, exam-style).
4. If the paragraph contains a code example:
   - Show the original code in a fenced Java code block labelled `java`.
   - Provide an "Annotated version" showing the same code with added inline comments and small refactors if helpful.
   - Add a brief step-by-step explanation (2–6 steps) that explains why the code works and what each part does.
5. If the concept benefits from a diagram, include an optional MermaidJS snippet labeled and properly fenced (```mermaid) with a short caption.
6. If any data or comparisons are easier in a table, include a small Markdown table.
7. Keep language simple and concise, suitable for quick review and study.
8. At the end of the full notes add:
   - A "Key points" summary (3–6 bullets).
Do not include extraneous commentary. If the source is not in English, keep notes in the source language; otherwise use English. When unsure about language or code language, assume English and Java.

```