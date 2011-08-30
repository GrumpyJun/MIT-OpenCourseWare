# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 8 - Intelligent Course Advisor
# Student: May Pongpitpitak
# July 30, 2011

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    
    # The following sample code reads lines from the specified file and prints
    # each one.
    
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).
    
    inputFile = open(filename,'r', 1)
    subjects = {}
    for line in inputFile:
        nextSubject                 = line.strip().split(',')      # First remove the extra chars then split them
#        subjectName                 = nextSubject[0]
#        subjectValue                = int(nextSubject[1])
#        subjectWork                 = int(nextSubject[2])
        subjects[nextSubject[0]]    = {VALUE : int(nextSubject[1]), WORK : int(nextSubject[2])}
    
    return(subjects)
       
    
    
def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = list(subjects.keys())                # Added list() to the code to force conversion from keys to list. object.keys() doesn't return a list-type and can't be sorted.
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a boolean
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    
    assert comparator is 'cmpRatio' or 'cmpValue' or 'cmpWork'  , "Invalid comparator"
    assert maxWork    >  0                                      , "Maximum work limit is not enough"

    bestCourse          = list(subjects.keys())[0]
    greedyCourseList    = {}
    totalWork           = 0
        
    # Select course by best value/work ratio
    if comparator is 'cmpRatio':
        while totalWork < maxWork:
            # Selecting the best course available in the list
            for course in subjects.keys():
                if cmpRatio(subjects[course], subjects[bestCourse]) is True \
                   and course not in greedyCourseList.keys():
                    bestCourse = course
                    
            # If not exceeding maxWork, add the selected course to the list
            totalWork += subjects[bestCourse][WORK]
            if totalWork <= maxWork:
                greedyCourseList[bestCourse] = subjects[bestCourse]   

    # Select course by best value
    elif comparator is 'cmpValue':
        while totalWork < maxWork:
            # Selecting the best course available in the list
            for course in subjects.keys():
                if cmpValue(subjects[course], subjects[bestCourse]) is True \
                   and course not in greedyCourseList.keys():
                    bestCourse = course
                    
            # If not exceeding maxWork, add the selected course to the list
            totalWork += subjects[bestCourse][WORK]
            if totalWork <= maxWork:
                greedyCourseList[bestCourse] = subjects[bestCourse]
                
    # Select course by best work load
    elif comparator is 'cmpWork' :
        while totalWork < maxWork:
            # Selecting the best course available in the list
            for course in subjects.keys():
                if cmpWork(subjects[course], subjects[bestCourse]) is True \
                   and course not in greedyCourseList.keys():
                    bestCourse = course
                    
            # If not exceeding maxWork, add the selected course to the list
            totalWork += subjects[bestCourse][WORK]
            if totalWork <= maxWork:
                greedyCourseList[bestCourse] = subjects[bestCourse]    
  
    return(greedyCourseList)
    
    

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue, \
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects, \
                    maxWork, i+1, bestSubset, bestSubsetValue, subset, \
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects, \
                maxWork, i+1, bestSubset, bestSubsetValue, subset, \
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime(subjects, maxWork):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    
    print("Measuring Brute Force method's performance.")
    startTimer              = time.time()
    bruteForceCourseList    = bruteForceAdvisor(subjects, maxWork)
    endTimer                = time.time()

    performanceTime         = endTimer-startTimer
    print("Total time to completion:", performanceTime)
    
    return(performanceTime, bruteForceCourseList)

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    
    dpCourseList        = {}

    subjectsKeysList    = list(subjects.keys())
    subjectsValuesList  = list(subjects.values())

    # Get the best course list using recursive method
    courseListTree, courseListTreeValue    = dpAdvisorHelperTree(subjectsValuesList, maxWork, \
                                              len(subjectsValuesList)-1, 0, {})

    for courses in courseListTree:
        dpCourseList[subjectsKeysList[courses]] = subjectsValuesList[courses]

    # Get the best course list using for-loop method
#    courseListTable    = dpAdvisorHelperTable(subjects, maxWork)    
    
    return(dpCourseList)


