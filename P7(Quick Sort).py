# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:22:00 2020

@author: ABC
"""

def quicksort(A,l,r):
    
    if r-l <= 1:
        return()
    
    
    yellow = l+1
    
    for green in range(l+1,r):
        if(A[green] <= A[l]):
            (A[green],A[yellow]) = (A[yellow],A[green])
            yellow += 1 
            
    (A[l],A[yellow-1]) = (A[yellow-1],A[l])
    
    quicksort(A,l,yellow-1)
    quicksort(A,yellow,r)
    
a = [3,6,5,9,4,9,6,4,6,6,32]
quicksort(a,0,len(a))
print(a)
    