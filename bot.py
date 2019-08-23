import bot_config
import telebot
from telebot import apihelper

TOKEN = bot_config.TOKEN
bot = telebot.TeleBot(TOKEN)

apihelper.proxy = {'https':'https://51.79.31.27:8080'}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.polling()
