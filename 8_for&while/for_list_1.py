"""
列表推倒式：
[表达式 for 变量 in 列表]
或者
[表达式 for 变量 in 列表 if 条件]
"""
li = [1,2,3,4,5,6,7,8,9]
print([i**2 for i in li])
print([i for i in li if i>5])