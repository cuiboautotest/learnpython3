s = "aaiougrt"
indices = [4,0,2,6,7,3,1,5]
L=[]
for i in zip(s,indices):
    L.append(i)
res=sorted(L,key=lambda x:x[1])
s=''
for i in res:
    s+=i[0]
print(s)

