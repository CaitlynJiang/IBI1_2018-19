#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:22:03 2019

@author: caitlynjiang
"""

import numpy as np
import matplotlib . pyplot as plt

population = np.zeros((100, 100))
outbreak = np.random.choice(range(100),2) 
population[outbreak[0],outbreak[1]] = 1 # Random choice 0 an 1? (first 2?= 2 random number)

def drawmap(i, population):
    if i in [1, 10, 50, 100]:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.savefig ('Plot_spatial'+str(i),type='png')
    return

b=0.3
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
    drawmap(i,population)
    # find infected points
    infectedIndex = np.where(population==1)
# loop through all infected points
    for i in range(0,len(infectedIndex[0])):
        
    # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?): 
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)Not necessary, because below it writes if ...=0
                if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                     if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-b,b])[0]
        r = np.random.choice(range(2),1,p = [1-g,g])
        if r == 1:
           population[x,y]=0.5
    

    
    
















