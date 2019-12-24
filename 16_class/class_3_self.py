class BoyFriend(object):
    #类属性
    height=175
    money=20
    age=25
    name='周杰伦'

    '''
    定义类方法
    '''
    def cooking(self):#self其实就是实例本身,通过打印可以看出来，这是为了区别类函数与普通函数区别
        print(self)
        print('会做饭')

    def hiking(self):
        print('喜欢户外运动')

    def swimming(self):
        print('会游泳')

    def coding(self):
        print('会写代码')


bf1=BoyFriend()#实例化类
print(bf1)#发现打印结果跟print(self)一样
print(bf1.age)#调用类属性
print(bf1.height)
bf1.coding()
bf1.cooking()