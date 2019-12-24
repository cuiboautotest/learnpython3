#coding=utf-8
import unittest
import time
from selenium import webdriver

class BaiduSearch(unittest.TestCase):
    '''
    测试固件的setUp()的代码，主要是测试的前提准备工作
    '''
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get('https://www.baidu.com')


    '''
    测试结束后的操作,主要是退出浏览器
    '''
    def tearDown(self):
        self.driver.quit()

    """
    设计test_case
    """
    def test_baidu_search(self):#这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        self.driver.find_element_by_id('kw').send_keys('selenium')
        #print(self.driver.title)title是百度一下，你就知道
        time.sleep(5)
        try:
            assert 'selenium' in self.driver.title
            print('Test pass!')
        except Exception as e:
            print('Test fail!',format(e))

if __name__=='__main__':
    unittest.main()

"""
测试固件（test fixture）
      一个测试固件包括两部分，执行测试代码之前的准备部分和测试结束之后的清扫代码。这两部分一般用函数setUp()和tearDown()表示。这里举例以下，例如要测试百度搜索selenium这个场景，我们的测试固件可以这样写，setUp()里写打开浏览器，浏览器最大化，和打开百度首页等脚本代码；在tearDown（）里写结束搜索后，退出并关闭浏览器的代码。
测试用例（test case）
       unittest中管理的最小单元是测试用例，一个测试用例，包括测试固件，和具体测试业务的函数或者方法。一个测试用例中，测试固件可以不写，但是至少有一个已test开头的函数。unittest会自动化识别test开头的函数是测试代码，如果你写的函数不是test开头，unittest是不会执行这个函数里面的脚本的，这个千万要记住，所有的测试函数都要test开头，记住是小写的哦。
测试套件 （test suite）
       很简单，就是很多测试用例的集合，叫测试套件，一个测试套件可以随意管理多个测试用例。如果测试用例比作单个学生，测试套件就是好像是班级的概念。
测试执行器 （test runner）
       test runner是一个用来执行加载测试用例，并执行用例，且提供测试输出的一个组建。test runner可以加载test case或者test suite进行执行测试任务。

我们举例来，练习一下test fixture和test case的使用，学习unittest的简单用法：
1. 新建一个testbaidu.py的文件
2. 导入unittest模块
3. 当前测试类继承unittest.TestCase，相当于当前利用unittest创建了一个test case，这个test case是能够被unittest直接识别。
4. 写setUP(),主要是打开浏览器和打开站点
5. 写一个test_search（）用例写搜索的代码
6. 写tearDown(),主要是浏览器退出操作


"""
