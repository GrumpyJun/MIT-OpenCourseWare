# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 2D
# Student: May Pongpitpitak
# May 13, 2011

# Calculate combination of nugget packages (small, medium and large package)
# to produce desire total numbers of nuggets
#
# ex: 6*sixPack + 9*ninePack + 20*twentyPack = totalNuggets

totalNuggets = 0
bestSoFar = 0
packageSize = (6, 9, 20)

for totalNuggets in range(1, 150): # define total nuggets want

    for smallPack in range(1, int(totalNuggets/packageSize[0])):
        for mediumPack in range(1, int(totalNuggets/packageSize[1])):
            for largePack in range(1, int(totalNuggets/packageSize[2])):
                if packageSize[0]*sixPack + packageSize[1]*ninePack + packageSize[2]*twentyPack != totalNuggets and totalNuggets > bestSoFar:
                    bestSoFar = totalNuggets

print(bestSoFar)
                    
