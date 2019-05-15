#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:01:24 2019

@author: caitlynjiang
"""
import numpy as np

with  open(r'/Users/caitlynjiang/OneDrive/IBI1_2018-19/Practical13/modelResults.csv' , 'r') as f:
    lines = f.readlines()
    first_line = lines[0]
    f.close()
    fl=first_line[:-1].split(',')
    names=np.array(fl)
    
    other_lines=lines[1:-1]
    ol=[]
    for i in other_lines:
        i=i[:-1]
        l=i.split(',')
        #print(l)
        ol.append(l)
    results=np.array(ol)
    results = results.astype(np.float)
    print(results [1 ,1])
    
