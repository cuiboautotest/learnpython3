
import requests
r= requests.get("https://www.baidu.com")
print('get请求的url：',r.url)#传递URL参数

print('get请求的响应内容：',r.text)#响应内容可以是html，xml,json
print('get请求的响应内容json格式：',r.json)#必须为json格式才有响应结果，不支持则无

print('get请求的状态码：',r.status_code)
print('get请求的响应体：',r.content)#以字节的方式访问请求响应体

print('get请求的响应体：',r.content.decode(encoding='utf-8'))#解码转为utf-8

print('get请求的响应头：',r.headers)
print('get请求的请求头：',r.request.headers)#默认请求头中代理是通过python-requests/2.21.0来进行请求

headers={'User-Agent': 'Mozilla5.0'}
url='http://www.jd.com'
res=requests.get(url,headers=headers)
print('get请求的请求头JD：',res.request.headers)



#get请求带参数
payload = {'key1':'value1','key2':['value2','value3']}
r2 = requests.get('https://httpbin.org/get',params=payload)
#r2 = requests.get('https://httpbin.org/get',payload)参数可以省略
print(r2.url)



