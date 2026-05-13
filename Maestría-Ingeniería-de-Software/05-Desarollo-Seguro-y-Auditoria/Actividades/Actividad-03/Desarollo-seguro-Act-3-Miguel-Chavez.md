# Actividad 3

## Introducción

Librería On-Line S.A. sufrió un incidente de seguridad que derivó en la exposición de credenciales de clientes. Este hecho afectó la reputación de la organización y puso en riesgo su posición en el mercado.

Como respuesta, se plantea una auditoría técnica integral orientada a identificar vulnerabilidades, priorizar riesgos y definir salvaguardas viables desde una perspectiva técnica y económica. El propósito es fortalecer la postura de seguridad de la empresa y contribuir a la recuperación de la confianza de clientes y grupos de interés.

## Objetivos

El objetivo general de este documento es evaluar el estado de seguridad de la infraestructura TI de Librería On-Line S.A. para identificar vulnerabilidades técnicas, estimar el riesgo asociado y establecer un plan de mitigación priorizado.

En consecuencia, el plan de auditoría aborda los siguientes components clave:

- El alcance de la auditoría.
- Las metodologías de evaluación.
- La organización y los recursos necesarios.
- La evaluación de riesgos del proyecto.
- Los entregables del proyecto.

## Alcance De la Auditoría Técnica De Seguridad

El alcance de la auditoría se define por capas con el fin de asegurar una cobertura integral de la infraestructura y de los servicios críticos del sistema. Este enfoque permite evaluar de manera ordenada los controles de seguridad en cada zona de la arquitectura.

Las capas incluidas en el alcance son las siguientes:

- Capa perimetral: VPN, firewall, IDS y publicación web.
- Capa de servicios: DNS, FTP, correo interno y correo externo.
- Capa de red interna: router, switch, VLAN y red Wi-Fi.
- Capa de aplicaciones: web expuesta, intranet y aplicaciones corporativas.
- Capa de identidad y endpoint: sistema AAA y antimalware.
- Capa de datos y cumplimiento: tratamiento de datos personales y RGPD.

En la capa perimetral se realizará la revisión de reglas de firewall para verificar el cumplimiento del principio de mínimo privilegio. De forma transversal, en todas las capas se validará la configuración de seguridad de los servicios y de los controles técnicos implementados. Asimismo, en la capa perimetral se revisará la configuración y actualización de firmas del IDS.

Las tareas principales del alcance son:

- Enumeración controlada de superficies expuestas en DNS y FTP.
- Revisión de políticas de contraseñas, MFA y registros del sistema AAA.
- Pruebas de autenticación y gestión de sesión en la aplicación web.
- Verificación de la segmentación efectiva entre VLAN de usuarios y servidores.
- Revisión del cifrado de datos en tránsito y en reposo.

Con el propósito de mantener expectativas realistas y preservar la calidad de la auditoría, se establecen las siguientes limitaciones:

- No se ejecutarán pruebas destructivas que afecten la disponibilidad en producción.
- No se incluye auditoría de código fuente interno no facilitado.
- Las pruebas de ingeniería social quedan fuera de alcance.
- Las pruebas activas se realizarán únicamente en horarios autorizados.

Los tipos de pruebas contemplados en esta auditoría son:

- Pruebas de configuración segura.
- Pruebas de vulnerabilidades conocidas.
- Pruebas de autenticación y autorización.
- Pruebas de segmentación de red.
- Pruebas de cumplimiento normativo para datos personales.

Este alcance permite una evaluación técnica estructurada, facilita la trazabilidad de hallazgos y mejora la capacidad de priorizar acciones de mitigación.

## Metodologías

La metodología de auditoría se fundamenta en un enfoque combinado que integra tres marcos de referencia complementarios: NIST SP 800-115, OWASP Testing Guide e ISO/IEC 27001-27002. Esta combinación permite abordar el análisis desde una perspectiva técnica y de gestión, manteniendo coherencia entre la identificación de vulnerabilidades, la evaluación de controles y la priorización de medidas correctivas. En el contexto de Librería On-Line S.A., esta integración es especialmente pertinente porque la infraestructura incluye servicios expuestos en Internet, segmentación por capas y tratamiento de datos personales de clientes (NIST, 2008).

