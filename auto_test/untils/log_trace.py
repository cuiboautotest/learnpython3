"""
日志打印，采用内置logging模块才记录运行日志，设置日志级别。
"""
import  logging
filename = "../report/test_case_run.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s1 %(filename)s [line:%(lineno)d]  %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=filename,
                    filemode='w')
