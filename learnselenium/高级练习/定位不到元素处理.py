from selenium import webdriver
import time
import os

driver_item=webdriver.Chrome()
url="https://movie.douban.com/"
driver_item.get(url)

while True:
    start = time.clock()
    try:
        sleep(10)
        driver_item.find_element_by_partial_link_text('排行榜').click()
        print('已定位到元素')
        end=time.clock()
        break
    except:
        print("还未定位到元素!")

print('定位耗费时间：' + str(end - start))

