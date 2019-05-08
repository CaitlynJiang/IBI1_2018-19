#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:58:16 2019

@author: caitlynjiang
"""

from Bio.SubsMat.MatrixInfo import blosum62 as blosum
from itertools import izip

blosum.update(((b,a),val) for (a,b),val in blosum.items())

def score_pairwise(seq1, seq2, matrix, gap_s, gap_e, gap = True):
    for A,B in izip(seq1, seq2):
        diag = ('-'==A) or ('-'==B)
        yield (gap_e if gap else gap_s) if diag else matrix[(A,B)]
        gap = diag

seq1 = 'PAVKDLGAEG-ASDKGT--SHVVY----------TI-QLASTFE'
seq2 = 'PAVEDLGATG-ANDKGT--LYNIYARNTEGHPRSTV-QLGSTFE'

print sum(score_pairwise(seq1, seq2, blosum, -5, -1))