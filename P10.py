#  ******************* Problem Statement *******************
# Write a program to print elements which are in even and odd positions.

List = list(map(int,input("Enter the values in List:").split()))

print("Numbers at odd position are : ")
i = 0
while(i < len(List)):
    print(List[i])
    i = i+2

print("Numbers at even position are : ")
i = 1
while(i < len(List)):
    print(List[i])
    i = i+2

