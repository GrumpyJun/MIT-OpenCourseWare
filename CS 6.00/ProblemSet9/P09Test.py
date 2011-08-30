# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 9 - Test
# Student: May Pongpitpitak
# August 13, 2011

import P09

"""
This file is for testing the P09 code
"""

# Global variable settings
INPUT_FILE  = "shapes.txt"

CIRCLE_1    = P09.Circle(5)
CIRCLE_2    = P09.Circle(10)
SQUARE_1    = P09.Square(2)
SQUARE_2    = P09.Square(4)



# Test Problem 1
print("---------- Test problem 1 ----------")
TRIANG_1    = P09.Triangle(3,6)
TRIANG_2    = P09.Triangle(4,5)
print(TRIANG_1)
print(TRIANG_2, '\n')



# Test Problem 2
print("---------- Test problem 2 ----------")
setTest = P09.ShapeSet()
setTest.addShape(CIRCLE_1)
setTest.addShape(CIRCLE_2)
setTest.addShape(SQUARE_1)
setTest.addShape(SQUARE_2)
setTest.addShape(TRIANG_1)
setTest.addShape(TRIANG_2)
print(setTest)



# Test Problem 3
print("---------- Test problem 3 ----------")
largestShape = P09.findLargest(setTest)

print("Largest shapes are:")
for shape in largestShape:
    print(shape)

if largestShape[0] == CIRCLE_2: print("Problem 3 test ..... SUCCESS \n")



# Test Problem 4
print("---------- Test problem 4 ----------")
shapesCreated = P09.readShapesFromFile(INPUT_FILE)
print(shapesCreated)
