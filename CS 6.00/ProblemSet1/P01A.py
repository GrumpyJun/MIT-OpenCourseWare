# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 1A
# Student: May Pongpitpitak
# May 11, 2011

# print all prime numbers in range

nextPrime = 2
divisor = 2

while nextPrime <= 1000 :
    if nextPrime % divisor != 0 : 
        divisor += 1
    elif nextPrime % divisor == 0 and nextPrime != divisor : # is not a prime, move on
        nextPrime += 1
        divisor = 2
    elif nextPrime % divisor == 0 and nextPrime == divisor : # is a prime, print and move on
        print(nextPrime)
        nextPrime += 1
        divisor = 2
    else:
        print('Error')
        
