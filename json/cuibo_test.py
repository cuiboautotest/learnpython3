import json
dict1={'name':'cuibo','number':123}
print(type(dict1))
#序列化，把python的数据类型转换为json格式的字符串
str1=json.dumps(dict1)
print("序列化dict1：",str1)
print(type(str1))
#反序列化,将json格式的字符串解码为python的数据对象
dict2=json.loads(str1)
print("反序列化str1：",dict2)
print(type(dict2))