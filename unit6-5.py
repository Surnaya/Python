class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. Отрисовка ручкой')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. Отрисовка карандашом')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки. Отрисовка маркером')

a = Pen('Ручка')
b = Pencil('Карандаш')
c = Handle('Маркер')
a.draw()
b.draw()
c.draw()
