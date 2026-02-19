# Guía Profunda Paso a Paso Para Desarrollar la Actividad 3

## 1. Propósito De Esta Guía

Esta guía te explica cómo construir un plan de auditoría técnica de seguridad completo para la empresa ficticia Librería On Line S.A., con enfoque directo en cumplir todos los criterios de la rúbrica con nivel máximo.

Incluye:

- Qué hacer en cada fase
- Cómo hacerlo
- Ejemplos de redacción académica
- Justificación de por qué cada paso suma puntos

Esta guía está alineada con los apartados solicitados en la actividad:

- Introducción
- Objetivos de la auditoría
- Alcance de la auditoría técnica de seguridad
- Metodologías
- Organización y recursos necesarios
- Evaluación de riesgos del proyecto
- Entregables del proyecto

## 2. Estrategia General Para Maximizar la Rúbrica

Antes de redactar, aplica estas tres reglas:

1. Cobertura total

- Ningún apartado puede quedar incompleto
- Cada criterio debe tener contenido técnico suficiente

1. Coherencia con el diagrama lógico y la infraestructura descrita

- Cita explícitamente los elementos a auditar: VPN, DMZ, FW, IDS, DNS, FTP, AAA, VLAN, Wi Fi, web expuesta, RGPD
- Si no conectas el texto con esos activos, pierdes puntuación en alcance y metodologías

1. Evidencia de enfoque professional

- Redacción formal
- Uso de marcos de referencia reconocidos
- Decisiones justificadas por riesgo, impacto y viabilidad

## 3. Plan De Trabajo Recomendado

## Fase 1. Preparación Del Documento

### Paso 1. Crear Estructura Base Con Los Siete Apartados Solicitados

Qué hacer

- Crea un documento con los encabezados exactos solicitados
- Reserva un espacio para referencias en formato APA

Ejemplo breve

- 1. Introducción
- 1. Objetivos de la auditoría
- 1. Alcance de la auditoría técnica de seguridad
- 1. Metodologías
- 1. Organización y recursos necesarios
- 1. Evaluación de riesgos del proyecto
- 1. Entregables del proyecto
- Referencias

Justificación

- Este paso evita omisiones y asegura cobertura de los criterios evaluados
- Sube puntos en calidad de memoria al mostrar orden y estructura académica

### Paso 2. Definir Contexto De Negocio Y Del Incidente

Qué hacer

- Resume el incidente de credenciales comprometidas
- Explica impacto reputacional y de mercado
- Introduce el objetivo de recuperación de confianza

Ejemplo de redacción

"Librería On Line S.A. sufrió un incidente de seguridad que derivó en la exposición de credenciales de clientes. Este hecho afectó la reputación de la empresa y su cuota de mercado. En respuesta, se plantea una auditoría técnica integral orientada a identificar vulnerabilidades, priorizar riesgos y definir salvaguardas viables desde el punto de vista técnico y económico."

Justificación

- Da sentido estratégico al plan
- Mejora la introducción y da coherencia a objetivos, alcance y riesgos

## Fase 2. Desarrollo Por Criterio De Rúbrica

## Criterio 1. Objetivos De la Auditoría

Meta para nota máxima

- Definir objetivos específicos, medibles y alineados con la arquitectura

### Paso 3. Redactar Objetivo General

Qué hacer

- Formula un objetivo general claro

Ejemplo

"Evaluar el estado de seguridad de la infraestructura TI de Librería On Line S.A. para identificar vulnerabilidades técnicas, estimar el riesgo asociado y establecer un plan de mitigación priorizado."

Justificación

- Marca la dirección de todo el documento

### Paso 4. Redactar Objetivos Específicos Por Dominio

Qué hacer

- Incluye al menos 6 objetivos específicos conectados con activos reales

Ejemplo

- Evaluar controles perimetrales en la DMZ de dos capas
- Revisar robustez del proceso de autenticación y sistema AAA
- Analizar exposición de servicios públicos DNS y FTP
- Verificar segmentación de red por VLAN y controles de acceso lateral
- Evaluar protección de datos personales en cumplimiento de RGPD
- Revisar trazabilidad y monitoreo para detección temprana de incidentes

Justificación

- Muestra ejecución total del criterio
- Si los objetivos reflejan la arquitectura del caso, evitas penalización por falta de reflejo del diagrama lógico

## Criterio 2. Alcance De la Auditoría Técnica De Seguridad

Meta para nota máxima

- Definir en detalle tareas, limitaciones y tipos de prueba
- Conectar el alcance con cada componente de infraestructura

### Paso 5. Delimitar Alcance Técnico Por Capas

