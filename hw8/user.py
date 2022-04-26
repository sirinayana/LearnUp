from string import ascii_letters, digits


class WrongLoginException(Exception):
    """Общий класс исключения логина"""


class WrongPasswordException(Exception):
    """Общий класс исключения пароля"""


class User:
    CHARS = ascii_letters + digits + '_'
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()
    LETTERS = ascii_letters + S_RUS + S_RUS_UPPER + '-'

    def __init__(self):
        self.__login = None
        self.__password = None
        self.__fio = None
        self.__age = None
        self.__passport = None

    @classmethod
    def check_login(cls, login):
        if type(login) != str:
            raise WrongLoginException("Логин должен быть строкой")

        if len(login) >= 20:
            raise WrongLoginException("Длина логина должна быть менее 20 символов")

        if len(login.strip(cls.CHARS)) != 0:
            raise WrongLoginException("Логин может включать в себят только латинские буквы, цифры и знаки подчеркивания")

    @classmethod
    def check_password(cls, password, confirm_password):
        if type(password) != str:
            raise WrongPasswordException("Пароль должен быть строкой")

        if len(password) >= 20:
            raise WrongPasswordException("Длина пароля должна быть менее 20 символов")

        if len(password.strip(cls.CHARS)) != 0:
            raise WrongPasswordException("Пароль может включать в себят только латинские буквы, цифры и знаки подчеркивания")

        if password != confirm_password:
            raise WrongPasswordException("Пароли не совпадают")

    @classmethod
    def check_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("ФИО должно включать в себя фамилию, имя и отчество")

        for s in f:
            if len(s.strip(cls.LETTERS)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")

    @classmethod
    def check_age(cls, age):
        if type(age) not in (str, int):
            raise TypeError("Возраст должен быть целым числом")

        if not str(age).isdigit():
            raise TypeError("Возраст должен быть целым числом")

        age = int(age)
        if type(age) != int or age < 14 or age > 120:
            raise TypeError("Вам должно быть от 14 до 120 лет")

    @classmethod
    def check_passport(cls, passport):
        if type(passport) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = passport.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    def set_login(self, login):
        self.check_login(login)
        self.__login = login

    def set_password(self, password, confirm_password):
        self.check_password(password, confirm_password)
        self.__password = password

    def set_fio(self, fio):
        self.check_fio(fio)
        self.__fio = fio

    def set_age(self, age):
        self.check_age(age)
        self.__age = age

    def set_passport(self, passport):
        self.check_passport(passport)
        self.__passport = passport

    def sign_up(self):
        while self.__login is None:
            login = input("Введите логин: ")
            try:
                self.set_login(login)
            except Exception as w:
                print(w)

        while self.__password is None:
            password = input("Введите пароль: ")
            confirm_password = input("Повторите пароль: ")
            try:
                self.set_password(password, confirm_password)
            except Exception as w:
                print(w)

        while self.__fio is None:
            fio = input("Введите ФИО: ")
            try:
                self.set_fio(fio)
            except Exception as w:
                print(w)

        while self.__age is None:
            age = input("Введите ваш возраст: ")
            try:
                self.set_age(age)
            except Exception as w:
                print(w)

        while self.__passport is None:
            passport = input("Введите номиер вашего паспорта: ")
            try:
                self.set_passport(passport)
            except Exception as w:
                print(w)


a = User()
a.sign_up()
print(a.__dict__)
