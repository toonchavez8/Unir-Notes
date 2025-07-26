

# ✅ Criterios de Aceptación - Simulación de Equipamiento para 4 Salas

## 🎯 Objetivo
Simular y documentar el cumplimiento de los criterios de aceptación para 4 salas que se usarán en sesiones simultáneas y una principal.

---

## 1. 📌 Identificación y Reserva de Salas

| Sala | Nombre Simulado | Capacidad | Tipo de Sesión |
|------|------------------|-----------|----------------|
| 1    | Sala Ágora       | 50        | Principal      |
| 2    | Sala Prisma      | 30        | Secundaria 1   |
| 3    | Sala Eclipse     | 30        | Secundaria 2   |
| 4    | Sala Quórum      | 30        | Secundaria 3   |

✅ **Todas las salas están identificadas y simuladas como reservadas.**

---

## 2. 🌐 Esquema de Red WiFi (por sala)

> Representación simple de conectividad y cobertura.

```plaintext
[Router Central] ---[Access Point Sala 1]---[Dispositivos (Proyector, Tablets, Streaming)]
                 └--[Access Point Sala 2]
                 └--[Access Point Sala 3]
                 └--[Access Point Sala 4]
````

✅ **Cada sala cuenta con su punto de acceso WiFi para streaming.**

---

## 3. 🖼️ Esquema Visual y de Sonido

### Sala Ejemplo: Sala Ágora (Principal)

![[Pasted image 20250712155825.png]]
- ✅ 1 Proyector + 4 pantallas unidas
    
- ✅ 2 micrófonos de alta calidad
    
    

_Repite este esquema para las demás salas según sea necesario._

---

## 4. 📦 Inventario de Equipos por Sala

| Sala         | Micrófonos | Proyector | Pantallas | Altavoces HQ 5.1 | Bocinas Ambientales | Tablets |
| ------------ | ---------- | --------- | --------- | ---------------- | ------------------- | ------- |
| Sala Ágora   | 2          | 1         | 4         | Sí               | Sí                  | 10      |
| Sala Prisma  | 2          | 1         | 1         | No               | Sí                  | 5       |
| Sala Eclipse | 2          | 1         | 1         | No               | Sí                  | 5       |
| Sala Quórum  | 2          | 1         | 1         | No               | Sí                  | 5       |
|              |            |           |           |                  |                     |         |
|              |            |           |           |                  |                     |         |

✅ **Inventario simulado completo.**

---

## 📝 Observaciones

- El equipo ha sido simulado para escenarios realistas.
    
- El objetivo del ejercicio es validar que se pueden gestionar sesiones paralelas y una principal sin conflictos de infraestructura.
    
- Los diagramas y tablas pueden evolucionar si cambian los requisitos.
    