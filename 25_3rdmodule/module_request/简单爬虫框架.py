#coding=utf-8
import requests
from requests import Response

url='http://www.baidu.com'
#data={}

try:
    r=requests.get(url=url,params=None,timeout=30)
    r.raise_for_status()#如果状态不是200则引发异常
    r.encoding=r.apparent_enconding#配置编码
    print(r.text)
except:
    print( '请求异常')
