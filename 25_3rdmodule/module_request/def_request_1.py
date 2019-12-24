#coding=utf-8
import requests
import json
#以函数方式定义，并将传入参数参数话
def http_request(url,data,http_method='POST'):#默认post请求

    if http_method.upper=='GET':
        res = requests.get(url, data)  # 执行get请求
    else:
        res = requests.post(url, data)  # 执行post请求

    print('请求的响应内容：', res.text)

    print('请求的状态码：', res.status_code)

login_url='http://www.baidu.com'
data={'name':'cuibo','age':12}
http_method='get'
http_request(login_url,data,http_method)#调用函数
http_request(login_url,data,'post')#直接传参
http_request(login_url,data)#不传参数，默认第三个参数使用默认post请求
