#!/usr/bin/python3

total = 0
elves = []

# Add each line of the input, when we hit a blank line put the current total in a list.
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        if line == '\n':
            elves.append(total)
            total = 0
        else:
            total += int(line)

# Find the total of the largest three items in the list.
topThree = 0
for i in range(3):
    topThree += max(elves)
    elves.remove(max(elves))

# Print the answer.
print(topThree)
