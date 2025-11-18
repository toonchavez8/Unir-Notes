# Análisis Y Gestión De Riesgos En Una Instalación De TI: Caso OCTAVE-S En Servicio Público


## Resumen

El presente documento narra el proceso completo de análisis de riesgos aplicado a un servicio de tramitación electrónica de una unidad administrativa, utilizando la metodología **OCTAVE-S** (Operationally Critical Threat, Asset, and Vulnerability Evaluation – Simplified). Se identificaron los activos críticos del sistema (información, hardware, software, infraestructura), sus requisitos de seguridad (confidencialidad, integridad, disponibilidad, cumplimiento), así como las amenazas y vulnerabilidades asociadas. Cada escenario de riesgo fue evaluado cualitativa y cuantitativamente, asignando probabilidades e impactos. A continuación se definieron estrategias de tratamiento (evitar, reducir, transferir o aceptar) y controles técnicos/organizativos (por ejemplo, MFA, cifrado, respaldos, detección de intrusos) para mitigar los riesgos más altos. Finalmente, se estimó el riesgo residual tras aplicar dichas salvaguardas y se establecieron responsables y cronogramas de revisión. El resultado es un análisis de riesgos exhaustivo y alineado con buenas prácticas[sei.cmu.edu](https://www.sei.cmu.edu/library/octave-s-implementation-guide-version-1/#:~:text=The%20Operationally%20Critical%20Threat%2C%20Asset%2C,mitigation%20plans%20based%20on%20the)[elmayorportaldegerencia.com](https://www.elmayorportaldegerencia.com/Publicaciones/%5BPD%5D%20Publicaciones%20-%20Octave%20S.pdf#:~:text=metodolog%C3%ADa%20que%20propone%20OCTAVE,activos%20organizaciones%2C%20evaluar%20practicas%20organizacionales), que puede servir de base para planes de seguridad y auditorías futuras.

## Introducción a la Metodología De Análisis De Riesgos

La **gestión de riesgos** en ciberseguridad es el proceso de identificar y manejar la exposición de una organización a amenazas y vulnerabilidades[continuumgrc.com](https://continuumgrc.com/es/what-are-risk-assessment-methodologies/#:~:text=La%20gesti%C3%B3n%20de%20riesgos%20de,en%20caso%20de%20que%20ocurran). Existen múltiples marcos y estándares para abordar esta tarea (por ejemplo, ISO/IEC 31000 e ISO/IEC 27005[iso.org](https://www.iso.org/standard/65694.html#:~:text=ISO%2031000%20is%20an%20international,communicating%20risks%20across%20an%20organization)[dataguard.com](https://www.dataguard.com/blog/iso-27001-risk-management-strategies#:~:text=assessment%20process%2C%20a%20risk%20treatment,risk%20retention%20and%20risk%20acceptance)), pero en este caso se eligió la metodología **OCTAVE-S**, dada su adecuación a organizaciones pequeñas y flexibles. OCTAVE-S es una variante de OCTAVE diseñada para equipos reducidos, en la que un pequeño grupo multidisciplinar de la propia entidad assume la responsabilidad de la evaluación y del diseño de la estrategia de seguridad[sei.cmu.edu](https://www.sei.cmu.edu/library/octave-s-implementation-guide-version-1/#:~:text=The%20Operationally%20Critical%20Threat%2C%20Asset%2C,mitigation%20plans%20based%20on%20the)[lazarusalliance.com](https://lazarusalliance.com/es/what-is-octave-and-octave-allegro/#more-139143#:~:text=OCTAVA,de%20tecnolog%C3%ADa%20de%20la%20informaci%C3%B3n). Según Alberts _et al._ (2005), OCTAVE-S lidera un proceso de autoevaluación que genera estrategias de protección basadas en los riesgos operativos particulares de la organización[sei.cmu.edu](https://www.sei.cmu.edu/library/octave-s-implementation-guide-version-1/#:~:text=The%20Operationally%20Critical%20Threat%2C%20Asset%2C,mitigation%20plans%20based%20on%20the). En la práctica, el proceso se estructura en fases secuenciales de identificación (activos, amenazas, vulnerabilidades), evaluación de riesgos y planificación de mitigaciones[elmayorportaldegerencia.com](https://www.elmayorportaldegerencia.com/Publicaciones/%5BPD%5D%20Publicaciones%20-%20Octave%20S.pdf#:~:text=metodolog%C3%ADa%20que%20propone%20OCTAVE,activos%20organizaciones%2C%20evaluar%20practicas%20organizacionales).

Para el caso estudiado, el alcance definido incluyó el servicio de tramitación electrónica (presencial y remota) y la información manejada (expedientes administrativos), junto con el equipamiento de cómputo y redes asociadas. Se decidió no evaluar en profundidad aún algunos elementos subsidiarios (por ejemplo, credenciales de usuarios, zonas de trabajo, servicios externos opacos), reservándolos para futuras fases. El análisis se condujo con la participación de un comité de seguimiento y un equipo técnico (ingeniero de sistemas) apoyado por consultores externos, garantizando así el conocimiento organizacional requerido por OCTAVE-S. A lo largo del proceso, se documentaron todos los pasos conforme a la metodología, asegurando trazabilidad y replicabilidad. Como observación, algunos autores han señalado que OCTAVE-S se divide en tres fases principales (perfilamiento de amenazas, revisión de infraestructura e identificación de riesgos/marcos de mitigación)[elmayorportaldegerencia.com](https://www.elmayorportaldegerencia.com/Publicaciones/%5BPD%5D%20Publicaciones%20-%20Octave%20S.pdf#:~:text=metodolog%C3%ADa%20que%20propone%20OCTAVE,activos%20organizaciones%2C%20evaluar%20practicas%20organizacionales), aunque en la ejecución práctica se complementó con pasos intermedios para adaptar su estructura a la guía del proyecto.

## Fase 1: Identificación De Activos Críticos

El primer paso consistió en **identificar los activos esenciales** del sistema de tramitación. Esto incluyó components tecnológicos (hardware y software), datos e información, servicios críticos, usuarios y dependencias externas. Por ejemplo, entre los activos se consideraron el servidor principal de tramitación, los PCs de oficina, la base de datos de expedientes, la aplicación de gestión, el sistema de correo electrónico, la infraestructura de red (cortafuegos, conexión a Internet), y la sala de equipos (centro de cómputo). Estos activos fueron evaluados en términos de confidencialidad, integridad y disponibilidad según la triada CIA, así como su impacto potential ante una falla. A continuación se muestra la tabla de activos clave elaborada (cada activo fue catalogado por tipo, propietario, ubicación y valorizado en C/I/A y nivel de impacto):

| ID Activo | Nombre del Activo                 | Tipo de Activo  | Propietario           | Ubicación        | Confidencialidad | Integridad | Disponibilidad | Impacto | Notas                                                            |
| --------- | --------------------------------- | --------------- | --------------------- | ---------------- | ---------------- | ---------- | -------------- | ------- | ---------------------------------------------------------------- |
| 1         | PCs de oficina (10 unidades)      | Hardware        | Unidad de Tramitación | Oficinas (LAN)   | Media            | Media      | Media          | Media   | Sin discos extraíbles; reinstalación periódica.                  |
| 2         | Servidor general (serv. central)  | Hardware        | Unidad de Sistemas    | Sala de Equipos  | Alta             | Alta       | Alta           | Alta    | Almacena app, BD y correo; no hay redundancia local.             |
| 3         | SW gestión de expedientes         | Software        | Unidad de Tramitación | Servidor Local   | Alta             | Alta       | Alta           | Alta    | Sistema propio de tramitación; soporte interno limitado.         |
| 4         | Base de datos de expedientes      | Base de datos   | Unidad de Tramitación | Servidor Local   | Alta             | Alta       | Alta           | Alta    | Contiene datos personales; se envía backup al archivo central.   |
| 5         | Sistema de correo electrónico     | Servicio SW     | Unidad de Tramitación | Servidor Local   | Media            | Media      | Media          | Media   | Mensajería interna; no hay filtros antispam robustos.            |
| 6         | Conexión Internet (ADSL/RDSI)     | Servicio        | Unidad de Tramitación | Externa (ISP)    | Baja             | Baja       | Alta           | Alta    | Soporta web/VPN; backup RDSI activado ante caídas.               |
| 7         | Cortafuegos perimetral            | Hardware/SW     | Unidad de Sistemas    | Sala de Equipos  | Media            | Alta       | Alta           | Alta    | Controla acceso Internet; único dispositivo de seguridad de red. |
| 8         | Sala de equipos (centro de datos) | Infraestructura | Unidad de Sistemas    | Edificio, piso 4 | Media            | Media      | Alta           | Alta    | Cerrada con llave, detector de incendios; lejos de tubería.      |

Cada activo fue calificado de **según sus requerimientos** de seguridad: por ejemplo, el servidor de tramitación (Activo 2) y la base de datos (Activo 4) obtuvieron valoraciones altas en C, I y A, dado que contienen datos sensibles y soportan el funcionamiento operativo. En contraste, los PCs de usuario (Activo 1) se valoraron como “Media” en CIA, pues sólo almacenan expedientes temporales y son fáciles de reinstalar. Este análisis de activos críticos provee la base para las siguientes fases: define qué recursos proteger y cuáles son sus criterios de confidencialidad, integridad y disponibilidad[elmayorportaldegerencia.com](https://www.elmayorportaldegerencia.com/Publicaciones/%5BPD%5D%20Publicaciones%20-%20Octave%20S.pdf#:~:text=metodolog%C3%ADa%20que%20propone%20OCTAVE,activos%20organizaciones%2C%20evaluar%20practicas%20organizacionales).

## Fase 2: Identificación De Amenazas Y Vulnerabilidades

### 3.1 Escenarios De Amenaza

Partiendo de los activos identificados, se generaron **escenarios de amenaza realistas** acorde al contexto operacional. Entre los escenarios considerados destacaron:

- **Ataques de ransomware:** cifrado malicioso de expedientes o sistemas críticos.
    
- **Acceso no autorizado a expedientes:** intrusiones internas o externas a la base de datos.
    
- **Interrupción del servicio:** fallos de conexión a Internet o problemas en la red local.
    
- **Pérdida o fuga de información vía APIs externas:** por ejemplo, exposición de datos durante interacciones con el archivo central.
    
- **Manipulación o alteración de datos de tramitaciones:** cambios maliciosos en expedientes abiertos o cerrados.
    
- **Errores de configuración en servidores o bases de datos:** desbordamientos, parches faltantes o servicios inseguros.
    
- **Saturación por picos de carga o ataques DDoS:** sobrecarga del enlace ADSL o del servidor web.

Para cada escenario se registró el activo afectado, la amenaza concreta y se asignó una probabilidad e impacto iniciales. Estos insumos poblaron la columna “Amenaza” y permitieron priorizar posteriores análisis. Cabe notar que las metodologías basadas en activos (como OCTAVE) enfatizan la comprensión de escenarios de riesgo contextuales[elmayorportaldegerencia.com](https://www.elmayorportaldegerencia.com/Publicaciones/%5BPD%5D%20Publicaciones%20-%20Octave%20S.pdf#:~:text=metodolog%C3%ADa%20que%20propone%20OCTAVE,activos%20organizaciones%2C%20evaluar%20practicas%20organizacionales)[lazarusalliance.com](https://lazarusalliance.com/es/what-is-octave-and-octave-allegro/#more-139143#:~:text=OCTAVA,de%20tecnolog%C3%ADa%20de%20la%20informaci%C3%B3n).

### 3.2 Vulnerabilidades Asociadas

A continuación se identificaron **vulnerabilidades** que podrían facilitar cada amenaza. Se examinaron debilidades técnicas, procedimientos y factores humanos. Por ejemplo:

- **Ausencia de MFA o controles de identidad débiles:** incrementa el riesgo de accesos no autorizados.
    
- **Configuraciones inseguras o servicios obsoletos:** p. ej., servidores sin parches o puertos abiertos innecesariamente.
    
- **Dependencia de un único proveedor/servicio:** si el enlace principal falla y el respaldo no se activa, cae el servicio remoto.
    
- **Falta de monitoreo centralizado:** dificulta la detección de intrusiones o anomalías de red.
    
- **Políticas de seguridad internas insuficientes:** ausencia de normas claras para gestión de contraseñas, respaldo o clasificación de información.
    
- **Copias de seguridad no probadas:** riesgo de pérdida de datos críticos si los backups no son recuperables.

Cada vulnerabilidad se vinculó a los escenarios correspondientes, completando así la columna “Vulnerabilidad” en la matriz. Este enfoque concordó con la fase de infraestructura de OCTAVE-S, donde se examina la relación entre activos y fallas técnicas[elmayorportaldegerencia.com](https://www.elmayorportaldegerencia.com/Publicaciones/%5BPD%5D%20Publicaciones%20-%20Octave%20S.pdf#:~:text=metodolog%C3%ADa%20que%20propone%20OCTAVE,activos%20organizaciones%2C%20evaluar%20practicas%20organizacionales).

### 3.3 Evaluación Del Riesgo

Con las amenazas y vulnerabilidades definidas, se estimó el **nivel de riesgo inicial** para cada escenario combinando la probabilidad de ocurrencia con el impacto sobre los activos. Esto se tradujo en un puntaje (score) o uso de matrices de calor, así como en una clasificación cualitativa (bajo, medio, alto, crítico). Un ejemplo práctico se aprecia en la siguiente tabla resumen (parte de la “Matriz de Análisis de Riesgos”):

| ID Escenario | Activo Relacionado       | Amenaza                                 | Vulnerabilidad                                      | Probabilidad | Impacto | Riesgo Score | Riesgo Cualitativo | Controles Existentes                          | Controles Recomendados                                  | Notas                                                    |
| ------------ | ------------------------ | --------------------------------------- | --------------------------------------------------- | ------------ | ------- | ------------ | ------------------ | --------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------- |
| 1            | PCs de oficina (Act. 1)  | Infección por malware                   | No hay antivirus corporativo ni políticas claras.   | Media        | Medio   | 6            | Medio              | Cortafuegos perimetral; sin antivirus en PCs. | Instalar antivirus endpoint; bloqueo USB/email.         | PCs son reinstalados periódicamente sin respaldo local.  |
| 2            | Servidor general (Act.2) | Fallo de disco duro                     | Servidor único sin respaldo local ni redundancia.   | Media        | Alto    | 6            | Alto               | Se envían expedientes cerrados al archivo.    | Implementar backups regulares locales; replicación.     | Aloja funciones críticas: web, BD, correo.               |
| 3            | Cortafuegos (Act.7)      | Configuración incorrecta/ataque externo | Firewall único sin IDS/IPS ni monitoreo activo.     | Baja         | Alto    | 5            | Medio              | Reglas básicas de tráfico (web y correo).     | Auditorías de configuración periódicas; añadir IDS/IPS. | Puntos de acceso limitados; falta detección de intrusos. |
| 4            | SW gestión (Act.3)       | Vulnerabilidad de software              | App heredada sin parches ni pruebas de seguridad.   | Media        | Alto    | 6            | Alto               | Acceso autenticado actual del software.       | Análisis y parcheo continuo; pruebas de seguridad.      | Desarrollo interno con poca documentación.               |
| 5            | Base de datos (Act.4)    | Acceso no autorizado/fuga de datos      | Contraseñas débiles; privilegios demasiado amplios. | Media        | Alto    | 6            | Alto               | Autenticación tradicional por contraseña.     | Cifrado de datos; reforzar controles de acceso; MFA.    | Contiene información personal sensible.                  |
| 6            | Correo (Act.5)           | Phishing/Suplantación                   | No hay filtro antispam; usuarios sin capacitación.  | Alta         | Medio   | 6            | Medio              | Servidor y cliente de correo actualizados.    | Implementar filtro antispam; formación en seguridad.    | Se usa para notificaciones externas.                     |
| 7            | Sala de equipos (Act.8)  | Incendio u otro desastre físico         | Detector de humo sin extinción automática ni gas.   | Baja         | Alto    | 5            | Medio              | Detector de incendios activo; sala con llave. | Instalar extintores automáticos; simulacros/emergencia. | Sala separada 50 m de tubería; acceso restringido.       |

En cada escenario, el nivel de riesgo inicial («Score» y categorización cualitativa) orientó la priorización. Por ejemplo, la infección de malware (Escenario 1) resultó con riesgo medio, mientras que el fallo de disco del servidor (Escenario 2) fue crítico. En esta fase se registraron también los **controles existentes** (por ejemplo, firewall perimetral, backups al archivo) y los **controles recomendados** iniciales (antivirus, redundancia de datos, auditorías) para cada caso. Este paso concluyó la elaboración de la Matriz de Análisis de Riesgos inicial.

## Fase 3: Selección De Mitigaciones Y Controles

### 4.1 Estrategias De Mitigación

Para cada riesgo identificado se definió una **estrategia de tratamiento** acorde al riesgo residual acceptable y costos asociados. Siguiendo prácticas como ISO 27001[dataguard.com](https://www.dataguard.com/blog/iso-27001-risk-management-strategies#:~:text=assessment%20process%2C%20a%20risk%20treatment,risk%20retention%20and%20risk%20acceptance), se consideraron cuatro opciones principales:

- **Evitar:** eliminar la causa del riesgo (por ejemplo, desactivar una funcionalidad no esencial vulnerable).
    
- **Reducir:** implementar controles para disminuir probabilidad o impacto (p.ej. reforzar autenticación, cifrado, copias de seguridad).
    
- **Transferir:** asignar el riesgo a terceros (por ejemplo, contratar seguro o delegar servicio a un proveedor con garantía de servicio).
    
- **Aceptar:** asumir el riesgo cuando sea leve o el costo de mitigarlo desproporcionado.

Estas opciones se anotaron en la matriz como “Estrategia de Mitigación” para cada escenario. Por ejemplo, ante riesgos altos se priorizó reducir (mejorar controles) o evitar (modificar procesos), mientras que riesgos menores se podrían aceptar o monitorizar pasivamente. Esta categorización se basa en guías de buenas prácticas de gestión de riesgos[dataguard.com](https://www.dataguard.com/blog/iso-27001-risk-management-strategies#:~:text=assessment%20process%2C%20a%20risk%20treatment,risk%20retention%20and%20risk%20acceptance).

### 4.2 Determinación De Controles

Con las estrategias definidas, se enlistaron los **controles técnicos y organizativos** necesarios. Se emplearon referencias de marcos de seguridad (ISO/IEC 27001, OWASP, NIST CSF, etc.) para sugerir prácticas adecuadas. Entre los controles recomendados destacan:

- **Autenticación multifactor (MFA):** fortalece el acceso a sistemas críticos.
    
- **Hardening de servidores:** deshabilitar servicios innecesarios, aplicar parches y configuraciones seguras.
    
- **Implementación de un SIEM o sistema de monitoreo centralizado:** para detectar incidentes en tiempo real.
    
- **Cifrado de datos en tránsito y reposo:** proteger información confidencial en la base de datos y comunicaciones.
    
- **Backups periódicos probados:** realizar copias de seguridad locales y en ubicaciones remotas y verificar su restauración.
    
- **Políticas de gestión de identidades (IAM):** definir perfiles mínimos y revisiones periódicas de permisos.
    
- **Control de red Zero Trust:** segmentación, VPN y reglas estrictas de acceso interno.
    
- **Validación y sanitización de datos en APIs:** proteger integraciones con el archivo central.

Algunos controles ya existían (por ejemplo, firewall perimetral, autenticación básica), otros se propusieron. Estos controles se registraron en la matriz como “Controles Recomendados” y también se marcó su estado de aplicación en la etapa final.

## Fase 4: Evaluación Del Riesgo Residual Y Plan De Acción

### 5.1 Riesgo Residual

Tras planificar la aplicación de los controles recomendados, se estimó el **nivel de riesgo residual** para cada escenario, recalculando la probabilidad e impacto asumibles con las salvaguardas propuestas. Se llenó la columna “Nivel de Riesgo Residual” en la matriz final. En la mayoría de los casos, los riesgos inicialmente altos o medios pasaron a niveles medios o bajos. Por ejemplo, instalando antivirus y políticas USB adecuadas, el riesgo de malware en PCs (Escenario 1) baja a “Bajo”. Este proceso de revisión confirma que los controles mitigatorios son efectivos en teoría, aunque debe validarse en la práctica.

### 5.2 Responsables Y Fechas De Revisión

Para asegurar el seguimiento, a cada control o grupo de medidas se asignó un **responsible encargado** (por ejemplo, administrador de sistemas, jefe de TI, equipo de desarrollo, seguridad física) y se fijó una **fecha de revisión** objetivo. Esto genera un cronograma de implementación y seguimiento continuo. En la Matriz final (Matriz de Estrategias de Mitigación y Riesgo Residual) se documentaron las columnas de “Responsible” y “Fecha de Revisión” junto a cada medida. De esta manera, el ciclo de OCTAVE-S concluye garantizando que los resultados sean accionables y auditables.

## Conclusiones

La aplicación de la metodología OCTAVE-S proporcionó un **análisis de riesgos completo y alineado con buenas prácticas** en el contexto de la tramitación electrónica municipal. En particular, permitió:

- **Identificar con claridad los activos críticos** (datos, sistemas e infraestructura esenciales para la continuidad del servicio).
    
- **Evaluar amenazas y vulnerabilidades operacionales relevantes** de manera estructurada, vinculando cada amenaza a activos específicos.
    
- **Determinar objetivamente niveles de riesgo iniciales** mediante matrices de probabilidad e impacto, priorizando los riesgos más significativos.
    
- **Proponer controles enfocados en riesgos altos** o críticos (autenticación multifactor, copias de seguridad, auditorías, cifrado, etc.), siguiendo marcos de referencia estándares.
    
- **Definir responsables y cronogramas** que aseguran la implementación práctica de las salvaguardas.

En resumen, el resultado final es un informe de riesgos **tangible y trazable**, listo para servir de base en planes de seguridad, auditorías internas o procesos de cumplimiento normativo. La involucración directa del equipo de la organización en el proceso (en línea con el espíritu autodirigido de OCTAVE) fortalece la cultura de seguridad. Este enfoque estratégico y metódico garantiza que la dirección disponga de información adecuada para gestionar riesgos antes de sufrir un incidente grave, alineándose con lo recomendado por la literatura especializada[sei.cmu.edu](https://www.sei.cmu.edu/library/octave-s-implementation-guide-version-1/#:~:text=The%20Operationally%20Critical%20Threat%2C%20Asset%2C,mitigation%20plans%20based%20on%20the)[dataguard.com](https://www.dataguard.com/blog/iso-27001-risk-management-strategies#:~:text=assessment%20process%2C%20a%20risk%20treatment,risk%20retention%20and%20risk%20acceptance).

## Referencias

- Alberts, C. J., Dorofee, A. J., Stevens, J. F., & Woody, C. (2005). _OCTAVE-S Implementation Guide, Version 1.0_. Pittsburgh, PA: Software Engineering Institute.
    
- Alianza Lázaro, Inc. (2023, 12 abril). **¿Qué es OCTAVE y OCTAVE Allegro?** Lazarus Alliance.
    
- DataGuard (2023, 11 de mayo). _ISO 27001 Risk Management: Strategies for Success_. Recuperado de https://www.dataguard.com/blog/iso-27001-risk-management-strategies
    
- Pascoe, J., & De Sevilla, M. (2013). _Aplicación de la norma OCTAVE-S en la empresa Pirámide Digital Cía. Ltda._ Tesis de grado. Universidad de Ingeniería (s.f.).