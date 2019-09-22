#coding=utf-8
import os
path='./test1.txt'
with open(path,'w')as f:
    f1=open(path,'w+')
    f1.write("welcome!\ncuibo!")
    f1=open(path,'r')
    print(f1.read())

#open(path,'w')
#os.rename('test1.txt','test2.txt') #重命名