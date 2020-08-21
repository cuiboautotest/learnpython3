import time,threading

def loop():
    print('thread %s is running'%threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print('thread%s>>%s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended'%threading.current_thread().name)

print('thread %s is running...'%threading.current_thread().name)
#子线程名LoopThread,默认均会启一个主线程，主线程名MainThread
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s is ended...'%threading.current_thread().name)