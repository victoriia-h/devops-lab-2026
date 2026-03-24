# Stage 1: Builder (Збираємо всі бібліотеки)
FROM python:3.11-alpine AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final (Створюємо легкий фінальний образ)
FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

# Запускаємо наш застосунок
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]