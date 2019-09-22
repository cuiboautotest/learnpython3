
#coding = utf-8
import requests
import json
payload = {"yoyo":"hello world",
           "pythonQQ群":"123456"}#字典格式
#转换json格式,json.dumps()用于将字典形式的数据转化为字符串，json.loads()用于将字符串形式的数据转化为字典
data_json=json.dumps(payload)
r = requests.post('http://httpbin.org/post',json=data_json)#post的body是json类型，也可以用json参数传入
print(r.text)
