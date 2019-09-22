#!/usr/bin/python3
#conding=utf-8
import json
#
data = {'no':'1',
        'name': 'cuibo',
        'url': 'http://www.baidu.com'
        }

json_str = json.dumps(data)

print("Python原始数据：",repr(data))
print("Json对象：",json_str)

data1 = json.loads(json_str)
print(data1['name'])
print(data1['url'])
print(data1['no'])

#如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
