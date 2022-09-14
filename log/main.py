from aiogram.utils import executor
from create_bot import dp, bot
from actions import greetings, mainMenu
from aiogram import types
async def on_start(_):
    print('go')

# ID-Chat = -659509581
greetings.greetingsBot(dp)
mainMenu.menu(dp)

"""
Мут
"""
@dp.message_handler()
async def test(message : types.Message):
    await bot.restrict_chat_member(message.chat.id, message.from_user.id, can_send_messages=False)


executor.start_polling(dp, skip_updates=True, on_startup=on_start)

# https://docs.aiogram.dev/en/latest/index.html