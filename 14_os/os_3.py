import os
"""
批量修改文件名

python 对文件进行批量改名用到的是 os 模块中的 listdir 方法和 rename 方法。

 os.listdir(dir) : 获取指定目录下的所有子目录和文件名
 os.rename(原文件名，新文件名） : 对文件或目录改名

"""
#把混乱的文件名改成有序的文件名:
path = input('请输入文件路径(结尾加上/)：')

# 获取该目录下所有文件，存入列表中
f = os.listdir(path)

n = 0
for i in f:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + f[n]

    # 设置新文件名
    newname = path + 'a' + str(n + 1) + '.JPG'

    # 用os模块中的rename方法对文件改名
    os.rename(oldname, newname)
    print(oldname, '======>', newname)

    n += 1