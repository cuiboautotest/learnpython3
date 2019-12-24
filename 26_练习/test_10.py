'''
判断用户名和密码是否正确
'''
import getpass
user=input('输入用户名：')
pwd=getpass.getpass('输入密码：')
if user=='Bob' and pwd=='123456':
    print('登陆成功！')
else:
    print('登陆失败')
