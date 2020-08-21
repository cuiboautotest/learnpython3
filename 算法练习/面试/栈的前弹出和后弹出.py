S="IDID"
n=len(S)
L=list(range(n+1))
res=[]
for i in S:
    if i=='I':
        res.append(L.pop(0))
    else:
        res.append(L.pop())
print(res+L)

