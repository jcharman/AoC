#!/usr/bin/python3

import re
from math import prod

if __name__ == '__main__':
    with open('input.txt', 'r' ) as input_file:
        input = input_file.read()

    res = 0
    en = True
    for cmd in re.findall(r"(do\(\)|don\'t\(\)|mul\(\d+,\d+\))", input, flags=re.MULTILINE):
        if cmd == 'do()':
            en = True
            continue
        if cmd =='don\'t()':
            en = False
            continue
        if en:
            digits = [int(y) for y in ''.join([x for x in cmd if x.isdigit() or x == ',']).split(',')]
            res += prod(digits)
    print(res)
