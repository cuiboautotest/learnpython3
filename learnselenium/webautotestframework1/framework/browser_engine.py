from selenium import webdriver
import time
class BrowserEngine(object):

    def __init__(self,driver):
        self.driver=driver

    browser_type='Chrome'# IE or Firefox



    def start_browser(self):
        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
        :return: driver
        """

        if self.browser_type == 'Firefox':
            driver = webdriver.Firefox()

        elif self.browser_type == 'IE':
            driver=webdriver.Ie()
        else:
            driver = webdriver.Chrome()
            print('成功打开谷歌浏览器')
        driver.maximize_window()
        driver.implicitly_wait(5)

        return driver


