import json
if __name__ == "__main__":
    print("将python对象转化为json对象并存储到文件")
    data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]
    with open('json_write.json','w') as f:#自动生成该文件
    #以可读性格式写入文件中
        json.dump(data,f,sort_keys=True,indent=4,separators=(',',':'))
