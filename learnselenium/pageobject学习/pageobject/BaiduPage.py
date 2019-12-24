from framework.base_page import BasePage

class baidu(BasePage):
    kw=['id','kw']#定位搜索输入框
    su=['id','su']#搜索按钮

    def kw_send(self,value):
        self.send(self.kw，value)

    def su_click(self):#点击搜索
        self.click(self.su)


"""
这是百度搜索页面的页面类。定位的元素单独拿出来，这样就可以重复使用。然后元素的操作也封装成一个方法。就比如上面这个搜索框输入内容。value这个值在后面测试类的时候，可以根据输入的不同，组装成不同的测试用例。
"""