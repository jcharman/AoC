#!/usr/bin/python3

overlaps = 0

# For each line in the input file, construct a list of all sections to be cleaned.
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        instructions = line.strip().split(',')
        startStop = []
        for group in instructions:
            sublist = []
            sublist.append(int(group.split('-')[0]))
            sublist.append(int(group.split('-')[1]))
            startStop.append(sublist)

        groups = [list(range(startStop[0][0], startStop[0][1] + 1)), list(range(startStop[1][0], startStop[1][1] + 1))]

        # Check if the lists share any elements.
        if(len(set(groups[0]).intersection(set(groups[1]))) > 0):
            overlaps += 1

# Print the answer.
print(overlaps)
