#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
driver.maximize_window()
#登陆界面要先进行账号密码切换登陆，F12打开之后查看到有iframe，所以先定位到iframe，使用id定位
iframe_id=driver.find_element_by_id('login_frame')#定位到iframe和
driver.switch_to.frame(iframe_id)
#点击账号密码登陆
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('794788503@qq.com')
driver.find_element_by_id('p').send_keys('qianqian910828..')
driver.find_element_by_class_name('btn').click()
time.sleep(5)
driver.quit()

