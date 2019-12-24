class Person(object):

    def __init__(self,name):
        self.name=name
        self._title='Mr'
        self.__job='student'

p=Person('Bob')
print(p.name)
print(p.title)#单下划线也不能访问
print(p.job)#双下划线不能访问