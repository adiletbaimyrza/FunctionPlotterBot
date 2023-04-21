import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

import linear
import interpreter
import plane
from PIL import Image
import turtle
import startMessages

Token = '6220004213:AAGuemjvfG0-p7fNO7BPKTEZXftdtoGftMU'

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def startMessages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    equation = update.message.text
    match = interpreter.Input.check_pattern_linear(equation)
    res = interpreter.Input.extract_args(match)


    coordinate_plane = plane.Plane()
    coordinate_plane.open_screen()
    coordinate_plane.make_grid()
    coordinate_plane.draw_plane()

    equation = linear.Linear()
    equation.plot_graph(res[0],res[1])
    equation.write_func_on_graph(res[0], res[1])

    ts = turtle.Screen().getcanvas()
    ts.postscript(file='my_drawing.eps')

    img = Image.open('my_drawing.eps')
    img.save('my_drawing.png', 'png')

    turtle.Screen().clear()

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('my_drawing.png', 'rb'))

if __name__ == '__main__':
    application = ApplicationBuilder().token(Token).build()

    start_handler = CommandHandler('start', startMessages)
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, help)
    application.add_handler(message_handler)
    application.add_handler(start_handler)

    application.run_polling()

