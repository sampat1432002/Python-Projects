#  ******************* Problem Statement *******************
# Write a program to print LCM (Lowest Common Multiple)

def LCM(X,Y):
    max = 0
    lcm = 0

    if X>Y:
        max = X
    else:
        max = Y
    while max <= X*Y:
        if max % X == 0 and max % Y == 0:
            lcm = max
            break
        max = max + 1

    return lcm


X = int(input("Enter first Number: "))
Y = int(input("Enter Second Number: "))

print("LCM of ",X," and ",Y," is ",LCM(X,Y))