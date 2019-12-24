
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()             # 最大化窗口
time.sleep(5)
driver.set_window_size(480,800)      # 设置窗口大小
driver.back()                        # 浏览器后退
driver.forward()                     # 浏览器前进
time.sleep(5)
driver.refresh()                     # 浏览器刷新
driver.quit()                        # 浏览器退出
