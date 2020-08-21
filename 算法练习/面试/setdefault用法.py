from collections import defaultdict
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
dic={}
for i in strs:
    dic.setdefault(''.join(sorted(i)), []).append(i)
print(dic)
res=[]
for v in dic.values():
    res.append(v)
print(res)