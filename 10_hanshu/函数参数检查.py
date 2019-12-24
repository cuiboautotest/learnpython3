def checkfunc(x):
    if not isinstance(x,(int,float)):#判断x是int或float
        raise TypeError('must be int or float ')
    if x>0:
        return x
    else:
        return -x

print(checkfunc(-1.0))
print(checkfunc(2.3))
print(checkfunc('abc'))

