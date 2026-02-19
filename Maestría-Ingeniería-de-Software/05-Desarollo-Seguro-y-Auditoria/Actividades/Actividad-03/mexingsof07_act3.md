# Actividad 3: Plan De Una Auditoría Técnica De Seguridad De Una Empresa

---

## Objetivos De la Actividad

- Aprender a realizar un plan de una auditoría técnica de seguridad de los sistemas TI de una organización.
- Comprender y estudiar las diferentes metodologías de evaluación de la seguridad de los sistemas TI (tecnología de la información) de una organización.

---

## Descripción De la Actividad

Con el objetivo de afianzar los conocimientos adquiridos sobre la realización de auditorías técnicas de seguridad, se pide realizar un **plan de una auditoría de seguridad** de una tienda de libros en línea llamada **Librería On-Line S.A.**

La librería ha sufrido un ciberataque que ha comprometido las credenciales de sus clientes. El incidente ha trascendido a los medios de comunicación, lo que ha producido una pérdida de cuota de mercado importante frente a sus competidores.

Con el objetivo de mantener su actual posición en el mercado de venta electrónica de libros y volver a recuperar e incluso superar la que tenía, ha contratado a la empresa **InfoSecurity** para llevar a cabo una auditoría técnica de seguridad a todos sus sistemas TI e implementar las salvaguardas que se deriven de él en función del nivel de riesgo y la disponibilidad económica.

La librería dispone de:

- Una **tienda web** en la que el cliente necesitará autenticarse con las credenciales de la cuenta de usuario.
- Verificación de credenciales contra una **base de datos en el backend** mediante una **interfaz de servicios web**.
- **Procesamiento de tarjetas de crédito subcontratado** a un procesador de terceros.
- Sitio web desplegado en Internet protegido por una **DMZ de dos capas** con acceso tanto para usuarios internos como externos.

---

## Infraestructura TI a Auditar

Se tendrá que elaborar un plan de auditoría para la siguiente infraestructura TI compuesta por:

- Accesos externos VPN.
- Zona DMZ: FW e IDS.
- Publicación del sitio web de la empresa.
- Correo externo e interno.
- Servicios públicos DNS y FTP.
- Infraestructura de red: router y switch.
- Aplicaciones internas de intranet y aplicaciones corporativas.
- Zona Wi-Fi.
- Segmentación en VLAN de la red interna: servidores y usuarios.
- Sistema AAA (autenticación, autorización y trazabilidad).
- Sistema de antimalware.
- Aplicación web de la empresa expuesta al exterior.
- Tratamiento de datos personales de clientes cumpliendo el **RGPD**.

---

## Esquema Lógico De la Infraestructura

![mexingsof07_act3](<Maestría-Ingeniería-de-Software/05-Desarollo-Seguro-y-Auditoria/Actividades/Actividad-03/Attachments/mexingsof07_act3%201.png>)

**Lectura profunda del esquema**

- Se distinguen **tres dominios principales**: `Internet/exterior`, `DMZ`, y `red interna`.
- La red interna está dividida en dos VLAN:
    - **VLAN SERVIDORES** (arriba): agrupa servicios corporativos y de backend.
    - **VLAN USUARIOS** (abajo): estaciones de trabajo, periféricos, dispositivos móviles y Wi-Fi.
- Entre Internet y red interna aparece una **DMZ de dos capas**, delimitada por dos controles tipo firewall (uno hacia fuera y otro hacia dentro), lo que sugiere arquitectura de defensa en profundidad.

**Cómo está organizado el esquema lógico**

- **Borde externo**: router de salida y conectividad hacia Internet; también se muestra acceso remoto (líneas punteadas con portátil/satélite), que sugiere VPN o enlaces externos.
- **Perímetro**: firewall externo filtra tráfico entrante/saliente antes de llegar a la DMZ.
- **DMZ (zona intermedia)**:
    - Aloja servicios expuestos o de tránsito (probables proxy, servicios web públicos, control de tráfico, inspección).
    - Incluye dispositivos de seguridad/monitorización (iconos que sugieren IDS/IPS o balanceo/inspección).
- **Firewall interno**: separa la DMZ de la LAN interna para evitar movimiento lateral directo.
- **LAN interna segmentada**:
    - VLAN de servidores para cargas críticas.
    - VLAN de usuarios con equipos finales y red inalámbrica.
    - Elementos de conectividad y control internos (switching/routing, appliances de seguridad).

**Flujos de comunicación implícitos**

- Flujo típico: `Internet -> Router -> Firewall externo -> DMZ -> Firewall interno -> VLAN internas`.
- Tráfico de usuarios internos hacia servicios públicos probablemente sale por el mismo perímetro, con controles intermedios.
- Accesos remotos entran por borde y deben atravesar controles antes de tocar recursos internos.

**Qué evidencia el diseño**

- **Fortalezas**:
    - Segmentación por zonas de confianza.
    - Double barrera perimetral alrededor de la DMZ.
    - Separación lógica entre usuarios y servidores.
- **Debilidades señaladas en la propia imagen**:
    - Texto “**No tráfico cifrado, gran volumen**” sugiere riesgo de confidencialidad y/o inspección insuficiente en red interna.
    - Texto “**Ataques exteriores, identificar problemas de configuración**” indica que el principal vector esperado es externo y muy dependiente de hardening/configuración.
    - Presencia de servicios históricamente sensibles (por ejemplo, FTP/DNS/correo en este tipo de diagrams) amplía superficie de ataque si no están reforzados.

**Interpretación de seguridad del esquema lógico**

- Es una arquitectura clásica de empresa con **modelo por capas** y **zonas de confianza decreciente**.
- El control real no depende solo del dibujo, sino de políticas concretas:
    - reglas de firewall entre zonas,
    - cifrado del tráfico interno y remoto,
    - segmentación efectiva entre VLAN,
    - monitoreo de eventos en DMZ y accesos remotos.
- En términos de auditoría, el diagrama sugiere revisar primero:
    1. perímetro y DMZ,
    2. acceso remoto,
    3. segmentación lateral entre VLAN,
    4. cifrado y trazabilidad en red interna.

---

## Pautas De Elaboración

El contenido típico de un plan de auditoría técnica de seguridad suele container los siguientes puntos:

1. Introducción.
2. Objetivos de la auditoría.
3. Alcance de la auditoría técnica de seguridad.
4. Metodologías.
5. Organización y recursos necesarios.
6. Procedimientos de comunicación con los responsables de proyecto.
7. Planificación.
8. Presupuesto.
9. Evaluación de riesgos del proyecto.
10. Entregables de proyecto.
11. Anexo I. Acuerdo de autorización.
12. Anexo II. Acuerdo de confidencialidad (opcional).

---

## Apartados Solicitados Al Estudiante

Se debe desarrollar únicamente lo siguiente:

1. **Introducción.**
2. **Objetivos de la auditoría.**
3. **Alcance de la auditoría técnica de seguridad.**
   - Detalle de las tareas a realizar.
   - Identificar las limitaciones aplicables.
   - Tipos de pruebas a realizar.
4. **Metodologías.**
5. **Organización y recursos necesarios**  
   - Solo incluir las herramientas por utilizar.
6. **Evaluación de riesgos del proyecto.**
7. **Entregables del proyecto.**

---
