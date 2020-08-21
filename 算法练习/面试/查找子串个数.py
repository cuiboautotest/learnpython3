words = ["leetcoder","leetcode","od","hamlet","am"]
res=[]
#先按照长度排
words=sorted(words,key=lambda x:len(x))
#words.sort()这个排序默认按照字母顺序排
print(words)
n=len(words)
for i in range(n):
    for j in range(i+1,n):
        if words[i] in words[j]:
            res.append(words[i])
print(list(set(res)))