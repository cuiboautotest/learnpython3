#-*- coding=UTF-8 -*-

print('装饰器作用：%s'%'用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能')

#基础平台提供的功能
def f1():
    print('f1')

def f2():
    print('f2')

def f3():
    print('f3')

def f4():
    print('f4')

#A部门调用平台功能
f1()
f2()
f3()
f4()

#B部门调用平台功能
f1()
f2()
f3()
f4()

#每个步骤增加需求增加验证功能

#定义装饰器函数
def w1(func):
    def inner():
        #验证1
        #验证2
        #验证3
        return  func()
    return inner

@w1
def f1():
    print('试用装饰器输出f1')

@w1
def f2():
    print('使用装饰器输出f2')

@w1
def f3():
    print('使用装饰器输出f3')

@w1
def f4():
    print('试用装饰器输出f4')
f1()
f2()
f3()
f4()




