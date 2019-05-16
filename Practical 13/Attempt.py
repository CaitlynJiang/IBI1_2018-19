#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:57:41 2019

@author: caitlynjiang
"""
import xml.dom.minidom

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
# 