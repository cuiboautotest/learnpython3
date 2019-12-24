class Person(object):
    address = 'Earth'#类属性
    def __init__(self, name):
        self.name = name


Person.address='China'#修改类属性

p=Person('cuibo')
print(p.address)
print(p.name)
print(Person.address)
