def f1(x):
    if x <= 3:
        return x ** 2 - 3 * x + 9
    else:
        return 1 / (x ** 3 + 6)


def f2(x):
    if x <= 2:
        return x ** 2 + 4 * x + 5
    else:
        return 1 / (x ** 2 + 4 * x + 5)


def f3(x):
    if x > 3:
        return -3 * x + 9
    else:
        return (x ** 3) / (x ** 2 + 8)
