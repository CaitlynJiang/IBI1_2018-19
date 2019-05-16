#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:22:03 2019

@author: caitlynjiang
"""

import numpy as np
import matplotlib . pyplot as plt

population = np.zeros((100, 100))
outbreak = np.random.choice(range(100),2)                                       # pick 2 random number in the range(100) to become x, y
population[outbreak[0],outbreak[1]] = 1                                         # Coordination: x,y = Random choice 0 an 1

def drawmap(i, population):                                                     # define function to draw hotmap
    if i in [1, 10, 50, 100]:                                                   # show (later save) the plot at time 1,10,50,100 (as given as sample plots)
        plt.figure(figsize=(6,4), dpi=150)                         
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.savefig ('Plot_spatial'+str(i),type='png')                          # save the plot every time
    return

b=0.3                                                                           # initialize parameters: beta and gamma
g=0.05

'''
my pseudo codes for preperation:
- How will you find the infected points?:
      where()
      infected people = np.where(population==1)
      
– For each infected point, how do you address all its neighbours? Are there cases where this could be difficult?:
    by using x-1,x+1,y-1,y+1...
    yes, may 'infect' oneself. use (formal) (x,y) != (x,y)
    and also, when the position in nparray reaches the edge. use x/y != -1 and 100
    
– How do you check that neighbours are not recovered?:
    only if ==0
    
– How do you infect the neighbours?:
    population[newx,newy]=np.random.choice(range(2),1,p=[1-b,b])
    
– How do you allow infected individuals to recover?:
    inf = np.where(population==1)
    
– How can you plot the outcome? (You don’t need to worry about saving the images for now, unless you want to):
    define a function to draw the hotmap at the time 1, 10, 50, 100
Btw, where is this(below) infection_snippet come from?    
'''

for i in range(0,101):
    drawmap(i,population)                                                       # find infected points
    infectedIndex = np.where(population==1)
    for i in range(0,len(infectedIndex[0])):
        x = infectedIndex[0][i]                                                 # get x, y coordinates for each point
        y = infectedIndex[1][i]
        for xNeighbour in range(x-1,x+2):                                      
            for yNeighbour in range(y-1,y+2):                                   # try to infect each neighbour with probability beta (infect all 8 neighbours)
            # don't infect yourself! (Is this strictly necessary?)              # Not necessary, because below it writes if ...=0
                if (xNeighbour,yNeighbour) != (x,y):                            # don't fall off an edge ⬇️
                     if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        if population[xNeighbour,yNeighbour]==0:                # only infect neighbours that are not already infected
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-b,b])[0]
        r = np.random.choice(range(2),1,p = [1-g,g])                            # try to recover each neighbour with probability gamma, 1 for recover, 0 for not
        if r == 1:
           population[x,y]=0.5
    

    
    
















