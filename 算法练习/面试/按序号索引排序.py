arr = [37,12,28,9,100,56,80,5,12]
L=sorted(list(set(arr)))
dic={}
for i,v in enumerate(L):
    dic[v]=i+1
res=[]
for i in arr:
    res+=[dic[i]]
print(res)

