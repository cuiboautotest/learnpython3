def function1(*args):
    print(args, type(args))#用来将参数打包成tuple给函数体调用

def function2(**kwargs):
    print(kwargs, type(kwargs))#打包关键字参数成dict给函数体调用

def function3(arg,*args,**kwargs):#顺序必须是固定的
    print(arg,args,kwargs)



function1(1)
function2(a=2)
function3(6,7,8,9,a=1,b=2,c=3)
function1()
function2()