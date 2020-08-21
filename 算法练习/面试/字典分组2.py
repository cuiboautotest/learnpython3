strs=["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict
result_dict = {}
for i in strs:
    key = "".join(sorted(i))
    result_dict[key] = result_dict.get(key, []) + [i]
print(result_dict)
L=[]
for v in result_dict.values():
    L.append(v)
print(L)

