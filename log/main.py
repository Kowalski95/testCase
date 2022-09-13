from aiogram import types
from aiogram.utils import executor
from create_bot import dp

async def on_start(_):
    print('go')



# @dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
# async def send_welcome(message: types.Message):



# import chat
# chat.create_chat(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_start)

# https://docs.aiogram.dev/en/latest/index.html