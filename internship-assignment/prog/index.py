# Unknown
# 1. read file input
# 2. Get Matrix width and height
# 3. Create empty Matrix
# 4. Assign test data to the Matrix
# 5. Find paths
#   - path finding logic

#   - result counter
#   - create aoutput

# Read text files input
fileNamesStr = raw_input()
fileNamesArr = str.split(' ')

w, h = None, None
Matrix = [[0 for x in range(w)] for y in range(h)]

# Read file input
def readFile( fileName ):
    ObjRead = open(fileName, "r")
    lines = ObjRead.readlines()
    matrixSizes = lines[0].split(' ')
    w = matrixSizes[0]
    h = matrixSizes[1]
    lines.pop(0)
    for line in lines
        characters = line.split(' ')
        Matrix[0] = characters

for fileName in fileNamesArr
    readFile(fileName)


# print(Matrix)

Matrix = [
    ['R','R','B']
    ['G','G','R']
    ['R','B','G']
]


def findNextStep()
# Check for all available directions
# if X go to next
# if same

def updateCounter(point)
# Finds character on given point
# and add 1 to the counter

def findNextStartPoint()
# Loops through next points
# IF find element which is not X
#   sets currentStartPoint to it
#   and runs findPath
# IF goes to the last element and
# do not find not X element finishes
# the proggram

def finishProggram()
# Finds the max num through conterR/G or
# B and returns the value

currentStartPoint = [0,0]
currentPoint = [0,0]
matrixAllElementsCount = h * w
countedPoints = 0
conterR = 0
conterG = 0
conterB = 0

findPath()
    if countedPoints >= matrixAllElementsCount
        finishProggram()
    updateCounter(currentPoint)
    countedPoints += 1
    Matrix[currentPoint[0]][currentPoint[0]] = 'X'
    nextStep = findNextStep(x,y,rows)
    if nextStep != None
        Matrix[nextStep[0]][nextStep[0]] = 'X'
        currentPoint =[nextStep[0], [nextStep[0]]
        updateCounter(nextStep)
        countedPoints += 1
        findPath()
    else
        nextStartPoint = findNextStartPoint()
        if nextStartPoint != None
            currentPoint = [nextStartPoint[0], nextStartPoint[1]]
            currentStartPoint = [nextStartPoint[0], nextStartPoint[1]]
            findPath()
        else
            finishProggram()
