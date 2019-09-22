#f.readlines() 将返回该文件中包含的所有行。
f = open("E:/python/python3/learnpython/13_file/file_read/foo.txt","r",encoding="utf-8")
print(f.readlines())

#等价于
#for line in f:
#   print(line,end='')