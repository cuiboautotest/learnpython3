l=[1,4,6,3,9,7]
l.sort()
print(l) #改变了原来列表的值

#如果需要一个排序好的副本，同时保持原有列表不变，怎么实现呢？不改变原列表进行排序
x=[2,5,7,3,6,1]
y=x[:]#通过分片将x复制给y
y.sort()
print(y)
print(x)

z = [3, 2, 8 ,0 , 1]
z.sort(reverse = True)#降序，false是升序
print (z) #[8, 3, 2, 1, 0]

#sorted方法,不改变原来的序列
s=[1,3,4,7,2,6,9]
t1=sorted(s)#排序
t2=sorted(s,reverse=True)
print(t1)
print(t2)
print(s)