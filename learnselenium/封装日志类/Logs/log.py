'''
问题分析：
我们需要封装一个简单的日志类，主要有以下内容：
1. 生成的日志文件格式是 年月日时分秒.log
2. 生成的xxx.log文件存储在项目根目录下Logs文件夹下
3. 这个日志类，支持INFO,ERROR两种日志级别
4. 日志里，每行日志输出，如上图，时间日期+执行类名称+日志级别+日志描述

解决问题思路：
1. 在根目录下新建一个Logs的文件夹，如何获取这个Log的相对路径，前面介绍过。
2. 日志的保存命名，需要系统时间，前面也介绍过时间格式化输出
3. Python中有一个logging模块来支持我们自定义封装一个新日志类。
4. 在脚本里，初始化一个日志类的实例对象，然后去控制输出INFO还是ERROR日志信息。


'''

import logging
import os
import time
'''
因为当前log.py默认环境变量存放的目录是Error_Logs目录，如果想调用getcwd.py这个函数，需要将跟getcwd.py同目录环境变量加入进来才能通过import引用，使用下面方法
如果不使用下面方法
需要将getcwd.py放到跟log.py同一个路径下（即对应同一个__int__）,直接import getcwd或from getcwd import get_cwd或from getcwd import *
'''
import sys
sys.path.append('..')#不同文件夹之间的引用，getcwd.py对应的目录是封装日志类，log.py对应的目录是Logs

import getcwd
class Logger(object):

    def __init__(self,logger):#如果报错TypeError: Logger() takes no arguments，注意是init不是int

        #创建一个logger
        self.logger=logging.getLogger(logger)#定义日志器输出名
        self.logger.setLevel(logging.DEBUG)
        """
        设置日志存放路径，日志文件名
        """
        #获取本地时间，转换为设置的格式
        rq=time.strftime('%Y%m%d%H%m',time.localtime(time.time()))

        #通过getcwd.py文件得绝对路径来拼接日志存放路径
        path=getcwd.get_cwd()#调用函数的方法

        #两种日志存放路径
        all_log_path=os.path.join(path,'Logs/All_Logs/')#拼接成 封装日志类/Logs/All_Logs/
        error_log_path=os.path.join(path,'Logs/Error_Logs/')#拼接成 封装日志类/Logs/Error_Logs/

        #设置日志文件名
        all_log_name=all_log_path + rq + '.log'
        #print(all_log_name)
        error_log_name=error_log_path + rq + '.log'

        '''
         创建handler步骤
        '''
        #创建一个handler写入所有日志
        fh=logging.FileHandler(all_log_name)
        fh.setLevel(logging.INFO)
        #创建一个handler写入错误日志
        eh=logging.FileHandler(error_log_name)
        eh.setLevel(logging.ERROR)
        #创建一个handler输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        '''
        定义日志输出格式
        '''
        #以时间-日志器名称-日志级别-日志内容形式展示所有日志
        all_log_formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        #以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        error_log_formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s--%(modelue)s-%(lineno)s-%(message)s')

        #将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)
        ch.setFormatter(all_log_formatter)

        #给laogger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

'''
日志类创建了一个实例，括号里面的selenium可以填项目名称表示哪个项目，在调用日志类的时候，直接import这个log1，不用在使用的时候再去初始化，一来避免重复去初始化，二来可以避免偶尔info日志重复打印的问题
'''





