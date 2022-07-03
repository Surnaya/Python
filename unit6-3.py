class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())

a = Position('Ivan', 'Ivanov', 'engineer', 100000, 10000)
print(f'Full name: {a.get_full_name()}')
print(f'Position: {a.position()}')
print(f'Profit: {a.get_total_income()}')