import hashlib
import tkinter
import sqlite3
from tkinter import messagebox

connect = sqlite3.connect("data.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
login VARCHAR(64) NOT NULL UNIQUE,
password VARCHAR(64) NOT NULL)""")


def register():
    login = entry_login.get().strip()
    password = entry_password.get()
    password_db = password_sha256(password)
    cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password_db))
    connect.commit()
    messagebox.showinfo("Регистрация", "Пользователь " + login + " успешно зарегистрирован!")


def auth_window():
    def authorize():
        login = entry_login_auth.get().strip()
        password = entry_password_auth.get()
        password_db = password_sha256(password)
        cursor.execute("SELECT login, password FROM users WHERE login = ? AND password = ?", (login, password_db))
        if cursor.fetchone():
            messagebox.showinfo("Авторизация", "Добро пожаловать!")
        else:
            messagebox.showerror("Авторизация", "Неверно введен логин или пароль")


    auth = tkinter.Toplevel()
    auth.geometry("300x300")
    auth.title("Авторизация")
    auth.resizable(0, 0)

    label_main = tkinter.Label(auth, text="Авторизация", font='Calibri 20')
    label_main.place(x=20, y=20)

    label_login = tkinter.Label(auth, text="Логин", font="Calibri 14")
    label_login.place(x=20, y=80)
    entry_login_auth = tkinter.Entry(auth, width=14, font="Calibri 14")
    entry_login_auth.place(x=100, y=80)

    label_password = tkinter.Label(auth, text="Пароль", font="Calibri 14")
    label_password.place(x=20, y=140)
    entry_password_auth = tkinter.Entry(auth, width=14, font="Calibri 14")
    entry_password_auth.place(x=100, y=140)

    button_authorize = tkinter.Button(auth, text="Войти", font="Calibri 16", command=authorize)
    button_authorize.place(x=20, y=250)


def password_sha256(user_password):
    salt = 'neverknow'
    password = bytes(user_password + salt, 'utf-8')
    password_hash = hashlib.sha256(password)
    return password_hash.hexdigest()


root = tkinter.Tk()
root.geometry("300x300")
root.title("Регистрация")
root.resizable(0, 0)

label_main = tkinter.Label(text="Регистрация", font='Calibri 20')
label_main.place(x=20, y=20)

label_login = tkinter.Label(text="Логин", font="Calibri 14")
label_login.place(x=20, y=80)
entry_login = tkinter.Entry(width=14, font="Calibri 14")
entry_login.place(x=100, y=80)

label_password = tkinter.Label(text="Пароль", font="Calibri 14")
label_password.place(x=20, y=140)
entry_password = tkinter.Entry(width=14, font="Calibri 14")
entry_password.place(x=100, y=140)

button_register = tkinter.Button(text="Зарегистрироваться", font="Calibri 16", command=register)
button_register.place(x=20, y=200)
button_authorize = tkinter.Button(text="Войти", font="Calibri 16", command=auth_window)
button_authorize.place(x=20, y=250)

root.mainloop()
