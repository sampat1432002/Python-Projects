#  **************** Problem Statement ******************
# Write a program to perform addition on two lists and print it in third.
# E.g. i/p - L1 = [ 1,2,3,”hello”,2.5] L2 = [1,2,3,”Hi”,2.2] o/p - [ 2,4,6,”helloHi”,4.7]
L1 = [1,2,3,"hello",2.5]
L2 = [1,2,3,"Hi",2.2]
L3 = []
for i in range(len(L1)):
    val = L1[i]+L2[i]
    L3.append(val)
print(L3)