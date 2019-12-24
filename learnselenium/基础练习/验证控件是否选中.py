import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://news.baidu.com/")
time.sleep(1)
try:
    driver.find_element_by_xpath("//*[@id='news']").is_selected()
    time.sleep(5)
    print('Test Pass.')
except Exception as e:
    print('Test fail', format(e))
