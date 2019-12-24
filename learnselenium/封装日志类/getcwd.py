import os
"""
通过getcwd.py文件的绝对路径，来获得项目所在文件夹地址。其他一些获取路径的方法，会获取当前执行文件的路径，会导致路径错误
"""

def get_cwd():
    path=os.path.dirname(os.path.abspath(__file__))
    return path

#print(get_cwd())#调试查看下当前getcwd的目录