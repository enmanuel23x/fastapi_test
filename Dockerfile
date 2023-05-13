# Configuración de la imagen base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Copia los archivos de la aplicación a la imagen de Docker
COPY ./app /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir psycopg2-binary
RUN pip install sqlalchemy
RUN pip install python-dotenv

# Configura las variables de entorno para la conexión a PostgreSQL
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV DB_NAME=testdb
ENV DB_HOST=db
ENV DB_PORT=5432

# Configuración de entrada para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]