NIST SP 800-115 se utilizará como marco base para estructurar la ejecución de pruebas técnicas. Su aporte principal en este proyecto es ordenar el trabajo en actividades verificables de planificación, levantamiento de información, pruebas y documentación de resultados. Aplicado al caso, permitirá definir el alcance operativo por capas, establecer reglas de autorización para pruebas activas sobre DMZ, VPN y red interna, y asegurar que cada hallazgo cuente con evidencia técnica trazable. De este modo, la auditoría evita acciones aisladas y se convierte en un proceso reproducible.

OWASP Testing Guide se aplicará de forma específica a la aplicación web expuesta y a su proceso de autenticación, dado que el incidente inicial estuvo relacionado con credenciales comprometidas. Este marco permitirá evaluar, de manera ordenada, aspectos como autenticación, gestión de sesión, control de acceso y validación de entradas (OWASP Foundation, 2021).

Por su parte, ISO/IEC 27001 y 27002 funcionarán como referencia para contrastar la madurez de los controles organizativos y técnicos en dominios clave, como gestión de accesos, monitoreo, protección de activos y tratamiento seguro de la información. En conjunto, OWASP aporta profundidad en pruebas web e ISO aporta criterios de gobierno y control para sostener la remediación (International Organization for Standardization [ISO], 2022).

El ciclo metodológico del plan de análisis se coordinará en seis etapas secuenciales y dependientes:

- planificación y autorización,
- recolección de información,
- análisis técnico
- pruebas,
- correlación de hallazgos,
- evaluación de riesgo
- recomendaciones de cierre.

En la primera etapa se validan alcance entre las distinas capas de conexcion de red lan y como se accede a las redes mediante las ventanas de trabajo y restricciones; en la segunda se consolida la línea base de activos y configuraciones; en la tercera se ejecutan pruebas por capa; en la cuarta se consolidan evidencias para eliminar falsos positivos; en la quinta se prioriza el riesgo por probabilidad e impacto; y en la sexta se definen acciones de mitigación con prioridad, responsables y horizonte de implementación. Esta secuencia garantiza control del proceso, consistencia de resultados y utilidad práctica para la toma de decisiones.

## Organización Y Recursos Necesarios

La organización del trabajo de auditoría require una coordinación formal entre perfiles técnicos y de gobierno para asegurar una evaluación completa y consistente. El liderazgo operativo recae en un líder de auditoría, responsible de definir el plan de ejecución, gestionar autorizaciones, coordinar ventanas de prueba y consolidar resultados para la toma de decisiones. Dado que el incidente crítico estuvo relacionado con exposición de credenciales, este rol también debe asegurar que las actividades prioricen controles de autenticación, trazabilidad y contención de riesgo reputacional.

Con base en la arquitectura del proyecto, representada en el diagrama lógico por capas de Internet, DMZ y red interna segmentada en VLAN, se justifica la participación de especialistas de red y de seguridad web. El especialista de red centrará su análisis en la revisión de reglas entre firewall externo e interno, tránsito entre DMZ y LAN, segmentación entre VLAN de usuarios y servidores, y calidad del monitoreo IDS para detectar movimiento lateral o tráfico anómalo. En paralelo, el especialista de seguridad web evaluará autenticación, gestión de sesión y exposición de la aplicación pública, mientras que el analista de cumplimiento y protección de datos verificará la alineación de controles técnicos durante pruebas y propuestas de remediación.

Nmap se utilizará para descubrimiento de activos, puertos y servicios expuestos en perímetro, DMZ y red interna. En este proyecto, su principal valor es validar el inventario técnico real frente al inventario esperado y detectar superficies de exposición no documentadas que puedan estar relacionadas con el incidente de credenciales comprometidas. También permite contrastar la segmentación teórica del diagrama con la exposición efectiva observable.

Nessus u OpenVAS se empleará para identificar vulnerabilidades conocidas en servidores, servicios y components de infraestructura. Su uso permitirá obtener una línea base de riesgos técnicos con severidades comparables, priorizando hallazgos que afecten autenticación, configuración de servicios públicos y debilidades explotables desde la DMZ. Esta información será clave para priorizar acciones correctivas con criterios de impacto y factibilidad.

Burp Suite u OWASP ZAP se aplicará específicamente sobre la aplicación web expuesta, por set el punto más directamente relacionado con la filtración de credenciales. Estas herramientas permitirán evaluar controles de autenticación, robustez de sesión, validación de entradas y posibles fallos de lógica de negocio que faciliten abuso de cuentas o acceso no autorizado. Su aporte es crítico para transformar el análisis del incidente en mejoras concretas de seguridad aplicativa.

