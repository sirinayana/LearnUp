import functions

n = input(f"Выберете тему викторины\n"
          f"1-Автомобили\n"
          "2-Космос\n"
          f"3-Животные\n"
          f"Ваш ответ (введите число): ").strip()

while n not in ('1', '2', '3'):
    n = input('Неверный формат ввода. Необходимо ввести число от 1 до 3: ').strip()

print()

if n == '1':
    print('Тема викторины: Автомобили')
    result = functions.car()
    print()
    print('Число набранных баллов (из 3) =', result)

elif n == '2':
    print('Тема викторины: Космос')
    result = functions.space()
    print()
    print('Число набранных баллов (из 3) =', result)

else:
    print('Тема викторины: Животные')
    result = functions.animal()
    print()
    print('Число набранных баллов (из 3) =', result)
