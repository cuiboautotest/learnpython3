#filter 方法求出列表所有奇数并构造新列表filter(函数，列表)
a=[1,2,3,4,5,6,7,8,9,10]
l=list(filter((lambda x:x%2==1),a))
print(l)