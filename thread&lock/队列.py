import queue
import threading

que = queue.Queue(10)


def s(i):
    que.put(i)
    # print("size:", que.qsize())


def x(i):
    g = que.get(i)
    print("get:", g)


for i in range(1, 13):
    t = threading.Thread(target=s, args=(i,))
    t.start()

for i in range(1, 11):
    t = threading.Thread(target=x, args=(i,))
    t.start()

print("size:", que.qsize())