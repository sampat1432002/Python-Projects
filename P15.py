#  ******************* Problem Statement *******************
# Write a program to check whether the entered number is Armstrong or not.


def check_Armstrong(N):
    x = len(N)
    ans = 0
    for i in N:
        ans = ans + pow(int(i), x)
    if ans == int(N):
        return "Yes It is an Armstrong Number"
    else:
        return "No It is not an Armstrong Number"


N = input("Enter a number to check for Armstrong:")
print(check_Armstrong(N))
