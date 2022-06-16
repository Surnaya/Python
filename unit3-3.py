a = float(input('Введи число A: '))
b = float(input('Введи число B: '))
c = float(input('Введи число C: '))

def my_func(a, b, c):

    if a > b and b > c:
        return print(a + b)

    elif a > b and c > b:
        return print(a + c)

    else:
        return print(b + c)

my_func(a,b,c)