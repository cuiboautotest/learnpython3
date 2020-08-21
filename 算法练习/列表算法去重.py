l=[1,2,2,4,8,8,10]
L=[]
for i in l:
    print(i)
    if i not in L:
        L.append(i)
print(L)