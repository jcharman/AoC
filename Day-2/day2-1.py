#!/usr/bin/python3

# Variables to hold our position.
x = 0
z = 0

# Read in the input file. Split each line on the space.
with open('input.txt', 'r') as inputFile:
    values = []
    for line in inputFile:
        splitLine = line.split()

        # Check the first word of each line to decide what to do.
        if splitLine[0] == "forward":
            x = x + int(splitLine[1])
        elif splitLine [0] == "down":
            z = z + int(splitLine[1])
        elif splitLine [0] == "up":
            z = z - int(splitLine[1])

# Print our final values.
print("X: " + str(x))
print("Z: " + str(z))
print("X * Z = " + str(x*z))