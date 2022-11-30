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

# Run through the line segments and plot them on the diagram if they are horizontal or vertical.
for segment in segments:
    startingX = int(segment[0].split(',')[0])
    startingY = int(segment[0].split(',')[1])
    endingX = int(segment[1].split(',')[0])
    endingY = int(segment[1].split(',')[1])
    if((startingX == endingX) or (startingY == endingY)):
        endX = endingX +1
        startX = startingX
        endY = endingY +1
        startY = startingY

        # Flip the start and end if the end is lower so our for loop will still run.
        if(startingX > endingX):
            endX = startingX +1
            startX = endingX
        if(startingY > endingY):
            endY = startingY +1
            startY = endingY
        
        for x in range(startX, endX):
            for y in range(startY, endY):
                diagram[y][x]+=1
                 
# Find points where two or more line segments overlap.                
for line in diagram:
    for num in line:
        if(num > 1):
            totalPoints+=1

# Print the results
print("There are " + str(totalPoints) + " points where two or more lines overlap.")

