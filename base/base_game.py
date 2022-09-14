import sqlite3

base = sqlite3.connect('base_game.db')
cur = base.cursor()

"""
CREATE TABLE - Создаем базу даннх для проверки наличия бота в чате
IF NOT EXISTS - Если база имееться пропускаем ее.
"""
base.execute('CREATE TABLE IF NOT EXISTS {}(chat_id PRIMARY KEY, user_id, role, stat)'.format('game'))
base.commit()

async def add_chat(chat_id, user_id):
    cur.execute('INSERT INTO game VALUES(?, ?, ?, ?)', (chat_id, user_id, '', 'True'))
    base.commit()

async def get_chat_stat(chat_id):
    schet = cur.execute('SELECT user_id FROM game WHERE chat_id ==?', (chat_id,)).fetchall()
    print(schet)




async def get_chat():
    r = cur.execute('SELECT * FROM chat').fetchall()
    print(r)