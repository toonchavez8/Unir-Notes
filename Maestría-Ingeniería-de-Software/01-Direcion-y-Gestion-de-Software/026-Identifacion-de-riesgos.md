# 🧠 Análisis De Riesgos En Proyectos

## 📌 1. Identificación De Riesgos

- Se realiza **una vez establecido el plan de gestión de riesgos**.
    
- Es un **proceso iterativo**, ya que los riesgos pueden cambiar a lo largo del ciclo de vida del proyecto.
    
- Se documentan **las características** de los riesgos.

### 🧱 Estructura De Desglose De Riesgos (RBS)

- Representa los riesgos **de forma jerárquica**.
    
- Agrupa riesgos por **categorías** y **subcategorías**.
    
- Facilita la identificación de **áreas críticas** del proyecto.

---

## ⚠️ 2. Tipos De Riesgos

```mermaid
flowchart LR
A["Tipos de Riesgo"]-->B1["Fuente del Riesgo"]
A-->B2["Afectación a Objetivos"]
A-->B3["Naturaleza Temporal"]
A-->B4["Punto de Vista Corporativo"]
B1-->C1["Técnica de calidad o ejecución"]
B1-->C2["Gestión del proyecto"]
B1-->C3["Organización"]
B1-->C4["Externos"]
B2-->D1["Alcance"]
B2-->D2["Tiempo"]
B2-->D3["Coste"]
B2-->D4["Calidad"]
B3-->E1["Discretos"]
B3-->E2["Estacionales"]
B4-->F1["Negocio"]
B4-->F2["Puros"]
```

---

## 🧰 3. Técnicas De Identificación De Riesgos

```mermaid
flowchart LR
A1["Técnicas"] --> B1["Tormenta de Ideas (Brainstorming)"]
A1 --> B2["Método Delphi"]
A1 --> B3["Entrevistas"]
A1 --> B4["Análisis DAFO (FODA)"]
A1 --> B5["Técnicas de Diagramación"]
B5 --> C1["Diagrama de causa-efecto"]
B5 --> C2["Diagrama de flujo"]
B5 --> C3["Diagramas de influencia"]
```

---

## 🔍 4. Análisis Cualitativo De Riesgos

- Permite **priorizar los riesgos** identificados.
    
- Define niveles: **bajo, medio, alto**, con porcentajes asignados.
    
- Herramienta principal: **Matriz de Probabilidad e Impacto**.

### 📊 Matriz De Probabilidad - Impacto

Representa visualmente la exposición al riesgo combinando:

- **Probabilidad de ocurrencia**
    
- **Impacto sobre el proyecto**

> También conocida como **"mapa de calor"**, permite comparar y priorizar riesgos fácilmente.

📎 **Ejemplo gráfico incluido en tu archivo:**

![Matriz de probabilidad-impacto](sandbox:/mnt/data/652fb62d-c2c0-4bcb-9596-77ace5e8347c.png)

---

## 📈 5. Análisis Cuantitativo De Riesgos

- Se realiza sobre los **riesgos prioritarios**.
    
- Asigna **valores numéricos** al impacto de los riesgos.
    
- Permite **decisiones bajo incertidumbre**.

```mermaid
quadrantChart
    title "Objetivos del Análisis Cuantitativo"
    x-axis "Impacto"
    y-axis "Probabilidad"
    quadrant-1 "Evaluar si se lograrán los objetivos"
    quadrant-2 "Identificar riesgos en coste, tiempo, alcance o calidad"
    quadrant-3 "Determinar los riesgos más críticos"
    quadrant-4 "Toma de decisiones informada"
```

### 🛠️ Herramientas De Análisis Cuantitativo

```mermaid
flowchart LR
1["Herramientas Cuantitativas"]-->2["Árboles de Decisión"]
1-->3["Simulación de Monte Carlo"]
1-->4["Análisis del Valor Monetario Esperado (EMV)"]
```

#### 📌 Valor Monetario Esperado (EMV)

- Técnica estadística que **estima el resultado promedio** bajo escenarios inciertos.
    
- Riesgos: valores negativos  
    Oportunidades: valores positivos
    
- Cálculo:  
    $EMV=∑(probabilidad×impacto)$

#### 📌 Simulación De Monte Carlo

- Se ejecuta el modelo del proyecto muchas veces con **valores aleatorios de entrada**.
    
- Genera una **distribución de probabilidad** de resultados:
    
    - Coste total
        
    - Duración
        
    - Fecha de entrega esperada

#### 📌 Análisis De Sensibilidad

- Determina qué riesgos tienen **mayor impacto potential**.
    
- Evalúa un riesgo a la vez, **manteniendo constantes los demás**.

## MicroTest

- ¿Qué se debe hacer con los riesgos no críticos?:
	- Documentarlos y revisarlos periódicamente.
- Si un proyecto tiene una probabilidad del 30 % de ganar 30 000 € y una probabilidad del 20 % de perder 30 000 €, ¿cuál es el valor monetario del proyecto?:
	[- 3000 €.](<Para calcular el **Valor Monetario Esperado (EMV)** del proyecto, usamos la fórmula:

$$
\text{EMV} = \sum (\text{Probabilidad} \times \text{Impacto})
$$

### Datos

* Probabilidad de ganar 30 000 €: 30% → $0.3 \times 30\,000 = +9\,000 €$
* Probabilidad de perder 30 000 €: 20% → $0.2 \times (-30\,000) = -6\,000 €$

### Cálculo

$$
\text{EMV} = 9\,000 - 6\,000 = \boxed{3\,000\,€}
$$

✅ Por tanto, **el valor monetario esperado del proyecto es de 3 000 €**.>)

- Si se tiene dificultades en evaluar el impacto en tiempo de un determinado riesgo, ¿qué se debe hacer?:
	- Evaluarlo cualitativamente.
