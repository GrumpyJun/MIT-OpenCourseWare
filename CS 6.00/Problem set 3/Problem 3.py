# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 3A
# Student: May Pongpitpitak
# May 21, 2011

from string import *



# 
# Problem 1
# 

def countSubStringMatch(target,key):

    assert len(key) != 0, "Invalid key"
    
    # if there's no match at all
    if str.find(target, key) < 0:
        print("No match found")
        
    else:
        currentPosition = 0
        nextMatch = 0
        while nextMatch >= 0:
            nextMatch = str.find(target, key, currentPosition)
            if nextMatch >= 0:
                print(nextMatch)
            currentPosition = nextMatch + len(key)
        print("Complete")
        

def countSubStringMatchRecursive(target, key):

    assert len(key) != 0, "Invalid key"
    
    nextMatch = str.find(target, key)
    
    # when there's no more matches left
    if nextMatch < 0:
        print("Complete")
        
    else:
        print(nextMatch)
        newTarget = target[(nextMatch + len(key)):]
        countSubStringMatchRecursive(newTarget, key)



# 
# Problem 2
# 

def countSubStringMatch(target,key):

    assert len(key) != 0, "Invalid key"

    keyLocations = []
    
    if str.find(target, key) < 0:
        print("No match found")
        
    else:
        currentPosition = 0
        nextMatch = 0
        while nextMatch >= 0:
            nextMatch = str.find(target, key, currentPosition)
            if nextMatch >= 0:
                keyLocations.append(nextMatch)
            currentPosition = nextMatch + len(key)

    return(keyLocations)



# 
# Problem 3
# 

def subStringMatchExact(target, key):

    # assert len(key) != 0, "Invalid key"

    keyLocations = []

    if len(key) == 0:
        print("No key")
        
    elif str.find(target, key) < 0:
        print("No match found")
        
    else:
        currentPosition = 0
        nextMatch = 0
        while nextMatch >= 0:
            nextMatch = str.find(target, key, currentPosition)
            if nextMatch >= 0:
                keyLocations.append(nextMatch)
            currentPosition = nextMatch + len(key)

    return(keyLocations)


def constrainedMatchPair(firstMatch,secondMatch,keyLength):
    
    allMatch = []
    
    for currentElement in range(len(firstMatch)):
        for anyElement in range(len(secondMatch)):
            if firstMatch[currentElement]+keyLength+1 == secondMatch[anyElement]:
                allMatch.append(firstMatch[currentElement])
    
    return(allMatch)




