def nod(n1, n2):
    big_number = max(n1, n2)
    small_number = min(n1, n2)
    for i in range(small_number, 0, -1):
        if small_number % i == 0 and big_number % i == 0:
            return i


def nok(n1, n2):
    big_number = max(n1, n2)
    small_number = min(n1, n2)
    result = big_number
    while not (result % big_number == 0 and result % small_number == 0):
        result += 1
    return result
