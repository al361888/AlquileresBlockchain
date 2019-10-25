import telebot
import telegram
import update as update

TOKEN = "1031956446:AAEqMOHrjTmC5lC0ub6sBbUrX-gY5pzfAdA"

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
