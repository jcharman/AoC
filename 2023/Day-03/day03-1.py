#!/usr/bin/python3

import re

def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
        lines = [line.strip() for line in lines]
    
    part_numbers = []

    for y in range(len(lines)):
        for digit in re.finditer(r'\d+', lines[y]):
            part_number = 0
            if(lines[y][digit.span()[0] - 1] != '.' 
               and not lines[y][digit.span()[0] - 1].isdigit()):
                part_number = digit.group()
                part_numbers.append(int(part_number))
                continue
            try:
                if(lines[y][digit.span()[1]] != '.' 
                and not lines[y][digit.span()[1]].isdigit()):
                    part_number = digit.group()
                    part_numbers.append(int(part_number))
                    continue
            except:
                pass
            for char in range(digit.span()[0] - 1, digit.span()[1] + 1):
                try:
                    if lines[y-1][char] != '.' and not lines[y-1][char].isdigit():
                        part_number = digit.group()
                        part_numbers.append(int(part_number))
                        continue
                except:
                    pass
                try:
                    if lines[y+1][char] != '.' and not lines[y+1][char].isdigit():
                        part_number = digit.group()
                        part_numbers.append(int(part_number))
                        continue
                except:
                    pass

    print(sum(part_numbers))

if __name__ == '__main__':
    main()
