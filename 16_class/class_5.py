class BoyFriend(object):
    # 类属性
    height = 175
    money = 20
    age = 25
    name = '周杰伦'

    '''
    定义类方法

    什么时候去定义类方法？
    1.如果你想直接通过类名.函数名调用
    2.方法跟属性没有直接的关联
    3.当有初始化函数可以直接定义为类方法
    '''

    # 装饰器
    @classmethod
    def cooking(cls):  # cooking用不到上面的类属性
        print('会做饭')

    @staticmethod
    def hiking():#静态方法可以不用传参self
        print('喜欢户外运动')

    def swimming(self):
        print('会游泳')

    def coding(self):
        print('会写代码')


bf = BoyFriend()  # 实例化类
bf.hiking()


