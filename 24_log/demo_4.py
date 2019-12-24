#coding=utf-8
import logging
LOG_FORMAT ='%(asctime)s - %(levelname)s - %(message)s'
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.DEBUG, filename='my.log',format=LOG_FORMAT,datefmt=DATE_FORMAT)
#日志格式默认是BASIC_FORMAT会输出格式"%(levelname)s:%(name)s:%(message)s"
logging.info('This is a info log.')
logging.debug('This is a debug log.')
logging.warning('This is a warning log.')
logging.error('This is a error log.')
logging.critical('This is a critical log.')