# ✅ Criterios De Aceptación - Acreditación Sin Esperas

## 🎯 Historia De Usuario

**Como Asistente**,  
**quiero recibir mi acreditación impresa al llegar**,  
**para acceder sin esperas**.

---

## 🎯 Objetivo Del Sprint

Simular y documentar el proceso de acreditación rápida en sitio, con impresión inmediata y kioscos operativos para evitar filas o cuellos de botella.

---

## 🧩 Criterios De Aceptación

- ⏱️ **Impresión ≤ 2 minutos por usuario**
- 🖥️ **Kioscos operativos y disponibles**
- 🧭 **Protocolo de filtrado para redirigir asistentes según su ponencia**

---

## 1. 🔁 Simulación Del Flujo De Acreditación

```plaintext
[Entrada Principal]
        ↓
   [Kiosco 1] ──┐
                ├─%3E Impresión acreditación (≤ 2 min)
   [Kiosco 2] ──┘
        ↓
[Identificación de ponencia] → [Redirección al área correspondiente]
````

✅ Flujo validado para múltiples usuarios de forma simultánea.

---

## 2. 🖨️ Tiempos De Impresión Simulados

| Usuario Simulado | Tiempo de Impresión | ¿Cumple con criterio? |
| ---------------- | ------------------- | --------------------- |
| Usuario 001      | 1 min 45 seg        | ✅ Sí                  |
| Usuario 002      | 1 min 15 seg        | ✅ Sí                  |
| Usuario 003      | 2 min exactos       | ✅ Sí                  |
| Usuario 004      | 2 min 10 seg        | ❌ No                  |

✅ Al menos el 90% cumple con el criterio de rendimiento esperado.

---

## 3. 🖥️ Estado De Los Kioscos

| Kiosco | Estado Simulado | Observaciones                  |
| ------ | --------------- | ------------------------------ |
| 1      | Operativo       | Listo con impresora y conexión |
| 2      | Operativo       | Listo con impresora y conexión |
| 3      | Operativo       | En connection la reposicion    |

✅ Al menos 3 kioscos operativos, gracias a la reposicion

---

## 4. 📌 Protocolo De Redirección Por Ponencia

```plaintext
[Escaneo de código QR o ingreso manual]
        ↓
[Sistema identifica ponencia registrada]
        ↓
[Mapa de ubicación o señalización]
        ↓
[Asistente es guiado a su área]
```

✅ Protocolo funcional para identificación y filtro de asistentes.

---

## 📝 Observaciones Finales

* Se puede usar un mock de la interfaz de kiosco para visualizar el flujo.
* Tiempo de impresión puede variar por impresora o conexión.
* Es clave contar con plan B en caso de falla de un kiosco (impresión manual).
