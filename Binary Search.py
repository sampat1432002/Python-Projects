def binarySearch(lst, l, r, value):
    mid = int((l + (r - 1)) / 2)

    if r >= l:
        if lst[mid] == value:
            return mid

        if lst[mid] > value:
            return binarySearch(lst, l, mid, value)

        return binarySearch(lst, mid + 1, r, value)

    return -1


lst = [2, 3, 4, 10, 40]
result = binarySearch(lst,0,len(lst)-1,10)
print("Array used : ",*lst)
if result == -1:
    print("Element is not present in List.")
else:
    print("The position of 10 in lst is : ",result)
