#coding=utf-8
import gevent

def fun1():
    print("www.baidu.com")   # 第一步
    gevent.sleep(0)
    print("end the baidu.com")  # 第三步

def fun2():
    print("www.zhihu.com")   # 第二步
    gevent.sleep(0)
    print("end the zhihu.com")  # 第四步

gevent.joinall([
    gevent.spawn(fun1),
    gevent.spawn(fun2),
])