Qué hacer

- Separa alcance por capas para mayor claridad

Ejemplo de alcance por capas

- Capa perimetral: VPN, firewall, IDS, publicación web
- Capa de servicios: DNS, FTP, correo interno y externo
- Capa de red interna: router, switch, VLAN, Wi Fi
- Capa de aplicaciones: web expuesta, intranet y aplicaciones corporativas
- Capa de identidad y endpoint: AAA y antimalware
- Capa de datos y cumplimiento: tratamiento de datos personales y RGPD

Justificación

- Demuestra profundidad técnica y cobertura integral
- Suma en el criterio con mayor peso de la rúbrica

### Paso 6. Definir Tareas Concretas De Auditoría

Qué hacer

- Presenta tareas accionables para cada zona

Ejemplo de tareas

- Revisión de reglas de firewall y principio de mínimo privilegio
- Validación de configuración y firmas del IDS
- Enumeración controlada de superficies expuestas en DNS y FTP
- Revisión de políticas de contraseñas, MFA y registro en AAA
- Pruebas de autenticación y gestión de sesión en aplicación web
- Verificación de segmentación efectiva entre VLAN de usuarios y servidores
- Revisión de cifrado de datos en tránsito y en reposo

Justificación

- El evaluador necesita ver que el alcance es operativo, no conceptual

### Paso 7. Incluir Limitaciones Y Supuestos

Qué hacer

- Especifica límites para una auditoría realista

Ejemplo

- No se ejecutarán pruebas destructivas que afecten disponibilidad en producción
- No se incluye auditoría de código fuente interno no facilitado
- Pruebas de ingeniería social fuera de alcance
- Horarios autorizados para pruebas activas

Justificación

- Muestra criterio professional
- Evita expectativas irreales y fortalece la calidad metodológica

### Paso 8. Definir Tipos De Prueba

Qué hacer

- Clasifica pruebas por tipo y objetivo

Ejemplo

- Pruebas de configuración segura
- Pruebas de vulnerabilidades conocidas
- Pruebas de autenticación y autorización
- Pruebas de segmentación de red
- Pruebas de cumplimiento normativo para datos personales

Justificación

- Completa el apartado solicitado de forma evaluable

## Criterio 3. Metodologías

Meta para nota máxima

- Usar metodologías reconocidas y explicar para qué aporta cada una

### Paso 9. Seleccionar Marcos Metodológicos

Qué hacer

- Elige un conjunto coherente

Recomendación

- NIST SP 800 115 para enfoque de pruebas técnicas
- OWASP Testing Guide para pruebas web
- ISO 27001 y 27002 como referencia de controles
- MITRE ATT and CK para modelado de tácticas de ataque
- CVSS para priorización técnica de vulnerabilidades

Justificación

- Referenciar marcos reconocidos incrementa rigor académico

### Paso 10. Definir Ciclo Metodológico De Ejecución

Qué hacer

- Describe proceso en etapas

Ejemplo de ciclo

1. Planificación y autorización
2. Recolección de información
3. Análisis técnico y pruebas
4. Correlación de hallazgos
5. Evaluación de riesgo
6. Recomendaciones y cierre

Justificación

- Muestra que la auditoría no es una lista aislada de escaneos
- Aporta trazabilidad y control

## Criterio 4. Organización Y Recursos Necesarios

Meta para nota máxima

- Incluir herramientas concretas y rol operativo de cada una

### Paso 11. Definir Roles Del Equipo De Auditoría

Qué hacer

- Aunque el enunciado pide herramientas, incluir roles aporta solidez

Ejemplo

- Líder de auditoría
- Especialista en seguridad de red
- Especialista en seguridad web
- Analista de cumplimiento y protección de datos

Justificación

- Refuerza viabilidad de ejecución y coordinación

### Paso 12. Definir Herramientas Por Dominio

Qué hacer

- Lista herramienta, objetivo y salida esperada

Ejemplo de herramientas

- Nmap para descubrimiento de activos y puertos
- Nessus u OpenVAS para detección de vulnerabilidades
- Burp Suite o OWASP ZAP para pruebas de seguridad web
- Wireshark para análisis de tráfico
- SIEM existente para correlación de eventos
- Lynis o CIS CAT para revisión de hardening

Justificación

- Este criterio evalúa organización y recursos
- Explicar el para qué de cada herramienta eleva la calidad

## Criterio 5. Evaluación De Riesgos Del Proyecto

Meta para nota máxima

- Construir análisis de riesgos propio del proyecto de auditoría

### Paso 13. Identificar Riesgos De Negocio Y Técnicos

Qué hacer

