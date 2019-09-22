class cuiboException(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    raise cuiboException('类型错误')
except cuiboException as e:
    print(e)