# CL-06 — Ciclo de vida de conexiones

## Resultado

**Fallida / requiere investigación.** Tras 20 operaciones se observaron 160 goroutines adicionales (`3` antes y `163` después) después de 250 ms. El SDK no expone un método para cerrar el `ClientConn` creado internamente.

Evidencia: `E38-CL06-connections.txt`.

Recomendación: devolver o gestionar explícitamente `ClientConn.Close`, reutilizar conexiones y repetir la medición después de un periodo de estabilización mayor.
