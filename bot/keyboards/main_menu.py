from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard(chat_id, user_languages):
    language = user_languages.get(chat_id, "ru")

    if language == 'ru':
        search_button = "Найти статью по названию"
        change_language_button = "Изменить язык"
    else:
        search_button = "Find an article by name"
        change_language_button = "Change language"

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(search_button),
        KeyboardButton(change_language_button)
    )
    return markup

def languages_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Русский \U0001F1F7\U0001F1FA"),
        KeyboardButton("English \U0001F1FA\U0001F1F8")
    )
    return markup
