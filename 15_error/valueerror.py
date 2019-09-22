#coding=utf-8
"""
try语句按照如下方式工作；

首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
"""


while True:
        try:
            x = int(input("Please enter a number: "))
            print("您输入的数字是:",x)
            break#如果输入数字则跳出循环
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")