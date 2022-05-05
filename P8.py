#  ******************* Problem Statement *******************
# Write a program to find the Highest common factor.


def HCF(m, n):
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            hcf = i

    return hcf


X = int(input("Enter first Number: "))
Y = int(input("Enter Second Number: "))
print("HCF of ",X," and ",Y," is ",HCF(X,Y))