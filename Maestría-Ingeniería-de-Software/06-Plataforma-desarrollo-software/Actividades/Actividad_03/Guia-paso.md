# Guía Paso a Paso — Paso 6 (Pruebas De Carga Con k6)

> Rol 5 — **Carga y análisis de rendimiento (Miguel)**

Esta guía te lleva, **paso a paso**, para cumplir el requisito:

- **1000 usuarios concurrentes (pico)**

- **p(95) < 5000 ms**

- **tasa de error < 1%**

---

## 1) Objetivo De Esta Prueba

Validar el comportamiento del backend de Petclinic bajo carga de lectura sobre una entidad estable, con ramp-up, pico de concurrencia y duración suficiente para observar degradación.

---

## 2) Justificación De Herramienta (texto Para Tu memoria)

Puedes usar este texto tal cual (o adaptarlo):

> Se seleccionó **k6** para pruebas de carga porque permite modelar escenarios de usuarios virtuales con ramp-up y umbrales medibles (p95, tasa de error), ofrece ejecución reproducible por script y genera evidencia exportable (resumen JSON y salida de consola), lo que facilita trazabilidad técnica y comparación entre corridas.

---

## 3) Prerrequisitos

- Backend y frontend ya preparados en tu entorno (ya tienes scripts).

- Java y Node instalados.

- `k6` instalado.

### 3.1 Instalar K6 (Windows)

Opción recomendada con Chocolatey:

```powershell

choco install k6 -y

```

Alternativa con Winget:

```powershellcd 

winget install k6 --source winget

```

Verificar instalación:

```powershell

k6 version

```

---

## 4) Levantar Aplicación Antes De Medir

Desde la raíz del repo orquestador:

```powershell

.\setup-and-start.cmd

```

Verifica backend en:

- <http://localhost:9966/petclinic/actuator/health>

- <http://localhost:9966/petclinic/swagger-ui/index.html>

Si el backend no responde, **no ejecutes carga todavía**.

---

## 5) Definir Escenario Técnico (6.1)

Se usará endpoint de lectura estable:

- `GET /petclinic/api/pettypes`

Razón: catálogo estable, consulta simple y repetible para medir rendimiento base.

Características del escenario:

- Ramp-up progresivo.

- Pico de 1000 usuarios concurrentes.

- Tiempo suficiente para observar comportamiento sostenido.

---

## 6) Crear Script K6

### 6.1 Crea Carpeta Para Carga Y Evidencias

```powershell

New-Item -ItemType Directory -Force .\carga, .\evidencias | Out-Null

```

### 6.2 Crea El Archivo `carga\petclinic-step6.js`

Copia este contenido:

```javascript

import http from 'k6/http';

import { check, sleep } from 'k6';

  

const BASE_URL = __ENV.BASE_URL || 'http://localhost:9966';

const PATH = '/petclinic/api/pettypes';

  

export const options = {

  stages: [

    { duration: '1m', target: 100 },

    { duration: '2m', target: 500 },

    { duration: '3m', target: 1000 },

    { duration: '3m', target: 1000 },

    { duration: '2m', target: 0 },

  ],

  thresholds: {

    http_req_duration: ['p(95)<5000'],

    http_req_failed: ['rate<0.01'],

    checks: ['rate>0.99'],

  },

};

  

export default function () {

  const res = http.get(`${BASE_URL}${PATH}`, {

    headers: {

      Accept: 'application/json',

    },

    timeout: '10s',

  });

  

  check(res, {

    'status es 200': (r) => r.status === 200,

    'respuesta no vacía': (r) => r.body && r.body.length > 2,

  });

  

  sleep(1);

}

```

---

## 7) Ejecutar Prueba Principal (6.3)

Desde la raíz del repo:

```powershell

k6 run --summary-export ./evidencias/k6-summary-step6.json [./carga/petclinic-StressTest.js](http://_vscodecontentref_/1) | tee ./evidencias/k6-console-step6.txt

```

> Si quieres cambiar host base:

```powershell

$env:BASE_URL="http://localhost:9966"

k6 run --summary-export .\evidencias\k6-summary-step6.json .\carga\petclinic-step6.js

```

---

## 8) Cómo Interpretar Resultados (cumple / no cumple)

En la salida de k6 revisa estos indicadores:

1. `http_req_duration` con `p(95)`

2. `http_req_failed` (rate)

3. `checks` (debe quedar alto)

### Regla De Decisión

- **Cumple** si:

  - `p(95) < 5000 ms`

  - `http_req_failed < 0.01` (menos de 1%)

- **No cumple** si uno o ambos umbrales fallan.

### Plantilla De Conclusión (para Copiar En memoria)

#### Si Cumple

> En el escenario de carga con pico de 1000 usuarios concurrentes, la API cumplió el requisito no funcional: p(95) se mantuvo por debajo de 5 segundos y la tasa de error fue inferior al 1%.

#### Si no Cumple

> En el escenario de carga con pico de 1000 usuarios concurrentes, la API no cumplió el requisito no funcional, debido a que [p(95) superó 5 segundos / tasa de error superó 1%]. Se proponen acciones de optimización sobre [backend / base de datos / infraestructura].

---

## 9) Hipótesis Y Recomendaciones Si no Cumple

Usa esta lista para tu análisis técnico:

- Saturación de hilos del servidor Java en picos altos.

- Cuello de botella en consultas SQL (faltan índices o N+1 queries).

- Contención de conexiones del pool de base de datos.

- Latencia local por recursos insuficientes (CPU/RAM) en tu máquina.

- Falta de caché para lecturas repetitivas.

Recomendaciones iniciales:

1. Monitorear CPU, RAM y GC durante la prueba.

2. Revisar pool de conexiones y tiempos de espera.

3. Perfilar consultas de DB para endpoint probado.

4. Repetir prueba con warm-up previo y comparar.

5. Ejecutar en entorno más cercano a producción para validación final.

---

## 10) Evidencias Que Debes Entregar

Genera y adjunta mínimo:

- Script de carga: `carga/petclinic-step6.js`

- Resumen JSON: `evidencias/k6-summary-step6.json`

- Salida de consola: `evidencias/k6-console-step6.txt`

- 2 capturas de pantalla:

  - Terminal al finalizar la ejecución.

  - Métricas clave donde se ve p(95) y tasa de error.

Checklist rápido:

- [ ] Script creado.

- [ ] Prueba ejecutada completa.

- [ ] Resultado interpretado (cumple/no cumple).

- [ ] Hipótesis técnicas redactadas si falla.

- [ ] Evidencias guardadas en carpeta `evidencias/`.

---

## 11) Texto Corto Para la Presentación (diapositiva)

> Se implementó una prueba de carga con k6 sobre el endpoint de lectura `/petclinic/api/pettypes`, aplicando ramp-up hasta 1000 usuarios concurrentes y umbrales p(95) < 5000 ms y error < 1%. El resultado fue [cumple/no cumple], respaldado por resumen JSON y salida de ejecución.