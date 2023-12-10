#!/usr/bin/python3

from math import prod

def main():
    times = []
    distances = []
    records = {}

    with open('input.txt', 'r') as input_file:
        for line in input_file:
            if line.startswith('Time:'):
                times = line.split(':')[1].split()
            elif line.startswith('Distance:'):
                distances = line.split(':')[1].split()
    
    for time in times:
        records[int(time)] = int(distances[times.index(time)])

    num_winners = []
    for total_time in records:
        winners = []
        for time_pressed in range(total_time + 1):
            distance_traveled = time_pressed * (total_time - time_pressed)
            if distance_traveled > records[total_time]:
                winners.append(time_pressed)
        num_winners.append(len(winners))

    print(prod(num_winners))

if __name__ == '__main__':
    main()
