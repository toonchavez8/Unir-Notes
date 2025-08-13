# Desarrollo Dirigido Por Comportamiento (BDD)

## Introducción a BDD

- **BDD (Behavior-Driven Development)** busca minimizar el despilfarro de recursos centrándose en desarrollar solo el código necesario para cumplir requisitos funcionales.
- Permite describir comportamientos en un lenguaje natural, accessible para todos los **stakeholders**:  
  - Clientes  
  - Usuarios  
  - Generadores de pruebas  
  - Desarrolladores  
  - Expertos en dominio  
- No require que todos tengan formación técnica.

## Relación Con TDD

- BDD es una extensión de TDD, pero menos centrada en la implementación técnica y más orientada al escenario y comportamiento del sistema.
- Se enfoca en el problema que se resuelve y en describir el comportamiento desde la perspectiva del usuario.

## Orígenes Y Referencias

- Creado por **Dan North** en 2009, quien desarrolló el framework **JBehave (jbj)**.
- Considerado una metodología ágil de segunda generación, orientada "de afuera hacia adentro".
- La metodología facilita extraer información de múltiples stakeholders con alta automatización.

## Herramientas Y Notaciones

- Herramientas para transformar historias de usuario a notaciones formales pero en lenguaje natural.
- Comportamientos esperados quedan claramente definidos y automatizados.
- Notación clave: **GWT (Given-When-Then)**  
  - **Given**: Contexto o precondiciones.  
  - **When**: Acción o evento que el usuario realiza.  
  - **Then**: Resultado esperado o respuesta del sistema.

## Ventajas De BDD

- Mejora la comunicación entre todos los participantes del proyecto.  
- Facilita el modelado del comportamiento desde el punto de vista del usuario.  
- Promueve la escritura de pruebas de aceptación claras y comprensibles.  

---

**Resumen:**  
BDD es una técnica que extiende TDD al involucrar stakeholders con lenguaje natural, enfocándose en el comportamiento esperado del sistema usando la plantilla Given-When-Then para definir pruebas y escenarios de aceptación de forma colaborativa y automatizada.

---

## MicroTest

### Pregunta 1

**¿Cuál de los siguientes no es una característica del desarrollo dirigido por comportamiento?**

**Respuesta:**  
c. Está claramente orientado a los objetivos de marketing.

**Por qué:**  
BDD se enfoca en el comportamiento del sistema y en satisfacer los requisitos funcionales desde la perspectiva del usuario y stakeholders técnicos y de negocio, no está orientado específicamente a objetivos de marketing.

---

### Pregunta 2

**¿Qué herramienta facilita un enfoque behavior driven development (BDD) con múltiples lenguajes de programación?**

**Respuesta:**  
c. Cucumber.

**Por qué:**  
Cucumber es una herramienta popular para BDD que soporta múltiples lenguajes de programación y permite definir pruebas en lenguaje natural siguiendo la notación Given-When-Then. JBehave también es una opción pero está más ligada a Java, mientras que Cucumber es más multi-lenguaje.

---

### Pregunta 3

**¿Cómo se compone la notación given-when-then?**

**Respuesta:**  
b. Se compone de tres partes: given (dado que), when (cuando) y then (entonces).

**Por qué:**  
La notación Given-When-Then es una plantilla estándar en BDD que define:

- **Given:** el contexto inicial o precondiciones.
    
- **When:** la acción o evento que ocurre.
    
- **Then:** el resultado esperado o la consecuencia.

---

¿Quieres que continúe ayudándote con más preguntas?

https://agilealliance.org/glossary/bdd/