import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

import plotter
from exceptions import *

start_message = "Hello, type your equation:"
help_message = "Type your equation and I will plot it for you"

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

users = {}

def identify_args(arg):
    if arg == 'equation':
        return 'equation'
    elif arg == 'range':
        return 'range'
    elif arg == 'perspective':
        return 'perspective'
    else:
        raise InvalidArgumentError

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    if user_id not in users:
        users[user_id] = plotter.Plotter('x**2', 10.5)
    await context.bot.send_message(chat_id=user_id, text=start_message)


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    equation = update.message.text
    try:
        my_plotter = users[user_id]
        my_plotter.set_equation(equation)
        my_plotter.coordinate_plane()
        my_plotter.plot(my_plotter.get_perpective())
        my_plotter.save('my_drawing.png')
        my_plotter.clear()

        await context.bot.send_photo(chat_id=user_id, photo=open('my_drawing.png', 'rb'))
    except InvalidEquationError:
        await context.bot.send_message(chat_id=user_id, text='Invalid equation')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


async def set(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    if user_id not in users:
        users[user_id] = plotter.Plotter('x**2', 10.5)
    my_plotter = users[user_id]

    args = context.args

    if len(args) == 2:
        my_plotter.setter(identify_args(args[0]), args[1])
    elif len(args) == 4:
        my_plotter.setter(identify_args(args[0]), args[1])
        my_plotter.setter(identify_args(args[2]), args[3])
    elif len(args) == 6:
        my_plotter.setter(identify_args(args[0]), args[1])
        my_plotter.setter(identify_args(args[2]), args[3])
        my_plotter.setter(identify_args(args[4]), args[5])
    else:
        await context.bot.send_message(chat_id=user_id, text='Invalid arguments')
        return
    
    my_plotter.coordinate_plane()
    my_plotter.plot(my_plotter.get_perpective())
    my_plotter.save('my_drawing.png')
    my_plotter.clear()

    await context.bot.send_photo(chat_id=user_id, photo=open('my_drawing.png', 'rb'))

if __name__ == '__main__':
    application = ApplicationBuilder().token('5770029784:AAHx7_4L4S_wuIm8kJr-9dky5_V0ALUWwjk').build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, message)
    set_handler = CommandHandler('set', set)

    application.add_handler(message_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(set_handler)

    application.run_polling()