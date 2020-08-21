s="abccccdd"
dic={}
res=0
for i in s:
    dic[i]=dic.get(i,0)+1
#print(dic)
for k,v in dic.items():
    if dic[k]%2==0:
        res+=dic[k]
    elif dic[k]>1 and dic[k]%2==1:
        res+=dic[k+1]//2
    else:
        res
print(res)

