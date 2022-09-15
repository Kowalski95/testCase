from log.create_bot import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
# from base import base_game

asd = types.InlineKeyboardMarkup()
asd.add(types.InlineKeyboardButton(text='Присоедениться', url='https://t.me/testKukSasBot'))


class Game(StatesGroup):
    new_game = State()


async def register_game(message : types.Message):
    if message.chat.type == "private":
        await message.answer('Данная команда работает только в чате')
    else:
        await message.answer('Ведеться набор игроков',reply_markup=asd)
        await Game.new_game.set()


async def load_uzer(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        print(message.chat.id)
        print(message.bot.id)
        print(message.chat.type)
    async with state.proxy() as text:
        text = 1
    await Game.new_game.set()


def menu(dp : Dispatcher):
    dp.register_message_handler(register_game, commands=['game'], state=None)
    dp.register_message_handler(load_uzer, commands=['start'], state=Game.new_game)

