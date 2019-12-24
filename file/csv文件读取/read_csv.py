import csv
import os
csvfile='test.csv'#单列数据
c=csv.reader(open(csvfile,'r'))
#print(type(c))
for cs in c:
    #print(type(cs[0]))
    #print(cs[0])#取出第一列
    #如果取出多行，要循环一下
    for i in range(len(cs)):
        print(cs[i])#无数据用空行




