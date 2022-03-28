a, b, c, d = [int(input('Введите число: ')) for i in range(4)]

print(' ', *[i for i in range(c, d + 1)], sep='\t')

for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()
