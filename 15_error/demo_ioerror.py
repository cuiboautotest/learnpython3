#coding=utf-8
try:
    f=open('testfile.txt',"w")
    f.write("这是一个测试文件，用于测试异常！")
#except IOError as e:自定义异常
#    print(e)
except IOError:
    print('Error:',没有找到文件或读取文件失败)
else:
    print("内容写入文件成功")
    f.close()