# Notas De Estudio

## Ingeniería De Requisitos De Seguridad

---

## 1. Importancia De Los Requisitos De Seguridad

### Errores Comunes En Requisitos

- Muchos problemas de seguridad en software provienen de **requisitos inadecuados, incompletos o ambiguous**.
    
- Es frecuente encontrar frases como “la aplicación será segura”, lo cual no define **qué significa seguridad** ni cómo verificarse.
    
- Errores en requisitos pueden representar hasta **30–50% del costo del desarrollo**, llegando incluso al **85%** cuando requieren correcciones tardías.

### Impacto Organizacional

- La ambigüedad genera conflictos entre desarrolladores y clientes, causando:
    
    - Interpretaciones diferentes.
        
    - Retrasos en el desarrollo.
        
    - Pérdida de confianza y reputación.

---

## 2. Tipos De Requisitos De Seguridad

Los requisitos de seguridad se dividen en dos tipos principales:

### 2.1 Requisitos De Servicios De Seguridad (Funcionales / Positivos)

Definen **funcionalidades de seguridad** que el sistema debe implementar.

**Objetivo:** garantizar los servicios esenciales de seguridad.

**Ejemplos de servicios incluidos:**

- Confidencialidad
    
- Integridad
    
- Disponibilidad
    
- Autenticación
    
- Autorización
    
- Trazabilidad

### 2.2 Requisitos Del Software Seguro (No Funcionales / Negativos)

Definen **restricciones** que evitan comportamientos inseguros.

**Ejemplos:**

- No permitir la entrada de caracteres prohibidos (ej.: `'` para evitar SQL Injection).
    
- Usar **procedimientos parametrizados** para todas las consultas SQL.
    
- Requisitos de:
    
    - Gestión de sesiones
        
    - Gestión y tratamiento de errores
        
    - Recuperación ante fallos
        
    - Prevención de condiciones de carrera
        
    - Validación de entrada y salida

### Tabla Comparativa

| Tipo de requisito          | Naturaleza                 | Enfoque                                            | Ejemplos                                               |
| -------------------------- | -------------------------- | -------------------------------------------------- | ------------------------------------------------------ |
| **Servicios de seguridad** | Funcionales / positivos    | Qué funciones de seguridad debe incluir el sistema | Autenticación, autorización, trazabilidad              |
| **Software seguro**        | No funcionales / negativos | Restricciones que prohíben conductas inseguras     | Validación de entrada, evitar SQLi, gestión de errores |
|                            |                            |                                                    |                                                        |

```mermaid
graph TD
    %% Activities (Top Row)
    T1("Modelado de amenazas")
    T2("Casos abuso")
    T4("Ing. Requisitos Seguridad")
    T5(" Análisis de riesgos")
    T6(" Patrones de diseño")
    T7(" Pruebas basadas en riesgos")
    T8(" Revisión del código")
    T11(" Revisión externa")
    T3(" Modelado de ataques")
    T9(" Pruebas de penetración")
    T10("Operaciones de seguridad")

    %% SDLC Phases (Bottom Row)
    P1["REQUISITOS / CASOS DE ABUSO"]
    P2["ARQUITECTURA / DISEÑO"]
    P3["CODIFICACIÓN E INTEGRACIÓN"]
    P4["PRUEBAS"]
    P5["DISTRIBUCIÓN Y DESPLIEGUE"]
    P6["OPERACIÓN Y MANTENIMIENTO"]

    %% Enforce Sequential Flow for Phases (P1 -> P6)
    P1 --> P2
    P2 --> P3
    P3 --> P4
    P4 --> P5
    P5 --> P6

    %% Connections from Activities to Phases

    %% Left Side Activities
    T1 --> P1
    T1 --> P2
    T2 --> P1
    T4 --> P1
    T4 --> P2
    T6 --> P2
    T6 --> P3
    T8 --> P3
    T7 --> P3
    T7 --> P4

    %% T5 (Análisis de riesgos) connects to ALL phases
    T5 --> P1
    T5 --> P2
    T5 --> P3
    T5 --> P4
    T5 --> P5
    T5 --> P6

    %% Right Side Activities
    T11 --> P5
    T11 --> P6
    T3 --> P4
    T3 --> P5
    T3 --> P6
    T9 --> P4
    T9 --> P5
    T9 --> P6
    T10 --> P6

    %% Feedback Loop (Realimentación) - Using a dashed line to mimic the curved arrow
    P6 -. REALIMENTACIÓN .-> P1

    %% Styling (To match the visual appearance of the source image)
    classDef activity fill:#e6f3ff,stroke:#3b82f6,stroke-width:2px;
    classDef phase fill:#007bff,stroke:#0056b3,color:#ffffff,font-weight:bold;

    class T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11 activity
    class P1,P2,P3,P4,P5,P6 phase
```

