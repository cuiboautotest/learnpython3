#coding=utf-8
'''
在python中，对excel表格读，写，追加数据，用以下三个模块：
1、wlrd 读取excel表中的数据
2、xlwt 创建一个全新的excel文件,然后对这个文件进行写入内容以及保存。
3、xlutils 读入一个excel文件，然后进行修改或追加，不能操作xlsx，只能操作xls。
————————————————
版权声明：本文为CSDN博主「EastonLiu」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lmj19851117/article/details/78814721

table = data.sheets()[0]       #通过索引顺序获取
table = data.sheet_by_index(0) #通过索引顺序获取
table = data.sheet_by_name(u'Sheet1')#通过名称获取
'''
import xlrd
i