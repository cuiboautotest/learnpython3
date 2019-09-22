#coding=utf-8
"""
定义多个fixture，然后用test_ 传多个fixture
"""
import pytest
@pytest.fixture()
def user():
    print("获取用户名：")
    a="cuibo"
    return a

@pytest.fixture()
def psw():
    print("输入密码：")
    b='123456'
    return b

def test_1(user,psw):
    print("测试账号:%s,密码：%s"%(user,psw))
    assert user=="cuibo"

if __name__=="__main__":
    pytest.main(["-s","test_fixt3.py"])