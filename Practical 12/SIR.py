#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:09:31 2019

@author: caitlynjiang
"""

import numpy as np
import matplotlib.pyplot as plt

# define basic variables
s = 9999
i = 1
r = 0
n = 10000
b = 0.3
y = 0.05

sarr = np.array ([s])
iarr = np.array ([i])
rarr = np.array ([r])

                                                                                # 1000 loop times
count=0
while count <= 1000:
    pofi = i/n                                                                  # Helped by Zhang Yiwei,at first I put this line before the loop and get a very flat wierd plot
    b2 = pofi*b
    b1 = 1-pofi*b
    niarr = np.random.choice(range(2),s,p=[b1,b2])
    nrarr = np.random.choice(range(2),i,p=[0.95,0.05])
    ni = np.sum(niarr==1)
    nr = np.sum(nrarr==1)
    s = s-ni
    i = i+ni-nr
    r = r+nr
                                                                                # record the output of each time step susceptible, infected, and recovered individuals) 
    
    sarr = np.append(sarr,s)
    iarr = np.append(iarr,i)
    rarr = np.append(rarr,r)
    count = count+1

                                                                                # plot(), xlabel(), ylabel(1), title(), legend()
plt.figure(figsize =(6,4),dpi=150)
plt.plot(sarr,label='susceptible')
plt.plot(iarr,label='infected')
plt.plot(rarr,label='recovered')
plt.xlabel("times") 
plt.ylabel("numbers of people")
plt.title("SIR model")
plt.legend()
plt.savefig ('Plot',type='png')






