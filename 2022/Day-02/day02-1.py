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
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

# Calculate whether we won or lost for a given pair of moves.
def outcome(myMove, yourMove):
    wins = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    if myMove == yourMove:
        return 'draw'
    elif theirMove == wins[myMove]:
        return 'win'
    else:
        return 'lose'

# For each set of moves in the input, work out our total score.
totalScore = 0
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        moves = line.strip().split(' ')
        ourMove = shapes[moves[1]]
        theirMove = shapes[moves[0]]
        totalScore += points[ourMove]
        totalScore += points[outcome(ourMove, theirMove)]

# Print the answer.
print(totalScore)
