#coding=utf-8
#Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。
# 线程首先acquire一个条件变量，然后判断一些条件。
# 如果条件不满足则wait；
# 如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，
# 其他处于wait状态的线程接到通知后会重新判断条件。不断的重复这一过程，从而解决复杂的同步问题。
import threading
import time


def consumer(cond):
    with cond:
        print("consumer before wait")
        cond.wait()
        print("consumer after wait")


def producer(cond):
    with cond:
        print("producer before notifyAll")
        cond.notifyAll()
        print("producer after notifyAll")


condition = threading.Condition()
c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
c2 = threading.Thread(name="c2", target=consumer, args=(condition,))

p = threading.Thread(name="p", target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

# consumer()线程要等待producer()设置了Condition之后才能继续。