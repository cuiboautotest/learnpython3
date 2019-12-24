class Student(object):
    def __init__(self,name,score):
        self.__name=name#私有属性双下划线
        self.__score=score

    def get_name(self):#定义实例方法，访问私有属性用get_
        return self.__name

    def get_socre(self):
        return self.__score

s=Student('cuibo',88)
#通过自定义方法访问私有属性
print(s.get_name())
print(s.get_socre())

#直接访问私有属性
print(s._Student__name)
print(s._Student__score)