"""
读写权限：
1、如果文件不存在
读文件会报错
写文件会创建文件
2、如果文件用于读权限
不可以进行写操作
反之亦然

read读全文
w覆盖文件已有内容
a追加内容
readline每次读一行，再次调用再读一行
writelines可以写

"""
#通过写操作写入hello
with open("1.txt","w")as f:
    #print(f.read())
    f.write("hello\n")

#读上一步系的内容
with open("1.txt","rb") as e:
    content = e.read().decode()#
    print(content)

#追加内容
with open("1.txt","a") as h:
    f.writelines(["a", "b", "c", "d"])