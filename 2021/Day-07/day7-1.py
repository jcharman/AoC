#!/usr/bin/python3

# Read in the file and split it into an array.
crabPositions = []
with open('/home/jake/Documents/AoC-2021/Day-7/input.txt') as inputFile:
    crabPositions = inputFile.readline().strip('\n').split(',')
    crabPositions = [ int(x) for x in crabPositions]

possiblePositions = list(range(min(crabPositions), max(crabPositions)))
fuelForPositions = []

# Calculate the lowest possible fuel usage.
for i in possiblePositions:
    fuelUsed = 0
    for crab in crabPositions:
        fuelUsed += abs(crab - i)
    fuelForPositions.append(fuelUsed)

# Print the results.
print("Lowest possible fuel usage is " + str(min(fuelForPositions)) + " by moving to position " + str(possiblePositions[fuelForPositions.index(min(fuelForPositions))]))