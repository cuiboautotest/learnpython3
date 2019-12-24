#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import timedelta,datetime,date



def date_n(n):
    return str((date.today()+timedelta(days=+int(n))).strftime("%Y-%m-%d"))

#出发站和到达站
from_station = '上海'
to_station = '杭州'
#定义Tomorrow变量

tomorrow=date_n(1)
print(tomorrow)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
# 打开携程网订票
driver.get('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
driver.implicitly_wait(5)
driver.maximize_window()
#定位出发城市
driver.find_element_by_id('notice01').send_keys(from_station)
#定位到达城市
driver.find_element_by_id('notice08').send_keys(to_station)
#时间输入框只读readonly,移除出发时间的只读
driver.execute_script("document.getElementById('dateObj').removeAttribute('readonly')")
#移除之后就可以通过sendkeys方式输入,由于输入框存在默认输入，先清除
time.sleep(2)
driver.find_element_by_id('dateObj').clear()
time.sleep(2)
#输入日期
driver.find_element_by_id('dateObj').send_keys(tomorrow)

#以下步骤是为了解决日期控件输入完毕之后无法消失，采用点击页面其它空白处让其消失
ActionChains(driver).move_by_offset(0,0).click().perform()

#点击车次搜索，开始搜索
driver.find_element_by_id('searchbtn').click()
time.sleep(5)

#开始预定K1805车次硬座
driver.find_element_by_css_selector('#tbody-01-K18050 > div.railway_list > div.w6 > div:nth-child(2) > a').click()
#不登陆携程系统订票
#driver.find_element_by_id('btn_nologin').click()
time.sleep(3)
#订单页面输入乘客姓名信息
driver.find_element_by_css_selector('#pasglistdiv > div > ul > li:nth-child(2) > input').send_keys('崔博')
#输入身份证号
driver.find_element_by_css_selector('#pasglistdiv > div:nth-child(1) > ul > li:nth-child(3) > input').send_keys('652701198910164519')
#输入联系人电话
driver.find_element_by_id('contact-mobile').send_keys('15927536501')
#点击立即预定
driver.find_element_by_css_selector('#UpdatePanel1 > div:nth-child(2) > div > button.btn-pay.big').click()
time.sleep(5)









