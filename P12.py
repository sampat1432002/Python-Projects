#  ******************* Problem Statement *******************
# Write a program to convert a list to set.

List = list(map(int,input("Enter the values in List:").split()))

print("List before conversion: ",List)
print("List after conversion to set: ",set(List))