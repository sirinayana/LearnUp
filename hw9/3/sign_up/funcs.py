from string import ascii_letters, digits

__all__ = ['sign_up']


def check_login(login):
    CHARS = ascii_letters + digits + '_'

    if len(login) >= 20:
        raise TypeError("Длина логина должна быть менее 20 символов")

    if len(login.strip(CHARS)) != 0:
        raise TypeError("Логин может включать в себят только латинские буквы, цифры и знаки подчеркивания")


def check_password(password, confirm_password):
    CHARS = ascii_letters + digits + '_'

    if len(password) >= 20:
        raise TypeError("Длина пароля должна быть менее 20 символов")

    if len(password.strip(CHARS)) != 0:
        raise TypeError("Пароль может включать в себят только латинские буквы, цифры и знаки подчеркивания")

    if password != confirm_password:
        raise TypeError("Пароли не совпадают")


def check_fio(fio):
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()
    LETTERS = ascii_letters + S_RUS + S_RUS_UPPER + '-'

    f = fio.split()
    if len(f) != 3:
        raise TypeError("ФИО должно включать в себя фамилию, имя и отчество")

    for s in f:
        if len(s.strip(LETTERS)) != 0:
            raise TypeError("В ФИО можно использовать только буквенные символы и дефис")


def check_age(age):
    if not str(age).isdigit():
        raise TypeError("Возраст должен быть целым числом")

    age = int(age)
    if type(age) != int or age < 14 or age > 120:
        raise TypeError("Вам должно быть от 14 до 120 лет")


def check_passport(passport):
    s = passport.split()
    if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
        raise TypeError("Серия (4 цифры) и номер (6 цифр) должны быть разделены пробелами")

    for p in s:
        if not p.isdigit():
            raise TypeError("Серия и номер паспорта должны быть числами")


def sign_up():
    login = None
    while login is None:
        login = input("Введите логин: ")
        try:
            check_login(login)
        except Exception as w:
            print(w)
            login = None

    password = None
    while password is None:
        password = input("Введите пароль: ")
        second_password = input("Повторите пароль: ")
        try:
            check_password(password, second_password)
        except Exception as w:
            print(w)
            password = None

    fio = None
    while fio is None:
        fio = input("Введите имя, фамилию и отчество: ")
        try:
            check_fio(fio)
        except Exception as w:
            print(w)
            fio = None

    age = None
    while age is None:
        age = input("Введите возраст: ")
        try:
            check_age(age)
            age = int(age)
        except Exception as w:
            print(w)
            age = None

    passport = None
    while passport is None:
        passport = input("Введите серию и номер паспорта: ")
        try:
            check_passport(passport)
            passport = passport.strip()
        except Exception as w:
            print(w)
            passport = None

    return login, password, fio, age, passport
