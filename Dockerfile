# Dockerfile
FROM python:3.13.5-slim

WORKDIR /app

COPY ./src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src
COPY ./migration /app/migration
COPY ./scripts /app/scripts
COPY ./template /app/template

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
