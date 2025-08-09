# 📘 Control De Costes En la Gestión De Proyectos

## 🎯 Objetivo Del Control De Costes

El control de costes tiene como finalidad **supervisar el presupuesto del proyecto**, detectar desviaciones y garantizar que el proyecto se mantenga **dentro de los límites financieros aprobados**.

### Preguntas Clave Que Responde El Control De Costes

- ¿Cuánto dinero lleva gastado el proyecto?
    
- ¿Cuánto queda por gastar?
    
- ¿Será necesario más dinero para acabar el proyecto?
    
- ¿Sobrará dinero respecto al presupuesto?
    
- ¿El proyecto va adelantado en tiempo?
    
- ¿El proyecto va retrasado con respecto a lo planificado?

---

## 🔧 Funciones Del Control De Costes

El proceso de **controlar los costes** abarca:

1. **Influir en los factores que generan cambios** en la línea base de costes.
    
2. **Aprobar y registrar cambios** relacionados con los costes.
    
3. **Prevenir sobrecostes** no autorizados que excedan la financiación disponible.
    
4. **Supervisar el desempeño de costes** para detectar variaciones.
    
5. **Mantener registros precisos** de todos los cambios aprobados.
    
6. **Comunicar las actualizaciones** a las partes interesadas.
    
7. **Tomar medidas correctivas** para mantener los costes dentro de lo previsto.

---

## 📊 Técnica Del Valor Ganado (Earned Value Management - EVM)

Una herramienta avanzada que **integra alcance, tiempo y coste** para medir el desempeño del proyecto y hacer predicciones fundamentadas.

### ¿Qué Permite El EVM?

- Medir el rendimiento del coste y el cronograma.
    
- Comparar el estado actual con la línea base.
    
- Identificar rutas críticas y tomar decisiones preventivas.
    
- Alinear costes con resultados.
    
- Dar visibilidad y responsabilidad a los stakeholders.

---

## 📐 Conceptos Clave Del Método Del Valor Ganado (I)

|Concepto|Nombre|Definición|
|---|---|---|
|**BCWS / PV**|_Planned Value_ (Valor planificado)|Coste presupuestado del trabajo programado. Se basa en el tiempo transcurrido vs. la planificación total.|
|**BCWP / EV**|_Earned Value_ (Valor ganado)|Coste presupuestado del trabajo efectivamente realizado. Mide el rendimiento real.|
|**ACWP / AC**|_Actual Cost_ (Coste actual)|Coste real del trabajo ejecutado. Se obtiene de los registros contables.|
|**BAC**|_Budget at Completion_|Presupuesto total autorizado del proyecto.|
|**EAC**|_Estimate at Completion_|Estimación del coste total al finalizar el proyecto.|
|**VAC**|_Variance at Completion_|Diferencia entre el presupuesto total y el coste estimado al final.|

---

![[Pasted image 20250630170152.png]]

## 🧮 Fórmulas Clave Del Valor Ganado

$$
CV (Cost Variance)=EV−AC\text{CV (Cost Variance)} = EV - AC
$$
> **Indica si hay sobrecoste o ahorro.**

- CV > 0 → Ahorro
    
- CV < 0 → Sobrecoste

$$
SV (Schedule Variance)=EV−PV\text{SV (Schedule Variance)} = EV - PV
$$
> **Indica si estamos adelantados o retrasados.**

- SV > 0 → Adelanto
    
- SV < 0 → Retraso

$$CPI (Cost Performance Index)=EVAC\text{CPI (Cost Performance Index)} = \frac{EV}{AC}$$

> **Eficiencia en uso del presupuesto.**

- CPI > 1 → Gasto eficiente
    
- CPI < 1 → Gasto ineficiente

$$SPI (Schedule Performance Index)=EVPV\text{SPI (Schedule Performance Index)} = \frac{EV}{PV}$$

> **Eficiencia en ejecución del cronograma.**

- SPI > 1 → Adelantado
    
- SPI < 1 → Retrasado

$$EAC=BACCPI  \space {EAC} = \frac{BAC}{CPI}$$

