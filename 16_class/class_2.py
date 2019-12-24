#coding=utf-8
'''
男朋友类
身高：175 money：20W 会做饭 喜欢户外运动 会游泳 会写代码
姓名
年龄

'''

class BoyFriend(object):
    #类属性
    height=175
    money=20
    age=25
    name='周杰伦'

    '''
    定义类方法
    '''
    def cooking(self):
        print('会做饭')

    def hiking(self):
        print('喜欢户外运动')

    def swimming(self):
        print('会游泳')

    def coding(self):
        print('会写代码')


bf1=BoyFriend()#实例化类
print(bf1.age)#调用类属性
print(bf1.height)
bf1.coding()
bf1.cooking()

bf2=BoyFriend
bf2.coding(BoyFriend())#传入类名，与实例化功能一样
print(bf2.name)
