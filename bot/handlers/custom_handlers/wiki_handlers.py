from telebot.types import Message
from loader import bot
from services.wiki_service import get_wiki_instance
from handlers.custom_handlers.language_handler import user_languages
from keyboards import main_menu


@bot.message_handler(func=lambda message: message.text == "Найти статью по названию" or message.text == "Find an article by name")
def search_text(message: Message):
    search(message)


@bot.message_handler(commands=["search"])
def search(message: Message):
    chat_id = message.chat.id
    language = user_languages.get(chat_id, "ru")
    try:
        text = "Что вы хотите найти на Википедии?" if language == "ru" else "What do you want to find on Wikipedia?"
        bot.send_message(chat_id, text=text)
        bot.register_next_step_handler(message, page_exist)
    except Exception:
        text = "Произошла ошибка. Попробуйте позже." if language == "ru" else "An error has occurred. Try again later."
        bot.send_message(chat_id, text)


def page_exist(message: Message):
    chat_id = message.chat.id
    language = user_languages.get(chat_id, "ru")
    wiki = get_wiki_instance(language)

    page_py = wiki.page(message.text)

    if page_py.exists():
        process(message, wiki)
    else:
        text = "Статья не найдена." if language == "ru" else "The article was not found."
        bot.send_message(chat_id, text)


def process(message, wiki):
    chat_id = message.chat.id
    language = user_languages.get(chat_id, "ru")
    page_py = wiki.page(f"{message.text}")

    if not page_py.exists():
        bot.send_message(chat_id, "Статья не найдена." if language == "ru" else "Article not found.")
        return

    page_summary = "\n\n".join([p for p in page_py.summary.split("\n") if p.strip()])

    mobile_url = f"https://{language}.m.wikipedia.org/wiki/{page_py.title.replace(' ', '_')}"

    text = "Ссылка на статью:" if language == "ru" else "Link to the article:"
    bot.send_message(chat_id, f"{page_summary}\n\n{text} {mobile_url}",
                     reply_markup=main_menu.main_menu_keyboard(chat_id, user_languages))
