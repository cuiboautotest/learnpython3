#eval，将字符串转为eval
a=eval('3+2.5')
print(a,type(a))
b=eval('3+5')
print(b,type(b))

while True:
    result = eval(input("请输入表达式："))#如3+2-6
    print("结果：",result)