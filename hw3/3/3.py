a = [[3, -1, 1, 4, -2], [1, 1, 2, 15, -5], [5, 1, 2, 0, 3], [0, 0, 0, 1, 0], [1, 3, -5, -7, 2]]

for c in range(1, len(a), 2):
    print(f'В строке №{c + 1} наименьший элемент равен {min(a[c])}')