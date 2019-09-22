#coding=utf-8
"""
发送带附件为txt的邮件
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart#带附件要加上这个

sender = 'cb794788503@163.com'
receiver = '794788503@qq.com'
smtpserver = 'smtp.163.com'
username = 'cb794788503@163.com'
pwd = 'cb123456'#授权码而不是登陆密码
subject = '主题：这是带附件的邮件'

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(subject, 'utf-8')#传入主题参数subject

# 邮件正文内容
message.attach(MIMEText('这是Python邮件发送测试......', 'plain', 'utf-8'))

# 构造附件1（附件为TXT格式的文本）
att1 = MIMEText(open('test1.txt', 'w+').read(), 'base64', 'utf-8')#w+方式如果目录没有该文件，则
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test1.txt"'
message.attach(att1)

# 构造附件2（附件为JPG格式的图片）
att2 = MIMEText(open('test2.txt', 'w+').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="test2.txt"'
message.attach(att2)

# 调用smtplib模块进行发送，使用非本地SMTP服务器要进行SSL连接认证
try:
    send_email = smtplib.SMTP_SSL("smtp.163.com",465)
    send_email.login(username, pwd)
    send_email.sendmail(sender, receiver, message.as_string())
    send_email.quit()
    print("邮件测试发送成功，请查收！")
except smtplib.SMTPException as e:
    print("邮件发送失败，错误代码为：%s"%e)

#两个附件txt文档是空内容，如果想发带文字内容的可以用write()方法进行扩展