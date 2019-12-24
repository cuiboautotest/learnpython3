import json
'''
jsonstr="{'name':'cuibo'}"
dict=json.loads(jsonstr)
print(dict)
print(dict.keys())
'''

data={'ids':1,'name':'cuibo','age':1}#字典
json_str=json.dumps(data)
print(json_str)#转化之后单引号变双引号
print(type(json_str))#json实质是字符串
print(repr(data))#再次输出原数据

#json格式转字典
dict=json.loads(json_str)
print(dict)
print(dict.keys())
print(dict['name'])

#遍历key值
for k in dict.keys():
    print(k)



