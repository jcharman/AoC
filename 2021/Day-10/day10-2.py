#!/usr/bin/python3

from statistics import median

lineScores = []

closers = {
    '(':')',
    '{':'}',
    '[':']',
    '<':'>'
}

points = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

with open('/home/jake/Documents/AoC-2021/Day-10/input.txt') as inputFile:
    for line in inputFile:
        line = line.strip('\n')
        expecting = []
        invalid = False
        for char in line:
            if(char in closers):
                expecting.insert(0,closers[char])
            else:
                if(expecting[0] != char):
                    invalid = True
                    break
                else:
                    del expecting[0]
        if(invalid):
            continue
        else:
            totalScore = 0
            for e in expecting:
                totalScore*=5
                totalScore+=points[e]
            lineScores.append(totalScore)
print("The middle score is: " + str(median(lineScores)))