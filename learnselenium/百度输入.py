#coding=utf-8
"""
webdriver放在python安装目录下即可，注意查看对应的谷歌浏览器版本
下载地址：https://npm.taobao.org/mirrors/chromedriver
"""
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
#implicitly_wait(10)
driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(3)
#执行清除输入框
driver.find_element_by_id('kw').clear()
time.sleep(3)
#重新输入搜索内容
driver.find_element_by_id('kw').send_keys('python')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(2)
title=driver.title
print(title)
driver.quit()
