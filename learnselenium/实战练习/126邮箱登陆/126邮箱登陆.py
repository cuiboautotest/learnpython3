#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.126.com')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id('switchAccountLogin').click()
#iframe 的ID是动态变化，因此需要用模糊定位元素，先用xpath定位，然后改写
iframe_id=driver.find_element_by_xpath("//*[starts-with(@id,'x-URS-iframe')]")
driver.switch_to.frame(iframe_id)
time.sleep(5)
class Account(object):

    def __init__(self,username,password):
        self.username=username
        self.password=password
        #self.driver=webdriver.Chrome()


    def do_login(self):
        driver.find_element_by_name('email').send_keys(self.username)
        driver.find_element_by_name('password').send_keys(self.password)
        driver.find_element_by_id('dologin').click()

admin1=Account('admin','123')
admin1.do_login()

