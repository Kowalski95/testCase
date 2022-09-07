import telebot


key = open('key.txt', 'r')
bot = telebot.TeleBot(key.readline())