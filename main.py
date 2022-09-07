import telebot


key = open('key.txt', 'r')
bot = telebot.TeleBot(key.readline())

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, я супер бот.\n Для начала новой игры введите команду: New \n Для получения информации о персонаже напишите: info ")


@bot.message_handler(content_types=['text'])
def message_input_step(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)

bot.polling()