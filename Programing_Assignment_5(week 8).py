# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:35:15 2020

@author: ABC
"""
# import sys
# total = 0
# def minpath(i,j,k):
#     global total
#     if(k == 1):
#         return
#     lst.remove((i,j))
#     print(lst)
#     minval = sys.maxsize
#     for (x,y) in lst:
#         val = abs(x-i) + abs(y-j)
#         print("val = ",val)
#         if(val < minval):
#             minval = val
#             ri = x
#             rj = y
#         print("min = ",minval,"total = ",total )    
#     total += minval
#     minpath(ri,rj, k-1)
        
# def minicor():
#     minr = sys.maxsize
#     for (x,y) in lst:
#         if(x+y < minr):
#             i = x
#             j = y
#             minr = x+y
#     global total
#     total += minr        
#     return (i,j)

# r,c,k,d = (int(x) for x in input().split())
# lst = []
# for i in range(d):
#     x,y = (int(x) for x in input().split())
#     lst.append((x,y))
# lst.sort()
# total += lst[0][0] + lst[0][1]
# # print(lst)
# # i,j = minicor()
# minpath(lst[0][0],lst[0][1], k)
# print(total)        


# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov  8 16:35:15 2020

# @author: ABC
# """
# import sys
# total = 0
# def minpath(i,j,k):
#     global total
#     if(k == 0):
#         return
#     lst.remove((i,j))
#     # print(lst)
#     minval = sys.maxsize
#     for (x,y) in lst:
#         val = abs(x-i) + abs(y-j)
#         print("val = ",val)
#         if(val < minval):
#             minval = val
#             ri = x
#             rj = y
#         # print("min = ",minval,"total = ",total )    
#     total += minval
#     minpath(ri,rj, k-1)

# def minicor():
#     minr = sys.maxsize
#     for (x,y) in lst:
#         if(x+y < minr):
#             i = x
#             j = y
#             minr = x+y
#     global total
#     total += minr        
#     return (i,j)

# r,c,k,d = (int(x) for x in input().split())
# lst = []
# for i in range(d):
#     x,y = (int(x) for x in input().split())
#     lst.append((x,y))
    
# i,j = minicor()
# minpath(i,j,k-1)
# print(total)        


R,C,K,D=input().split()
D=int(D)
R=int(R)
K=int(K)
C=int(C)
Dragon_position=list()
distance=0
store=dict()
for g in range(D):
        x,y=input().split()
        x=int(x)
        y=int(y)
        Dragon_position.append([x,y])

ans=9999999
from itertools import combinations
comb = combinations(Dragon_position, K)
list_comb=list()
for i in list(comb):
    list_comb.append(sorted(i))
#print(list_comb)
dragon_initial_position=[0,0]
store=dict()
for row in list_comb:
    for column in range(len(row)):
         if row[:column+1] in store.values():
             sub_part_list = row[:column + 1]
             p=sub_part_list[len(sub_part_list) - 1:len(sub_part_list)]
             #print("p=",p)
             distance=list(store.keys())[list(store.values()).index(row[:column+1])]
             dragon_initial_position[0] = p[0][0]
             dragon_initial_position[1] = p[0][1]
             #print("went for dynamic")
         else:
            r=row[column][0]
            c=row[column][1]
            distance = distance + abs(dragon_initial_position[0] - r) + abs(dragon_initial_position[1] - c)
            dragon_initial_position[0] = r
            dragon_initial_position[1] = c
            sub_part=[]
            sub_part=row[:column+1]
            store[distance]=sub_part
    if ans>distance:
        ans=distance
    distance=0
    dragon_initial_position[0] = 0
    dragon_initial_position[1] = 0
print(ans)