def tuodi():
    print('我要拖地了')
    time.sleep(1)
    print('我拖完了')

def shaoshui():
    print('我要烧水了')
    time.sleep(6)
    print('水烧开了')

start_time = time.time()
t1 = threading.Thread(target=heat_up_watrt)
t2 = threading.Thread(target=mop_floor)
t1.run()
t2.run()
# 注意这里不能加上join()
end_time = time.time()
print('总共耗时:{}'.format(end_time - start_time))

"""
两个子线程都用run()方法启动，但却是先运行t1.run()，运行完之后才按顺序运行t2.run()，两个线程都工作在主线程，没有启动新线程，因此，run()方法仅仅是普通函数调用。
"""