- Distingue riesgos derivados del incidente y de la infraestructura actual

Ejemplos

- Reutilización de credenciales comprometidas
- Movimiento lateral por segmentación ineficiente
- Exposición de servicios legacy inseguros
- Impacto legal por incumplimiento de RGPD

Justificación

- Sin identificación explícita de riesgos, el criterio queda parcial

### Paso 14. Valorar Probabilidad E Impacto

Qué hacer

- Crea matriz cualitativa con niveles Bajo Medio Alto

Ejemplo de redacción

"La exposición de credenciales presenta probabilidad alta e impacto alto, debido a la recurrencia de ataques de credential stuffing y al daño reputacional asociado."

Justificación

- La valoración formal permite priorizar acciones con lógica de riesgo

### Paso 15. Proponer Tratamiento De Riesgos

Qué hacer

- Para cada riesgo relevante, define control y prioridad

Ejemplo

- Riesgo: toma de cuentas por credenciales reutilizadas
- Tratamiento: MFA obligatorio, política de contraseñas robusta, monitorización de intentos fallidos
- Prioridad: Alta

Justificación

- Convierte la auditoría en plan de acción real

## Criterio 6. Entregables Del Proyecto

Meta para nota máxima

- Presentar entregables completos y vinculados a amenazas y riesgos

### Paso 16. Definir Entregables Obligatorios

Qué hacer

- Enumera documentos con contenido mínimo

Entregables recomendados

- Plan de auditoría aprobado
- Matriz de activos y amenazas
- Matriz de riesgos priorizados
- Informe técnico de hallazgos con evidencias
- Plan de remediación priorizado por criticidad
- Resumen ejecutivo para dirección

Justificación

- Este criterio pide valorar amenazas de forma completa
- La matriz amenaza riesgo control es clave para obtener puntuación máxima

### Paso 17. Definir Evidencia Por Entregable

Qué hacer

- Especifica qué incluirás como evidencia técnica

Ejemplos

- Capturas de configuraciones críticas
- Trazas anonimizadas de eventos
- Resultados de escaneos con fecha y alcance
- Tabla de vulnerabilidades con severidad y recomendación

Justificación

- Una auditoría sin evidencia pierde fuerza técnica y académica

## Criterio 7. Calidad De la Memoria Y Citación

Meta para nota máxima

- Estilo académico formal y referencias en APA

### Paso 18. Aplicar Estilo De Redacción Académica

Qué hacer

- Usar lenguaje técnico formal
- Evitar frases coloquiales
- Mantener coherencia terminológica

Ejemplo de mejora

- Coloquial: "La empresa está mal en seguridad"
- Académico: "Se identifican brechas de control que incrementan la superficie de exposición de la organización"

Justificación

- Este criterio se penaliza rápido si el tono no es formal

### Paso 19. Aplicar Citación APA En Fuentes Técnicas

Qué hacer

- Cita normativas y guías usadas

Ejemplos de fuentes que puedes citar

- NIST SP 800 115
- OWASP Testing Guide
- ISO IEC 27001 e ISO IEC 27002
- Agencia Española de Protección de Datos para RGPD

Justificación

- APA correcta y consistente aporta puntuación máxima en calidad de memoria

## Criterio 8. Ortografía

Meta

- Cero penalizaciones

### Paso 20. Ejecutar Control De Calidad Lingüística Final

Qué hacer

- Revisión ortográfica automática
- Relectura manual completa
- Verificación de tildes, concordancia y puntuación

Justificación

- Las penalizaciones por faltas pueden reducir significativamente la nota final

## 4. Plantilla Profunda Para Redactar Cada Apartado

## 4.1 Introducción

Qué debes incluir

- Contexto del incidente
- Situación de negocio
- Necesidad de auditoría
- Propósito del documento

Mini plantilla

"El presente documento define el plan de auditoría técnica de seguridad para Librería On Line S.A. tras el incidente de compromiso de credenciales de clientes. El objetivo del plan es establecer un proceso sistemático de evaluación de la postura de seguridad de la infraestructura TI para identificar vulnerabilidades, estimar riesgos y proponer medidas de mitigación priorizadas."

## 4.2 Objetivos De la Auditoría

Qué debes incluir

- Un objetivo general
- Objetivos específicos por capa tecnológica

Mini plantilla

"Objetivo general: …"

"Objetivos específicos: …"

## 4.3 Alcance De la Auditoría Técnica De Seguridad

Qué debes incluir

- Activos y sistemas incluidos
- Tareas por ejecutar
- Limitaciones y supuestos
- Tipos de pruebas

Mini plantilla

