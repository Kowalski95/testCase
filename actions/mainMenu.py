from log.create_bot import bot
from aiogram import types, Dispatcher
from base import base_game


# @dp.message_handler(commands=['game'])
async def game(message : types.Message):
    await base_game.add_chat(message.chat.id, message.from_user.id)
    await base_game.get_chat()


def menu(dp : Dispatcher):
    dp.register_message_handler(game, commands=['game'])
