my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for num,i in enumerate(my_list) if my_list[num-1] != my_list[num]]
print(new_list)
