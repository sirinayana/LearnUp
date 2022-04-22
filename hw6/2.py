from math import pi


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        self.__p = self.perimeter() / 2
        return (self.__p * (self.__p - self.a) * (self.__p - self.b) * (self.__p - self.c)) ** 0.5


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * pi * self.r

    def area(self):
        return pi * self.r ** 2
    

figures = [Rectangle(2, 4),
           Rectangle(10, 20),
           Circle(3),
           Triangle(3, 4, 5),
           Circle(1),
           Rectangle(5, 7),
           Triangle(5, 12, 13)]

for figure in figures:
    print(figure.perimeter())
    print(figure.area())
    print()
