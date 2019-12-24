#coding=utf-8
from selenium import webdriver
from time import sleep
'''
二次封装一个登陆sohu邮箱操作，test_.py做测试
'''

class SohuEmail(object):
    def __init__(self,driver):
        self.dr=driver

    '''
    打开网页
    '''
    def openUrl(self):
        self.dr.get('https://mail.sohu.com/fe/#/login')
        sleep(3)
        self.dr.maximize_window()
        sleep(2)


    '''
    输入账号和密码并登陆，传入account，password两个参数
    '''
    def login(self,account,password):
        self.dr.find_element_by_xpath('//*[@id="theme"]/form/div[1]/div[1]/input').send_keys(account)
        self.dr.find_element_by_xpath('//*[@id="theme"]/form/div[2]/div[1]/input').send_keys(password)
        self.dr.find_element_by_xpath('//*[@id="theme"]/form/div[5]/input').click()

    '''
    退出账号
    '''
    def logout(self):
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="addSkinClass"]/div[1]/div[3]/ul/li[5]').click()


    '''
    关闭浏览器
    '''
    def close_browser(self):
        self.dr.quit()

    '''
    定义一个函数把前面的所有函数再次封装
    '''
    def all_actions(self,account,password):
        self.openUrl()
        self.login(account,password)
        self.logout()
        self.close_browser()
