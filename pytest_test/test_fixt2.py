#coding=utf-8
"""
使用多个fixture,可以返回元组，字典，list
"""
import pytest
@pytest.fixture()
def user():
    print("获取用户名")
    a="cuibo"
    b="123456"
    return (a,b)

def test_1(user):
    u= user[0]
    p=user[1]
    print("测试账号:%s,密码：%s"%(u,p))
    assert u=="cuibo"

def test_2(user):
    u= user[0]
    p=user[1]
    print("测试账号:%s,密码：%s"%(u,p))
    assert u=="cuibo123"

if __name__=="__main__":
    pytest.main(["-s","test_fixt2.py"])