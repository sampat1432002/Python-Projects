# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:37:47 2020

@author: ABC
"""

# def InsertionSort(l):
#     for pos in range(0,len(l)):
#         while pos > 0 and l[pos] < l[pos-1]:
#             (l[pos],l[pos-1]) = (l[pos-1],l[pos])
#             pos -=1
#     return l
    
        
# Recursive Method

def insert(l,k):
    pos = k
    while pos > 0 and l[pos] < l[pos-1]:
        (l[pos],l[pos-1]) = (l[pos-1],l[pos])
        pos -=1

def issort(l,k):
    if(k>1):
        issort(l,k-1)
        insert(l,k-1)

def RecInsertionSort(l):
    issort(l,len(l))
    return l
    
    
print(RecInsertionSort([9,5,6,2,3,4]))