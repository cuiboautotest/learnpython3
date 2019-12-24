#coding=utf-8
import requests
import json
class HttpRequest(object):

    def http_request_baidu(self,url,data,http_method):

        if http_method.upper=='GET':
            res = requests.get(url, data)  # 执行get请求
            print('get请求结果',res.text)
            print(res.status_code)
        else:
            res = requests.post(url, data)  # 执行post请求
            print('post请求结果',res.text)
            print(res.status_code)

    def http_request_jd(self):
        pass

login_url='http://www.baidu.com'
data={'name':'cuibo','age':12}
http1=HttpRequest()
http1.http_request_baidu(login_url,data,'get')