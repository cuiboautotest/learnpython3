a=[1,2]
b=[3,4]
res =[i for i in zip(a,b)]
print(res)

c='ab'
d='xyz'
res=[i for i in zip(c,d)]#传入参数的长度不同时，zip能自动以最短序列长度为准进行截取
print(res)