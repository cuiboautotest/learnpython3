#"r"以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
f = open("E:/python/python3/learnpython/13_file/file_read/foo.txt","r",encoding="utf-8")
print(f.readline())