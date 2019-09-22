#coding=utf-8
import threading

lock = threading.Lock()
lock.acquire()
lock.acquire()  # 产生死锁
lock.release()
lock.release()
print("end.")