#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:38:38 2019

@author: caitlynjiang
"""
# Note: I didn't come to the practical on time beacause I went to the hospital (I've asked for premission from my acdemic advisor). So this code is edit one day later, and apology that might be very similar to sample code given in the tutorial...

import xml.dom.minidom
import re
import pandas as pd                                                             # pandas.DataFrame.to_excel

def child(id, resultset):                                                       # Add parameters!!
    for i in terms:
        parents = i.getElementsByTagName('is_a')
        geneid = i.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultset.add(geneid)                                           # from tutorial:  don't use resultset = resultset |set([geneid]) or will create a new set instead of modifying the existing one
                child(geneid, resultset)
        
df = pd.DataFrame(columns = ['id','name','definition','childnodes'])            # create a panda.dataframe to store the output   
DomTree = xml.dom.minidom.parse('go_obo.xml')                                   # didn't use filepath beacause I set the xml file under the same directory
terms = DomTree.documentElement.getElementsByTagName('term')


for term in terms:
     genetype = term.getElementsByTagName('defstr')[0].childNodes[0].data
     defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
     if re.search('autophagosome',genetype):
        id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        resultset = set()
        child(id, resultset)
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[genetype],'childnodes':[len(resultset)]}))

df.to_excel('autophagosome.xlsx',index=False)                                   # save data as an excel file

