# Wiki Telegram Bot

## Описание

**Wiki Telegram Bot** — это телеграм-бот, который позволяет искать статьи на **Wikipedia** по названию на русском или английском языке.

## Возможности

* Поиск статей по названию
* Переключение между языками (русский / английский)
* Быстрый доступ к вики-статьям

## Запуск бота

### 1. Клонируйте репозиторий

```sh
git clone https://github.com/your_username/wiki_tg_bot.git
cd wiki_tg_bot
```

### 2. Версия Python

Проверьте, что у вас установлен Python **3.8+**:

```sh
python --version
```

### 3. Установите зависимости

```sh
pip install -r requirements.txt
```

### 4. Пропишите .env

Создайте файл `.env` и добавьте:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

### 5. Запуск

```sh
python main.py
```

## Запуск в Docker

```sh
docker build -t wiki_tg_bot .
docker run -d --env-file .env --name wiki_bot wiki_tg_bot
```

## English

### Description

**Wiki Telegram Bot** is a simple Telegram bot that allows users to search for **Wikipedia** articles by name in **Russian** and **English**.

### Features

* Search articles by title
* Switch between languages (Russian / English)
* Get quick access to Wikipedia articles

### Run the bot

#### 1. Clone the repository

```sh
git clone https://github.com/your_username/wiki_tg_bot.git
cd wiki_tg_bot
```

#### 2. Check Python version

Make sure you have Python **3.8+** installed:

```sh
python --version
```

#### 3. Install dependencies

```sh
pip install -r requirements.txt
```

#### 4. Create `.env` file

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

#### 5. Run the bot

```sh
python main.py
```

### Run in Docker

```sh
docker build -t wiki_tg_bot .
docker run -d --env-file .env --name wiki_bot wiki_tg_bot
```
