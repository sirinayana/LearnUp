class User:
    def __init__(self,  name: str = "", surname: str = "", year: int = 0, city: str = "", hobby: str = ""):
        self.name = name
        self.surname = surname
        self.year = year
        self.city = city
        self.hobby = hobby

    def print_info(self):
        print(f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Возраст: {2022 - self.year}\n'
              f'Город: {self.city}\n'
              f'Хобби: {self.hobby}\n')

    def set_name(self, name: str):
        self.name = name

    def set_surname(self, surname: str):
        self.surname = surname

    def set_city(self, city: str):
        self.city = city

    def set_year(self, year: int):
        self.year = year

    def set_hobby(self, hobby: str):
        self.hobby = hobby


# first task
user1, user2 = User(), User()
user1.name, user1.surname, user1.year, user1.city, user1.hobby = 'Yana', 'Sirina', 2002, 'Perm', 'taekwondo'
user2.name, user2.surname, user2.year, user2.city, user2.hobby = 'Ivan', 'Ivanov', 1990, 'Moscow', 'knitting'
print(f'Возраст пользователя {user1} - {2022 - user1.year}')
print(f'Возраст пользователя {user2} - {2022 - user2.year}')
print()


# second task
user3 = User('Sergey', 'Petrov', 2008, 'New York', 'tiktok')
user4 = User('Maria', 'Petrova', 1981, 'New York', 'instagram')
user3.print_info()
user4.print_info()


# third task
user5 = User()
print(user5.__dict__)
user5.set_name('Anna')
user5.set_surname('Ivanova')
user5.set_year(1999)
user5.set_city('Kazan')
user5.set_hobby('snowboarding')
print(user5.__dict__)

