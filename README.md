# Proyecto FastAPI + MySQL con Docker

Este proyecto utiliza Docker y Docker Compose para levantar un entorno de desarrollo con una API en FastAPI y una base de datos MySQL.

## Estructura del Proyecto

```
.
├── app/                 # Código fuente de la aplicación FastAPI
│   └── main.py
├── sql/                 # Archivos SQL de inicialización
│   └── init.sql
├── .env                 # Variables de entorno
├── Dockerfile           # Imagen de FastAPI
├── docker-compose.yml   # Servicios: app y base de datos
└── README.md
```

## Requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

## Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
DB_USER=root
DB_PASSWORD=root
DB_HOST=db
DB_PORT=3306
DB_NAME=pruebas
```

## Instrucciones para levantar el entorno

1. **Clona este repositorio:**


2. **Levanta los servicios con Docker Compose:**

```bash
docker-compose up --build
```

Esto ejecutará:

- La base de datos MySQL en el puerto `3308` (expuesto desde el interno `3306`)
- La aplicación FastAPI en el puerto `8005` (expuesto desde el interno `8000`)

3. **Verifica la API en tu navegador o con curl:**

```
http://localhost:8005
```

## Detalles técnicos

### Base de datos

- Imagen: `mysql:8.0`
- Puerto: `3308:3306`
- Credenciales definidas en `.env`
- Archivos de inicialización en `./sql/`

### FastAPI

- Montada desde `./app`
- Ejecutada con `fastapi dev main.py`
- Dockerfile en base a `python:3.11-slim`

## Comandos útiles

- **Apagar los servicios:**

```bash
docker-compose down
```

- **Ver los logs:**

```bash
docker-compose logs -f
```

- **Reconstruir contenedores:**

```bash
docker-compose up --build
```

## Notas

- Asegúrate de que el puerto `3308` no esté siendo usado por otro proceso.
- La base de datos puede tardar unos segundos en iniciar completamente.

## Autor

Kevin Salazar – [KEFAB]
