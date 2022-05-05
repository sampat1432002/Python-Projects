#  ******************* Problem Statement *******************
# Write a program to print following pyramid
# *
# **
# ***
# ****

for i in range(5):
    for j in range(i):
        print("*",end ="")
    print()