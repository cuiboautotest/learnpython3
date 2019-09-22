import time
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper
@decorator
def f1():
    print('this is a function')
f1()