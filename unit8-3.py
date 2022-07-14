class Number:
    def __init__(self, my_list):
        self.my_list = []

    def my_numb(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Список - {self.my_list} \n ')
            except:
                print(f"Введено недопустимое значение")
                y_n = input(f'Попробовать еще раз? Y/N ')

                if y_n == 'Y' or y_n == 'y':
                    print(try_except.my_num())
                elif y_n == 'N' or y_n == 'n':
                    return f'Выход'
                else:
                    return f'Выход'

try_except = Number(1)
print(try_except.my_numb())