#!/usr/bin/python3

# Open the file and read the one line into an array.
fish = []
with open('/home/jake/Documents/AoC-2021/Day-6/input.txt') as inputFile:
    fish = inputFile.readline().strip('\n').split(',')
    fish = [ int(x) for x in fish ]

fishFrequency = []
for i in range(0, 9):
    fishFrequency.append(0)

for f in fish:
    fishFrequency[f]+=1

# Loop over the array decrementing and adding fish as required for 80 days.
days = 0
origFish = []
for num in fishFrequency:
    origFish.append(num)
while days < 256:
    for i in range(1,len(fishFrequency)):
            fishFrequency[i-1] = origFish[i]
    fishFrequency[6] += origFish[0]
    fishFrequency[8] = origFish[0]

    origFish=[]
    for num in fishFrequency:
        origFish.append(num)

    days+=1

totalFish = 0
for total in fishFrequency:
    totalFish += total

# Print the results.
print("Total fish afer " + str(days) + " days: " + str(totalFish))