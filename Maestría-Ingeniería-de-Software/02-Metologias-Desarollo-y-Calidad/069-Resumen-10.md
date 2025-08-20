# Resumen Tema 10: Verificación, Validación Y Calidad Del Software

## Verificación Y Validación (V&V)

- **Verificación:** Comprobar que el software se construyó correctamente, funciona bien y está libre de errores.
- **Validación:** Asegurar que el software es apropiado para su uso previsto.
- Preguntas clave:
  - ¿Estamos construyendo el sistema correctamente? (Verificación)
  - ¿Estamos construyendo el sistema correcto? (Validación)

## Tipos De Pruebas De Software

1. **Pruebas Unitarias**
   - Se realizan de forma aislada.
   - Recomiendan simular dependencias para asegurar independencia.
   - Aplican el patrón **Triple-A:** Arrange, Act, Assert.
2. **Pruebas de Integración**
   - Verifican la interacción correcta entre módulos o components.
3. **Pruebas Funcionales o de Validación**
   - Incluyen pruebas alfa y beta.
4. **Pruebas del Sistema**
   - Incluyen pruebas específicas como recuperación, seguridad y esfuerzo.
5. **Pruebas de Aceptación**
   - Confirman que el trabajo está finalizado.
   - Diferencian en objetivo y resultado con las unitarias.

## Desarrollo Dirigido Por Pruebas (TDD Y BDD)

- **TDD:** Escribir tests antes del código para reducir errores y costos.
- No es lo mismo que pruebas automatizadas, aunque se utilizan juntos.
- Métricas relevantes: cobertura, tamaño del código, acoplamiento, cohesión, complejidad.
- Frameworks y herramientas populares: Serenity, Robot Framework, PHPUnit.
- **BDD (Desarrollo Dirigido por Pruebas de Aceptación):**
  - Involucra a clientes, usuarios, desarrolladores y expertos en pruebas.
  - Minimiza desperdicio y enfoca en requisitos funcionales concretos.

## Normativas Y Modelos De Calidad De Software

### ISO 9000:2005

- Define calidad como el grado en que un conjunto de características inherentes cumple con los requisitos.

### ISO IEC 9126-2001

- Enfoques en tres perspectivas:
  - Calidad interna (código)
  - Calidad externa (comportamiento en ejecución)
  - Calidad en uso (desde la perspectiva del usuario)

### ISO IEC 141998

- Establece procesos para evaluar la calidad del software.

### Problemas Con Normas Anteriores

- Inconsistencias entre ISO 9126 y ISO 141998 llevaron a desarrollo de la familia **ISO IEC 25000**.

### ISO IEC 25000 (SQuaRE)

- Marco común para evaluar la calidad del producto software.
- Se divide en cinco grandes divisiones con normas específicas:
  - **25001-2:** Calidad de datos inherentes y dependientes del sistema.
  - **25002-0:** Medición de calidad del software.
  - **25004-0:** Evaluación del software.
- Beneficios de certificación:
  - Diferenciación para fabricantes.
  - Facilita acuerdos de servicio.
  - Detecta y reduce costos de mantenimiento.

### SISC (Consorcio OMG)

- Enfocado en automatizar la medición del tamaño del software y calidad estructural.
- Basado en características clave: fiabilidad, eficiencia, seguridad y mantenibilidad.

## Factores Que Afectan la Calidad Del Producto Software

- Calidad del proceso.
- Tecnología empleada.
- Cualificación del personal.
- Recursos disponibles (tiempo, presupuesto).

## Modelos Para la Mejora Del Proceso De Software

- **CMM y CMMI (Software Engineering Institute)**
  - Indicadores sobre madurez y calidad del proceso.
  - Escalas ordinales para evaluar nivel de madurez organizacional.
  - Marcos conceptuales para la mejora continua.
  - Componente clave: conjunto de buenas prácticas para procesos eficaces.
  
---

**Gracias por tu atención.**
