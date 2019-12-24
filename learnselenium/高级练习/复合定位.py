#coding=utf-8
'''
打开百度首页，设置，搜索设置，选择搜索语言范围，选择仅简体中文
'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
ActionChains(driver).move_to_element(driver.find_element_by_link_text('设置')).perform()
time.sleep(2)
driver.find_element_by_class_name('setpref').click()
time.sleep(2)
r=driver.find_elements_by_name('SL')#定位复选框，定位对象是一个列表
r.pop(1).click()#选择第二2个元素