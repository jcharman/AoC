#!/usr/bin/python3

# Variables to hold our totals.
keptNumbers = []
co2 = 0
o2 = 0

# Read in the input file. Split the file up into an array.
rawValues = []
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        rawValues.append(line.strip('\n'))

# Loop through twice, collecting the opposite set of results each time.
for i in range(0,2):
    values = rawValues
    mostPopular=0

    # Determine the most popular bit.
    for bit in range(0, len(values[0])):
        currentBitCount = 0
        for value in values:
            currentBitCount = currentBitCount + int(value[bit])
        
        # Keep values which contain the most popular bit.
        if((len(values) - currentBitCount) < currentBitCount):
            mostPopular = 1
            for value in values:
                if(value[bit] == str(mostPopular) and i == 1):
                    keptNumbers.append(value)
                elif(value[bit] != str(mostPopular) and i == 0):
                    keptNumbers.append(value)

        elif((len(values) - currentBitCount) > currentBitCount):
            mostPopular = 0
            for value in values:
                if(value[bit] == str(mostPopular) and i == 1):
                    keptNumbers.append(value)
                elif(value[bit] != str(mostPopular) and i == 0):
                    keptNumbers.append(value)

        elif((len(values) - currentBitCount) == currentBitCount):
            for value in values:
                if(value[bit] == str(i)):
                    keptNumbers.append(value)

        values = keptNumbers
        keptNumbers = []

        # Break if we only have one value left.
        if(len(values) == 1):
            break

    # Put the value in the right variable.
    if(i == 0):
        co2 = values[0]
    elif(i == 1):
        o2 = values[0]

# Convert the binary numbers to ints.
o2Int = int(o2, 2)
co2Int = int(co2, 2)

# Print results.
print("O2 Generator reading is " + str(o2) + " (" + str(o2Int) + ")")
print("CO2 Scrubber reading is " + str(co2) + " (" + str(co2Int) + ")")
print("The readings multipied together is " + str(o2Int * co2Int))