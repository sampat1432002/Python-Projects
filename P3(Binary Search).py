# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:51:38 2020

@author: ABC
"""

def bsearch(seq,v,l,r):
    if(r-l == 0):
        return False
    
    mid =  (l+r)//2
    
    if(v == seq[mid]):
        return True
    
    if(v < seq[mid]):
        return bsearch(seq, v, l, mid)
    else:
        return bsearch(seq, v, l, mid + 1)
    