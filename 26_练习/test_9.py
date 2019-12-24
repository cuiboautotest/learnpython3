'''
字典基础
如何统计数组中出现次数最多的数据
'''
a=['a','b','a','c','a','c']
#set集合去重
duixiang=set(a)
print(duixiang)
#保存为dict，一一对应
dict={}
for i in duixiang:
    dict[i]=a.count(i)
print(dict)
#对字典按照value排序
a=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(a)