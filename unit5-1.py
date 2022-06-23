my_file = input('Файл:')
f = open(my_file,'w')
while True:
    s = input()
    if s == ' ':
        break
    f.write(s +'\n')
f.close()