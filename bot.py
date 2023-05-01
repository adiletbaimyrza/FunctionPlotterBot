import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

import plotter
from exceptions import InvalidEquationError

import os
from dotenv import load_dotenv
load_dotenv() # load environment variables from .env file


start_message = "Hello, type your equation:"

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    equation = update.message.text
    try:
        my_plotter = plotter.Plotter(equation, 10)
        my_plotter.coordinate_plane()
        my_plotter.plot()
        my_plotter.save('my_drawing.png')
        my_plotter.clear()

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('my_drawing.png', 'rb'))
    except InvalidEquationError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Invalid equation')

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('token_key')).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, help)
    application.add_handler(message_handler)
    application.add_handler(start_handler)

    application.run_polling()

