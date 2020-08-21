#不可变对象，整形，字符串，元组
a=1
b=1
c=2
print(id(a))
print(id(b))#相同的值的对象，在内存中则只有一个对象（一个地址）
print(id(c))

d=(1,2)
e=(1,2)
print(id(d))
print(id(e))


#可变对象
l=[1,2]
l1=[1,2]
print(id(l))
print(id(l1))#列表和字典均为可变对象
