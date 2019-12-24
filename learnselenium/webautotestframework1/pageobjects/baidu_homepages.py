# coding=utf-8
from framework.base_page import BasePage
'''
页面对象中，百度主页的元素定位和简单的操作函数，页面类主要是元素定位和页面操作写成函数，供测试类调用。
'''
#页面对象继承base_page基类
class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

"""
这里注意下元素定位写法，=>和base_page.py中find_element()方法元素定位切割有关系，网上有些人写根据逗号切割或者等号切割，在实际使用xpath定位，发现单独逗号或者单独等号切割都不精确，造成元素定位失败。
"""

