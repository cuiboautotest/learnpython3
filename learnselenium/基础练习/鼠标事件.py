#coding=utf-8
'''
context_click()右键
double_click()双击
drag_and_drop()拖拽
move_to_element()悬停
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
#先定位到设置
element=driver.find_element_by_link_text('新闻')
#实现在新闻超链接上右击
ActionChains(driver).context_click(element).perform()