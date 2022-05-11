import sqlite3

with sqlite3.connect('user.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    'name' VARCHAR(20),
    surname VARCHAR(40),
    phone VARCHAR(20),
    email VARCHAR(40)
    )""")

    cur.execute("""INSERT INTO users
    VALUES 
    (NULL, 'yanasirina', '123654', 'Yana', 'Sirina', '+79194970000', 'yana123@gmail.com'),
    (NULL, 'hello_world', 'hello_password', 'Hello', 'World', '+79999999999', 'helloeworld@yandex.ru'),
    (NULL, '$$$', 'ilikemoney', 'Ivan', 'Ivanov', '+79252525252', 'money@mail.ru')
    """)


