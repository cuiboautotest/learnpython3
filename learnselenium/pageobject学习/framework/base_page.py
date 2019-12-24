#coding=utf-8
class BasePage(object):
    def __int__(self,driver):
        self.driver=driver

    def find_element(self,selector):
        by = selector[0]
        value=selector[1]
        element=None

        if by=='id' or by=='name' or by=='xpath' or by=='class' or by=='link' or by=='plink' or by =='css' or by =='tag':
            if by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif by == 'tag':
                element = self.driver.find_element_by_tag_name(value)
            elif by == 'link':
                element = self.driver.find_element_by_link_text(value)
            elif by == 'plink':
                element = self.driver.find_element_by_partial_link_text(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'xpath':
                element = self.driver.find_element_by_xpath(value)
            else:
                print('没有找到元素')
    #自定义send方法
    def send(self,selector,value):
        element=self.find_element(selector)#调用的封装的定位元素方法

        try:
            element.send_keys(value)
            print('输入的内容:%s'%value)
        except:
            print('error')

    #自定义click方法
    def click(self,selector):
        element=self.find_element(selector)
        element.click()

"""
这是封装的公共方法。封装的元素定位方法需要传一个数组，数组下标第一个是定位方式，第二个是具体的值。元素定位写在封装的元素操作里面，不写在后面页面类里是因为方便在页面类里面重复使用元素。
"""