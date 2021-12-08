#!/usr/bin/python3

totalUnique = 0

# Read in the input file.
with open('/home/jake/Documents/AoC-2021/Day-8/input.txt') as inputFile:
    for line in inputFile:
        for output in line.strip('\n').split('|')[1].split():
            if(len(output) in [2,3,4,7]):
                totalUnique += 1

print(totalUnique)