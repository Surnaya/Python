class ByZero:
    def __init__(self, divider1, divider2):
        self.divider1 = divider1
        self.divider2 = divider2

    @staticmethod
    def by_zero(divider1, divider2):
        try:
            return (divider1 / divider2)
        except:
            return (f"Ошибка деления на ноль")


print(ByZero.by_zero(12, 0))
print(ByZero.by_zero(120, 6))
