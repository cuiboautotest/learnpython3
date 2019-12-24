from selenium import webdriver
from pageobject.BaiduPage import baidu
import unittest

class BaiduSearch(unittest.TestCase):


    def test_baidu(self):
        dr=webdriver.Chrome()
        dr.get("https://www.baidu.com")
        bai=baidu(dr)#每个页面都需要把driver传进去。使用WebDriver有一个要注意的就是 脚本运行的时候要保持只有一个driver。
        bai.kw_send('selenium')
        bai.su_click()


if __name__=='__main__':
    unittest.main()
