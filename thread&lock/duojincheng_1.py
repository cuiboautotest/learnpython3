#coding=utf-8
from multiprocessing import Process
import threading
import time

def work(name):
    print("Hello, %s" % name)


if __name__ == "__main__":
    for i in range(10):
        p = Process(target=work, args=("nick",))
        p.start()