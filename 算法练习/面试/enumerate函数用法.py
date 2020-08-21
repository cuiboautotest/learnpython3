#打印列表的下标索引和对应数据
l=['one','two','three']
n=0
for i in l:
    print(n,l[n])
    n+=1

#list(enumerate(l))
#使用enumerate函数
seq=['one','two','three']
for i,element in enumerate(seq):
    print(i,element)
