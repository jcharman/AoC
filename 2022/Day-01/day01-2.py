#!/usr/bin/python3

total = 0
elves = []

with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        if line == '\n':
            elves.append(total)
            total = 0
        else:
            total += int(line)

topThree = 0
for i in range(3):
    topThree += max(elves)
    elves.remove(max(elves))

print(topThree)
