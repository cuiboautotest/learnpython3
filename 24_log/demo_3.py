import os
import logging
logging.basicConfig(level=logging.DEBUG)
path=os.path.dirname(os.path.abspath(__file__))
print(path)
#手动创建一个test.txt的文件夹，通过路径拼接
filepath=os.path.join(path,'test1.txt')
print(filepath)
fh=logging.FileHandler(filepath)#传入变量
fh.setLevel(logging.INFO)#通过setLevel()方法可以设置logger的日志输出级别

#返回一个logger实例，可以传入一个logger的名字，如果没有传，默认是root logger
cb=logging.getLogger('my logger')

cb.addHandler(fh)#给logger添加handler
cb.info('cui bo is testing log module')

#配置日志输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')#formatter不像handler还需要先创建一个对应的实例，直接配置就可以了
fh.setFormatter(formatter)
cb.info('1111222333444')