---

## 3. Otros Requisitos Relacionados Con la Seguridad (no específicos)

Contribuyen indirectamente a la seguridad del sistema:

- Requisitos del entorno de producción
    
- Hardening y configuración
    
- Interoperabilidad
    
- Auditoría y validación de seguridad
    
- Cumplimiento normativo:
    
    - Leyes de protección de datos
        
    - Esquema Nacional de Seguridad
        
    - ISO/IEC 27001 y 27002

---

## 4. Fuentes Comunes Para Extraer Requisitos De Seguridad

### Principales Fuentes

- **Normativas y estándares** (ISO 27001, 27002, ENS).
    
- **Modelado de ataques** y análisis de amenazas.
    
- **Análisis de riesgos arquitectónico**.
    
- **Reuniones con usuarios y stakeholders**.
    
- **Políticas de seguridad de la organización**.
    
- **Casos de uso** y sus implicaciones de seguridad.
    
- **Components a reutilizar**, tecnología existente y vulnerabilidades conocidas.
    
    - Aquí se utilize el **Software Composition Analysis (SCA)**.
        
- **Tendencias tecnológicas** y nuevas soluciones de seguridad.

---

## 5. Diagrama General Para Especificar Requisitos De Seguridad

```mermaid
flowchart TD
    A[Identificación de requisitos de seguridad] --> B[Validación de entrada]
    A --> C[Validación de salida]
    A --> D[Seguridad de datos]
    A --> E[Seguridad del entorno y componentes]
    D --> D1[Clasificación de datos<br/>críticos o confidenciales]
    D --> D2[Definición de medidas de protección]
    E --> E1[Seguridad de organismos y servicios externos]
```

---

## 6. Ejemplos De Requisitos (del transcript)

### 6.1 Requisito Positivo

“El sistema deberá registrar todas las acciones de acceso y modificación de datos.”

### 6.2 Requisito Negativo

“No se permitirá el uso de comillas simples en los parámetros de entrada para evitar inyección SQL.”

---

## 7. Información Adicional Relevante

- La especificación de requisitos de seguridad debe set:
    
    - Clara
        
    - Medible
        
    - Verificable
        
    - No ambigua
        
- Dejar requisitos abiertos o subjetivos incrementa riesgos técnicos y contractuales.

---

## Resumen De Puntos Clave

- La mayoría de vulnerabilidades provienen de **requisitos inadecuados o mal definidos**.
    
- Existen **dos tipos**: requisitos funcionales de seguridad y requisitos no funcionales (restricciones).
    
- Fuentes principales: **normativas, análisis de amenazas, políticas internas y SCA**.
    
- La especificación debe incluir validación de entrada/salida, seguridad de datos, seguridad del entorno y consideraciones normativas.

---

## MicroTest

1. Señalar la respuesta incorrecta. Respecto a la ingeniería de requisitos de seguridad:
    
    - **La respuesta:** B
        
    - **Justificación:**  
        La opción B describe **funciones de seguridad** (mecanismos como autenticación, autorización, cifrado), no **requisitos de software seguro**. Los requisitos de software seguro son condiciones que reducen la probabilidad de fallos de seguridad, mientras que las funciones mencionadas en B corresponden a requisitos funcionales de seguridad. Por lo tanto, es la afirmación incorrecta.

---

1. Los requisitos que se especifican para protegerse contra la destrucción de la información o el propio software se denominan comúnmente:
    
    - **La respuesta:** B
        
    - **Justificación:**  
        La destrucción de información o software es una violación de **integridad**, que implica proteger los datos contra modificaciones no autorizadas, corrupción o eliminación. Confidencialidad, disponibilidad y autenticación no se enfocan en evitar la destrucción de la información.

---

1. ¿Cuál de los siguientes bloques de requisitos debe incluir el siguiente requisito? «Todos los programas de procesamiento de transacciones financieras deben utilizar más de un factor para verificar la identidad de la entidad que solicita el acceso»:
    
    - **La respuesta:** B
        
    - **Justificación:**  
        El uso de más de un factor para verificar la identidad corresponde directamente a **autenticación multifactor**. Su objetivo es validar la identidad del sujeto antes de permitir acceso. No es un requisito de autorización, auditoría ni disponibilidad.