seasons_lt = ['winter', 'spring', 'summer', 'autumn']
month = int(input("Введите номер месяца: "))
if 3 <= month <= 5:
    print(seasons_lt[1])
elif 6 <= month <= 8:
    print(seasons_lt[2])
elif 9 <= month <= 11:
    print(seasons_lt[3])
elif month == 1 or month == 12 or month == 2:
    print(seasons_lt[0])
else:
    print("Ошибка")

seasons_dt = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите номер месяца: "))
if 3 <= month <= 5:
    print(seasons_dt.get(2))
elif 6 <= month <= 8:
    print(seasons_dt.get(3))
elif 9 <= month <= 11:
    print(seasons_dt.get(4))
elif month == 1 or month == 12 or month == 2:
    print(seasons_dt.get(1))
else:
    print("Ошибка")