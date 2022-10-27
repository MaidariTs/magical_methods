class Car:
    def __init__(self, make, model, price):
        super().__init__()
        self.make = make
        self.model = model
        self.price = price
        self._discount = 0.25

    # вызов объекта как функцию
    def __call__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
        self._discount = 0.25

    # метод будет вызываться когда будет происходить попытка доступа к атрибуту
    # например, когда вызывается атрибут "price" - применяем скидку 25%
    def __getattribute__(self, name):
        if name == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__('_discount')
            return p - (p * d)
        return super().__getattribute__(name)

    # установить атрибут
    # например, если будет вызываться атрибут "price" - проверяем на float
    def __setattr__(self, name, value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError('Price must be float!')
        return super().__setattr__(name, value)

    # сделать что-то, если вызван несуществующий атрибут
    def __getattr__(self, name):
        return name + ' not implemented'

    def __repr__(self):
        return f'make = {self.make} model = {self.model} price = {self.price}'


car1 = Car('Toyota', 'Camri', 7000.5)
car2 = Car('Opel', 'Mokka', float(14000))
car3 = Car('Mazda', 'Q6', float(10000))

# __getattribute__() применит скидку 25%, __setattr__() проверит на float
print(car1)

# __dict__ преобразует в словарь
car1('Porsche', 'Carrera', 67700.00)
print(car1.__dict__)

# # __getattr__(), атрибут engine не существует:
# # engine not implemented
# print(car1.engine)

# # __call__() вызовет объект ка функцию
# car1 = ('Wv', 'Passat', 4500.69)
# print(car1)
