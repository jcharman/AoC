#!/usr/bin/python3

finalTotal = 0

# Function to find and return common chars in a string.
def findCommon(s1, s2):
    common = ""
    for i in s1:
        if(i in s2):
            common += i
    return common

# Read in the input file. Put the signals and outputs in two 
with open('/home/jake/Documents/AoC-2021/Day-8/input.txt') as inputFile:
    for line in inputFile:
        newNums = ['0','0','0','0','0','0','0','0','0','0']
        out = ""
        signals = line.strip('\n').split('|')[0].split()
        output = line.strip('\n').split('|')[1].split()

        for signal in signals:
            if(len(signal) == 2):
                newNums[1] = "".join(sorted(signal)) 
            elif(len(signal) == 3):
                newNums[7] = "".join(sorted(signal)) 
            elif(len(signal) == 4):
                newNums[4] = "".join(sorted(signal)) 
            elif(len(signal) == 7):
                newNums[8] = "".join(sorted(signal)) 
            else:
                continue

        for signal in signals:
            sortedSignal = "".join(sorted(signal))
            if(sortedSignal in newNums):
                continue
            
            if(len(signal) == 5):
                # Check for 2.
                if(len(findCommon(signal, newNums[4])) == 2 and len(findCommon(signal, newNums[1])) == 1 and len(findCommon(signal, newNums[7])) == 2):
                    newNums[2] = "".join(sorted(signal))
                # Check for 3.
                elif(len(findCommon(signal, newNums[7])) == 3 and len(findCommon(signal, newNums[1])) == 2):
                    newNums[3] = "".join(sorted(signal))
                # Check for 5.
                elif(len(findCommon(signal, newNums[4])) == 3 and len(findCommon(signal, newNums[1])) == 1):
                    newNums[5] = "".join(sorted(signal))
            elif(len(signal) == 6):
                # Check for 6.
                if(len(findCommon(signal, newNums[1])) == 1 and len(findCommon(signal, newNums[8])) == 6 and len(findCommon(signal, newNums[4])) == 3):
                    newNums[6] = "".join(sorted(signal))
                # Check for 9.
                elif(len(findCommon(signal, newNums[7])) == 3 and len(findCommon(signal, newNums[4])) == 4):
                    newNums[9] = "".join(sorted(signal))
                # Check for 0.
                elif(len(findCommon(signal, newNums[4])) == 3 and len(findCommon(signal, newNums[8])) == 6 and len(findCommon(signal, newNums[1])) == 2):
                    newNums[0] = "".join(sorted(signal))
        
        for num in output:
            sortedNum = "".join(sorted(num))
            displayedNum = newNums.index(sortedNum)
            out = str(out) + str(displayedNum)
        finalTotal += int(out)
        print(finalTotal)