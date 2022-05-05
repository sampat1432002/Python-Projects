# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:35:05 2020

@author: ABC
"""

#Replace all ______ with rjust, ljust or center. 

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# M,N = int(input().split())

# m = int(M)
# n = int(N)

# des = '.|.'

# for i in range(1,m//2 + 1):
#     print(((des*((2*i)-1)).center(n,'-')))

# print("Welcome".center(n,'-'))

# for i in range(m//2,0,-1):
#     print(((des*((2*i)-1)).center(n,'-')))