Wireshark se utilizará para analizar tráfico de red y verificar la protección de datos en tránsito entre components críticos. En el contexto de la empresa, permitirá comprobar si existen comunicaciones sensibles sin cifrado adecuado entre zonas de red o servicios internos, aspecto relevante considerando que el diagrama sugiere alto volumen de tráfico y riesgo de exposición. Su uso también contribuye a confirmar hipótesis técnicas durante la investigación de hallazgos.

Lynis o CIS-CAT se utilizará para evaluar el nivel de hardening de sistemas, comparando configuraciones actuales contra referencias de seguridad reconocidas. En este caso, su función es detectar configuraciones débiles en servidores y servicios críticos que puedan haber facilitado el escalamiento del incidente o incrementado la superficie de ataque. Los resultados de esta revisión aportarán recomendaciones de endurecimiento con prioridad técnica y orden de implementación.

En conjunto, esta organización de roles y herramientas permite convertir la auditoría en un proceso controlado, verificable y orientado a riesgo. La combinación entre análisis de red, pruebas de aplicación web, correlación de eventos y revisión de hardening asegura una investigación más precisa del error crítico sufrido por la empresa y una base sólida para su plan de mitigación.

## Evaluación De Riesgos Del Proyecto

La evaluación de riesgos del proyecto se construye con una matriz cualitativa de probabilidad e impacto, alineada con la arquitectura por capas observada en el diagrama lógico de red: acceso externo, perímetro, DMZ, núcleo de red y red interna segmentada en VLAN de servidores y VLAN de usuarios. Este enfoque permite priorizar de forma técnica y de negocio los riesgos más relevantes para Librería On-Line S.A., con especial atención al incidente crítico de exposición de credenciales y a sus posibles vectors de repetición.

Para la valoración se emplean tres niveles cualitativos. En probabilidad, bajo representa escenarios poco frecuentes por existencia de controles efectivos; medio representa ocurrencia possible con controles parciales; y alto representa ocurrencia esperable por exposición elevada, controles débiles o antecedentes de incidente. En impacto, bajo corresponde a afectación limitada y recuperable sin daño mayor; medio implica interrupción operativa o afectación moderada de datos; y alto implica impacto significativo en continuidad, reputación, cumplimiento normativo o confianza del cliente. Con base en esta combinación, se define el nivel de riesgo como medio, alto o crítico, considerando además los principios de protección de datos aplicables al RGPD (Parlamento Europeo y Consejo de la Unión Europea, 2016).

Matriz cualitativa por capas y activos

| ID  | Capa / activo principal                     | Riesgo identificado                                                                        | Probabilidad | Impacto | Nivel de riesgo | Tratamiento recomendado                                                                                                              | Prioridad |
| --- | ------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------ | ------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| R1  | Acceso externo y aplicación web             | Reutilización de credenciales y toma de cuentas (credential stuffing)                      | Alto         | Alto    | Crítico         | MFA obligatorio, políticas robustas de contraseña, limitación de intentos, detección de comportamiento anómalo y bloqueo adaptativo  | Inmediata |
| R2  | Perímetro (router, FW externo e interno)    | Reglas permisivas o mal segmentadas que habilitan acceso no autorizado a DMZ o red interna | Medio        | Alto    | Alto            | Revisión de reglas con mínimo privilegio, recertificación periódica de ACL, pruebas de conectividad controlada entre zonas           | Alta      |
| R3  | DMZ (Web, DNS, FTP, Mail, Reverse Proxy)    | Exposición de servicios con configuración insegura o endurecimiento insuficiente           | Alto         | Alto    | Crítico         | Hardening por servicio, cierre de puertos no necesarios, cifrado fuerte, segmentación de servicios críticos y control de publicación | Inmediata |
| R4  | DMZ y monitoreo IDS                         | Detección deficiente por firmas desactualizadas o cobertura parcial de IDS                 | Medio        | Alto    | Alto            | Actualización de firmas, tuning de reglas, casos de uso por capa y validación continua con eventos de prueba                         | Alta      |
| R5  | Núcleo de red y VLAN                        | Movimiento lateral entre VLAN de usuarios y servidores por segmentación ineficiente        | Medio        | Alto    | Alto            | Endurecimiento de segmentación, ACL por rol, control del tráfico este-oeste y alertas de lateralidad                                 | Alta      |
| R6  | VLAN servidores (DB, AD/Auth, File, Backup) | Escalamiento de privilegios y compromiso de activos críticos de backend                    | Medio        | Alto    | Alto            | Gestión de privilegios, separación de funciones, hardening de servidores y monitoreo de cuentas privilegiadas                        | Alta      |
| R7  | VLAN usuarios y Wi-Fi                       | Propagación de malware o robo de sesiones desde endpoints comprometidos                    | Medio        | Medio   | Medio           | EDR/antimalware, políticas de actualización, control de dispositivos y segmentación de acceso de red inalámbrica                     | Media     |
| R8  | Tráfico interno entre capas                 | Exposición de datos por ausencia o debilidad de cifrado en tránsito                        | Medio        | Alto    | Alto            | Cifrado TLS robusto, eliminación de protocolos inseguros y verificación de certificados en servicios internos                        | Alta      |
| R9  | Registros y SIEM                            | Trazabilidad insuficiente para detectar y responder a incidentes de forma temprana         | Medio        | Medio   | Medio           | Normalización de logs, correlación de eventos, retención adecuada y alertas priorizadas por criticidad                               | Media     |
| R10 | Datos personales de clientes (RGPD)         | Incumplimiento normativo por controles técnicos insuficientes sobre datos personales       | Medio        | Alto    | Alto            | Minimización de datos, control de acceso basado en necesidad, trazabilidad de tratamiento y revisión periódica de cumplimiento       | Alta      |

