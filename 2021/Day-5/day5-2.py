#!/usr/bin/python3

diagram = []
totalPoints = 0

# Read all the line segments into an array.
segments = []
with open('/home/jake/Documents/AoC-2021/Day-5/input.txt') as inputFile:
    for line in inputFile:
        segment = line.strip('\n').split(' -> ')
        segments.append(segment)

# Work out the bounds of our diagram and create an array for it.
largestX = 0
largestY = 0
for segment in segments:
    if(int(segment[0].split(',')[0]) > largestX):
        largestX = int(segment[0].split(',')[0])
    
    if(int(segment[1].split(',')[0]) > largestX):
        largestX = int(segment[1].split(',')[0])

    if(int(segment[0].split(',')[1]) > largestY):
        largestY = int(segment[0].split(',')[1])
    
    if(int(segment[1].split(',')[1]) > largestX):
        largestY = int(segment[1].split(',')[1])

for i in range(0, largestY+1):
    diagLine = []
    for i in range(0,largestX+1):
        diagLine.append(0)
    diagram.append(diagLine)

# Run through the line segments and plot them on the diagram.
for segment in segments:
    startingX = int(segment[0].split(',')[0])
    startingY = int(segment[0].split(',')[1])
    endingX = int(segment[1].split(',')[0])
    endingY = int(segment[1].split(',')[1])

    # Create lists for the X and Y points our lines will go through.
    if(startingX > endingX):
        xStep = -1
        endingX-=1
    else:
        xStep = 1
        endingX+=1
    if(startingY > endingY):
        yStep = -1
        endingY-=1
    else:
        yStep=1
        endingY+=1

    xList = list(range(startingX, endingX, xStep))
    yList = list(range(startingY, endingY, yStep))

    # If the line is horizontal or vertical there will be differing numbers of indexes so we need to loop though them separately.
    if(len(xList) != len(yList)):
        for x in xList:
            for y in yList:
                diagram[y][x]+=1
    # Otherwise they will be identical and we need to increment both lists together.
    else:
        for i in range(0, len(xList)):
            currentX = xList[i]
            currentY = yList[i]
            diagram[currentY][currentX]+=1

# Find points where two or more line segments overlap.                
for line in diagram:
    for num in line:
        if(num > 1):
            totalPoints+=1

# Print the results.
print("There are " + str(totalPoints) + " points where two or more lines overlap.")

