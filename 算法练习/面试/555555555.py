s = "covid2019"
l1 = []
l2 = []
res = ''
for i in s:
    if i.isdigit():
        l1.append(i)
    else:
        l2.append(i)
for i in zip(l1,l2):
    res+=i[0]+i[1]
print(res)