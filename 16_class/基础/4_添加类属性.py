class Flower(object):
    height=20#类属性,
    def __init__(self, name, color,height):#括号里的是实例属性
        self.name = name
        self.color = color  # self返回的是类对象本身
        self.height = height #实例属性
        print(self)


print(Flower.height)#类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问：

f=Flower('玫瑰','红色',10)
print(f.height)#实例属性优先级高于类属性，所以输出结果是10

del f.height#删除
print(f.height)#删除实例属性自动调用类属性