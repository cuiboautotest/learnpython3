#coding=utf-8
import selenium
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_name('tj_login').click()
#driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys('narutoxiaobo')直接定位定位不到
'''
driver.find_element_by_class_name('tang-content').find_element_by_name('userName').send_keys('narutoxiaobo')#二次定位，先定位父亲div，再定位儿子username
driver.find_element_by_name('password').send_keys('qianqian910828')

driver.find_element_by_id('TANGRAM__PSP_10__submit').click()

'''

