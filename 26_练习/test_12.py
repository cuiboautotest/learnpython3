'''
列表方法
'''
alist = [1, 2, 3, 'bob', 'alice']
alist[0] = 10
print(alist)
alist[1:3] = [20, 30]
alist[2:2] = [22, 24, 26, 28]
alist.append(100)
alist.remove(24)  # 删除第一个24
print(alist.index('bob'))  # 返回下标
blist = alist.copy()  # 相当于blist = alist[:]
print(blist)
alist.insert(1, 15)  # 向下标为1的位置插入数字15
print(alist)
alist.pop()  # 默认弹出最后一项
print(alist)
alist.pop(2) # 弹出下标为2的项目
print(alist)
alist.pop(alist.index('bob'))
print(alist)
alist.sort()
alist.reverse()
alist.count(20)  # 统计20在列表中出现的次数
alist.clear()  # 清空
alist.append('new')
alist.extend('new')
alist.extend(['hello', 'world', 'hehe'])
print(alist)
