#!/usr/bin/python3

from math import prod

def main():
    total = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:

            total_colours = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }

            line = line.strip()
            game_res = [result.split(',') for result in line.split(':')[1].split(';')]

            for result in game_res:
                for colour in result:
                    num_colour = int(colour.strip().split(' ')[0])
                    colour_name = colour.strip().split(' ', 1)[1]

                    if num_colour > total_colours[colour_name]:
                        total_colours[colour_name] = num_colour

            total += prod(total_colours.values())
        print(total)

if __name__ == '__main__':
    main()
