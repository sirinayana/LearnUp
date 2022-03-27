n = int(input('Введите число: '))
result = 0
while n != 0:
    result += n
    n = int(input('Введите число: '))
print('Сумма введенных чисел равна', result)