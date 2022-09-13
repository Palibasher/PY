import  telebot
from extensions import Converter

BOT_token = '5502900689:AAFMEiP9pGfCRkuB5hqKR4gACK7qKjeFY_s'
bot = telebot.TeleBot(BOT_token)
coins = {"юань": "CNY", "доллар": "USD", "рубль": "RUB", "биткоин": "BTC", "евро":"EUR", "йена": "JPY"}
suf_coints = {"CNY": "юаней", "USD": "долларов", "RUB": "рублей", "BTC": "биткоинов", "EUR":"евро", "JPY": "йен"}

@bot.message_handler(commands=["start", "help"]) #обработка команды, сообщение с цитированием
def handle_start_help(message):
    bot.reply_to(message, f"Доброго дня, {message.chat.username}. Чтобы начать работу, введите комманду в следующем формате (через пробел):\n"
                          f"<Имя валюты> <В какую валюту перевести> <Кол-во переводимой валюты>\n\n"
                          f"Для того, чтобы увидеть список доступных валют, введите /values")

@bot.message_handler(commands=["values"])
def handle_list(message):
    bot.reply_to(message, f"В данный момент доступны следующие валюты:\n"
                          f"1) Рубль\n"
                          f"2) Доллар США\n"
                          f"3) Евро\n"
                          f"4) Йена\n"
                          f"5) Юань\n"
                          f"6) Биткоин\n")


@bot.message_handler(content_types=["text"]) #берем текст
def testfunc(message: telebot.types.Message):
    values = message.text.split(" ")
    what_we_have, what_we_need, ammount = values
    what_we_need = coins[what_we_need.lower()]
    what_we_have = coins[what_we_have.lower()]
    what_we_need_suf = suf_coints[what_we_need]
    what_we_have_suf = suf_coints[what_we_have]
    ammount = int(ammount)
    print(what_we_have, what_we_need, ammount)
    bot.reply_to(message, f"Конвертация {ammount} {what_we_have_suf}....\nРезультат: {Converter.get_ammount(what_we_need,what_we_have,ammount)} {what_we_need_suf}.")
    return what_we_have, what_we_need, ammount





bot.polling(none_stop=True)