> **Proyección del coste final si continúa el rendimiento actual.**

$$VAC=BAC−EAC\space{VAC} = BAC - EAC$$

> **Diferencia entre el presupuesto original y la estimación actual.**

- VAC > 0 → Ahorro esperado
    
- VAC < 0 → Sobrecoste esperado

---

## 📈 Interpretación De Indicadores

|Indicador|Resultado > 1 / > 0|Resultado < 1 / < 0|
|---|---|---|
|**CV**|Ahorro|Sobrecoste|
|**SV**|Adelanto|Retraso|
|**CPI**|Bajo coste / Eficiente|Alto coste / Ineficiente|
|**SPI**|Advance rápido|Advance lento|
|**VAC**|Proyecto terminará por debajo del presupuesto|Proyecto excederá presupuesto|

---

## 💡 Observaciones Importantes

- Es crucial registrar **todos los costes reales**, incluyendo materiales, licencias, software, servicios subcontratados y gastos ocultos.
    
- El seguimiento puede hacerse **acumulativamente** (desde el inicio del proyecto) o por **periodos específicos**.
    
- Las decisiones estratégicas (replanificación, reestimación, gestión de riesgos) deben basarse en los **índices e indicadores de EVM**.
    
- El EVM proporciona una **base cuantitativa para justificar cambios**, solicitar recursos adicionales o redefinir el alcance.

---

## 🧠 Reflexión Final

El control de costes y la técnica del valor ganado **van más allá del simple seguimiento financiero**. Permiten **tomar decisiones fundamentadas**, proyectar resultados, detectar desviaciones a tiempo y garantizar la **sostenibilidad y éxito del proyecto**.

---

## MicroTest


### **Pregunta 1:**

**¿Cuál de estas afirmaciones es correcta?**

✅ **Respuesta correcta: d.**  
**"Los criterios de imputación de costes tratan de reconocer el coste sobre las actividades del proyecto cuando este se produce, a la vez de requerir la menor carga burocrática posible."**

🔍 **Explicación:**

- La opción **a** es incorrecta porque si el **CV (Cost Variance)** es positivo, significa que el proyecto **va por debajo del presupuesto** (no sobrecoste), y si el **SV (Schedule Variance)** es negativo, **va con retraso** (no adelantado).
    
- La opción **b** es incorrecta: cuando **VC y VP son negativos**, es señal de problemas (más coste o más retraso), **no de estar mejor**.
    
- La opción **c** es incorrecta: **CPI** y **SPI** sí **permiten hacer previsiones futuras** del comportamiento del proyecto (por ejemplo, estimaciones a final del proyecto: **EAC**, **ETC**, etc.).
    

---

### **Pregunta 2:**

**¿En qué situación nos encontraremos al terminar el proyecto (aproximadamente)?**

✅ **Respuesta correcta: c.**  
**"Con un adelanto de un mes y 2000 € por debajo de coste."**

🔍 **Explicación:**

- CPI = 1.02 ⇒ eficiencia en coste del 102%, es decir, **estamos gastando menos de lo presupuestado**.
    
- SPI = 1.09 ⇒ eficiencia temporal del 109%, es decir, **vamos más rápido de lo previsto**.
    
- Si el proyecto es de 12 meses, un SPI de 1.09 indica una ganancia de tiempo del **9% del total**, es decir, aproximadamente **1 mes de adelanto**.
    
- Un CPI de 1.02 en un presupuesto de 100,000 € indica que **ahorraremos aproximadamente un 2%**, o sea **2,000 €**.
    

---

### **Pregunta 3:**

**¿Qué permite el EVT (Earned Value Technique)?**

✅ **Respuesta correcta: d.**  
**"Permite controlar la ejecución de un proyecto a través de su presupuesto y de su calendario de ejecución."**

🔍 **Explicación:**

- El **Valor Ganado (EVT)** es una técnica que **integra** el avance temporal y el coste, permitiendo hacer **comparaciones del trabajo planificado vs. el realizado vs. el coste**.
    
- Por tanto, **no se limita solo a presupuesto o solo al calendario**, como sugieren las opciones **b** y **c**.
    
