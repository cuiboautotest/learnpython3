#对序列做累积运算
from functools import reduce
print(reduce(lambda x, y: x+y, [1,2,3,4,5]) ) # 使用 lambda 匿名函数


str1="hello"
print(reduce(lambda x,y:y+x,str1))
# 倒序输出 olleh