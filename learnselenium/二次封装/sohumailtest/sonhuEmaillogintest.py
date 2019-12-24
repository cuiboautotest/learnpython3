#coding=utf-8
from time import sleep
from selenium import webdriver
#import sys
#sys.path.append('..')
from sohuEmailPublic import *
dr=webdriver.Chrome()

# L=SohuEmail(dr)                             #实例化类
# L.openUrl()                                 #调用封装的方法，打开网页
# L.login('15927536501@sohu.com','cuibo123456')       #输入账号和密码并登录
# L.logout()                                  #退出邮箱账号
# L.close_brower()                            #关闭浏览器
'''
简单快捷的办法
'''
L=SohuEmail(dr)
L.all_actions('15927536501@sohu.com','cuibo123456')#调用二次封装所有方法