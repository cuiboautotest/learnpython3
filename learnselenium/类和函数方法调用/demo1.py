import time
from selenium import webdriver

class BaiduSearch(object):

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    def open_baidu(self):
        self.driver.get('https://www.baidu.com') #self总是指调用时的类的实例
        time.sleep(1)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        print(self.driver.title)
        try:
            assert 'selenium' in self.driver.title
            print('Test pass!')
        except Exception as e:
            print('Test fail!',format(e))

test1=BaiduSearch()#实例化一个对象
#print(test1)
#print(type(test1))

#调用类中的方法
test1.open_baidu()
test1.test_search()