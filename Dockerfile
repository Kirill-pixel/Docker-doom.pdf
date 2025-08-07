# Используем легковесный образ Python
FROM python:3.9-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем скрипт сервера в контейнер
COPY server.py .

# Копируем наш PDF-файл в контейнер
COPY public/index.pdf .

# Открываем порт 5050
EXPOSE 5050

# Запускаем Python-скрипт, который будет работать как сервер
CMD ["python", "server.py"]