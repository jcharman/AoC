#!/usr/bin/python3

# Define points values for each move and outcome.
points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'lose': 0,
    'draw': 3,
    'win': 6 
}

# Map letters to moves.
shapes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

# Define what move will win/lose for a given move.
wins = {
    'rock': ['paper', 'scissors'],
    'paper': ['scissors', 'rock'],
    'scissors': ['rock', 'paper']
}

# Map letters to the outcome they represent.
outcomes = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

# For each line in the input, work out what move we require and what our score would be.
totalScore = 0
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        moves = line.strip().split(' ')
        theirMove = shapes[moves[0]]
        requiredOutcome = outcomes[moves[1]]
        if requiredOutcome == 'win':
            requiredMove = wins[theirMove][0]
        elif requiredOutcome == 'lose':
            requiredMove = wins[theirMove][1]
        else:
            requiredMove = theirMove
        
        totalScore += (points[requiredOutcome] + points[requiredMove])

# Print the answer.
print(totalScore)
