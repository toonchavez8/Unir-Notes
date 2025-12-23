# Tema 4: Resumen sobre plataformas Low-Code, No-Code y Aceleradoras

## 1. Contexto dentro del ciclo de vida del software

### Ciclo de vida del desarrollo

El desarrollo de software se estructura en las siguientes fases:

- Requisitos
    
- Análisis
    
- Diseño
    
- Implementación
    
- Pruebas
    
- Despliegue
    
- Monitorización
    

Este ciclo es independiente de la metodología utilizada:

- **Waterfall**: fases secuenciales.
    
- **Iterativa o incremental**: fases repetidas en ciclos cortos.
    

### Ubicación de las plataformas Low-Code y No-Code

- Actúan principalmente en la **fase de implementación**.
    
- También impactan en el **diseño**, ya que el desarrollo se basa en modelos que luego generan código automáticamente.
    
- Muchas plataformas también automatizan **despliegue y mantenimiento**.
    

---

## 2. Pruebas en plataformas Low-Code y No-Code

### Tipos de pruebas

- **Pruebas de verificación**: comprueban que el código generado es correcto.
    
- **Pruebas de validación**: verifican que el sistema hace lo que el usuario realmente necesita.
    

### Situación en estas plataformas

- Generalmente **no requieren pruebas de verificación**, ya que el código se genera automáticamente.
    
- **No sustituyen las pruebas de validación**, ya que un mal modelado puede producir un sistema incorrecto desde el punto de vista del usuario.
    

---

## 3. Valor y utilidad de las plataformas Low-Code y No-Code

### Problemas actuales del desarrollo software

1. Crecimiento constante de lenguajes y frameworks.
    
2. Reducción del tiempo exigido por las empresas para entregar soluciones.
    
3. Falta de perfiles cualificados suficientes a nivel global.
    

### Soluciones propuestas

- Aumentar vocaciones **STEM**.
    
- Incorporar perfiles no técnicos al desarrollo (concepto de **Citizen Developer**).
    
- Proporcionar herramientas:
    
    - Low-Code
        
    - No-Code
        
    - Asistentes y copilotos para desarrolladores profesionales.
        

---

## 4. Diferencia entre Low-Code y No-Code

### No-Code

- No permiten extender la funcionalidad con código.
    
- Todo el desarrollo se realiza mediante modelado visual.
    
- Menor flexibilidad.
    

### Low-Code

- Permiten cierta extensión mediante código propio.
    
- La extensión debe hacerse en la misma pila tecnológica.
    
- Ofrecen un equilibrio entre velocidad y flexibilidad.
    

---

## 5. Taxonomía según nivel de abstracción

### Escala de abstracción y velocidad

```mermaid
graph LR
    A[Código fuente<br/>Java] --> B[Frameworks<br/>Spring]
    B --> C[Plataformas aceleradoras<br/>JHipster]
    C --> D[Entornos Full-Stack]
    D --> E[Low-Code / No-Code]
```

### Interpretación

- A mayor abstracción:
    
    - Mayor velocidad de desarrollo.
        
    - Menor flexibilidad.
        
- A menor abstracción:
    
    - Mayor control.
        
    - Mayor esfuerzo y tiempo.
        

---

## 6. Criterios de clasificación de plataformas

### Según su foco principal

|Categoría|Punto de partida|
|---|---|
|Data-driven|Base de datos|
|Process-driven|Procesos de negocio|
|UI-driven|Interfaz de usuario|
|General Purpose|Cualquiera de las anteriores|

---

## 7. Riesgos y costes: el Lock-in

### Definición de Lock-in

El **lock-in** es el riesgo de quedar atado a una plataforma debido a que:

- El valor principal está en los modelos.
    
- No se tiene acceso al código fuente o no es fácilmente mantenible.
    
- El coste de licencias puede aumentar.
    
- La plataforma puede desaparecer.
    

### Impacto

- Mucho esfuerzo en análisis, diseño e implementación.
    
- Poco control sobre el resultado final.
    
- Dificultad para migrar a otra tecnología.
    

---

## 8. Plataformas comerciales Low-Code

### Ejemplos habituales

- OutSystems
    
- Mendix
    
- Microsoft Power Platform
    

### Proceso típico de desarrollo

1. Creación de la base de datos.
    
2. Generación automática de listas y formularios mediante drag-and-drop.
    
3. Ajuste de la experiencia de usuario (UX).
    
4. Añadir lógica:
    
    - Lado cliente.
        
    - Lado servidor.
        
5. Validación y despliegue automático desde un único entorno.
    

---

## 9. Plataformas Open Source: enfoque Data-Driven

### Ejemplo: Saltcorn

#### Características

- Desarrollo basado en datos.
    
- Flujo principal:
    
    1. Crear tablas y relaciones.
        
    2. Definir vistas (listas, fichas, filtros).
        
    3. Agrupar vistas en páginas.
        
- No genera código fuente:
    
    - El comportamiento es interpretado en tiempo de ejecución.
        
    - Aumenta el riesgo de lock-in, incluso siendo open source.
        

---

## 10. Plataformas aceleradoras

### Concepto

Las plataformas aceleradoras:

- Generan grandes cantidades de código automáticamente.
    
- No se consideran Low-Code o No-Code.
    
- Aceleran el **bootstrap** inicial del proyecto.
    

### Ejemplo: JHipster

#### Funcionamiento general

- Asistente inicial con preguntas de configuración.
    
- Las respuestas se guardan en un fichero.
    
- Generación automática de:
    
    - Cliente (Angular, React, Vue).
        
    - Servidor (Spring Boot).
        
    - Base de datos gestionada con Liquibase.
        
- Soporte para:
    
    - Arquitectura monolítica.
        
    - Microservicios.
        
    - Contenedores y despliegue en la nube.
        

#### Modelado con JDL

- Permite definir entidades y relaciones.
    
- Genera automáticamente:
    
    - Entidades.
        
    - Servicios CRUD.
        
    - Controladores REST.
        
    - APIs accesibles mediante OpenAPI.
        

### Limitación principal

- Si se modifica manualmente el código y se vuelve a regenerar:
    
    - Aparecen conflictos.
        
    - Es necesario gestionar cuidadosamente el merge.
        

---

## 11. Comparativa general de enfoques

|Enfoque|Código generado|Flexibilidad|Riesgo de Lock-in|
|---|---|---|---|
|Código tradicional|No|Muy alta|Bajo|
|Frameworks|Parcial|Alta|Bajo|
|Aceleradoras|Sí|Media|Medio|
|Low-Code|Sí|Baja|Alto|
|No-Code|Sí|Muy baja|Muy alto|

---

## Resumen de puntos clave

- Las plataformas Low-Code y No-Code se sitúan principalmente en la fase de implementación.
    
- Reducen tiempo de desarrollo a cambio de flexibilidad.
    
- El riesgo de lock-in es un factor crítico en su elección.
    
- Existen soluciones comerciales, open source y aceleradoras.
    
- Las plataformas aceleradoras generan código, pero requieren gestión cuidadosa de cambios.
    
- Elegir la plataforma adecuada implica equilibrar velocidad, control y sostenibilidad.
    

## MicroTest

[[026-resumen-04]]