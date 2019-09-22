import threading
def run1():
    while 1:
        if L1.acquire():
            # 如果第一把锁上锁了
            print('我是老大，我先运行')
            L2.release()
            # 释放第二把锁
def run2():
    while 1:
        if L2.acquire():
            # 如果第二把锁上锁了
            print('我是老二，我第二运行')
            L3.release()
            # 释放第三把锁

def run3():
    while 1:
        if L3.acquire():
            # 如果第三把锁上锁了
            print('我是老三，我最后运行')
            L1.release()
            # 释放第一把锁


t1 = threading.Thread(target=run1)
t2 = threading.Thread(target=run2)
t3 = threading.Thread(target=run3)

L1 = threading.Lock()
L2 = threading.Lock()
L3 = threading.Lock()
# 实例化三把锁

L2.acquire()
L3.acquire()

t1.start()
t2.start()
t3.start()
