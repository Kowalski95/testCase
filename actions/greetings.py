from aiogram import types, Dispatcher
from base import sql_base


# @dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def chat_welcome(message: types.Message):
    if message.new_chat_members.pop().id == 5480211404:
        if await sql_base.get_chat_id(message.chat.id):
            await sql_base.update_chat_stat(message.chat.id, 1)
        else:
            await sql_base.add_chat(message.chat.id, True)
        await message.answer('Привет лохматые, с вами бот компот😜')

# @dp.message_handler(content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def chat_goodbye(message: types.Message):
    if message.left_chat_member.id == 5480211404:
        await sql_base.update_chat_stat(message.chat.id, 0)

def greetingsBot(dp : Dispatcher ):
    dp.register_message_handler(chat_welcome, content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
    dp.register_message_handler(chat_goodbye, content_types=types.ContentTypes.LEFT_CHAT_MEMBER)