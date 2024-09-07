from pyexpat.errors import messages

from telebot import TeleBot

TOKEN = "7304930355:AAF-JHr5mBCQx301sk5sq60UZLI9R_iVX8A"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    print(message)
    bot.reply_to(message, text="Hey there! How can I help you?")

@bot.message_handler(func=lambda message: True)
def respond_to_all(message):
    print(message)
    bot.reply_to(message, message.text)

# Start the server
bot.infinity_polling()