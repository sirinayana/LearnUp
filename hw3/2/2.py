list_of_words = input('Введите строку: ').lower().split()
set_of_words = set(list_of_words)
for c in set_of_words:
    print(c, list_of_words.count(c))
