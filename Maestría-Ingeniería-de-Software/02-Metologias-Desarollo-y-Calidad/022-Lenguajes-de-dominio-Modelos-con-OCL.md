# **Idea Clave 4. Lenguajes De Dominio Específico. Refinamientos De Modelos Con OCL**

---

## **Lenguajes De Dominio Específico (DSL)**

- Los **lenguajes de dominio específico (DSL)** son diseñados para un dominio concreto.
    
- Ejemplos de DSL incluyen **HTML**, **VHDL** y **SQL**.
    
- Si el lenguaje es de modelado, se lo conoce como **lenguaje de modelado de dominio específico (DSML)**.
    
- Un DSL se puede ver como un **metamodelo** que incluye conceptos propios de un determinado dominio:
    
    - Ejemplo: un DSL para **domótica** incluiría conceptos como:
        
        - _Sensor de temperatura_
            
        - _Calefacción automática_
            
        - _Sensor de luz de persiana automática_, etc.
            
- Cada metamodelo puede tener asociado un DSL concreto que describe:
    
    - Los **elementos del modelo**
        
    - Su **disposición**
        
    - Sus **relaciones**
        
    - Sus **restricciones**
        
- Utilizar un DSL ayuda a **recoger las necesidades de los stakeholders** para un dominio específico.
    
- Aunque **UML** es un lenguaje de propósito general, algunos dominios pueden necesitar elementos específicos **no disponibles en UML**.
    
    - Se pueden utilizar **perfiles de UML** para definir un DSL concreto, pero esto arrastra todo el metamodelo de UML (no solo la parte relevante para el DSL).

---

## **Object Constraint Language (OCL)**

- **OCL** es un lenguaje que surgió para resolver limitaciones de UML en la especificación de aspectos en modelos de diseño de software.
    
- Es un lenguaje **formal** adoptado como estándar por el **OMG (Object Management Group)**.
    
- Las expresiones en OCL agregan información **clara** y **no ambigua** a modelos orientados a objetos.
    
- En **UML 1.1**, OCL se usaba exclusivamente para especificar **restricciones sobre valores** en modelos u objetos.
    
- En **UML 2**, OCL no solo se usa para definir restricciones, sino también para:
    
    - Reglas formales en el diseño de **DSL**
        
    - Otras operaciones en modelos
        
- **Características de OCL** (Brambilla, M., Cabot, J. y Wimmer, M., 2012):
    
    1. **Tipado**:
        
        - Cada expresión OCL tiene un tipo.
            
        - Evalúa a un valor de ese tipo y debe set conforme a las reglas y operaciones del tipo.
            
    2. **Sin efectos laterales**:
        
        - Las expresiones OCL pueden hacer consultas o imponer restricciones en el estado del sistema, pero **no lo modifican**.
            
    3. **Declarativo**:
        
        - OCL **no incluye** construcciones imperativas.
            
    4. **Especificación**:
        
        - Es un lenguaje de especificación que **no incluye detalles de implementación** ni ofrece guías para la implementación del sistema.
            
- OCL se suele utilizar como **complemento en la definición de metamodelos**, proporcionando un conjunto de reglas textuales que todo modelo conforme a dicho metamodelo debe cumplir.
    
- Las restricciones en OCL se presentan como **invariantes** definidas en el contexto de un tipo específico (conocido como _tipo de contexto_).
    
    - Como cuerpo de la restricción se define una **expresión booleana** que debe satisfacerse en todas las instancias del tipo de contexto.

---

### **Ejemplos De Invariantes En OCL**

1. **Restricción sobre atributos de fecha**
    
    - Contexto: `Convocatoria`
        
    - Invariante: el atributo `end` debe set mayor que el atributo `start`.

    ```ocl
    context Convocatoria
    inv: self.end > self.start
    ```

2. **Restricción sobre colección de participantes**
    
    - Contexto: `Convocatoria`
        
    - Invariante: `numParticipantes` debe set igual al total de participantes únicos en todos los programas incluidos en la convocatoria.
        
    - Se usa la operación `asSet()` para evitar contar más de una vez al mismo objeto participante.

    ```ocl
    context Convocatoria
    inv: numParticipantes = programas.participantes -> asSet() -> size()
    ```

---

> **Referencia bibliográfica para OCL:**  
> Brambilla, M., Cabot, J. y Wimmer, M. (2012). _Model-driven software engineering in practice_. Synthesis Lectures on Software Engineering.

---

# **Resumen De Contenidos**

1. **Lenguajes de Dominio Específico (DSL)**
    
    - Definición y ejemplos prácticos.
        
    - Relación con metamodelos y DSML.
        
    - Ventajas de usar DSL frente a UML puro para dominios concretos.
        
2. **Object Constraint Language (OCL)**
    
    - Origen y adopción como estándar.
        
    - Características principales: tipado, sin efectos laterales, declarativo y de especificación.
        
    - Uso de OCL en metamodelos para definir restricciones e invariantes.
        
    - Ejemplos de invariantes en un contexto real (Convocatoria en un sistema de gestión de eventos).
---

## MicroTest

- ¿Cuáles son ejemplos de lenguajes de dominio específico?
	- HTML para el desarrollo de páginas web, VHDL para lenguajes de descripción de hardware y SQL para las bases de datos.
- ¿Cómo se les conoce a los lenguajes de modelado de dominio específico?
	- Lenguaje de modelado de dominio específico (domain-specific modeling language, DSML).
- ¿Cuáles son algunos conceptos que incluiría un domain-specific languages (DSL) para domótica?
	- Sensor de temperatura, calefacción automática y sensor de luz de persiana automática.
- ¿Qué tipo de lenguaje es object constraint language (OCL)?
	- Lenguaje formal de propósito general.
- ¿Cómo se definen las restricciones en OCL?
	- Como invariantes definidas en el contexto de un tipo específico.
---

## Saber Mas

https://modeling-languages.com/ocl-tutorial/
