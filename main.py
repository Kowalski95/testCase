import telebot


key = open('key.txt', 'r')              # В данной переменной храниться токен ботта
bot = telebot.TeleBot(key.readline())

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, я супер бот.\n Для начала новой игры введите команду: New \n Для получения информации о персонаже напишите: info ")


@bot.message_handler(content_types=['text'])
def message_input_step(message):
    bot.send_message(message.chat.id,'Добрый день ' + message.chat.first_name)



bot.polling()