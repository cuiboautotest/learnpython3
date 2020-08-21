s='a12cD12#$C2E'
L=[]
for i in s:
    if i.isupper()==True:
        L.append(i)
print(len(L))

#解法2
# count=0
# for i in s:
#     if i.isupper()==True:
#         count+=1
# print(count)