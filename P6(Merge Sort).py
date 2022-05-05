# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:13:53 2020

@author: ABC
"""


def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    i,j = 0,0
    while i+j < m+n:
        if(i == m):
            C.append(B[j])
            j += 1
        
        elif(j == n):
            C.append(A[i])
            i += 1
            
        elif(A[i] <= B[j]):
            C.append(A[i])
            i += 1
            
        elif(A[i] > B[j]):
            C.append(B[j])
            j += 1

    return C

def mergesort(l,left,right):
    if right - left <= 1:
        return l[left:right]
    
    else:
        mid = (left + right)//2
        
        L = mergesort(l,left,mid)
        R = mergesort(l,mid,right)
 
        return(merge(L,R))


a = list(range(0,100,2)) + list(range(1,100,2))
print(mergesort(a,0,len(a)))
            

        