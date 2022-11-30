#!/usr/bin/python3

totalScore = 0

closers = {
    '(':')',
    '{':'}',
    '[':']',
    '<':'>'
}

points = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

with open('/home/jake/Documents/AoC-2021/Day-10/input.txt') as inputFile:
    for line in inputFile:
        line = line.strip('\n')
        i = 0
        expecting = []
        i = 0
        for char in line:
            if(char in closers):
                expecting.insert(0,closers[char])
            else:
                if(expecting[i] != char):
                    totalScore += points[char]
                    break
                else:
                    del expecting[i]
print("Our total score was: " + str(totalScore))