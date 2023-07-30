class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Устройство: {self.name}, цена: {self.price}"

class Printer(Equipment):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        if color not in ['Черно-белый', 'Цветной']:
            raise ValueError ('Некорректный ввод параметра')
        else:
            self.color = color

    def print(self):
        return f'принтер {self.name}'

class Scanner(Equipment):
    def __init__(self, name, price):
        super().__init__(name, price)

    def scan(self):
        return f'сканнер {self.name}'

class Xerox(Equipment):
    def __init__(self, name, price):
        super().__init__(name, price)

    def xerox(self):
        return f'ксерокс {self.name}'

a = Printer('HP', 120, 'Цветной')
b = Scanner('Canon', 150)
c = Xerox('Xerox', 200)
print(a.print())
print(b.scan())
print(c.xerox())