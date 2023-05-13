# Use an base image for FastAPI application
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Copy the application code to the container
COPY ./app /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set up the environment variables for the PostgreSQL connection
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV DB_NAME=testdb
ENV DB_HOST=db
ENV DB_PORT=5432

# Set the entrypoint command to wait for the database and start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]