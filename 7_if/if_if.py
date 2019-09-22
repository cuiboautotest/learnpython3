#！/usr/bin/python3
#coding=utf-8
print("==========欢迎进入狗狗年龄对比系统==========")
while True:
    try:
        age = int(input("请输入你家狗狗得年龄："))
        print("")
        if age < 0:
            print("不可能")
        elif age ==1:
            print("相当于人类14岁！")
        elif age ==2:
            print("相当于人类22岁！")
        else:
            human = 22+(age-2)*5
            print("相当于人类：%d"%human)
            break #不加会一直循环下去

    except ValueError:
        print("输入不合法，请输入有效年龄")
###退出提示
input("点击 enter 键退出")