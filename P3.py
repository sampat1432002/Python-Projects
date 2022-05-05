#  **************** Problem Statement ******************
# Write a program to solve a quadratic equation.
from math import sqrt

print("If your quadratic equation is AX^2 + BX + C = 0. Then, ")
print("Enter values of ")
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
disc = sqrt(pow(B,2) - (4*A*C))
print("Now, \nSolution of the equation (",A,")X^2 + (",B,")X + (",C,") = 0 is")
print("X = ",((-B + disc)/2*A),"\nX = ",((-B - disc)/2*A))
