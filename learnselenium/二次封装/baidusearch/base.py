#coding=utf-8
from selenium import webdriver
from time import sleep
class BaseBaidu():
    def __init__(self):
        self.dr=webdriver.Chrome()

    '''
    将8大定位元素方法封装起来
    
    '''
    # id定位
    def by_id(self, locator):
        return self.dr.find_element_by_id(locator)

    # name定位
    def by_name(self, locator):
        return self.dr.find_element_by_name(locator)

    #class定位
    def by_class(self,locator):
        return self.dr.find_element_by_class_name(locator)

    # link_text定位
    def by_link_text(self, locator):
        return self.dr.find_element_by_link_text(locator)

    # partial_link_text定位
    def by_link_text(self, locator):
        return self.dr.find_elements_by_partial_link_text(locator)

    # css定位
    def by_css(self, locator):
        return self.dr.find_element_by_css_selector(locator)

    # xpath定位
    def by_xpath(self, locator):
        return self.dr.find_element_by_xpath(locator)

    # tagname定位
    def by_classname(self,locator):
        return self.dr.find_element_by_tag_name(locator)

    '''
    封装常用操作
    '''

    #打开网页
    def getUrl(self,url):
        return self.dr.get(url)

    #输入内容
    def input_text(self,locator,text):
        return self.by_id(locator).send_keys(text)

    #点击搜索
    def click_btn(self,locator):
        return self.by_id(locator).click()

    #关闭浏览器
    def close_browser(self):
        self.dr.quit()

    #断言
    def assert_text(self,demo):
        try:
            sleep(3)
            if demo in self.dr.title:
                print('断言成功！')
        except Exception as e:
            print('断言失败！%s'%e)

    '''
    各个步骤封装导一个函数，再次封装
    '''
    def all_actions(self,url,text,loc1,loc2):
        self.getUrl(url)
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()
        self.input_text(loc1,text)
        self.click_btn(loc2)
        sleep(3)
        self.assert_text()
        self.close_browser()