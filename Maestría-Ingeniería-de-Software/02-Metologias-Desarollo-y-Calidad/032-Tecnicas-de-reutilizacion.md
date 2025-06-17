# Reutilización De Software En Ingeniería

Los enfoques más antiguos permitieron la reutilización de rutinas encapsuladas en simples funciones.  
El paradigma de la orientación a objetos permitió reutilizar elementos de complejidad y granularidad creciente, como las clases.  
La comunidad de ingeniería de software desarrolló **patrones de arquitectura y diseño** para evitar enfrentarse desde cero a problemas habituales.

Actualmente, existen components y subsistemas enteros, _frameworks_ de desarrollo y servicios que podemos aprovechar en nuestros proyectos.

---

## Diseño Arquitectónico

El diseño arquitectónico es una **representación de la estructura general de un sistema a un alto nivel de abstracción**.

- Los buenos diseños arquitectónicos permiten:
    
    - Identificar relaciones entre sistemas.
        
    - Favorecer la reutilización de elementos existentes.
        
    - Set una herramienta de documentación eficaz.

A lo largo de los años se han creado muchos **patrones arquitectónicos** para resolver problemas específicos.

---

## Patrones De Diseño

- Son **soluciones generales para resolver problemas frecuentes** en el diseño de software.
    
- Estas soluciones han sido probadas y aplicadas con éxito múltiples veces.
    
- Los patrones deben poder set **descritos de manera general para aplicarse en diferentes contextos**.
    
- La reutilización es un valor deseable en los patrones de diseño.

> Al aplicar un patrón, se reutilizan elementos del diseño y se pueden requerir elementos adicionales que pueden aumentar la complejidad del sistema.

---

## Librerías De Código

Una **librería de código** es un conjunto de funciones reutilizables contenidas en uno o varios ficheros.

- Estas funciones suelen estar **agrupadas según la funcionalidad** que aportan.
    
- El código de la librería se encuentra **alojado externamente al proyecto**.

### Enlaces

Hay dos enfoques para reutilizar el código de las librerías:

- **Enlace estático**:  
    El código se combina con el del programa generando un ejecutable grande.
    
- **Enlace dinámico**:  
    Las librerías están separadas del software y se solicitan al sistema operativo.

> La utilización de librerías de enlace dinámico puede causar problemas de compatibilidad y de mantenimiento.

- Las librerías también pueden incluir otros recursos como **imágenes, sonidos, objetos, etc.**

---

## Programación Orientada a Objetos (POO)

La POO busca la reutilización de código a través de características como:

- Abstracción
    
- Herencia
    
- Polimorfismo
    
- Encapsulación

---

## Servicios

Un **servicio** es una funcionalidad que un proveedor ofrece a los clientes de forma remota, y se utilize a través de las operaciones que ofrece su interfaz.

Según el **W3C**, un **servicio web** es un sistema software que permite la interacción entre máquinas a través de una red, utilizando:

- Formatos como **XML**
    
- Protocolos como **SOAP**
    
