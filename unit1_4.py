number = int(input("Введите любое целое число:"))
a = number % 10
while a > 0:
    number = number // 10
    if number % 10 > a:
        a = number % 10
    else:
        print("Максимальное цифра:" , a)
        break
