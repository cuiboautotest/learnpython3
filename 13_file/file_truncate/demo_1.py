import os
#print(os.getcwd())
#file=os.getcwd()+'/tmp/bbb'
#print (file)
f=open("./tmp/bbb",'r+',encoding='utf-8')
print(f.name)
f.seek(36)#光标停在36个字节上
f.tell()
f.truncate()#从第36个字节以后内容全部删除了
f.seek(0,0)#光标停留在第0行第0列
line=f.readlines()
print(line)
f.truncate(10)#
f.seek(0,0)
print(f.read())
f.close()

'''
1:www.runoob.com
2:www.runoob.com
3:www.runoob.com
4:www.runoob.com
5:www.runoob.com
第一次截取，第一行共18个字节，最后省略了换行\n，单行共18个字节
所以从36字节开始删除，即是345行均删除
第二次删除，从第10个后面开始删除，光标停留在o后面为第十个
'''