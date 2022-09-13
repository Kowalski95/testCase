from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMgame(StatesGroup):
    start = State()
    game = State()




async def creat_new_chat(message : types.Message):
    await FSMgame.start.set()
    await message.answer('Всем привет!')

async def menu(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['new game'] = message.text
    await FSMgame.next()
    await message.answer('Некст')

async def close(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['game'] = message.text
    await message.answer('Финишь')
    await state.finish()


def create_chat(dp : Dispatcher):
    dp.register_message_handler(creat_new_chat, state=None)
    dp.register_message_handler(menu,commands=['go'], state=FSMgame.start)
    dp.register_message_handler(close,state=FSMgame.game)