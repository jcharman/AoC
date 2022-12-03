#!/usr/bin/python3

# Import lists of the alphabet so we can find indxes later.
from string import ascii_lowercase, ascii_uppercase

commonItems = []

# For each backpack, split the contents into two lists and find the common item.
with open('input.txt', 'r') as inputFile:
    for backpack in inputFile:
        items = [*backpack.strip()]
        comp1 = []
        comp2 = []
        for item in range(int(len(items) / 2)):
            comp1.append(items[item])
        for item in range(int(len(items) / 2), int(len(items))):
            comp2.append(items[item])

        for item in comp1:
            if(item in comp2):
                commonItems.append(item)
                break

# For all of the common items we found, total up the priorities.
totalPriority = 0
for item in commonItems:
    if(item in ascii_lowercase):
        totalPriority += (ascii_lowercase.index(item) + 1)
    elif(item in ascii_uppercase):
        totalPriority += (ascii_uppercase.index(item) + 27)

# Print the answer.
print(totalPriority)