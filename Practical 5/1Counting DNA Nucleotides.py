#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:10:43 2019

@author: caitlynjiang
"""

DNA = "ATGCTTCAGAAAGGTCTTACGAACGGGCAATATGTCTCTGTGTGGATTA"
#DNAstring=' '.join(DNA)
#print (DNAstring)
#DNAstring = DNAstring.split(' ')
Dict = {}
for n in DNA:
       if n in Dict:
           Dict[n] += 1
       else:
           Dict[n] = 1
# about 1: if not been seen, set the count to one; if seen, add 1 to the count
print (Dict)

Dict.keys()

import matplotlib.pyplot as plt
labels=Dict.keys()
sizes= Dict.values()
explode = (0, 0.1, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()


