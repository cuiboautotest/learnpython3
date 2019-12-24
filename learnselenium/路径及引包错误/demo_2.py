import os
# 获取当前文件的路径
real_path = os.path.realpath(__file__)
# 从当前文件路径中获取目录
file_dir = os.path.dirname(real_path)
# 从当前文件路径中获取文件名
file_name = os.path.basename(real_path)

print(real_path)
print(file_dir)
print(file_name)
# 只显示该目录下的文件名和目录名
# 不包含子目录中的文件，默认为当前文件所在目录
print(os.listdir(file_dir))