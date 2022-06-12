number = int(input("Введите любое целое число:"))
a = number % 10
while a > 0:
    number = number // 10
    if number % 10 > a:
        a = number % 10
    else number = number // 10:
        
        print("Максимальное цифра:" , a)
        break

