#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:24:35 2019

@author: caitlynjiang
"""

import itertools

print('Please input N numbers in the range of 1 to 23:')
Num=input()
print("Input numbers:" + Num)

L=Num.split(',')
S = ''.join(L)
A=len(S)
a=A-1
#print(a)
lis=[]
for i in itertools.permutations(S,A):
    #print(i)
    lis.append(i)
#print(lis)
    
lis2=[]
for i in lis:
        if i not in lis2:
            lis2.append(i)
print(lis2)


