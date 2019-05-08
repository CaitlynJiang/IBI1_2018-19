#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:18:06 2019

@author: caitlynjiang
"""



def readmatrix(filename):
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

matrix=readmatrix("BLOSUM62.txt")
#print(matrix)

seq01 = input("Please put in sequence1:" )
name1=input("Please write down the name of sequence1:")
seq02 = input("Please put in sequence2:" )
name2=input("Please write down the name of sequence2:")
seq1=seq01.replace(' ', '')
seq2=seq02.replace(' ', '')
score = 0
for i in range (len(seq1)):
    score += int(matrix[seq1[i]][seq2[i]])

print("The score of",name1,"and",name2,"is",score)

