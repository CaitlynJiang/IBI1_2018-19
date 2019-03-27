#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:18:10 2019

@author: caitlynjiang
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.zju.edu.cn"  #设置服务器
mail_user="3180111436"    #用户名
mail_pass="Fuga@7831"   #口令 
 
 
sender = '3180111436@zju.edu.cn'
receivers = ['1051751858@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

name="1"
Mt="Dear User,\nPlease find the results of your gene set linkage analysis result in attached file.\nThis is an email sent by the server, please don't reply.\nThank you for using GSLA."
Sj="To User: Your analysis has been finished!"
Mt = re.sub(r'User',name,Mt) 
Sj = re.sub(r'User',name,Sj)
print (Mt)
print (Sj)
 
message = MIMEText(Mt, 'plain', 'utf-8')
message['From'] = Header("Caitlyn", 'utf-8')
message['To'] =  Header("test", 'utf-8')
 
subject = Sj
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")