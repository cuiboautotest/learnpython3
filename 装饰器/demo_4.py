import time
def decorator(func):
    def wrapper(*args,**kwargs):#*args为可变参数,**kw为关键字参数，可任意命名
        print(time.time())
        func(*args,**kwargs)
    return wrapper
@decorator
def f1(func_name):
    print('this is a function'+func_name)

@decorator
def f2(func_name1,func_name2,**kw):
    print('this is a function'+func_name1)
    print('this is a function'+func_name2)
    print(kw)

f1('test1')
f2('test2','test3',a=1,b=2,c='123')