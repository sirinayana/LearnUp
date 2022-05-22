import tkinter as tk
from tkinter import messagebox


def new_line():
    with open("log.txt", "a", encoding="utf-8") as file:
        line = ent.get()
        file.write(line + "\n")
    ent.delete(0, tk.END)


def clear_file():
    with open("log.txt", "w", encoding="utf-8"):
        pass
    messagebox.showinfo("Внимание", "Файл был очищен")


def press_key(event):
    if event.char == "\r":
        new_line()


win = tk.Tk()
win.title("Запись данных в log.txt")
win.geometry("350x150")
win.resizable(False, False)

win.bind("<Key>", press_key)

lbl = tk.Label(win, text="Введите строку для ввода в файл:")
lbl.pack()

ent = tk.Entry(win)
ent.pack()

write = tk.Button(win, text="Записать", command=new_line)
write.pack()
clear = tk.Button(win, text="Очистить файл", command=clear_file)
clear.pack()

win.mainloop()
