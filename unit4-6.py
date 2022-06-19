from itertools import count
for i in count(4):
    if i > 7:
        break
    else:
        print(i)

from itertools import cycle

a = 0
for el in cycle("Hello!"):
    if a > 11:
        break
    print(el)
    a += 1

