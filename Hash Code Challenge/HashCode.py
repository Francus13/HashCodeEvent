#Initializing data
with open('a_example.txt', 'r') as f:
    data = f.read()
o = open('output.txt', 'w')

lines = data.split('\n')

totalBooks = lines[0][0]
totalLibraries = lines[0][1]
totalDays = lines[0][2]

answer = ''
#compute scores
def computeLibraryScore(l,d):
    
# ALL ALGORITHM WORK GOES HERE

libraryScore = computeLibraryScore(library, daysAvailable)


#writing the output file
o.write(answer)
f.close()
o.close()

