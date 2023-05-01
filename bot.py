import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

import plotter
from exceptions import InvalidEquationError

import os
from dotenv import load_dotenv
load_dotenv() # load environment variables from .env file


start_message = "Hello, type your equation:"
help_message = "Type your equation and I will plot it for you"

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

my_plotter = plotter.Plotter('x**2', 10.5)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    equation = update.message.text
    try:
        my_plotter.set_equation(equation)
        my_plotter.coordinate_plane()
        my_plotter.plot()
        my_plotter.save('my_drawing.png')
        my_plotter.clear()

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('my_drawing.png', 'rb'))
    except InvalidEquationError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Invalid equation')

async def range(update: Update, context: ContextTypes.DEFAULT_TYPE):
    x_range = abs(float(context.args[0]))

    try:
        my_plotter.set_x_range(float(x_range))
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Invalid range')
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Range set to ' + str(x_range))

    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('token_key')).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    range = CommandHandler('range', range)

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, message)
    application.add_handler(message_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(range)

    application.run_polling()

