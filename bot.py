import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

import plotter
from exceptions import InvalidEquationError

start_message = "Hello, type your equation:"
help_message = "Type your equation and I will plot it for you"

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

users = {}

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


async def range(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    x_range = abs(float(context.args[0]))
    if user_id not in users:
        users[user_id] = plotter.Plotter('x**2', 10.5)
    my_plotter = users[user_id]
    my_plotter.set_x_range(float(x_range))
    
    if context.args[1] == 'apply':
        my_plotter.coordinate_plane()
        my_plotter.plot(my_plotter.get_perpective())
        my_plotter.save('my_drawing.png')
        my_plotter.clear()

        await context.bot.send_photo(chat_id=user_id, photo=open('my_drawing.png', 'rb'))
    else:
        await context.bot.send_message(chat_id=user_id, text='Range set to ' + str(x_range))


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


async def perspective(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    if user_id not in users:
        users[user_id] = plotter.Plotter('x**2', 10.5)
    my_plotter = users[user_id]
    my_plotter.set_perspective(bool(int(context.args[0])))

    if context.args[1] == 'apply':
        my_plotter.coordinate_plane()
        my_plotter.plot(my_plotter.get_perpective())
        my_plotter.save('my_drawing.png')
        my_plotter.clear()

        await context.bot.send_photo(chat_id=user_id, photo=open('my_drawing.png', 'rb'))
    else:
        await context.bot.send_message(chat_id=user_id, text='Perspective set to ' + str(my_plotter.get_perpective()))

async def plot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    my_plotter = users[user_id]
    my_plotter.coordinate_plane()
    my_plotter.plot(my_plotter.get_perpective())
    my_plotter.save('my_drawing.png')
    my_plotter.clear()

    await context.bot.send_photo(chat_id=user_id, photo=open('my_drawing.png', 'rb'))

if __name__ == '__main__':
    application = ApplicationBuilder().token('5770029784:AAHx7_4L4S_wuIm8kJr-9dky5_V0ALUWwjk').build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    range_handler = CommandHandler('range', range)
    perspective_handler = CommandHandler('perspective', perspective)
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, message)
    plot_handler = CommandHandler('plot', plot)

    application.add_handler(message_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(range_handler)
    application.add_handler(perspective_handler)
    application.add_handler(plot_handler)

    application.run_polling()