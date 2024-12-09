#!/usr/bin/python3

def look_around(coords: tuple, direction: tuple):
    global found
    letters = ['X','M','A','S']
    orig_x = coords[0]
    orig_y = coords[1]
    x_to_check = direction[0]
    y_to_check = direction[1]

    try:
        next_letter = letters[letters.index(wordsearch[orig_y][orig_x]) + 1]
    except IndexError:
        found += 1
        return
    for diff_x in x_to_check:
        for diff_y in y_to_check:
            x = orig_x + diff_x
            y = orig_y + diff_y 
            if x < 0 or y < 0:
                continue
            try:
                if wordsearch[y][x] == next_letter:
                    look_around((x, y), ([diff_x], [diff_y]))
            except IndexError:
                pass

if __name__ == '__main__':
    found = 0
    with open('input.txt', 'r') as input_file:
        wordsearch = [list(x.strip()) for x in input_file.readlines()]

    for y in range(len(wordsearch)):
        for x in range(len(wordsearch[y])):
            if wordsearch[y][x] != 'X':
                continue
            res = look_around((x,y), ([-1,0,1],[-1,0,1]))
            if res:
                found += 1
    print(found)
