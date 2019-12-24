from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
#先定位到设置
element=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(element).perform()
#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)
#点击保存
driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()
#弹出告警框，接受弹框
driver.switch_to.alert.accept()#注意python2和python3区别
#driver.switch_to_alert().accept()pyhton2写法
#获取警告框信息
#print(driver.switch_to.alert().text)
