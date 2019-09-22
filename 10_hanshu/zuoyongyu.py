"""
对于变量作用域，
变量的访问以 L（Local） –> E（Enclosing） –> G（Global） –>B（Built-in） 的规则查找，
即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，
再者去内建中找。
"""
#1.局部作用域
x = int(3.3)
x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print(x)
    inner()

outer()
#执行结果为 2，因为此时直接在函数 inner 内部找到了变量 x。


#2.闭包函数外的函数中
x = int(3.3)
x = 0
def outer():
    x = 1
    def inner():
        i = 2
        print(x)
    inner()

outer()
#因为在内部函数 inner 中找不到变量 x，继续去局部外的局部——函数 outer 中找，这时找到了，输出 1。


#3.全局作用域
x = int(3.3)
x = 0 #变量x以最新的值
def outer():
    o = 1
    def inner():
        i = 2
        print(x) #输出0
    inner()

outer()
#在局部（inner函数）、局部的局部（outer函数）都没找到变量 x，于是访问全局变量，此时找到了并输出。


#4.内建作用域
x = int(3.3) #内建函数，int（）将float型转换为整形
g = 0
def outer():
    o = 1
    def inner():
        i = 2
        print(x)
    inner()

outer()
#在局部（inner函数）、局部的局部（outer函数）以及全局变量中都没有找到变量x，于是访问内建变量，此时找到了并输出。