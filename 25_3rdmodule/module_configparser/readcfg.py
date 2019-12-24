import configparser
import os
curpath=os.path.dirname(os.path.realpath(__file__))#所在文件夹的绝对路径
print(curpath)
cfgpath=os.path.join(curpath,'cfg.ini')#拼接成文件所在路径
print(cfgpath)

#实例化对象--创建管理对象
conf=configparser.ConfigParser()

#读ini文件
conf.read(cfgpath,encoding='utf-8')#配置文件含有中文注释需要加encoding
#conf.read(cfgpath)#pyhton2写法

#获取所有的section
sections=conf.sections()
print(sections)

items=conf.items('email_163')
print(items)#返回的是一个列表

print(items[0][1])#取值