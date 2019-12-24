import pytest

class TestDemo:
    #@pytest.mark.parametrize pytest参数化用法
    @pytest.mark.parametrize("a,b,expected",[(1,2,3),(2,3,5),(3,4,8)])
    def test_add(self,a,b,expected):
        #求和
        sum =a +b
        #断言
        assert sum ==expected

        #减法
    @pytest.mark.parametrize("a,b,expected",[(1,2,-1),(8,3,5),(3,4,8)])
    def test_sub(self,a,b,expected):
        s = a - b
        #断言
        assert s==expected
if __name__=='__main__':
    pytest.main('pytest_demo1')
