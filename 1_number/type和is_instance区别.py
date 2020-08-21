a = 10
b = 10.1
c = '10'
d = True

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c) )# <class 'str'>
print(type(d)) # <class 'bool'>
print(isinstance(a, int))# True
print(isinstance(b, float)) # True
print(isinstance(c, str))# True
print(isinstance(d, bool)) # True
isinstance(a, (int, float, str, bool)) # True，只要是元祖中某一个类的实例就是True

