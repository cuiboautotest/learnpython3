#coding=utf-8
class ClassA(object):
    string1='这是一个字符串'

    def instancefunc(self):
        print('这是一个实例方法')

    @classmethod
    def classfunc(cls):
        print('这是一个类方法。')
        print(cls)

    @staticmethod
    def staticfun():
        print('这是一个静态方法')


# 初始化一个ClassA的对象
test=ClassA()

#对象调用实例方法
test.instancefunc()

#对象调用类方法
test.classfunc()

#对象调用类变量
print(test.string1)

ClassA.instancefunc(test)  # 类调用实例方法，需要带参数，这里的test是一个对象参数
ClassA.instancefunc(ClassA) # 类调用实例方法，需要带参数，这里的ClassA是一个类参数
ClassA.staticfun() # 类调用静态方法
ClassA.classfunc()  # 类调用类方法

