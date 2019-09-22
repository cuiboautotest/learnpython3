"""

你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

"""


# !/usr/bin/python3

# 计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
print(area(4, 5))