st={}


print(st.get('name'),None)#默认是None

print(st.get('cuibo'))#如果前面不存在则返回空字典

print(st.get('name'),'未指定')

print(st['name'])#这样取值会报错，因为不会返回None
