#!/usr/bin/python3

# Variables to hold our totals.
gamma = ''
epsilon = ''

# Read in the input file. Split the file up into an array.
values = []
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        values.append(line.strip('\n'))

# Add up all the 1 values for each bit, then use the length of the array to calculate the most common bit.
for i in range(0, len(values[0])):
    currentBitCount = 0
    for value in values:
        currentBitCount = currentBitCount + int(value[i])
    
    if((len(values) - currentBitCount) < currentBitCount):
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    elif((len(values) - currentBitCount) > currentBitCount):
        gamma = gamma + '0'
        epsilon = epsilon + '1'

# Convert the binary strings to decimal ints.
gammaInt = int(gamma, 2)
epsilonInt = int(epsilon, 2)

# Print results.
print("Gamma is " + str(gamma) + " (" + str(gammaInt) + ")") 
print("Epsilon is " + str(epsilon) + " (" + str(epsilonInt) + ")") 
print("Gamma multiplied by Epsilon is: " + str(gammaInt * epsilonInt))