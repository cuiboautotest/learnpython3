list1=[1,2,3,4,5]
list2=[7,8,9]
list=list1.extend(list2)#extend只是修改被扩展的序列
print(list)#返回的是None
print(list1)#改变了原来的序列

list3=list1+list2#注意拼接与extend方法的区别，连接会返回一个全新的列表
print(list3)