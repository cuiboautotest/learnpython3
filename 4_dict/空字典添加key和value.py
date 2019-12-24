'''
data={}
data['name']='cuibo'
print(data)
'''

data1={}
json={'name':'cuibo1','num':12}
for key in json.keys():
    #if json[key]=='' or json[key] is None:
    #   continue
    #print(json[key])
    data1[key]=json[key]#key=name时，json[key]=cuibo,第一次取值把cuibo赋值给 data1[name]，所以data1这时变成{'name':'cuibo'},再循环一次，再添加一个key-value，num=12
    print(data1)
