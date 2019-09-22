# coding=utf-8
import pytest

def test_s4(login):
    print("用例4：登陆之后其它动作444")

def test_s5():
    print("用例5：不需要登陆，操作555")

if __name__ == '__main__':
    pytest.main(["-s", "test_fix2"])