from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(10)


try:
    driver.find_element_by_partial_link_text('主页').click()
    time.sleep(5)
    print('test pass:element found by partial link text')
except Exception as e:
    print('定位失败：case:%s'%e)
finally:
    driver.quit()
