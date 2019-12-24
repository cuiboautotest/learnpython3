#coding=utf-8
#import sys
#sys.path.append('..')#不同文件夹之间的引用
from selenium import webdriver
from log import *
mylogger=Logger(logger='TestMylog').getlog()

class TestMylog(object):

    def print_log(self):
        driver = webdriver.Chrome()
        mylogger.info(u"打开浏览器")
        driver.maximize_window()
        mylogger.info(u"最大化浏览器窗口。")
        driver.implicitly_wait(8)

        driver.get("https://www.baidu.com")
        mylogger.info(u"打开百度首页。")
        time.sleep(1)
        mylogger.info(u"暂停一秒。")
        driver.quit()
        mylogger.info(u"关闭并退出浏览器。")

testlog=TestMylog()
testlog.print_log()

