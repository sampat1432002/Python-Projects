# *************************************** Problem Statement ************************************
# Finally, a COVID vaccine is out on the market and the Chefland government has asked you to form a plan to distribute it to the public as soon as possible. There are a total of N people with ages a1,a2,...an
# There is only one hospital where vaccination is done and it is only possible to vaccinate up to D people per day. Anyone whose age is ≥80≥80 or ≤9 is considered to be at risk. On each day, you may not vaccinate both a person who is at risk and a person who is not at risk. Find the smallest number of days needed to vaccinate everyone.
# Input
#
# Output
# For each test case, print a single line containing one integer ― the smallest required number of days.
# Example Input
# 2
# 10 1
# 10 20 30 40 50 60 90 80 100 1
# 5 2
# 9 80 27 72 79
# Example Output
# 10
# 3

from math import ceil

T = int(input("Enter number of test cases: "))
while T:
    n,d = input().split()
    N = int(n)
    D = int(d)
    age_of_people = list(map(int,input("Enter ages of people: ").split()))[:N]

    count_no_risk = 0
    count_risk = 0

    for i in age_of_people:
        if(i>= 80 or i<= 9):
            count_risk = count_risk + 1
        else:
            count_no_risk = count_no_risk + 1

    min_days = ceil(count_risk/D) + ceil(count_no_risk/D)
    print(min_days)
    T = T - 1