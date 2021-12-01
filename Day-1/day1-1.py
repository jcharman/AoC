#!/usr/bin/python3

# Variables to hold our totals.
increased = 0
decreased = 0

# Read in the input file and make it an array.
with open('input.txt', 'r') as inputFile:
    values = []
    for line in inputFile:
        values.append(int(line))

# Loop through the array skipping the first value.
for v in range(0, len(values)):
    if(v == 0):
        continue
    
    # Check each value against the one before it.
    if(values[v - 1] < values[v]):
        increased+=1
    elif(values[v - 1] > values[v]):
        decreased+=1
    else:
        pass

# Print the output.
print("Decreased: " + str(decreased))
print("Increased: " + str(increased))