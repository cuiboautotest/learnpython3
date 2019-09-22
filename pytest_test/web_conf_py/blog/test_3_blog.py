import pytest
import time

def test_03(start, open_blog):
    print("测试用例test_03")
    time.sleep(1)
    assert start=="cuibo"

def test_04(start,open_blog):
    print("测试用例test_04")
    time.sleep(1)
    assert start=="cuibo"

def test_05(start,open_blog):
    '''
    跨模块调用baidu模块下的conftest
    '''
    print("测试用例test_05，跨模块调用baidu")
    time.sleep(1)
    assert start=="cuibo"

if __name__=='__main__':
    pyetst.main(["-s","test_3_blog.py"])