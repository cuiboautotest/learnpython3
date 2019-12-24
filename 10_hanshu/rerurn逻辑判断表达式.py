def fun1():
    # 所有条件都为真，返回最后一个值
    return "21" and True


def fun2():
    # 检测所有表达式，直到遇到假为止，并返回假
    return 54 and 1 and True and 0


def fun3():
    # 遇到真，继续后面的判断，直到遇到假为止，如果遇见假直接返回，不再继续判断
    return 1 and True and False and 54 and 0


print(fun1())
print(fun2())
print(fun3())