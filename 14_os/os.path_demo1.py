import os
path='E:/test.py'
print(os.path.split(path))#以路径最后一个'/'为分隔，分隔路径与文件名。若路径中无文件名，则输出路径与空文件名。通过元组形式返回字符串
a=os.path.split(path)[0]
print(a)
b=os.path.split(path)[1]
print(b)
path1=os.path.join(a,b)#os.path.join(path,name):连接目录与文件名或目录
print(path1)

#os.path.dirname(path)#返回文件路径

