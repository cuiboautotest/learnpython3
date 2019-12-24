import os


os.getcwd()  # 获取当前工作目录
os.chdir()   # 更改当前工作目录 change
os.makedirs('dirname1/dirname2')  # 可生成多层递归目录
os.removedirs()  #（递归）删除空文件夹
os.mkdir('dirname')  # 生成一个文件夹
os.rmdir('dirname')  # 删除一个空文件夹，若文件不为空，报错
os.remove()   #只能删除文件，不能删除文件夹
os.listdir("G:\python")  # 显示出目录下的所有文件
os.rename('oldname','newname')  # 改变文件夹名称
os.path.dirname('./abc')  # 返回abc所在的文件的路径
os.path.exists(path)  # 如果path存在，返回Ture
os.path.join(path1,path2,) # 将多个路径合并并返回
os.path.abspath (__file__)  #将文件的相对路径转化为绝对路径
#if __name__ = "__main__":只会在自己模块中执行，外部调用模块时，不会执行