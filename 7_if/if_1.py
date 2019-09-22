"""
x 为 0-99 取一个数，y 为 0-199
取一个数,如果 x>y 则输出 x，
如果 x 等于 y 则输出 x+y，
否则输出y。
"""
import random
x = random.randrange(0,100)
y = random.randrange(0,200)
print(x,y) #打印x,y值
if x > y :
    print(x)
elif x == y:
    print(x+y)
else:
    print(y)
