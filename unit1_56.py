revenue = int(input('Размер выручки: '))
costs = int(input('Издержки:'))
if revenue > costs:
    print('Финансовый результат положительный')
    profit = (revenue - costs) / revenue
    employee = int(input('Количество сотрудников: '))
    profit_emp = (revenue - costs) / employee
    print('Прибыль в расчете на 1 сотрудника:' , round(profit_emp , 2))

else:
    print('Фирма несет убыток')

