# *************************************** Problem Statement ************************************
# Write a program to Reverse the Number where
# Input :-  The first line contains an integer T, total number of test cases.
# Then follow T lines, each line contains an integer N.
# Output:- For each test case, display the reverse of the given number N, in a new line.
# Input
# 4
# 12345
# 31203
# 2123
# 2300
# Output
# 54321
# 30213
# 3212
# 32

T = int(input("Enter number of cases: "))
while T:
    N = int(input())
    rev_number = 0
    while N != 0:
        x = N % 10
        rev_number = rev_number*10 + x
        N = N//10
    T = T-1
    print(rev_number)