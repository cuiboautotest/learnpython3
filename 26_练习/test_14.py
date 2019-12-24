'''
计算千万相加时间

'''

import time
start=time.time()
sum=0
for i in range(1,10000000):
    sum+=i
end=time.time()
print(end-start)
print(sum)