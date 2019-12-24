'''
列表内建函数，常用方法
'''


#删除列表
list = ["Google","cuibo",1999,2000,"last"]

del list[2]#删除索引
print(list)

list.append("cuibo123")#末尾加新元素
print(list)
print(len(list))

list.insert(1,'d')#在索引1位置插入d
print(list)
list.insert(2,[3,4,5])#列表中插入列表
print(list)

list.pop()#删除最后一个
print(list)

list.pop(-2)#index，-2代表删除倒数第二个
print(list)

list.reverse()#反转
print(list)

list.clear()#清空列表
print(list)
