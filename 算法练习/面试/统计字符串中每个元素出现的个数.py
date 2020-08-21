s='aabbcccddeffff'
# print(s.count('a'))统计多个
l=[]
d={}
for i in s:
    if i not in l:
        l.append(i)
        d.update({i:1})
    else:
        #d.get(i)+1
        #d.update({i:d.get(i)+1})
        d[i]=d.get(i)+1
print(d)
print(l)
