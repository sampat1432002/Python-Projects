# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:58:28 2020

# @author: Shreyash Patel
"""

# ******************** SIMPLE BASIC METHOD WE LEARN *********************

# import sys

# def max_lst(l):
#     max = 0
#     for _ in l:
#         if (_ > max):
#             max = _
#     return max

# def min_lst(l):
#     min = sys.maxsize
#     for _ in l:
#         if (_ < min):
#             min = _
#     return min

# print(max_lst([4,6,7,9,1,3,4,5]))

# ************************************** RECURSIVE METHOD(LESS TIME COMPLEXITY) ***********************************

# def min_max(low,high,arr):
#     # If the array has only one element 
#     if(low == high):
#         arr_min = arr[low]
#         arr_max = arr[low]
#         return(arr_min,arr_max)
        
#     # If array has two elements
#     elif(high == low + 1):
#         if(arr[high] > arr[low]):
#             arr_max,arr_min = arr[high],arr[low]
#         else:
#             arr_max,arr_min = arr[low],arr[high]
#         return(arr_min,arr_max)
    
#     # If array has more than two elements
#     else:
#         mid = (high + low) // 2
#         arr_max1,arr_min1 = min_max(low,mid, arr)
#         arr_max2,arr_min2 = min_max(mid+1,high,arr)
        
#     return(min(arr_min1,arr_min2),max(arr_max1,arr_max2))


# arr = [6,4,6,7,4,3,3,6]
# high = len(arr) - 1
# low = 0

# arr_min,arr_max = min_max(low, high, arr)
# print("Max Element of Array: ",arr_max,"\nMin Element of Array: ",arr_min)


# ******************************************************************* Compare in Pairs) *********************************************# Python3 program of above implementation 
def getMinMax(arr):
	
	n = len(arr)
	
	# If array has even number of elements then 
	# initialize the first two elements as minimum 
	# and maximum 
	if(n % 2 == 0):
		mx = max(arr[0], arr[1])
		mn = min(arr[0], arr[1])
		
		# set the starting index for loop 
		i = 2
		
	# If array has odd number of elements then 
	# initialize the first element as minimum 
	# and maximum 
	else:
		mx = mn = arr[0]
		
		# set the starting index for loop 
		i = 1
		
	# In the while loop, pick elements in pair and 
	# compare the pair with max and min so far 
	while(i < n - 1):
		if arr[i] < arr[i + 1]:
			mx = max(mx, arr[i + 1])
			mn = min(mn, arr[i])
		else:
			mx = max(mx, arr[i])
			mn = min(mn, arr[i + 1])
			
		# Increment the index by 2 as two 
		# elements are processed in loop 
		i += 2
	
	return (mx, mn)
	
# Driver Code
if __name__ =='__main__':
	
	arr = [1000, 11, 445, 1, 330, 3000]
	mx, mn = getMinMax(arr)
	print("Minimum element is", mn)
	print("Maximum element is", mx)
	
# This code is contributed by Kaustav
