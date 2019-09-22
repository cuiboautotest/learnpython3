#coding=utf-8
"""
混合发送，带文字，带HTML，带图片的类型
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
att1 = MIMEText(open('text5.txt', 'w+').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="text5.txt"'
message.attach(att1)

# 构造附件2（附件为JPG格式的图片）
att2 = MIMEText(open('123.jpg', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
message.attach(att2)

# 构造附件3（附件为HTML格式的网页）
att3 = MIMEText(open('report_test.html', 'rb').read(), 'base64', 'utf-8')
att3["Content-Type"] = 'application/octet-stream'
att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
message.attach(att3)

# 调用smtplib模块进行发送，使用非本地SMTP服务器要进行SSL连接认证
try:
    send_email = smtplib.SMTP_SSL("smtp.163.com",465)
    send_email.login(username, pwd)
    send_email.sendmail(sender, receiver, message.as_string())
    send_email.quit()
    print("邮件测试发送成功，请查收！")
except smtplib.SMTPException as e:
    print("邮件发送失败，错误代码为：%s"%e)