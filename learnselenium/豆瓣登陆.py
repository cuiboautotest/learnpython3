import requests
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://www.douban.com')
#切换iframe子框架
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#最大化窗口
driver.maximize_window()
time.sleep(2)
#点击密码输入的标签，切换到密码登陆界面
driver.find_element_by_css_selector('li.account-tab-account').click()
#driver.find_element_by_xpath('//li[contains(@class,"account-tab-account")]')
#定位输入框
driver.find_element_by_id('username').send_keys('15927536501')
driver.find_element_by_id('password').send_keys('cuibo123456')
#这里需要注意，当元素的class属性有好几个的时候，此函数的参数填class的第一个就好,如：btn btn-account 只写btn
driver.find_element_by_class_name('btn').click()#点击登陆
#driver.find_element_by_xpath('//a[contains(@class,"btn-account")]')

time.sleep(5)
driver.quit()
'''
#获取cookies
cookies = {i['name']: i['value'] for i in driver.get_cookies()}
print(cookies)


'''