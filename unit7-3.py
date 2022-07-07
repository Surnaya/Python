class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.star = '*'

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return Cell(self.cell - other.cell)
        else:
            return None

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self,count):
        n = self.cell
        while n >0:
            for i in range(1, count+1):
                print(self.star, end='')
                n -= 1
                if n <= 0:
                    break
            print('\n', end='')

a = Cell(5)
b = Cell(3)
print(f'Количество ячеек клетки {a}')
print(f'Количество ячеек клетки {b}')
print(f'Результат сложения двух клеток - {a + b} ячеек')
print(f'Результат вычитания двух клеток - {a - b} ячейки')
print(f'Результат умножения двух клеток - {a * b} ячеек')
print(f'Результат деления двух клеток - {a / b} ячейка')

a.make_order(7)
b.make_order(3)