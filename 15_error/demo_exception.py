"""
exception捕获任意异常
"""
s1 = 'hello'
try:
    int(s1)
except Exception as e:
    print(e)