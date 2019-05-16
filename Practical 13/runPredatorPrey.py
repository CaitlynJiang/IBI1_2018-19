#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:01:24 2019

@author: caitlynjiang
"""
import numpy as np
import matplotlib.pyplot as plt
import xml.dom.minidom

with  open(r'/Users/caitlynjiang/OneDrive/IBI1_2018-19/Practical 13/modelResults.csv' , 'r') as f:
    lines = f.readlines()  # read all the lines
    first_line = lines[0]
    f.close()
    fl=first_line[:-1].split(',')
    names=np.array(fl)     #first array
    
    other_lines=lines[1:-1]
    ol=[]
    for i in other_lines:
        i=i[:-1]
        l=i.split(',')
        ol.append(l)       # list of list
    results=np.array(ol)   # second array that contains the result data
    results = results.astype(np.float)

plt.plot(results[:,0],results[:,1], label='Predator (b=0.02,d=4)')
plt.plot(results[:,0],results[:,2], label='Prey (b=0.1,d=0.02')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()
plt.show()
# plot a time course of the predator and prey population
plt.plot(results[:,1],results[:,2])
plt.xlabel('predator population')
plt.ylabel('prey populaition')
plt.title('Limit cycle')
plt.show() # plot A limit cycle plot: predator population against prey population.
           # (Why would this be useful or interesting?) Useful for analysis about relationship between species.


DomTree = xml.dom.minidom.parse('predator-prey-copy.xml')
parameters = DomTree.documentElement.getElementsByTagName('parameter') # find parameters and form a node list
#print(parameters)

parameters[0].setAttribute('value','0.1') # change the value in node list
parameters[1].setAttribute('value','0.2')
parameters[2].setAttribute('value','0.3')
parameters[3].setAttribute('value','0.4')

f = open('predator-prey.xml','w')         # write into the file
DomTree.writexml(f)
f.close()

# At first I use the file predator-prey.xml, and it doesn't work, I 'borrow ' a file from Jessie and that work...it might be some damage in the previous file
# Thoughts for the following tasks(task 5 haven't complete)
# 1. plot new images: use the same algorithm as before, but lable needed to be find with getAttribute(‘id’)==‘k_predator/prey_breeds/dies’
# 2. For task 6: add function to pick random value (numpy.random.sample()), loop 100 times or more, maybe save plots
# 3. what you would like the output to be: put the certain results (like minimum of prey number under different parameters) out in a array like before and plot them in another plot



