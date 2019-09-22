#coding:utf-8
#导入request库
import  requests
#请求URL
url = "https:www.baidu.com"
res = requests.get(url=url)
print(res.json())
