import sqlite3
from sign_up.funcs import sign_up

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
login VARCHAR (20),
password VARCHAR (20),
fio VARCHAR (128),
age INTEGER (3),
passport VARCHAR (16)
)""")
connect.commit()

data = sign_up()
cursor.execute("""INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?)""", data)
connect.commit()

connect.close()
