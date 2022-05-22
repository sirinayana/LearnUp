with open("log.txt", "a", encoding="utf-8") as file:
    line = input("Введите строку для ввода в файл (чтобы закончить введите \"off\"): ")
    while line != "off":
        file.write(line + '\n')
        line = input("Введите строку для ввода в файл (чтобы закончить введите \"off\"): ")
