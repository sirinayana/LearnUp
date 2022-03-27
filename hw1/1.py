from datetime import datetime

year = datetime.today().year

name = input('Введите ваше имя: ').strip()
surname = input('Введите вашу фамилию: ').strip()
year_of_birth = int(input('Введите год рождения: '))
city = input('Введите город проживания: ').strip()
hobby = input('Введите ваше хобби: ').strip()
occupation = input('Введите вашу профессию: ').strip()
info = input('Введите дополнительную информацию о себе: ').strip()

print()
print('Обрабатываю информацию…')
print()
print('Имя пользователя:', name)
print('Фамилия пользователя:', surname)
print('Возраст пользователя:', year - year_of_birth)
print('Город пользователя:', city)
print('Хобби пользователя:', hobby)
print('Профессия пользователя', occupation)
print('Дополнительная информация о пользователя:', info)
