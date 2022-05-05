# *************************************** Problem Statement ************************************
# There are N students living in the dormitory of Berland State University. Each of them sometimes wants to use the kitchen, so the head of the dormitory came up with a timetable for kitchen's usage in order to avoid the conflicts:
# The first student starts to use the kitchen at the time 0 and should finish the cooking not later than at the time A1.
# The second student starts to use the kitchen at the time A1 and should finish the cooking not later than at the time A2.
# And so on.
# The N-th student starts to use the kitchen at the time AN-1 and should finish the cooking not later than at the time AN
# The holidays in Berland are approaching, so today each of these N students wants to cook some pancakes. The i-th student needs Bi units of time to cook.
# The students have understood that probably not all of them will be able to cook everything they want. How many students will be able to cook without violating the schedule?
# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains a single integer N denoting the number of students.
# The second line contains N space-separated integers A1, A2, ..., AN denoting the moments of time by when the corresponding student should finish cooking.
# The third line contains N space-separated integers B1, B2, ..., BN denoting the time required for each of the students to cook.
# Output
# For each test case, output a single line containing the number of students that will be able to finish the cooking.
# Input:
# 2
# 3
# 1 10 15
# 1 10 3
# 3
# 10 20 30
# 15 5 20
# Output:
# 2
# 1


T = int(input("Enter number of test cases: "))
while T:
    N = int(input("Enter number of students: "))
    moments_of_time = list(map(int,input("Enter finish time of cooking for each student: ").split()))[:N]
    time_required = list(map(int,input("Enter required time of cooking for each student: ").split()))[:N]

    count = 0

    computed_moments_of_time = []
    computed_moments_of_time.append(moments_of_time[0])

    for i in range(1,len(moments_of_time)):
        x = moments_of_time[i] - moments_of_time[i-1]
        computed_moments_of_time.append(x)

    for i in range(len(time_required)):
        if time_required[i] <= computed_moments_of_time[i]:
            count = count + 1
    print("Numbers of students can complete their cooking: ",count)
    T = T - 1