"El alcance incluye los activos perimetrales, de red, de aplicación y de identidad descritos en la arquitectura lógica. Se excluyen pruebas destructivas en producción y actividades de ingeniería social no autorizadas."

## 4.4 Metodologías

Qué debes incluir

- Marcos de referencia
- Fases de trabajo
- Criterios de severidad

Mini plantilla

"La auditoría seguirá un enfoque basado en NIST SP 800 115 para planificación y ejecución, OWASP Testing Guide para pruebas web y CVSS para priorización técnica de vulnerabilidades."

## 4.5 Organización Y Recursos Necesarios

Qué debes incluir

- Herramientas técnicas
- Uso previsto de cada herramienta
- Dependencias operativas mínimas

Mini plantilla

"Para análisis de superficie de exposición se empleará Nmap. Para validación de vulnerabilidades en aplicaciones web se utilizará OWASP ZAP, y para análisis de tráfico se empleará Wireshark."

## 4.6 Evaluación De Riesgos Del Proyecto

Qué debes incluir

- Riesgos identificados
- Probabilidad e impacto
- Tratamiento y prioridad

Mini plantilla

"Riesgo R1: Suplantación de cuentas por credenciales comprometidas. Probabilidad alta, impacto alto. Tratamiento propuesto: MFA obligatorio, limitación de intentos e implementación de alertas de comportamiento anómalo."

## 4.7 Entregables Del Proyecto

Qué debes incluir

- Lista cerrada de entregables
- Objetivo de cada entregable
- Evidencia asociada

Mini plantilla

"Entregable E3: Matriz de riesgos priorizada. Contenido mínimo: amenaza, vulnerabilidad asociada, impacto, probabilidad, nivel de riesgo, control propuesto y responsible de implementación."

## 5. Ejemplo De Matriz De Riesgos Para Incluir En Tu Documento

Puedes copiar este formato en tu memoria

- Riesgo R1
  - Activo afectado: plataforma web de autenticación
  - Amenaza: credential stuffing
  - Vulnerabilidad: ausencia de MFA y controles de tasa
  - Probabilidad: Alta
  - Impacto: Alto
  - Nivel de riesgo: Crítico
  - Tratamiento: MFA, limitación de intentos, monitoreo en tiempo real
  - Prioridad: Inmediata

- Riesgo R2
  - Activo afectado: servicio FTP público
  - Amenaza: acceso no autorizado o exfiltración
  - Vulnerabilidad: configuración insegura o cifrado insuficiente
  - Probabilidad: Media
  - Impacto: Alto
  - Nivel de riesgo: Alto
  - Tratamiento: endurecimiento, cifrado y restricción de acceso
  - Prioridad: Alta

- Riesgo R3
  - Activo afectado: segmentación VLAN
  - Amenaza: movimiento lateral
  - Vulnerabilidad: reglas de segmentación permisivas
  - Probabilidad: Media
  - Impacto: Alto
  - Nivel de riesgo: Alto
  - Tratamiento: revisión ACL, separación estricta por rol y monitoreo
  - Prioridad: Alta

## 6. Checklist Final De Cumplimiento Antes De Entregar

### Cobertura De Contenido

- Incluí todos los apartados solicitados
- Cada apartado tiene desarrollo técnico suficiente
- El alcance refleja la arquitectura del caso

### Calidad Técnica

- Expliqué tareas de auditoría concretas
- Definí limitaciones realistas
- Incluí tipos de pruebas coherentes
- Seleccioné metodologías reconocidas
- Presenté herramientas con propósito claro

### Riesgo Y Entregables

- Construí evaluación de riesgos con probabilidad e impacto
- Definí tratamientos priorizados
- Entregables cubren amenazas y evidencias

### Calidad Formal

- Redacción académica homogénea
- Referencias en APA
- Revisión ortográfica final

## 7. Recomendación De Orden De Redacción Para Avanzar Más Rápido

Orden sugerido

1. Alcance
2. Objetivos
3. Metodologías
4. Organización y recursos
5. Evaluación de riesgos
6. Entregables
7. Introducción al final

Justificación

- Si empiezas por el alcance, todo lo demás sale más coherente
- Redactar la introducción al final mejora precisión y consistencia

## 8. Resultado Esperado Si Sigues Esta Guía

Si ejecutas estos pasos con profundidad y coherencia, tendrás un documento con alta probabilidad de obtener máxima puntuación porque:

- Cumples todos los apartados solicitados
- Cubres cada criterio con evidencia de trabajo completo
- Vinculas la auditoría con la arquitectura lógica y el incidente real
- Presentas una memoria formal, técnica y defendible en contexto académico
