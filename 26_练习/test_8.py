'''
元组基础

元组与列表基本上是一样的，只是元组不可变，列表可变
'''

atuple = (10, 20, 30, 'bob', 'alice', [1, 2, 3])
print(len(atuple))
10 in atuple
print(atuple[2])
print(atuple[3:5])
# atuple[-1] = 100  # 错误，元组是不可变的

