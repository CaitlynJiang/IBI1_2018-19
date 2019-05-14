#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:26:00 2019

@author: caitlynjiang
"""

s = input('Please input a sentence:')
s=s[::-1]
s=s.split(' ')
s.sort()
s.reverse()
print(s)