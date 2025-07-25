import telebot

TOKEN = '8417723954:AAFAQf9hB_N7hr8mAu92fdVaAns9Myjlfbs'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в MyBotGPT!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы сказали: {message.text}")

bot.infinity_polling()
