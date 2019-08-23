import bot_config
import telebot
from pprint import pprint
from telebot import apihelper

TOKEN = bot_config.TOKEN
bot = telebot.TeleBot(TOKEN)

apihelper.proxy = {'https':'https://51.79.31.27:8080'}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Привет")

@bot.message_handler(content_types=['sticker'])
def print_message(message):
    pprint(message.json)
    bot.send_sticker(message.chat.id, "CAADAgADeQMAArarPwullRa4zzq2ThYE")

bot.polling()
