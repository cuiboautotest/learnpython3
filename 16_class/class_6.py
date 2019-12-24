class BoyFriend:
    def __int__(self,name,weight,money,age):
        self.name=name
        self.weight=weight
        self.money=money
        self.age=age

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

    def swimming(self,long):
        print(self.name+'喜欢游泳，一次可以游{0}米'.format(long))


    def coding(self,args):
        self.swimming(long)
        return (self.name+'会写{0}代码'.format(args))


bf = BoyFriend('cuibo',180,10000,18)  # 实例化类

bf.swimming(100)
res=bf.coding(100)
print(res)