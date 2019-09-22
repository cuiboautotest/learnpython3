import json

data = {
    'name' : 'Connor',
    'sex' : 'boy',
    'age' : 26
}
print(data)
data1=json.dumps(data)
print(data1)
data2=json.loads(data1)
print(data2)
print(type(data))#输出原始数据格式
print(type(data1))#输出经过json.dumps的数据格式
print(type(data2))#输出经过json.loads的数据格式
