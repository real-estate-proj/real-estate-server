# Dockerfile
FROM python:3.13.5-slim

# Tạo thư mục làm việc trong container
WORKDIR /app

# Copy requirements.txt từ src/
COPY ./src/requirements.txt .

# Cài đặt các package Python
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn cần thiết
COPY ./src /app/src
COPY ./migration /app/migration
COPY ./scripts /app/scripts
COPY ./template /app/template

# Chạy FastAPI app từ src/main.py
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]