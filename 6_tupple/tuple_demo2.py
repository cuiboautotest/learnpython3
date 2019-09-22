"""
元组操作,元组取值同列表一样，元组中的元素值是不允许修改的，
可以对元组进行连接组合
"""
tuple = ("a","xyz",[123],456)
print(tuple)
print(tuple[0])

tuple1 = (1000,)
print(tuple+tuple1)

#元组不能删除，但是可以删除整个
tuple3 = (1,2,3)
del tuple3
print(tuple3)