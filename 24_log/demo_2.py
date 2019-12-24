import logging
#设置日志级别，一次性设置，需要在开头就设置，在中间设置没有作用
#默认日志输出级别为warning，如果想要输出debug以上级别需要下面这个方法进行修改，修改必须在开始就设置，中途设置无效
logging.basicConfig(level=logging.DEBUG)
logging.debug("a")
logging.info("b")
logging.warning('c')
logging.error('d')
logging.critical('e')
#结果输出所有
logging.basicConfig(level=logging.ERROR)#