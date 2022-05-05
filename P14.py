#  ******************* Problem Statement *******************
# Write a program to display Fibonacci using recursion.


def Fibonacci(n):

    if n <= 1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


N = int(input("Enter number of terms of Fibonacci series: "))
List = []
for i in range(N):
    List.append(Fibonacci(i))

print("Fibonacci of ",N," terms is",*List)