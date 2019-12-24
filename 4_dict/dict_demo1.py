dict ={'abc':456,'age':7}
print(dict['abc'])#取值


dict['name']='cuibo'#添加新元素
print(dict)
print(len(dict))

dict['name']='cuibo123'#修改元素
print(dict)

del dict['name']#删除 键'name'
print(dict)
print(str(dict))

dict.pop('age')#删除 键'age'
print(dict)
