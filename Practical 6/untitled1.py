#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:01:30 2019

@author: caitlynjiang
"""

import re

emaillist=''
file = open(r'address_information.csv')
for line in file:
    line = line.rstrip()
    s = re.split(',', line)
    email = re.findall(r'\S+@\S+com|cn',line)
#    print (email)
    emaillist = emaillist + str(email)[1:-1]
print(emaillist)

 #   print(line)
   # print (s)
# cannot use path to open, cannot change directory, I finally moved the file to the same directory same as this code is stored.
#email = re.findall(r',(\S+@\S+),',line)
#,'r(.com|.cn)'
#print (email)

