#Import necessary libraries
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters


import quadratic
import linear
import trigonometric
import math
import interpreter
import plane
import re
from PIL import Image
import turtle

Token = '6220004213:AAGuemjvfG0-p7fNO7BPKTEZXftdtoGftMU'

#Set up logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#Define start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Nice cock.')

#Define help command function
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    equation = update.message.text
    match = interpreter.Input.check_pattern_linear(equation)
    res = interpreter.Input.extract_args(match)

    # Set up coordinate plane
    coordinate_plane = plane.Plane()
    coordinate_plane.open_screen()
    coordinate_plane.make_grid()
    coordinate_plane.draw_plane()

    # Plot linear equation on coordinate plane
    equation = linear.Linear()
    equation.plot_graph(res[0],res[1])
    equation.write_func_on_graph(res[0], res[1])

    # Save drawing as PNG file
    ts = turtle.Screen().getcanvas()
    ts.postscript(file='my_drawing.eps')

    img = Image.open('my_drawing.eps')
    img.save('my_drawing.png', 'png')

    turtle.Screen().clear()

    # Send PNG file to user
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('my_drawing.png', 'rb'))

# Set up Telegram bot application
if __name__ == '__main__':
    application = ApplicationBuilder().token(Token).build()

    # Add handlers for start and help commands
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, help)
    application.add_handler(message_handler)
    application.add_handler(start_handler)

    # Start polling for incoming messages
    application.run_polling()

