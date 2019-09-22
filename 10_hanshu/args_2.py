#两个星号 ** 的参数会以字典的形式导入
# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# 调用printinfo 函数
printinfo(1, a=2, b=3)

#def(**kwargs) 把N个关键字参数转化为字典:
def func(country,province,**kwargs):
    print(country,province,kwargs)

func("china","sichuan",city="chengdu",section = "jingjiang")


