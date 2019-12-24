
import os
base_dir = os.path.dirname(__file__)# 获取当前文件目录
path = os.path.join(base_dir,'123.txt')#获取文件拼接后的路径
print(base_dir)
print(path)
print(os.path.split(path))#分割成字符串

