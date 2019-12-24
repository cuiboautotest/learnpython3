#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.hao123.com')
driver.maximize_window()
#获取当前句柄
current_handle=driver.current_window_handle
print(current_handle)
#单机超链接
driver.find_element_by_link_text('hao123新闻').click()
time.sleep(5)
#所有窗口句柄，即列表类型
handles=driver.window_handles
print(handles)
#切换到新窗口
driver.switch_to.window(handles[1])
time.sleep(5)
driver.find_element_by_xpath('//*[@id="fixedNav"]/div/div[1]/ul/li[2]/a').click()
