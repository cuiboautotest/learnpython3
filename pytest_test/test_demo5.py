#coding:utf-8
"""
模块函数式
setup_module是所有用例开始前只执行一次
teardown_module是所有用例结束后只执行一次
setup_function只在函数用例生效
teardown_function
4种方法可以任意组合
"""
import pytest
def setup_module():
    print("setup_module:整个.py开始只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")
def teardown_module():
    print("teardown_module:整个.py最后只执行一次")
    print("比如：所有用例执行结束后只最后关闭浏览器")

def setup_function():
    print("setup_function:每个用例开始前都会执行")
def teardown_function():
    print("teardown_function:每个用例结束后都会执行")

def test_one():
    print("正在执行----test_one")
    x='this'
    assert 'h'in x

def test_two():
    print("正在执行----test_two")
    1==1

def test_three():
    print("正在执行---test_three")
    a='hello'
    b='hello world'
    assert a in b

if __name__=='__main__':
    pytest.main()

#test所在目录执行pytest --html=（xxxx名字）.html
'''
①切换到要执行文件的目录
$pytest --html=report.html
#默认会将报告存在与当前路径下
②执行指定用例
pytest test_exception.py --html=../reports/test_exception.html
#test_exception.py为需要执行的用例
#../reports/  专门创建了一个文件夹用于存储测试报告，此为目录地址
#test_exception.html为测试报名名称

'''





