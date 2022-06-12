my_str = input("Введите строку: ")
new_str = []
numb = 1
for el in range(my_str.count(' ') + 1):
    new_str = my_str.split()
    if len(str(new_str)) <= 10:
        print(f" {numb} {new_str [el]}")
        numb += 1
    else:
        print(f" {numb} {new_str [el] [0:10]}")
        numb += 1