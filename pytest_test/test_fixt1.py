import pytest
@pytest.fixture()
def user():
    print("获取用户名")
    a="cuibo"
    return a

def test_1(user):#fixture作为参数传入，直接把fixture的函数名当成变量名称
    assert user=="cuibo"

def test_2(user):
    assert user=="yoyo"

if __name__=="__main__":
    pytest.main(["-s","test_fixt1.py"])
