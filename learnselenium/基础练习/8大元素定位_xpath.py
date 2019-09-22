from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.jd.com')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="J_cate"]/ul/li[3]/a[1]').click()#定位电脑

driver.implicitly_wait(10)
#验证控件是否选中
driver.find_element_by_id('channel').is_selected()
print('select ok')
#增加断言方法：通过selenium方法is_displayed() 来判断我们的目标元素是否在页面显示。
driver.find_element_by_id('channel').is_displayed()#查看新打开的页面电脑分类是否显示
print('test success!')
