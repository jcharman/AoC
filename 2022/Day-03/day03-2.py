#!/usr/bin/python3

from string import ascii_lowercase, ascii_uppercase

commonItems = []
backpacks = []

with open('input.txt', 'r') as inputFile:
    backpacks = inputFile.readlines()

currentBackpack = 0

while(currentBackpack < len(backpacks)):
    currentGroup = []
    while(len(currentGroup) < 3):
        currentGroup.append(backpacks[currentBackpack].strip())
        currentBackpack += 1
    for item in currentGroup[0]:
        if(item in currentGroup[1] and item in currentGroup[2]):
            commonItems.append(item)
            break

totalPriority = 0

for item in commonItems:
    if(item in ascii_lowercase):
        totalPriority += (ascii_lowercase.index(item) + 1)
    elif(item in ascii_uppercase):
        totalPriority += (ascii_uppercase.index(item) + 27)

print(totalPriority)
