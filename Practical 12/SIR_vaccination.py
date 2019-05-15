#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:09:31 2019

@author: caitlynjiang
"""

import numpy as np
import matplotlib.pyplot as plt

# define basic variables
#s = 9999
#i = 1
r = 0
n = 10000
b = 0.3
y = 0.05
listtotal=[]


for a in range (0,11):
    vc =int(a/10*n)
    if vc==n:
        s=0
        i=0
    else:
        s=n-vc-1
        i=1
        r=0
    iarr = np.array ([i])
                                                     
    count=0
    while count <= 1000:
        pofi = i/n                                                              
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
        iarr = np.append(iarr,i)
        count = count+1
    listtotal.append(list(iarr))                                                # maybe it'll be easier using the list but not array...
    #print (listtotal)

                                                                                # plot(), xlabel(), ylabel(1), title(), legend()
plt.figure(figsize =(6,4),dpi=150)
x = range(0,1001)
y = range(0,10001)
for b in range(0,11):                                                           # plot all the lines in the same image
    plt.plot(listtotal[b],label=str(b*10)+'%') 
plt.xlabel("times") 
plt.ylabel("numbers of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.savefig ('Plot_vaccination',type='png')






