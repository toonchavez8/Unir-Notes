# Titulo

## Introducción a la Metodología De OCTAVE

Este documento narra mi proceso completo de **análisis de riesgos** aplicado a un servicio de tramitación electrónica, utilizando la metodología **OCTAVE** (Operationally Critical Threat, Asset, and Vulnerability Evaluation).

Primero se identificaron los **activos críticos** del sistema (**DEFINIR**) y sus **requisitos de seguridad** (**DEFINIR**), junto con las amenazas y vulnerabilidades asociadas. Cada escenario de riesgo fue evaluado cualitativa y cuantitativamente, asignando probabilidades e impactos, también siguiendo los conceptos vistos en el video **(SeguridadTV, 2020)**.

Después se definieron **estrategias de tratamiento** (**DEFINIR**) y **controles** técnicos/organizativos (**DEFINIR**) para mitigar los riesgos más altos.

## Fase 1: Identificación De Activos

El primer paso consistió en identificar los **activos esenciales** del sistema de tramitación.

Tomando la definición de activo como concepto clave propuesto por (SeguridadTV, 2020) que lo describe como cualquier cosa que tenga valor para la organización, ya sea tangible o intangible, podemos asumir que los components tecnológicos críticos para este proceso son:

- El servidor principal de tramitación.
    
- Los PCs de oficina.
    
- La base de datos de expedientes.
    
- La aplicación de gestión.
    
- El sistema de correo electrónico.
    
- La infraestructura de red.
    
- La sala de equipos.

Estos activos fueron evaluados según los términos de **Confidencialidad**, **Integridad** y **Disponibilidad** (C/I/A), así como su impacto potential ante una falla. A continuación, se muestra la tabla de activos clave elaborada (cada activo fue catalogado por tipo, propietario, ubicación y valorizado en C/I/A y nivel de impacto):

![[Pasted image 20251117141957.png]]

Cada activo fue calificado según lo que implicaría su nivel de seguridad. Por ejemplo, el **Servidor** y la **Base de Datos** obtuvieron valoraciones **altas** en C/I/A, dado que contienen **datos sensibles** y soportan el **funcionamiento operativo** esencial de la unidad.

En contraste, los **PCs de oficina** se valoraron como **medios** en C/I/A, puesto que solo almacenan expedientes de forma temporal y existe un procedimiento sencillo y periódico para reinstalar el sistema íntegro.

Esta valoración aporta los cimientos de las siguientes fases del análisis de riesgos, ya que define claramente **los recursos a proteger** e identifica cuáles son más críticos en términos de **Confidencialidad, Integridad y Disponibilidad**.

## Fase 2: Identificación De Amenazas Y Vulnerabilidades

Siguiendo la definición de activos que identificamos, generamos escenarios de amenazas para cada activo, una amenaza concreta y una vulnerabilidad. Ente los escenarios considerados lo que desacataron mayormente fueron:

- **Ataques de ransomware:** cifrado malicioso de expedientes o sistemas críticos.
    
- **Acceso no autorizado a expedientes:** intrusiones internas o externas a la base de datos.
    
- **Interrupción del servicio:** fallos de conexión a Internet o problemas en la red local.
    
- **Pérdida o fuga de información vía APIs externas:** por ejemplo, exposición de datos durante interacciones con el archivo central.
    
- **Manipulación o alteración de datos de tramitaciones:** cambios maliciosos en expedientes abiertos o cerrados.
    
- **Errores de configuración en servidores o bases de datos:** desbordamientos, parches faltantes o servicios inseguros.
    
- **Saturación por picos de carga o ataques DDoS:** sobrecarga del enlace ADSL o del servidor web.

En cada escenario se evalúa la **probabilidad** en una escala del 1 al 5 y el **impacto** percibido en el negocio. Esto permite calcular el **puntaje de riesgo** (Probabilidad × Impacto) y asignarle una calificación cualitativa.

![[Pasted image 20251117153335.png]]

Por ejemplo, en el Escenario 1 "Infección por malware" en los PCs, una probabilidad media de 3 e impacto de negocio siendo 2 resultan en un riesgo de 6 con el cualitativo siendo Medio. Además, se documentan los **controles existentes** y se proponen **controles recomendados** para mitigar cada vulnerabilidad.

## Fase 3: Selección De Mitigaciones Y Controles

Al revisar los riegos identificados de cada activo podemos definir estrategias de tratamiento según el riesgo acceptable y costos asociados. Siguendo las definiciones de conceptos estrategias de riegos mitigados como indica la pagina (DataGuard, 2023) tenemos 4 tipos de Estrategias:

- **Evitar:** eliminar la causa del riesgo (por ejemplo, desactivar una funcionalidad no esencial vulnerable).
    
- **Reducir:** implementar controles para disminuir probabilidad o impacto (p.ej. reforzar autenticación, cifrado, copias de seguridad).
    
- **Transferir:** asignar el riesgo a terceros (por ejemplo, contratar seguro o delegar servicio a un proveedor con garantía de servicio).
    
