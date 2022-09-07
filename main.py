import telebot


key = open('key.txt', 'r')
print(key)
bot = telebot.TeleBot(key)