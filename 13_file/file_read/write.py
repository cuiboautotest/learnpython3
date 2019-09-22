#f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
f = open("E:/python/python3/learnpython/13_file/file_read/foo.txt","w",encoding="utf-8")
f1=f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(f1)