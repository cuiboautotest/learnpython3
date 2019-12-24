import yaml
file_1=open('./config.yml')
#data=file_1.read()
#print(data)
#print(type(data))
yml=yaml.load(file_1,Loader=yaml.FullLoader)
print(yml)
print(type(yml))