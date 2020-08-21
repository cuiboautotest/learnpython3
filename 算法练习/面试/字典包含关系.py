words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
res=0
from collections import Counter
c=Counter(chars)
print(c)
for word in words:
    word_counter=Counter(word)
    print(word_counter)
    for k in word_counter:
        if word_counter[k]>c[k]:
            break
    else:
        res+=len(word)
print(res)

