class Foo(object):

    def bar(self):
        print('bar')

    @staticmethod
    def sta():#静态方法不需要传self参数
        print('123')

    @staticmethod
    def stat(a1,a2):
        print(a1,a2)

Foo.sta()#静态方法不需要实例化对象，直接通过类调用，相当于函数
Foo.stat('a','b')

'''
应用场景：
如果对象中需要保存一些值，执行某功能时，需要使用对象中的值 >>普通方法
不需要对象中的值，静态方法
'''