#coding=utf-8
import threading
import time
class tuodi(threading.Thread):#threading.Thread类
    def __int__(self):
        super().__int__()

    def run(self):
        print('我要拖地了')
        time.sleep(1)
        print('地拖完了')

class shaoshui(threading.Thread):
    def __int__(self,name):#这里传入参数name，就是传入子线程名字
        super().__int__(name=name)

    def run(self):
        print('我要烧水了')
        print(self.name)
        print(threading.current_thread().name)#打印出当前子线程名字
        time.sleep(6)
        print('水烧开了')

start_time=time.time()
t1=tuodi()
t2=shaoshui()
t1.start()
t2.start()
t1.join()
t2.join()
end_time=time.time()
print('总共耗时：{}'.format(end_time-start_time))

