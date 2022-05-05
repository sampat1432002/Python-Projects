
def prime(n):
    for i in range(2,int(n/2)+1):
        if(n%i == 0 or n == 1):
            return False
    return True
    

def primeproduct(a):
    lst = []
    for i in range(2,int(a/2)+1):
        if(a%i == 0):
            if(prime(i)):
                lst.append(i)
                
    for j in range(0,len(lst)):
        for k in range(j+1,len(lst)):
            if(lst[j]*lst[k] == a):
                return True
     #           return print("True",end = "")

    #return print("False",end = "")
    return False
    
def delchar(string,del_element):
    final = ""
    for i in string:
        if(i != del_element):
            final += i
    return final
            
def shuffle(lst1,lst2):
    lst = []
    for i in range(0,max(len(lst1),len(lst2))):
        if(i < len(lst1)):
            lst.append(lst1[i]) 
        if(i < len(lst2)):
            lst.append(lst2[i]) 
    return lst
    
