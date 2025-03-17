from loader import bot
from telebot.types import Message
from keyboards.main_menu import main_menu_keyboard
from handlers.custom_handlers.language_handler import user_languages
from .help import bot_help


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    chat_id = message.chat.id
    language = user_languages.get(chat_id, "ru")  # Определяем язык пользователя

    welcome_text = {
        "ru": f"Добро пожаловать, {message.from_user.full_name}! Я бот, созданный чтобы искать статьи на Википедии.",
        "en": f"Welcome, {message.from_user.full_name}! I'm a bot created to search for Wikipedia articles."
    }

    bot.send_message(
        chat_id,
        welcome_text[language],
        reply_markup=main_menu_keyboard(chat_id, user_languages)
    )
    bot_help(message)  # Вызываем help, чтобы показать команды
