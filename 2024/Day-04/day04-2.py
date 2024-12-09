#!/usr/bin/python3

def look_around(coords: tuple, direction: tuple):
    letters = ['M','S']
    orig_x = coords[0]
    orig_y = coords[1]
    x_to_check = direction[0]
    y_to_check = direction[1]
    letters_found = {}
    for diff_x in x_to_check:
        for diff_y in y_to_check:
            x = orig_x + diff_x
            letters_found[x] = letters_found.get(x, [])
            y = orig_y + diff_y
            if x < 0 or y < 0:
                continue
            try:
                if wordsearch[y][x] in letters:
                    letters_found[x].append(wordsearch[y][x])
            except IndexError:
                pass

    letters_found = list(letters_found.values())
    success = 0
    if any([len(x) < 2 for x in letters_found]):
        return False
    match letters_found[0][0]:
        case 'M':
            if letters_found[1][1] == 'S':
                success += 1
        case 'S':
            if letters_found[1][1] == 'M':
                success += 1
    match letters_found[0][1]:
        case 'M':
            if letters_found[1][0] == 'S':
                success += 1
        case 'S':
            if letters_found[1][0] == 'M':
                success += 1
    if success == 2:
        return True
    return False

if __name__ == '__main__':
    found = 0
    with open('input.txt', 'r') as input_file:
        wordsearch = [list(x.strip()) for x in input_file.readlines()]

    for y in range(len(wordsearch)):
        for x in range(len(wordsearch[y])):
            if wordsearch[y][x] != 'A':
                continue
            if look_around((x,y), ([-1,1],[-1,1])):
                found += 1
    print(found)
