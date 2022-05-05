#  ******************* Problem Statement *******************
# Write a program to compare two lists.
L1 = list(map(int,input("Enter the values in List:").split()))
L2 = list(map(int,input("Enter the values in List:").split()))

if L1 == L2:
    print("Lists are equal...")
else:
    print("Lists are not equal...")
