tup = (4, 6, 7,8, 9, 10 ,0)
tup = list(tup)#将元组转化为列表
print(tup)
print()

list2 = ['谁', '说', '元', '组', '不', '能', '改']
for i in range(7):
    tup[i] = list2[i]#用列表赋值
print(tup)