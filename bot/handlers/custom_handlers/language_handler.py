import telebot
from telebot.types import Message
from loader import bot
from keyboards import main_menu

# Словарь для хранения языков пользователей
user_languages = {}

@bot.message_handler(func=lambda message: message.text == "Изменить язык" or message.text == "Change language")
def change_language_text(message: Message):
    set_language(message)

@bot.message_handler(commands=["change_language"])
def set_language(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text='Выбери язык\nChoose a language', reply_markup=main_menu.languages_keyboard())
    bot.register_next_step_handler(message, change_language)

def change_language(message: Message):
    chat_id = message.chat.id
    if message.text == "Русский 🇷🇺":
        user_languages[chat_id] = "ru"
        bot.send_message(chat_id, "Язык изменен на русский.", reply_markup=main_menu.main_menu_keyboard(chat_id, user_languages))
    elif message.text == "English 🇺🇸":
        user_languages[chat_id] = "en"
        bot.send_message(chat_id, "The language has been changed to English.", reply_markup=main_menu.main_menu_keyboard(chat_id, user_languages))
    else:
        bot.send_message(chat_id, "Неверный выбор. Попробуйте еще раз.")
