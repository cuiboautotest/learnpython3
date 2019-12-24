from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
#先定位到设置
bg=driver.find_element_by_link_text('设置')
#执行悬停
ActionChains(driver).move_to_element(bg).perform()
time.sleep(5)
#悬停时执行点击设置
driver.find_element_by_link_text('搜索设置').click()
#不同页面跳转需要等待时间
time.sleep(5)
#先定位到下拉框
sel=driver.find_element_by_id('nr')
#方法1：执行下拉框选择，索引从0开始
ops=Select(sel).options#options返回所有选项
for i in ops:
    print(i.text)
Select(sel).select_by_index(1)#选择20条
#Select(sel).select_by_value('20')方法2
#Select(sel).select_by_visible_text("每页显示20条")#方法3

ops1=Select(sel).all_selected_options#所有已选择的
for j in ops1:
    print('查看已选择的：',j.text)

time.sleep(5)

driver.quit()
