#!/usr/bin/python3

numbersDrawn = []
boards = []

# Function to check a given board for completed columns
def checkColumns(board):
    match = False
    for i in range(0,len(board[0])):
        for line in board:
            if(line[i] == '*'):
                match = True
                continue
            else:
                match = False
                break
        if(match):
            return True
        else:
            continue
    return False

# Function to check a given board for completed rows.
def checkRows(board):
    for line in board:
        match = False
        for num in line:
            if(num == '*'):
                match = True
                continue
            else:
                match = False
                break
        if(match):
            return True
        else:
            continue
    return False

# Open the file. Put the numbers to be drawn in one array and the boards in another.
with open('/home/jake/Documents/AoC-2021/Day-4/input.txt', 'r') as inputFile:
    numbersDrawn = inputFile.readline().split(',')
    boardsFromFile = inputFile.readlines()[1:]
    
    currentBoard = []
    for line in boardsFromFile:
        currentLine = []

        if(line == '\n'):
            boards.append(currentBoard)
            currentBoard = []
            continue
        
        currentLine = line.split()
        currentBoard.append(currentLine)
    boards.append(currentBoard)

# Mark off the numbers drawn on the boards.
for i in range(0, len(numbersDrawn)):
    for board in boards:
        for line in board:
            for num in range(len(line)):
                if(line[num] == numbersDrawn[i]):
                    line[num] = '*'

        # Check for a winning board
        if(checkRows(board) or checkColumns(board)):
            print("Found winning board: " + str(board))
            total = 0
            for line in board:
                for num in line:
                    if(num != '*'):
                        total = total+int(num)
            score = total * int(numbersDrawn[i])
            print("Total score of winning board is: " + str(score))
            exit()
        else:
            continue