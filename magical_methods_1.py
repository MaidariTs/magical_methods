"""
from dataclasses import dataclass

Декоратор dataclass автоматически добавляет специальные методы, такие как:
__init__() и __repr__() в определямые пользователем классы.
"""


class Car:
    # метод-конструктор класса __init__()
    def __init__(self, make, model, price):
        # super() позволяет получить доступ к унаследованным методам
        super().__init__()
        self.make = make
        self.model = model
        self.price = price

    # метод __str__() отвечает за строковое представление объекта
    # т.е. без него при печати будет выведен адрес в памяти
    # <__main__.Car object at 0x00000294C9CCBEB0>
    def __str__(self):
        return f'{self.make} {self.model} costs: {self.price}'

    # метод __repr__() отвечает за представление объекта в строковом формате
    def __repr__(self):
        return f'make = {self.make} model = {self.model} price = {self.price}'

    # метод __eq__() дает возможность сравнивать не адрес в памяти а value
    def __eq__(self, value):
        if not isinstance(value, Car):
            raise ValueError('Can`t compare bc of type mismatch')
        return (self.make == value.make and
                self.model == value.model and
                self.price == value.price)

    # метод сравнение больше или равно
    def __ge__(self, value):
        if not isinstance(value, Car):
            raise ValueError('Can`t compare bc of type mismatch')
        return self.price >= value.price

    # метод сравнение меньше
    def __lt__(self, value):
        if not isinstance(value, Car):
            raise ValueError('Can`t compare bc of type mismatch')
        return self.price < value.price


car1 = Car('Toyota', 'Camri', 7000)
car2 = Car('Opel', 'Mokka', 14000)
car3 = Car('Mazda', 'Q6', 10000)


# можем обратиться к методам напрямую
print(str(car1))
print(repr(car2))


# __eq__()
print(car2 == car3)


# __ge__(), __lt__()
print(car2 >= car1)
print(car2 < car3)


# после создания методов сравнения можно сортировать объекты
cars = [car1, car2, car3]
cars.sort()
print([car.model for car in cars])
