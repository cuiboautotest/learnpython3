l=[1,2,3,4,5]
def fn(x):
    return x**2
res=map(fn,l)
print(res)
print(list(res))


#结合lamda
data = list(range(10))
print(list(map(lambda x: x * x, data)))