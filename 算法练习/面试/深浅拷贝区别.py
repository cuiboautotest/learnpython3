import copy
lis = [12,39,10,5,11,66]  #一维列表
lis.append(['I','like','python'])  #添加 ['I','like','python']
li = copy.copy(lis)  #浅度拷贝
print(lis)  #输出：[12,39,10,5,11,66,['I','like','python']]   变成一个二维列表
lis[6][2] = 'you'
lis[1]=00
print(lis)  #[12,0,10,5,11,66,['I','like','you']]
print(li)   #[12,39,10,5,11,66,['I','like','you']]
'''
1.对于一维列表，当列表中的元素发生改变，copy和deepcopy都不会随着原列表的元素改变而发生任何改变。
2.对于二维列表，copy只拷贝最外层，当一个列表的二维列表中的元素发生改变，则另外一个列表也会随着发生改变；deepcopy内外层全部拷贝，当一个列表的二维列表中的元素发生改变，另一个列表不发生任何改变。
'''

#深度拷贝