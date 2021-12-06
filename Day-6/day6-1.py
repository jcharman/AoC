#!/usr/bin/python3

# Open the file and read the one line into an array.
fish = []
with open('/home/jake/Documents/AoC-2021/Day-6/input.txt') as inputFile:
    fish = inputFile.readline().strip('\n').split(',')
    fish = [ int(x) for x in fish ]

# Loop over the array decrementing and adding fish as required for 80 days.
days = 0
while days < 80:
    for i in range(0, len(fish)):
        if(fish[i] == 0):
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] = fish[i] -1
    days+=1

# Print the results.
print("Total fish afer " + str(days) + " days: " + str(len(fish)))