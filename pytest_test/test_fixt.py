#coding=utf-8
import pytest
#不带参数默认scope='function'
#实现场景：用例1需要先登录，用例2不需要登录，用例3需要先登录
"""
在同一个.py文件中，多个用例调用一个登陆功能，如果有多个.py的文件都需要调用这个登陆功能的话，那就不能把登陆写到用例里面去了。
"""
@pytest.fixture()
def login():
    print("输入账号、密码，先登录")

def test_s1(login):
    print("用例1：登陆之后其它动作111")

def test_s2():#不传login
    print("用例2：不需要登陆，操作222")

def test_s(login):
    print("用例3：登陆之后其它动作333") #调用login装饰器，都要先执行装饰器的内容

if __name__=='__main__':
    pytest.main(["-s","test_fixt.py"])