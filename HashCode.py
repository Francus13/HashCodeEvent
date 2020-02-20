#Initializing data
with open('a_example.txt', 'r') as f:
    data = f.read()

print(data)
lines = data.split('\n')
print(lines)

totalBooks = lines[0][0]
totalLibraries = lines[0][1]
totalDays = lines[0][2]

#compute scores
def computeLibraryScore(l,d):
    
daysRemaining = totalDays


#libraryScore = computeLibraryScore(library, daysAvailable)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

