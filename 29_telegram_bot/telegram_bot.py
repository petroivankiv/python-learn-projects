from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# pipenv install python-telegram-bot
from difflib import get_close_matches
import json
from os import getenv
from dotenv import load_dotenv, find_dotenv

# find the .env file and load it
load_dotenv(find_dotenv())

# Constants
TOKEN: Final[str] = getenv("TELEGRAM_API_TOKEN")
BOT_USERNAME: Final[str] = getenv("TELEGRAM_BOT_USER_NAME")

with open('29_telegram_bot/brain.json', 'r', encoding='utf-8') as f:
    brain: dict = json.load(f)


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привіт! Радий вас тут бачити!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Задайте мені питання, а я спробую відповісти!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Команда поки не активна.')


# Create your own response logic
def handle_response(text: str) -> str:
    processed: str = text.lower()

    questions: list[str] = [q for q in brain]
    matches: list = get_close_matches(processed, questions, n=1, cutoff=0.6)

    if matches:
        return brain.get(matches[0])

    return 'Вибачте, але я не зрозумів...'


# Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    chatId: str = update.message.chat.id

    # Log users
    print(f'User ({chatId}) in {message_type}: "{text}"')

    # Handle message type
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    # Reply
    print('Bot:', response)
    await update.message.reply_text(response)


# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')


def main():
    print('Starting up bot...')

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Define a poll interval
    print('Polling...')

    app.run_polling(poll_interval=5)


if __name__ == '__main__':
    main()
