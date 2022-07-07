from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def expense(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 2 + 0.3


a = Coat(48)
b = Suit(1.76)
c = a.expense + b.expense
print(f'Размер {a}')
print(f'Рост {b}')
print(f'Расход ткани на пальто {a.expense}')
print(f'Расход ткани на костюм {b.expense}')
print(f'Общий расход ткани {round(c)}')
