# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:37:47 2020

@author: ABC
"""

def SelectionSort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start,len(l)):
            if(l[i] < l[minpos] ):
                minpos = i
                
        (l[start],l[minpos]) = (l[minpos],l[start])
        
    return l
        
print(SelectionSort([9,5,6,2,3,4]))
        