# -*- coding: utf-8 -*-
"""
Created on Sat May 07 22:31:44 2016

@author: Arthur CAHEN
"""

#==============================================================================
# Even Tree
#==============================================================================
"""https://www.hackerrank.com/challenges/even-tree"""

# set the input
N,M = map(int, raw_input().strip().split(' '))

T = []
for i in xrange(M): 
    a,b = map(int, raw_input().strip().split(' '))
    T.append([a,b])

# build Categories: components
C = {}
for i in range(1,N+1):
    for j in xrange(M):
        if i in T[j]:
            if i in C.keys():
                C[i] += 1
            else:
                C[i] = 1
        