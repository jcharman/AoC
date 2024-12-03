#!/usr/bin/python3

import re
from math import prod

if __name__ == '__main__':
    with open('input.txt', 'r' ) as input_file:
        input = input_file.read()

    res = 0
    for cmd in re.findall(r"mul\(\d+,\d+\)", input, flags=re.MULTILINE):
        digits = [int(y) for y in ''.join([x for x in cmd if x.isdigit() or x == ',']).split(',')]
        res += prod(digits)
    print(res)
