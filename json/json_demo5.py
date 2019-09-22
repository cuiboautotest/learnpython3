import json
# 写入 JSON 数据
with open('data1.json', 'w') as f:
    json.dump(data1, f)

# 读取数据
with open('data1.json', 'r') as f:
    data = json.load(f)


'''
如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到json.dump(),

json.load()用于从json文件中读取数据.

with open('data3.json','a',encoding='utf-8') as f: 
    f.write(data1)
    f.close()
data4=json.load(open('data3.json'))#json.load（）用于读取json数据
print(data4)
'''