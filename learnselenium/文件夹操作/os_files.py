#coding=utf-8
import os
#打印当前执行脚本所在目录
print(os.getcwd())
#当前目录创建文件夹
os.mkdir('./test1234')
#创建多级目录
os.makedirs('/test34/1/2/3')
