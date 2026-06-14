

Due date: **Monday, 13 July 2026, 11:59 PM** 

Despliegue de un aplicativo en alta disponibilidad en nube pública con redes públicas y privadas (grupal)


Objetivos

El objetivo de esta actividad es desarrollar los conocimientos obtenidos a través de los temas dedicados a nube pública.

Pautas de elaboración

Vamos a crear una arquitectura de un aplicativo en alta disponibilidad en nube pública. El aplicativo puede ser un Wordpress u otro aplicativo que el estudiante conozca o un aplicativo trabajado en otras asignaturas del máster.

Para ello, deberemos desplegar nuestro aplicativo en nube pública con ayuda de la cuenta de AWS Academy.

Los requisitos serán los siguientes:

- Creación de una red (VPC) con direccionamiento privado con seis subredes, con salida a Internet, tanto las redes privadas como públicas.
- Creación de un frontend en red privada expuesto a Internet a través de un balanceador.
- Creación de un grupo de autoescalado para el frontend del aplicativo si se despliega en EC2. (Opcional: se puede sustituir las EC2 por un almacenamiento S3 para el frontend).
- Creación de una base de datos en alta disponibilidad en subredes privadas separadas del frontend.

NOTA:

La arquitectura de cada estudiante puede ser diferente, pudiendo usar arquitecturas de dos capas o tres capas. En este caso solo la parte de presentación estará en subred pública y el resto en subredes privadas.

Extensión y formato

La entrega consistirá en un informe en un archivo PDF con un máximo de veinte páginas, para dejar constancia de todo lo realizado. Formato del PDF: fuente Calibri, tamaño 11 e interlineado 1,5 líneas).

Rúbrica

Ver Excel adjunto.