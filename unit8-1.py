class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def my_method(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Корректная дата'
                else:
                    return f'Некорректное значение даты'
            else:
                return f'Некорректное значение даты'
        else:
            return f'Некорректное значение даты'


print(Data.my_method('11 - 11 - 2011'))
print(Data.valid(1, 15, 2000))
print(Data.valid(12, 7, 2022))