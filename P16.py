#  ******************* Problem Statement *******************
# Write a program to check whether the entered number is prime or not.


def isprime(N):
    for i in range(2,N):
        if N%i != 0:
            return "Yes,It is a Prime Number"
        else:
            return "No,It is not a Prime Number"


N = int(input("Enter number to check for prime or not: "))
print(isprime(N))