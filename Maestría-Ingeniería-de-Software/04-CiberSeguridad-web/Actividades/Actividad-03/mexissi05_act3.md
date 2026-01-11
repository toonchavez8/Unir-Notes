Actividad grupal: Test de penetración a la aplicación web BADSTORE

**Objetivos de la actividad:**

- Aprender a encontrar vulnerabilidades de seguridad en una aplicación web.
- Explotar vulnerabilidades de seguridad en una aplicación web.
- Aprender a utilizar una herramienta de análisis dinámico DAST en aplicaciones web a través de un procedimiento por fases.

**Pautas de elaboración de la actividad**.

Realización de un test de penetración a la aplicación web Badstore.

Descarga:

- ORACLE Virtualbox desde [https://www.virtualbox.org/](https://www.virtualbox.org/) e instala ZAP desde: [https://owasp.org/www-project-zap/](https://owasp.org/www-project-zap/)
- La máquina virtual con la aplicación BADSTORE, desde: [https://www.dropbox.com/sh/7ewzuosszqslkok/AADL6CSiXkoFPWdmfnwjHDLYa?dl=0](https://www.dropbox.com/sh/7ewzuosszqslkok/AADL6CSiXkoFPWdmfnwjHDLYa?dl=0)
- Importa el servicio virtualizado badstore.ova desde ORACLE virtualbox.
- En configuración - almacenamiento, asocia la imagen BadStore-212.iso en el controlador IDE (cdrom) y configura la máquina virtual para que arranque primero desde el cdrom.

![mexissi05_act3](Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/mexissi05_act3.png)

Figura 1. Ejemplo 1 configuración. Fuente: elaboración propia.

- Crea una red virtualbox HOST ONLY en VIRTUALBOX (Archivo- preferencias- red- redes solo anfitrión- añadir una red- habilitar DCHP) según versión y configurar de la siguiente forma:

![mexissi05_act3](<Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/mexissi05_act3%201.png>)

Figura 2. Ejemplo 2 configuración. Fuente: elaboración propia.

- Configura el adaptador de red solo-anfitrión con las siguientes direcciones:

![mexissi05_act3](<Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/mexissi05_act3%202.png>)

Figura 3. Ejemplo 3 configuración. Fuente: elaboración propia.

![mexissi05_act3](<Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/mexissi05_act3%203.png>)

Figura 4. Ejemplo 4 configuración. Fuente: elaboración propia.

- Comprobar en la configuración de la máquina virtual Badstore: red que el adaptador 1 está habilitado y conectado a adaptador solo anfitrión.

![mexissi05_act3](<Maestría-Ingeniería-de-Software/04-CiberSeguridad-web/Actividades/Actividad-03/Attachments/mexissi05_act3%204.png>)

Figura 5. Ejemplo 5 configuración. Fuente: elaboración propia.

- Arranca la máquina virtual y ejecuta **ifconfig -a** para comprobar la dirección IP asociada al dispositivo eth0.
- Incluir en el fichero host de la máquina anfitriona la entrada correspondiente a la dirección IP de ETH0. Por ejemplo, si la dirección IP obtenida por DHCP para el dispositivo ETH0 es 192.168.56.110:

192.168.56.110 [www.badstore.net](http://www.badstore.net)

- Realiza el test de penetración de la aplicación Badstore con el Scanner de vulnerabilidades ZAP atacando al nombre asociado a la dirección del dispositivo eth0 obtenida en el paso anterior: [http://www.badstore.net/cgi-bin/badstore.cgi](http://www.badstore.net/cgi-bin/badstore.cgi)

- Audita manualmente al menos tres vulnerabilidades para comprobar la veracidad de las alertas por parte de ZAP.
- Se podrá disponer de un procedimiento de test de penetración con ZAP disponible en vuestra carpeta personal.

**Extensión**

Debes confeccionar una memoria en formato pdf, explicando el proceso y los resultados obtenidos adjuntando el informe de la herramienta ZAP en formato html. 15 páginas en un documento de Word, tipo de letra Georgia, tamaño 11 e interlineado 1,5.

- **Rúbrica**:

|   |   |   |   |
|---|---|---|---|
|Actividad 2|Descripción|Puntuación máxima<br><br>(puntos)|Peso<br><br>%|
|Criterio 1|Como se ha llevado a cabo el procedimiento de test|3|30%|
|Criterio 2|Resultados de vulnerabilidades encontradas|3|30%|
|Criterio 3|Auditoría de las vulnerabilidades encontradas|3|30%|
|Criterio 4|Calidad de la memoria|1|10%|
|||**10**|**100 %**|