import sys
import os
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
        path=os.getcwd()#调用函数的方法

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