Desde una perspectiva de causa raíz, el riesgo R1 se considera el más crítico porque se vincula directamente con el incidente ya materializado y con una superficie de ataque sostenida en el tiempo. Además, su impacto no se limita al plano técnico: también afecta reputación, pérdida de clientes y exposición legal. En consecuencia, las primeras medidas de tratamiento deben concentrarse en fortalecer autenticación y sesión en la aplicación web, cerrar vectors de abuso automatizado y elevar la capacidad de monitoreo de intentos anómalos.

La segunda prioridad de intervención se concentra en la relación entre perímetro, DMZ y segmentación interna, ya que el diagrama de red refleja una arquitectura de defensa en profundidad que solo funciona si los controles entre capas son estrictos y verificables. Por ello, se recomienda ejecutar en paralelo la recertificación de reglas de firewall, el hardening de servicios expuestos y la validación de segmentación entre VLAN. Esta combinación reduce probabilidad de acceso inicial, limita el movimiento lateral y disminuye el impacto potential sobre activos críticos de servidores.

Como criterio de ejecución, la remediación debe organizarse en tres horizontes. En el corto plazo, atender riesgos críticos y altos con medidas de contención inmediata; en el mediano plazo, consolidar endurecimiento técnico y mejora de monitoreo; y en el largo plazo, institucionalizar controles mediante revisiones periódicas y métricas de eficacia. Este enfoque permite que la evaluación de riesgos no sea un ejercicio descriptivo aislado, sino una base práctica para la toma de decisiones y la mejora continua de la postura de seguridad de la empresa.

## Entregables Del Proyecto

Esta sección define los productos que se entregarían durante y al cierre del análisis de seguridad, indicando su utilidad y el tipo de evidencia que demuestran. Bajo este enfoque, los entregables no se presentan solo como una lista documental, sino como resultados verificables que conectan amenazas, vulnerabilidades, impacto y acciones de mejora. Además, se distingue entre entregables que pueden elaborarse desde esta fase de planificación y entregables que, en un entorno productivo existente, requerirían evidencia operativa adicional.

El primer entregable consolidado es la matriz de riesgos priorizados, ya desarrollada en este documento, que permite justificar técnicamente el orden de intervención por criticidad. Como complemento directo, se incorpora la matriz de activos y amenazas, cuya función es demostrar qué activos son críticos en cada capa de la red y cuáles son las amenazas más probables sobre cada uno. Este entregable aporta trazabilidad entre arquitectura, riesgo y decisión de control.

Matriz de activos y amenazas propuesta

