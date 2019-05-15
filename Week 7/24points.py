#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:24:35 2019

@author: caitlynjiang
"""

from fractions import Fraction


#use function to add tomrecursion times
def dfs(n):
    global count
    global l
    count=count+1
    
    if n==1:
        if (float(l[0])==24):
            return 1
        else:
            return 0
        
    for i in range (0,n):
        for j in range (i+1,n):
            a=l[i]
            b=l[j]
            l[j]=l[i-1]
                
            l[i]=a+b
            if(dfs(n-1)):
                return 1                
                
            l[i]=a-b
            if(dfs(n-1)):
                return 1
                
            l[i]=b-a
            if(dfs(n-1)):
                return 1
                
            l[i]=a*b
            if(dfs(n-1)):
                return 1
                
            if a:
                l[i]= Fraction(b,a)
                if(dfs(n-1)):
                    return 1
                
            if b:
                l[i]= Fraction(a,b)
                if(dfs(n-1)):
                    return 1
            l[i]=a
            l[j]=b
    return 0
                    
print('Please input N numbers in the range of 1 to 23\n(use commas to separate):')
num=input()
# whether input format is correct
l=num.split(',')
a=False
for i in l:
    if i.isdigit()==True:     
        #print(i)
        if not 1<=int(i)<=23:
            a=False
            break
        else:
            a=True
    else:
        a=False
        break
        
if a==False:
    print('The input number must be intergers from 1 to 23')
else:
    print("Input numbers:" + num)
    l=list(map(int,l))
    #n=len(l)
    count=0
    if a==True:    
        if (dfs(len(l))): # returns 0
            print('Yes')
        else: 
            print('No')
        print ('recurtion times:',count)
                
            
        

