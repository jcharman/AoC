#!/usr/bin/python3

points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'lose': 0,
    'draw': 3,
    'win': 6 
}

shapes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

wins = {
    'rock': ['paper', 'scissors'],
    'paper': ['scissors', 'rock'],
    'scissors': ['rock', 'paper']
}


outcomes = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

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


print(totalScore)
