class Employee:
    def __init__(self, age):
        self.age = age

    def get_info(self):
        print(f'должность: {self.occupation}\n'
              f'возраст: {self.age}\n')


class Nurse(Employee):
    def __init__(self, age):
        super().__init__(age)
        self.occupation = 'медсестра'


class Surgeon(Employee):
    def __init__(self, age):
        super().__init__(age)
        self.occupation = 'хирург'


n = Nurse(25)
s = Surgeon(40)

n.get_info()
s.get_info()
