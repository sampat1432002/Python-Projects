#  ******************* Problem Statement *******************
# Write a program to read a string and print a number of unique characters from the string using set

string = input("Enter String: ")
string = set(string)
print("Number of unique characters in this string is ",len(string))