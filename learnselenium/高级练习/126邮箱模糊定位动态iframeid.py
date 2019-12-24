#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.126.com')
driver.find_element_by_id('switchAccountLogin').click()
driver.maximize_window()
time.sleep(2)
#iframe 的ID是动态变化，因此需要用模糊定位元素，先用xpath定位，然后改写,里面用单引号，外面用双引号，否则会出现语法错误
iframe=driver.find_element_by_xpath("//*[starts-with(@id,'x-URS-iframe')]")
#[starts-with(@id, 'x-URS-iframe')]
driver.switch_to.frame(iframe)
#driver.find_element_by_id('idInput').send_keys('admin')id变化不能用id定位
driver.find_element_by_name('email').send_keys('cb794788503')
driver.find_element_by_name('password').send_keys('admin123')
time.sleep(5)
driver.find_element_by_id('dologin').click()
time.sleep(5)

'''
如果是动态Id需要借助xpath部分元素属性定位,xpath中提供了三个非常好的方法来为我们定位部分属性值：

driver.find_element_by_xpath

("//div[contains(@id, 'btn-attention')]")

driver.find_element_by_xpath

("//div[starts-with(@id, 'btn-attention')]")

driver.find_element_by_xpath

("//div[ends-with(@id, 'btn-attention')]") 

# 这个需要结尾是‘btn-attention’

contains(a, b) 如果a中含有字符串b，则返回true，否则返回false

starts-with(a, b) 如果a是以字符串b开头，返回true，否则返回false

ends-with(a, b) 如果a是以字符串b结尾，返回true，否则返回false

注意元素用单引号

'''