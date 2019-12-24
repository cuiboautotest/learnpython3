"""
绝对路径就是文件的真正存在的路径，是指从硬盘的根目录(盘符)开始，进行一级级目录指向文件。
   相对路径就是以当前文件为基准进行一级级目录指向被引用的资源文件。
    以下是常用的表示当前目录和当前目录的父级目录的标识符
  
../ 表示当前文件所在的目录的上一级目录
./ 表示当前文件所在的目录(可以省略)
/ 表示当前站点的根目录(域名映射的硬盘目录)


--------------------------------------------------------------------------------

if __name__ == '__main__' 我们简单的理解就是： 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。


--------------------------------------------------------------------------------
有一个文件夹/home/a, 里面有个模块叫b.py, 我怎么把他import到程序里？

方法一:    (属于刚开始分析的代码里第一种情况)

import sys;
sys.path.append(“/home/a/”) #添加相关的路径
import b

方法二：

  在目录里面增加__init__.py文件，里面可以写import时执行的代码，当然也可以留空就可以.
import home.a.b

方法三：

from home.a.b import *
  前提 home、a中都包括__init__.py 即：要导入的文件的当前目录和父目录都要有init.py文件


举例
1）主程序与模块程序在同一目录下:

如下面程序结构:
– src
  |– mod1.py
  |– test1.py

  若在程序test1.py中导入模块mod1, 则直接使用import mod1或from mod1 import *;

（2）主程序所在目录是模块所在目录的父(或祖辈)目录
如下面程序结构:
– src
|– mod1.py
|– mod2
  | – mod2.py
– test1.py

  若在程序test1.py中导入模块mod2, 需要在mod2文件夹中建立空文件__init__.py文件(也可以在该文件中自定义输出模块接口); 然后使用 from mod2.mod2 import * 或import mod2.mod2.

（3）主程序导入上层目录中模块或其他目录(平级)下的模块
如下面程序结构:
– src
  |– mod1.py
  |– mod2
   |– mod2.py
  |– sub
    | – test2.py
  – test1.py
  若在程序test2.py中导入模块mod1.py和mod2.py。首先需要在mod2下建立__init__.py文件(同(2))，src下不必建立该文件。然后调用方式如下:
  下面程序执行方式均在程序文件所在目录下执行，如test2.py是在cd sub;之后执行python test2.py
而test1.py是在cd src;之后执行python test1.py; 不保证在src目录下执行python sub/test2.py成功。
import sys
sys.path.append(“..”)
import mod1
import mod2.mod2
"""
import os
path1=os.path.abspath('.')#当前所处文件夹的绝对路径
print(path1)

path2=os.path.abspath('..')#表示当前所处文件的上一级文件夹的绝对路径（父亲目录）
print(path2)


dir1=os.path.dirname(os.path.abspath('.'))#获取当前项目的根目录的相对路径
print(dir1)

path3=os.getcwd()#获取当前工作目录
print(path3)


#当我们导入一个模块时：import  xxx，默认情况下python解析器会搜索当前目录、已安装的内置模块和第三方模块，搜索路径存放在sys模块的path中
#sys模块包含了与python解释器和它的环境有关的函数,print(dir(sys))
import sys
print(sys.path)#返回值是一个列表
#该路径已经添加到系统的环境变量了，当我们要添加自己的搜索目录时，可以通过列表的append()方法；对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append('xxx')：sys.path.append(’引用模块的地址')

'''
我的总结：
每一个.py文件对应一个__init__.py文件，这个文件的当前路径为.py所在的目录文件夹
不同文件夹之间引用，需要添加环境变量

'''

#python3 的写法，获取相对路径应该是os.path.dirname(os.path.abspath('.'))





