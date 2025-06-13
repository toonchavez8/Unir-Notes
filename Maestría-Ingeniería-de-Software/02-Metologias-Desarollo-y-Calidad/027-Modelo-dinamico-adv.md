# Modelo Dinamico Avanzados

La vista eståtica del sistema determina la estructura completa a implementar.Es necesario modelar el comportamento en funcionalidades que requieran tratamlento especial. UML ofrece varios modelos dinåmicos para especificar el comportamiento del sistema.

Entre estos modelos se encuentran los diagrams de interacciön, de actividad y de estado.

Elementos de la vista dinåmica del sistema requieren atenciön especial.

La Ley de Demeter es una referencia clave para entender la comunicaciön entre objetos en un sistema

Define a qué instancias puede enviar mensajes una instancia. Puede enviar mensajes a instancias

Conectadas mediante enlaces navegables, recibidas como paråmetros, creadas localmente o a si

Misma.

Es importante tener en cuenta esta ley para una comunicaciön eficiente entre objetos en un sistema.

![[{3A709DB7-874E-4E89-A631-BD135A53B1FC}.png]]

Creaciön y destrucciön de objetos

![[{F8EF9865-CD01-4518-9560-2960D7D848D7}.png]]

La figura ilustra como se ha de modelar con UML la

Creaciön y Ia destrucciön de objetos en un diagrama

de interacciön. En este caso concreto, se muestra

Como se cancela una cuenta y se transfiere el saldo

A una nueva de Otro tipo.