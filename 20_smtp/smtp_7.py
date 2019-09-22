#!/usr/bin/python3
"""
我第一次测试邮件发送成功啦-----------------------------------！！！！！！！！！！！！！！！！
"""
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr
from email.utils import formataddr
# from email.mime.multipart import MIMEMultipart
smtpserver='smtp.163.com'#设置smtp服务器

username='cb794788503@163.com'#用户名
pwd='cb123456'#授权码

sender = 'cb794788503@163.com'
receiver = '794788503@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
subject = 'Python SMTP 邮件测试'

#body=‘Python 邮件发送测试...\n收到邮件请回复！’----------------通过变量引入
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...\n收到邮件请回复！', 'plain', 'utf-8')
#message = MIMEText('body', 'plain', 'utf-8')
'''
message['From'] = Header("邮件测试", 'utf-8')  # 发送者
message['To'] = Header("测试ing..........", 'utf-8')  # 接收者
message['Subject'] = Header(subject, 'utf-8')
'''
message['From'] = sender
# 作用同'From'
message['To'] = receiver
message['Subject']=Header(subject,'utf-8')

# 调用smtplib模块进行发送
try:#不加判断不知道到底发送成功没有，错误会抛出smtp异常代码
    #使用非本地服务器，需要建立SSL连接
    send_mail = smtplib.SMTP_SSL("smtp.163.com",465)
    send_mail.login(username, pwd)
    send_mail.sendmail(sender, receiver, message.as_string())
    send_mail.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error：无法发送邮件.Case：%s"%e)
