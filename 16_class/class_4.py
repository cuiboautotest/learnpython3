class BoyFriend(object):
    #类属性
    height=175
    money=20
    age=25
    name='周杰伦'

    '''
    定义类方法
    
    什么时候去定义类方法？
    1.如果你想直接通过类名.函数名调用
    2.方法跟属性没有直接的关联
    3.当有初始化函数可以直接定义为类方法
    '''
    #装饰器
    @classmethod
    def cooking(cls):#cooking用不到上面的类属性
        print('会做饭')

    def hiking(self):
        print('喜欢户外运动')

    def swimming(self):
        print('会游泳')

    def coding(self):
        print('会写代码')


bf=BoyFriend()#实例化类
bf.cooking()

BoyFriend.cooking()#cooking用不到属性，直接调用，不用实例化
print(BoyFriend.age)
