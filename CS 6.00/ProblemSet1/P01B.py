# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 1B
# Student: May Pongpitpitak
# May 12, 2011

# Calculate the sum of logarithm value of all prime numbers in range

from math import *

nextPrime = 2
divisor = 2
logSum = 0

while nextPrime <= 10 :
    if nextPrime % divisor != 0 : 
        divisor += 1
    elif nextPrime % divisor == 0 and nextPrime != divisor : # is not a prime, move on
        nextPrime += 1
        divisor = 2
    elif nextPrime % divisor == 0 and nextPrime == divisor : # is a prime, add log value and move on
        logSum += log(nextPrime)
        nextPrime += 1
        divisor = 2
    else:
        print('Error')

print(logSum)
