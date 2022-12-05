#!/usr/bin/python

stackIndex = []
numStacks = 0
instructions = []

# Move a given number of itmes from the top of one stack to the top of another.
def moveItems(num, fromStack, toStack):
    stacks[fromStack - 1].reverse()

    numMoved = 0
    while numMoved < num:
        stacks[toStack - 1].append(stacks[fromStack - 1][(num - 1) - numMoved])
        del stacks[fromStack - 1][(num - 1) - numMoved]
        numMoved += 1
    
    stacks[fromStack - 1].reverse()

# Find the line containing the stack definitions and store it as a list.
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        if(line[1].isdigit()):
            stackIndex = list(line.strip('\n'))
            numStacks = len(line.strip().replace(' ', ''))
            break

# Now use the indexes of those definitions to build lists for each stack.
with open('input.txt', 'r') as inputFile:
    rawStacks = []
    for i in range(len(stackIndex)):
        rawStacks.append([])

    for line in inputFile:
        if('[' not in line[0]):
            break
        for i in range(len(stackIndex)):
            if(stackIndex[i].isdigit() and line[i] != ' '):
                rawStacks[i].append(line[i])

    # Ditch any empty lists.
    stacks = []
    for stack in rawStacks:
        if(stack != []):
            stack.reverse()
            stacks.append(stack)
    
    # Clean up the instructions and put them in lists we can use.
    rawInstructions = []
    for line in inputFile:
        thisLine = (line.strip().replace('move','').replace('from','').replace('to','').split(' '))
        cleanLine = []
        for i in thisLine:
            if(i != ''):
                cleanLine.append(i)
        instructions.append(cleanLine)

    # Run through the instructions and call the move() function.
    for i in instructions:
        try:
            numToMove = int(i[0])
            fromStack = int(i[1])
            toStack = int(i[2])
            moveItems(numToMove, fromStack, toStack)
        except IndexError:
            pass

# Print the answer.
finalItems = []
for stack in stacks:
    stack.reverse()
    print(stack[0], end='')
print('\n', end='')
