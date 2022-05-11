import sqlite3


def view_products(cursor):
    cursor.execute("SELECT id, product FROM products WHERE is_bought = 0")
    products = cursor.fetchall()
    for product in products:
        print(str(product[0]) + ' - ' + product[1])


with sqlite3.connect('product.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS products (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product VARCHAR(128) NOT NULL,
                   is_bought INTEGER(1) DEFAULT 0 NOT NULL)""")

    action = input("""Добро пожаловать в \"Список продуктов\"
    Введите:
    0 - выйти из программы
    1 - вывести список продуктов
    2 - добавить продукт
    3 - отметить продукт купленым
    Ваш ввод:  """)
    print()

    while action != '0':

        if action == '1':
            print("Список продуктов:")
            view_products(cur)
            print()

        elif action == '2':
            prod = input("Введите продукт: ")
            cur.execute("""INSERT INTO products (product)
                              VALUES (?)""", (prod,))
            print(f'Продукт "{prod}" добавлен')
            print()

        elif action == '3':
            view_products(cur)
            prod = int(input("Введите номер продукта, который вы хотите отметить купленным: "))
            name = cur.execute("SELECT product FROM products WHERE id = (?)", (prod,))
            name = cur.fetchone()[0]
            cur.execute("UPDATE products SET is_bought = 1 WHERE id = (?)", (prod,))
            print(f'Продукт "{name}" отмечен купленным')
            print()

        else:
            print('Неверный формат ввода')
            print()

        action = input("""Введите:
        0 - выйти из программы
        1 - вывести список продуктов
        2 - добавить продукт
        3 - отметить продукт купленым
        Ваш ввод:  """)
        print()

print("Спасибо, что воспользовались списком продуктов! До свидания!")
