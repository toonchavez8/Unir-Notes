# Diseño Basado En Components

El **diseño basado en components** favorece la **reutilización de objetos y software**.  
Permite crear nuevos elementos a partir de piezas ya existentes, lo que impulsa la eficiencia y la escalabilidad del desarrollo.

---

## Características De Los Components

- Ofrecen un **alto nivel de abstracción**
- Deben set desarrollados de manera **genérica**
- Se prioriza:
  - **Alta cohesión interna**
  - **Bajo acoplamiento externo**
- Un componente se define como una **unidad de despliegue independiente**
- Pueden set utilizados por cualquier organización **sin necesidad de conocimientos previous**
- No tienen estado persistente por sí mismos (aunque sus objetos pueden tenerlo opcionalmente)
- Implementan una series de **interfaces** y **utilizan otras**
- Encapsulan elementos como **clases** y otros **módulos de código**

---

## Definiciones Clásicas

> **Stevens y Pooley (2000)** definen un componente como:  
> *“Un elemento reutilizable y reemplazable con una interfaz bien definida, abstracción cohesiva y bajo acoplamiento.”*  
> — *Using UML. Software engineering with objects and components. Pearson Addison-Wesley*

> **Booch, Rumbaugh y Jacobson (2006)** lo describen como:  
> *“Una parte reemplazable que implementa un conjunto de interfaces.”*  
> — *El lenguaje unificado de modelado. UML 2.0 (2.ª ed.). Pearson Addison-Wesley*

---

## Interfaces Y Dependencias

- Las **interfaces** especifican un servicio **proporcionado** o **solicitado** por un componente.
- Los sistemas de software utilizan components que **pueden depender de otros**.
- Estas **dependencias** se representan en UML mediante **relaciones de dependencia**.
- Para lograr el **bajo acoplamiento**, un componente **no depende directamente de otro**, sino de una o varias de sus **interfaces**.

---

## Tipos De Components Soportados Por UML

UML da soporte tanto a:

- **Components lógicos**  
  Ej: components de negocio, de procesos, etc.

- **Components físicos**  
  Ej: EJB, CORBA, COM+, JavaBeans, .NET, etc.

Referencia:  

> OMG (2011). *OMG Unified Modeling Language (OMG UML), Superstructure. Version 2.4.1.*  
> [http://www.omg.org/spec/UML/2.4.1/Superstructure/PDF](http://www.omg.org/spec/UML/2.4.1/Superstructure/PDF)

---

## Diagrams De Components UML

A continuación, se presentan ejemplos visuals de **diagrams de components** modelados con UML:

![[Pasted image 20250617094444.png]]  
![[Pasted image 20250617094451.png]]  

---

## Diagrams De Components En Mermaid

Aquí tienes un ejemplo de cómo representar diagrams de components usando **Mermaid**:

```mermaid
graph TD
  subgraph Cliente
    A[Aplicación Cliente]
  end

  subgraph Servidor
    B[Componente Web] -->|Usa| C[Componente Servicio]
    C -->|Usa| D[Componente DAO]
  end

  A -->|Petición HTTP| B
  ```

```mermaid
graph TD
  ComponentA["ComponentA"]
  InterfaceX[<<interface>> InterfaceX]
  ComponentB["ComponentB"]
  InterfaceY[<<interface>> InterfaceY]

  ComponentA -->|realiza| InterfaceX
  ComponentB -->|usa| InterfaceX
  ComponentB -->|realiza| InterfaceY

```

---

## MicroTest

- ¿Qué características definen a un componente según Szyperski?
	- Un componente podría set utilizado por cualquier organización sin necesidad de ningún conocimiento previo.
- ¿Qué elemento no es mencionado en las características de un componente, según Stevens y Pooley?
	- Interacción directa con otros components sin interfaces.
- ¿Cómo se denota en UML la relación de uso de unos components por otros en los sistemas de software?
	- A través de una relación de dependencia.

## ReadMore

https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/diagrama-de-componentes/

