import requests
r= requests.get("https://www.baidu.com")
print(r.url)#传递URL参数
print('\n')
print(r.text)#响应内容
print('\n')
print(r.content)#以字节的方式访问请求响应体
print('\n')
print(r.content.decode(encoding='utf-8'))
payload = {'key1':'value1','key2':['value2','value3']}
r2 = requests.get('https://httpbin.org/get',params=payload)
print(r2.url)