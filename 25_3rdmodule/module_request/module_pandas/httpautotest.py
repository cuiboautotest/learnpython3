#coding=utf-8
import pandas as pd
from class_request import *
df=pd.read_excel('./test_data.xlsx')#打开excel获取所有数据
#data=df.head()#默认读取前5行的数据
#print("获取到所有的值:\n{0}".format(data))#格式化输出
#print(df.values)
test_data=df.values#将数据存储到变量test_data,data是一个嵌套列表

'''
完成HTTP接口测试
'''

for item in test_data:
    print('目前正在执行的是{0}:{1}用例'.format(item[0],item[1]))

    f=HttpRequest()
    res=f.http_request_baidu(item[2],eval(item[3]),item[4])
    print('http执行的结果是：{0}'.format(res))
#单元测试
#自动化测试
#jenkins