#coding=utf-8
import unittest
class TestCase_01(unittest.TestSuite):

    @classmethod
    def setUpClass(cls):
        print("这是所有case的前置条件01")

    @classmethod
    def tearDownClass(cls):
        print("这是所有case的后置条件02")

    def setUp(self):
        print("这是每条测试的前置条件01")

    def tearDown(self):
        print("这是每条测试的后置条件02")

#测试用例的命名必须以test开头，否则不予执行
    def testFirst_01(self):
        print("01：第一条case")

    @unittest.skip('不执行这条case')#装饰器，跳过这条case
    def testSecond_01(self):
        print("01:第二条case")

    def testThird_01(self):
        print("01:第三条case")

    def testFourth_01(self):
        print("01:第四条case")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCase_01('testThird_01'),TestCase_01('testSecond_01'),TestCase_01('testFirst_01')]

    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)

    runner.run(suite)



