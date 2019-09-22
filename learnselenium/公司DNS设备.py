#coding=utf-8
'''
模拟设备登陆操作，将验证码屏蔽
'''
import requests
from selenium import webdriver
import time
import pytest

driver=webdriver.Chrome()
driver.get('https://10.91.3.73')
#切换iframe子框架
#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#最大化窗口
driver.maximize_window()
time.sleep(2)

#定位输入框,如果没有id属性，要用xpath定位，直接选定之后邮件拷贝xpath
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/input').send_keys('sysadmin')

driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/input').send_keys('admin321')

driver.find_element_by_class_name('login-button').click()#点击登陆

time.sleep(5)
#driver.quit()
'''
1.切换到系统页面，属于一级菜单
'''
#driver.find_element_by_class_name('dns-menu')#定位一级菜单
driver.find_element_by_class_name('dns-menu').find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/div[1]/li[7]').click()#系统
#driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/div[1]/li[6]')#审计
#driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/div[1]/li[5]')#策略
#driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/div[1]/li[4]')#报表
#driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/div[1]/li[3]')#日志
#driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/div[1]/li[2]')#告警
#driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[1]/div[1]/li[1]')#首页
time.sleep(15)

'''
切换到二级目录，点击基础配置
'''
#要定位到基础配置先要定位到二级菜单
driver.find_element_by_class_name('second-menu')
#driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[2]')

driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[2]/li[1]').click()

'''
开始邮件服务器配置
'''

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div/form/div[1]/div/div[1]/input').send_keys('lisiyi_2@webworktest.com')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div/form/div[2]/div/div/input').send_keys('admin123')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div/form/div[3]/div/div/input').send_keys('10.91.4.127')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div/form/div[4]/div/div/input').send_keys('25')

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div/form/div[6]/button[1]/span').click()#点击确定

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div/form/div[6]/button[3]/span').click()#发送测试邮件，后续加上断言


'''
升级管理
'''

#driver.find_element_by_xpath('//*[@id="app"]/div[1]/ul[2]/li[2]').click()

'''
时钟同步测试
'''
#系统时间同步,如果不为空，先执行清除
try:
    driver.find_element_by_xpath('//*[@id="Time"]/div/div[2]/div/div/div[3]/input').clear()#send_keys(Keys.CONTROL,'a')
    print('清空内容成功')
except Exception as e:
    print('删除失败：case.%s'% e)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="Time"]/div/div[2]/div/div/div[3]/input').send_keys('pool.ntp.org')
#点击保存
driver.find_element_by_xpath('//*[@id="Time"]/div/div[3]/div/button').click()
#点击立即同步
driver.find_element_by_xpath('//*[@id="Time"]/div/div[2]/div/div/div[3]/button/span').click()
time.sleep(5)



