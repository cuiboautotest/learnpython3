A=[4,2,5,7]
N=len(A)
ans=[None]*N
#偶数索引插入偶数，偶数索引第一个为0
t=0
for i,x in enumerate(A):
    if x%2==0:
        ans[t]=x
        t+=2
#print(res) [4,None,2,None]
#奇数索引插入奇数，奇数索引第一个为0
t=1
for i,x in enumerate(A):
    if x%2==1:
        res[t]=x
        t+=2
return res