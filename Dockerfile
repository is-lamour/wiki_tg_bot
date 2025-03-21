# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt .
COPY bot/ bot/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем переменные окружения
ENV BOT_TOKEN=${BOT_TOKEN}

# Запускаем бота
CMD ["python", "bot/main.py"]
