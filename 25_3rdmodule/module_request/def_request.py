import requests
#以函数方式定义，并将传入参数参数话
def http_request(url,data):
    res=requests.get(url,data)#参数化
    print('请求的url：', res.url)  # 传递URL参数

    print('请求的响应内容：', res.text)

    print('请求的状态码：', res.status_code)

login_url='http://www.baidu.com'
data={'name':'cuibo','age':12}
http_request(login_url,data)#传入实参，调用函数