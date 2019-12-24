\from selenium import webdriver
from functions import date_n,id,xpath,css,js,return_driver,open_base_site
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=return_driver()
open_base_site('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx')

from_station = '上海'
to_station = '杭州'
#定义Tomorrow变量
tomorrow=date_n(1)
print(tomorrow)

driver.maximize_window()
#定位出发城市
id('notice01').send_keys(from_station)
#定位到达城市
id('notice08').send_keys(to_station)
#时间输入框只读readonly,移除出发时间的只读
js('dateObj')
#移除之后就可以通过sendkeys方式输入,由于输入框存在默认输入，先清除
time.sleep(2)
id('dateObj').clear()
time.sleep(2)
#输入日期
id('dateObj').send_keys(tomorrow)

#以下步骤是为了解决日期控件输入完毕之后无法消失，采用点击页面其它空白处让其消失
ActionChains(driver).move_by_offset(0,0).click().perform()

#点击车次搜索，开始搜索
id('searchbtn').click()
time.sleep(5)

#开始预定K1805车次硬座
#css('#tbody-01-K18050 > div.railway_list > div.w6 > div:nth-child(2) > a').click()
xpath('//*[starts-with(@id,"tbody-01-K18050")]/div[1]/div[6]/div[2]/a')
#不登陆携程系统订票
#driver.find_element_by_id('btn_nologin').click()
time.sleep(5)
#订单页面输入乘客姓名信息
css('#pasglistdiv > div > ul > li:nth-child(2) > input').send_keys('崔博')
#输入身份证号
css('#pasglistdiv > div:nth-child(1) > ul > li:nth-child(3) > input').send_keys('632701198910162345')
#输入联系人电话
id('contact-mobile').send_keys('15927536501')
#点击立即预定
css('#UpdatePanel1 > div:nth-child(2) > div > button.btn-pay.big').click()
time.sleep(5)