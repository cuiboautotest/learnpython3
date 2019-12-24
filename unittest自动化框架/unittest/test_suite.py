#coding=utf-8
import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_add"),TestMathFunc("test_minus"),TestMathFunc("test_divide")]
    # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    suite.addTests(tests)

    with open('UnittestTextReport.txt','a') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)


