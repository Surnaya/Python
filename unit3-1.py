a = float(input('Введи число A: '))
b = float(input('Введи число B: '))
if b > 0:
    def my_div(a, b):
        return a / b
    print(my_div(a, b))
else:
    print('На ноль делить нельзя')