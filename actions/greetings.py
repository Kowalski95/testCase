from aiogram import types, Dispatcher
from base import base_greetings_chat
from log.create_bot import bot


# @dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def chat_welcome(message: types.Message):
    if message.new_chat_members.pop().id == bot.id:
        if await base_greetings_chat.get_chat_id(message.chat.id):
            pass
        else:
            await base_greetings_chat.add_chat(message.chat.id, True)
        await message.answer('Привет лохматые, с вами бот компот😜')

# @dp.message_handler(content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def chat_goodbye(message: types.Message):
    if message.left_chat_member.id == bot.id:
        await base_greetings_chat.del_chat(message.chat.id)

def greetingsBot(dp : Dispatcher ):
    dp.register_message_handler(chat_welcome, content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
    dp.register_message_handler(chat_goodbye, content_types=types.ContentTypes.LEFT_CHAT_MEMBER)