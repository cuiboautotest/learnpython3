import pytest
import time
def test_06(start,open_baidu):
    print("测试用例test_06")
    time.sleep(1)
    assert start=="cuibo"

def test_07(start,open_baidu):
    print("测试用例test_07")
    time.sleep(1)
    assert start=="cuibo"

if __name__=='__main__':
    pyetst.main(["-s","test_2_baidu.py"])