#coding = utf-8
import time
import threading
def tuodi():
    print("我要拖地了")
    time.sleep(1)
    print("地拖完了")
def shaoshui():
    print("我要烧水了")
    time.sleep(6)
    print("水烧好了")
start_time= time.time()
t1 = threading.Thread(target = shaoshui)#target后面跟函数名,生成一个子线程
t2 = threading.Thread(target = tuodi)
t1.start()#启动子线程
t2.start()
t1.join()
t2.join()#等到线程1与线程2执行完毕后再执行主线程
end_time = time.time()
print("总共耗时:{}".format(end_time-start_time))
"""
可以看到烧水等待的时候直接执行拖地任务，并且总共耗时为6秒，关于这里的start和jion都是固定的操作套路，记住这两个代词以后直接套用即可，需要注意的是多线程程序的执行顺序是不确定的。当执行到sleep语句时，线程将被阻塞（Blocked），到sleep结束后，线程进入就绪（Runnable）状态，等待调度的命令执行另一个子线程，线程调度将自行选择一个线程执行。

主线程：一个进程中至少有一个线程，并作为程序的入口，这个线程就是主线程(从一开始的代码执行到最后的打印出执行时间为主线程)

子线程：一个进程至少有一个主线程，其它线程称为子线程(拖地与烧水两个子线程)
"""