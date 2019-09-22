# !/usr/bin/python3
# coding: utf-8
'''
发送HTML格式邮件
'''
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr
from email.utils import formataddr


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))


sender = "cb794788503@163.com" # 邮箱地址
username="cb794788503@163.com"
pwd = "cb123456"  # 授权码
receiver = "794788503@qq.com" # 接收者邮箱
smtp_server = "smtp.163.com"
#如果是HTML，3个参数中第一个内容就写HTML，第二个参数换成html
msg = MIMEText("<html><body><h3>hello</h3><p>hello, send by python</p></body></html>", "html", "utf-8")
#如果参数内容过长，可以采用如下，将第一个参数以变量的方式引入
#mail_msg="xxxxx" 传参直接传入mail_msg

msg["From"] = format_addr("%s" % (sender))
msg["To"] = format_addr("%s" % (receiver))
msg["Subject"] = Header("python email测试：by cuibo", "utf-8").encode()

try:

    server = smtplib.SMTP_SSL(smtp_server, port=465) #网易企业邮箱配置（SSL）
    # server = smtplib.SMTP(smtp_server, port=25) # 网易126邮箱
    server.set_debuglevel(1)
    server.login(username,pwd)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    print("带HTML格式邮件发送成功！")
except smtplib.SMTPException as e:
    print("HTML格式邮件发送失败.Case:%s"%e)
