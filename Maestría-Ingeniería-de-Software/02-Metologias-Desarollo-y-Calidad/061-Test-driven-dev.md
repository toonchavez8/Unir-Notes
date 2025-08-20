Aquí tienes las notas estructuradas de la clase sobre **Test-Driven Development (TDD)**:

---

# 📌 Notas Sobre Test-Driven Development (TDD)

## 1. Definición Y Contexto

- **TDD** (_Test-Driven Development_) es una técnica de construcción de software que **guía el desarrollo empezando por escribir las pruebas**.
    
- Surge principalmente del contexto de **Extreme Programming (XP)**.
    
- Se aplica de forma más efectiva en **modelos de desarrollo iterativos y ágiles**.
    
- Evita el problema de realizar pruebas solo al final del proyecto (donde los costos de corregir errores son más altos) → se **adelanta la fase de pruebas**.

---

## 2. Ciclo Básico De TDD

El flujo de trabajo de TDD sigue **tres pasos iterativos**:

1. **Escribir una prueba que falle**.
    
2. **Hacer que el código pase la prueba**.
    
3. **Refactorizar**: limpiar, reorganizar y optimizar el código sin romper las pruebas.

> **Objetivo final:** tener código limpio, funcional y fácil de mantener.

---

## 3. Diferencia Con Enfoques Tradicionales

- **Tradicional**: desarrollo → integración → pruebas al final.
    
- **TDD**: cada iteración incluye **análisis, diseño, implementación y pruebas**.
    
- Incluye refactorización continua para mantener calidad y simplicidad.

---

## 4. Conceptos Erróneos Frecuentes (según Estudio De Hansen Y Saidian)

- ❌ Pensar que **TDD = pruebas automatizadas**.
    
- ❌ Creer que **TDD implica escribir todos los tests al inicio**.
    
- ✅ TDD implica **pequeñas iteraciones**, centradas en **una funcionalidad concreta**.

---

## 5. Beneficios Y Métricas Asociadas

- **Mayor cobertura de pruebas** → más confianza en el código.
    
- **Menor tamaño del código** → simplicidad y facilidad de mantenimiento.
    
- **Menor acoplamiento** → módulos más independientes.
    
- **Mayor cohesión** → métodos y datos bien relacionados dentro de una unidad.
    
- **Menor complejidad** → clases y métodos más pequeños y fáciles de entender.

---

## 6. Uso Como Técnica De Análisis Y Diseño

- Las pruebas asociadas garantizan que **cualquier cambio futuro no rompa la funcionalidad existente**.
    
- Ayuda a **pensar en los requisitos antes de escribir código**.

---

## 7. Patrón Triple A (AAA)

- **Arrange**: inicializar objetos y variables necesarias.
    
- **Act**: ejecutar la acción o método a probar.
    
- **Assert**: verificar que el resultado es el esperado.

Ejemplo:

```java
// Arrange
Calculadora calc = new Calculadora();
int esperado = 4;

// Act
int resultado = calc.sumar(2, 2);

// Assert
assertEquals(esperado, resultado);
```

---

## 8. Herramientas Y Frameworks Para TDD

- **Serenity**
    
- **Robot Framework**
    
- **PHPUnit**

---

# Microtest

## Pregunta 1

**¿Cuál de las siguientes es una ventaja del enfoque de desarrollo TDD?**

**Respuesta:**  
d. Las respuestas A y C son correctas.

**Por qué:**  
TDD ayuda a construir código que se verifica automáticamente mediante pruebas (respuesta A) y también mejora el diseño del producto porque obliga a pensar en pruebas y diseño antes de la implementación, aunque no haya una fase específica dedicada a diseño (respuesta C). Por eso, ambas son ventajas reales de TDD.

---

## Pregunta 2

**El concepto TDD es sinónimo de:**

**Respuesta:**  
b. Test-first.

**Por qué:**  
TDD (Test-Driven Development) significa desarrollar con pruebas primero, es decir, escribir las pruebas antes de implementar el código. No es sinónimo de pruebas automatizadas (aunque las usa), ni de BDD (Behavior-Driven Development) o ATDD (Acceptance Test-Driven Development), que son metodologías relacionadas pero distintas.

---

## Pregunta 3

**¿En qué consiste el patrón AAA dentro de la técnica TDD?**

**Respuesta:**  
d. En estructurar las pruebas, comenzando por la definición de parámetros de entrada, colocar luego las acciones a ejecutar y, finalmente, comprobar los resultados esperados.

**Por qué:**  
El patrón AAA (Arrange, Act, Assert) es una forma estándar de organizar pruebas unitarias: primero se preparan los datos y condiciones (Arrange), luego se ejecuta el código a probar (Act), y finalmente se verifica que el resultado sea el esperado (Assert).

---

Claro, aquí tienes las preguntas con sus respuestas y la explicación de por qué son correctas:

---

### Pregunta 1

**¿Cuál de las siguientes es una ventaja del enfoque de desarrollo TDD?**

**Respuesta:**  
d. Las respuestas A y C son correctas.

**Por qué:**  
TDD ayuda a construir código que se verifica automáticamente mediante pruebas (respuesta A) y también mejora el diseño del producto porque obliga a pensar en pruebas y diseño antes de la implementación, aunque no haya una fase específica dedicada a diseño (respuesta C). Por eso, ambas son ventajas reales de TDD.

---

### Pregunta 2

**El concepto TDD es sinónimo de:**

**Respuesta:**  
b. Test-first.

**Por qué:**  
TDD (Test-Driven Development) significa desarrollar con pruebas primero, es decir, escribir las pruebas antes de implementar el código. No es sinónimo de pruebas automatizadas (aunque las usa), ni de BDD (Behavior-Driven Development) o ATDD (Acceptance Test-Driven Development), que son metodologías relacionadas pero distintas.

---

### Pregunta 3

**¿En qué consiste el patrón AAA dentro de la técnica TDD?**

**Respuesta:**  
d. En estructurar las pruebas, comenzando por la definición de parámetros de entrada, colocar luego las acciones a ejecutar y, finalmente, comprobar los resultados esperados.

**Por qué:**  
El patrón AAA (Arrange, Act, Assert) es una forma estándar de organizar pruebas unitarias: primero se preparan los datos y condiciones (Arrange), luego se ejecuta el código a probar (Act), y finalmente se verifica que el resultado sea el esperado (Assert).

---

https://martinfowler.com/bliki/TestDrivenDevelopment.HTML
