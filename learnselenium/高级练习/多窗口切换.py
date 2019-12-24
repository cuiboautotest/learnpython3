
# -*- coding: utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
sreach_windows = driver.current_window_handle    # 获取当前百度搜索窗口的句柄，是一个字符串
print(sreach_windows)
driver.find_element_by_link_text(u'登录').click()
driver.find_element_by_link_text(u'立即注册').click()
all_handles = driver.window_handles                  # 得到搜索页面和注册页面所有的窗口句柄，返回的是一个列表
print(all_handles)
# 进入到注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)          # 切换到指定窗口
        print("现在进入的是注册窗口")
        driver.find_element_by_name('userName').send_keys('123')
# 切换到搜索窗口
for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to.window(handle)          # 切换到指定窗口
        print("现在进入的是搜索窗口")
        driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()  # 关闭注册窗口
        driver.find_element_by_id('kw').send_keys('python')
