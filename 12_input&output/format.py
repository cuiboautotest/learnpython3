"""
括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。

在括号中的数字用于指向传入对象在 format() 中的位置
"""

#使用位置参数
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))

#使用默认参数
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))


#使用关键字参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

#位置及关键字参数可以任意的结合:

print('{0},{1},{other}'.format('google','cuibo',other= 'taobao'))


#打印平方和立方表
#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
for x in range(1,10):
    print('{0:2d}{1:4d}{2:6d}'.format(x,x*x,x*x*x))
    #print(x,x*x,x*x*x,end=" ")