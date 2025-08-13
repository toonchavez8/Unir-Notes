# Modelos De Calidad Del Producto Software

## Estructura General De Los Modelos De Calidad

- Los modelos se organizan en:  
  - **Factores de calidad**  
  - Dentro de cada factor, **criterios**  
  - Dentro de cada criterio, **métricas** cuantitativas que permiten medir la presencia de atributos.

## Clasificación De Modelos De Calidad

| Tipo de modelo | Descripción | Ventajas | Inconvenientes |
|----------------|-------------|----------|----------------|
| **Fijos**      | Catálogo estándar de factores y criterios para evaluación | Facilita comparación común entre proyectos | Falta de flexibilidad, assume que un conjunto fijo aplica a todos los proyectos |
| **A medida**   | Definidos específicamente para cada proyecto, basados en objetivos concretos | Adaptabilidad total a las características del producto | Alto costo de desarrollo, falta de reutilización |
| **Mixtos**     | Combinan factores de alto nivel reutilizables con refinamientos específicos para cada proyecto | Combina ventajas de fijos y a medida | Puede set complejo de implementar |

## Normas Y Estándares Relevantes

- **ISO/IEC 9126 (1991) y su actualización ISO/IEC 25000 (2014)**  
  - Definen la calidad del software en tres perspectivas:  
    - Calidad interna (calidad del código)  
    - Calidad externa (características en ejecución)  
    - Calidad en uso (perspectiva del usuario)

- **ISO/IEC 14598 (2001)**  
  - Establece procesos para evaluar la calidad del software.  
  - Relacionada con ISO/IEC 9126 pero con algunas inconsistencias.

- **Familia ISO/IEC 25000**  
  - Integra modelos de calidad y guías para evaluación.  
  - Busca unificar y mejorar las normas anteriores.

## Otros Modelos Y Organizaciones

- **SQuaRE (ISO/IEC 25000)**: Modelo mixto que clasifica calidad en características, subcaracterísticas y atributos.

- **SQuaRE (Concertium for IT Software Quality - CISQ)**  
  - Organización fundada por OMG para desarrollar estándares que permitan medir automáticamente tamaño y calidad estructural del software.  
  - Se basa en SQUERC (Software Quality Model) que propone 8 características de calidad.

- **Características clave para medición automática según OMG y CISQ:**  
  - Fiabilidad  
  - Eficiencia de desempeño  
  - Seguridad  
  - Mantenibilidad  

---

**Resumen:**  
Los modelos de calidad del software varían entre enfoques fijos, a medida y mixtos, con normas internacionales que guían su estructura y evaluación. Organizaciones como OMG impulsan estándares para automatizar la medición de atributos críticos como fiabilidad y mantenibilidad, facilitando el aseguramiento de calidad en el desarrollo de software.

---

## MicroTest

### Pregunta 1

**¿Qué tipo de modelo de calidad intenta combinar las ventajas de los modelos fijos y a medida?**

**Respuesta:**  
c. Modelos mixtos.

**Por qué:**  
Los modelos mixtos ofrecen factores reutilizables como en los modelos fijos, pero permiten refinamientos y adaptaciones específicas para cada proyecto, combinando así las ventajas de ambos enfoques.

---

### Pregunta 2

**¿Cuántas características contempla el estándar ISO/IEC 9126?**

**Respuesta:**  
c. Seis.

**Por qué:**  
ISO/IEC 9126 define seis características principales de calidad para el software: funcionalidad, fiabilidad, usabilidad, eficiencia, mantenibilidad y portabilidad.

---

### Pregunta 3

**¿Cuáles son las cuatro características que CISQ propone para automatizar su medida?**

**Respuesta:**  
d. Fiabilidad, eficiencia de desempeño, seguridad y mantenibilidad.

**Por qué:**  
CISQ destaca estas cuatro características porque son las más importantes y susceptibles de set medidas automáticamente con herramientas para evaluar la calidad estructural del código.

---

¿Quieres que siga ayudándote con más preguntas?

https://www.methodsandtools.com/archive/archive.php?id=20