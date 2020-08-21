def maopaopaixu(l):
    max = 0
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                print(l)
            max += 1
            print(max)
    return l


import random

l = []
for i in range(0, 10):
    l.append(random.randint(1, 10))
print(l)
maopaopaixu(l)