- Descripciones de servicios como **WSDL**  
    ([W3C. (2004). Web Services Glossary](https://www.w3.org/TR/ws-gloss/))

> Actualmente, se considera cualquier funcionalidad ofrecida por un servidor remoto como un servicio web, y es común encontrar **APIs** que utilizan formatos como **JSON** y adoptan el estilo **RESTful**.

---

## Enfoques De Reutilización

_(POIO Usaola, M. (2012). Desarrollo de software basado en reutilización. Universitat Oberta de Catalunya)_

- **Enfoque oportunista**:  
    Simplemente aprovecha recursos disponibles cuando son necesarios, aunque no se hubiera planificado previamente para ello.
    
- **Enfoque proactivo**:  
    Considera no solo la utilidad del desarrollo, sino también su possible aprovechamiento futuro.

---

## Components De Software

Un **componente** es una unidad de software independiente que se puede combinar con otros para crear un sistema.

Debe cumplir con un **modelo estándar** y poder desplegarse y componerse independientemente.

- Un componente:
    
    - Ofrece un conjunto de interfaces estandarizadas.
        
    - Se ve como una **caja negra** en el sistema.

### Características De Un Componente

- Estar **estandarizado**
    
- Set **independiente**
    
- **Componible**
    
- **Implementable**
    
- **Documentado**

> Un componente tiene interfaces **proporcionadas** y **requeridas** para definir los servicios ofrecidos y los servicios de otros components de los cuales depende.

---

![[Pasted image 20250617131753.png]]

---

## Frameworks De Desarrollo

La programación orientada a objetos puede resultar difícil para reutilizar objetos individuales.  
Los **frameworks de desarrollo** simplifican y guían la reutilización de components más finos.

Un **framework de desarrollo** es un conjunto integrado de artefactos de software que proporcionan una **arquitectura reutilizable** para aplicaciones relacionadas.

### Beneficios

- Desacopla partes de código específicas de la aplicación de aquellas que son comunes.
    
- Reutilización del diseño, implementaciones y validaciones.

### Problemas

- Dificultad de aprendizaje
    
- Desarrollo complejo

> Los frameworks web se basan en el patrón **Modelo-Vista-Controlador (MVC)** y suelen incluir otros frameworks específicos.

---

## Características De Frameworks Web

- Seguridad
    
- Páginas web dinámicas
    
- Soporte para bases de datos
    
- Interacción con usuarios

Ofrecen:

- Clases para autenticación de usuarios y control de acceso.
    
- Sistemas de plantillas para contenidos específicos.
    
- Conectividad flexible con diferentes bases de datos.
    
- Integración con frameworks de desarrollo _front-end_.

---

## Productos COTS (Commercial-Off-The-Shelf)

A veces, se puede reutilizar un sistema software sin modificarlo mucho.  
Los productos **COTS** se pueden adaptar a las necesidades del cliente sin cambiar el código fuente.

### Ventajas

- Rapidez de implementación
    
- Uso de software probado

### Desventajas

- Posibles cambios en procesos internos
    
- Dependencia del proveedor

---

## Categorías De COTS

### Sistema De Solución COTS

- Un único producto satisface los requisitos.
    
- Solución genérica basada en procesos estándar.
    
- El desarrollo es la configuración del sistema.
    
- El proveedor es responsible del mantenimiento.
    
- El proveedor aporta la plataforma.

### Sistemas Integrados COTS

- Se integran varios sistemas de solución.
    
- Mayor flexibilidad de adaptación a los procesos del cliente.
    
- El desarrollo es la integración del sistema.
    
- El cliente es responsible del mantenimiento.
    
- El cliente aporta la plataforma.

---

## Ejemplo De Sistema COTS

Supongamos que una empresa necesita crear un **blog empresarial**.  
Podría adoptar dos enfoques dentro de una solución COTS:

1. **Contratar un blog en WordPress.com**
    
    - Configurarlo según sus necesidades.
        
    - Seleccionar plantilla y plugins adecuados.
        
2. **Descargar WordPress.org**
    
    - Instalarlo en su propia infraestructura.
        
    - Configurar base de datos y subsistemas.

---

![[Pasted image 20250617132123.png]] 

---

## Conclusión

La **reutilización del software** busca:

- Reducir los tiempos de desarrollo del producto (y su coste).
    
- Aumentar la calidad del sistema producido.

> Es importante integrar esta práctica de manera rutinaria en nuestros procesos de desarrollo, ya que existen diferentes **niveles** en los que se puede producir esta reutilización.

---

## MicroTest

- ¿Qué tipo de librería no se describe en el texto proporcionado?
	- Librerías de enlace instantáneo.
- ¿Cuál de las siguientes es una desventaja de utilizar un sistema de repositorio?
	- Un único punto de falla al centralizar los datos en un repositorio.
- **¿Qué papel desempeñan las aplicaciones COTS (commercial-off-the-shelf)?**
	- Se adaptan a las necesidades específicas sin cambiar el código fuente.

https://queue.acm.org/detail.cfm?id=1017005
