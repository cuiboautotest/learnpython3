#coding=utf-8
"""
RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的锁。
"""
import threading

rlock = threading.RLock()
rlock.acquire()
rlock.acquire()  # 在同一线程内，程序不会堵塞。
rlock.release()
rlock.release()
print("end.")