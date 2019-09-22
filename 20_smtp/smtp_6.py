#!/usr/bin/python3

import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr
from email.utils import formataddr
# from email.mime.multipart import MIMEMultipart

sender = 'cb794788503@163.com'
username='cb794788503@163.com'
pwd='cb123456'

receiver = '794788503@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
subject = 'Python SMTP 邮件测试'
smtpserver='smtp.163.com'#服务器是smtp.163.com而不是smtp@163.com
#body=‘Python 邮件发送测试...\n收到邮件请回复！’----------------通过变量引入
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...时间是23：20\n收到邮件请回复！', 'plain', 'utf-8')
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
try:
    send_email = smtplib.SMTP_SSL("smtp.163.com",465)
    send_email.login(username, pwd)
    send_email.sendmail(sender, receiver, message.as_string())
    send_email.quit()
    print("邮件测试发送成功，请查收！")
except smtplib.SMTPException as e:
    print("邮件发送失败，错误代码为：%s"%e)

