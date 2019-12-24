import time
class GetTime(object):
    def get_system_time(self):
        print(time.time())#时间戳，获取的是从1970年到现在的间隔，单位是秒
        #print(time.localtime())
        new_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())#格式化时间
        print(new_time)

gettime=GetTime()
gettime.get_system_time()