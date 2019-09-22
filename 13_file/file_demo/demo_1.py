#coding=utf-8
import os
path=("./test.txt")
filename=open(path,'w')#如果存在该文件则进行覆盖，如果不存在，创建新的文件
print("当前路径：",os.path.realpath(path))#返回文件的真是路径，用到了os.path模块

print(filename.write("hello world！"))#先写入,write()返回字符串的长度
filename=open(path,'r+')#打开再读
print(filename.read())#读操作，如果跟了参数数字，代表读取多少个字符，不加参数代表读取全部

filename=open(path,'a')#在文件末尾追加新的内容
print(filename.write("welcome!"))
filename=open(path,'r+')
print(filename.read())

filename=open(path,'a')#在文件末尾追加新的内容
print(filename.write("\ncuibo!"))#追加文件如果在下一行前面加上换行符
filename=open(path,'r+')
print(filename.read())

filename=open(path,'r')
for line in filename:
    print("循环输出文件内容：",line)

filename.close()