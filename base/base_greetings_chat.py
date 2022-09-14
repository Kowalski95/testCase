import sqlite3


base = sqlite3.connect('base.db')
cur = base.cursor()

"""
CREATE TABLE - Создаем базу даннх для проверки наличия бота в чате
IF NOT EXISTS - Если база имееться пропускаем ее.
"""
base.execute('CREATE TABLE IF NOT EXISTS {}(chat_id PRIMARY KEY, stat)'.format('chat'))
base.commit()

"""
Создаем чат в БД с ИД и задаем статус присутствия по ID_Чата и булевому значению
"""
async def add_chat(chat_id, stat):
    cur.execute('INSERT INTO chat VALUES(?, ?)', (chat_id, stat))
    base.commit()

"""
Удалить данные по ID_чата
"""
async def del_chat(chat_id):
    cur.execute('DELETE FROM chat WHERE chat_id == ?', (chat_id,))
    base.commit()

"""
Считываем статус бота по ID_Чата в группе и отправляем результат обратно
"""
async def get_chat_stat(chat_id):
    return cur.execute('SELECT stat FROM chat WHERE chat_id ==?', (chat_id,)).fetchone()[0]

"""
Проверка на наличие в БД ID_Чат
"""
async def get_chat_id(chat_id):
    r = cur.execute('SELECT chat_id FROM chat').fetchall()
    for scrol in r:
        if scrol[0] == chat_id:
            return True
        else:
            return False

"""
Обновить статус бота.
"""
async def update_chat_stat(chat_id, stat):
    cur.execute('UPDATE chat SET stat == ? WHERE chat_id == ?', (stat, chat_id))
    base.commit()

"""
Вывод БД в консоль
"""
async def get_chat():
    r = cur.execute('SELECT * FROM chat').fetchall()
    print(r)