| ID Activo | Capa de red | Activo principal | Amenaza relevante | Vulnerabilidad asociada | Impacto esperado |
|---|---|---|---|---|---|
| A1 | Acceso externo | Portal web de autenticación | Credential stuffing | Falta de MFA y controles de tasa | Compromiso de cuentas y fraude |
| A2 | Perímetro | Firewall externo e interno | Acceso no autorizado | Reglas excesivamente permisivas | Exposición de servicios internos |
| A3 | DMZ | DNS público | Enumeración y abuso de servicio | Configuración insegura | Interrupción o desvío de tráfico |
| A4 | DMZ | FTP público | Exfiltración de información | Cifrado insuficiente / mala configuración | Fuga de datos |
| A5 | DMZ | Servidor web | Explotación de vulnerabilidades web | Hardening insuficiente | Intrusión y manipulación de contenido |
| A6 | Red interna (VLAN) | Segmentación usuarios-servidores | Movimiento lateral | ACL débiles entre VLAN | Escalamiento de incidente |
| A7 | VLAN servidores | Auth/AD y base de datos | Escalamiento de privilegios | Gestión débil de privilegios | Compromiso de activos críticos |
| A8 | Datos personales | Información de clientes | Acceso indebido o uso no autorizado | Controles de acceso y trazabilidad insuficientes | Incumplimiento RGPD y sanciones |

El tercer entregable es el informe técnico de hallazgos. En esta etapa académica, se define su estructura y el contenido mínimo que deberá incluir: alcance evaluado, método aplicado, hallazgos por capa, severidad, evidencia, riesgo asociado y recomendación de tratamiento. Si la arquitectura estuviera desplegada y se ejecutaran pruebas reales, este informe incorporaría evidencias directas como resultados de escaneo con fecha, registros anonimizados, capturas de configuración, trazas de red y validación de remediaciones.

El cuarto entregable es el plan de remediación priorizado por criticidad, con medidas de corto, mediano y largo plazo. Este plan debe indicar, por cada riesgo, el control recomendado, el responsable, la urgencia y el resultado esperado. Su valor principal es traducir el diagnóstico técnico en una hoja de ruta ejecutable por la organización, evitando que la auditoría quede en conclusiones generales sin implementación.

Como entregable final de cierre, se contempla un resumen ejecutivo para dirección. Este documento sintetiza los riesgos críticos, el impacto para negocio, las decisiones prioritarias y los pasos de remediación recomendados en lenguaje claro para nivel directivo. Desde una perspectiva práctica, este resumen demuestra que el análisis no solo identifica fallas técnicas, sino que habilita decisiones de gestión para recuperar confianza, reducir exposición y fortalecer la continuidad operativa.

En síntesis, bajo el alcance de este trabajo, ya es posible entregar la matriz de riesgos, la matriz de activos y amenazas, la estructura formal del informe técnico y el plan de remediación priorizado. En un escenario con infraestructura plenamente operativa y pruebas ejecutadas, estos mismos entregables se completarían con evidencia técnica directa, incrementando su valor probatorio y su aplicabilidad inmediata.

## Conclusión

El análisis técnico realizado evidencia que la postura de seguridad de Librería On-Line S.A. requiere fortalecimiento coordinado entre controles perimetrales, servicios en DMZ, segmentación interna y gobierno de seguridad. La evaluación por capas, apoyada en marcos metodológicos reconocidos y en una matriz cualitativa de riesgos, permitió priorizar hallazgos con criterio operativo y de negocio, transformando el incidente de credenciales comprometidas en una base estructurada para la mejora continua. En conjunto, los entregables definidos demuestran trazabilidad entre activos críticos, amenazas, vulnerabilidades y acciones de tratamiento.

El riesgo de mayor criticidad es la reutilización de credenciales y la toma de cuentas en el portal web de autenticación, por su alta probabilidad de repetición y su impacto directo en reputación, confianza de clientes y cumplimiento. La solución prioritaria consiste en implantar un esquema robusto de protección de identidad, centrado en MFA obligatorio, políticas de contraseñas reforzadas, limitación inteligente de intentos, monitoreo de comportamientos anómalos y respuesta temprana desde el SIEM. Esta línea de acción, complementada con hardening de servicios expuestos y validación estricta de segmentación entre capas, reduce de forma sustancial la superficie de ataque y mejora la resiliencia global del entorno.

## Referencias

International Organization for Standardization. (2022). ISO/IEC 27001:2022 information security, cybersecurity and privacy protection—Information security management systems—Requirements. <https://www.iso.org/standard/27001>

National Institute of Standards and Technology. (2008). Technical guide to information security testing and assessment (NIST SP 800-115). <https://doi.org/10.6028/NIST.SP.800-115>

OWASP Foundation. (2021). OWASP web security testing guide (Version 4.2). <https://owasp.org/www-project-web-security-testing-guide/>

Parlamento Europeo y Consejo de la Unión Europea. (2016). Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo de 27 de abril de 2016 (Reglamento General de Protección de Datos). Diario Oficial de la Unión Europea. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
