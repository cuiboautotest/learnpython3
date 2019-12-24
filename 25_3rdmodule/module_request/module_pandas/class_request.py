#coding=utf-8
import requests
import json
class HttpRequest(object):

    def http_request_baidu(self,url,data,http_method):

        if http_method.upper=='GET':#忽略大小写，如Get使用upper变为GET
            res = requests.get(url, data)  # 执行get请求

        else:
            res = requests.post(url, data)  # 执行post请求

        return res.text

    def http_request_jd(self):
        pass


if __name__=='__main__':
    main()