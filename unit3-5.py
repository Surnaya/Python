def my_sum():
    sum_end = 0
    condition = False
    while condition == False:
        number = input('Введите числа: ').split()

        result = 0
        for el in range(len(number)):
            if number[el] == 'x':
                condition = True
                break
            else:
                result = result + int(number[el])
        sum_end = sum_end + result
        print(f'Сумма {sum_end}')
    print(f'Процесс завершен. Сумма: {sum_end}')


my_sum()