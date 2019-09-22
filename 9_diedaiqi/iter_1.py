
"""
迭代器对象从集合的第一个元素开始访问，
直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
"""
list = [1,2,3,4]
it = iter(list)
#使用next函数输出
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))#超过4个抛出异常StopIteration
#上述代码可以循环实现
"""while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
"""



#迭代器对象可以使用常规for语句进行遍历：
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")



