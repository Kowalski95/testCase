from aiogram.utils import executor
from create_bot import dp
from actions.greetings import greetingsBot
async def on_start(_):
    print('go')

# ID-Chat = -659509581
greetingsBot(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_start)

# https://docs.aiogram.dev/en/latest/index.html