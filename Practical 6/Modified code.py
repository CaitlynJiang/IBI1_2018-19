#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:32:43 2019

@author: caitlynjiang
"""

import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

file = open(r'address_information.csv')
for l in file:
    l = l.rstrip()
    #print (l)
    emails = re.findall(r',\S+@\S+,',l)
# if (r',(\S+@\S+),',l), means not include commas using parenthesis）
#    print(emails)
    for i in emails:
        if re.match(r'\S+@\S+com|cn',l):
            name = str(re.findall(r'.com,To (\S+):',l))
            name = name[2:-2]
            #print(name)
            i=i[1:-1]
            #print (i)
            print(i,':Correct Address!')
            mail_host="smtp.zju.edu.cn"  
            mail_user="3180111436"    
            mail_pass="*****"   #This cannot run for this is a fake password
 
 
            sender = '3180111436@zju.edu.cn' #my zju email
            receivers = [i]  

            text= open(r'body.txt','r')
            Mt=''
            for words in text:
                Mt=Mt+words
                
            Sj="To User: Your analysis has been finished!"
            Mt = re.sub(r'User',name,Mt) 
            Sj = re.sub(r'User',name,Sj)
            print (Sj) # Pseudo these two print lines if donnot want to see the content shown in the consoel. P.S. This is for showing the content of the email for the emails cannot be sent unless correct email address with correct password is provided 
            print (Mt) # Note: the sender's name will not be shown in the console
 
            message = MIMEText(Mt, 'plain', 'utf-8')
            message['From'] = Header("Caitlyn", 'utf-8')
            message['To'] =  Header("test", 'utf-8')
 
            subject = Sj
            message['Subject'] = Header(subject, 'utf-8')
 
 
            try:
                
                smtpObj = smtplib.SMTP() 
                smtpObj.connect(mail_host, 25)   
                smtpObj.login(mail_user,mail_pass)  
                smtpObj.sendmail(sender, receivers, message.as_string())
                print ("Mail sent seccesfully!")
            except smtplib.SMTPException:
                print ("Error: Failed to send mail")
            
        else:
            print(i[1:-1],':Wrong Address!')
            
