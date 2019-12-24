import logging
logging.debug("a")
logging.info("b")
logging.warning('c')
logging.error('d')
logging.critical('e')
"""
CRITICAL > ERROR > WARNING > INFO > DEBUG >NOTSET 日志的信息量会依次减少

当指定一个日志级别之后，会记录大于或等于这个日志级别的日志信息，小于的将会被丢弃

默认级别是logging.warning，低于该级别的就不输出了
"""