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

print(max(elves))
