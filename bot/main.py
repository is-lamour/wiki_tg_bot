import loader
from handlers import custom_handlers, default_handlers

print("Бот загружен:", loader.bot)

if __name__ == "__main__":
    loader.bot.polling(none_stop=True)
