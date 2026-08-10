# Ejecución del laboratorio de seguridad — 2026-08-10

## Estado

**Inconclusa / bloqueada antes de las pruebas dinámicas.**

## Comprobaciones realizadas

- Docker Desktop quedó operativo usando el contexto `desktop-linux`.
- El contexto Docker no contenía la imagen `dominus-broker:security-lab`.
- Se intentó construir la imagen desde `Referance/dominus-broker/Dockerfile`.
- Las imágenes base `golang:1.26-alpine3.23` y `alpine:3.23.3` se descargaron correctamente.

## Motivo del bloqueo

El build falló durante `go mod tidy` porque no pudo descargar el módulo privado:

```text
github.com/MBI-88/dominus-proto-definition@v1.3.7
remote: Repository not found.
fatal: Authentication failed
```

No se ejecutaron BE-01–BE-07 ni las pruebas dinámicas del SDK en esta sesión, porque no se creó un broker verificable.

## Reanudación

Proporcionar al entorno un token de GitHub con acceso de lectura al repositorio privado y reconstruir:

```bash
docker build --build-arg GITHUB_TOKEN=<token-no-registrar> \
  -t dominus-broker:security-lab Referance/dominus-broker
```

No guardar el token en esta carpeta ni en los logs.
