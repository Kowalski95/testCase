from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot1 = Bot(token=TOKEN)
dp = Dispatcher(bot1)


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def send_welcome(message: types.Message):
	    await message.answer("hi")


if __name__ == '__main__':
    executor.start_polling(dp)

# https://docs.aiogram.dev/en/latest/index.html