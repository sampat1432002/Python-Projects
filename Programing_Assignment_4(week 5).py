# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:07:07 2020

@author: ABC
"""

def grades(a):
    if a=="A":
        return 10
    if a=="AB":
        return 9
    if a=="B":
        return 8
    if a=="BC":
        return 7
    if a=="C":
        return 6
    if a=="CD":
        return 5
    if a=="D":
        return 4
    
rollname = {}
gradepoint = {}
coursecount = {}

nextline = input().split()
while nextline.find("Courses") < 0:
    nextline =input().split()

nextline = input().split()
while nextline.find("Students") < 0:
    nextline = input().split()
    
nextline = input().split()
while nextline.find("Grades") < 0:
    set = nextline.split("~")
    roll = set[0]
    name = set[1]
    rollname[roll] = name
    gradepoint[roll] = 0
    coursecount[roll] = 0
    nextline = input().split()
    
nextline = input().split()
while nextline.find("EndOfInput") < 0:
    set = nextline.split("~")
    roll = set[3]    
    grade = set[4]
    gradepoint[roll] += grades(grade)
    coursecount[roll] += 1
    nextline = input().split()

for roll in sorted(rollname.keys()):
    if coursecount[roll] > 0:
        gpa = round(gradepoint[roll]/coursecount[roll],2)
    else:
        gpa = 0
    print(roll,"~",rollname[roll],"~",gpa)

    