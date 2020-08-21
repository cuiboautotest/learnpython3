l1=["dixyp","uq","q","KFC"]
l2=["yl","fjugc","rlni","dixyp","uq","q","KFC"]
#l2=["Shogun","Tapioca Express","Burger King","KFC"]
#l2=["KFC","Shogun","Burger King"]
s=set(l1)&set(l2)
print(s)#{'Burger King', 'Shogun', 'KFC'}
#他们共同喜爱且具有最小索引和
dic={}
for i in s:
    dic[i]=l1.index(i)+l2.index(i)
dic1=sorted(dic.items(),key=lambda x:x[1],reverse=False)
print(dic1)
#先找到最小索引和的值
index=dic1[0][1]
print('index:%d'%index)
L=[]
for k in dic:
    if dic[k]==index:
        L.append(k)
print(L)


