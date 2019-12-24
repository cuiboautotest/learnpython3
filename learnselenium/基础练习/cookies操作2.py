
# -*- coding: utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
cookie = driver.get_cookies()                # 获取所有的cookie，cookie数据以字典的形式存放
print(cookie)
print(driver.get_cookie('BAIDUID'))          # get_cookie(name)方法用来获取cookie键值name对应的值
driver.add_cookie({'name': 'hello','value' : 'world'})  # 添加cookie
for cookie in driver.get_cookies():
    print(driver.get_cookie('hello'))
driver.delete_cookie('hello')                # 删除指定的cookie
# driver.delete_all_cookies()                  # 删除所有的cookie
driver.quit()
