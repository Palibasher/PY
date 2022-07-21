import telebot

bot = telebot.TeleBot('5457087414:AAHhrFC3QtS9TWaul16L0w8OIi-mYIbQ42E')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b> Юля в жопе пуля </b>', parse_mode='html')


bot.polling(non_stop=True)
