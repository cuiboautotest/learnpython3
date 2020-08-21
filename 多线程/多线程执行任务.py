#coding=utf-8
import threading
import os
import time

def send_dns(cmd):
    return os.system(cmd)

t1 = threading.Thread(target = send_dns,args=("nslookup _leboremote._tcp.local 10.91.3.79",))
print(os.getpid())
t2= threading.Thread(target = send_dns,args=("nslookup _leboremote._tcp.local 10.91.3.79",))
print(t2)
t1.start()
t2.start()
t1.join()
t2.join()

