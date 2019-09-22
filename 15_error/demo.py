"""
未捕获异常，仍然正常报错
"""
s1 = 'hello'
try :
    int(s1)
except IndexError as e:
    print(e)
else:
    print("没有异常")

