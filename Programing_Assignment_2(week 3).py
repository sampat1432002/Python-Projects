def contracting(lst):
    
    lstdiff = []
    for i in range(1,len(lst)-1):
        diff = abs(lst[i] - lst[i-1])
        lstdiff.append(diff)
        if(len(lstdiff) > 1):
            if(lstdiff[-1] >= lstdiff[-2]):
                return False
        else:
            continue
        
    return True

def counthv(lst):

    hc = vc= 0
    for i in range(1,len(lst)-1):
        if((lst[i] > lst[i-1]) and (lst[i] > lst[i+1])):
            hc += 1
        elif((lst[i] < lst[i-1]) and (lst[i] < lst[i+1])) :
            vc += 1
        
    return [hc,vc]

def leftrotate(lst):
    rlst = []
    for i in range(0,len(lst)):
        l = []
        for j in range(0,len(lst)):
            l.append(lst[j][i])

        rlst.insert(0,l)
        
    return rlst