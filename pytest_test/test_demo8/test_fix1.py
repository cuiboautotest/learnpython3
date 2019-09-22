#coding=utf-8
import pytest
def test_s1(login):
    print("用例1：登陆之后其它动作111")

def test_s2():
    print("用例2：不需要登陆，操作222")

def test_s3():
    print("用例3：登陆之后其它动作333")

if __name__=='__main__':
    pytest.main(["-s","test_fix1"])