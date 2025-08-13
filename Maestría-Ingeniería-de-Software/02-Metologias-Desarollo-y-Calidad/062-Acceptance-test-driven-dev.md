# Desarrollo Dirigido Por Pruebas De Aceptación (ATDD)

## Definición

- **ATDD (Acceptance Test-Driven Development)** es similar al TDD (Test-Driven Development), pero involucra a diferentes miembros del equipo:  
  - Clientes  
  - Usuarios  
  - Desarrolladores  
  - Expertos en pruebas  
- Todos colaboran para escribir **pruebas de aceptación** antes de implementar la funcionalidad.

## Diferencias Con TDD

- Las pruebas de aceptación se definen en estrecha colaboración con el cliente.  
- Ayuda a entender y capturar la esencia de las historias de usuario en pruebas ejecutables.

## Ciclo De Vida ATDD Según Gentricson

1. **Discutir (Discuss)**  
   - Revisión y discusión de requisitos con el cliente o Product Owner.  
   - Identificación de posibles problemas o complejidades en las historias de usuario seleccionadas para la iteración.

2. **Materializar (Distill)**  
   - Creación y definición concreta de las pruebas de aceptación.  
   - Uso de frameworks adecuados para automatizar las pruebas según tecnología y proyecto.  
   - Frameworks comunes:  
     - Fit  
     - FitNesse  
     - Concordion  
     - Robot Framework

3. **Desarrollar (Develop)**  
   - Implementación del código para que las pruebas de aceptación se ejecuten correctamente.  
   - Se puede aplicar la técnica TDD para desarrollar incrementalmente cada historia.

4. **Ver o Demostrar (Demo)**  
   - Al finalizar la iteración se presenta el incremento funcional.  
   - Se comprueba que todas las pruebas de aceptación definidas se ejecutan satisfactoriamente.

---

**Resumen:**  
ATDD es una técnica colaborativa que vincula directamente los requisitos del cliente con las pruebas automatizadas, asegurando que el software cumple con las expectativas mediante ciclos iterativos de discusión, definición, desarrollo y demostración.

---

## Microtest

### Pregunta 1

**¿Cuál de las siguientes fases no es parte del ciclo de vida ATDD?**

**Respuesta:**  
**Distill**

**Pero si debes escoger una:**  
No hay opción correcta para "no es parte" porque las cuatro (Develop, Demo, Discuss, Distill) sí son fases del ciclo ATDD.

---

### Pregunta 2

**¿Cuál es la diferencia principal entre test driven development (TDD) y acceptance test driven development (ATDD)?**

**Respuesta:**  
C. La diferencia estå en que estas pruebas se definen en estrecha colaboraciån con
El cliente, de manera que ayudan a comprender las historias de usuario y a capturar
Su esencia en pruebas ejecutables.

**Por qué:**  
La diferencia clave es la colaboración amplia en ATDD con diversas perspectivas para definir pruebas de aceptación, mientras que TDD se centra principalmente en el desarrollador escribiendo pruebas unitarias.

---

### Pregunta 3

**¿Cuál es la última fase del ciclo de vida ATDD?**

**Respuesta:**  
d. Demo.

**Por qué:**  
La última fase del ciclo ATDD es la demostración final (Demo), donde se muestra el incremento desarrollado y se verifica que las pruebas de aceptación definidas se ejecutan correctamente.

---

[¿Quieres que te ayude con más preguntas?](https://www.stickyminds.com/sites/default/files/presentation/file/2013/08STRWR_T13.pdf)