"""
json格式化
sort_keys：是否按照字典排序（a-z）输出，True代表是，False代表否。
indent=4：设置缩进格数，一般由于Linux的习惯，这里会设置为4。
separators：设置分隔符，在dic = {'a': 1, 'b': 2, 'c': 3}这行代码里可以看到冒号和逗号后面都带了个空格，这也是因为Python的默认格式也是如此，如果不想后面带有空格输出，那就可以设置成separators=(',', ':')，如果想保持原样，可以写成separators=(', ', ': ')
ensure_ascii=False ：是否显示ascii这个码，默认是ture，改为False 即可

"""
import json
if __name__ =="__main__":
    print("python json串格式化实例")
    data = [{"a":1,"b":2,"c":3,"d":4,"e":5}]
    json_data = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'))
    print(json_data)