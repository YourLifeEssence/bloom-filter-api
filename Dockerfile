FROM python:3.11-slim

WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

RUN pip install flask

EXPOSE 5000

CMD ["python", "main.py"]