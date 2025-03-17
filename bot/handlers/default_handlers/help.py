from loader import bot
from telebot.types import Message
from handlers.custom_handlers.language_handler import user_languages


DEFAULT_COMMANDS = {
    "ru": [
        ("/start", "Запустить бота"),
        ("/help", "Вывести справку"),
        ("/search", "Найти статью по названию"),
        ("/change_language", "Изменить язык")
    ],
    "en": [
        ("/start", "Start the bot"),
        ("/help", "Show help"),
        ("/search", "Search for an article"),
        ("/change_language", "Change language")
    ]
}


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    chat_id = message.chat.id
    language = user_languages.get(chat_id, "ru")  # Определяем язык

    text = [f"{command} - {desc}" for command, desc in DEFAULT_COMMANDS[language]]

    help_text = {
        "ru": "Вот список моих команд:",
        "en": "Here is a list of my commands:"
    }

    bot.send_message(chat_id, help_text[language])
    bot.send_message(chat_id, "\n".join(text))
