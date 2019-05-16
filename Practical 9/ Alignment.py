#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:18:06 2019

@author: caitlynjiang
"""

def readmatrix(filename):                                                    # define function to read matrix so that it can be used to read different kinds of BLOSUM file
  handle = open(filename, "r")
  content = handle.readlines()
  handle.close()

  matrix = {}
  letters = []

  first = True
  for line in content:
    splitted = line.split()
    if first:
      for a in splitted:
        matrix[a] = {}
        letters.append(a)
      first = False
    else:
      a = splitted[0]
      for i in range(1, len(splitted)):
        b = letters[i-1]
        matrix[a][b] = splitted[i]

  return matrix

def ipercent(a,b):                                                              # define function to calculate identical percentage
    count=0
    total=len(a)
    x=0
    for i in a:
        if a[x]==b[x]:
            count +=1
            x+=1
        else:
            count=count
            x+=1
    if count!=0:
        iscore=str('%.2f' % ((float(count)/total)*100))+'%'                    # Reserve the percentage of two decimal places
    else:
        iscore=0
        return iscore
    
def snormal(c,d):                                                              # New function to normalise score according to lenth
    lenth1=len(c)
    nmlzds=d/lenth1
    return nmlzds
 
matrix=readmatrix("BLOSUM62.txt")                                               # file found in a gov website, relatively trustable
#print(matrix)

seq01 = input("Please put in sequence1:" )                                      # here copy and paste the sequence
name1 = input("Please write down the name of sequence1:")
seq02 = input("Please put in sequence2:" )
name2 = input("Please write down the name of sequence2:")
seq1 = seq01.replace(' ', '')                                                   # delete the blank space in the sequence (probably \n is necessary)
seq2 = seq02.replace(' ', '')
if len(seq1)==len(seq2):                                                        # Error dectecting of different sequence lenth
    score = 0
    for i in range (len(seq1)):
        score += int(matrix[seq1[i]][seq2[i]])
    nmlzds='%.2f' %(snormal(seq1,score))   
    pis = ipercent(seq1,seq2)                                    

    print("The score of",name1,"and",name2,"is",score)
    print("The percentage identity is",pis)
    print("The normalised BLOUSUM score of",name1,"and",name2,"is",nmlzds)

else:
    print('Error: Please input sequences that have the same lenth!' )

