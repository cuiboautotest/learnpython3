"""
字符串格式化
"""
from math import pi
#第一种，%占位符，需要指定数据类型，字符串用%s，整数用%d，%.f 表示保留小数位，多个被替换的按顺序提供，使用元祖。
str='hello %s , Today is 星期%d。'
value=('mike',3)#元组顺序要对上，数据类型要对上
print(str%value)
print('\n')

#对于字符串有%s,浮点型或者整数还有其他格式

str1=('圆周率是%.4f,保留小数点后%d位')
value1=(pi,4)#引用pi要从math模块导入，否则报错
print(pi,str1%value1)
print('\n')

#如果同时用到百分号，要用两个占位符
str2='成功率是10%%，如果%s首发成功率是%d%%'
value2=('Mike',50)
print(str2 % value2)
print('\n')

#重点！！！！！！！！format方法：用一对大括号 { } 表示要格式化参数，
# format方法主要注意三部分：{指定字段：转换标志+设置格式}

#按顺序传参
s1='{}，{}，{}是好朋友'
print(s1.format('小明','小红','小强'))


#按关键字传参
print('{a}{b}{c}'.format(a=1,c=2,b='cuibo'))


#按索引取参，可以混合关键字传参一起用
print('{0}成{s}于{1}{2}'.format('中国','1949年','10月1日',s='立'))#0对应元组第一个


'''
数字format格式方法：格式：format（数字，字符串形式的样式）
'''
print('设置小数点后位数：',format(0.05,'0.3f'))

print(format(0.05,'0.2%'))
# 5.00%

print(format(123456,','))
# 123,456 千分位逗号分隔

print(format(0.123,'>10.2f'))
# 10个字符长度内，右对齐，保留2位

print(format(0.12345,'0>10.2f'))
# 0000000.12 右对齐>补0，左对齐是<

print(format(0.12345,'@^10.4f'))
# @@0.1235@@ 中心对齐，补@

print(format(0.12345,'e'))
# 1.234500e-01

print(format(0.12345,'0.2e'))
# 1.23e-01

'''
字符串的format用法：格式为：'{：样式}'.format(值)
'''

print("hello, {}. you are {}?".format(name, age))



