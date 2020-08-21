#给定字符串表达式，返回计算值
print(eval( '3 * 5' ))

#能使字符串本身的引号去掉，保留字符的原本属性。
a='123'
print(type(a))
b=eval(a)
print(b)
print(type(b))