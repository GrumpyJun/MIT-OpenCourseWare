# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 2A
# Student: May Pongpitpitak
# May 12, 2011

# Calculate combination of nugget packages (6, 9 and 15)
# to produce desire total numbers of nuggets
#
# 6*sixPack + 9*ninePack + 15*fifteenPack = totalNuggets

for totalNuggets in range(51, 55): # define total nuggets want

    for sixPack in range(1, int(totalNuggets/6)):
        for ninePack in range(1, int(totalNuggets/9)):
            for fifteenPack in range(1, int(totalNuggets/15)):
                if 6*sixPack + 9*ninePack + 15*fifteenPack == totalNuggets:
                    print('For', totalNuggets, 'nuggets, we need to buy:')
                    print('  ', sixPack, 'packs of 6 nuggets')
                    print('  ', ninePack, 'packs of 9 nuggets')
                    print('  ', fifteenPack, 'packs of 15 nuggets')
                    
