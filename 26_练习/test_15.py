'''

时间相关模块
'''
import time
import time
t=time.localtime()
print(t ) # 返回当前时间的九元组

print(time.time() ) # 常用，与1970-1-1 8:00之间的秒数，时间戳

print(time.mktime(t) ) # 把九元组时间转成时间戳

print(time.ctime() ) # 返回当前时间，参数是时间戳，常用
print(time.strftime("%Y-%m-%d") ) # 常用,年月日
print(time.strftime('%H:%M:%S'))#时分秒
print(time.strptime('2018-07-20', "%Y-%m-%d") ) # 返回九元组时间格式


###########################################
from datetime import datetime
from datetime import timedelta

datetime.today()  # 返回当前时间的datetime对象
datetime.now()  # 同上，可以用时区作参数
datetime.strptime('2018/06/30', '%Y/%m/%d')  # 返回datetime对象
dt = datetime.today()
datetime.ctime(dt)
datetime.strftime(dt, "%Y%m%d")

days = timedelta(days=90, hours=3)  # 常用
dt2 = dt + days
dt2.year
dt2.month
dt2.day
dt2.hour
