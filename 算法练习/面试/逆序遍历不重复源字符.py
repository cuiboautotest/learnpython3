s='12233455'
l=[]
for i in s[::-1]:
    if i not in l:
        l.append(i)
print(l)
print("".join(l))