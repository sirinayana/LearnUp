class BankAccount:
    def __init__(self, name, surname, age, balance, salary):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__balance = balance
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_surname(self):
        return self.__surname

    def set_surname(self, value):
        self.__surname = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        self.__balance = value

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        self.__salary = value


account = BankAccount('Yana', 'Sirina', 18, 100000, 100000)

account.set_age(19)
account.set_salary(500000)
account.set_balance(100000000)

print(account.get_name())
print(account.get_surname())
print(account.get_age())
print(account.get_balance())
print(account.get_salary())
