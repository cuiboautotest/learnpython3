import time
"""
def func():
    start_time=time.time()
    print('hello world')
    time.sleep(1)
    print('hello world')
    end_time=time.time()
    msec=end_time-start_time
    print('time is %d ms'%msec)
"""
def deco(func):#把函数当作参数传入
    start_time=time.time()
    func()
    end_time = time.time()
    msec = end_time - start_time
    print('time is %d ms' % msec)

def func():
    print('hello')
    time.sleep(1)
    print('world!')

if __name_=='__main__':
    f=func
    deco(f)#只有把func()或者f()作为参数执行，新加入功能才会生效
    print(f.__name__)

