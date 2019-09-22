import time
def decorator(func):
    def wrapper(*args):#*args为可变参数
        print(time.time())
        func(*args)
    return wrapper
@decorator
def f1(func_name):
    print('this is a function'+func_name)

@decorator
def f2(func_name1,func_name2):
    print('this is a function'+func_name1)
    print('this is a function'+func_name2)

f1('test1')
f2('test2','test3')