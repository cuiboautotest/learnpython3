#不定长参数
"""
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
"""
def printinfor(arg1,*vartuple):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    print(vartuple)
#调用函数
printinfor(70,60,50)

print("如果在函数调用时没有指定参数，它就是一个空元组,我们也可以不向函数传递未命名的变量")


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)