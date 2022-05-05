"""
Created on Sun Oct 11 18:53:02 2020

@author: ABC
"""

    # dic = {}
    # for i in set(l):
    #     dic[i] = l.count(i)
    
    # imax = max(dic.values())
    # imin = min(dic.values())
    
    # minl = []
    # maxl = []
        
    
    # for x in dic:
    #     v = dic.get(x)
    #     if len(dic) == 1:
    #         minl.append(x)
    #         maxl.append(x)
    #         break
    #     if imin == imax:
    #         minl = l
    #         maxl = l
    #         break
    #     if  v == imin:
    #         minl.append(x)
    #     elif v == imax:
    #         maxl.append(x)
    
    # return (minl, maxl)
 #   return (list(dic.viewkeys(imin)),list(dic.viewkeys(imax)))
    
# def frequency(l):
#     lstmin = []
#     lstmax = []    
    
#     lst = []
    
#     unique = list(set(l))
    
#     for i in unique:
#         lst.append(l.count(i))
    
#     for i in unique:
#         if(l.count(i) == max(lst)):
#             lstmax.append(i)
        
#     for i in unique:
#         if(l.count(i) == min(lst)):
#             lstmin.append(i)
    
#     lstmin.sort()
#     lstmax.sort()
#     return (lstmin,lstmax)
def frequency(l):
    unique_l = list(set(l))
    freq_list = [l.count(x) for x in unique_l]
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    print(min_freq_list,max_freq_list)
    return (min_freq_list,max_freq_list)

def onehop(l):
    finlst = []
    for i in l:
        for j in l:
            if(i != j):
                if(i[1] == j[0] and i[0] != j[1]):
                    finlst.append((i[0],j[1]))                        
            else:
                continue
    finlst = list(set(finlst))
    finlst.sort()
    return finlst
  
# print(frequency([1, 2, 3, 4, 5, 6]))
print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14]))
# print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14]))
# frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])

# onehop([(2,3),(1,2)])
# onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])
# onehop([(1,2),(3,4),(5,6)])