import psutil
import datetime
cpuinfo=psutil.cpu_times()
print(cpuinfo)
cpu_use=psutil.cpu_percent()#cpu利用率
print(cpu_use)

mem = psutil.virtual_memory()#内存利用率
print(mem)
print(mem.total)


##以linux时间格式返回，可以使用时间戳转换
start_time=psutil.boot_time()#系统开机时间
print(start_time)


#转换成自然时间格式

datetime.datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H: %M: %S")
