import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError(".env не загружается. Проверь расположение файла!")

print(f"BOT_TOKEN загружен: {BOT_TOKEN}")  # Отладка
