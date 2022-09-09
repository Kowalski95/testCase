import telebot
from aiogram import types


key = open('key.txt', 'r')              # В данной переменной храниться токен ботта
bot = telebot.TeleBot(key.readline())

@bot.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def send_welcome(message: types.Message):
	    await message.reply("hi")


@bot.message_handler(content_types=["new_chat_members"]) #Зашел
async def on_user_joined(message: types.Message):
    await message.delete()

@bot.message_handler(content_types=['text'])
def message_input_step(message):
    bot.send_message(message.user.id,'Добрый день ')

# @bot.message_handler()
# def test(message):
#     bot.send_message(message.from_user_id, 'Hi')

bot.polling()


# https://docs-python.ru/packages/biblioteka-python-telegram-bot-python/filtry-soobschenij/