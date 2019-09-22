#coding = utf-8
import time

def tuodi():
    print("我要拖地了")
    time.sleep(1)
    print("地拖完了")
def shaoshui():
    print("我要烧水了")
    time.sleep(6)
    print("水烧好了")
start_time= time.time()
tuodi()
shaoshui()
end_time = time.time()
print("总共耗时:{}".format(end_time-start_time))