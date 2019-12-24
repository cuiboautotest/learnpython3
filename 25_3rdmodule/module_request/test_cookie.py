# 导入模块
from requests.sessions import Session

# 创建实例
s = Session()
data = {'username':'mouse','password':'123456'}
headers = {'Content-Type':'application/json'}
r = s.post(url='https://www.imooc.com', json=data, headers=headers)
