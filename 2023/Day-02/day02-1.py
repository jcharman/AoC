#!/usr/bin/python3

def main():
    allowed_totals = {
        'red': 12,
        'green': 13,
        'blue':14,
    }

    possible_games = []

    with open('input.txt', 'r') as input_file:
        for line in input_file:
            possible = True
            line = line.strip()
            game_num = int(line.split(':')[0].split(' ')[1])
            game_res = [result.split(',') for result in line.split(':')[1].split(';')]

            for result in game_res:
                for colour in result:
                    num_colour = int(colour.strip().split(' ')[0])
                    colour_name = colour.strip().split(' ', 1)[1]

                    if num_colour > allowed_totals[colour_name]:
                        possible = False

            if possible:
                possible_games.append(game_num)
        print(sum(possible_games))

if __name__ == '__main__':
    main()
