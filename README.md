## Levantar el proyecto
### Desarrollo
- API
```sh
uvicorn main:app --reload --port 5000
```
- DB
```SH
docker-compose up -d db
```
### Produccion
```sh
docker-compose up --build
```