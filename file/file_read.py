#coding=utf-8
# 打开文本文件
fp = open('C:/Users/songlihui/PycharmProjects/test001keshanchu/test.txt', 'r')
# 使用readlines读取
lines = fp.readlines()
list = {}

for line in lines:
    # 将读取的每行内容过滤掉换行符,如果不加这个条件，输入的内容中将会添加换行符\n
    line = line.strip('\n')
    ss = line.split('=')  # 将每行内容根据=分割
    list[ss[0]] = ss[1]
fp.close()
print(list)


