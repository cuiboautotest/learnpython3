def dec1(func):
    print("1111")

    def one():
        print("2222")
        func()
        print("3333")

    return one


def dec2(func):
    print("aaaa")

    def two():
        print("bbbb")
        func()
        print("cccc")
    return two

@dec1
@dec2
#相当于执行了test=dect1(dect2(test))，此时先执行dect2(test)，结果是输出aaaa、将func指向函数test、并返回函数two，然后执行dect1(two)，结果是输出1111、将func指向函数two、并返回函数one，然后进行赋值。
def test():
    print("test test")
test()
