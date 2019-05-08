#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:38:38 2019

@author: caitlynjiang
"""

from xml.dom.minidom import parse
import  xml.dom.minidom

domtree = xml.dom.minidom.parse('go_obo.xml')

root = domtree.documentElement
genepool=root.getElementByTagName("gene")

n


print (root.nodeName)
print (root.nodeValue)
print (root.nodeType)
print (root.ELEMENT_NODE)
