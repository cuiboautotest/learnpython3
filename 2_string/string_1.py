#！/usr/bin/python3

print ("我叫 %s,今年 %d 岁!"%('小明', 10))


#字符串转化为列表
str = "cuibo123"
list = []
list = [i for i in str]
print(list)

#列表转化为字符
str1 = ','.join(list)
print(str1)