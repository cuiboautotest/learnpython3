#coding=utf-8
'''
百度首页登录不能直接定位，
'''
import selenium
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_css_selector('#u1 > a.lb').click()
time.sleep(2)
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('narutoxiaobo')
driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys('qianqian910828')
driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
time.sleep(5)
'''
登陆验证需要手动做验证码处理
'''