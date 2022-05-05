# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:44:42 2020

@author: ABC
"""
# ***************** BASIC METHOD ****************

# def sorti(arr):
#     for i in range(len(arr)-1):
#         for j  in range(i,len(arr)-1):
#             if(arr[i] > arr[j+1]):
#                 arr[i],arr[j+1] = arr[j+1],arr[i]
#     return arr

# def maxi(low,high,arr,k):
#     arr = sorti(arr)
#     return arr[-k]


# arr = [6,5,2,1,9,8,3]
# k = 2
# high = len(arr) - 1
# low = 0
# arr_max = maxi(low, high, arr,k)

# print(k ,"th ","Max Element of Array: ",arr_max)

# ********************************** QUICK SORT METHOD ***********************

import sys
import random

def kthSmallest(arr,l,r,k):
    if(k > 0 and k <= r - l + 1):
        pos = randomPartition(arr,l,r)
        if(pos - l == k -l):
            return arr[pos]
        if(pos -l > k-1):
            return kthSmallest(arr,l,pos -l,k)
        return kthSmallest(arr,pos+1,r,k-pos+l-1)
    return sys.maxsize

def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def partition(arr,l,r):
    x = arr[r]
    i =l
    for j in range(l,r):
        if(arr[j] <= x):
            swap(arr,i,j)
            i+=1
    swap(arr,i,r)
    return i
    
def randomPartition(arr,l,r):
    n = r - l + 1
    pivot = int(random.random() % n)
    swap(arr,l + pivot,r)
    return partition(arr,l,r)

arr = [8,9,6,4,5,6,1,16]
l = 0
r = len(arr)
k = int(input())
print("The ",k,"th element of array is ",kthSmallest(arr,l,r-1,k))