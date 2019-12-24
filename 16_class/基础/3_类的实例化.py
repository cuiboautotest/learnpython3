class Flower(object):

    def __init__(self, name, color, height):#括号里的是实例属性
        self.name = name  # 实例属性
        self.color = color  #
        self.height = height
        print(self)#self返回的是类对象本身，相当于Flower()

f=Flower('玫瑰','红色',20)#实例化

print(f)
print(f.name)
print(f.color)
print(f.height)