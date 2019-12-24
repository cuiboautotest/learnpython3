#coding:utf-8
"""
函数方式 前置和后置用法 setup_function teardown_function
"""
import pytest
import allure

def setup_function():
    print("setup_function:每个用例开始前都会执行")
def teardown_function():
    print("teardown_function:每个用例结束后都会执行")

@allure.feature('测试用例1')
def test_one():
    print("正在执行----test_one")
    x='this'
    assert 'h'in x

@allure.feature('测试用例2')
def test_two():
    print("正在执行----test_two")
    1==1

@allure.feature('测试用例3')
def test_three():
    print("正在执行---test_three")
    a='hello'
    b='hello world'
    assert a in b

if __name__=='__main__':
    pytest.main()