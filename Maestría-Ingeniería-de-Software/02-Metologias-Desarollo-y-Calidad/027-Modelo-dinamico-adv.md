# Modelo Dinámico Avanzado

La **vista estática** del sistema determina la estructura completa a implementar.  
Sin embargo, es necesario modelar también el **comportamiento**, especialmente en funcionalidades que requieran tratamiento especial.  

UML ofrece varios **modelos dinámicos** para especificar el comportamiento del sistema:

- Diagrams de interacción  
- Diagrams de actividad  
- Diagrams de estado  

Elementos de la **vista dinámica** del sistema requieren atención especial.

---

## Ley De Demeter

La **Ley de Demeter** es una referencia clave para entender la comunicación entre objetos en un sistema.  

Define a qué instancias puede enviar mensajes una instancia. Una instancia puede enviar mensajes a:

- Instancias **conectadas mediante enlaces navegables**  
- Instancias **recibidas como parámetros**  
- Instancias **creadas localmente**  
- A **sí misma**

> Es importante tener en cuenta esta ley para lograr una comunicación eficiente entre objetos.

![[{3A709DB7-874E-4E89-A631-BD135A53B1FC}.png]]

### Ejemplo Mermaid

```mermaid
flowchart TD
	id[Ana:Cliente] --(1:emitirTransferencia)-->id1[banco:Banco]
	id1 --sacarDinero(cantidad)-->id2[origin:Cuenta]
	id2 --esdisponible(cantidad)-->id2
	id1 --meterDienro(cantidad)--> id3[destino:Cuenta]	
````

---

## Creación Y Destrucción De Objetos

La figura ilustra cómo se ha de modelar con UML la **creación** y la **destrucción de objetos** en un diagrama de interacción.

En este caso concreto, se muestra cómo se **cancela una cuenta** y se **transfiere el saldo** a una nueva cuenta de otro tipo.

![[{F8EF9865-CD01-4518-9560-2960D7D848D7}.png]]

---

## Polimorfismo De Mensajes

**Los objetos se comunican entre sí mediante el envío de mensajes.**  
El envío de mensajes es más expresivo cuando se utilize el **polimorfismo**.

Características clave:

- Varios objetos pueden **interpretar un mensaje de manera distinta**, aunque compartan la misma interfaz.
    
- Facilita la **evolución del sistema** al permitir añadir nuevas clases sin necesidad de ramificaciones múltiples.
    
- La **ramificación** en el polimorfismo es **implícita**, interpretando el mensaje según la clase del objeto.

![[Pasted image 20250613120926.png]]

---

## Microtest

- La ley de Demeter sirve de referencia clave a la hora de entender cómo se realiza la comunicación vía mensajes entre los objetos que constituyen el sistema, por lo cual:
	- Define a qué instancias puede enviar mensajes una instancia determinada de una clase.
- Un lenguaje empleado para modelar la creación y destrucción de objetos es:
	- UML
- ¿Cuál es la ventaja del uso correcto del polimorfismo de mensajes?
	- El uso correcto de la propiedad de polimorfismo va a facilitar la evolución del sistema en el caso de que se tenga necesidad de añadir nuevas clases a su estructura, sin que haya necesidad de hacer uso de instrucciones de ramificación múltiple, ya que la ramificación es implícita, es decir, interpretará el mensaje según sea la clase del objeto.