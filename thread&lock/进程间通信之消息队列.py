#coding=utf-8
import queue
import time
import threading

q = queue.Queue(maxsize=5)

def t1(q):
    while 1:
        for i in range(10):
            q.put(i)

def t2(q):
    while not q.empty():
        print('队列中的数量：'+str(q.qsize()))#q.qsize()获取队列中数量
        print('取出值：'+str(q.get()))
        print('-----')
        time.sleep(0.1)
t1 = threading.Thread(target=t1,args=(q,))
t2 = threading.Thread(target=t2,args=(q,))
t1.start()
t2.start()