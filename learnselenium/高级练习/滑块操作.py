#coding=utf-8
'''
1.打开携程网注册页面
2.单击同意并继续按钮，出现弹框
3.验证手机步骤显示‘滑块验证’
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get('https://passport.ctrip.com/user/reg/home')

#点击同意并继续
driver.find_element_by_xpath('//*[@id="agr_pop"]/div[3]/a[2]').click()
#方法2：driver.find_element_by_css_selector('agr_pop > div.pop_footer > a.reg_btn.reg_agree').click()

driver.find_element_by_id('mobilephone').send_keys('15927536501')

#获取滑块元素,查看宽和高
source=driver.find_element_by_css_selector('#slideCode > div.cpt-drop-box > div.cpt-drop-btn')
print(source.size['width'])
print(source.size['height'])

#获取滑块移动区域元素，查看宽和高
area=driver.find_element_by_css_selector('#slideCode > div.cpt-drop-box > div.cpt-bg-bar')
print(area.size['width'])
print(area.size['height'])

#执行鼠标拖动,变为绿色代表成功
ActionChains(driver).drag_and_drop_by_offset(source,area.size['width'],-source.size['height']).perform()
time.sleep(5)



