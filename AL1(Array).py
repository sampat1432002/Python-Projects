# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:43:48 2020

@author: Shreyash Patel
"""

# Algorithm 1:Reverse the array
arr = [int(x) for x in input().split()]
print(arr)
for i in range(0,int(len(arr)/2)):
    (arr[i],arr[-(i+1)]) = (arr[-(i+1)],arr[i]) 
print(arr)
    
# Algorithm 1.2:Reverse the string
n = int(input())
arry = []
for i in range(n):
    arry.append(input())
for arr in arry:
    strg = ""
    for i in range(len(arr)-1,-1,-1):
        strg = strg + arr[i]
    print(strg)
    