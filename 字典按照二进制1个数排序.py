arr =[0,1,2,3,4,5,6,7,8]
dic={}
for i in arr:
    dic[i]=str(bin(i)).count('1')
print(dic)
res=sorted(dic.items(),key=lambda x:x[1],reverse=False)
print(res)
L=[]
for i in res:
    L.append(i[0])
print(L)