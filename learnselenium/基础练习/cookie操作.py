#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
#打开博客园
driver.get('https://www.cnblogs.com')
print('before login:')
#打印全部cookie
for cookie_detail in driver.get_cookies():
    print(cookie_detail)
driver.find_element_by_xpath('//*[@id="span_userinfo"]/a[1]').click()
time.sleep(5)
driver.find_element_by_id('LoginName').send_keys('narutoxiaozhi')
driver.find_element_by_id('Password').send_keys('cuibo123456..')
driver.find_element_by_class_name('ladda-label').click()
#等待30s
time.sleep(30)
print('after login:')
for cookie_detail in driver.get_cookies():
    print(cookie_detail)

driver.quit()