- **Aceptar:** asumir el riesgo cuando sea leve o el costo de mitigarlo desproporcionado.

Estas opciones se anotaron en la matriz como “Estrategia de Mitigación” para cada escenario. Por ejemplo, ante riesgos altos se priorizó reducir (mejorar controles) o evitar (modificar procesos), mientras que riesgos menores se podrían aceptar o monitorizar pasivamente. 

![[Pasted image 20251117164449.png]]

Con las estrategias definidas, se enlistaron los **controles a aplicar** necesarios. Entre los controles recomendados destacan:

- **Autenticación multifactor (MFA):** fortalece el acceso a sistemas críticos.
    
- **Mejoiamiento de servidores:** deshabilitar servicios innecesarios, aplicar parches y configuraciones seguras con duplicacion de datos.
    
- **Implementación sistema de monitoreo centralizado:** para detectar incidentes en tiempo real.
    
- **Cifrado de datos en tránsito y reposo:** proteger información confidencial en la base de datos y comunicaciones.
    
- **Backups periódicos probados:** realizar copias de seguridad locales y en ubicaciones remotas y verificar su restauración.
    
- **Validación y sanitización de datos en APIs:** proteger integraciones con el archivo central.
Algunos controles ya existían (por ejemplo, firewall perimetral, autenticación básica), otros se propusieron. Estos controles se registraron en la matriz como “Controles Aplicados” y también se marcó su estado riegos residual en la etapa final.

## Fase 4: Evaluación Del Riesgo Residual Y Plan De Acción

Tras planificar la aplicación de los controles recomendados, se estimó el **nivel de riesgo residual** para cada escenario, recalculando la probabilidad e impacto asumibles con las salvaguardas propuestas. Se llenó la columna “Nivel de Riesgo Residual” en la matriz final. 

En la mayoría de los casos, los riesgos inicialmente altos o medios pasaron a niveles medios o bajos. Por ejemplo, instalando antivirus y políticas USB adecuadas, el riesgo de malware en PCs (Escenario 1) baja a “Bajo”. Este proceso de revisión confirma que los controles mitigatorios son efectivos en teoría, aunque debe validarse en la práctica.

Para asegurar el seguimiento, a cada control o grupo de medidas se asignó un **responsible encargado** (por ejemplo, administrador de sistemas, jefe de TI, equipo de desarrollo, seguridad física) y se fijó una **fecha de revisión** objetivo. Esto genera un cronograma de implementación y seguimiento continuo. En la Matriz final (Matriz de Estrategias de Mitigación y Riesgo Residual) se documentaron las columnas de “Responsible” y “Fecha de Revisión” junto a cada medida. De esta manera, el ciclo de OCTAVE-S concluye garantizando que los resultados sean accionables y auditables.

![[Pasted image 20251117164409.png]]

## Conclusiones

La aplicación de la metodología OCTAVE proporciona un **análisis de riesgos completo y alineado con buenas prácticas** en el contexto de la tramitación electrónica municipal. En particular, permitió:

- **Identificar con claridad los activos críticos** (datos, sistemas e infraestructura esenciales para la continuidad del servicio).
    
- **Evaluar amenazas y vulnerabilidades operacionales relevantes** de manera estructurada, vinculando cada amenaza a activos específicos.
    
- **Determinar objetivamente niveles de riesgo iniciales** mediante matrices de probabilidad e impacto, priorizando los riesgos más significativos.
    
- **Proponer controles enfocados en riesgos altos** o críticos (autenticación multifactor, copias de seguridad, auditorías, cifrado, etc.), siguiendo marcos de referencia estándares.
    
- **Definir responsables y cronogramas** que aseguran la implementación práctica de las salvaguardas.

En resumen, el resultado final es un informe de riesgos **tangible y trazable**, listo para servir de base en planes de seguridad, auditorías internas o procesos de cumplimiento normativo.

## Referencias

Caralli, Richard A., Stevens, James F., Young, L. R., & Wilson, W. R. (2007). _Introducing OCTAVE Allegro: Improving the Information Security Risk Assessment Process_ (No. CMU/SEI-2007-TR-012). Software Engineering Institute, Carnegie Mellon University. [https://www.sei.cmu.edu/documents/786/2007_005_001_14885.pdf](https://www.sei.cmu.edu/documents/786/2007_005_001_14885.pdf)

Emrick Etheridge. (2023, mayo 11). ISO 27001 risk management: Strategies for success [Blog]. _DataGuard_. [https://www.dataguard.com/blog/iso-27001-risk-management-strategies](https://www.dataguard.com/blog/iso-27001-risk-management-strategies)

SeguridadTV (Director). (2020, mayo 10). _Metodología de análisis de riesgos con Octave Allegro (Parte I)_ [Video]. SeguridadTV. [http://www.youtube.com/watch?v=U8zQS8Q9nKw](http://www.youtube.com/watch?v=U8zQS8Q9nKw)