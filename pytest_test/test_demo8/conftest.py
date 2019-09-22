#coding=utf-8
"""
conftest.py配置需要注意以下点：
conftest.py配置脚本名称是固定的，不能改名称
conftest.py与运行的用例要在同一个package下，并且有init.py文件
不需要import导入 conftest.py，pytest用例会自动查找
单独运行test_fix1.py和test_fix2.py都能调用到login()方法，这样就能实现一些公共的操作可以单独拿出来了
"""
import pytest
@pytest.fixture()
def login():
    print("输入账号，密码先登陆")