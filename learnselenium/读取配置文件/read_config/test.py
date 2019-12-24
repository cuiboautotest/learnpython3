import os
import configparser
'''
模块常用函数：
1）读取配置文件
read(filename) 直接读取ini文件内容
sections() 得到所有的section，并以列表的形式返回
options(section) 得到该section的所有option
items(section) 得到该section的所有键值对
get(section,option) 得到section中option的值，返回为string类型
getint(section,option)得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。
2）写入配置文件
add_section(section) 添加一个新的section
set( section, option, value) 对section中的option进行设置，需要调用write将内容写入配置文件。
'''
class ReadConfigFile(object):


    def get_value(self):
        # 创建conf对象
        conf = configparser.ConfigParser()

        # 文件所在目录
        root_dir = os.path.dirname(os.path.abspath('.'))
        # print(root_dir)

        # 将路径拼接成 /读取配置文件/config/config.ini
        file_path = root_dir + '/config/config.ini'
        # print(file_path)

        #读取配置文件
        conf.read(file_path)
        browser=conf.get("browserType","browserName")
        url=conf.get("testServer","URL")

        return (browser,url)

    def write_value(self):
        # 创建conf对象
        conf = configparser.ConfigParser()

        # 文件所在目录
        root_dir = os.path.dirname(os.path.abspath('.'))
        # print(root_dir)

        # 将路径拼接成 /读取配置文件/config/config.ini
        file_path = root_dir + '/config/config.ini'
        # print(file_path)

        '''
        开始写配置文件，文件内容如下
        [mysql]
        ip = 127.0.0.1
        port = 3306
        username=cuibo
        password=123456   
        '''
        conf.add_section('mysql')
        conf.set('mysql','ip','127.0.0.1')
        conf.set('mysql','port','3306')
        conf.set('mysql','username','cuibo')
        conf.set('mysql','password','123456')
        conf.write(open(filepath,'w'))





trcf=ReadConfigFile()
print(trcf.get_value())
print(trcf.write_value)


