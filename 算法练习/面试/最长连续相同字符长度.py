s = "cc"
res=1
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
        res = max(count, res)
    else:
        count=1
print(res)