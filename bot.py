import bot_config
import telebot

TOKEN = bot_config.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.polling()
