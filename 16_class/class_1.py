class People:
    #定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁。"%(self.name,self.age))

#实例化类
p = People('cuibo',10,30)
p.speak()