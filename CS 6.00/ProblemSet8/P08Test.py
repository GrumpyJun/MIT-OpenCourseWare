# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 8 - Test
# Student: May Pongpitpitak
# July 30, 2011

import P08

"""
This file is for testing the P08 code
"""

# Global settings
SUBJECT_LIST    = {}
MAX_WORK        = 20


# Test Problem 1
print("---------- Test problem 1 ----------")
SUBJECT_LIST = P08.loadSubjects("subjects.txt")
P08.printSubjects(SUBJECT_LIST)



# Test Problem 2
print("---------- Test problem 2 ----------")
bestRatioSchedule = P08.greedyAdvisor(SUBJECT_LIST, MAX_WORK, 'cmpRatio')
#bestValueSchedule = P08.greedyAdvisor(SUBJECT_LIST, MAX_WORK, 'cmpValue')
#bestWorkSchedule  = P08.greedyAdvisor(SUBJECT_LIST, MAX_WORK, 'cmpWork')

print("Best course schedule by work ratio:")
P08.printSubjects(bestRatioSchedule)  

# print("Best course schedule by value:")
# P08.printSubjects(bestValueSchedule)

# print("Best course schedule by work load:")
# P08.printSubjects(bestWorkSchedule)



# Test Problem 3
print("---------- Test problem 3 ----------")
##time, bruteForceCourseList = P08.bruteForceTime(SUBJECT_LIST, MAX_WORK)
###P08.printSubjects(bruteForceCourseList)
print("Problem 3's bruteForce code is not compatible with Python 3.2 \n")


# Test Problem 4
print("---------- Test problem 4 ----------")
dpCourseList = P08.dpAdvisor(SUBJECT_LIST, MAX_WORK)
P08.printSubjects(dpCourseList)



# Test Problem 5
print("---------- Test problem 5 ----------")
P08.dpTime(SUBJECT_LIST, MAX_WORK)



