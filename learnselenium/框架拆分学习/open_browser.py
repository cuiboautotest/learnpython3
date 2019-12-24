#coding=utf-8
from selenium import webdriver
class Driver(object):

    def __init__(self):
        self.browser=webdriver.Chrome()


    '''
    打开浏览器操作
    '''
    def open_browser(self):

        #窗口最大化
        self.browser.maximize_window()
        #打开地址链接
        url='http://www.baidu.com'#实际业务我们可以将其抽离出来，根据自己的需要，传入不同的url地址
        self.browser.get(url)
        return self.browser

    '''
    关闭浏览器操作
    '''
    def close_browser(self):
        self.browser.quit()



