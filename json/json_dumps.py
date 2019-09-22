#!/usr/bin/python3
#conding=utf-8
import json
#
data = {'no':'1',
        'name': 'cuibo',
        'url': 'http://www.baidu.com'
        }

json_str = json.dumps(data)

print("Python原始数据：",repr(data))#将对象data转换为表达式字符串
print("Json对象：",json_str)