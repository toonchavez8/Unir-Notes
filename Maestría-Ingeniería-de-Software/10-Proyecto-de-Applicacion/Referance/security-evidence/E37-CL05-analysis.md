# CL-05 — Error de serialización

## Resultado

**Fallida.** Al enviar una función no serializable:

- `json.Marshal` falla internamente.
- El error se descarta.
- Se llama `Send`.
- El servidor recibe un payload vacío de longitud 0.

Evidencia: `E37-CL05-serialization.txt`.

Recomendación: devolver el error de `json.Marshal` y no invocar `Send` cuando la serialización falle.
