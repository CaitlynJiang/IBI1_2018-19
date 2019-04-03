#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:45:17 2019

@author: caitlynjiang
"""


#给定n个数字,计算出一个满足24点的表达式:比如1,11,2,1:(11+1)*2/1

#基本思路就是枚举计算顺序(在一开始进行一次全排列),括号,加减乘除。其实有很多是重复计算过了的。这个程序我为了高效找到一个解就算了,但是我们把程序稍微修改就可以找到所有的解(表达顺序可能会重复,比如1+2和2+1),同时也可以计算多个数字的组合。

def compute(x,y,op):
    if op=='+':return x+y
    elif op=='*':return x*y
    elif op=='-':return x-y
    else:return x/y if y else None

def exp(p,iter=0):
    from itertools import permutations
    if len(p)==1:return [(p[0],str(p[0]))]
    operation = ['+','-','*','/']
    ret = []
    p = permutations(p) if iter==0 else [p]
    for array_n in p:
        #print(array_n)
        for num in range(1,len(array_n)):
            ret1 = exp(array_n[:num],iter+1)
            ret2 = exp(array_n[num:],iter+1)
            for op in operation:
                for va1,expression in ret1:
                    if va1==None:continue
                    for va2,expression2 in ret2:
                        if va2==None:continue
                        combined_exp = '{}{}' if expression.isalnum() else '({}){}'
                        combined_exp += '{}' if expression2.isalnum() else '({})'
                        new_val = compute(va1,va2,op)
                        ret.append((new_val,combined_exp.format(expression,op,expression2)))
                        if iter==0 and new_val==24:
                            return ''.join(e+'\n' for x,e in ret if x==24)
    return ret
print(exp([8,3,4,11]))
