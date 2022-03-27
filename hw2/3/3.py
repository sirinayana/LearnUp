item = input('Введите товар для добавления в список покупок: ').strip()
list_of_items = []
while item.lower() != 'стоп':
    list_of_items.append(item)
    item = input('Введите товар для добавления в список (для остановки введите "стоп"): ').strip()
while len(list_of_items) != 0:
    print(list_of_items[0])
    list_of_items.pop(0)
