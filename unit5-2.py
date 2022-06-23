f = open('file2.txt')
line = 0
for i in f:
    line += 1

    flag = 0
    words: int = 0
    for j in i:
        if j != ' ' and flag == 0:
            words += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i,len(i),'симв.',words,'сл.')

print(line,'стр.')
f.close()