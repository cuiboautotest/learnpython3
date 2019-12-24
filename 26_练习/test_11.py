'''
猜数
'''
import random
rannum=random.randint(1,10)#随机取整
print(rannum)
num=input('猜数字：')#输入的是个整形字符串，需要做格式转换
if int(num)>rannum:
    print('猜大了')
elif int(num)==rannum:
    print('猜对了')
else:
    print('猜小了')