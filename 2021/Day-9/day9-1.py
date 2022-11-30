#!/usr/bin/python3

sumOfLowest = 0
map = []

def checkSurrounding(list, x, y):
    possibleX = [x, x-1, x+1]
    possibleY = [y, y-1, y+1]

    for newY in possibleY:
        if(newY < 0 or newY >= len(list)):
            continue
        for newX in possibleX:
            if(newX < 0 or newX >= len(list[0])):
                continue
            if(list[y][x] > list[newY][newX]):
                return False
    return True
        
with open('/home/jake/Documents/AoC-2021/Day-9/input.txt') as inputFile:
    for line in inputFile:
        lineList = list(line.strip('\n'))
        lineList = [int(x) for x in lineList]
        map.append(lineList)

for x in range(len(map[0])):
    for y in range(len(map)):
        if(checkSurrounding(map, x, y)):
            sumOfLowest += (map[y][x] + 1) 

print("Sum of risk levels is: " + str(sumOfLowest))