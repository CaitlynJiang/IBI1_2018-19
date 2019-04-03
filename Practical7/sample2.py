#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:41:49 2019

@author: caitlynjiang
"""

class Solution(object):
    def judgePoint24(self, nums):
        def get_result(order):
            numbers = []
            result = 0
            
for word in order:
    if ord(word) > ord('0') and ord(word) <= ord('9'):
        numbers.append(float(ord(word) - ord('0')))
    else:
        if word=='+':
            n2 = numbers.pop(-1)
            n1 = numbers.pop(-1)
            numbers.append(n1 + n2)
        if word == '-':
            n2 = numbers.pop(-1)
            n1 = numbers.pop(-1)
            numbers.append(n1 - n2)
        if word == '*':
            n2 = numbers.pop(-1)
            n1 = numbers.pop(-1)
            numbers.append(n1 * n2)
        if word == '/':
            n2 = numbers.pop(-1)
            n1 = numbers.pop(-1)
if n2 == 0:
    return 0
else:
    numbers.append(n1 / n2)

return int(numbers[0])

def get_symbol():
    symbol_order = []
    symbol=['+','-','*','/']
    for s1 in symbol:
        for s2 in symbol:
             for s3 in symbol:
                  symbol_order.append([s1,s2,s3])
    return symbol_order

def get_order():
    the_order=[[]]
    for i in range(len(nums)):
        l_order=[]
    for the in the_order:
        for j in range(len(nums)):
            if j not in the:
                t=the[:]
                t.append(j)
                l_order.append(t)
                the_order=l_order
                return the_order
def fd(expresion,number_num,symbol_number,number,symbol):
    if symbol_number!=3:
        if (number_num - symbol_number)>1:
            n_expression = expresion[:]
            n_expression.append(symbol[symbol_number])
            fd(n_expression, number_num, symbol_number + 1, number,symbol)
if number_num < 4:
    n_expression = expresion[:]
    n_expression.append(str(number[number_num]))
    fd(n_expression, number_num + 1, symbol_number, number,symbol)
else:
#print expresion
#print get_result(expresion)
    if get_result(expresion)==24:
        flag[0]=1

def computer():
    symbol=get_symbol()
    order=get_order()
    num_order=[]
    for o in order:
        num_order.append([nums[x] for x in o])

for o in num_order:
    for s in symbol:
        fd([],0,0,o,s)


order = ['0', '0', '+', '0', '+', '0', '+']
flag=[0]
computer()
if flag[0]==0:
    return False
else:
    return True