def dpAdvisorHelperTree(subjectsValuesList, maxWork, i, trackedWork, courseMemoTree):
    """
    DESC:   the best course list is determined by going down a decision tree between
            taking or not taking each course (binary)
    
    NOTE:   This function might be better if the dictionary of all intermediate steps
            were made Global and doesn't need to be pass around
    
    subjectsValuesList: a list of all courses offer created from keys
    maxWork:            limit amount of work load impose
    i:                  index of courses for tracking location on the subject list
    trackedWork:        the total amount of work accumulated so far. This variable is also used
                        as a second key in the courseMemoTree dictionary as it gives insight to
                        the depth of tree
    courseMemoTree:    a dictionary mapping index number and list of courses(keys)
                        to the total value and work of the list for references
                        (i, trackedWork) : (totalValue, totalWork)

    return:             the better list of courses and its corresponding values
                        as two separate items                        
    """


    # Check if the element has already been computed and stored in the reference
    try: return(courseMemoTree[i, trackedWork])

    # If not, proceed
    except KeyError:
        # Check if at the first/bottom possible element in the list.
        if i == 0:
            courseList                     = []
            courseListValue                = 0
            courseMemoTree[i, trackedWork] = (courseList, courseListValue)
            return(courseList, courseListValue)

        else:  
            # SCENARIO 1 - If not taking this course
            courseNotTaken, courseNotTakenValue = dpAdvisorHelperTree(subjectsValuesList, maxWork, i-1,
                                                                      trackedWork, courseMemoTree)

            # SCENARIO 2 - Take this course
            # If there is no space
            if trackedWork >= maxWork:
                courseMemoTree[i, trackedWork] = (courseNotTaken, courseNotTakenValue)
                return(courseNotTaken, courseNotTakenValue)

            # If there is space
            elif (trackedWork + subjectsValuesList[i][WORK]) <= maxWork:
                # Get the beginning of the list. Remember we are working backward in this method.
                courseTaken, courseTakenValue   = dpAdvisorHelperTree(subjectsValuesList, maxWork, i-1,
                                                                      trackedWork + subjectsValuesList[i][WORK], courseMemoTree)
                courseTaken.append(i)
                courseTakenValue += subjectsValuesList[i][VALUE]
            
            # Compare the results from the two scenarios
            courseListValue = max(courseTakenValue, courseNotTakenValue)
            if courseListValue == courseTakenValue: courseList = courseTaken
            else:                                   courseList = courseNotTaken
                
            # Store for reference
            courseMemoTree[i, trackedWork] = (courseList, courseListValue)
            
            return(courseList, courseListValue)


##def dpAdvisorHelperTable(subjects, maxWork):
##    """
##    DESC:   solving the problem using for-loop instead of decision tree
##    
##    subjects:           a dictionary mapping of all courses offer to their work load and value
##    maxWork:            limit amount of work load impose
##
##    return:             a dictionary mapping the best courses and their wprk load and value
##    """
##
##    courseMemoTable    = {0:([], 0)}   # a dictionary for storing the references
##    courseList          = {}            # the final result list of best courses
##
##    # Check through all the possible total work load value even at less than max
##    for trackedWork in range(maxWork):  
##        bestCourseCombo = ([], 0)       # set/re-set the best choice (list, total value)
##
##        #
##        for course in subjects:
##
##            # Check if we're not going over work load limit and doesn't already exist in the reference
##            if subjects[course][WORK] < trackedWork and course not in courseMemoTable[trackedWork][0]:
##                currentCourseComboValue = courseMemoTable[trackedWork][1] + subjects[course][VALUE]
##
##                #
##                if currentCourseComboValue > bestCourseCombo[1]:
##                    bestCourseCombo = (courseMemoTable[trackedWork][0].append(course), currentCourseComboValue)
##
##        courseMemoTable[trackedWork] = bestCourseCombo
##       
##    #    
##    for course in courseMemoTable[max(courseMemoTable)][0]:
##        courseList[course] = subjects[course]
##
##    return(courseList)

                       
#
# Problem 5: Performance Comparison
#
def dpTime(subjects, maxWork):
    """
    DESC:   Runs tests on dpAdvisor and measures the time required to compute an
            answer.

    return: the time value and the dictionary of selected courses from dpAdvisor
    """
    # TODO...

    print("Measuring Dynamic Programming method's performance")
    startTimer      = time.time()
    dpCourseList    = dpAdvisor(subjects, maxWork)
    endTimer        = time.time()

    performanceTime = endTimer-startTimer
    print("Total time to completion:", performanceTime)
    
#    return(performanceTime, bruteForceCourseList)

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
