#获取本周/本月/上月最后一天
import time
import datetime

#本周
today = datetime.date.today()
print(today)
sunday = today + datetime.timedelta(6 - today.weekday())#weekday()函数返回的是当前日期所在的星期数
print(sunday)

#本月
import calendar
today = datetime.date.today()
_,last_day_num = calendar.monthrange(today.year, today.month)
last_day = datetime.date(today.year, today.month, last_day_num)
print(last_day)



#获取上个月的最后一天(可能跨年)
today = datetime.date.today()
first = datetime.date(day=1, month=today.month, year=today.year)
lastMonth = first - datetime.timedelta(days=1)
print(lastMonth)

