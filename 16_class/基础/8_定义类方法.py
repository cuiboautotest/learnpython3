class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())
'''
通过标记一个 @classmethod，该方法将绑定到 Person 类上，而非类的实例。类方法的第一个参数将传入类本身，通常将参数名命名为 cls，
上面的 cls.count 实际上相当于 Person.count。
'''