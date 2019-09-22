#repr()： 产生一个解释器易读的表达形式,参数可以是任何对象
s = "cuibo"
print(repr(s))

print(repr(('x', "y", ('Google', 'Runoob'))))

#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello,cuibo\n'
hellos = repr(hello)
print(hellos)