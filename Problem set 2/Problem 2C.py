# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 2C
# Student: May Pongpitpitak
# May 12, 2011

# Calculate the largest number that a combination of 
# nugget packages (6, 9 and 20) couldn't purchase
#
# 6*sixPack + 9*ninePack + 20*twentyPack = totalNuggets

totalNuggets = 0
bestSoFar = 0 # largest number that couldn't be purchase

for totalNuggets in range(51, 55): # define total nuggets want

    for sixPack in range(1, int(totalNuggets/6)):
        for ninePack in range(1, int(totalNuggets/9)):
            for twentyPack in range(1, int(totalNuggets/20)):
                if 6*sixPack + 9*ninePack + 20*twentyPack != totalNuggets and totalNuggets > bestSoFar:
                    bestSoFar = totalNuggets

print(bestSoFar)
