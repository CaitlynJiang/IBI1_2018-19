#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:10:23 2019

@author: caitlynjiang
"""

pam250 = readMatrix('pam250.txt')
seq1 = 'EREHSISIVLE'
seq2 = 'QNHKTLGFICN'
(values,directions) = buildNWTablesM(seq1,seq2,actionValuesDefault,pam250)
alignment = oneAlignment(directions, len(seq2), len(seq1))
showAlignment(alignment, seq1, seq2)